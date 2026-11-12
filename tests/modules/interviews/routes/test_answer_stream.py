"""POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events (sse-starlette).

Pre-stream checks fail as plain JSON; a stream that opens ends with exactly one `done` or `error`, and `done` is what the
JSON endpoint returns for the same turn (sse-streaming Steps 6-7; AC1-AC5, AC7-AC9, AC21, EC1-EC5, EC13-EC19).
"""

import json
import uuid

import pytest
from sqlalchemy import func, select

from app.core.ai.fake import FakeStream
from app.main import app
from app.modules.interviews.ai.interviews_turn import Interviewer
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V5_PROMPT_VERSION,
)
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from app.modules.interviews.repositories.interviews_repository import (
    InterviewsRepository,
)
from app.modules.interviews.routes import interviews_route
from app.modules.interviews.schemas.interviews_schema import AnswerOut

STREAM_PATH = "/api/v1/interviews/{session_id}/messages/stream"
TERMINAL = {"done", "error"}


def message_count(db) -> int:
    return db.scalar(select(func.count()).select_from(InterviewMessage))


def follow_up_json(question="What was the outcome for your team?") -> str:
    return json.dumps({"question": question})


@pytest.fixture
def started(make_user, start_interview):
    """An owner with a started 3-question behavioral interview: (owner, session_id, first question)."""
    owner = make_user(email="owner@example.com")
    created = start_interview(owner, question_count=3).json()
    return owner, created["session"]["id"], created["current_question"]


def assert_one_terminal(turn) -> None:
    names = turn.names()
    assert [n for n in names if n in TERMINAL] == [names[-1]], names


# --- AC1: the stream itself ---


def test_a_stream_is_an_uncached_unbuffered_event_stream(
    stream_answer, started, db, llm
):  # AC1
    owner, session_id, q1 = started

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.status_code == 200
    assert turn.headers["content-type"].startswith("text/event-stream")
    assert turn.headers["cache-control"] in {"no-store", "no-cache"}
    assert turn.headers["x-accel-buffering"] == "no"


def test_the_json_endpoint_still_answers_as_before(answer, started, db, llm):  # AC1
    owner, session_id, q1 = started

    r = answer(owner, session_id, q1["id"])

    assert r.status_code == 201
    assert set(r.json()) == set(AnswerOut.model_fields)


# --- AC2, EC1-EC4: failures before the stream are plain JSON ---


def test_no_token_is_a_json_401_and_no_stream(client, started, db):  # EC1
    _, session_id, q1 = started

    r = client.post(
        STREAM_PATH.format(session_id=session_id),
        json={"question_id": q1["id"], "answer": "hi"},
    )

    assert r.status_code == 401
    assert r.headers["content-type"].startswith("application/json")
    assert r.json()["error"]["code"] == "TOKEN_MISSING"


def test_caller_without_answer_permission_is_a_json_403(
    stream_answer, make_user, started, db
):  # EC1
    _, session_id, q1 = started
    outsider = make_user(email="odd@example.com", role="superuser")

    turn = stream_answer(outsider, session_id, q1["id"])

    assert turn.status_code == 403
    assert turn.body["error"]["code"] == "FORBIDDEN"


@pytest.mark.parametrize(
    "overrides",
    [
        {"answer": ""},
        {"answer": "x" * 2001},
        {"question_id": "not-a-uuid"},
        {"status": "completed"},
    ],
    ids=["empty", "too-long", "bad-question-id", "extra-field"],
)
def test_invalid_input_is_a_json_422_and_saves_nothing(
    stream_answer, started, db, llm, overrides
):  # EC1
    owner, session_id, q1 = started
    question_id = overrides.pop("question_id", q1["id"])

    turn = stream_answer(owner, session_id, question_id, **overrides)

    assert turn.status_code == 422
    assert turn.body["error"]["code"] == "VALIDATION_ERROR"
    assert message_count(db) == 0
    assert llm.fake.calls == []


def test_missing_and_foreign_sessions_are_the_same_json_404(
    stream_answer, make_user, started, db, llm
):  # EC2
    _, session_id, q1 = started
    stranger = make_user(email="stranger@example.com")

    foreign = stream_answer(stranger, session_id, q1["id"])
    missing = stream_answer(stranger, uuid.uuid7(), q1["id"])

    assert foreign.status_code == missing.status_code == 404
    assert {**foreign.body["error"], "request_id": None} == {
        **missing.body["error"],
        "request_id": None,
    }
    assert llm.fake.calls == llm.decide.calls == []


