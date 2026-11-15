import random

import pytest

from app.core.ai.provider import LLMRateLimitError, LLMRequestError, LLMServerError
from app.core.ai.retry import (
    parse_retry_after,
    raise_for_status,
    retry_delay,
    run_with_retries,
)


@pytest.fixture
def anyio_backend():
    return "asyncio"


def delay_for(exc, *, elapsed=0.0, budget=30.0):
    return retry_delay(exc, attempt=1, max_retries=2, elapsed=elapsed, budget=budget, rng=random.Random(0))


@pytest.mark.parametrize(("header", "seconds"), [("3", 3.0), ("0", 0.0), ("1.5", 1.5), (" 7 ", 7.0)])
def test_retry_after_in_seconds_is_read(header, seconds):
    assert parse_retry_after(header) == seconds


@pytest.mark.parametrize("header", [None, "", "Wed, 21 Oct 2026 07:28:00 GMT", "-5", "nan", "inf", "soon"])
def test_anything_but_plain_seconds_counts_as_not_said(header):
    assert parse_retry_after(header) is None


@pytest.mark.parametrize(("status", "error"), [(429, LLMRateLimitError), (503, LLMServerError)])
def test_a_transient_error_carries_the_wait_the_vendor_asked_for(status, error):
    with pytest.raises(error) as exc:
        raise_for_status(status, "12")

    assert exc.value.retry_after == 12.0


def test_without_the_header_the_error_has_no_wait():
    with pytest.raises(LLMRateLimitError) as exc:
        raise_for_status(429)

    assert exc.value.retry_after is None


def test_a_rejected_request_is_not_retried_whatever_the_header_says():
    with pytest.raises(LLMRequestError) as exc:
        raise_for_status(400, "12")

    assert exc.value.retry_after is None


def test_the_retry_waits_at_least_as_long_as_the_vendor_asked():
    assert delay_for(LLMRateLimitError("slow down", retry_after=10)) == 10  # the 0.5 s backoff alone would be too soon


def test_a_shorter_ask_than_the_backoff_does_not_shorten_it():
    assert 0.5 <= delay_for(LLMRateLimitError("slow down", retry_after=0)) <= 0.75


def test_no_ask_keeps_the_plain_backoff():
    assert 0.5 <= delay_for(LLMRateLimitError("slow down")) <= 0.75


@pytest.mark.parametrize(("ask", "elapsed"), [(40, 0.0), (20, 15.0)])
def test_it_gives_up_when_the_asked_wait_does_not_fit_the_budget(ask, elapsed):
    assert delay_for(LLMRateLimitError("slow down", retry_after=ask), elapsed=elapsed, budget=30.0) is None


# --- run_with_retries: the attempt loop every vendor adapter shares ---


class Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    async def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def scripted(*steps, clock: Clock, cost: float = 0.0):
    """An attempt function that returns or raises each step in turn; records the remaining budget it was given."""
    remaining: list[float] = []
    queue = list(steps)

    async def attempt(left: float):
        remaining.append(left)
        clock.now += cost
        step = queue.pop(0)
        if isinstance(step, Exception):
            raise step
        return step

    return attempt, remaining


async def run(attempt, clock: Clock, *, max_retries=2, budget=20.0):
    return await run_with_retries(
        attempt, max_retries=max_retries, budget=budget, clock=clock, sleep=clock.sleep, rng=random.Random(0)
    )


@pytest.mark.anyio
async def test_a_first_success_returns_at_once_with_one_attempt():
    clock = Clock()
    attempt, remaining = scripted("ok", clock=clock, cost=0.25)

    result = await run(attempt, clock)

    assert (result.value, result.attempts, result.latency_ms) == ("ok", 1, 250)
    assert remaining == [20.0]
    assert clock.sleeps == []


@pytest.mark.anyio
async def test_a_retryable_failure_then_success_takes_two_attempts_and_one_wait():
    clock = Clock()
    attempt, remaining = scripted(LLMServerError("down"), "ok", clock=clock)

    result = await run(attempt, clock)

    assert (result.value, result.attempts) == ("ok", 2)
    assert len(clock.sleeps) == 1
    assert remaining[1] == pytest.approx(20.0 - clock.sleeps[0])  # the second attempt gets what is left of the budget


@pytest.mark.anyio
async def test_a_non_retryable_failure_is_raised_at_once_with_attempts_and_latency():
    clock = Clock()
    attempt, _ = scripted(LLMRequestError("bad key", status_code=401), clock=clock, cost=0.1)

    with pytest.raises(LLMRequestError) as exc:
        await run(attempt, clock)

    assert (exc.value.attempts, exc.value.latency_ms) == (1, 100)
    assert clock.sleeps == []


@pytest.mark.anyio
async def test_retries_stop_at_max_retries():
    clock = Clock()
    attempt, remaining = scripted(LLMServerError("1"), LLMServerError("2"), clock=clock)

    with pytest.raises(LLMServerError) as exc:
        await run(attempt, clock, max_retries=1)

    assert exc.value.attempts == 2
    assert len(remaining) == 2


@pytest.mark.anyio
async def test_no_attempt_starts_once_the_wait_would_pass_the_budget():
    clock = Clock()
    attempt, remaining = scripted(LLMRateLimitError("slow down", retry_after=30), "never", clock=clock)

    with pytest.raises(LLMRateLimitError) as exc:
        await run(attempt, clock, budget=20.0)

    assert exc.value.attempts == 1
    assert len(remaining) == 1
