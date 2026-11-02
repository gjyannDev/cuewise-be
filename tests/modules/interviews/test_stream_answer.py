"""InterviewsController.stream_answer driven directly, for what a test client can't do: leave mid-stream, and time the
first event (sse-streaming Step 6; AC6, AC10, AC17, EC6)."""

import random
import time
import uuid

import anyio
import pytest
from sqlalchemy import func, select

from app.core.ai.fake import FakeStream
from app.modules.interviews.interviews_controller import InterviewsController
from app.modules.interviews.interviews_model import InterviewMessage, InterviewSession
from app.modules.interviews.interviews_repository import InterviewsRepository
from app.modules.interviews.interviews_schema import AnswerIn

pytestmark = pytest.mark.anyio

ANSWER = "My private answer about the payments outage."


@pytest.fixture
def turn(make_user, start_interview, db, bank, llm, clock):
    """A started interview and a controller wired like the app's: returns (controller, prepared turn, session id)."""
    owner = make_user(email="owner@example.com")
    created = start_interview(owner, question_count=3).json()
    session_id = uuid.UUID(created["session"]["id"])
    controller = InterviewsController(
        InterviewsRepository(db), bank, random.Random(0), llm, 800, llm_budget_seconds=30, clock=clock
    )
    ctx = controller.prepare_answer(
        owner, session_id, AnswerIn(question_id=created["current_question"]["id"], answer=ANSWER)
    )
    return controller, ctx, session_id


def saved_answers(db) -> int:
    return db.scalar(select(func.count()).select_from(InterviewMessage).where(InterviewMessage.role == "candidate"))


def summaries(app_logs) -> list[str]:
    return [r.getMessage() for r in app_logs.records if r.getMessage().startswith("stream_turn_summary")]


async def test_the_first_event_is_sent_before_any_llm_call_returns(turn, llm, app_logs):  # AC10
    controller, ctx, _ = turn
    llm.script_decide(on_call=lambda: time.sleep(1.5))
    started = time.perf_counter()

    events = controller.stream_answer(ctx, started_at=started)
    first = await anext(events)
    elapsed = time.perf_counter() - started
    rest = [event async for event in events]

    assert first.event == "status" and first.data.phase == "received"
    assert elapsed < 1.0
    assert rest[-1].event == "done"
    [summary] = summaries(app_logs)
    assert "terminal=done" in summary
    first_event_ms = int(summary.split("first_event_ms=")[1].split()[0])
    assert first_event_ms < 1000


async def test_leaving_while_the_decide_call_runs_saves_nothing(turn, llm, db, app_logs):  # AC6, EC6
    controller, ctx, session_id = turn
    llm.script_decide(on_call=lambda: time.sleep(0.5))
    events = controller.stream_answer(ctx, started_at=time.perf_counter())

    assert [(await anext(events)).data.phase for _ in range(2)] == ["received", "deciding"]
    with anyio.move_on_after(0.05):  # the client leaves; sse-starlette cancels the stream like this
        await anext(events)

    assert saved_answers(db) == 0
    assert db.get(InterviewSession, session_id).current_position == 1
    [summary] = summaries(app_logs)
    assert "cancelled=true" in summary and "terminal=-" in summary


async def test_closing_the_stream_mid_turn_saves_nothing(turn, llm, db, app_logs):  # AC6, EC6
    controller, ctx, session_id = turn
    events = controller.stream_answer(ctx, started_at=time.perf_counter())

    names = [(await anext(events)).event for _ in range(3)]
    await events.aclose()

    assert names == ["status", "status", "reaction"]
    assert saved_answers(db) == 0
    assert db.get(InterviewSession, session_id).current_position == 1
    assert "cancelled=true" in summaries(app_logs)[0]


async def test_the_stream_summary_is_metadata_only(turn, app_logs):  # AC17
    controller, ctx, _ = turn

    [_ async for _ in controller.stream_answer(ctx, started_at=time.perf_counter())]

    [summary] = summaries(app_logs)
    for field in ("terminal=", "first_event_ms=", "first_token_ms=", "total_ms=", "resets=", "cancelled="):
        assert field in summary
    assert all(ANSWER not in r.getMessage() for r in app_logs.records)


async def test_the_summary_times_the_first_token_and_counts_resets(turn, llm, app_logs):  # AC17
    controller, ctx, _ = turn
    llm.script(
        "CATEGORY: behavioral\nWhat did you build? And why?",
        FakeStream(["CATEGORY: behavioral\n", "Tell me about ", "a deadline you missed?"], delay=0.05),
    )

    events = [e async for e in controller.stream_answer(ctx, started_at=time.perf_counter())]

    assert [e.event for e in events].count("reset") == 1
    [summary] = summaries(app_logs)
    assert "resets=1" in summary and "terminal=done" in summary
    first_token_ms = summary.split("first_token_ms=")[1].split()[0]
    assert first_token_ms.isdigit()


async def test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing(
    turn, llm, db, app_logs
):  # AC6, AC15, EC6
    controller, ctx, session_id = turn
    llm.script(FakeStream(["CATEGORY: behavioral\n", "Tell me ", "about a ", "deadline?"], delay=0.05))
    events = controller.stream_answer(ctx, started_at=time.perf_counter())

    async for event in events:
        if event.event == "question.delta":
            break
    await events.aclose()

    assert llm.fake.cancelled is True
    assert saved_answers(db) == 0
    assert db.get(InterviewSession, session_id).current_position == 1
    assert "cancelled=true" in summaries(app_logs)[0]
    [call] = [r.getMessage() for r in app_logs.records if "outcome=cancelled" in r.getMessage()]
    assert "task=interviewer_stream" in call
