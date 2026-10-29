import json
import logging
import uuid
from itertools import pairwise

from sqlalchemy import func, select

from app.core.ai.provider import LLMResult, LLMServerError
from app.modules.interviews.interviews_constants import CLOSING_REACTIONS, REACTION_POOLS
from app.modules.interviews.interviews_model import InterviewMessage, InterviewQuestion, InterviewSession
from app.modules.interviews.interviews_repository import InterviewsRepository

ALL_REACTIONS = {r for pool in REACTION_POOLS.values() for r in pool}
ALL_CLOSINGS = {r for pool in CLOSING_REACTIONS.values() for r in pool}


def questions(db, session_id):
    query = select(InterviewQuestion).where(InterviewQuestion.session_id == uuid.UUID(session_id))
    return db.scalars(query.order_by(InterviewQuestion.position)).all()


def messages(db, session_id, role=None):
    query = select(InterviewMessage).where(InterviewMessage.session_id == uuid.UUID(session_id))
    if role:
        query = query.where(InterviewMessage.role == role)
    return db.scalars(query.order_by(InterviewMessage.id)).all()


def run_interview(answer, owner, created, texts=None):
    """Answer every question of a started interview; returns the list of answer responses."""
    session_id, current, responses = created["session"]["id"], created["current_question"], []
    for i in range(created["session"]["question_count"]):
        r = answer(owner, session_id, current["id"], text=(texts[i] if texts else f"My answer {i}."))
        responses.append(r)
        current = r.json()["current_question"]
    return responses


def test_a_non_final_answer_gets_a_reaction_and_the_llms_next_question(
    start_interview, make_user, answer, llm, reply_json, db
):  # AC3, AC25
    owner = make_user()
    llm.script(reply_json("Opening question?", "behavioral"), reply_json("Second question?", "behavioral"))
    created = start_interview(owner, question_count=3).json()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert r.status_code == 201
    body = r.json()
    assert body["session"]["status"] == "in_progress"
    assert body["current_question"]["text"] == "Second question?" and body["current_question"]["position"] == 2
    assert body["reaction"]["text"] in ALL_REACTIONS
    q2 = questions(db, created["session"]["id"])[1]
    assert (q2.source, q2.category, q2.prompt_version) == ("llm", "behavioral", "interviewer_v1")
    assert len(llm.fake.calls) == 2


def test_the_final_answer_closes_without_an_llm_call(start_interview, make_user, answer, llm, db):  # AC4, EC11
    owner = make_user()
    created = start_interview(owner, question_count=2).json()
    responses = run_interview(answer, owner, created)

    final = responses[-1].json()
    assert final["session"]["status"] == "completed"
    assert final["current_question"] is None
    assert final["reaction"]["text"] in ALL_CLOSINGS
    assert len(llm.fake.calls) == 2  # opening + question 2; nothing for the last answer
    assert len(questions(db, created["session"]["id"])) == 2


def test_a_one_question_interview_makes_one_call(start_interview, make_user, answer, llm):  # EC12
    owner = make_user()
    created = start_interview(owner, question_count=1).json()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert r.json()["session"]["status"] == "completed"
    assert len(llm.fake.calls) == 1


def test_without_an_llm_the_whole_interview_runs_on_the_bank(start_interview, make_user, answer, db):  # EC1, AC8
    owner = make_user()
    created = start_interview(owner, interview_type="technical", question_count=5).json()

    responses = run_interview(answer, owner, created)

    stored = questions(db, created["session"]["id"])
    assert [q.source for q in stored] == ["bank"] * 5
    assert len({q.bank_id for q in stored}) == 5  # never the same bank question twice
    assert all(r.json()["reaction"] for r in responses)
    assert responses[-1].json()["session"]["status"] == "completed"


