"""The logging pipeline (U1 structlog): what actually lands in the log file and on the console."""

import datetime
import json
import logging
import uuid

import pytest

from app.core.logging import RECORD_KEYS, REDACTED, ReadableRenderer, get_logger

SECRET = "my secret answer text"


# --- the file: one JSON object per line ---


def test_a_stdlib_call_outside_a_request_is_one_json_line(log_lines):  # AC2, EC1
    logging.getLogger("app.llm").info("llm_call task=%s", "write")

    [line] = log_lines.lines()
    assert set(RECORD_KEYS) <= line.keys()
    assert (line["event"], line["logger"], line["level"], line["request_id"]) == ("llm_call task=write", "app.llm", "info", "-")


def test_a_structlog_event_keeps_its_fields_typed(log_lines):
    get_logger("app.llm").info("llm_call", task="write", latency_ms=430, cached_tokens=None, cancelled=False)

    [line] = log_lines.lines()
    assert line["event"] == "llm_call"
    assert (line["task"], line["latency_ms"], line["cached_tokens"], line["cancelled"]) == ("write", 430, None, False)


# --- redaction ---


@pytest.mark.parametrize("key", ["answer", "resume", "job_description", "token", "password", "authorization"])
def test_a_sensitive_key_is_masked_in_the_file_and_on_the_console(capture_logs, key):  # AC1
    logs = capture_logs(debug=True)

    get_logger("app.test").info("event_with_pii", **{key: SECRET})

    [line] = logs.lines()
    assert line[key] == REDACTED
    assert SECRET not in logs.path.read_text(encoding="utf-8")
    assert SECRET not in logs.console() and REDACTED in logs.console()


def test_a_nested_or_mixed_case_sensitive_key_is_masked(log_lines):  # EC2
    get_logger("app.test").info("nested", data={"Answer": SECRET, "items": [{"PASSWORD": SECRET}], "count": 2})

    [line] = log_lines.lines()
    assert line["data"] == {"Answer": REDACTED, "items": [{"PASSWORD": REDACTED}], "count": 2}


def test_a_key_that_only_contains_a_sensitive_word_is_kept(log_lines):
    get_logger("app.llm").info("llm_call", prompt_tokens=12, cached_tokens=3)

    [line] = log_lines.lines()
    assert (line["prompt_tokens"], line["cached_tokens"]) == (12, 3)


# --- values and exceptions ---


def test_a_value_json_cannot_encode_is_written_as_text(log_lines):  # AC9, EC5
    session = uuid.UUID(int=10)
    moment = datetime.datetime(2026, 11, 26, 9, 0, tzinfo=datetime.UTC)

    get_logger("app.test").info("odd_values", session=session, at=moment, error=ValueError("bad"), thing=object())

    [line] = log_lines.lines()
    assert (line["session"], line["at"], line["error"]) == (str(session), str(moment), "bad")
    assert line["thing"].startswith("<object object")


def test_a_logged_exception_is_one_line_with_the_traceback(log_lines):  # AC11, EC7
    try:
        raise RuntimeError("boom")
    except RuntimeError:
        logging.getLogger("app.errors").exception("unhandled_exception")
        get_logger("app.errors").exception("stream_turn_failed")

    lines = log_lines.lines()
    assert len(lines) == 2
    assert all("Traceback" in line["exception"] and "RuntimeError: boom" in line["exception"] for line in lines)


# --- library loggers ---


@pytest.mark.parametrize("name", ["uvicorn.error", "sqlalchemy.engine", "httpx"])
def test_library_warnings_land_in_the_file_as_json(log_lines, name):  # AC6
    logging.getLogger(name).warning("library said %s", "hello")

    [line] = log_lines.lines()
    assert (line["logger"], line["event"], line["level"]) == (name, "library said hello", "warning")


def test_library_info_lines_stay_out_of_the_file(log_lines):
    # httpx logs every request URL at INFO; those can carry query-string keys.
    logging.getLogger("httpx").info("HTTP Request: GET https://example.test/?key=abc")

    assert log_lines.lines() == []


# --- the console ---


def test_debug_on_gives_the_readable_console(capture_logs):  # AC5
    logs = capture_logs(debug=True)

    get_logger("app.llm").error("llm_call", session="01a1", model=None, latency_ms=191, outcome="LLMRequestError")

    lines = logs.console().splitlines()
    assert lines[0].endswith("ERROR   [-       ] app.llm: llm_call")
    assert lines[1:] == [
        "    session     01a1",
        "    model       -",
        "    latency_ms  191",
        "    outcome     LLMRequestError",
    ]
    assert "\x1b[" not in logs.console()  # not a terminal: no colour codes


def test_debug_off_gives_json_on_the_console_like_the_file(capture_logs):  # AC5
    logs = capture_logs(debug=False)

    get_logger("app.llm").info("llm_call", task="write")

    [console_line] = logs.console().splitlines()
    [file_line] = logs.lines()
    assert json.loads(console_line) == file_line


def test_the_readable_console_keeps_free_text_on_one_line(capture_logs):
    logs = capture_logs(debug=True)

    logging.getLogger("app.request").info("POST /api/v1/interviews -> 201 (548.9ms)")

    assert logs.console().rstrip("\n").endswith("INFO    [-       ] app.request: POST /api/v1/interviews -> 201 (548.9ms)")


def test_the_readable_console_colours_outcome_by_success():
    render = ReadableRenderer(use_color=True)
    base = {"timestamp": "2026-11-26T09:00:00Z", "logger": "app.llm", "request_id": "-", "event": "llm_call"}

    ok = render(None, "info", {**base, "level": "info", "outcome": "summary_ok"})
    failed = render(None, "error", {**base, "level": "error", "outcome": "LLMRequestError"})

    assert "\x1b[1;32msummary_ok\x1b[0m" in ok
    assert "\x1b[1;31mLLMRequestError\x1b[0m" in failed


def test_the_readable_console_appends_the_traceback(capture_logs):
    logs = capture_logs(debug=True)
    try:
        raise RuntimeError("boom")
    except RuntimeError:
        get_logger("app.errors").exception("unhandled_exception")

    assert "Traceback" in logs.console() and "RuntimeError: boom" in logs.console()


# --- an unwritable log folder ---


def test_an_unwritable_log_folder_falls_back_to_the_console_with_one_warning(capture_logs, tmp_path):  # AC10, EC6
    blocker = tmp_path / "not-a-folder"
    blocker.write_text("", encoding="utf-8")

    logs = capture_logs(log_file=blocker / "app.log")
    get_logger("app.llm").info("llm_call", task="write")

    console = [json.loads(line) for line in logs.console().splitlines()]
    assert [line["event"] for line in console] == ["log_file_unavailable", "llm_call"]
    assert console[0]["level"] == "warning"
    assert not (blocker / "app.log").exists()
