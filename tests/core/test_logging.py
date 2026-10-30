import logging
import sys

from app.core.logging import ConsoleFormatter, split_fields

LLM_CALL = "llm_call session=01a1 model=- prompt_version=interviewer_v2 latency_ms=191 outcome=LLMRequestError"


def _record(
    message: str,
    level: int = logging.INFO,
    request_id: str = "12d420d1c5ed42649a4f99371124887d",
):
    record = logging.LogRecord("app.llm", level, __file__, 1, message, None, None)
    record.request_id = request_id
    return record


def test_split_fields_reads_event_and_key_values():
    assert split_fields("context_build task=a dropped=0 ") == (
        "context_build",
        [("task", "a"), ("dropped", "0")],
    )


def test_split_fields_leaves_free_text_whole():
    message = "POST /api/v1/interviews -> 201 (548.9ms)"

    assert split_fields(message) == (message, [])
    assert split_fields("llm_call") == ("llm_call", [])
    assert split_fields("") == ("", [])


def test_console_puts_one_aligned_field_per_line():
    lines = (
        ConsoleFormatter(use_color=False)
        .format(_record(LLM_CALL, logging.ERROR))
        .splitlines()
    )

    assert lines[0].endswith("ERROR   [12d420d1] app.llm: llm_call")
    assert lines[1:] == [
        "    session         01a1",
        "    model           -",
        "    prompt_version  interviewer_v2",
        "    latency_ms      191",
        "    outcome         LLMRequestError",
    ]


def test_console_keeps_free_text_on_one_line():
    output = ConsoleFormatter(use_color=False).format(
        _record("POST /api/v1/interviews -> 201 (548.9ms)")
    )

    assert "\n" not in output
    assert output.endswith(
        "INFO    [12d420d1] app.llm: POST /api/v1/interviews -> 201 (548.9ms)"
    )


def test_console_colours_outcome_by_success():
    formatter = ConsoleFormatter(use_color=True)

    ok = formatter.format(_record("llm_call outcome=summary_ok"))
    failed = formatter.format(
        _record("llm_call outcome=LLMRequestError", logging.ERROR)
    )

    assert "\x1b[1;32msummary_ok\x1b[0m" in ok
    assert "\x1b[1;31mLLMRequestError\x1b[0m" in failed


def test_console_without_colour_has_no_escape_codes():
    assert "\x1b[" not in ConsoleFormatter(use_color=False).format(
        _record(LLM_CALL, logging.WARNING)
    )


def test_console_appends_the_traceback():
    try:
        raise RuntimeError("boom")
    except RuntimeError:
        record = _record("Unhandled RuntimeError: boom", logging.ERROR)
        record.exc_info = sys.exc_info()

    output = ConsoleFormatter(use_color=False).format(record)

    assert "Traceback" in output
    assert "RuntimeError: boom" in output