def test_a_completed_session_is_a_json_409(stream_answer, started, db, llm):  # EC3
    owner, session_id, q1 = started
    db.get(InterviewSession, uuid.UUID(session_id)).status = "completed"
    db.commit()

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.status_code == 409
    assert turn.body["error"]["code"] == "SESSION_NOT_IN_PROGRESS"
    assert message_count(db) == 0


def test_a_question_that_is_not_current_is_a_json_409(
    stream_answer, started, db, llm
):  # EC4
    owner, session_id, _ = started

    turn = stream_answer(owner, session_id, uuid.uuid7())

    assert turn.status_code == 409
    assert turn.body["error"]["code"] == "QUESTION_NOT_CURRENT"
    assert llm.fake.calls == llm.decide.calls == []


# --- AC3, AC4, AC5, AC9: what a stream sends and saves ---


def test_a_move_on_turn_streams_progress_the_reaction_and_done(
    stream_answer, started, db, llm
):  # AC3, AC9
    owner, session_id, q1 = started

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.flow() == ["status", "status", "reaction", "status", "question.delta", "done"]
    assert [d["phase"] for d in turn.data("status")] == [
        "received",
        "deciding",
        "writing",
    ]
    assert_one_terminal(turn)
    [done] = turn.data("done")
    assert done["reaction"] == turn.data("reaction")[0]


def test_done_has_the_json_endpoints_shape_and_content(
    stream_answer, answer, make_user, start_interview, db, llm, reply_json
):  # AC4
    def run(via):
        owner = make_user(email=f"{via}@example.com")
        created = start_interview(owner, question_count=3).json()
        llm.script(reply_json("Tell me about a deadline you missed?", "behavioral"))
        if via == "json":
            return answer(
                owner, created["session"]["id"], created["current_question"]["id"]
            ).json()
        return stream_answer(
            owner, created["session"]["id"], created["current_question"]["id"]
        ).data("done")[0]

    json_body, done = run("json"), run("stream")

    assert set(done) == set(AnswerOut.model_fields)
    for body in (json_body, done):
        body["session"].pop("id")
        body["session"].pop("created_at", None)
        body["current_question"].pop("id")
        body["reaction"].pop("id")
        body["reaction"].pop("text")  # picked at random from the same pool
    assert done == json_body


def test_a_streamed_turn_saves_the_rows_the_json_turn_would(
    stream_answer,
    answer,
    make_user,
    start_interview,
    client,
    auth_header,
    db,
    llm,
    reply_json,
    decision_json,
):  # AC5
    def run(via):
        owner = make_user(email=f"{via}@example.com")
        created = start_interview(owner, question_count=3).json()
        llm.script_decide(decision_json(note="Named the conflict but not the result."))
        llm.script(reply_json("Describe a project you led?", "behavioral"))
        send = answer if via == "json" else stream_answer
        send(
            owner,
            created["session"]["id"],
            created["current_question"]["id"],
            text="We argued, then compromised.",
        )
        items = client.get(
            f"/api/v1/interviews/{created['session']['id']}/messages",
            headers=auth_header(owner),
        ).json()["items"]
        notes = [
            m.note
            for m in db.scalars(
                select(InterviewMessage).where(InterviewMessage.role == "candidate")
            )
        ]
        return (
            [(i["kind"], i["role"], i["position"], i["question_kind"]) for i in items],
            # The first question's generated text differs per session by design; everything after it must match.
            [i["text"] for i in items[1:] if i["kind"] != "reaction"],
            notes[-1],
        )

    assert run("stream") == run("json")


def test_a_follow_up_streams_no_reaction(
    stream_answer, started, db, llm, decision_json
):  # EC13
    owner, session_id, q1 = started
    llm.script_decide(decision_json("follow_up", "missing_result"))
    llm.script(follow_up_json())

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.flow() == ["status", "status", "status", "question.delta", "done"]
    [done] = turn.data("done")
    assert done["reaction"] is None
    assert done["current_question"]["question_kind"] == "follow_up"


