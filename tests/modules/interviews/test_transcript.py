import uuid

import pytest

from app.core.ai.provider import LLMTimeoutError
from app.main import app

MESSAGES = "/api/v1/interviews/{}/messages"


@pytest.fixture
def started(make_user, start_interview):
    owner = make_user(email="owner@example.com")
    created = start_interview(owner, question_count=3).json()
    return owner, created["session"]["id"], created["current_question"]


@pytest.fixture
def transcript(client, auth_header):
    def _get(user, session_id):
        return client.get(MESSAGES.format(session_id), headers=auth_header(user))

    return _get


def shape(items):
    return [(i["position"], i["role"], i["kind"]) for i in items]


def test_fresh_session_shows_only_the_first_question(transcript, started):  # EC27, AC23
    owner, session_id, q1 = started

    r = transcript(owner, session_id)

    assert r.status_code == 200
    [item] = r.json()["items"]
    assert item == {
        "id": q1["id"],
        "question_id": q1["id"],
        "position": 1,
        "role": "interviewer",
        "kind": "question",
        "text": q1["text"],
        "created_at": None,
    }


def test_answered_turns_come_back_in_conversation_order(transcript, answer, started, llm):  # AC23, concept 2
    owner, session_id, q1 = started
    llm.script("Reaction one.", "Reaction two.")
    q2 = answer(owner, session_id, q1["id"], text="Answer one.").json()["current_question"]
    answer(owner, session_id, q2["id"], text="Answer two.")

    items = transcript(owner, session_id).json()["items"]

    assert shape(items) == [
        (1, "interviewer", "question"),
        (1, "candidate", "answer"),
        (1, "interviewer", "reaction"),
        (2, "interviewer", "question"),
        (2, "candidate", "answer"),
        (2, "interviewer", "reaction"),
        (3, "interviewer", "question"),
    ]
    assert [i["text"] for i in items[1:3]] == ["Answer one.", "Reaction one."]
    assert all(i["created_at"] for i in items if i["kind"] != "question")
    assert len({i["question_id"] for i in items}) == 3


def test_missing_reaction_has_no_item_and_no_placeholder(transcript, answer, started, llm):  # EC28
    owner, session_id, q1 = started
    llm.script(LLMTimeoutError("slow"))
    answer(owner, session_id, q1["id"])

    items = transcript(owner, session_id).json()["items"]

    assert shape(items) == [(1, "interviewer", "question"), (1, "candidate", "answer"), (2, "interviewer", "question")]


def test_transcript_never_leaks_future_questions_or_internals(transcript, answer, started, llm):  # AC25
    owner, session_id, q1 = started
    answer(owner, session_id, q1["id"])

    r = transcript(owner, session_id)

    assert max(i["position"] for i in r.json()["items"]) == 2
    for leaked in ("bank_id", "prompt_tokens", "completion_tokens", "latency_ms", "prompt_version", "fake-model"):
        assert leaked not in r.text


def test_completed_session_shows_every_question(transcript, answer, started, llm):  # EC30, AC23
    owner, session_id, current = started
    for _ in range(3):
        current = answer(owner, session_id, current["id"]).json()["current_question"]

    items = transcript(owner, session_id).json()["items"]

    assert len(items) == 9
    assert shape(items)[-1] == (3, "interviewer", "reaction")


def test_abandoned_session_stops_where_it_was_left(transcript, answer, start_interview, started):  # EC30, AC24
    owner, session_id, q1 = started
    answer(owner, session_id, q1["id"])
    start_interview(owner)

    r = transcript(owner, session_id)

    assert r.status_code == 200
    assert shape(r.json()["items"]) == [
        (1, "interviewer", "question"),
        (1, "candidate", "answer"),
        (2, "interviewer", "question"),
    ]


def test_missing_and_foreign_sessions_are_the_same_404(transcript, make_user, started):  # EC29, AC24
    _, session_id, _ = started
    stranger = make_user(email="stranger@example.com")

    foreign, missing = transcript(stranger, session_id), transcript(stranger, uuid.uuid7())

    assert foreign.status_code == missing.status_code == 404
    assert {**foreign.json()["error"], "request_id": None} == {**missing.json()["error"], "request_id": None}


def test_auth_and_validation_errors(client, auth_header, make_user, started):  # EC29, AC24
    _, session_id, _ = started
    outsider = make_user(email="odd@example.com", role="superuser")

    assert client.get(MESSAGES.format(session_id)).status_code == 401
    assert client.get(MESSAGES.format(session_id), headers=auth_header(outsider)).status_code == 403
    owner_header = auth_header(started[0])
    assert client.get(MESSAGES.format("not-a-uuid"), headers=owner_header).status_code == 422


def test_transcript_route_documents_its_error_responses():  # AC25
    responses = app.openapi()["paths"]["/api/v1/interviews/{session_id}/messages"]["get"]["responses"]

    for status in ("401", "403", "404", "422"):
        assert responses[status]["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorResponse")