def test_a_mixed_bank_only_interview_alternates_behavioral_first(start_interview, make_user, answer, db):  # AC8
    owner = make_user()
    created = start_interview(owner, interview_type="mixed", question_count=5).json()

    run_interview(answer, owner, created)

    assert [q.category for q in questions(db, created["session"]["id"])] == [
        "behavioral",
        "technical",
        "behavioral",
        "technical",
        "behavioral",
    ]


def test_llm_failure_mid_interview_falls_back_to_an_unused_bank_question(
    start_interview, make_user, answer, llm, db
):  # EC4, EC24
    owner = make_user()
    llm.script(LLMServerError("503"), LLMServerError("503"))
    created = start_interview(owner, question_count=3).json()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert r.status_code == 201 and r.json()["reaction"]["text"] in ALL_REACTIONS
    q1, q2 = questions(db, created["session"]["id"])
    assert (q1.source, q2.source) == ("bank", "bank") and q1.bank_id != q2.bank_id


def test_each_turn_resends_the_conversation_without_reactions(
    start_interview, make_user, answer, llm, reply_json
):  # AC11
    owner = make_user()
    llm.script(
        reply_json("Q one?", "behavioral"), reply_json("Q two?", "behavioral"), reply_json("Q three?", "behavioral")
    )
    created = start_interview(owner, question_count=4).json()
    session_id = created["session"]["id"]
    q2 = answer(owner, session_id, created["current_question"]["id"], text="Answer one.").json()["current_question"]
    answer(owner, session_id, q2["id"], text="Answer two.")

    opening, turn2, turn3 = llm.fake.calls
    assert [m.role for m in turn3] == ["system", "user", "assistant", "user", "assistant", "user"]
    assert json.loads(turn3[2].content)["question"] == "Q one?" and turn3[3].content == "Answer one."
    assert turn3[-1].content == "Answer two."
    assert "question 3 of 4" in turn3[0].content
    assert len(opening) < len(turn2) < len(turn3)
    sent = " ".join(m.content for call in llm.fake.calls for m in call)
    assert not any(reaction in sent for reaction in ALL_REACTIONS)


def test_usage_is_stored_with_the_question_it_produced(start_interview, make_user, answer, llm, reply_json, db):  # AC13
    owner = make_user()

    def result(question, tokens):
        return LLMResult(
            text=reply_json(question, "behavioral"),
            model="m",
            prompt_tokens=tokens,
            completion_tokens=10,
            latency_ms=5,
            finish_reason="stop",
            attempts=1,
        )

    llm.script(result("Q1?", 100), result("Q2?", 150))
    created = start_interview(owner, question_count=3).json()
    answer(owner, created["session"]["id"], created["current_question"]["id"])

    total = db.scalar(
        select(func.sum(InterviewQuestion.prompt_tokens + InterviewQuestion.completion_tokens)).where(
            InterviewQuestion.session_id == uuid.UUID(created["session"]["id"])
        )
    )
    assert total == 270


def test_no_transaction_is_open_while_the_llm_writes_the_next_question(
    start_interview, make_user, answer, llm, db
):  # plan design point
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    seen = []
    llm.script(on_call=lambda: seen.append(db.in_transaction()))

    answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert seen == [False]


def test_a_turn_is_saved_all_or_nothing(start_interview, make_user, answer, llm, db, monkeypatch):  # AC9, EC18
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session_id, q1 = created["session"]["id"], created["current_question"]
    real_commit = db.commit
    armed = [True]

    def failing_commit():
        monkeypatch.setattr(db, "commit", real_commit)
        raise RuntimeError("disk full")

    def arm_once():  # only the first turn's save fails; the resubmit must go through
        if armed:
            armed.clear()
            monkeypatch.setattr(db, "commit", failing_commit)

    llm.script(on_call=arm_once)
    r = answer(owner, session_id, q1["id"])

    assert r.status_code == 500
    assert messages(db, session_id) == []
    assert len(questions(db, session_id)) == 1
    assert db.get(InterviewSession, uuid.UUID(session_id)).current_position == 1

    retry = answer(owner, session_id, q1["id"])
    assert retry.status_code == 201 and retry.json()["current_question"]["position"] == 2


