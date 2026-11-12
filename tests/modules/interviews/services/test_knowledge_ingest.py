"""ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag Step 6; AC6-AC8, EC10-EC15)."""

import logging

import pytest
from sqlalchemy import select

from app.core.ai.embedder import EmbeddingKind
from app.core.ai.fake import FakeEmbedder
from app.core.ai.provider import LLMServerError
from app.modules.interviews.constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE
from app.modules.interviews.dependencies.models.interviews_knowledge_model import (
    InterviewSessionChunk,
    KnowledgeChunk,
    KnowledgeChunkScope,
)
from app.modules.interviews.dependencies.models.interviews_model import InterviewSession
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.services.interviews_knowledge_service import (
    IngestError,
    ingest_corpus,
)
from app.modules.interviews.utils.interviews_knowledge_utils import (
    NoteChunk,
    parse_note,
)

HEADER = "---\nroles: backend, general\nlevels: mid\nsource: user\n---\n"
NOTE = HEADER + "## Error handling\nStatus codes and retries.\n## API design\nVersioning.\n"


def chunks(text: str = NOTE, name: str = "api.md") -> list[NoteChunk]:
    return parse_note(name, text).chunks


def corpus(*notes: tuple[str, str]) -> list[NoteChunk]:
    found = [chunk for name, text in notes for chunk in chunks(text, name)]
    return [chunk._replace(order=i) for i, chunk in enumerate(found)]


def rows(db) -> list[KnowledgeChunk]:
    return list(db.scalars(select(KnowledgeChunk).order_by(KnowledgeChunk.corpus_order, KnowledgeChunk.id)))


def active(db) -> dict[str, KnowledgeChunk]:
    return {row.note_key: row for row in rows(db) if row.active}


def run(db, notes, embedder=None, **kwargs):
    return ingest_corpus(notes, embedder or FakeEmbedder(), KnowledgeRepository(db), **kwargs)


class FailingOn(FakeEmbedder):
    """Fails on the n-th embed call (1-based), then works again."""

    def __init__(self, n: int):
        super().__init__()
        self.n = n
        self.attempts = 0

    def embed(self, texts, *, kind, budget_seconds=None):
        self.attempts += 1
        if self.attempts == self.n:
            raise LLMServerError("down")
        return super().embed(texts, kind=kind, budget_seconds=budget_seconds)


def interview(db, make_user) -> InterviewSession:
    user = make_user()
    session = InterviewSession(user_id=user.id, role="backend", level="mid", interview_type="technical", question_count=3)
    db.add(session)
    db.commit()
    return session


def test_a_first_run_embeds_every_chunk_as_a_document_and_stores_it_with_its_scopes(db):  # AC6, AC10
    embedder = FakeEmbedder()

    counts = run(db, corpus(("api.md", NOTE)), embedder)

    assert counts == (2, 0, 0, 0, 0)
    assert [(c.kind, c.texts) for c in embedder.calls] == [
        (EmbeddingKind.document, ("Error handling\nStatus codes and retries.",)),
        (EmbeddingKind.document, ("API design\nVersioning.",)),
    ]
    stored = rows(db)
    assert [(r.note_key, r.competency, r.source, r.corpus_order, r.active) for r in stored] == [
        ("api.md#Error handling", "Error handling", "user", 0, True),
        ("api.md#API design", "API design", "user", 1, True),
    ]
    assert all(len(r.embedding) == KNOWLEDGE_VECTOR_SIZE and r.embedding_model == "fake-embedding" for r in stored)
    scopes = {(s.role, s.level) for s in db.scalars(select(KnowledgeChunkScope).where(KnowledgeChunkScope.chunk_id == stored[0].id))}
    assert scopes == {("backend", "mid"), ("general", "mid")}


def test_a_second_run_on_an_unchanged_corpus_makes_no_call_and_changes_no_row(db):  # AC6, EC11
    run(db, corpus(("api.md", NOTE)))
    before = [(r.id, r.content_hash, r.active) for r in rows(db)]
    embedder = FakeEmbedder()

    counts = run(db, corpus(("api.md", NOTE)), embedder)

    assert counts == (0, 0, 2, 0, 0)
    assert embedder.calls == []
    assert [(r.id, r.content_hash, r.active) for r in rows(db)] == before


def test_editing_one_section_embeds_exactly_that_chunk_and_replaces_its_row(db):  # AC6, AC7
    run(db, corpus(("api.md", NOTE)))
    old_id = active(db)["api.md#API design"].id
    embedder = FakeEmbedder()

    counts = run(db, corpus(("api.md", NOTE.replace("Versioning.", "Versioning and deprecation."))), embedder)

    assert counts == (0, 1, 1, 0, 1)  # the old row was referenced by nothing, so it is deleted at the end
    assert [c.texts for c in embedder.calls] == [("API design\nVersioning and deprecation.",)]
    new = active(db)["api.md#API design"]
    assert new.id != old_id and new.text == "Versioning and deprecation."
    assert len(rows(db)) == 2


