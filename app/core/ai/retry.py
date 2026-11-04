"""Retry rules shared by every vendor client in `core/ai` (the LLM provider and the transcriber).

One place decides which failures are worth another attempt and how long to wait, so both vendors behave the same:
retry only timeouts, 429 and 5xx, back off exponentially with jitter, and never start an attempt the caller would
wait for past the total budget.
"""

import random

from .provider import LLMError, LLMRateLimitError, LLMRequestError, LLMServerError

BACKOFF_BASE_SECONDS = 0.5


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
    # Give up rather than start a retry the user would wait for past the budget.
    if elapsed + delay >= budget:
        return None
    return delay


def raise_for_status(status: int) -> None:
    """Map a vendor's HTTP status to the typed errors; 200 passes."""
    if status == 429:
        raise LLMRateLimitError("LLM rate limited", status_code=status)
    if status >= 500:
        raise LLMServerError("LLM provider error", status_code=status)
    if status != 200:
        raise LLMRequestError("LLM request rejected", status_code=status)
