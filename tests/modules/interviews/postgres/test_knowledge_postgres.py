"""Opt-in: the knowledge-base migration and pgvector on a real Postgres (knowledge-base-rag Step 4; AC16, AC21, EC21).

The normal suite runs on SQLite, which has no vector type and doesn't enforce foreign keys, so these checks need the
pgvector Docker database. They migrate it to head, downgrade this feature's revision and upgrade again, so point
TEST_POSTGRES_URL at a throwaway database, never the dev one:

    TEST_POSTGRES_URL=postgresql+psycopg://postgres:postgres_236@127.0.0.1:5433/cuewise_test uv run pytest -m postgres
"""

import os
import random
import uuid
from pathlib import Path

import pytest
from alembic.config import Config
from sqlalchemy import create_engine, delete, inspect, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from alembic import command
from app.core import config as app_config
from app.modules.auth.models.auth_model import User
from app.modules.interviews.constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE
from app.modules.interviews.dependencies.models.interviews_knowledge_model import (
    InterviewSessionChunk,
    KnowledgeChunk,
)
from app.modules.interviews.dependencies.models.interviews_model import InterviewSession
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.utils.interviews_knowledge_utils import (
    cosine_similarity,
    parse_note,
)

URL = os.getenv("TEST_POSTGRES_URL", "")
PREVIOUS_REVISION = "f5c2a9d84b17"
TABLES = {"knowledge_chunks", "knowledge_chunk_scopes", "interview_session_chunks"}

pytestmark = [
    pytest.mark.postgres,
    pytest.mark.skipif(not URL, reason="set TEST_POSTGRES_URL to a throwaway pgvector database"),
]


@pytest.fixture(scope="module")
def alembic_config():
    with pytest.MonkeyPatch.context() as patch:
        # alembic/env.py reads the URL from the app settings.
        patch.setattr(app_config.settings, "database_url", URL)
        cfg = Config(str(Path(__file__).resolve().parents[4] / "alembic.ini"))
        command.upgrade(cfg, "head")
        yield cfg


@pytest.fixture
def session(alembic_config):
    engine = create_engine(URL)
    with Session(engine) as db:
        yield db
        db.rollback()
    engine.dispose()


def make_chunk(db: Session) -> KnowledgeChunk:
    row = KnowledgeChunk(
        note_key=f"test-{uuid.uuid7()}.md#Section",
        competency="Section",
        source="drafted",
        text="A test note.",
        content_hash="b" * 64,
        embedding=[0.25] * KNOWLEDGE_VECTOR_SIZE,
        embedding_model="fake-embedding",
        corpus_order=0,
    )
    db.add(row)
    db.flush()
    return row


def make_session(db: Session) -> InterviewSession:
    user = User(email=f"{uuid.uuid7()}@example.com", password_hash="x", role="user")
    db.add(user)
    db.flush()
    interview = InterviewSession(
        user_id=user.id, role="backend", level="mid", interview_type="technical", question_count=3
    )
    db.add(interview)
    db.flush()
    return interview


def test_the_migration_creates_and_drops_the_tables_and_keeps_the_extension(alembic_config):  # AC16
    engine = create_engine(URL)
    try:
        assert TABLES <= set(inspect(engine).get_table_names())
        command.downgrade(alembic_config, PREVIOUS_REVISION)
        assert not TABLES & set(inspect(engine).get_table_names())
        with engine.connect() as connection:
            assert connection.exec_driver_sql("SELECT 1 FROM pg_extension WHERE extname = 'vector'").scalar() == 1
    finally:
        command.upgrade(alembic_config, "head")
        engine.dispose()


def test_a_vector_round_trips_as_pgvector(session):  # AC16
    row = make_chunk(session)
    session.expire_all()

    assert session.get(KnowledgeChunk, row.id).embedding == [0.25] * KNOWLEDGE_VECTOR_SIZE


def test_deleting_an_interview_deletes_its_note_references_and_keeps_the_note(session):  # AC21, EC21
    note = make_chunk(session)
    interview = make_session(session)
    session.add(InterviewSessionChunk(session_id=interview.id, chunk_id=note.id, rank=1, score=0.8, mode="vector"))
    session.flush()

    session.execute(delete(InterviewSession).where(InterviewSession.id == interview.id))
    session.expire_all()

    assert session.scalars(select(InterviewSessionChunk).where(InterviewSessionChunk.chunk_id == note.id)).all() == []
    assert session.get(KnowledgeChunk, note.id) is not None


def test_a_note_an_interview_points_at_cannot_be_deleted(session):  # AC7
    note = make_chunk(session)
    interview = make_session(session)
    session.add(InterviewSessionChunk(session_id=interview.id, chunk_id=note.id, rank=1, score=None, mode="filter"))
    session.flush()

    with pytest.raises(IntegrityError):
        session.execute(delete(KnowledgeChunk).where(KnowledgeChunk.id == note.id))


def test_pgvector_ranks_like_the_python_cosine_used_on_sqlite(session):  # Step 7: the real `<=>` path
    rng = random.Random(7)
    # A level of its own keeps this test's rows apart from anything else in the database. The column holds 32
    # characters and SQLite never checks that, so keep the name short.
    level = f"test-{uuid.uuid7().hex[-20:]}"
    repo = KnowledgeRepository(session)
    for i in range(12):
        [chunk] = parse_note(f"rank-{i}.md", f"---\nroles: backend\nlevels: mid\nsource: user\n---\n## N{i}\nx\n").chunks
        vector = [rng.uniform(-1, 1) for _ in range(KNOWLEDGE_VECTOR_SIZE)]
        repo.add(chunk._replace(note_key=f"{level}-{i}", levels=(level,), order=i), vector, "fake-embedding")
    query = [rng.uniform(-1, 1) for _ in range(KNOWLEDGE_VECTOR_SIZE)]

    from_postgres = repo.nearest_chunks("backend", level, "fake-embedding", query, 6)
    rows = session.execute(select(KnowledgeChunk.id, KnowledgeChunk.embedding).where(KnowledgeChunk.note_key.like(f"{level}-%")))
    in_python = sorted(((cosine_similarity(v, query), i) for i, v in rows), reverse=True)[:6]

    assert [chunk.id for chunk, _ in from_postgres] == [i for _, i in in_python]
    assert [score for _, score in from_postgres] == pytest.approx([s for s, _ in in_python], abs=1e-5)
