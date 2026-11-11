"""The interview itself: start it (first question, optional job-description summary), read it, list the history and
the transcript. Answer turns are in interviews_answer_service.py, voice answers in interviews_transcription_service.py.
"""

import logging
import random
import time
import uuid
from collections.abc import Callable, Sequence
from typing import NamedTuple

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMError, LLMProvider
from app.core.ai.tracing import Tracer
from app.core.pagination import PageParams
from app.modules.auth.models.auth_model import User

from ..ai.interviews_context import CONTEXT_MANAGER, SummaryInputs
from ..ai.interviews_reply import InvalidReplyError, validate_summary
from ..ai.interviews_turn import Interviewer
from ..ai.interviews_turn_log import log_llm_call, log_result
from ..constants.interviews_constants import (
    FIRST_POSITION,
    SUMMARY_TASK,
    SUMMARY_THRESHOLD,
    SUMMARY_TIME_CAP_SECONDS,
    HistorySortColumn,
    SessionStatus,
    SortDirection,
)
from ..models.interviews_knowledge_model import InterviewSessionChunk
from ..models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..schemas.interviews_schema import BankQuestion, InterviewCreateIn
from ..services.interviews_retrieval_service import RetrievalService
from ..utils.interviews_session_utils import (
    InterviewSetup,
    bank_question,
    interviewer_inputs,
    llm_question,
    owned_session,
)
from ..utils.interviews_utils import answered_main_questions, select_questions


class InterviewState(NamedTuple):
    session: InterviewSession
    # None once the session is completed.
    current_question: InterviewQuestion | None


class HistoryPage(NamedTuple):
    """One page of the user's interviews, each with its answered main-question count, and the total."""

    rows: list[tuple[InterviewSession, int]]
    total: int


class Transcript(NamedTuple):
    questions: Sequence[InterviewQuestion]
    messages: Sequence[InterviewMessage]


class InterviewsService:
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
        retrieval: RetrievalService | None = None,
    ):
        self.repo = repo
        self.bank = bank
        self.rng = rng
        # None = LLM off: every question comes from the bank.
        self.llm = llm
        # Picks the interview's reference notes at start (knowledge-base RAG); None = no notes (evals, older tests).
        self.retrieval = retrieval
        # Langfuse traces (one per request that can call the LLM); a disabled tracer costs nothing.
        self.tracer = tracer or Tracer(None)
        self.llm_max_tokens = llm_max_tokens
        # Decides what each LLM call sends (strategy, trimming); see ai/interviews_context.py.
        self.context = context
        # Writes the first question (ai/interviews_turn.py).
        self.interviewer = (
            None
            if llm is None
            else Interviewer(
                llm, context, max_tokens=llm_max_tokens, budget_seconds=llm_budget_seconds, clock=clock
            )
        )

    def start(self, user: User, data: InterviewCreateIn) -> InterviewState:
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
            note_refs: list[InterviewSessionChunk] = []
            if self.retrieval is not None:
                # After the summary: the query is the summary when there is one. Never fails the start.
                retrieval = self.retrieval.retrieve(
                    setup.session_id,
                    setup.role,
                    setup.level,
                    summary=setup.job_description_summary,
                    job_description=setup.job_description,
                )
                setup = setup._replace(reference_notes=tuple(retrieval.notes))
                note_refs = [
                    InterviewSessionChunk(chunk_id=note.chunk_id, rank=note.rank, score=note.score, mode=retrieval.mode)
                    for note in retrieval.notes
                ]
            first = None
            if self.interviewer is not None:
                written = self.interviewer.first_question(setup.session_id, interviewer_inputs(setup, []))
                if written.reply is not None:
                    first = llm_question(written, written.results, FIRST_POSITION, 1)
            if first is None:
                first = bank_question(self.bank, self.rng, setup, FIRST_POSITION, 1, set())
            self.repo.start(session, [first], note_refs)
            return InterviewState(session, first)

    def get(self, user: User, session_id: uuid.UUID) -> InterviewState:
        session = owned_session(self.repo, user, session_id)
        return InterviewState(session, self._current_question(session))

    def list_interviews(
        self,
        user: User,
        status: SessionStatus | None,
        sort_by: HistorySortColumn,
        sort_dir: SortDirection,
        page: PageParams,
    ) -> HistoryPage:
        """The user's own interviews in the requested order: the history table. Under the default order (newest first)
        the in-progress one (at most one) is first."""
        rows = self.repo.list_for_user(user.id, status, sort_by, sort_dir, page.limit, page.offset)
        counted = [
            (s, answered_main_questions(SessionStatus(s.status), s.question_count, main_number))
            for s, main_number in rows
        ]
        return HistoryPage(counted, self.repo.count_for_user(user.id, status))

    def transcript(self, user: User, session_id: uuid.UUID) -> Transcript:
        session = owned_session(self.repo, user, session_id)
        # A completed session stays at its last position, so this covers every question it ever showed.
        questions = self.repo.list_questions(session.id, session.current_position)
        return Transcript(questions, self.repo.list_messages(session.id))

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

    def _current_question(self, session: InterviewSession) -> InterviewQuestion | None:
        if session.status == SessionStatus.completed:
            return None
        return self.repo.get_question(session.id, session.current_position)
