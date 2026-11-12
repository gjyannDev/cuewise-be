"""Reference notes at interview start: retrieved, stored with the interview, reloaded for answers, given to every
main-question write and never exposed (knowledge-base-rag Steps 8-9; AC13-AC17, AC20, EC8, EC19, EC20).
"""

import uuid

import pytest
from sqlalchemy import select

from app.core.ai.fake import FakeEmbedder
from app.core.ai.provider import LLMServerError
from app.main import app
from app.modules.interviews.constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE
from app.modules.interviews.dependencies.interviews_shared_dependencies import (
    get_embedder,
)
from app.modules.interviews.models.interviews_knowledge_model import (
    InterviewSessionChunk,
)
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.repositories.interviews_repository import (
    InterviewsRepository,
)
from app.modules.interviews.services.interviews_knowledge_service import ingest_corpus
from app.modules.interviews.utils.interviews_knowledge_utils import (
    embedding_text,
    parse_note,
)

JOB = "We build Python REST APIs and need someone who designs them well."


def vec(*head: float) -> list[float]:
    return [*head, *[0.0] * (KNOWLEDGE_VECTOR_SIZE - len(head))]


# Against the job's vector (0.9, 0.1): API design 0.994 > Communication 0.781 > Caching 0.606. All three clear the
# shipped RETRIEVAL_MIN_SIMILARITY (0.55), as related notes do with real embeddings.
NOTES = [
    ("api.md", "backend", "API design", vec(1, 0, 0)),
    ("cache.md", "backend", "Caching", vec(0.6, 1, 0)),
    ("talk.md", "general", "Communication", vec(0.5, 0.5, 0)),
]


@pytest.fixture
def vectors():
    return {JOB: vec(0.9, 0.1, 0)}


@pytest.fixture
def corpus(db, vectors):
    chunks = []
    for name, role, heading, direction in NOTES:
        text = f"---\nroles: {role}\nlevels: junior\nsource: user\n---\n## {heading}\nPrivate note text about {heading}.\n"
        [chunk] = parse_note(name, text).chunks
        chunks.append(chunk._replace(order=len(chunks)))
        vectors[embedding_text(chunk)] = direction
    ingest_corpus(chunks, FakeEmbedder(vectors), KnowledgeRepository(db))


@pytest.fixture
def embedder(vectors):
    fake = FakeEmbedder(vectors)
    app.dependency_overrides[get_embedder] = lambda: fake
    yield fake
    app.dependency_overrides.pop(get_embedder, None)


def stored(db, response) -> list[InterviewSessionChunk]:
    db.expire_all()
    query = select(InterviewSessionChunk).where(InterviewSessionChunk.session_id == session_of(response))
    return list(db.scalars(query.order_by(InterviewSessionChunk.rank)))


def session_of(response) -> uuid.UUID:
    return uuid.UUID(response.json()["session"]["id"])


def retrieval_lines(app_logs) -> list[str]:
    return [r.getMessage() for r in app_logs.records if r.getMessage().startswith("retrieval ")]


def test_a_start_with_a_job_description_stores_ranked_vector_notes_and_returns_none(
    db, make_user, start_interview, llm, corpus, embedder
):  # AC16, AC11
    response = start_interview(make_user(), job_description=JOB)

    assert response.status_code == 201
    rows = stored(db, response)
    assert [(r.rank, r.mode) for r in rows] == [(1, "vector"), (2, "vector"), (3, "vector")]
    first, second = rows[0].score, rows[1].score
    assert first is not None and second is not None and first > second
    assert "Private note text" not in response.text and "reference" not in response.text.lower()


def test_a_start_without_a_job_description_stores_filter_notes_with_no_call(
    db, make_user, start_interview, llm, corpus, embedder
):  # AC13, EC1
    response = start_interview(make_user())

    rows = stored(db, response)
    assert len(rows) == 3 and {r.mode for r in rows} == {"filter"} and all(r.score is None for r in rows)
    assert embedder.calls == []


def test_a_failing_embedder_still_starts_with_filter_notes(
    db, make_user, start_interview, llm, corpus, vectors, app_logs
):  # AC14, EC7
    app.dependency_overrides[get_embedder] = lambda: FakeEmbedder(vectors, errors=[LLMServerError("down")])
    try:
        response = start_interview(make_user(), job_description=JOB)
    finally:
        app.dependency_overrides.pop(get_embedder, None)

    assert response.status_code == 201
    assert {r.mode for r in stored(db, response)} == {"filter"}
    assert any("outcome=retrieval_degraded:embedder_error" in line for line in retrieval_lines(app_logs))


