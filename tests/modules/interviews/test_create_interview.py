import uuid

import pytest
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from app.modules.auth.auth_model import User
from app.modules.interviews.interviews_model import InterviewQuestion, InterviewSession
from app.modules.interviews.interviews_repository import InterviewsRepository

INTERVIEWS = "/api/v1/interviews"


def _sessions(db, user=None):
    query = select(InterviewSession).order_by(InterviewSession.id)
    if user is not None:
        query = query.where(InterviewSession.user_id == user.id)
    return db.scalars(query).all()


def _questions(db, session_id):
    query = select(InterviewQuestion).where(InterviewQuestion.session_id == uuid.UUID(session_id))
    return db.scalars(query.order_by(InterviewQuestion.position)).all()


def _question_count(db):
    return db.scalar(select(func.count()).select_from(InterviewQuestion))


# --- happy path ---


def test_start_creates_saved_session_and_returns_only_the_first_question(start_interview, make_user, db):  # AC2
    user = make_user()

    r = start_interview(user, job_description="Build APIs with FastAPI.")

    assert r.status_code == 201
    body = r.json()
    assert set(body) == {"session", "current_question"}
    session = body["session"]
    assert set(session) == {
        "id",
        "role",
        "level",
        "interview_type",
        "question_count",
        "job_description",
        "status",
        "created_at",
    }
    assert session["role"] == "backend"
    assert session["level"] == "junior"
    assert session["interview_type"] == "behavioral"
    assert session["question_count"] == 3
    assert session["job_description"] == "Build APIs with FastAPI."
    assert session["status"] == "in_progress"

    [saved] = _sessions(db, user)
    assert str(saved.id) == session["id"]
    # llm-interviewer: questions are created one per turn, so only question 1 exists after the start.
    [stored] = _questions(db, session["id"])
    assert stored.position == 1

    current = body["current_question"]
    assert set(current) == {"id", "position", "text", "category"}  # AC16: no bank_id
    assert current["position"] == 1
    assert current["id"] == str(stored.id)
    assert current["text"] == stored.text


def test_first_bank_question_fits_the_setup(start_interview, make_user, db):  # AC3, EC11 (no LLM configured)
    user = make_user()
    for _ in range(10):
        r = start_interview(user, interview_type="technical", question_count=5)

        [stored] = _questions(db, r.json()["session"]["id"])
        assert stored.bank_id != "frontend-only"
        assert stored.category == "technical"


def test_mixed_session_starts_with_a_behavioral_question(start_interview, make_user, db):  # AC4, EC9
    r = start_interview(make_user(), interview_type="mixed", question_count=5)

    assert [q.category for q in _questions(db, r.json()["session"]["id"])] == ["behavioral"]


# --- not enough questions ---


def test_not_enough_questions_is_409_and_leaves_existing_session_alone(start_interview, make_user, db):  # AC5, EC8
    user = make_user()
    first = start_interview(user).json()["session"]

    r = start_interview(user, question_count=6)  # fixture bank has 5 behavioral

    assert r.status_code == 409
    error = r.json()["error"]
    assert error["code"] == "NOT_ENOUGH_QUESTIONS"
    assert error["details"] == {"requested": 6, "available": 5}
    [only] = _sessions(db, user)
    assert str(only.id) == first["id"]
    assert only.status == "in_progress"


def test_mixed_short_on_one_type_is_409(start_interview, make_user, make_bank_question, bank, db):  # AC4, EC10
    bank[:] = [q for q in bank if q.type == "behavioral"] + [make_bank_question("t0", "technical")]

    r = start_interview(make_user(), interview_type="mixed", question_count=4)

    assert r.status_code == 409
    assert r.json()["error"]["details"] == {"requested": 4, "available": 3}
    assert _sessions(db) == []


# --- validation ---


@pytest.mark.parametrize(
    "overrides",
    [
        pytest.param({"role": "devops"}, id="unknown-role"),
        pytest.param({"level": "Junior"}, id="wrong-case-level"),
        pytest.param({"interview_type": "system_design"}, id="unknown-type"),
        pytest.param({"question_count": 0}, id="count-0"),
        pytest.param({"question_count": 11}, id="count-11"),
        pytest.param({"question_count": -1}, id="count-negative"),
        pytest.param({"question_count": 2.5}, id="count-fraction"),
        pytest.param({"question_count": "3"}, id="count-string"),
        pytest.param({"question_count": None}, id="count-missing"),
        pytest.param({"role": None}, id="role-missing"),
        pytest.param({"status": "abandoned"}, id="server-field-status"),
        pytest.param({"user_id": str(uuid.uuid4())}, id="server-field-user-id"),
        pytest.param({"job_description": "x" * 2001}, id="description-too-long"),
        pytest.param({"job_description": "  " + "x" * 2001 + "  "}, id="description-too-long-after-trim"),
    ],
)
def test_invalid_setup_is_422_and_creates_nothing(start_interview, make_user, db, overrides):  # AC6, EC3-EC6
    r = start_interview(make_user(), **overrides)

    assert r.status_code == 422
    assert r.json()["error"]["code"] == "VALIDATION_ERROR"
    assert _sessions(db) == []


