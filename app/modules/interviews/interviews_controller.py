import logging
import random
import uuid
from collections.abc import Sequence

from app.core.ai.provider import ChatMessage, LLMError, LLMProvider, LLMResult
from app.core.errors import (
    NotFoundError,
    QuestionNotCurrentError,
    SessionNotInProgressError,
)
from app.modules.auth.auth_model import User

from .interviews_constants import (
    FIRST_POSITION,
    REACTION_PROMPT_VERSION,
    JobRole,
    Level,
    MessageRole,
    SessionStatus,
)
from .interviews_model import InterviewMessage, InterviewQuestion, InterviewSession
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
    Turn,
    build_llm_messages,
    build_transcript,
    history_turns,
    render_reaction_prompt,
    select_questions,
)

# One line per LLM call: metadata only (ids, model, tokens, timing, outcome), never answer or reply text.
llm_logger = logging.getLogger("app.llm")


def _log_llm_call(
    level: int,
    session_id: uuid.UUID,
    outcome: str,
    *,
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
        REACTION_PROMPT_VERSION,
        "-" if prompt_tokens is None else prompt_tokens,
        "-" if completion_tokens is None else completion_tokens,
        latency_ms,
        attempts,
        finish or "-",
        outcome,
    )


class InterviewsController:
    def __init__(
        self,
        repo: InterviewsRepository,
        bank: list[BankQuestion],
        rng: random.Random,
        llm: LLMProvider | None = None,
        llm_max_tokens: int = 150,
    ):
        self.repo = repo
        self.bank = bank
        self.rng = rng
        # None = LLM off: answers still work, reactions are null.
        self.llm = llm
        self.llm_max_tokens = llm_max_tokens

    def start(self, user: User, data: InterviewCreateIn) -> InterviewOut:
        picked = select_questions(
            self.bank,
            data.role,
            data.level,
            data.interview_type,
            data.question_count,
            self.rng,
        )
        session = InterviewSession(user_id=user.id, **data.model_dump())
        # Copy the text now: later bank edits must not change a session already started.
        questions = [
            InterviewQuestion(
                position=position, text=q.text, category=q.type, bank_id=q.id
            )
            for position, q in enumerate(picked, start=FIRST_POSITION)
        ]
        self.repo.start(session, questions)
        return InterviewOut(
            session=SessionOut.model_validate(session),
            current_question=QuestionOut.model_validate(questions[0]),
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

        completes = position == session.question_count
        # Built now, while the transaction is open: after the commit every ORM attribute expires, and touching one
        # would quietly start a new transaction that stays open for the whole (slow) LLM call.
        llm_messages = (
            self._llm_messages(session, question, data.answer) if self.llm else None
        )
        session_pk, question_pk = session.id, question.id
        answer = InterviewMessage(
            session_id=session_pk,
            question_id=question_pk,
            role=MessageRole.candidate,
            content=data.answer,
        )
        if not self.repo.record_answer(answer, position, completes=completes):
            # Lost a race with another submit of the same question.
            raise QuestionNotCurrentError(
                "This is not the current question of the interview"
            )

        # Short write, slow call, short write: the answer is safe before the LLM is asked anything.
        reaction = (
            self._react(self.llm, session_pk, question_pk, llm_messages)
            if self.llm and llm_messages
            else None
        )

        next_question = (
            None if completes else self.repo.get_question(session_pk, position + 1)
        )
        return AnswerOut(
            session=SessionOut.model_validate(session),
            reaction=reaction,
            current_question=self._question_out(next_question),
        )

    def _llm_messages(
        self, session: InterviewSession, question: InterviewQuestion, answer: str
    ) -> list[ChatMessage]:
        earlier = self.repo.list_questions(session.id, question.position - 1)
        turns = [
            *history_turns(earlier, self.repo.list_messages(session.id)),
            Turn(question.text, answer, None),
        ]
        system_prompt = render_reaction_prompt(
            JobRole(session.role), Level(session.level)
        )
        return build_llm_messages(system_prompt, turns)

    def _react(
        self,
        llm: LLMProvider,
        session_id: uuid.UUID,
        question_id: uuid.UUID,
        messages: Sequence[ChatMessage],
    ) -> ReactionOut | None:
        """Ask the LLM for a reaction; any failure is a missing reaction, never a failed answer."""
        try:
            result = llm.complete(messages, max_tokens=self.llm_max_tokens)
        except LLMError as exc:
            # Transient faults are expected now and then; a bad key or broken reply needs someone to look.
            level = logging.WARNING if exc.retryable else logging.ERROR
            _log_llm_call(
                level,
                session_id,
                type(exc).__name__,
                latency_ms=exc.latency_ms,
                attempts=exc.attempts,
            )
            return None
        text = result.text.strip()
        _log_llm_call(
            logging.INFO if text else logging.WARNING,
            session_id,
            "ok" if text else "empty_reply",
            model=result.model,
            prompt_tokens=result.prompt_tokens,
            completion_tokens=result.completion_tokens,
            latency_ms=result.latency_ms,
            attempts=result.attempts,
            finish=result.finish_reason,
        )
        if not text:
            return None
        reaction_id = uuid.uuid7()
        self.repo.save_message(
            self._reaction_message(reaction_id, session_id, question_id, text, result)
        )
        return ReactionOut(id=reaction_id, text=text)

    @staticmethod
    def _reaction_message(
        reaction_id: uuid.UUID,
        session_id: uuid.UUID,
        question_id: uuid.UUID,
        text: str,
        result: LLMResult,
    ) -> InterviewMessage:
        return InterviewMessage(
            id=reaction_id,
            session_id=session_id,
            question_id=question_id,
            role=MessageRole.interviewer,
            content=text,
            model=result.model,
            prompt_version=REACTION_PROMPT_VERSION,
            prompt_tokens=result.prompt_tokens,
            completion_tokens=result.completion_tokens,
            latency_ms=result.latency_ms,
        )

    def transcript(self, user: User, session_id: uuid.UUID) -> TranscriptOut:
        session = self._owned_session(user, session_id)
        # A completed session stays at its last position, so this covers every question it ever showed.
        questions = self.repo.list_questions(session.id, session.current_position)
        return TranscriptOut(
            items=build_transcript(questions, self.repo.list_messages(session.id))
        )

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
