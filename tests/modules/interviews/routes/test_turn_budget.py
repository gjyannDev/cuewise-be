"""One deadline per answer turn, shared by the decide and the write call (AC13, AC18, AC19, EC6, EC20, EC21).

The fake clock only moves when a fake provider's `on_call` moves it, so each test states exactly how slow a call was.
"""

import json

import pytest

from app.core.ai.provider import LLMResult, LLMTimeoutError
from app.core.config import settings
from app.modules.interviews.constants.interviews_constants import (
    DECIDE_MAX_SECONDS,
    MIN_SECONDS_FOR_WRITE,
    WRITE_RESERVE_SECONDS,
)


@pytest.fixture
def budget(monkeypatch):
    def _set(seconds: float) -> None:
        monkeypatch.setattr(settings, "llm_total_budget_seconds", seconds)

    _set(30.0)
    return _set


def result(text: str, prompt: int, completion: int, latency: int) -> LLMResult:
    return LLMResult(
        text=text,
        model="vendor/model-x",
        prompt_tokens=prompt,
        completion_tokens=completion,
        latency_ms=latency,
        finish_reason="stop",
        attempts=1,
    )


def start(start_interview, make_user, question_count=2):
    owner = make_user()
    created = start_interview(owner, question_count=question_count).json()
    return owner, created["session"]["id"], created["current_question"]["id"]


def llm_lines(app_logs):
    return [r.getMessage() for r in app_logs.records if r.name == "app.llm"]


def test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(
    start_interview, make_user, answer, llm, clock, budget, app_logs
):  # AC18, EC20
    owner, session_id, q1 = start(start_interview, make_user)
    llm.script_decide(LLMTimeoutError("no answer"), on_call=lambda: clock.advance(DECIDE_MAX_SECONDS))

    body = answer(owner, session_id, q1).json()

    assert llm.decide.budgets == [DECIDE_MAX_SECONDS]
    assert llm.fake.budgets[-1] == 30.0 - DECIDE_MAX_SECONDS >= WRITE_RESERVE_SECONDS
    assert body["current_question"]["question_kind"] == "main"
    [summary] = [line for line in llm_lines(app_logs) if line.startswith("turn_summary")]
    assert "decision=none" in summary and "source=llm" in summary


def test_the_decide_budget_shrinks_so_the_write_reserve_is_never_used(
    start_interview, make_user, answer, llm, clock, budget
):  # AC18
    owner, session_id, q1 = start(start_interview, make_user)
    budget(12.0)

    answer(owner, session_id, q1)

    assert llm.decide.budgets == [12.0 - WRITE_RESERVE_SECONDS]


def test_a_failed_decide_call_is_not_retried_with_the_last_seconds(
    start_interview, make_user, answer, llm, clock, budget
):  # AC18, EC21
    owner, session_id, q1 = start(start_interview, make_user)
    llm.script_decide("not json", on_call=lambda: clock.advance(DECIDE_MAX_SECONDS - 3))

    body = answer(owner, session_id, q1).json()

    assert len(llm.decide.calls) == 1
    assert body["current_question"]["question_kind"] == "main" and len(llm.fake.calls) == 2


def test_no_write_call_starts_below_its_minimum_and_the_bank_asks(
    start_interview, make_user, answer, llm, clock, budget, decision_json, app_logs, db
):  # AC13, AC20, EC6
    owner, session_id, q1 = start(start_interview, make_user)
    llm.script_decide(
        decision_json("follow_up", "no_how"), on_call=lambda: clock.advance(30.0 - MIN_SECONDS_FOR_WRITE + 1)
    )

    body = answer(owner, session_id, q1).json()

    assert len(llm.fake.calls) == 1  # only the opening question
    assert body["reaction"] is not None and body["current_question"]["question_kind"] == "main"
    [summary] = [line for line in llm_lines(app_logs) if line.startswith("turn_summary")]
    assert "override=no_time" in summary and "source=bank" in summary and "fallback=no_time" in summary


def test_a_write_retry_is_skipped_below_the_retry_minimum(
    start_interview, make_user, answer, llm, clock, budget, reply_json
):  # AC13
    llm.script(reply_json("Opening?", "behavioral"), "not json", on_call=lambda: clock.advance(26))
    owner, session_id, q1 = start(start_interview, make_user)

    body = answer(owner, session_id, q1).json()

    assert len(llm.fake.calls) == 2
    assert body["current_question"]["text"].startswith("Question b")  # from the fixture bank


def test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only(
    start_interview, make_user, answer, llm, budget, reply_json, decision_json, app_logs, db
):  # AC10, AC19
    owner, session_id, q1 = start(start_interview, make_user)
    secret_note = "Talked about the SECRET-NOTE project."
    llm.script_decide(result(decision_json(note=secret_note), 100, 10, 300))
    llm.script(result(reply_json("SECRET-QUESTION?", "behavioral"), 200, 20, 500))

    answer(owner, session_id, q1, text="SECRET-ANSWER text.")

    from app.modules.interviews.models.interviews_model import InterviewQuestion

    q2 = db.query(InterviewQuestion).filter_by(position=2).one()
    assert (q2.prompt_tokens, q2.completion_tokens, q2.latency_ms) == (300, 30, 800)
    lines = llm_lines(app_logs)
    decide_line = next(line for line in lines if "task=follow_up_decision" in line)
    write_line = next(line for line in lines if "task=interviewer_turn" in line and "SECRET" not in line)
    assert "action=next_question" in decide_line and "gap=-" in decide_line and "budget_left_ms=30000" in decide_line
    assert "budget_left_ms=" in write_line and "prompt_version=interviewer_v4" in write_line
    for line in lines:
        assert "SECRET" not in line
    assert json.loads(decision_json())["action"] == "next_question"
