"""Retry rules shared by every vendor client in `core/ai` (the LLM provider, the transcriber and the synthesizer).

One place decides which failures are worth another attempt and how long to wait, so all vendors behave the same:
retry only timeouts, 429 and 5xx, back off exponentially with jitter, and never start an attempt the caller would
wait for past the total budget. When the vendor says how long to wait (Retry-After), that is the minimum delay.
"""

import math
import random
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

from .provider import LLMError, LLMRateLimitError, LLMRequestError, LLMServerError

BACKOFF_BASE_SECONDS = 0.5


@dataclass(frozen=True)
class Attempted[T]:
    """What one call returned, plus how many attempts and how long it took (for the caller's log line)."""

    value: T
    attempts: int
    latency_ms: int


async def run_with_retries[T](
    attempt: Callable[[float], Awaitable[T]],
    *,
    max_retries: int,
    budget: float,
    clock: Callable[[], float],
    sleep: Callable[[float], Awaitable[None]],
    rng: random.Random,
) -> Attempted[T]:
    """Call `attempt(remaining_budget)` until it returns or `retry_delay` says stop.

    The async request/response adapters (Deepgram speech-to-text and text-to-speech) share this loop and only build
    their request and parse their response. The final `LLMError` carries `attempts` and `latency_ms`, so the caller can
    log them. The LLM provider keeps its own loops: its `complete` is sync, and a stream must never retry after it has
    yielded output.
    """
    start = clock()
    tries = 0
    while True:
        tries += 1
        try:
            value = await attempt(budget - (clock() - start))
        except LLMError as exc:
            exc.attempts, exc.latency_ms = tries, _elapsed_ms(clock, start)
            delay = retry_delay(
                exc, attempt=tries, max_retries=max_retries, elapsed=clock() - start, budget=budget, rng=rng
            )
            if delay is None:
                raise
            await sleep(delay)
            continue
        return Attempted(value=value, attempts=tries, latency_ms=_elapsed_ms(clock, start))


def _elapsed_ms(clock: Callable[[], float], start: float) -> int:
    return round((clock() - start) * 1000)


def backoff_seconds(attempt: int, rng: random.Random) -> float:
    # Exponential (0.5s, 1s, 2s, ...) plus jitter, so many clients don't retry in lockstep.
    delay = BACKOFF_BASE_SECONDS * 2 ** (attempt - 1)
    return delay + rng.uniform(0, delay / 2)


def retry_delay(
    exc: LLMError, *, attempt: int, max_retries: int, elapsed: float, budget: float, rng: random.Random
) -> float | None:
    """How long to wait before retrying `exc` after `attempt` attempts, or None to give up."""
    if not exc.retryable or attempt > max_retries:
        return None
    delay = backoff_seconds(attempt, rng)
    if exc.retry_after is not None:
        # The vendor knows when its limit resets; retrying sooner only burns an attempt on another 429.
        delay = max(delay, exc.retry_after)
    # Give up rather than start a retry the user would wait for past the budget.
    if elapsed + delay >= budget:
        return None
    return delay


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
