"""Context management: the one place that decides what each LLM call sends.

The model keeps no memory, so every call is rebuilt from stored data. A *task* (one kind of call, e.g. the
interviewer's next question) owns named *strategies* (ways to turn that data into messages). The manager runs the
chosen strategy, estimates the size, trims the oldest entries when the strategy has a limit, and logs one
metadata-only line per build. Feature-agnostic: features register their own tasks and strategies.
"""

import logging
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, NamedTuple, Protocol

from .provider import ChatMessage

# Rough rule of thumb (~4 characters per token for English); real counts come from the provider's `usage`.
CHARS_PER_TOKEN = 4

logger = logging.getLogger("app.llm.context")


def estimate_tokens(messages: Sequence[ChatMessage]) -> int:
    return sum(len(m.content) for m in messages) // CHARS_PER_TOKEN


class StrategyOutput(NamedTuple):
    messages: list[ChatMessage]
    prompt_version: str
    # Numbers only (they go to the log): e.g. turns sent in full, ledger entries.
    counts: Mapping[str, int]


class Strategy(Protocol):
    # Estimated input tokens; None = never trimmed.
    limit: int | None

    def droppable(self, inputs: Any) -> int:
        """How many oldest entries may be dropped; everything else is required."""
        ...

    def build(self, inputs: Any, dropped: int) -> StrategyOutput: ...


@dataclass(frozen=True)
class Task:
    default: str
    strategies: Mapping[str, Strategy]


class ContextReport(NamedTuple):
    task: str
    strategy: str
    estimated_tokens: int
    system_tokens: int
    dropped: int
    counts: Mapping[str, int]


class BuiltContext(NamedTuple):
    messages: list[ChatMessage]
    prompt_version: str
    report: ContextReport


class ContextTooLargeError(Exception):
    """Even with every droppable entry gone the input is over the strategy's limit."""

    def __init__(self, report: ContextReport):
        super().__init__(f"context for {report.task} is too large")
        self.report = report


class ContextManager:
    def __init__(self, tasks: Mapping[str, Task]):
        self._tasks = tasks

    def build(self, task: str, inputs: Any, strategy: str | None = None) -> BuiltContext:
        if task not in self._tasks:
            raise ValueError(f"Unknown context task {task!r}; valid: {', '.join(self._tasks)}")
        spec = self._tasks[task]
        name = strategy or spec.default
        if name not in spec.strategies:
            raise ValueError(f"Unknown strategy {name!r} for {task}; valid: {', '.join(spec.strategies)}")
        chosen = spec.strategies[name]

        dropped = 0
        output = chosen.build(inputs, dropped)
        if chosen.limit is not None:
            most = chosen.droppable(inputs)
            while estimate_tokens(output.messages) > chosen.limit and dropped < most:
                dropped += 1
                output = chosen.build(inputs, dropped)

        report = ContextReport(
            task=task,
            strategy=name,
            estimated_tokens=estimate_tokens(output.messages),
            system_tokens=estimate_tokens([m for m in output.messages if m.role == "system"]),
            dropped=dropped,
            counts=output.counts,
        )
        if chosen.limit is not None and report.estimated_tokens > chosen.limit:
            _log(logging.WARNING, report, "too_large")
            raise ContextTooLargeError(report)
        _log(logging.INFO, report, "ok")
        return BuiltContext(output.messages, output.prompt_version, report)


def _log(level: int, report: ContextReport, outcome: str) -> None:
    counts = " ".join(f"{key}={value}" for key, value in sorted(report.counts.items()))
    logger.log(
        level,
        "context_build task=%s strategy=%s est_tokens=%s system_tokens=%s dropped=%s outcome=%s %s",
        report.task,
        report.strategy,
        report.estimated_tokens,
        report.system_tokens,
        report.dropped,
        outcome,
        counts,
    )