def test_a_follow_up_that_falls_back_sends_its_reaction_only_in_done(
    stream_answer, started, db, llm, decision_json
):  # EC14
    owner, session_id, q1 = started
    llm.script_decide(decision_json("follow_up", "missing_result"))
    # Invalid in both formats (two questions): both drafts are taken back and the bank asks the next main question.
    llm.script(follow_up_json("What happened? And why?"), follow_up_json("What did you do? And then?"))

    turn = stream_answer(owner, session_id, q1["id"])

    assert "reaction" not in turn.names()
    [done] = turn.data("done")
    assert done["reaction"] is not None
    assert done["current_question"]["question_kind"] == "main"


def test_the_last_thread_completes_with_a_final_reaction_and_no_writing(
    stream_answer, make_user, start_interview, db, llm
):  # EC15
    owner = make_user()
    created = start_interview(owner, question_count=1).json()

    turn = stream_answer(
        owner, created["session"]["id"], created["current_question"]["id"]
    )

    assert turn.names() == ["status", "status", "reaction", "done"]
    assert [d["phase"] for d in turn.data("status")] == ["received", "deciding"]
    [done] = turn.data("done")
    assert done["current_question"] is None
    assert done["session"]["status"] == "completed"


def test_without_an_llm_the_stream_is_received_reaction_done(
    stream_answer, started, db
):  # EC16
    owner, session_id, q1 = started

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.names() == ["status", "reaction", "done"]
    assert turn.data("status") == [{"phase": "received"}]
    assert turn.data("done")[0]["current_question"]["text"].startswith("Question ")  # the fixture bank's


def test_a_session_with_stored_questions_streams_without_the_llm(
    stream_answer, make_user, db, llm
):  # EC16
    owner = make_user(email="legacy@example.com")
    session = InterviewSession(
        user_id=owner.id,
        role="backend",
        level="junior",
        interview_type="behavioral",
        question_count=3,
    )
    stored = [
        InterviewQuestion(
            position=i, text=f"Q{i}?", category="behavioral", bank_id=f"b{i}"
        )
        for i in (1, 2, 3)
    ]
    InterviewsRepository(db).start(session, stored)

    turn = stream_answer(owner, session.id, stored[0].id)

    assert turn.names() == ["status", "reaction", "done"]
    assert turn.data("done")[0]["current_question"]["text"] == "Q2?"
    assert llm.fake.calls == llm.decide.calls == []


# --- AC7, AC8, EC5, EC17, EC18: failures after the stream opened ---


def test_two_submits_of_one_question_save_one_turn_and_the_loser_gets_an_error_event(
    stream_answer, answer, started, db, llm
):  # AC7, EC5
    owner, session_id, q1 = started
    raced = []

    def submit_the_same_answer_elsewhere():
        if not raced:  # the other tab's own LLM calls run this hook too, so mark it before submitting
            raced.append(None)
            raced[0] = answer(owner, session_id, q1["id"], text="from the other tab")

    llm.script_decide(on_call=submit_the_same_answer_elsewhere)

    turn = stream_answer(owner, session_id, q1["id"], text="from this tab")

    assert raced[0].status_code == 201
    assert turn.names()[-1] == "error"
    assert_one_terminal(turn)
    [error] = turn.data("error")
    assert error["code"] == "QUESTION_NOT_CURRENT"
    answers = db.scalars(
        select(InterviewMessage).where(InterviewMessage.role == "candidate")
    ).all()
    assert [a.content for a in answers] == ["from the other tab"]


def test_a_save_that_fails_sends_one_generic_error_and_saves_nothing(
    stream_answer, started, db, llm, monkeypatch
):  # AC8, EC18
    owner, session_id, q1 = started

    def broken_save(*args, **kwargs):
        raise RuntimeError("disk full at /var/lib/secret-host")

    monkeypatch.setattr(InterviewsRepository, "record_turn", broken_save)

    turn = stream_answer(owner, session_id, q1["id"], text="my private answer text")

    assert_one_terminal(turn)
    [error] = turn.data("error")
    assert error["code"] == "INTERNAL_ERROR"
    assert error["message"] == "An unexpected error occurred"
    assert error["request_id"]
    raw = json.dumps(turn.events)
    assert (
        "secret-host" not in raw
        and "disk full" not in raw
        and "my private answer text" not in raw
    )
    assert message_count(db) == 0
    assert db.get(InterviewSession, uuid.UUID(session_id)).current_position == 1


