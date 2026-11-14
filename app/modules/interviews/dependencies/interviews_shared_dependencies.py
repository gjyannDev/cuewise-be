import time
from collections.abc import Callable
from datetime import UTC, datetime

from fastapi import Request

from app.core.ai.context import ContextManager

# Shared with every feature; re-exported so the interviews imports and test overrides stay the same objects.
from app.core.ai.dependencies import get_llm_provider, get_tracer  # noqa: F401
from app.core.ai.embedder import Embedder
from app.core.ai.transcriber import Transcriber

from ..ai.interviews_context import CONTEXT_MANAGER
from ..schemas.interviews_schema import BankQuestion
from ..utils.interviews_utils import QUESTION_BANK


def get_bank() -> list[BankQuestion]:
    """The question source; tests override it with a fixture bank."""
    return QUESTION_BANK


def get_transcriber(request: Request) -> Transcriber | None:
    """Built once at startup (app lifespan); None when no Deepgram key is configured or the lifespan didn't run."""
    return getattr(request.app.state, "transcriber", None)


def get_embedder(request: Request) -> Embedder | None:
    """Built once at startup (app lifespan); None without the Google key or when the lifespan didn't run."""
    return getattr(request.app.state, "embedder", None)


def get_clock() -> Callable[[], float]:
    """Monotonic clock for the per-turn LLM time budget; tests swap in a fake one."""
    return time.monotonic


def _utc_now() -> datetime:
    return datetime.now(UTC)


def get_now() -> Callable[[], datetime]:
    """Wall-clock time for stored timestamps (the feedback claim and its stale takeover); tests swap in a fake one."""
    return _utc_now


def get_context_manager() -> ContextManager:
    """Decides what each LLM call sends; tests swap in one with a tiny limit."""
    return CONTEXT_MANAGER
