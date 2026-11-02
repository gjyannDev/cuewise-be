import logging
import random
import time
import uuid
from collections.abc import AsyncGenerator, Callable, Sequence
from contextlib import aclosing
from typing import NamedTuple

import anyio
from pydantic import BaseModel

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMError, LLMProvider, LLMResult
from app.core.ai.tracing import Tracer
from app.core.errors import (
    NotFoundError,
    QuestionNotCurrentError,
    SessionNotInProgressError,
)
from app.core.logging import request_id_ctx
from app.modules.auth.auth_model import User

from .interviews_constants import (
    FIRST_POSITION,
    SUMMARY_TASK,
    SUMMARY_THRESHOLD,
    SUMMARY_TIME_CAP_SECONDS,
    InterviewType,
    JobRole,
    Level,
    MessageRole,
    QuestionCategory,
    QuestionKind,
    QuestionSource,
    SessionStatus,
    StreamEvent,
    TurnPhase,
)
from .interviews_context import CONTEXT_MANAGER, InterviewerInputs, SummaryInputs
from .interviews_model import InterviewMessage, InterviewQuestion, InterviewSession
from .interviews_reply import InvalidReplyError, validate_summary
from .interviews_repository import InterviewsRepository
from .interviews_schema import (
    AnswerIn,
    AnswerOut,
    BankQuestion,
    InterviewCreateIn,
    InterviewOut,
    QuestionDeltaOut,
    QuestionOut,
    ReactionOut,
    ResetOut,
    SessionOut,
    StatusEventOut,
    StreamErrorOut,
    StreamEventOut,
    TranscriptOut,
)
from .interviews_turn import (
    ActionKnown,
    Delta,
    Interviewer,
    PhaseChanged,
    Reset,
    Settled,
    TurnAction,
    TurnOutcome,
    Written,
    log_llm_call,
    log_result,
    log_stream_summary,
    log_turn_summary,
    sum_known,
)
from .interviews_utils import (
    QuestionTurn,
    build_transcript,
    interviewer_history,
    pick_fallback_question,
    pick_reaction,
    select_questions,
)

# Streamed turns that fail after their stream opened: the client gets a generic `error` event, the details land here.
stream_logger = logging.getLogger("app.errors")


class InterviewSetup(NamedTuple):
    """The session fields the interviewer needs, as plain values that survive the end of a transaction."""

    session_id: uuid.UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    job_description: str | None
    # Sent instead of job_description when present (made once at start for long descriptions).
    job_description_summary: str | None = None


class Thread(NamedTuple):
    """The main question the answered question belongs to (itself, or a follow-up's parent), as plain values."""

    main_id: uuid.UUID
    main_number: int
    category: QuestionCategory


class TurnContext(NamedTuple):
    """Everything an answer turn needs, read before its LLM calls (the read transaction has ended by then)."""

    # Only used to build the response after the save (its fields reload then).
    session: InterviewSession
    setup: InterviewSetup
    position: int
    question_id: uuid.UUID
    history: list[QuestionTurn]
    thread: Thread
    last_main: bool
    used_bank_ids: set[str]
    stored_next: InterviewQuestion | None
    previous_reaction: str | None
    # The candidate's answer, saved with the rest of the turn (its note is filled in by the decide call).
    answer: InterviewMessage
    # For the request's trace; read here because `session` reloads from the DB once its transaction has ended.
    user_id: uuid.UUID


