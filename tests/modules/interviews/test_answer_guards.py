import uuid

import pytest
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from app.main import app
from app.modules.interviews.interviews_model import InterviewMessage, InterviewQuestion, InterviewSession
from app.modules.interviews.interviews_repository import InterviewsRepository

INTERVIEWS = "/api/v1/interviews"
MESSAGES = "/api/v1/interviews/{}/messages"


def message_count(db) -> int:
    return db.scalar(select(func.count()).select_from(InterviewMessage))


@pytest.fixture
def started(make_user, start_interview):
    """An owner with a started 3-question interview: (owner, session_id, first question)."""
    owner = make_user(email="owner@example.com")
    created = start_interview(owner, question_count=3).json()
    return owner, created["session"]["id"], created["current_question"]


def test_no_or_bad_token_is_401(client, db, started):  # EC1
    _, session_id, q1 = started
    body = {"question_id": q1["id"], "answer": "hi"}

    assert client.post(MESSAGES.format(session_id), json=body).json()["error"]["code"] == "TOKEN_MISSING"
    bad = client.post(MESSAGES.format(session_id), json=body, headers={"Authorization": "Bearer nope"})
    assert bad.status_code == 401


def test_caller_without_answer_permission_is_403(client, auth_header, make_user, started):  # EC2
    _, session_id, q1 = started
    outsider = make_user(email="odd@example.com", role="superuser")

    r = client.post(
        MESSAGES.format(session_id), json={"question_id": q1["id"], "answer": "hi"}, headers=auth_header(outsider)
    )

    assert r.status_code == 403


def test_missing_and_foreign_sessions_are_the_same_404(answer, make_user, started, db, llm):  # EC3, AC6
    _, session_id, q1 = started
    stranger = make_user(email="stranger@example.com")

    foreign = answer(stranger, session_id, q1["id"])
    missing = answer(stranger, uuid.uuid7(), q1["id"])

    assert foreign.status_code == missing.status_code == 404
    assert {**foreign.json()["error"], "request_id": None} == {**missing.json()["error"], "request_id": None}
    assert message_count(db) == 0
    assert llm.fake.calls == []


@pytest.mark.parametrize(
    ("overrides", "bad_session"),
    [
        ({"question_id": "not-a-uuid"}, False),
        ({}, True),
        ({"answer": ""}, False),
        ({"answer": "   \n\t "}, False),
        ({"answer": "x" * 2001}, False),
        ({"status": "completed"}, False),
        ({"role": "interviewer"}, False),
    ],
    ids=["bad-question-id", "bad-session-id", "empty", "whitespace", "too-long", "extra-status", "extra-role"],
)
def test_invalid_input_is_422_and_saves_nothing(
    client, auth_header, started, db, overrides, bad_session
):  # EC4-EC7, AC5
    owner, session_id, q1 = started
    body = {"question_id": q1["id"], "answer": "fine"} | overrides
    url = MESSAGES.format("not-a-uuid" if bad_session else session_id)

    r = client.post(url, json=body, headers=auth_header(owner))

    assert r.status_code == 422
    assert r.json()["error"]["code"] == "VALIDATION_ERROR"
    assert message_count(db) == 0


def test_missing_answer_field_is_422(client, auth_header, started):  # EC5
    owner, session_id, q1 = started

    r = client.post(MESSAGES.format(session_id), json={"question_id": q1["id"]}, headers=auth_header(owner))

    assert r.status_code == 422


def test_answer_of_exactly_2000_characters_is_accepted_after_trimming(answer, started):  # EC6
    owner, session_id, q1 = started

    assert answer(owner, session_id, q1["id"], text="  " + "x" * 2000 + "  ").status_code == 201


@pytest.mark.parametrize("ending", ["abandoned", "completed"])
def test_session_not_in_progress_is_409_and_nothing_happens(
    answer, start_interview, started, db, llm, ending
):  # EC8, AC7
    owner, session_id, q1 = started
    if ending == "abandoned":
        start_interview(owner)
    else:
        db.get(InterviewSession, uuid.UUID(session_id)).status = "completed"
        db.commit()
    before = message_count(db)

    r = answer(owner, session_id, q1["id"])

    assert r.status_code == 409
    assert r.json()["error"]["code"] == "SESSION_NOT_IN_PROGRESS"
    assert message_count(db) == before
    assert llm.fake.calls == []


