"""The attempt header the four reply loops share: decide, write, write stream and the feedback turn.

These are content retries (the model answered, but the reply was malformed or empty), not transport retries: no
backoff, no Retry-After, no HTTP errors (`core/ai/retry.py` already retried those, and an `LLMError` stops the loop).
They are bounded by the turn's time, so they stay out of tenacity. Only the header is shared; each loop keeps its own
call, parse and logging body, because those differ (the stream's resets, the feedback turn's checks).
"""

from collections.abc import Callable, Iterator

from app.modules.interviews.constants.interviews_constants import (
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
)


class ReplyAttempts:
    """Iterate to get `(attempt, seconds_left)` for each reply attempt that may start.

    It stops after `MAX_REPLY_ATTEMPTS`, when no time is left, or, after the first attempt, when less than
    `MIN_SECONDS_FOR_RETRY` is left (a retry that can't finish only delays the fallback). `stopped_at` is the attempt
    that did not start for lack of time, or None.
    """

    def __init__(self, time_left: Callable[[], float]):
        self._time_left = time_left
        self.stopped_at: int | None = None

    def __iter__(self) -> Iterator[tuple[int, float]]:
        for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
            left = self._time_left()
            if left <= 0 or (attempt > 1 and left < MIN_SECONDS_FOR_RETRY):
                self.stopped_at = attempt
                return
            yield attempt, left
