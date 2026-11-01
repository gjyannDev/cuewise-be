import logging
import random
import time
import uuid
from collections.abc import Callable, Sequence
from typing import NamedTuple

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMError, LLMProvider, LLMResult
from app.core.errors import (
    NotFoundError,
    QuestionNotCurrentError,
    SessionNotInProgressError,
)
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
    QuestionOut,
    ReactionOut,
    SessionOut,
    TranscriptOut,
)
from .interviews_turn import (
    Interviewer,
    TurnAction,
    Written,
    log_llm_call,
    log_result,
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
    ):
        self.repo = repo
        self.bank = bank
        self.rng = rng
        # None = LLM off: every question comes from the bank.
        self.llm = llm
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
        last_main = thread.main_number == setup.question_count
        used_bank_ids = {q.bank_id for q in asked if q.bank_id}
        # Pre-slice-2 sessions stored every question up front: no LLM, no follow-ups, the stored order.
        stored_next = self.repo.get_question(session.id, position + 1)
        previous_reaction = next(
            (m.content for m in reversed(saved) if m.role == MessageRole.interviewer),
            None,
        )
        answer = InterviewMessage(
            session_id=session.id,
            question_id=question.id,
            role=MessageRole.candidate,
            content=data.answer,
        )
        self.repo.release()

        new_question: InterviewQuestion | None = None
        if stored_next is not None:
            completes = False
            log_turn_summary(setup.session_id, decision="skipped", action=TurnAction.next_question, source="stored")
        elif self.interviewer is None:
            completes = last_main
            if not completes:
                new_question = self._bank_question(setup, position + 1, thread.main_number + 1, used_bank_ids)
            log_turn_summary(
                setup.session_id,
                decision="skipped",
                action=TurnAction.complete if completes else TurnAction.next_question,
                source="-" if completes else "bank",
            )
        else:
            outcome = self.interviewer.answer_turn(
                setup.session_id, self._inputs(setup, history), last_main=last_main
            )
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
                new_question = self._bank_question(setup, position + 1, thread.main_number + 1, used_bank_ids)

        follows_up = new_question is not None and new_question.kind == QuestionKind.follow_up
        reaction, reaction_text, reaction_id = None, "", uuid.uuid7()
        # A follow-up comes straight after the answer; moving on or completing gets the predefined acknowledgement.
        if not follows_up:
            reaction_text = pick_reaction(
                thread.category,
                setup.level,
                final=completes,
                previous=previous_reaction,
                rng=self.rng,
            )
            # The id is set here so the response needs no read of the committed (expired) row.
            reaction = InterviewMessage(
                id=reaction_id,
                session_id=setup.session_id,
                question_id=data.question_id,
                role=MessageRole.interviewer,
                content=reaction_text,
            )
        if not self.repo.record_turn(
            answer, reaction, new_question, position, completes=completes
        ):
            # Lost a race: another submit of this question, or a newer interview, got there first.
            raise QuestionNotCurrentError(
                "This is not the current question of the interview"
            )

        return AnswerOut(
            session=SessionOut.model_validate(session),
            reaction=None if reaction is None else ReactionOut(id=reaction_id, text=reaction_text),
            current_question=self._question_out(stored_next or new_question),
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
