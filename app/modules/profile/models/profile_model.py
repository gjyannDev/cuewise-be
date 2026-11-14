import uuid
from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.mixins import UUIDPrimaryKeyMixin
from app.db.session import Base


class CandidateProfileRow(UUIDPrimaryKeyMixin, Base):
    """A user's résumé profile: at most one per user (the unique user_id is the guarantee), replaced on re-upload.

    Only the extracted profile is stored. There is no column for the file, its name, its raw or scrubbed text: those
    exist only in memory during the upload (resume-upload AC11).
    """

    __tablename__ = "candidate_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    # CandidateProfile as JSON; always assigned whole (in-place edits of a JSON value aren't tracked).
    profile: Mapped[dict] = mapped_column(JSON)
    prompt_version: Mapped[str] = mapped_column(String(64))
    model: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
