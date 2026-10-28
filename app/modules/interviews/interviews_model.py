import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, UniqueConstraint, func
from sqlalchemy import text as sql_text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.mixins import UUIDPrimaryKeyMixin
from app.db.session import Base

from .interviews_constants import JOB_DESCRIPTION_MAX_LENGTH, SessionStatus

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
        String(32), default=SessionStatus.in_progress, server_default=SessionStatus.in_progress.value
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class InterviewQuestion(UUIDPrimaryKeyMixin, Base):
    """A snapshot of a bank question, so later bank edits never change an existing session."""

    __tablename__ = "interview_questions"
    __table_args__ = (UniqueConstraint("session_id", "position"),)

    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("interview_sessions.id", ondelete="CASCADE"))
    position: Mapped[int]
    text: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(32))
    bank_id: Mapped[str] = mapped_column(String(64))
