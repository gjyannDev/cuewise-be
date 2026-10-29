import logging
import random
import time
import uuid
from collections.abc import Callable, Sequence
from typing import NamedTuple

from app.core.ai.provider import LLMError, LLMProvider, LLMResult
from app.core.errors import (
    NotFoundError,
    QuestionNotCurrentError,
    SessionNotInProgressError,
)
from app.modules.auth.auth_model import User

from .interviews_constants import (
    FIRST_POSITION,
    INTERVIEWER_PROMPT_VERSION,
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
    InterviewType,
    JobRole,
    Level,
    MessageRole,
    QuestionCategory,
    QuestionSource,
    SessionStatus,
)
from .interviews_model import InterviewMessage, InterviewQuestion, InterviewSession
from .interviews_reply import InvalidReplyError, parse_interviewer_reply
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
from .interviews_utils import (
    QuestionTurn,
    build_interviewer_messages,
    build_transcript,
    interviewer_history,
    pick_fallback_question,
    pick_reaction,
    render_interviewer_prompt,
    select_questions,
)

# One line per LLM call: metadata only (ids, model, tokens, timing, outcome), never answer or reply text.
llm_logger = logging.getLogger("app.llm")


def _log_llm_call(
    level: int,
    session_id: uuid.UUID,
    outcome: str,
    *,
    prompt_version: str = INTERVIEWER_PROMPT_VERSION,
    model: str = "-",
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    latency_ms: int,
    attempts: int,
    finish: str | None = None,
) -> None:
    llm_logger.log(
        level,
        "llm_call session=%s model=%s prompt_version=%s prompt_tokens=%s completion_tokens=%s "
        "latency_ms=%s attempts=%s finish=%s outcome=%s",
        session_id,
        model,
        prompt_version,
        "-" if prompt_tokens is None else prompt_tokens,
        "-" if completion_tokens is None else completion_tokens,
        latency_ms,
        attempts,
        finish or "-",
        outcome,
    )


def _log_result(
    level: int, session_id: uuid.UUID, outcome: str, result: LLMResult
) -> None:
    _log_llm_call(
        level,
        session_id,
        outcome,
        model=result.model,
        prompt_tokens=result.prompt_tokens,
        completion_tokens=result.completion_tokens,
        latency_ms=result.latency_ms,
        attempts=result.attempts,
        finish=result.finish_reason,
    )


def _sum_known(values: Sequence[int | None]) -> int | None:
    known = [v for v in values if v is not None]
    return sum(known) if known else None


