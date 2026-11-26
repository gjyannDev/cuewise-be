import json

import pytest

from app.modules.interviews.tooling.interviews_log import LogEvent, parse_log

TEXT = [
    "2026-11-15 20:18:53,416 INFO    [req-1] app.llm: llm_call session=s1 task=interviewer model=m latency_ms=120 cached_tokens=- outcome=ok",
    "2026-11-15 20:18:53,419 INFO    [req-1] app.request: POST /api/v1/interviews -> 201 (16300.1ms)",
]
JSON = [
    json.dumps({"timestamp": "2026-11-15T20:18:53Z", "level": "info", "logger": "app.llm", "request_id": "req-1",
                "event": "llm_call", "session": "s1", "task": "interviewer", "model": "m", "latency_ms": 120,
                "cached_tokens": None, "outcome": "ok"}),
    json.dumps({"timestamp": "2026-11-15T20:18:53Z", "level": "info", "logger": "app.request", "request_id": "req-1",
                "event": "http_request", "method": "POST", "path": "/api/v1/interviews", "status": 201,
                "duration_ms": 16300.1}),
]


def test_a_json_log_reads_the_same_as_the_text_log():
    assert parse_log(JSON) == parse_log(TEXT)


def test_a_log_that_changed_format_part_way_reads_as_one():
    assert parse_log([*TEXT, *JSON]) == parse_log(TEXT) * 2


def test_booleans_and_missing_values_read_like_the_text_format():
    line = json.dumps({"logger": "app.llm", "request_id": "r", "event": "stream_turn_summary", "cancelled": False, "first_token_ms": None})
    assert parse_log([line]) == [LogEvent("r", "app.llm", "stream_turn_summary", {"cancelled": "false", "first_token_ms": "-"})]


def test_lines_that_are_not_records_are_skipped():
    assert parse_log(["Traceback (most recent call last):", "{broken", '{"no_event": 1}', '["list"]']) == []


def test_an_old_text_line_splits_into_its_event_and_fields():
    line = "2026-11-15 20:18:53,416 INFO    [r] app.llm.context: context_build task=a dropped=0 "

    assert parse_log([line]) == [LogEvent("r", "app.llm.context", "context_build", {"task": "a", "dropped": "0"})]


@pytest.mark.parametrize("message", ["POST /api/v1/interviews -> 201 (548.9ms)", "llm_call", "LLM disabled: key empty"])
def test_an_old_text_line_without_key_values_keeps_its_message_whole(message):
    line = f"2026-11-15 20:18:53,416 WARNING [-] app.llm: {message}"

    assert parse_log([line]) == [LogEvent("-", "app.llm", message, {})]
