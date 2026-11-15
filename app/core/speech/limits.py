"""Per-user caps on paid speech calls. One limiter instance per process: every request shares the counts (see
`core/rate_limit.py` for the multi-instance caveat).

Only the counters live here. The FastAPI dependencies that apply them need the signed-in user from the auth module,
so they live with each feature's adapter (`core` never imports `app.modules`).
"""

from app.core.rate_limit import RateLimiter

TRANSCRIPTIONS_PER_MINUTE = 10
# Interviewer lines spoken per user per minute, shared by every speech route. Replays come from the web app's cache and
# don't reach here, so this only bounds fresh clips (a turn speaks at most a reaction and a question).
SPEECH_PER_MINUTE = 30

TRANSCRIPTION_LIMITER = RateLimiter(limit=TRANSCRIPTIONS_PER_MINUTE, window_seconds=60)
SPEECH_LIMITER = RateLimiter(limit=SPEECH_PER_MINUTE, window_seconds=60)