def test_with_the_llm_off_retrieval_is_skipped_and_nothing_is_stored(
    db, make_user, start_interview, corpus, embedder, app_logs
):  # AC15, EC9
    response = start_interview(make_user(), job_description=JOB)

    assert response.status_code == 201
    assert stored(db, response) == [] and embedder.calls == []
    assert any("outcome=retrieval_skipped:llm_off" in line for line in retrieval_lines(app_logs))


def test_an_empty_corpus_starts_as_before(db, make_user, start_interview, llm, embedder, app_logs):  # AC15, EC8
    response = start_interview(make_user(), job_description=JOB)

    assert response.status_code == 201 and stored(db, response) == []
    assert any("outcome=retrieval_skipped:no_match" in line for line in retrieval_lines(app_logs))


def test_two_interviews_keep_their_own_notes(db, make_user, start_interview, llm, corpus, embedder):  # EC19
    first = start_interview(make_user("a@example.com"), job_description=JOB)
    second = start_interview(make_user("b@example.com"))

    assert {r.mode for r in stored(db, first)} == {"vector"}
    assert {r.mode for r in stored(db, second)} == {"filter"}


def test_the_saved_notes_are_reloaded_in_rank_order_for_answer_turns(
    db, make_user, start_interview, llm, corpus, embedder
):  # AC17 (the read side), EC10
    session_id = session_of(start_interview(make_user(), job_description=JOB))

    notes = InterviewsRepository(db).reference_notes(session_id)

    assert [n.competency for n in notes] == ["API design", "Communication", "Caching"]
    assert [n.rank for n in notes] == [1, 2, 3] and notes[0].text == "Private note text about API design."


def test_an_interview_without_stored_notes_reloads_none(db, make_user, start_interview, llm, embedder):  # EC20
    session_id = session_of(start_interview(make_user()))

    assert InterviewsRepository(db).reference_notes(session_id) == []


def test_logs_carry_no_job_description_or_note_text(
    db, make_user, start_interview, llm, corpus, embedder, app_logs
):  # AC20
    start_interview(make_user(), job_description=JOB)

    messages = " ".join(r.getMessage() for r in app_logs.records)
    assert "REST" not in messages and "Private note text" not in messages
    [line] = retrieval_lines(app_logs)
    assert "mode=vector" in line and "count=3" in line and "outcome=ok" in line


# --- which LLM calls see the notes (AC17) ---


def has_notes(messages) -> bool:
    return any("<reference_notes>" in m.content for m in messages)


def started(start_interview, make_user):
    body = start_interview(make_user(), job_description=JOB).json()
    return body["session"]["id"], body["current_question"]["id"]


def test_the_first_question_is_written_with_the_notes(make_user, start_interview, llm, corpus, embedder):  # AC17
    started(start_interview, make_user)

    [first] = llm.fake.calls
    assert has_notes(first) and "interview notes for this role" in first[0].content


def test_the_json_answer_route_writes_the_next_main_question_with_the_notes_but_never_decides_with_them(
    make_user, start_interview, answer, llm, corpus, embedder
):  # AC17
    user = make_user()
    body = start_interview(user, job_description=JOB).json()

    response = answer(user, body["session"]["id"], body["current_question"]["id"])

    assert response.status_code == 201
    assert has_notes(llm.fake.calls[-1])
    assert llm.decide.calls and not any(has_notes(call) for call in llm.decide.calls)


def test_the_streamed_route_writes_the_next_main_question_with_the_notes(
    make_user, start_interview, stream_answer, llm, corpus, embedder
):  # AC17
    user = make_user()
    body = start_interview(user, job_description=JOB).json()

    turn = stream_answer(user, body["session"]["id"], body["current_question"]["id"])

    assert turn.status_code == 200
    assert has_notes(llm.fake.calls[-1]) and "CATEGORY:" in llm.fake.calls[-1][0].content


def test_a_follow_up_is_written_without_the_notes(
    make_user, start_interview, answer, llm, corpus, embedder, decision_json
):  # AC17
    user = make_user()
    body = start_interview(user, job_description=JOB).json()
    llm.script_decide(decision_json("follow_up", "no_example"))
    llm.script('{"question": "Can you give a concrete example of that?"}')

    response = answer(user, body["session"]["id"], body["current_question"]["id"])

    assert response.json()["current_question"]["question_kind"] == "follow_up"
    assert not has_notes(llm.fake.calls[-1])


def test_an_interview_without_notes_never_sends_a_notes_block(
    make_user, start_interview, answer, llm, embedder
):  # AC17, EC20: the empty corpus case
    user = make_user()
    body = start_interview(user, job_description=JOB).json()
    answer(user, body["session"]["id"], body["current_question"]["id"])

    assert not any(has_notes(call) for call in llm.fake.calls)