class InterviewsController:
    def __init__(
        self,
        repo: InterviewsRepository,
        bank: list[BankQuestion],
        rng: random.Random,
        llm: LLMProvider | None = None,
        llm_max_tokens: int = 800,
        *,
        llm_budget_seconds: float = 30,
        clock: Callable[[], float] = time.monotonic,
        context: ContextManager = CONTEXT_MANAGER,
        tracer: Tracer | None = None,
    ):
        self.repo = repo
        self.bank = bank
        self.rng = rng
        # None = LLM off: every question comes from the bank.
        self.llm = llm
        # Langfuse traces (one per request that can call the LLM); a disabled tracer costs nothing.
        self.tracer = tracer or Tracer(None)
        self.llm_max_tokens = llm_max_tokens
        # Decides what each LLM call sends (strategy, trimming); see interviews_context.py.
        self.context = context
        # Decide, limits, write: one answer turn of the LLM interviewer (interviews_turn.py).
        self.interviewer = (
            None
            if llm is None
            else Interviewer(
                llm, context, max_tokens=llm_max_tokens, budget_seconds=llm_budget_seconds, clock=clock
            )
        )

    def start(self, user: User, data: InterviewCreateIn) -> InterviewOut:
        # The bank must be able to back every position (the fallback), and a refused setup costs no LLM call.
        select_questions(
            self.bank,
            data.role,
            data.level,
            data.interview_type,
            data.question_count,
            self.rng,
        )
        session = InterviewSession(
            id=uuid.uuid7(), user_id=user.id, **data.model_dump()
        )
        setup = InterviewSetup(
            session.id,
            data.role,
            data.level,
            data.interview_type,
            data.question_count,
            data.job_description,
        )
        trace = self.tracer.trace(
            "start-interview", user_id=str(user.id), session_id=str(session.id), input=data.model_dump(mode="json")
        )
        with trace:
            self.repo.release()
            summary = self._summarize(setup)
            if summary is not None:
                session.job_description_summary = summary
                setup = setup._replace(job_description_summary=summary)
            first = None
            if self.interviewer is not None:
                written = self.interviewer.first_question(setup.session_id, self._inputs(setup, []))
                if written.reply is not None:
                    first = _llm_question(written, written.results, FIRST_POSITION, 1)
            if first is None:
                first = self._bank_question(setup, FIRST_POSITION, 1, set())
            self.repo.start(session, [first])
            return InterviewOut(
                session=SessionOut.model_validate(session),
                current_question=QuestionOut.model_validate(first),
            )

    def get(self, user: User, session_id: uuid.UUID) -> InterviewOut:
        session = self._owned_session(user, session_id)
        return InterviewOut(
            session=SessionOut.model_validate(session),
            current_question=self._question_out(self._current_question(session)),
        )

    def answer(self, user: User, session_id: uuid.UUID, data: AnswerIn) -> AnswerOut:
        ctx = self.prepare_answer(user, session_id, data)
        outcome = None
        with self._answer_trace(ctx):
            if self.uses_interviewer(ctx):
                assert self.interviewer is not None
                outcome = self.interviewer.answer_turn(
                    ctx.setup.session_id, self.turn_inputs(ctx), last_main=ctx.last_main
                )
        return self.finish_answer(ctx, outcome)

    def _answer_trace(self, ctx: TurnContext):
        return self.tracer.trace(
            "answer-turn",
            user_id=str(ctx.user_id),
            session_id=str(ctx.setup.session_id),
            input={"question_id": str(ctx.question_id), "answer": ctx.answer.content},
        )

    def prepare_answer(self, user: User, session_id: uuid.UUID, data: AnswerIn) -> TurnContext:
        """Every check and read of an answer turn, before any LLM call. Raises the usual errors (404, 409), so a
        streamed turn fails as plain HTTP before its stream opens. The read transaction is released on return."""
        session = self._owned_session(user, session_id)
        if session.status != SessionStatus.in_progress:
            raise SessionNotInProgressError("This interview is not in progress")
        position = session.current_position
        question = self.repo.get_question(session.id, position)
        # One response for every mismatch (stale, future, foreign, random id), so ids can't be probed.
        if question is None or question.id != data.question_id:
            raise QuestionNotCurrentError(
                "This is not the current question of the interview"
            )

        # Read everything as plain values first: the read transaction ends before the (slow) LLM calls, and after
        # that every loaded ORM object is expired.
        setup = InterviewSetup(
            session.id,
            JobRole(session.role),
            Level(session.level),
            InterviewType(session.interview_type),
            session.question_count,
            session.job_description,
            session.job_description_summary,
        )
        asked = self.repo.list_questions(session.id, position)
        saved = self.repo.list_messages(session.id)
        history = [
            *interviewer_history(asked[:-1], saved),
            QuestionTurn(question.text, question.category, data.answer, kind=question.kind),
        ]
        main = (
            question
            if question.kind == QuestionKind.main
            else next(q for q in asked if q.id == question.parent_question_id)
        )
        thread = Thread(main.id, main.main_number, QuestionCategory(main.category))
        ctx = TurnContext(
            session=session,
            setup=setup,
            position=position,
            question_id=question.id,
            history=history,
            thread=thread,
            last_main=thread.main_number == setup.question_count,
            used_bank_ids={q.bank_id for q in asked if q.bank_id},
            # Pre-slice-2 sessions stored every question up front: no LLM, no follow-ups, the stored order.
            stored_next=self.repo.get_question(session.id, position + 1),
            previous_reaction=next(
                (m.content for m in reversed(saved) if m.role == MessageRole.interviewer),
                None,
            ),
            answer=InterviewMessage(
                session_id=session.id,
                question_id=question.id,
                role=MessageRole.candidate,
                content=data.answer,
            ),
            user_id=user.id,
        )
        self.repo.release()
        return ctx

    def uses_interviewer(self, ctx: TurnContext) -> bool:
        """False when the LLM is off or the session's questions were all stored up front: no decide, no write."""
        return self.interviewer is not None and ctx.stored_next is None

    def turn_inputs(self, ctx: TurnContext) -> InterviewerInputs:
        return self._inputs(ctx.setup, ctx.history)

    def completes_without_llm(self, ctx: TurnContext) -> bool:
        """For a turn that doesn't use the interviewer: a stored next question never completes; otherwise the last
        main question does."""
        return ctx.stored_next is None and ctx.last_main

    def choose_reaction(self, ctx: TurnContext, *, completes: bool) -> ReactionOut:
        """The predefined acknowledgement for moving on (or completing). The id is set here, so it is the same in
        an early `reaction` event and in the saved row, and the response needs no read of the committed row."""
        text = pick_reaction(
            ctx.thread.category,
            ctx.setup.level,
            final=completes,
            previous=ctx.previous_reaction,
            rng=self.rng,
        )
        return ReactionOut(id=uuid.uuid7(), text=text)

    def finish_answer(
        self, ctx: TurnContext, outcome: TurnOutcome | None, reaction: ReactionOut | None = None
    ) -> AnswerOut:
        """Turn the outcome into rows and save the whole turn in one commit. `reaction` is one already picked (and
        shown) by a streamed turn; otherwise it is picked here. Raises QuestionNotCurrentError on a lost race."""
        setup, thread, position = ctx.setup, ctx.thread, ctx.position
        answer = ctx.answer
        new_question: InterviewQuestion | None = None
        if ctx.stored_next is not None:
            completes = False
            log_turn_summary(setup.session_id, decision="skipped", action=TurnAction.next_question, source="stored")
        elif outcome is None:
            completes = ctx.last_main
            if not completes:
                new_question = self._bank_question(setup, position + 1, thread.main_number + 1, ctx.used_bank_ids)
            log_turn_summary(
                setup.session_id,
                decision="skipped",
                action=TurnAction.complete if completes else TurnAction.next_question,
                source="-" if completes else "bank",
            )
        else:
            answer.note = outcome.note
            completes = outcome.action == TurnAction.complete
            if outcome.action == TurnAction.follow_up and outcome.written is not None:
                new_question = _llm_question(
                    outcome.written,
                    outcome.results,
                    position + 1,
                    thread.main_number,
                    kind=QuestionKind.follow_up,
                    thread=thread,
                    decision_version=outcome.decision_prompt_version,
                )
            elif outcome.action == TurnAction.next_question and outcome.written is not None:
                new_question = _llm_question(
                    outcome.written,
                    outcome.results,
                    position + 1,
                    thread.main_number + 1,
                    decision_version=outcome.decision_prompt_version,
                )
            elif outcome.action == TurnAction.next_question:
                new_question = self._bank_question(setup, position + 1, thread.main_number + 1, ctx.used_bank_ids)

        follows_up = new_question is not None and new_question.kind == QuestionKind.follow_up
        # A follow-up comes straight after the answer; moving on or completing gets the predefined acknowledgement.
        if follows_up:
            reaction = None
        elif reaction is None:
            reaction = self.choose_reaction(ctx, completes=completes)
        reaction_row = (
            None
            if reaction is None
            else InterviewMessage(
                id=reaction.id,
                session_id=setup.session_id,
                question_id=ctx.question_id,
                role=MessageRole.interviewer,
                content=reaction.text,
            )
        )
        if not self.repo.record_turn(
            answer, reaction_row, new_question, position, completes=completes
        ):
            # Lost a race: another submit of this question, or a newer interview, got there first.
            raise QuestionNotCurrentError(
                "This is not the current question of the interview"
            )

        return AnswerOut(
            session=SessionOut.model_validate(ctx.session),
            reaction=reaction,
            current_question=self._question_out(ctx.stored_next or new_question),
        )

    async def stream_answer(self, ctx: TurnContext, *, started_at: float) -> AsyncGenerator[StreamEventOut]:
        """The same turn as `answer`, as events: progress first, then the saved turn in `done`. Every stream ends with
        exactly one `done` or `error`. Nothing is saved before `done`, so a client that leaves early (its stream is
        cancelled) leaves the session on the same question. `started_at` is the request's perf_counter time."""
        terminal, cancelled, first_event_ms = "-", False, None
        first_token_ms, resets, writing_at = None, 0, None
        # One trace for the whole stream; it runs after the route returned, so it opens here, not in the route.
        with self._answer_trace(ctx):
            try:
                yield _event(StreamEvent.status, StatusEventOut(phase=TurnPhase.received))
                first_event_ms = _elapsed_ms(started_at)
                reaction, outcome = None, None
                if self.uses_interviewer(ctx):
                    assert self.interviewer is not None
                    turn = self.interviewer.stream_turn(
                        ctx.setup.session_id, self.turn_inputs(ctx), last_main=ctx.last_main
                    )
                    async with aclosing(turn) as events:
                        async for event in events:
                            match event:
                                case PhaseChanged(phase=phase):
                                    if phase == TurnPhase.writing:
                                        writing_at = time.perf_counter()
                                    yield _event(StreamEvent.status, StatusEventOut(phase=phase))
                                # A reaction is shown before the question it introduces, so only when the action was
                                # known before writing; a follow-up that fell back gets its reaction in `done` instead.
                                case ActionKnown(action=action) if action != TurnAction.follow_up and writing_at is None:
                                    reaction = self.choose_reaction(ctx, completes=action == TurnAction.complete)
                                    yield _event(StreamEvent.reaction, reaction)
                                case Delta(text=text):
                                    if first_token_ms is None and writing_at is not None:
                                        first_token_ms = _elapsed_ms(writing_at)
                                    yield _event(StreamEvent.question_delta, QuestionDeltaOut(text=text))
                                case Reset():
                                    resets += 1
                                    yield _event(StreamEvent.reset, ResetOut())
                                case Settled(outcome=settled):
                                    outcome = settled
                else:
                    reaction = self.choose_reaction(ctx, completes=self.completes_without_llm(ctx))
                    yield _event(StreamEvent.reaction, reaction)
                done = await anyio.to_thread.run_sync(self.finish_answer, ctx, outcome, reaction)
                terminal = StreamEvent.done.value
                yield _event(StreamEvent.done, done)
            except QuestionNotCurrentError as exc:
                # Lost the race to another submit of this question: the other one saved the turn.
                terminal = exc.code
                yield _error_event(exc.code, exc.message)
            except Exception:
                stream_logger.exception("stream_turn_failed session=%s", ctx.setup.session_id)
                terminal = "INTERNAL_ERROR"
                yield _error_event("INTERNAL_ERROR", "An unexpected error occurred")
            except BaseException:
                # The client left (the stream was cancelled or closed): nothing was saved.
                cancelled = True
                raise
            finally:
                log_stream_summary(
                    ctx.setup.session_id,
                    terminal=terminal,
                    first_event_ms=first_event_ms,
                    first_token_ms=first_token_ms,
                    total_ms=_elapsed_ms(started_at),
                    resets=resets,
                    cancelled=cancelled,
                )

    def transcript(self, user: User, session_id: uuid.UUID) -> TranscriptOut:
        session = self._owned_session(user, session_id)
        # A completed session stays at its last position, so this covers every question it ever showed.
        questions = self.repo.list_questions(session.id, session.current_position)
        return TranscriptOut(
            items=build_transcript(questions, self.repo.list_messages(session.id))
        )

    # --- the LLM's inputs, the bank fallback and the summary ---

    @staticmethod
    def _inputs(setup: InterviewSetup, turns: Sequence[QuestionTurn]) -> InterviewerInputs:
        return InterviewerInputs(
            role=setup.role,
            level=setup.level,
            interview_type=setup.interview_type,
            question_count=setup.question_count,
            job_description=setup.job_description_summary or setup.job_description,
            turns=turns,
            summary_used=setup.job_description_summary is not None,
        )

    def _bank_question(
        self, setup: InterviewSetup, position: int, main_number: int, used_bank_ids: set[str]
    ) -> InterviewQuestion:
        """The fallback when the LLM is off, fails, runs out of time or keeps breaking the contract."""
        picked = pick_fallback_question(
            self.bank,
            setup.role,
            setup.level,
            setup.interview_type,
            main_number,
            used_bank_ids,
            self.rng,
        )
        return InterviewQuestion(
            position=position,
            main_number=main_number,
            kind=QuestionKind.main,
            text=picked.text,
            category=picked.type,
            bank_id=picked.id,
            source=QuestionSource.bank,
        )

    def _summarize(self, setup: InterviewSetup) -> str | None:
        """Condense a long job description once, so later calls send less. One attempt with its own short time cap;
        any failure keeps the original text and never blocks the interview. Usage is logged, not stored.
        """
        original = setup.job_description
        if self.llm is None or not original or len(original) <= SUMMARY_THRESHOLD:
            return None
        built = self.context.build(SUMMARY_TASK, SummaryInputs(original))
        try:
            result = self.llm.complete(
                built.messages,
                max_tokens=self.llm_max_tokens,
                budget_seconds=SUMMARY_TIME_CAP_SECONDS,
                trace_labels={"task": SUMMARY_TASK, "prompt_version": built.prompt_version},
            )
        except LLMError as exc:
            log_llm_call(
                logging.WARNING,
                setup.session_id,
                f"summary_failed:{type(exc).__name__}",
                task=SUMMARY_TASK,
                prompt_version=built.prompt_version,
                latency_ms=exc.latency_ms,
                attempts=exc.attempts,
                finish=exc.finish_reason,
            )
            return None
        try:
            summary = validate_summary(original, result.text)
        except InvalidReplyError as exc:
            log_result(
                logging.WARNING,
                setup.session_id,
                f"summary_invalid:{exc.reason}",
                result,
                SUMMARY_TASK,
                built.prompt_version,
            )
            return None
        log_result(logging.INFO, setup.session_id, "summary_ok", result, SUMMARY_TASK, built.prompt_version)
        return summary

    # --- helpers ---

    def _owned_session(self, user: User, session_id: uuid.UUID) -> InterviewSession:
        session = self.repo.get_for_user(session_id, user.id)
        if session is None:
            raise NotFoundError("Interview not found")
        return session

    def _current_question(self, session: InterviewSession) -> InterviewQuestion | None:
        if session.status == SessionStatus.completed:
            return None
        return self.repo.get_question(session.id, session.current_position)

    @staticmethod
    def _question_out(question: InterviewQuestion | None) -> QuestionOut | None:
        return None if question is None else QuestionOut.model_validate(question)


