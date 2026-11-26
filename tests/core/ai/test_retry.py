import asyncio
import random

import anyio
import pytest
from anyio.lowlevel import checkpoint

from app.core.ai.provider import (
    LLMBadResponseError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.ai.retry import RetryPolicy, parse_retry_after, raise_for_status
from app.core.logging import RECORD_KEYS, get_logger


@pytest.fixture
def anyio_backend():
    return "asyncio"


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


# --- RetryPolicy: the transport retry rules every vendor adapter shares, through its sync and its async call ---


class Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds

    async def async_sleep(self, seconds: float) -> None:
        self.sleep(seconds)
        await checkpoint()  # let a concurrent call run, as a real wait would


def make_policy(clock: Clock, *, max_retries: int = 2) -> RetryPolicy:
    return RetryPolicy(
        max_retries=max_retries,
        clock=clock,
        sleep=clock.sleep,
        async_sleep=clock.async_sleep,
        task="test",
        logger=get_logger("app.llm"),
    )


def scripted(*steps, clock: Clock, cost: float = 0.0):
    """An attempt that returns or raises each step in turn; records the remaining budget it was given."""
    remaining: list[float] = []
    queue = list(steps)

    def attempt(left: float):
        remaining.append(left)
        clock.now += cost
        step = queue.pop(0)
        if isinstance(step, BaseException):
            raise step
        return step

    return attempt, remaining


@pytest.fixture(params=["sync", "async"])
def run(request):
    """Run an attempt through the policy's sync `call` or its async `acall`: both must behave the same."""

    async def _run(policy: RetryPolicy, attempt, *, budget: float = 20.0):
        if request.param == "sync":
            return policy.call(attempt, budget=budget)

        async def async_attempt(left: float):
            return attempt(left)

        return await policy.acall(async_attempt, budget=budget)

    return _run


@pytest.mark.anyio
async def test_a_first_success_returns_at_once_with_one_attempt(run):
    clock = Clock()
    attempt, remaining = scripted("ok", clock=clock, cost=0.25)

    result = await run(make_policy(clock), attempt)

    assert (result.value, result.attempts, result.latency_ms) == ("ok", 1, 250)
    assert remaining == [20.0]
    assert clock.sleeps == []


@pytest.mark.anyio
@pytest.mark.parametrize("error", [LLMServerError("down"), LLMTimeoutError("slow"), LLMRateLimitError("busy")])
async def test_a_transient_failure_then_success_takes_two_attempts_and_one_wait(run, error):
    clock = Clock()
    attempt, remaining = scripted(error, "ok", clock=clock)

    result = await run(make_policy(clock), attempt)

    assert (result.value, result.attempts) == ("ok", 2)
    assert len(clock.sleeps) == 1
    assert remaining[1] == pytest.approx(20.0 - clock.sleeps[0])  # the second attempt gets what is left of the budget


@pytest.mark.anyio
async def test_each_wait_is_a_random_value_up_to_its_doubling_cap(run):
    random.seed(7)
    clock = Clock()
    attempt, _ = scripted(*[LLMServerError("down")] * 6, clock=clock)

    with pytest.raises(LLMServerError):
        await run(make_policy(clock, max_retries=5), attempt, budget=1000.0)

    assert len(clock.sleeps) == 5
    for n, wait in enumerate(clock.sleeps):
        assert 0 <= wait <= 0.5 * 2**n


@pytest.mark.anyio
async def test_the_retry_waits_at_least_as_long_as_the_vendor_asked(run):
    clock = Clock()
    attempt, _ = scripted(LLMRateLimitError("slow down", retry_after=10), "ok", clock=clock)

    await run(make_policy(clock), attempt)

    assert clock.sleeps == [10]  # the 0 to 0.5 s backoff alone would be too soon


@pytest.mark.anyio
async def test_a_shorter_ask_than_the_backoff_does_not_shorten_it(run):
    random.seed(3)
    clock = Clock()
    attempt, _ = scripted(LLMRateLimitError("slow down", retry_after=0), "ok", clock=clock)

    await run(make_policy(clock), attempt)
    random.seed(3)
    expected = random.uniform(0, 0.5)

    assert clock.sleeps == [pytest.approx(expected)]  # the jittered backoff, not the vendor's 0


@pytest.mark.anyio
@pytest.mark.parametrize(
    "error", [LLMRequestError("bad key", status_code=401), LLMBadResponseError("no message")]
)
async def test_a_non_retryable_failure_is_raised_at_once_with_attempts_and_latency(run, error):
    clock = Clock()
    attempt, remaining = scripted(error, "never", clock=clock, cost=0.1)

    with pytest.raises(type(error)) as exc:
        await run(make_policy(clock), attempt)

    assert (exc.value.attempts, exc.value.latency_ms) == (1, 100)
    assert len(remaining) == 1
    assert clock.sleeps == []


@pytest.mark.anyio
async def test_an_exception_that_is_not_an_llm_error_propagates_unchanged(run):
    clock = Clock()
    bug = ValueError("a bug")
    attempt, remaining = scripted(bug, "never", clock=clock)

    with pytest.raises(ValueError) as exc:
        await run(make_policy(clock), attempt)

    assert exc.value is bug
    assert not hasattr(exc.value, "attempts")
    assert len(remaining) == 1


@pytest.mark.anyio
async def test_retries_stop_at_max_retries(run):
    clock = Clock()
    attempt, remaining = scripted(LLMServerError("1"), LLMServerError("2"), "never", clock=clock)

    with pytest.raises(LLMServerError) as exc:
        await run(make_policy(clock, max_retries=1), attempt)

    assert exc.value.attempts == 2
    assert len(remaining) == 2


@pytest.mark.anyio
async def test_zero_max_retries_means_exactly_one_attempt(run):
    clock = Clock()
    attempt, remaining = scripted(LLMServerError("down"), "never", clock=clock)

    with pytest.raises(LLMServerError) as exc:
        await run(make_policy(clock, max_retries=0), attempt)

    assert exc.value.attempts == 1
    assert len(remaining) == 1
    assert clock.sleeps == []


@pytest.mark.anyio
@pytest.mark.parametrize(("ask", "cost"), [(40, 0.0), (20, 15.0), (30, 0.0)])
async def test_no_attempt_starts_once_the_asked_wait_would_pass_the_budget(run, ask, cost):
    clock = Clock()
    attempt, remaining = scripted(LLMRateLimitError("slow down", retry_after=ask), "never", clock=clock, cost=cost)

    with pytest.raises(LLMRateLimitError) as exc:
        await run(make_policy(clock), attempt, budget=30.0)

    assert exc.value.attempts == 1
    assert len(remaining) == 1
    assert clock.sleeps == []  # gave up at once, without sleeping first


@pytest.mark.anyio
async def test_an_almost_over_budget_still_runs_the_first_attempt_then_gives_up(run):
    clock = Clock()
    attempt, remaining = scripted(LLMServerError("down"), "never", clock=clock, cost=0.1)

    with pytest.raises(LLMServerError) as exc:
        await run(make_policy(clock), attempt, budget=0.1)

    assert remaining == [0.1]  # the attempt's own time limit is what was left
    assert (exc.value.attempts, exc.value.latency_ms) == (1, 100)
    assert clock.sleeps == []


@pytest.mark.anyio
async def test_the_error_after_retries_carries_every_attempt_and_the_whole_latency(run):
    clock = Clock()
    attempt, _ = scripted(
        LLMServerError("1"), LLMRateLimitError("2", retry_after=1), LLMServerError("3"), clock=clock, cost=0.5
    )

    with pytest.raises(LLMServerError) as exc:
        await run(make_policy(clock), attempt)

    assert exc.value.attempts == 3
    assert exc.value.latency_ms == round((1.5 + sum(clock.sleeps)) * 1000)


@pytest.mark.anyio
async def test_two_concurrent_calls_on_one_policy_keep_their_own_attempts():
    clock = Clock()
    policy = make_policy(clock)
    first, _ = scripted(LLMServerError("1"), "a", clock=clock)
    second, _ = scripted(LLMServerError("1"), LLMServerError("2"), "b", clock=clock)
    results = {}

    async def go(name, attempt):
        async def async_attempt(left):
            return attempt(left)

        results[name] = await policy.acall(async_attempt, budget=100.0)

    async with anyio.create_task_group() as tg:
        tg.start_soon(go, "first", first)
        tg.start_soon(go, "second", second)

    assert (results["first"].value, results["first"].attempts) == ("a", 2)
    assert (results["second"].value, results["second"].attempts) == ("b", 3)
    assert len(clock.sleeps) == 3


# --- the retry_wait / retry_giveup events ---

EVENT_FIELDS = {
    "retry_wait": {"task", "attempt", "wait_seconds", "error_class"},
    "retry_giveup": {"task", "attempts", "elapsed_ms", "error_class", "reason"},
}


def fields(line: dict) -> set[str]:
    return set(line) - set(RECORD_KEYS)


@pytest.mark.anyio
async def test_a_retry_wait_event_is_logged_before_each_wait(run, log_lines):
    clock = Clock()
    attempt, _ = scripted(LLMServerError("1"), LLMRateLimitError("2", retry_after=3), "ok", clock=clock)

    await run(make_policy(clock), attempt)

    waits = log_lines.events("retry_wait")
    assert [(w["attempt"], w["error_class"]) for w in waits] == [(1, "LLMServerError"), (2, "LLMRateLimitError")]
    assert [w["wait_seconds"] for w in waits] == [pytest.approx(s, abs=0.001) for s in clock.sleeps]
    assert {w["task"] for w in waits} == {"test"}
    assert {w["logger"] for w in waits} == {"app.llm"}
    assert log_lines.events("retry_giveup") == []


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("steps", "max_retries", "reason", "error_class", "attempts"),
    [
        ([LLMServerError("1"), LLMServerError("2")], 1, "max_attempts", "LLMServerError", 2),
        ([LLMServerError("1")], 0, "max_attempts", "LLMServerError", 1),
        ([LLMRateLimitError("1", retry_after=99)], 2, "deadline", "LLMRateLimitError", 1),
        ([LLMRequestError("1", status_code=401)], 2, "not_retryable", "LLMRequestError", 1),
    ],
)
async def test_a_give_up_event_says_why_retrying_stopped(run, log_lines, steps, max_retries, reason, error_class, attempts):
    clock = Clock()
    attempt, _ = scripted(*steps, clock=clock, cost=0.2)

    with pytest.raises(type(steps[-1])):
        await run(make_policy(clock, max_retries=max_retries), attempt)

    [giveup] = log_lines.events("retry_giveup")
    assert (giveup["reason"], giveup["error_class"], giveup["attempts"]) == (reason, error_class, attempts)
    assert giveup["elapsed_ms"] == round(clock.now * 1000)
    assert len(log_lines.events("retry_wait")) == attempts - 1


