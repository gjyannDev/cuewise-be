"""End-of-interview feedback: ownership, the claim, the two LLM steps, and what is stored and returned.

Database work and orchestration only: the contract is in interviews_feedback.py, the LLM calls in
interviews_feedback_turn.py. No transaction stays open during an LLM call (the read is released first and every write
commits at once), and every write after the claim lands only while this request still holds the claim.
"""

import uuid
from collections.abc import Callable
from datetime import datetime, timedelta
from typing import Any, NamedTuple

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider, LLMResult
from app.core.ai.tracing import Tracer
from app.core.errors import (
    FeedbackFailedError,
    FeedbackInProgressError,
    FeedbackNotFoundError,
    FeedbackUnavailableError,
    InterviewNotCompletedError,
    NotFoundError,
)
from app.modules.auth.auth_model import User

from .interviews_constants import (
    FEEDBACK_INSUFFICIENT_MESSAGE,
    FEEDBACK_RUBRIC_VERSION,
    FeedbackStatus,
    InterviewType,
    JobRole,
    Level,
    SessionStatus,
    TextSource,
)
from .interviews_context import FeedbackScoreInputs, FeedbackWriteInputs
from .interviews_feedback import (
    FeedbackThread,
    StoredResult,
    assess_evidence,
    build_threads,
    compute_overall,
    stored_scores,
    template_text,
)
from .interviews_feedback_turn import CallUsage, FeedbackGenerator, log_feedback_summary
from .interviews_model import InterviewFeedback, InterviewSession
from .interviews_repository import InterviewsRepository
from .interviews_schema import FeedbackEvidenceOut, FeedbackOut, FeedbackQuestionOut


class _Interview(NamedTuple):
    """The interview as plain values, read before the claim's commit expires the loaded rows."""

    session_id: uuid.UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    # The effective one: the stored summary when there is one, else the original.
    job_description: str | None
    summary_used: bool


class _Claim(NamedTuple):
    feedback_id: uuid.UUID
    # The claim token: every later write must match it.
    started_at: datetime
    # Validated scores a crashed request already stored; a takeover then only writes the text.
    stored: StoredResult | None


class _Outcome(NamedTuple):
    """How a generation ended, for the trace (metadata only)."""

    status: FeedbackStatus
    overall: float | None = None
    text_source: TextSource | None = None
    quotes_rejected: int = 0
    scores: dict[int, dict[str, int]] | None = None
    # generated, insufficient (too little to assess) or failed: what a reader of the trace list wants first.
    outcome: str = "generated"


class _LostClaim(Exception):
    """Another request took the row over while this one ran: this one's writes are dropped."""