def test_a_row_an_interview_points_at_is_kept_unchanged_when_its_section_changes(db, make_user):  # AC7, EC10
    run(db, corpus(("api.md", NOTE)))
    old = active(db)["api.md#API design"]
    old_id, old_text = old.id, old.text
    db.add(InterviewSessionChunk(session_id=interview(db, make_user).id, chunk_id=old_id, rank=1, mode="filter"))
    db.commit()

    counts = run(db, corpus(("api.md", NOTE.replace("Versioning.", "Versioning and deprecation."))))

    assert counts == (0, 1, 1, 0, 0)
    db.expire_all()
    kept = db.get(KnowledgeChunk, old_id)
    assert kept is not None and kept.active is False and kept.text == old_text
    assert active(db)["api.md#API design"].id != old_id


def test_a_removed_note_is_retired_and_unreferenced_rows_are_deleted(db, make_user):  # EC12
    other = HEADER + "## Caching\nWhen to cache.\n"
    run(db, corpus(("api.md", NOTE), ("cache.md", other)))
    kept_id = active(db)["api.md#Error handling"].id
    db.add(InterviewSessionChunk(session_id=interview(db, make_user).id, chunk_id=kept_id, rank=1, mode="filter"))
    db.commit()

    counts = run(db, corpus(("cache.md", other)))

    assert counts == (0, 0, 1, 2, 1)
    assert set(active(db)) == {"cache.md#Caching"}
    assert {r.id for r in rows(db) if not r.active} == {kept_id}
    orphans = db.scalars(select(KnowledgeChunkScope).where(KnowledgeChunkScope.chunk_id.not_in([r.id for r in rows(db)])))
    assert list(orphans) == []


def test_a_failure_partway_keeps_what_was_stored_and_a_rerun_finishes(db):  # EC13
    notes = corpus(("api.md", NOTE), ("cache.md", HEADER + "## Caching\nWhen to cache.\n"))

    with pytest.raises(IngestError) as caught:
        run(db, notes, FailingOn(2))

    assert str(caught.value).startswith("api.md#API design:")
    assert set(active(db)) == {"api.md#Error handling"}
    assert run(db, notes) == (2, 0, 1, 0, 0)


def test_an_embedder_of_another_size_is_refused_before_any_write(db):  # AC8, EC14
    embedder = FakeEmbedder(dimensions=KNOWLEDGE_VECTOR_SIZE // 2)

    with pytest.raises(IngestError, match="migration"):
        run(db, corpus(("api.md", NOTE)), embedder)

    assert embedder.calls == [] and rows(db) == []


def test_a_returned_vector_of_the_wrong_size_writes_nothing_for_it(db):  # EC14
    embedder = FakeEmbedder({"Error handling\nStatus codes and retries.": [0.1, 0.2]})

    with pytest.raises(IngestError, match=r"^api\.md#Error handling:"):
        run(db, corpus(("api.md", NOTE)), embedder)

    assert rows(db) == []


def test_rows_of_another_model_are_re_embedded(db):  # AC8, EC15
    run(db, corpus(("api.md", NOTE)), FakeEmbedder(model="old-model"))

    counts = run(db, corpus(("api.md", NOTE)), FakeEmbedder(model="new-model"))

    assert counts == (0, 2, 0, 0, 2)
    assert {r.embedding_model for r in rows(db)} == {"new-model"}


def test_calls_are_paced_and_logged_without_text(db, app_logs):  # free-tier pacing; AC20
    waits: list[float] = []

    run(db, corpus(("api.md", NOTE)), pause_seconds=1.5, sleep=waits.append)

    assert waits == [1.5]
    lines = [r.getMessage() for r in app_logs.records if r.getMessage().startswith("embedding_call")]
    assert len(lines) == 2
    assert all("purpose=ingest" in line and "model=fake-embedding" in line and "outcome=ok" in line for line in lines)
    assert not any("Status codes" in r.getMessage() or "Versioning" in r.getMessage() for r in app_logs.records)


def test_a_failed_call_is_logged_with_its_error_type(db, app_logs):
    with pytest.raises(IngestError):
        run(db, corpus(("api.md", NOTE)), FailingOn(1))

    [line] = [r for r in app_logs.records if r.getMessage().startswith("embedding_call")]
    assert line.levelno == logging.WARNING and "outcome=LLMServerError" in line.getMessage()
