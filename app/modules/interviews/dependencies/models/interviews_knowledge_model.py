"""The reference-note corpus (knowledge-base RAG) and the notes each interview was given.

A note file is split by heading into chunks; each chunk is one row here, with its vector (its "embedding": the text
as a list of numbers, so meaning can be compared). Rows are never edited once an interview references them: a changed
section becomes a new row and the old one is retired, so an interview keeps the exact notes it started with.
"""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, UniqueConstraint, func
from sqlalchemy import text as sql_text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.mixins import UUIDPrimaryKeyMixin
from app.db.session import Base
from app.db.types import portable_vector

from ...constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE

_ACTIVE = sql_text("active")


class KnowledgeChunk(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "knowledge_chunks"
    __table_args__ = (
        # One active row per note section; retired versions may share the key (interviews still point at them).
        Index(
            "uq_knowledge_chunks_active_note_key",
            "note_key",
            unique=True,
            postgresql_where=_ACTIVE,
            sqlite_where=_ACTIVE,
        ),
    )

    # Stable across environments ("backend-api-design.md#Error handling"): eval labels name chunks by it, not by id.
    note_key: Mapped[str] = mapped_column(String(255))
    # The section heading: what this chunk helps the writer probe.
    competency: Mapped[str] = mapped_column(String(128))
    # NoteSource as a plain string, like the session status.
    source: Mapped[str] = mapped_column(String(16))
    text: Mapped[str] = mapped_column(Text)
    # sha256 of the header values and the section text: unchanged hash = no embedding call on re-ingest.
    content_hash: Mapped[str] = mapped_column(String(64))
    embedding: Mapped[list[float]] = mapped_column(portable_vector(KNOWLEDGE_VECTOR_SIZE))
    # Vectors from different models can't be compared: vector mode uses only rows of the configured model.
    embedding_model: Mapped[str] = mapped_column(String(128))
    # False once the section changed or its note was removed; retired rows are never retrieved again.
    active: Mapped[bool] = mapped_column(default=True, server_default=sql_text("true"))
    # Position in the corpus (file, then section), so filter mode and reports have a stable order.
    corpus_order: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class KnowledgeChunkScope(UUIDPrimaryKeyMixin, Base):
    """One (role, level) a chunk applies to. Rows instead of array columns, so the filter is plain SQL everywhere."""

    __tablename__ = "knowledge_chunk_scopes"
    __table_args__ = (
        UniqueConstraint("chunk_id", "role", "level"),
        # The retrieval filter: role IN (the interview's role, 'general') AND level = the interview's level.
        Index("ix_knowledge_chunk_scopes_level_role", "level", "role"),
    )

    chunk_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("knowledge_chunks.id", ondelete="CASCADE"))
    # A JobRole value or GENERAL_ROLE.
    role: Mapped[str] = mapped_column(String(32))
    level: Mapped[str] = mapped_column(String(32))


class InterviewSessionChunk(UUIDPrimaryKeyMixin, Base):
    """A reference note one interview was given at start: the same notes for every main question of it."""

    __tablename__ = "interview_session_chunks"
    __table_args__ = (
        UniqueConstraint("session_id", "rank"),
        # Ingestion asks "is this chunk referenced by any interview?" before it removes a retired row.
        Index("ix_interview_session_chunks_chunk_id", "chunk_id"),
    )

    # Deleting an interview deletes its references; the notes themselves stay.
    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("interview_sessions.id", ondelete="CASCADE"))
    # No cascade: a chunk an interview points at can't be deleted.
    chunk_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("knowledge_chunks.id"))
    # 1 = most relevant.
    rank: Mapped[int]
    # Cosine similarity in vector mode; None in filter mode (nothing was compared).
    score: Mapped[float | None]
    # RetrievalMode as a plain string.
    mode: Mapped[str] = mapped_column(String(16))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
