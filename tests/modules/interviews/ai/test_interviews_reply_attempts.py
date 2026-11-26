"""The attempt header the four reply loops share (decide, write, write stream, feedback turn), U2 AC13."""

import asyncio

import pytest

from app.modules.interviews.ai.interviews_reply_attempts import ReplyAttempts
from app.modules.interviews.constants.interviews_constants import (
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
)

PLENTY = MIN_SECONDS_FOR_RETRY + 10


def clock_of(*values: float):
    """`time_left` returning each value in turn."""
    queue = list(values)
    return lambda: queue.pop(0)


def test_it_stops_at_the_maximum_number_of_attempts():
    attempts = ReplyAttempts(lambda: PLENTY)

    assert [n for n, _ in attempts] == list(range(1, MAX_REPLY_ATTEMPTS + 1))
    assert attempts.stopped_at is None


def test_each_attempt_receives_the_time_left_when_it_starts():
    attempts = ReplyAttempts(clock_of(PLENTY + 3, PLENTY + 1))

    assert [left for _, left in attempts] == [PLENTY + 3, PLENTY + 1]


def test_a_retry_with_less_than_the_minimum_time_left_does_not_start():  # EC16
    attempts = ReplyAttempts(clock_of(PLENTY, MIN_SECONDS_FOR_RETRY - 0.1))

    assert [n for n, _ in attempts] == [1]
    assert attempts.stopped_at == 2  # the feedback turn records retry_skipped:no_time


def test_the_first_attempt_runs_with_less_than_the_retry_minimum():
    attempts = ReplyAttempts(clock_of(1.0, 0.5))

    assert [n for n, _ in attempts] == [1]
    assert attempts.stopped_at == 2


@pytest.mark.parametrize("left", [0.0, -1.0])
def test_no_time_before_the_first_attempt_means_no_attempt(left):  # EC17
    attempts = ReplyAttempts(lambda: left)

    assert list(attempts) == []
    assert attempts.stopped_at == 1  # the feedback turn records no_time


def test_a_cancellation_in_the_loop_body_is_not_swallowed():  # EC18
    with pytest.raises(asyncio.CancelledError):
        for _ in ReplyAttempts(lambda: PLENTY):
            raise asyncio.CancelledError
