"""Reading the app's own log back: what each request did for an interview, from logs/app.log.

Every turn leaves `llm_call`, `context_build` and `turn_summary` lines (plus one `app.request` line per HTTP call).
This turns them into `Turn`s: the start of an interview, then one per answer. The lines carry numbers, ids and
reason codes only, never question, answer or job-description text, so nothing read here can leak any.
"""

import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import NamedTuple

from app.core.logging import split_fields

from ..constants.interviews_constants import FEEDBACK_SCORE_TASK, FEEDBACK_WRITE_TASK

# One record of logs/app.log: `<date> <time> <LEVEL> [<request id>] <logger>: <message>`.
_LINE = re.compile(r"^\S+ \S+ \w+\s+\[(?P<request>[^\]]*)\] (?P<logger>[\w.]+): (?P<message>.*)$")
_HTTP = re.compile(r"^(?P<method>[A-Z]+) (?P<path>\S+) -> (?P<status>\d+) \((?P<ms>[\d.]+)ms\)$")
_FEEDBACK_TASKS = {FEEDBACK_SCORE_TASK, FEEDBACK_WRITE_TASK}


class LogEvent(NamedTuple):
    request: str
    logger: str
    event: str
    fields: dict[str, str]


class Call(NamedTuple):
    """One `llm_call` line, with the size the context builder estimated for its input (`context_build`)."""

    task: str
    model: str
    prompt_version: str
    prompt_tokens: int | None
    completion_tokens: int | None
    cached_tokens: int | None
    reasoning_tokens: int | None
    latency_ms: int | None
    budget_left_ms: int | None
    attempts: int | None
    finish: str
    est_tokens: int | None
    # The fixed system prompt's share of est_tokens: the part every call of this task repeats.
    system_tokens: int | None
    outcome: str
    action: str | None
    gap: str | None

    @property
    def tokens(self) -> int:
        return (self.prompt_tokens or 0) + (self.completion_tokens or 0)


@dataclass
class Turn:
    """One HTTP request that touched an interview: the start, or one answer."""

    request: str
    calls: list[Call]
    summary: dict[str, str] | None
    is_start: bool
    status: str | None
    http_ms: int | None
    label: str = "start"

    @property
    def llm_ms(self) -> int | None:
        if self.summary:
            return _int(self.summary.get("llm_ms"))
        known = [c.latency_ms for c in self.calls if c.latency_ms is not None]
        return sum(known) if known else None


def parse_log(lines: Iterable[str]) -> list[LogEvent]:
    """Lines that aren't a log record (the continuation lines of a traceback) are skipped."""
    events: list[LogEvent] = []
    for line in lines:
        if match := _LINE.match(line.rstrip("\n")):
            event, fields = split_fields(match["message"])
            events.append(LogEvent(match["request"], match["logger"], event, dict(fields)))
    return events


def group_requests(events: Iterable[LogEvent]) -> dict[str, list[LogEvent]]:
    """The events of each request, oldest request first (the id is on every line of one request)."""
    by_request: dict[str, list[LogEvent]] = {}
    for event in events:
        if event.request != "-":
            by_request.setdefault(event.request, []).append(event)
    return by_request


def turns_of(requests: dict[str, list[LogEvent]], session_id: str) -> list[Turn]:
    """The requests that logged this session, oldest first: the start, then one numbered turn per answer. A feedback
    request is not a turn (its cost is stored on the feedback row), so it is left out rather than shown as failed."""
    turns: list[Turn] = []
    answers = 0
    for request, events in requests.items():
        if not any(e.fields.get("session") == session_id for e in events):
            continue
        tasks = {e.fields.get("task") for e in events if e.event == "llm_call"}
        if tasks and tasks <= _FEEDBACK_TASKS:
            continue
        turn = _turn(request, events)
        if turn.summary is not None:
            answers += 1
            turn.label = str(answers)
        elif not turn.is_start:
            turn.label = "partial"  # LLM calls logged but no turn_summary: the request failed part-way
        turns.append(turn)
    return turns


def _turn(request: str, events: Sequence[LogEvent]) -> Turn:
    estimates: dict[str, tuple[int | None, int | None]] = {}
    calls: list[Call] = []
    summary: dict[str, str] | None = None
    http: re.Match[str] | None = None
    for event in events:
        f = event.fields
        if event.event == "context_build":
            estimates[f.get("task", "")] = (_int(f.get("est_tokens")), _int(f.get("system_tokens")))
        elif event.event == "llm_call":
            task = f.get("task", "-")
            est, system = estimates.pop(task, (None, None))
            calls.append(
                Call(
                    task,
                    f.get("model", "-"),
                    f.get("prompt_version", "-"),
                    _int(f.get("prompt_tokens")),
                    _int(f.get("completion_tokens")),
                    _int(f.get("cached_tokens")),
                    _int(f.get("reasoning_tokens")),
                    _int(f.get("latency_ms")),
                    _int(f.get("budget_left_ms")),
                    _int(f.get("attempts")),
                    f.get("finish", "-"),
                    est,
                    system,
                    f.get("outcome", "-"),
                    f.get("action"),
                    f.get("gap"),
                )
            )
        elif event.event == "turn_summary":
            summary = f
        elif event.logger == "app.request":
            http = _HTTP.match(event.event) or http
    return Turn(
        request,
        calls,
        summary,
        is_start=bool(http) and http["method"] == "POST" and http["path"].endswith("/interviews"),
        status=http["status"] if http else None,
        http_ms=round(float(http["ms"])) if http else None,
    )


def _int(value: str | None) -> int | None:
    return int(value) if value is not None and value.isdigit() else None  # "-" means the provider didn't say
