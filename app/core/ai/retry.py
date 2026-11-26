"""Transport retry rules shared by every vendor client in `core/ai` (the LLM provider, the embedder, the transcriber
and the synthesizer).

The AI call layer has two retry layers, kept apart on purpose:
- Transport retries (here, `RetryPolicy` on tenacity): the call never got an answer (a timeout, a 429, a 5xx). Retry
  only those, wait a random time from 0 up to a doubling cap (full jitter), never sooner than the vendor's
  Retry-After, and never start an attempt the caller would wait for past the total budget.
- Content retries (`app/modules/interviews/ai/interviews_reply_attempts.py`): the model answered, but the answer was
  malformed. No backoff and no HTTP errors; an `LLMError` from this layer stops them.

Worst case, one LLM task makes (llm_max_retries + 1) x MAX_REPLY_ATTEMPTS HTTP calls (3 x 2 = 6 with the defaults);
`tests/core/ai/test_retry_budget.py` pins it so a new layer can't silently multiply it.
"""

import math
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

import anyio
from tenacity import (
    AsyncRetrying,
    RetryCallState,
    Retrying,
    retry_if_exception,
    stop_after_attempt,
    stop_any,
    wait_random_exponential,
)

from app.core.logging import Logger

from .provider import LLMError, LLMRateLimitError, LLMRequestError, LLMServerError

# Full jitter: each wait is a random value from 0 up to 0.5 s, 1 s, 2 s, ... (doubling per attempt).
_jitter = wait_random_exponential(multiplier=0.5)


@dataclass(frozen=True)
class Attempted[T]:
    """What one call returned, plus how many attempts and how long it took (for the caller's log line)."""

    value: T
    attempts: int
    latency_ms: int


class _Call:
    """The state of one call (its start, budget, attempt count and event label). Built per call, never kept on the
    policy."""

    def __init__(self, clock: Callable[[], float], budget: float, task: str):
        self.clock, self.budget, self.task = clock, budget, task
        self.start = clock()
        self.attempts = 0

    def elapsed(self) -> float:
        return self.clock() - self.start

    def latency_ms(self) -> int:
        return round(self.elapsed() * 1000)

    def stamp(self, exc: LLMError) -> None:
        exc.attempts, exc.latency_ms = self.attempts, self.latency_ms()


class RetryPolicy:
    """The transport retry rules for one vendor adapter, on tenacity.

    It holds configuration only: one adapter (so one policy) serves concurrent requests, and `complete` runs in worker
    threads, so every call builds its own tenacity object and its own attempt count.
    """

    def __init__(
        self,
        *,
        max_retries: int,
        task: str,
        logger: Logger,
        clock: Callable[[], float] = time.perf_counter,
        sleep: Callable[[float], None] = time.sleep,
        async_sleep: Callable[[float], Awaitable[None]] = anyio.sleep,
    ):
        self._max_retries = max_retries
        self._task = task
        self._logger = logger
        self._clock = clock
        self._sleep = sleep
        self._async_sleep = async_sleep

    def call[T](self, attempt: Callable[[float], T], *, budget: float, task: str | None = None) -> Attempted[T]:
        """Run `attempt(remaining_budget)` until it returns or the rules say stop (sync callers only). `task` labels
        the retry events with the caller's task (e.g. `follow_up_decision`); without one, the adapter's label."""
        state = _Call(self._clock, budget, task or self._task)

        def once() -> T:
            state.attempts += 1
            try:
                return attempt(budget - state.elapsed())
            except LLMError as exc:
                state.stamp(exc)
                raise

        try:
            value = Retrying(sleep=self._sleep, **self._rules(state))(once)
        except LLMError as exc:
            self.log_giveup(exc, task=state.task)
            raise
        return Attempted(value=value, attempts=state.attempts, latency_ms=state.latency_ms())

    async def acall[T](
        self, attempt: Callable[[float], Awaitable[T]], *, budget: float, task: str | None = None
    ) -> Attempted[T]:
        """The same rules for an async attempt; waits are awaited, so the event loop stays free."""
        state = _Call(self._clock, budget, task or self._task)

        async def once() -> T:
            state.attempts += 1
            try:
                return await attempt(budget - state.elapsed())
            except LLMError as exc:
                state.stamp(exc)
                raise

        try:
            value = await AsyncRetrying(sleep=self._async_sleep, **self._rules(state))(once)
        except LLMError as exc:
            self.log_giveup(exc, task=state.task)
            raise
        return Attempted(value=value, attempts=state.attempts, latency_ms=state.latency_ms())

    def _rules(self, state: _Call) -> dict:
        def out_of_time(rs: RetryCallState) -> bool:
            # tenacity runs `wait` before `stop`, so the coming wait is known here. Read on the adapter's clock, not
            # tenacity's, so a test's fake clock decides it too.
            return state.elapsed() + rs.upcoming_sleep >= state.budget

        return {
            "retry": retry_if_exception(_transient),
            "stop": stop_any(stop_after_attempt(self._max_retries + 1), out_of_time),
            "wait": _wait,
            "before_sleep": lambda rs: self._log_wait(rs, state.task),
            "reraise": True,
        }

    # Fixed event names and fields, never a payload: a later report reads them, joined to `llm_call` by request_id.
    def _log_wait(self, rs: RetryCallState, task: str) -> None:
        self._logger.info(
            "retry_wait",
            task=task,
            attempt=rs.attempt_number,
            wait_seconds=round(rs.upcoming_sleep, 3),
            error_class=type(rs.outcome.exception()).__name__,  # type: ignore[union-attr]
        )

    def log_giveup(self, exc: LLMError, *, task: str | None = None) -> None:
        """Log why a stamped error ends the call. Public for the stream, whose failure after output never reaches the
        retry loop. The reason is derived after the failure, in one place: no tenacity callbacks to coordinate."""
        if not exc.retryable or exc.after_output:
            reason = "not_retryable"
        elif exc.attempts > self._max_retries:
            reason = "max_attempts"
        else:
            reason = "deadline"
        self._logger.warning(
            "retry_giveup",
            task=task or self._task,
            attempts=exc.attempts,
            elapsed_ms=exc.latency_ms,
            error_class=type(exc).__name__,
            reason=reason,
        )


def _transient(exc: BaseException) -> bool:
    # Timeouts, 429 and 5xx only; a rejected request or a bad response would fail the same way again.
    return isinstance(exc, LLMError) and exc.retryable


def _wait(rs: RetryCallState) -> float:
    wait = _jitter(rs)
    retry_after = rs.outcome.exception().retry_after  # type: ignore[union-attr]  # only LLMErrors are retried
    # The vendor knows when its limit resets; retrying sooner only burns an attempt on another 429.
    return wait if retry_after is None else max(wait, retry_after)


def parse_retry_after(value: str | None) -> float | None:
    """The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP date, a negative number or
    anything garbled counts as 'not said', so the normal backoff applies."""
    if value is None:
        return None
    try:
        seconds = float(value)
    except ValueError:
        return None
    return seconds if math.isfinite(seconds) and seconds >= 0 else None


def raise_for_status(status: int, retry_after: str | None = None) -> None:
    """Map a vendor's HTTP status to the typed errors; 200 passes. `retry_after` is the raw Retry-After header."""
    wait = parse_retry_after(retry_after)
    if status == 429:
        raise LLMRateLimitError("LLM rate limited", status_code=status, retry_after=wait)
    if status >= 500:
        raise LLMServerError("LLM provider error", status_code=status, retry_after=wait)
    if status != 200:
        raise LLMRequestError("LLM request rejected", status_code=status)
