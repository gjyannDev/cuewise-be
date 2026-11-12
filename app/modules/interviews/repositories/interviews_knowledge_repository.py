"""Database access for the reference-note corpus. No business rules: which rows to add or retire is the service's job.

Rows are added and retired, never edited: an interview that points at a row keeps exactly the text it started with.
Retrieval reads plain values (not ORM objects), so the service can end the transaction before the slow embedding call
without the rows expiring under it.
"""

import uuid
from collections.abc import Sequence
from typing import NamedTuple

from sqlalchemy import Select, delete, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ..constants.interviews_constants import GENERAL_ROLE
from ..dependencies.models.interviews_knowledge_model import (
    InterviewSessionChunk,
    KnowledgeChunk,
    KnowledgeChunkScope,
)
from ..utils.interviews_knowledge_utils import NoteChunk, cosine_similarity


class EligibleChunk(NamedTuple):
    id: uuid.UUID
    # Stable across environments: the retrieval eval's labels name chunks by it.
    note_key: str
    competency: str
    text: str


_COLUMNS = (KnowledgeChunk.id, KnowledgeChunk.note_key, KnowledgeChunk.competency, KnowledgeChunk.text)


def _eligible(role: str, level: str) -> Select:
    """Active chunks scoped to this role (or every role) and this level. Role and level come from the interview setup
    only, never from the job description."""
    scoped = select(KnowledgeChunkScope.chunk_id).where(
        KnowledgeChunkScope.role.in_([role, GENERAL_ROLE]), KnowledgeChunkScope.level == level
    )
    return select(*_COLUMNS).where(KnowledgeChunk.active, KnowledgeChunk.id.in_(scoped))


class KnowledgeRepository:
    def __init__(self, db: Session):
        self.db = db

    def active_chunks(self) -> list[KnowledgeChunk]:
        return list(
            self.db.scalars(select(KnowledgeChunk).where(KnowledgeChunk.active).order_by(KnowledgeChunk.corpus_order))
        )

    def release(self) -> None:
        """End the read transaction before a slow call (the embedding), so no connection is held while waiting."""
        self.db.rollback()

    def eligible_chunks(self, role: str, level: str) -> list[EligibleChunk]:
        rows = self.db.execute(_eligible(role, level).order_by(KnowledgeChunk.corpus_order))
        return [EligibleChunk(*row) for row in rows]

    def nearest_chunks(
        self, role: str, level: str, model: str, query: Sequence[float], k: int
    ) -> list[tuple[EligibleChunk, float]]:
        """The k eligible chunks embedded with `model` that are most similar to the query, most similar first, with
        their cosine similarity. Postgres ranks inside the query (pgvector's `<=>` is cosine distance = 1 -
        similarity); SQLite (tests) has no vector type, so there the same ranking is done in Python."""
        eligible = _eligible(role, level).where(KnowledgeChunk.embedding_model == model)
        if self.db.get_bind().dialect.name == "postgresql":
            distance = KnowledgeChunk.embedding.cosine_distance(query)
            rows = self.db.execute(
                eligible.add_columns(distance).order_by(distance, KnowledgeChunk.corpus_order).limit(k)
            )
            return [(EligibleChunk(*row[:4]), 1 - row[4]) for row in rows]
        rows = self.db.execute(eligible.add_columns(KnowledgeChunk.embedding).order_by(KnowledgeChunk.corpus_order))
        scored = [(EligibleChunk(*row[:4]), cosine_similarity(row[4], query)) for row in rows]
        # Stable sort: equal scores keep corpus order, as on Postgres.
        return sorted(scored, key=lambda pair: pair[1], reverse=True)[:k]

    def add(
        self, chunk: NoteChunk, embedding: list[float], model: str, *, replaces: KnowledgeChunk | None = None
    ) -> KnowledgeChunk:
        """Store one chunk with its scopes, retiring the row it replaces, in one commit (a crash leaves either both
        changes or neither)."""
        try:
            if replaces is not None:
                replaces.active = False
                # Before the insert: only one active row per note key may exist (a partial unique index).
                self.db.flush()
            row = KnowledgeChunk(
                note_key=chunk.note_key,
                competency=chunk.competency,
                source=chunk.source,
                text=chunk.text,
                content_hash=chunk.content_hash,
                embedding=embedding,
                embedding_model=model,
                corpus_order=chunk.order,
            )
            self.db.add(row)
            self.db.flush()
            self.db.add_all(
                KnowledgeChunkScope(chunk_id=row.id, role=role, level=level)
                for role in chunk.roles
                for level in chunk.levels
            )
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise
        return row

    def retire(self, rows: Sequence[KnowledgeChunk]) -> None:
        for row in rows:
            row.active = False
        self.db.commit()

    def delete_unreferenced_retired(self) -> int:
        """Remove retired rows no interview points at (with their scopes); returns how many."""
        referenced = select(InterviewSessionChunk.chunk_id)
        ids = list(
            self.db.scalars(select(KnowledgeChunk.id).where(~KnowledgeChunk.active, KnowledgeChunk.id.not_in(referenced)))
        )
        if ids:
            # Scopes first: the database cascade would do it, but SQLite (tests) doesn't enforce foreign keys.
            self.db.execute(delete(KnowledgeChunkScope).where(KnowledgeChunkScope.chunk_id.in_(ids)))
            self.db.execute(delete(KnowledgeChunk).where(KnowledgeChunk.id.in_(ids)))
            self.db.commit()
        return len(ids)
