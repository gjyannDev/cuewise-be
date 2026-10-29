import uuid

from sqlalchemy import select

from app.modules.interviews.interviews_model import InterviewMessage, InterviewSession

INTERVIEWS = "/api/v1/interviews"


def session_uuid(created) -> uuid.UUID:
    return uuid.UUID(created["session"]["id"])


def candidate_rows(db, session_id):
    return db.scalars(
        select(InterviewMessage).where(InterviewMessage.session_id == session_id, InterviewMessage.role == "candidate")
    ).all()


def test_answering_a_question_saves_it_and_moves_to_the_next(make_user, start_interview, answer, db):  # AC2
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session_id, q1 = created["session"]["id"], created["current_question"]

    r = answer(owner, session_id, q1["id"], text="  We argued, so I built a prototype.  ")

    assert r.status_code == 201
    body = r.json()
    assert set(body) == {"session", "reaction", "current_question"}
    assert body["session"]["status"] == "in_progress"
    assert body["reaction"]["text"]  # predefined, present even with no LLM configured (llm-interviewer EC1)
    assert body["current_question"]["position"] == 2
    assert "bank_id" not in r.text
    [row] = candidate_rows(db, session_uuid(created))
    assert row.content == "We argued, so I built a prototype."  # trimmed
    assert row.question_id == uuid.UUID(q1["id"])
    assert db.get(InterviewSession, session_uuid(created)).current_position == 2


def test_full_interview_without_llm_completes(make_user, start_interview, answer, db):  # AC4, EC18, EC20
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session_id, current = created["session"]["id"], created["current_question"]

    positions = []
    for _ in range(3):
        body = answer(owner, session_id, current["id"]).json()
        positions.append(current["position"])
        current = body["current_question"]

    assert positions == [1, 2, 3]
    assert body["session"]["status"] == "completed"
    assert body["current_question"] is None
    assert len(candidate_rows(db, session_uuid(created))) == 3


def test_after_completing_the_user_can_start_a_new_interview(
    make_user, start_interview, answer, client, auth_header
):  # EC20
    owner = make_user()
    created = start_interview(owner, question_count=1).json()
    answer(owner, created["session"]["id"], created["current_question"]["id"])

    r = start_interview(owner)

    assert r.status_code == 201
    old = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(owner)).json()
    assert old["session"]["status"] == "completed"  # finishing is not "abandoning"


def test_get_returns_the_question_the_candidate_is_on(make_user, start_interview, answer, client, auth_header):  # AC17
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session_id = created["session"]["id"]
    next_question = answer(owner, session_id, created["current_question"]["id"]).json()["current_question"]

    r = client.get(f"{INTERVIEWS}/{session_id}", headers=auth_header(owner))

    assert r.json()["current_question"] == next_question


def test_get_on_a_completed_session_has_no_current_question(
    make_user, start_interview, answer, client, auth_header
):  # EC25
    owner = make_user()
    created = start_interview(owner, question_count=1).json()
    answer(owner, created["session"]["id"], created["current_question"]["id"])

    r = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(owner))

    assert r.status_code == 200
    assert r.json()["session"]["status"] == "completed"
    assert r.json()["current_question"] is None


def test_get_on_an_abandoned_session_shows_where_it_stopped(
    make_user, start_interview, answer, client, auth_header
):  # EC25
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session_id = created["session"]["id"]
    q2 = answer(owner, session_id, created["current_question"]["id"]).json()["current_question"]
    start_interview(owner)

    r = client.get(f"{INTERVIEWS}/{session_id}", headers=auth_header(owner))

    assert r.json()["session"]["status"] == "abandoned"
    assert r.json()["current_question"] == q2
