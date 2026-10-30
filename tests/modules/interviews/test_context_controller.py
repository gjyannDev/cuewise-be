import json
import uuid

import pytest
from sqlalchemy import select

from app.core.ai.context import ContextManager, Task
from app.core.ai.provider import LLMServerError
from app.main import app
from app.modules.interviews.interviews_constants import INTERVIEWER_TASK, WINDOW_LEDGER
from app.modules.interviews.interviews_context import WindowLedger
from app.modules.interviews.interviews_dependencies import get_context_manager
from app.modules.interviews.interviews_model import InterviewMessage, InterviewQuestion


def noted(question, note=None, category="behavioral"):
    body = {"question": question, "category": category}
    if note is not None:
        body["note"] = note
    return json.dumps(body)


def candidate_messages(db, session_id):
    query = select(InterviewMessage).where(
        InterviewMessage.session_id == uuid.UUID(session_id), InterviewMessage.role == "candidate"
    )
    return db.scalars(query.order_by(InterviewMessage.id)).all()


def run(answer, owner, created, n):
    session_id, current = created["session"]["id"], created["current_question"]
    responses = []
    for i in range(1, n + 1):
        r = answer(owner, session_id, current["id"], text=f"Unique answer number {i} about my project.")
        responses.append(r)
        current = r.json()["current_question"]
    return responses


@pytest.fixture
def tiny_context():
    app.dependency_overrides[get_context_manager] = lambda: ContextManager(
        {INTERVIEWER_TASK: Task(default=WINDOW_LEDGER, strategies={WINDOW_LEDGER: WindowLedger(limit=10)})}
    )
    yield
    app.dependency_overrides.pop(get_context_manager, None)


def test_the_live_default_is_the_window_layout_with_v2(start_interview, make_user, answer, llm, db):  # AC2
    owner = make_user()
    created = start_interview(owner, question_count=3).json()

    answer(owner, created["session"]["id"], created["current_question"]["id"])

    system, *_, last = llm.fake.calls[1]
    assert "question 2 of" not in system.content and "question 2 of 3" in last.content
    q2 = db.scalars(select(InterviewQuestion).where(InterviewQuestion.position == 2)).one()
    assert q2.prompt_version == "interviewer_v2"


def test_older_answers_are_not_resent_in_a_long_interview(start_interview, make_user, answer, llm):  # AC3
    owner = make_user()
    created = start_interview(owner, interview_type="mixed", question_count=6).json()  # the fixture bank backs 6

    run(answer, owner, created, 5)

    sent = " ".join(m.content for m in llm.fake.calls[-1])
    assert "Unique answer number 1 " not in sent and "Unique answer number 2 " not in sent
    assert all(f"Unique answer number {i} " in sent for i in (3, 4, 5))


def test_a_valid_note_is_stored_and_shown_in_later_ledgers(start_interview, make_user, answer, llm, db):  # AC16, AC17
    owner = make_user()
    llm.script(
        noted("Opening question?"),
        noted("Second question?", note="Talked about a payments migration."),
        noted("Third question?", note="Explained a tricky bug hunt."),
        noted("Fourth question?", note="Described mentoring a junior."),
        noted("Fifth question?", note="Covered on-call habits."),
    )
    created = start_interview(owner, question_count=5).json()

    run(answer, owner, created, 4)

    notes = [m.note for m in candidate_messages(db, created["session"]["id"])]
    assert notes == [
        "Talked about a payments migration.",
        "Explained a tricky bug hunt.",
        "Described mentoring a junior.",
        "Covered on-call habits.",
    ]
    ledger = llm.fake.calls[-1][-1].content
    assert "Talked about a payments migration." in ledger and "Unique answer number 1 " not in ledger


def test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(
    start_interview, make_user, answer, llm, db, app_logs
):  # AC15, EC20
    owner = make_user()
    llm.script(noted("Opening question?"), noted("Second question?", note="x" * 500))
    created = start_interview(owner, question_count=3).json()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert r.json()["current_question"]["text"] == "Second question?"
    assert len(llm.fake.calls) == 2
    assert candidate_messages(db, created["session"]["id"])[0].note is None
    assert any("note_dropped" in rec.getMessage() and "too_long" in rec.getMessage() for rec in app_logs.records)
    assert all("xxxxxxxxxx" not in rec.getMessage() for rec in app_logs.records)


def test_no_note_after_a_bank_fallback_or_for_the_final_answer(start_interview, make_user, answer, llm, db):  # EC22
    owner = make_user()
    llm.script(noted("Opening question?"), LLMServerError("503"), LLMServerError("503"))
    created = start_interview(owner, question_count=2).json()

    run(answer, owner, created, 2)

    assert [m.note for m in candidate_messages(db, created["session"]["id"])] == [None, None]


def test_a_too_large_context_uses_the_bank_without_calling_the_llm(
    start_interview, make_user, llm, db, app_logs, tiny_context
):  # AC7, EC7
    r = start_interview(make_user(), question_count=3)

    assert r.status_code == 201
    assert llm.fake.calls == []
    q1 = db.scalars(select(InterviewQuestion)).one()
    assert q1.source == "bank"
    assert any("outcome=too_large" in rec.getMessage() for rec in app_logs.records if rec.name == "app.llm.context")


def test_without_an_llm_no_context_is_built(start_interview, make_user, app_logs):  # EC16
    start_interview(make_user(), question_count=3)

    assert not [rec for rec in app_logs.records if rec.name == "app.llm.context"]


def test_notes_never_appear_in_responses_or_logs(
    start_interview, make_user, answer, llm, client, auth_header, app_logs
):  # AC16
    owner = make_user()
    llm.script(noted("Opening question?"), noted("Second question?", note="Mentioned a SECRET-NOTE-42 detail."))
    created = start_interview(owner, question_count=3).json()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])
    transcript = client.get(f"/api/v1/interviews/{created['session']['id']}/messages", headers=auth_header(owner))
    current = client.get(f"/api/v1/interviews/{created['session']['id']}", headers=auth_header(owner))

    assert "SECRET-NOTE-42" not in r.text + transcript.text + current.text
    assert all("SECRET-NOTE-42" not in rec.getMessage() for rec in app_logs.records)