def test_any_question_but_the_current_one_is_the_same_409(
    answer, start_interview, make_user, started, db, llm
):  # EC9, AC7
    owner, session_id, q1 = started
    q2 = answer(owner, session_id, q1["id"]).json()["current_question"]
    llm.script()  # fresh fake: count only calls made from here on
    other_user = make_user(email="other@example.com")
    foreign_q = start_interview(other_user).json()["current_question"]
    before = message_count(db)

    candidates = {
        "stale": q1["id"],
        "foreign": foreign_q["id"],
        "random": str(uuid.uuid7()),
    }
    responses = {name: answer(owner, session_id, qid) for name, qid in candidates.items()}

    assert {r.status_code for r in responses.values()} == {409}
    bodies = {name: {**r.json()["error"], "request_id": None} for name, r in responses.items()}
    assert len({str(b) for b in bodies.values()}) == 1
    assert bodies["stale"]["code"] == "QUESTION_NOT_CURRENT"
    assert message_count(db) == before
    assert llm.fake.calls == []
    assert q2["position"] == 2


def test_a_future_question_is_not_current_either(answer, started, db):  # EC9
    owner, session_id, q1 = started
    answer(owner, session_id, q1["id"])  # now on question 2
    q3 = db.scalar(
        select(InterviewQuestion).where(
            InterviewQuestion.session_id == uuid.UUID(session_id), InterviewQuestion.position == 3
        )
    )

    r = answer(owner, session_id, q3.id)

    assert r.status_code == 409
    assert r.json()["error"]["code"] == "QUESTION_NOT_CURRENT"
    assert db.get(InterviewSession, uuid.UUID(session_id)).current_position == 2


def test_submitting_the_same_question_twice_stores_one_answer(answer, started, db, llm):  # EC10, AC8
    owner, session_id, q1 = started

    first = answer(owner, session_id, q1["id"], text="first click")
    second = answer(owner, session_id, q1["id"], text="second click")

    assert first.status_code == 201
    assert second.status_code == 409
    assert second.json()["error"]["code"] == "QUESTION_NOT_CURRENT"
    rows = db.scalars(select(InterviewMessage).where(InterviewMessage.role == "candidate")).all()
    assert [r.content for r in rows] == ["first click"]
    assert len(llm.fake.calls) == 1


def test_lost_race_on_the_advance_saves_nothing(
    make_user, start_interview, db
):  # EC10, AC8: the compare-and-swap itself
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session = db.get(InterviewSession, uuid.UUID(created["session"]["id"]))
    question_id = uuid.UUID(created["current_question"]["id"])
    repo = InterviewsRepository(db)

    def candidate(text):
        return InterviewMessage(session_id=session.id, question_id=question_id, role="candidate", content=text)

    assert repo.record_answer(candidate("winner"), expected_position=1, completes=False) is True
    # The loser read position 1 before the winner committed; its conditional update now matches no row.
    assert repo.record_answer(candidate("loser"), expected_position=1, completes=False) is False

    assert db.get(InterviewSession, session.id).current_position == 2
    assert [m.content for m in db.scalars(select(InterviewMessage))] == ["winner"]


def test_database_rejects_a_second_answer_for_one_question(make_user, start_interview, db):  # EC10 backstop
    owner = make_user()
    created = start_interview(owner).json()
    session_id, question_id = uuid.UUID(created["session"]["id"]), uuid.UUID(created["current_question"]["id"])

    db.add_all(
        [
            InterviewMessage(session_id=session_id, question_id=question_id, role="candidate", content="a"),
            InterviewMessage(session_id=session_id, question_id=question_id, role="candidate", content="b"),
        ]
    )
    with pytest.raises(IntegrityError):
        db.commit()
    db.rollback()


def test_database_failure_while_saving_the_answer_persists_nothing(answer, started, db, llm, monkeypatch):  # EC21, AC18
    owner, session_id, q1 = started
    real_commit = db.commit

    def failing_commit():
        monkeypatch.setattr(db, "commit", real_commit)
        raise RuntimeError("disk full")

    monkeypatch.setattr(db, "commit", failing_commit)

    r = answer(owner, session_id, q1["id"])

    assert r.status_code == 500
    assert r.json()["error"]["code"] == "INTERNAL_ERROR"
    assert message_count(db) == 0
    assert db.get(InterviewSession, uuid.UUID(session_id)).current_position == 1
    assert llm.fake.calls == []


def test_answer_route_documents_its_error_responses():  # AC20
    responses = app.openapi()["paths"]["/api/v1/interviews/{session_id}/messages"]["post"]["responses"]

    assert "201" in responses
    for status in ("401", "403", "404", "409", "422"):
        assert responses[status]["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorResponse")
