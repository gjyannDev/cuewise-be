import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, UniqueConstraint, func
from sqlalchemy import text as sql_text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.mixins import UUIDPrimaryKeyMixin
from app.db.session import Base

from .interviews_constants import (
    FIRST_POSITION,
    JOB_DESCRIPTION_MAX_LENGTH,
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
    )

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    # Plain strings validated by Pydantic enums, so new values need no ALTER TYPE migration (like User.role).
    role: Mapped[str] = mapped_column(String(32))
    level: Mapped[str] = mapped_column(String(32))
    interview_type: Mapped[str] = mapped_column(String(32))
    question_count: Mapped[int]
    job_description: Mapped[str | None] = mapped_column(String(JOB_DESCRIPTION_MAX_LENGTH))
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
    # LLM call metadata, legacy LLM-written reactions only (predefined reactions leave these null).
    model: Mapped[str | None] = mapped_column(String(128))
    prompt_version: Mapped[str | None] = mapped_column(String(64))
    prompt_tokens: Mapped[int | None]
    completion_tokens: Mapped[int | None]
    latency_ms: Mapped[int | None]
