"""Knowledge-base tables and the portable vector column (knowledge-base-rag Step 4; AC16, AC21, EC21).

SQLite does not enforce foreign keys here, so the cascade is checked on the declared schema; the opt-in Postgres test
(tests/modules/interviews/postgres/) checks it on a real database after the migration.
"""

import uuid

import pytest
from sqlalchemy import select
from sqlalchemy.dialects import postgresql
from sqlalchemy.exc import IntegrityError

from app.modules.interviews.constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE
from app.modules.interviews.models.interviews_knowledge_model import (
    InterviewSessionChunk,
    KnowledgeChunk,
    KnowledgeChunkScope,
)


def chunk(note_key="backend-api.md#Error handling", *, active=True, order=0) -> KnowledgeChunk:
    return KnowledgeChunk(
        note_key=note_key,
        competency="Error handling",
        source="drafted",
        text="Probe how they map failures to status codes.",
        content_hash="a" * 64,
        embedding=[0.5] * KNOWLEDGE_VECTOR_SIZE,
        embedding_model="fake-embedding",
        active=active,
        corpus_order=order,
    )


def test_deleting_an_interview_deletes_its_note_references_but_never_the_notes():  # AC21, EC21
    [session_fk] = InterviewSessionChunk.__table__.c.session_id.foreign_keys
    [chunk_fk] = InterviewSessionChunk.__table__.c.chunk_id.foreign_keys

    assert session_fk.column.table.name == "interview_sessions" and session_fk.ondelete == "CASCADE"
    assert chunk_fk.column.table.name == "knowledge_chunks" and chunk_fk.ondelete is None


def test_scopes_go_with_their_chunk():  # inferred: removing an unreferenced retired chunk leaves no orphans
    [fk] = KnowledgeChunkScope.__table__.c.chunk_id.foreign_keys

    assert fk.ondelete == "CASCADE"


def test_the_vector_column_is_pgvector_on_postgres():  # AC16: the real `<=>` path needs the real type
    column_type = KnowledgeChunk.__table__.c.embedding.type

    assert column_type.dialect_impl(postgresql.dialect()).compile(dialect=postgresql.dialect()) == "VECTOR(768)"


def test_a_vector_round_trips_through_the_portable_column_on_sqlite(db):  # AC16
    vector = [i / KNOWLEDGE_VECTOR_SIZE for i in range(KNOWLEDGE_VECTOR_SIZE)]
    row = chunk()
    row.embedding = vector
    db.add(row)
    db.commit()
    db.expire_all()

    stored = db.scalars(select(KnowledgeChunk)).one()
    assert stored.embedding == vector
    assert isinstance(stored.id, uuid.UUID) and stored.id.version == 7
    assert stored.active is True


def test_only_one_active_row_per_note_key_but_retired_versions_may_share_it(db):  # AC7: a changed section is a new row
    db.add_all([chunk(active=False), chunk(active=False, order=1), chunk(order=2)])
    db.commit()

    db.add(chunk(order=3))
    with pytest.raises(IntegrityError):
        db.commit()