def test_an_unexpected_crash_mid_turn_is_one_generic_error_event(
    stream_answer, started, db, llm, monkeypatch, app_logs
):  # AC8, EC17
    owner, session_id, q1 = started

    def crash(*args, **kwargs):
        raise ValueError("kaboom internal detail")

    monkeypatch.setattr(Interviewer, "plan_write", crash)

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.names()[-1] == "error"
    assert_one_terminal(turn)
    [error] = turn.data("error")
    assert error["code"] == "INTERNAL_ERROR"
    assert "kaboom" not in json.dumps(turn.events)
    assert any(
        "kaboom internal detail" in r.getMessage() or r.exc_info
        for r in app_logs.records
    )
    assert message_count(db) == 0


# --- EC19: heartbeats ---


def test_a_long_wait_sends_heartbeat_comments_and_no_extra_events(
    stream_answer, started, db, llm, monkeypatch
):  # EC19
    import time

    owner, session_id, q1 = started
    monkeypatch.setattr(interviews_route, "STREAM_PING_SECONDS", 0.05)
    llm.script_decide(on_call=lambda: time.sleep(0.3))

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.comments >= 1
    assert turn.flow() == ["status", "status", "reaction", "status", "question.delta", "done"]


# --- AC13, AC14 (Phase B): the question streams as it is written ---


def test_the_streamed_question_is_the_saved_one_and_never_shows_its_category(
    stream_answer, started, db, llm
):  # AC13
    owner, session_id, q1 = started
    llm.script(FakeStream(["CATEGORY: behav", "ioral\nTell me about a ", "time you ", "led a project?"]))

    turn = stream_answer(owner, session_id, q1["id"])

    deltas = [d["text"] for d in turn.data("question.delta")]
    assert len(deltas) >= 2
    [done] = turn.data("done")
    assert turn.question() == done["current_question"]["text"] == "Tell me about a time you led a project?"
    assert not any("CATEGORY" in d or "behavioral" in d for d in deltas)
    saved = db.get(InterviewQuestion, uuid.UUID(done["current_question"]["id"]))
    assert saved.prompt_version == INTERVIEWER_V5_PROMPT_VERSION


def test_a_draft_that_fails_its_checks_is_reset_before_the_next_one(stream_answer, started, db, llm):  # AC14, EC7
    owner, session_id, q1 = started
    llm.script(
        "CATEGORY: behavioral\nWhat did you build? And why?",
        "CATEGORY: behavioral\nTell me about a deadline you missed?",
    )

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.flow()[-4:] == ["question.delta", "reset", "question.delta", "done"]
    assert turn.question() == turn.data("done")[0]["current_question"]["text"] == "Tell me about a deadline you missed?"


# --- AC16: a waiting stream doesn't block other requests ---


@pytest.mark.anyio
async def test_other_requests_are_served_while_a_stream_waits_on_the_llm(started, db, llm, auth_header):  # AC16
    import time

    import anyio
    import httpx

    owner, session_id, q1 = started
    llm.script(FakeStream(["CATEGORY: behavioral\n", "Tell me about ", "a deadline you missed?"], delay=0.4))
    finished: dict[str, float] = {}

    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:

        async def stream() -> None:
            r = await client.post(
                STREAM_PATH.format(session_id=session_id),
                json={"question_id": q1["id"], "answer": "We shipped it late."},
                headers=auth_header(owner),
            )
            assert r.status_code == 200 and "event: done" in r.text
            finished["stream"] = time.perf_counter()

        async def health() -> None:
            await anyio.sleep(0.1)  # the stream is waiting on its first chunk by now
            started_at = time.perf_counter()
            assert (await client.get("/health")).status_code == 200
            finished["health"] = time.perf_counter()
            finished["health_ms"] = (finished["health"] - started_at) * 1000

        async with anyio.create_task_group() as tg:
            tg.start_soon(stream)
            tg.start_soon(health)

    assert finished["health"] < finished["stream"]
    assert finished["health_ms"] < 300


# --- AC21: the contract is documented ---


def test_the_stream_route_documents_its_events_and_errors():  # AC21
    operation = app.openapi()["paths"][
        STREAM_PATH.replace("{session_id}", "{session_id}")
    ]["post"]
    responses = operation["responses"]

    assert "text/event-stream" in responses["200"]["content"]
    description = responses["200"]["description"]
    for name in ("status", "reaction", "question.delta", "reset", "done", "error"):
        assert name in description
    for status in ("401", "403", "404", "409", "422"):
        assert responses[status]["content"]["application/json"]["schema"][
            "$ref"
        ].endswith("/ErrorResponse")
