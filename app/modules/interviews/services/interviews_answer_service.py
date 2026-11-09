"""One answer turn: the checks and reads, the LLM interviewer (or the bank), and the save of the whole turn.

The streamed turn yields domain events (the ai module's PhaseChanged, Delta and Reset, plus the ones below); the answer
controller turns them into SSE frames. Errors, the trace and the stream summary log stay here, so a stream logs the
same however it is presented.
"""

import logging
import random
import time
import uuid
from collections.abc import AsyncGenerator, Callable
from contextlib import aclosing
from typing import NamedTuple

import anyio

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider
from app.core.ai.tracing import Tracer
from app.core.errors import QuestionNotCurrentError, SessionNotInProgressError
from app.modules.auth.models.auth_model import User

from ..ai.interviews_context import CONTEXT_MANAGER, InterviewerInputs
from ..ai.interviews_turn import Interviewer
from ..ai.interviews_turn_log import log_stream_summary, log_turn_summary
from ..ai.interviews_turn_types import (
    ActionKnown,
    Delta,
    PhaseChanged,
    Reset,
    Settled,
    TurnAction,
    TurnOutcome,
)
from ..constants.interviews_constants import (
    InterviewType,
    JobRole,
    Level,
    MessageRole,
    QuestionCategory,
    QuestionKind,
    SessionStatus,
    TurnPhase,
)
from ..models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..schemas.interviews_schema import AnswerIn, BankQuestion
from ..utils.interviews_session_utils import (
    InterviewSetup,
    Thread,
    bank_question,
    interviewer_inputs,
    llm_question,
    owned_session,
)
from ..utils.interviews_utils import QuestionTurn, interviewer_history, pick_reaction

# Streamed turns that fail after their stream opened: the client gets a generic `error` event, the details land here.
stream_logger = logging.getLogger("app.errors")


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


class Reaction(NamedTuple):
    """The predefined acknowledgement; its id is the saved row's, so an early event and the saved turn agree."""

    id: uuid.UUID
    text: str


class TurnResult(NamedTuple):
    """The saved turn. `session` and `current_question` are refreshed after the commit, so reading them needs no
    further database call."""

    session: InterviewSession
    reaction: Reaction | None
    # The next question, or None when this answer completed the session.
    current_question: InterviewQuestion | None


# --- What a streamed turn yields besides the ai module's PhaseChanged, Delta and Reset ---


class ReactionChosen(NamedTuple):
    reaction: Reaction


class TurnSaved(NamedTuple):
    result: TurnResult


class TurnFailed(NamedTuple):
    """The stream's terminal error: a stable code and a generic message (details are logged, never sent)."""

    code: str
    message: str


AnswerEvent = PhaseChanged | ReactionChosen | Delta | Reset | TurnSaved | TurnFailed


class AnswerService:
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
        # Langfuse traces (one per request that can call the LLM); a disabled tracer costs nothing.
        self.tracer = tracer or Tracer(None)
        # Decide, limits, write: one answer turn of the LLM interviewer (ai/interviews_turn.py). None = LLM off.
        self.interviewer = (
            None
            if llm is None
            else Interviewer(
                llm, context, max_tokens=llm_max_tokens, budget_seconds=llm_budget_seconds, clock=clock
            )
        )

    def answer(self, user: User, session_id: uuid.UUID, data: AnswerIn) -> TurnResult:
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
        session = owned_session(self.repo, user, session_id)
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
        return interviewer_inputs(ctx.setup, ctx.history)

    def completes_without_llm(self, ctx: TurnContext) -> bool:
        """For a turn that doesn't use the interviewer: a stored next question never completes; otherwise the last
        main question does."""
        return ctx.stored_next is None and ctx.last_main

    def choose_reaction(self, ctx: TurnContext, *, completes: bool) -> Reaction:
        """The predefined acknowledgement for moving on (or completing). The id is set here, so it is the same in
        an early `reaction` event and in the saved row, and the response needs no read of the committed row."""
        text = pick_reaction(
            ctx.thread.category,
            ctx.setup.level,
            final=completes,
            previous=ctx.previous_reaction,
            rng=self.rng,
        )
        return Reaction(id=uuid.uuid7(), text=text)

    def finish_answer(
        self, ctx: TurnContext, outcome: TurnOutcome | None, reaction: Reaction | None = None
    ) -> TurnResult:
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
                new_question = llm_question(
                    outcome.written,
                    outcome.results,
                    position + 1,
                    thread.main_number,
                    kind=QuestionKind.follow_up,
                    thread=thread,
                    decision_version=outcome.decision_prompt_version,
                )
            elif outcome.action == TurnAction.next_question and outcome.written is not None:
                new_question = llm_question(
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

        current = ctx.stored_next or new_question
        # The commit expired these rows: reload them here (a worker thread), not where the response is built.
        self.repo.refresh(ctx.session, current)
        return TurnResult(session=ctx.session, reaction=reaction, current_question=current)

    async def stream_answer(self, ctx: TurnContext, *, started_at: float) -> AsyncGenerator[AnswerEvent]:
        """The same turn as `answer`, as events: progress first, then the saved turn. Every stream ends with exactly
        one TurnSaved or TurnFailed. Nothing is saved before TurnSaved, so a client that leaves early (its stream is
        cancelled) leaves the session on the same question. `started_at` is the request's perf_counter time."""
        terminal, cancelled, first_event_ms = "-", False, None
        first_token_ms, resets, writing_at = None, 0, None
        # One trace for the whole stream; it runs after the route returned, so it opens here, not in the route.
        with self._answer_trace(ctx):
            try:
                yield PhaseChanged(TurnPhase.received)
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
                                    yield event
                                # A reaction is shown before the question it introduces, so only when the action was
                                # known before writing; a follow-up that fell back gets its reaction in `done` instead.
                                case ActionKnown(action=action) if action != TurnAction.follow_up and writing_at is None:
                                    reaction = self.choose_reaction(ctx, completes=action == TurnAction.complete)
                                    yield ReactionChosen(reaction)
                                case Delta():
                                    if first_token_ms is None and writing_at is not None:
                                        first_token_ms = _elapsed_ms(writing_at)
                                    yield event
                                case Reset():
                                    resets += 1
                                    yield event
                                case Settled(outcome=settled):
                                    outcome = settled
                else:
                    reaction = self.choose_reaction(ctx, completes=self.completes_without_llm(ctx))
                    yield ReactionChosen(reaction)
                done = await anyio.to_thread.run_sync(self.finish_answer, ctx, outcome, reaction)
                terminal = "done"
                yield TurnSaved(done)
            except QuestionNotCurrentError as exc:
                # Lost the race to another submit of this question: the other one saved the turn.
                terminal = exc.code
                yield TurnFailed(exc.code, exc.message)
            except Exception:
                stream_logger.exception("stream_turn_failed session=%s", ctx.setup.session_id)
                terminal = "INTERNAL_ERROR"
                yield TurnFailed("INTERNAL_ERROR", "An unexpected error occurred")
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

    def _bank_question(
        self, setup: InterviewSetup, position: int, main_number: int, used_bank_ids: set[str]
    ) -> InterviewQuestion:
        return bank_question(self.bank, self.rng, setup, position, main_number, used_bank_ids)


def _elapsed_ms(started_at: float) -> int:
    return round((time.perf_counter() - started_at) * 1000)