def _event(name: StreamEvent, data: BaseModel) -> StreamEventOut:
    return StreamEventOut(name, data)


def _error_event(code: str, message: str) -> StreamEventOut:
    request_id = request_id_ctx.get()
    return _event(
        StreamEvent.error,
        StreamErrorOut(code=code, message=message, request_id=None if request_id == "-" else request_id),
    )


def _elapsed_ms(started_at: float) -> int:
    return round((time.perf_counter() - started_at) * 1000)


def _llm_question(
    written: Written,
    results: Sequence[LLMResult],
    position: int,
    main_number: int,
    *,
    kind: QuestionKind = QuestionKind.main,
    thread: Thread | None = None,
    decision_version: str | None = None,
) -> InterviewQuestion:
    """A question the LLM wrote; `results` is every call of the turn, so the stored usage is what the turn cost.

    A follow-up takes its thread's main question as parent and its category, whatever the model would have chosen.
    """
    reply = written.reply
    assert reply is not None
    return InterviewQuestion(
        position=position,
        main_number=main_number,
        kind=kind,
        parent_question_id=thread.main_id if thread else None,
        text=reply.question,
        category=thread.category if thread else reply.category,
        source=QuestionSource.llm,
        model=written.results[-1].model,
        prompt_version=written.prompt_version,
        decision_prompt_version=decision_version,
        prompt_tokens=sum_known([r.prompt_tokens for r in results]),
        completion_tokens=sum_known([r.completion_tokens for r in results]),
        latency_ms=sum(r.latency_ms for r in results),
    )