@pytest.mark.anyio
async def test_the_events_carry_no_payload(run, log_lines):
    clock = Clock()
    secret = "my secret answer about a past employer"
    attempt, _ = scripted(LLMServerError(secret), LLMRequestError(secret, status_code=400), clock=clock)

    with pytest.raises(LLMRequestError):
        await run(make_policy(clock), attempt)

    lines = log_lines.events("retry_wait") + log_lines.events("retry_giveup")
    assert len(lines) == 2
    for line in lines:
        assert fields(line) <= EVENT_FIELDS[line["event"]] | {"session"}
    assert secret not in log_lines.path.read_text(encoding="utf-8")


@pytest.mark.anyio
async def test_a_cancelled_wait_stops_at_once_without_a_give_up_event(log_lines):
    clock = Clock()
    attempt, remaining = scripted(LLMServerError("down"), "never", clock=clock)

    async def cancelled_sleep(seconds: float) -> None:
        raise asyncio.CancelledError

    policy = RetryPolicy(
        max_retries=2, clock=clock, sleep=clock.sleep, async_sleep=cancelled_sleep, task="test", logger=get_logger("app.llm")
    )

    async def async_attempt(left: float):
        return attempt(left)

    with pytest.raises(asyncio.CancelledError):
        await policy.acall(async_attempt, budget=20.0)

    assert len(remaining) == 1
    assert log_lines.events("retry_giveup") == []


@pytest.mark.anyio
async def test_the_events_name_the_callers_task_when_given(log_lines):  # U2 review R2
    clock = Clock()
    attempt, _ = scripted(LLMServerError("1"), LLMServerError("2"), LLMServerError("3"), clock=clock)

    with pytest.raises(LLMServerError):
        make_policy(clock).call(attempt, budget=20.0, task="follow_up_decision")

    lines = log_lines.events("retry_wait") + log_lines.events("retry_giveup")
    assert len(lines) == 3 and {line["task"] for line in lines} == {"follow_up_decision"}
