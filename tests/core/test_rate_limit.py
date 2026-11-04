from app.core.rate_limit import RateLimiter


class Clock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self) -> float:
        return self.now


def test_allows_the_limit_then_refuses_with_the_seconds_left():  # voice AC7, EC21
    clock = Clock()
    limiter = RateLimiter(limit=10, window_seconds=60, clock=clock)

    assert all(limiter.hit("user-1") is None for _ in range(10))
    clock.now += 15
    assert limiter.hit("user-1") == 45


def test_each_key_has_its_own_window():  # EC21: other users unaffected
    limiter = RateLimiter(limit=1, window_seconds=60, clock=Clock())

    assert limiter.hit("user-1") is None
    assert limiter.hit("user-1") is not None
    assert limiter.hit("user-2") is None


def test_a_new_window_allows_again():
    clock = Clock()
    limiter = RateLimiter(limit=1, window_seconds=60, clock=clock)
    limiter.hit("user-1")

    clock.now += 60

    assert limiter.hit("user-1") is None


def test_refused_hits_do_not_extend_the_window():  # inferred: retrying while blocked must not lock a user out
    clock = Clock()
    limiter = RateLimiter(limit=1, window_seconds=60, clock=clock)
    limiter.hit("user-1")

    clock.now += 30
    limiter.hit("user-1")
    clock.now += 30

    assert limiter.hit("user-1") is None


def test_retry_after_is_at_least_one_second():  # inferred: Retry-After 0 would invite an instant retry
    clock = Clock()
    limiter = RateLimiter(limit=1, window_seconds=60, clock=clock)
    limiter.hit("user-1")

    clock.now += 59.9

    assert limiter.hit("user-1") == 1
