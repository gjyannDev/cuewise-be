import random

import pytest

from app.core.ai.provider import LLMRateLimitError, LLMRequestError, LLMServerError
from app.core.ai.retry import parse_retry_after, raise_for_status, retry_delay


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