class FeedbackController:
    def __init__(
        self,
        repo: InterviewsRepository,
        llm: LLMProvider | None,
        *,
        context: ContextManager,
        clock: Callable[[], float],
        now: Callable[[], datetime],
        tracer: Tracer | None = None,
        budget_seconds: float,
        stale_margin_seconds: float,
        score_max_tokens: int,
        write_max_tokens: int,
        score_temperature: float,
    ):
        self.repo = repo
        # Wall-clock time, stored as the claim token and compared for stale takeover (in SQL). The LLM deadline uses
        # the monotonic `clock` instead.
        self.now = now
        self.tracer = tracer or Tracer(None)
        self.budget_seconds = budget_seconds
        self.stale_margin_seconds = stale_margin_seconds
        # None = LLM off: POST answers 503, GET still works.
        self.generator = (
            None
            if llm is None
            else FeedbackGenerator(
                llm,
                context,
                score_max_tokens=score_max_tokens,
                write_max_tokens=write_max_tokens,
                score_temperature=score_temperature,
                clock=clock,
                tracer=self.tracer,
            )
        )

    def get(self, user: User, session_id: uuid.UUID) -> FeedbackOut:
        session = self._owned_session(user, session_id)
        feedback = self.repo.get_feedback(session.id)
        if feedback is None:
            raise FeedbackNotFoundError("No feedback for this interview yet")
        return feedback_out(feedback)

    def generate(self, user: User, session_id: uuid.UUID) -> tuple[FeedbackOut, bool]:
        """The feedback, generated now (True) or already stored (False). Checks run in this order so a stored result
        is returned even when the LLM is off, and nothing is claimed for a request that can't run."""
        session = self._owned_session(user, session_id)
        if session.status != SessionStatus.completed:
            raise InterviewNotCompletedError("Feedback is available once the interview is completed")
        interview = _Interview(
            session.id,
            JobRole(session.role),
            Level(session.level),
            InterviewType(session.interview_type),
            session.job_description_summary or session.job_description,
            session.job_description_summary is not None,
        )
        existing = self.repo.get_feedback(session.id)
        if existing is not None and existing.status == FeedbackStatus.generated:
            return feedback_out(existing), False
        if self.generator is None:
            raise FeedbackUnavailableError("Feedback is not available right now. Try again later.")

        claim = self._claim(interview.session_id, existing)
        threads = build_threads(
            self.repo.list_session_questions(interview.session_id), self.repo.list_messages(interview.session_id)
        )
        # Plain values from here on: no connection sits idle in a transaction during the LLM calls.
        self.repo.release()

        with self.tracer.trace(
            "interview-feedback",
            user_id=str(user.id),
            session_id=str(interview.session_id),
            input={"interview_id": str(interview.session_id)},
            tags=["feedback"],
            metadata={"rubric_version": FEEDBACK_RUBRIC_VERSION},
        ) as trace_id:
            try:
                outcome = self._run(interview, threads, claim)
            except _LostClaim:
                current = self.repo.get_feedback(interview.session_id)
                if current is not None and current.status == FeedbackStatus.generated:
                    return feedback_out(current), False
                raise FeedbackInProgressError("Feedback for this interview is already being generated") from None
            self.tracer.set_trace_output(outcome._asdict())
        if outcome.overall is not None:
            self.tracer.score(trace_id, "overall", outcome.overall)
        if outcome.overall is not None or outcome.status == FeedbackStatus.failed:
            self.tracer.score(trace_id, "quotes_rejected", outcome.quotes_rejected)
        if outcome.status == FeedbackStatus.failed:
            raise FeedbackFailedError("Feedback could not be generated. Try again.")
        feedback = self.repo.get_feedback(interview.session_id)
        assert feedback is not None
        return feedback_out(feedback), True

    def _claim(self, session_id: uuid.UUID, existing: InterviewFeedback | None) -> _Claim:
        started_at = self.now()
        if existing is None:
            feedback_id = uuid.uuid7()
            row = InterviewFeedback(
                id=feedback_id,
                session_id=session_id,
                status=FeedbackStatus.generating,
                rubric_version=FEEDBACK_RUBRIC_VERSION,
                started_at=started_at,
            )
            if not self.repo.insert_feedback(row):
                raise FeedbackInProgressError("Feedback for this interview is already being generated")
            return _Claim(feedback_id, started_at, None)
        feedback_id = existing.id
        stored = None if existing.result is None else StoredResult.model_validate(existing.result)
        stale_before = started_at - timedelta(seconds=self.budget_seconds + self.stale_margin_seconds)
        if not self.repo.reclaim_feedback(session_id, started_at, stale_before):
            raise FeedbackInProgressError("Feedback for this interview is already being generated")
        return _Claim(feedback_id, started_at, stored)

    def _run(self, interview: _Interview, threads: list[FeedbackThread], claim: _Claim) -> _Outcome:
        assert self.generator is not None
        session_id = interview.session_id
        deadline = self.generator.deadline(self.budget_seconds)
        stored = claim.stored
        score_results: list[LLMResult] = []
        quotes_rejected = truncated = 0
        if stored is None:
            if not assess_evidence(threads):
                return self._insufficient(claim, session_id, {})
            scored = self.generator.score(
                session_id,
                FeedbackScoreInputs(
                    interview.role,
                    interview.level,
                    interview.interview_type,
                    interview.job_description,
                    threads,
                    interview.summary_used,
                ),
                deadline,
            )
            score_results, quotes_rejected, truncated = scored.results, scored.quotes_rejected, scored.truncated
            usage = _usage("score", scored.results) | {
                "score_prompt_version": scored.prompt_version,
                "rubric_version": FEEDBACK_RUBRIC_VERSION,
            }
            if scored.result is None:
                self._write(claim, status=FeedbackStatus.failed, failure_reason=scored.failure, finished_at=self.now(), **usage)
                log_feedback_summary(
                    session_id,
                    outcome="failed",
                    score=score_results,
                    quotes_rejected=quotes_rejected,
                    truncated=truncated,
                    failure=scored.failure,
                )
                return _Outcome(FeedbackStatus.failed, quotes_rejected=quotes_rejected, outcome="failed")
            if not scored.result.enough_evidence:
                return self._insufficient(claim, session_id, usage, score_results)
            stored = stored_scores(threads, scored.result.questions)
            overall = compute_overall(scored.result.questions)
            # Stored before the write call: a failed or crashed write never repeats the expensive score call.
            self._write(
                claim, enough_evidence=True, overall=overall, result=stored.model_dump(mode="json"), **usage
            )
        else:
            overall = compute_overall(stored.question_scores())

        written = self.generator.write(
            session_id,
            FeedbackWriteInputs(interview.role, interview.level, interview.interview_type, overall, stored),
            [q.main_number for q in stored.questions],
            deadline,
        )
        text, source = (
            (written.text, TextSource.llm)
            if written.text is not None
            else (template_text(stored.question_scores(), overall), TextSource.template)
        )
        self._write(
            claim,
            status=FeedbackStatus.generated,
            text_source=source,
            result=stored.with_text(text).model_dump(mode="json"),
            write_prompt_version=written.prompt_version,
            finished_at=self.now(),
            **_usage("write", written.results),
        )
        log_feedback_summary(
            session_id,
            outcome="generated",
            overall=overall,
            text_source=source,
            score=score_results,
            write=written.results,
            quotes_rejected=quotes_rejected,
            truncated=truncated,
            failure=written.failure,
        )
        scores = {q.main_number: {c.value: v for c, v in q.scores.items()} for q in stored.questions}
        return _Outcome(FeedbackStatus.generated, overall, source, quotes_rejected, scores)

    def _insufficient(
        self, claim: _Claim, session_id: uuid.UUID, usage: dict[str, Any], score_results: list[LLMResult] | None = None
    ) -> _Outcome:
        """Too little to assess (the code's pre-check, or the model's flag): final, with no scores invented."""
        self._write(
            claim,
            status=FeedbackStatus.generated,
            enough_evidence=False,
            finished_at=self.now(),
            **({"rubric_version": FEEDBACK_RUBRIC_VERSION} | usage),
        )
        log_feedback_summary(session_id, outcome="insufficient", score=score_results or [])
        return _Outcome(FeedbackStatus.generated, outcome="insufficient")

    def _write(self, claim: _Claim, **values: Any) -> None:
        if not self.repo.update_claimed_feedback(claim.feedback_id, claim.started_at, values):
            raise _LostClaim

    def _owned_session(self, user: User, session_id: uuid.UUID) -> InterviewSession:
        session = self.repo.get_for_user(session_id, user.id)
        if session is None:
            raise NotFoundError("Interview not found")
        return session


