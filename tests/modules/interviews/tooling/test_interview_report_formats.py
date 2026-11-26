"""The interview report must not move when the log format changes (U1 structlog, AC8).

`data/legacy_interview.log` is one interview written in the old text format, and `data/legacy_interview_report.txt`
is the report it gave. Both were produced once, before the format changed, from the text-format version of
`emit_golden_interview` below; the same interview is now emitted through the structlog events.
Any later log format has to give exactly the same report for the same interview.
"""

import logging
import uuid
from pathlib import Path

import pytest
import structlog

from app.core.ai.provider import LLMServerError
from app.core.ai.retry import RetryPolicy
from app.core.logging import bind_log_context, get_logger
from app.modules.interviews.ai.interviews_turn_log import (
    log_llm_call,
    log_retrieval,
    log_stream_summary,
    log_turn_summary,
)
from app.modules.interviews.constants.interviews_constants import (
    DECISION_TASK,
    FEEDBACK_SCORE_TASK,
    FEEDBACK_WRITE_TASK,
    INTERVIEWER_TASK,
    SUMMARY_TASK,
)
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from app.modules.interviews.tooling.interviews_log import parse_log
from app.modules.interviews.tooling.interviews_report import analyze_interview
from app.modules.interviews.tooling.interviews_report_render import render_text

DATA = Path(__file__).parent / "data"
LEGACY_LOG = DATA / "legacy_interview.log"
LEGACY_REPORT = DATA / "legacy_interview_report.txt"

S = uuid.UUID(int=10)
OTHER = uuid.UUID(int=11)
BUDGET = 30.0


# --- the interview: a start with reference notes, a follow-up turn, a move-on turn (streamed, cache hit), a request
# that failed half-way, a feedback request, another interview's request and a startup line outside any request ---


def _context_build(task, est, system=700):
    get_logger("app.llm.context").info(
        "context_build", task=task, strategy="window_ledger", est_tokens=est, system_tokens=system, dropped=0,
        outcome="ok", ledger=0, notes=0, summary=1, turns_full=1,
    )  # fmt: skip


def _call(session_id, task, version, *, prompt, completion, ms, left, est, outcome="ok", cached=None, action=None,
          gap=None, attempts=1, finish="stop"):  # fmt: skip
    bind_log_context(session=str(session_id))
    _context_build(task, est)
    log_llm_call(
        logging.INFO, outcome, task=task, prompt_version=version, model="test-model", prompt_tokens=prompt,
        completion_tokens=completion, cached_tokens=cached, latency_ms=ms, attempts=attempts, finish=finish,
        budget_left_ms=left, action=action, gap=gap,
    )  # fmt: skip


def _http(method, path, status, ms):
    get_logger("app.request").info("http_request", method=method, path=path, status=status, duration_ms=ms)


def emit_golden_interview():
    structlog.contextvars.clear_contextvars()
    get_logger("app.llm").warning("LLM startup line outside any request")

    structlog.contextvars.clear_contextvars()
    bind_log_context(request_id="req-start")
    bind_log_context(session=str(S))
    log_retrieval(logging.INFO, mode="hybrid", scores=[0.8123, 0.7, None], outcome="ok", latency_ms=45, profile_notes=1)
    _call(S, SUMMARY_TASK, "job_description_summary_v2", prompt=444, completion=60, ms=9669, left=None, est=542, outcome="summary_ok")
    _call(S, INTERVIEWER_TASK, "interviewer_v4", prompt=824, completion=38, ms=6586, left=30000, est=926)
    _http("POST", "/api/v1/interviews", 201, 16300.1)

    structlog.contextvars.clear_contextvars()
    bind_log_context(request_id="req-1")
    _call(S, DECISION_TASK, "follow_up_decision_v1", prompt=777, completion=42, ms=9735, left=30000, est=1000, action="follow_up", gap="no_example")
    _call(S, INTERVIEWER_TASK, "interviewer_v4", prompt=943, completion=36, ms=12800, left=20265, est=1000)
    log_turn_summary(decision="follow_up:no_example", action="follow_up", source="llm", llm_ms=22536)
    _http("POST", f"/api/v1/interviews/{S}/messages", 201, 22556.4)

    structlog.contextvars.clear_contextvars()
    bind_log_context(request_id="req-2")
    _call(S, DECISION_TASK, "follow_up_decision_v1", prompt=700, completion=30, ms=2000, left=30000, est=800, action="next_question")
    _call(S, INTERVIEWER_TASK, "interviewer_v4", prompt=800, completion=30, ms=3000, left=28000, est=800, cached=400, attempts=2, finish="length")
    log_turn_summary(decision="next_question", action="next_question", override="cap_reached", source="llm", fallback="no_time", llm_ms=5000)
    log_stream_summary(terminal="done", first_event_ms=120, first_token_ms=2300, total_ms=5100, resets=1, cancelled=False)
    _http("POST", f"/api/v1/interviews/{S}/messages/stream", 200, 5120.0)

    structlog.contextvars.clear_contextvars()
    bind_log_context(request_id="req-crashed")
    _call(S, DECISION_TASK, "follow_up_decision_v1", prompt=700, completion=30, ms=100, left=30000, est=700, action="next_question")
    _http("POST", f"/api/v1/interviews/{S}/messages", 500, 150.0)

    structlog.contextvars.clear_contextvars()
    bind_log_context(request_id="req-feedback")
    _call(S, FEEDBACK_SCORE_TASK, "feedback_score_v1", prompt=3000, completion=900, ms=8000, left=60000, est=3000)
    _call(S, FEEDBACK_WRITE_TASK, "feedback_write_v1", prompt=1500, completion=300, ms=3000, left=52000, est=1500)
    _http("POST", f"/api/v1/interviews/{S}/feedback", 201, 11100.0)

    structlog.contextvars.clear_contextvars()
    bind_log_context(request_id="req-other")
    _call(OTHER, INTERVIEWER_TASK, "interviewer_v4", prompt=999, completion=99, ms=999, left=30000, est=999)
    _http("POST", "/api/v1/interviews", 201, 1000.0)
    structlog.contextvars.clear_contextvars()


