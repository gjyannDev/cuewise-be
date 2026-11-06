import uuid
from datetime import datetime

from sqlalchemy import (
    JSON,
    DateTime,
    ForeignKey,
    Index,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy import text as sql_text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.mixins import UUIDPrimaryKeyMixin
from app.db.session import Base

from .interviews_constants import (
    FIRST_POSITION,
    JOB_DESCRIPTION_MAX_LENGTH,
    NOTE_MAX_LENGTH,
    SUMMARY_MAX_LENGTH,
    QuestionKind,
    QuestionSource,
    SessionStatus,
)

_IN_PROGRESS = sql_text(f"status = '{SessionStatus.in_progress.value}'")


class InterviewSession(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "interview_sessions"
    __table_args__ = (
        # The real guarantee behind "one active interview per user": two concurrent starts can't both win.
        Index(
            "uq_interview_sessions_user_in_progress",
            "user_id",
            unique=True,
            postgresql_where=_IN_PROGRESS,
            sqlite_where=_IN_PROGRESS,
        ),
        # The history list: one user's interviews, newest first (UUIDv7 id order; a btree scans either direction).
        Index("ix_interview_sessions_user_id_id", "user_id", "id"),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    # Plain strings validated by Pydantic enums, so new values need no ALTER TYPE migration (like User.role).
    role: Mapped[str] = mapped_column(String(32))
    level: Mapped[str] = mapped_column(String(32))
    interview_type: Mapped[str] = mapped_column(String(32))
    question_count: Mapped[int]
    job_description: Mapped[str | None] = mapped_column(String(JOB_DESCRIPTION_MAX_LENGTH))
    # Made once at start when the job description is long; sent instead of it on every call. Never returned by the API.
    job_description_summary: Mapped[str | None] = mapped_column(String(SUMMARY_MAX_LENGTH))
    status: Mapped[str] = mapped_column(
        String(32),
        default=SessionStatus.in_progress,
        server_default=SessionStatus.in_progress.value,
    )
    # The question awaiting an answer; only ever moved by the compare-and-swap in the repository.
    current_position: Mapped[int] = mapped_column(default=FIRST_POSITION, server_default=str(FIRST_POSITION))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class InterviewQuestion(UUIDPrimaryKeyMixin, Base):
    """A question as it was shown: written by the LLM, or snapshotted from the bank (so bank edits never change it)."""

    __tablename__ = "interview_questions"
    __table_args__ = (UniqueConstraint("session_id", "position"),)

    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("interview_sessions.id", ondelete="CASCADE"))
    position: Mapped[int]
    text: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(32))
    # Set only for bank questions; it also keeps the fallback from repeating a bank question in one session.
    bank_id: Mapped[str | None] = mapped_column(String(64))
    source: Mapped[str] = mapped_column(
        String(16), default=QuestionSource.bank, server_default=QuestionSource.bank.value
    )
    # Usage of the LLM turn that produced this question (summed over its calls); null for bank questions.
    model: Mapped[str | None] = mapped_column(String(128))
    prompt_version: Mapped[str | None] = mapped_column(String(64))
    prompt_tokens: Mapped[int | None]
    completion_tokens: Mapped[int | None]
    latency_ms: Mapped[int | None]
    # A main question opens a thread; a follow-up points at it and copies its category and main_number.
    kind: Mapped[str] = mapped_column(String(16), default=QuestionKind.main, server_default=QuestionKind.main.value)
    parent_question_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("interview_questions.id", ondelete="CASCADE")
    )
    # "Question 3 of 5": stored so no response has to count rows. Defaults to position (true when there are no
    # follow-ups, as in every session from before them).
    main_number: Mapped[int] = mapped_column(default=lambda ctx: ctx.get_current_parameters()["position"])
    # The decide call's prompt when one ran for the turn that produced this question (prompt_version is the writer's).
    decision_prompt_version: Mapped[str | None] = mapped_column(String(64))


class InterviewMessage(UUIDPrimaryKeyMixin, Base):
    """A candidate answer or the interviewer's reaction to one question.

    The questions themselves live in interview_questions; together they are the whole conversation.
    UUIDv7 ids are time-ordered, so ordering by id is conversation order.
    """

    __tablename__ = "interview_messages"
    # One answer and one reaction per question in this slice; the backstop behind the compare-and-swap.
    __table_args__ = (UniqueConstraint("question_id", "role"),)

    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("interview_sessions.id", ondelete="CASCADE"))
    question_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("interview_questions.id", ondelete="CASCADE"))
    role: Mapped[str] = mapped_column(String(32))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    # Candidate rows only: the model's short running note about this answer (window_ledger sends it for old turns).
    note: Mapped[str | None] = mapped_column(String(NOTE_MAX_LENGTH))
    # LLM call metadata, legacy LLM-written reactions only (predefined reactions leave these null).
    model: Mapped[str | None] = mapped_column(String(128))
    prompt_version: Mapped[str | None] = mapped_column(String(64))
    prompt_tokens: Mapped[int | None]
    completion_tokens: Mapped[int | None]
    latency_ms: Mapped[int | None]


class InterviewFeedback(UUIDPrimaryKeyMixin, Base):
    """The end-of-interview feedback: at most one per interview (the unique session_id is the guarantee).

    Written in steps by the request that holds the claim (`started_at` is the claim token): the scores as soon as the
    score call validates, then the text. Personal data (quotes, text) lives only in `result`, never in a log.
    """

    __tablename__ = "interview_feedback"

    session_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("interview_sessions.id", ondelete="CASCADE"), unique=True
    )
    # FeedbackStatus as a plain string, like the session status.
    status: Mapped[str] = mapped_column(String(16))
    # None until known; False = too little to assess (no scores, final).
    enough_evidence: Mapped[bool | None]
    rubric_version: Mapped[str] = mapped_column(String(64))
    score_prompt_version: Mapped[str | None] = mapped_column(String(64))
    write_prompt_version: Mapped[str | None] = mapped_column(String(64))
    # TextSource: llm or template. Stored for reports, never returned.
    text_source: Mapped[str | None] = mapped_column(String(16))
    # Computed by the code from the scores; a column so later reports can query it.
    overall: Mapped[float | None]
    # StoredResult as JSON: scores, evidence, then the text. Always assigned whole, never edited in place (in-place
    # changes to a JSON value aren't tracked).
    result: Mapped[dict | None] = mapped_column(JSON)
    # Usage per call (summed over its attempts), for cost and latency reports.
    score_model: Mapped[str | None] = mapped_column(String(128))
    score_prompt_tokens: Mapped[int | None]
    score_completion_tokens: Mapped[int | None]
    score_latency_ms: Mapped[int | None]
    write_model: Mapped[str | None] = mapped_column(String(128))
    write_prompt_tokens: Mapped[int | None]
    write_completion_tokens: Mapped[int | None]
    write_latency_ms: Mapped[int | None]
    # A reason code only (e.g. invalid_reply:quote_not_found), never model or user text.
    failure_reason: Mapped[str | None] = mapped_column(String(64))
    # Set by each claim from the app's clock; a `generating` row older than the budget plus a margin may be taken over.
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