def _usage(call: str, results: list[LLMResult]) -> dict[str, Any]:
    usage = CallUsage.of(results)
    return {
        f"{call}_model": usage.model,
        f"{call}_prompt_tokens": usage.prompt_tokens,
        f"{call}_completion_tokens": usage.completion_tokens,
        f"{call}_latency_ms": usage.latency_ms if results else None,
    }


def feedback_out(feedback: InterviewFeedback) -> FeedbackOut:
    """What the client sees. Scores and text only once generated, so a half-written or failed row never shows any."""
    generated = feedback.status == FeedbackStatus.generated
    result = (
        StoredResult.model_validate(feedback.result)
        if generated and feedback.enough_evidence and feedback.result is not None
        else None
    )
    summary = FEEDBACK_INSUFFICIENT_MESSAGE if generated and feedback.enough_evidence is False else None
    return FeedbackOut(
        id=feedback.id,
        interview_id=feedback.session_id,
        status=FeedbackStatus(feedback.status),
        enough_evidence=feedback.enough_evidence,
        overall=feedback.overall if result else None,
        summary=result.summary if result else summary,
        strengths=result.strengths if result else [],
        improvements=result.improvements if result else [],
        next_steps=result.next_steps if result else [],
        questions=[
            FeedbackQuestionOut(
                main_number=q.main_number,
                category=q.category,
                question=q.question,
                scores=q.scores,
                note=q.note,
                evidence=[FeedbackEvidenceOut(criterion=e.criterion, quote=e.quote, reason=e.reason) for e in q.evidence],
            )
            for q in (result.questions if result else [])
        ],
        rubric_version=feedback.rubric_version,
        created_at=feedback.created_at,
    )