def golden_session():
    return InterviewSession(
        id=S, user_id=uuid.UUID(int=1), role="backend", level="mid", interview_type="mixed", question_count=5, status="in_progress"
    )


def _question(position, kind="main", main=None, parent=None, decide=None, prompt=100, completion=10):
    return InterviewQuestion(
        id=uuid.UUID(int=100 + position), session_id=S, position=position, kind=kind, main_number=main or position,
        parent_question_id=parent, text="Secret question text", category="technical", source="llm",
        prompt_version="interviewer_v4", decision_prompt_version=decide, prompt_tokens=prompt,
        completion_tokens=completion, latency_ms=1000,
    )  # fmt: skip


GOLDEN_QUESTIONS = [
    _question(1, prompt=824, completion=38),
    _question(2, "follow_up", main=1, parent=uuid.UUID(int=101), decide="follow_up_decision_v1", prompt=1720, completion=78),
    _question(3, decide="follow_up_decision_v1", prompt=1530, completion=60),
]
GOLDEN_MESSAGES = [
    InterviewMessage(session_id=S, question_id=uuid.UUID(int=101), role="candidate", content="a" * 120),
    InterviewMessage(session_id=S, question_id=uuid.UUID(int=102), role="candidate", content="a" * 300),
]


def report_of(lines: list[str]) -> str:
    analysis = analyze_interview(golden_session(), GOLDEN_QUESTIONS, GOLDEN_MESSAGES, parse_log(lines), budget_seconds=BUDGET)
    return render_text(analysis)


def test_the_old_text_log_still_gives_the_saved_report():
    lines = LEGACY_LOG.read_text(encoding="utf-8").splitlines()

    assert report_of(lines) == LEGACY_REPORT.read_text(encoding="utf-8")


def test_the_same_interview_logged_as_json_gives_the_same_report(log_lines):  # AC8
    emit_golden_interview()

    lines = log_lines.path.read_text(encoding="utf-8").splitlines()
    assert lines and all(line.startswith("{") for line in lines)
    assert report_of(lines) == LEGACY_REPORT.read_text(encoding="utf-8")


def test_a_call_logged_without_a_session_still_reports(log_lines):  # EC10
    emit_golden_interview()
    bind_log_context(request_id="req-orphan")
    log_llm_call(logging.INFO, "ok", task=INTERVIEWER_TASK, model="test-model", latency_ms=5, attempts=1)

    lines = log_lines.path.read_text(encoding="utf-8").splitlines()
    assert report_of(lines) == LEGACY_REPORT.read_text(encoding="utf-8")


def test_retry_events_in_the_log_leave_the_report_unchanged(log_lines):  # U2 AC15, EC20
    emit_golden_interview()
    bind_log_context(request_id="req-2", session=str(S))
    clock = iter(range(100))
    policy = RetryPolicy(
        max_retries=1, task=INTERVIEWER_TASK, logger=get_logger("app.llm"), clock=lambda: next(clock), sleep=lambda s: None
    )

    def always_down(_left):
        raise LLMServerError("down")

    with pytest.raises(LLMServerError):
        policy.call(always_down, budget=BUDGET)
    structlog.contextvars.clear_contextvars()

    lines = log_lines.path.read_text(encoding="utf-8").splitlines()
    assert any('"retry_wait"' in line for line in lines) and any('"retry_giveup"' in line for line in lines)
    assert report_of(lines) == LEGACY_REPORT.read_text(encoding="utf-8")