def test_a_new_interview_started_during_the_call_wins(start_interview, make_user, answer, llm, db):  # EC22
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    session_id = created["session"]["id"]

    def abandon_meanwhile():
        db.get(InterviewSession, uuid.UUID(session_id)).status = "abandoned"
        db.commit()

    llm.script(on_call=abandon_meanwhile)
    r = answer(owner, session_id, created["current_question"]["id"])

    assert r.status_code == 409 and r.json()["error"]["code"] == "QUESTION_NOT_CURRENT"
    assert messages(db, session_id) == []
    assert len(questions(db, session_id)) == 1


def test_a_double_submit_stores_one_answer_and_makes_one_call(start_interview, make_user, answer, llm, db):  # AC15
    owner = make_user()
    created = start_interview(owner, question_count=3).json()
    calls_before = len(llm.fake.calls)

    first = answer(owner, created["session"]["id"], created["current_question"]["id"], text="first click")
    second = answer(owner, created["session"]["id"], created["current_question"]["id"], text="second click")

    assert (first.status_code, second.status_code) == (201, 409)
    assert [m.content for m in messages(db, created["session"]["id"], "candidate")] == ["first click"]
    assert len(llm.fake.calls) - calls_before == 1


def test_reactions_never_repeat_back_to_back_and_survive_a_reload(
    start_interview, make_user, answer, client, auth_header
):  # AC24, AC25
    owner = make_user()
    created = start_interview(owner, question_count=5).json()

    responses = run_interview(answer, owner, created)

    texts = [r.json()["reaction"]["text"] for r in responses]
    assert all(a != b for a, b in pairwise(texts))
    items = client.get(f"/api/v1/interviews/{created['session']['id']}/messages", headers=auth_header(owner)).json()
    assert [i["text"] for i in items["items"] if i["kind"] == "reaction"] == texts


def test_a_legacy_session_uses_its_stored_questions_and_no_llm(make_user, answer, llm, db):  # AC16, EC19, EC25
    owner = make_user()
    session = InterviewSession(
        user_id=owner.id,
        role="backend",
        level="junior",
        interview_type="behavioral",
        question_count=3,
        current_position=2,
    )
    stored = [
        InterviewQuestion(position=i, text=f"Legacy {i}?", category="behavioral", bank_id=f"b{i}") for i in (1, 2, 3)
    ]
    InterviewsRepository(db).start(session, stored)
    # Slice 1 left an answer and an LLM-written reaction on question 1.
    db.add_all(
        [
            InterviewMessage(session_id=session.id, question_id=stored[0].id, role="candidate", content="Old answer."),
            InterviewMessage(
                session_id=session.id, question_id=stored[0].id, role="interviewer", content="Old LLM text."
            ),
        ]
    )
    db.commit()
    session_id, q2_id = str(session.id), stored[1].id

    r2 = answer(owner, session_id, q2_id)
    r3 = answer(owner, session_id, r2.json()["current_question"]["id"])

    assert r2.json()["current_question"]["text"] == "Legacy 3?"
    assert r2.json()["reaction"]["text"] in ALL_REACTIONS
    assert r3.json()["session"]["status"] == "completed" and r3.json()["reaction"]["text"] in ALL_CLOSINGS
    assert llm.fake.calls == []
    assert len(questions(db, session_id)) == 3


def test_answer_turn_logs_carry_no_answer_text(start_interview, make_user, answer, llm, app_logs):  # AC12
    owner = make_user()
    created = start_interview(owner, question_count=3).json()

    answer(owner, created["session"]["id"], created["current_question"]["id"], text="My phone is 555-0100.")

    lines = [r for r in app_logs.records if r.name == "app.llm"]
    assert len(lines) == 2 and all(line.levelno == logging.INFO for line in lines)
    assert all("555-0100" not in r.getMessage() for r in app_logs.records)
