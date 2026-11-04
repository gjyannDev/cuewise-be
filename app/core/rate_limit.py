"""In-memory fixed-window rate limiting for sensitive endpoints.

Per process only: with several app instances each keeps its own counts. Good enough for one instance; a shared store
(e.g. Redis) replaces this when the app scales out.
"""

import math
import threading
import time
from collections.abc import Callable


class RateLimiter:
    def __init__(self, *, limit: int, window_seconds: float, clock: Callable[[], float] = time.monotonic):
        self._limit = limit
        self._window = window_seconds
        self._clock = clock
        self._lock = threading.Lock()
        # key -> (window start, hits in that window)
        self._windows: dict[str, tuple[float, int]] = {}

    def hit(self, key: str) -> int | None:
        """Count one request for `key`: None when allowed, else whole seconds until its window resets."""
        now = self._clock()
        with self._lock:
            start, count = self._windows.get(key, (now, 0))
            if now - start >= self._window:
                start, count = now, 0
            if count >= self._limit:
                return max(1, math.ceil(start + self._window - now))
            self._windows[key] = (start, count + 1)
            return None