@pytest.mark.parametrize(
    ("sent", "stored"),
    [
        pytest.param("x" * 2000, "x" * 2000, id="exactly-2000"),
        pytest.param("  " + "x" * 2000 + "\n", "x" * 2000, id="2000-after-trim"),
        pytest.param("   ", None, id="whitespace-only"),
        pytest.param("", None, id="empty"),
        pytest.param(None, None, id="omitted"),
    ],
)
def test_job_description_is_trimmed_and_blank_becomes_null(
    start_interview, make_user, db, sent, stored
):  # AC6, EC6, EC7
    user = make_user()

    r = start_interview(user, job_description=sent)

    assert r.status_code == 201
    assert r.json()["session"]["job_description"] == stored
    assert _sessions(db, user)[0].job_description == stored


# --- one in-progress session per user ---


def test_starting_again_abandons_the_previous_session(start_interview, make_user, db):  # AC7, EC13
    user = make_user()
    first = start_interview(user).json()["session"]

    second = start_interview(user).json()["session"]

    statuses = {str(s.id): s.status for s in _sessions(db, user)}
    assert statuses == {first["id"]: "abandoned", second["id"]: "in_progress"}


def test_different_users_each_keep_their_own_in_progress_session(
    start_interview, make_user, db
):  # inferred: per-user, not global
    ana, ben = make_user(email="ana@example.com"), make_user(email="ben@example.com")

    start_interview(ana)
    start_interview(ben)

    assert [s.status for s in _sessions(db, ana)] == ["in_progress"]
    assert [s.status for s in _sessions(db, ben)] == ["in_progress"]


def test_failure_while_saving_questions_rolls_everything_back(start_interview, make_user, db, monkeypatch):  # AC8, EC15
    user = make_user()
    first = start_interview(user).json()["session"]

    def fail(*args, **kwargs):
        raise RuntimeError("disk full")

    monkeypatch.setattr(db, "add_all", fail)
    r = start_interview(user)

    assert r.status_code == 500
    assert r.json()["error"]["code"] == "INTERNAL_ERROR"
    [only] = _sessions(db, user)
    assert str(only.id) == first["id"]
    assert only.status == "in_progress"
    assert _question_count(db) == 1


def test_database_rejects_two_in_progress_sessions_for_one_user(db, make_user):  # AC9, EC14
    user = make_user()

    def session_for(owner: User):
        return InterviewSession(
            user_id=owner.id, role="backend", level="junior", interview_type="behavioral", question_count=1
        )

    db.add(session_for(user))
    db.commit()
    db.add(session_for(user))
    with pytest.raises(IntegrityError):
        db.commit()


def test_losing_a_concurrent_start_is_409_conflict(start_interview, make_user, db, monkeypatch):  # AC9, EC14
    user = make_user()
    first = start_interview(user).json()["session"]
    # Simulate the race: another request created an in-progress session after this one's abandon step ran.
    monkeypatch.setattr(InterviewsRepository, "_abandon_in_progress", lambda self, user_id: None)

    r = start_interview(user)

    assert r.status_code == 409
    assert r.json()["error"]["code"] == "CONFLICT"
    [only] = _sessions(db, user)
    assert str(only.id) == first["id"]
    assert _question_count(db) == 1


# --- snapshot ---


def test_editing_the_bank_never_changes_a_saved_session(start_interview, make_user, bank, db):  # AC13, EC16
    r = start_interview(make_user(), question_count=5)
    before = [(q.bank_id, q.text) for q in _questions(db, r.json()["session"]["id"])]

    bank[:] = [q.model_copy(update={"text": "Edited later?"}) for q in bank]

    db.expire_all()
    assert [(q.bank_id, q.text) for q in _questions(db, r.json()["session"]["id"])] == before


# --- auth ---


def test_start_without_token_is_401(client, db, bank):  # AC12, EC1
    r = client.post(
        INTERVIEWS, json={"role": "backend", "level": "junior", "interview_type": "mixed", "question_count": 1}
    )

    assert r.status_code == 401
    assert r.json()["error"]["code"] == "TOKEN_MISSING"


def test_start_without_permission_is_403(start_interview, make_user, db):  # AC12, EC2
    r = start_interview(make_user(role="superuser"))

    assert r.status_code == 403
    assert _sessions(db) == []


# --- privacy ---


def test_job_description_never_appears_in_logs(start_interview, make_user, app_logs):  # AC17
    user = make_user()
    secret = "Confidential-JD-acme-payments-team"

    start_interview(user, job_description=secret)
    start_interview(user, job_description=secret, question_count=99)

    assert app_logs.records
    assert all(secret not in record.getMessage() for record in app_logs.records)