class InterviewSetup(NamedTuple):
    """The session fields the interviewer needs, as plain values that survive the end of a transaction."""

    session_id: uuid.UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    job_description: str | None


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
    ):
        self.repo = repo
        self.bank = bank
        self.rng = rng
        # None = LLM off: every question comes from the bank.
        self.llm = llm
        self.llm_max_tokens = llm_max_tokens
        self.llm_budget_seconds = llm_budget_seconds
        self.clock = clock

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
        first = self._next_question(
            setup, FIRST_POSITION, history=[], used_bank_ids=set()
        )
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

        # Read everything as plain values first: the read transaction ends before the (slow) LLM call, and after
        # that every loaded ORM object is expired.
        setup = InterviewSetup(
            session.id,
            JobRole(session.role),
            Level(session.level),
            InterviewType(session.interview_type),
            session.question_count,
            session.job_description,
        )
        completes = position == session.question_count
        asked = self.repo.list_questions(session.id, position)
        saved = self.repo.list_messages(session.id)
        history = [
            *interviewer_history(asked[:-1], saved),
            QuestionTurn(question.text, question.category, data.answer),
        ]
        used_bank_ids = {q.bank_id for q in asked if q.bank_id}
        stored_next = (
            None if completes else self.repo.get_question(session.id, position + 1)
        )
        previous_reaction = next(
            (m.content for m in reversed(saved) if m.role == MessageRole.interviewer),
            None,
        )
        reaction_text = pick_reaction(
            QuestionCategory(question.category),
            setup.level,
            final=completes,
            previous=previous_reaction,
            rng=self.rng,
        )
        answer = InterviewMessage(
            session_id=session.id,
            question_id=question.id,
            role=MessageRole.candidate,
            content=data.answer,
        )
        # The id is set here so the response needs no read of the committed (expired) row.
        reaction_id = uuid.uuid7()
        reaction = InterviewMessage(
            id=reaction_id,
            session_id=session.id,
            question_id=question.id,
            role=MessageRole.interviewer,
            content=reaction_text,
        )
        self.repo.release()

        # Pre-slice-2 sessions already stored every question; otherwise the interviewer writes the next one.
        next_question = stored_next
        if not completes and next_question is None:
            next_question = self._next_question(
                setup, position + 1, history=history, used_bank_ids=used_bank_ids
            )
        new_question = None if stored_next is not None else next_question
        if not self.repo.record_turn(
            answer, reaction, new_question, position, completes=completes
        ):
            # Lost a race: another submit of this question, or a newer interview, got there first.
            raise QuestionNotCurrentError(
                "This is not the current question of the interview"
            )

        return AnswerOut(
            session=SessionOut.model_validate(session),
            reaction=ReactionOut(id=reaction_id, text=reaction_text),
            current_question=self._question_out(next_question),
        )

    def transcript(self, user: User, session_id: uuid.UUID) -> TranscriptOut:
        session = self._owned_session(user, session_id)
        # A completed session stays at its last position, so this covers every question it ever showed.
        questions = self.repo.list_questions(session.id, session.current_position)
        return TranscriptOut(
            items=build_transcript(questions, self.repo.list_messages(session.id))
        )

    # --- the next question: the LLM first, the bank as the fallback ---

    def _next_question(
        self,
        setup: InterviewSetup,
        position: int,
        *,
        history: Sequence[QuestionTurn],
        used_bank_ids: set[str],
    ) -> InterviewQuestion:
        """Never fails because of the LLM: if it is off, fails, or keeps breaking the contract, the bank answers."""
        if self.llm is not None:
            question = self._ask_llm(self.llm, setup, position, history)
            if question is not None:
                return question
        picked = pick_fallback_question(
            self.bank,
            setup.role,
            setup.level,
            setup.interview_type,
            position,
            used_bank_ids,
            self.rng,
        )
        return InterviewQuestion(
            position=position,
            text=picked.text,
            category=picked.type,
            bank_id=picked.id,
            source=QuestionSource.bank,
        )

    def _ask_llm(
        self,
        llm: LLMProvider,
        setup: InterviewSetup,
        position: int,
        history: Sequence[QuestionTurn],
    ) -> InterviewQuestion | None:
        """At most two attempts sharing one time budget. Only a reply that came back but broke the contract is
        retried: a provider error was already retried inside the provider, and an empty reply would fail the same way.
        """
        system_prompt = render_interviewer_prompt(
            role=setup.role,
            level=setup.level,
            interview_type=setup.interview_type,
            question_number=position,
            question_count=setup.question_count,
        )
        messages = build_interviewer_messages(
            system_prompt, setup.job_description, history
        )
        earlier = [turn.question for turn in history]
        deadline = self.clock() + self.llm_budget_seconds
        results: list[LLMResult] = []

        for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
            remaining = deadline - self.clock()
            if attempt > 1 and remaining < MIN_SECONDS_FOR_RETRY:
                return None
            try:
                result = llm.complete(
                    messages, max_tokens=self.llm_max_tokens, budget_seconds=remaining
                )
            except LLMError as exc:
                # Transient faults are expected now and then; a bad key or broken reply needs someone to look.
                level = logging.WARNING if exc.retryable else logging.ERROR
                _log_llm_call(
                    level,
                    setup.session_id,
                    type(exc).__name__,
                    latency_ms=exc.latency_ms,
                    attempts=exc.attempts,
                    finish=exc.finish_reason,
                )
                return None
            results.append(result)
            if not result.text.strip():
                _log_result(logging.WARNING, setup.session_id, "empty_reply", result)
                return None
            try:
                reply = parse_interviewer_reply(
                    result.text,
                    interview_type=setup.interview_type,
                    earlier_questions=earlier,
                )
            except InvalidReplyError as exc:
                _log_result(
                    logging.WARNING,
                    setup.session_id,
                    f"invalid_reply:{exc.reason}",
                    result,
                )
                continue
            _log_result(logging.INFO, setup.session_id, "ok", result)
            return InterviewQuestion(
                position=position,
                text=reply.question,
                category=reply.category,
                source=QuestionSource.llm,
                model=result.model,
                prompt_version=INTERVIEWER_PROMPT_VERSION,
                prompt_tokens=_sum_known([r.prompt_tokens for r in results]),
                completion_tokens=_sum_known([r.completion_tokens for r in results]),
                latency_ms=sum(r.latency_ms for r in results),
            )
        return None

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
