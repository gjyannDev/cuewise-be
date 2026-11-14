import time
from collections.abc import Callable
from datetime import UTC, datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.ai.dependencies import get_llm_provider
from app.core.ai.provider import LLMProvider
from app.core.config import settings
from app.core.errors import RateLimitedError
from app.core.rate_limit import RateLimiter
from app.db.session import get_db
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions
from app.modules.auth.models.auth_model import User

from ..constants.profile_constants import RESUME_UPLOADS_PER_MINUTE
from ..controllers.profile_controller import ProfileController
from ..repositories.profile_repository import ProfileRepository
from ..services.profile_service import ProfileService

# One per process: every request shares the counts (see core/rate_limit.py for the multi-instance caveat).
RESUME_LIMITER = RateLimiter(limit=RESUME_UPLOADS_PER_MINUTE, window_seconds=60)

ProfileUser = Annotated[User, require_permissions(Permission.profile_manage_self)]


def get_resume_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return RESUME_LIMITER


def get_profile_clock() -> Callable[[], float]:
    """Monotonic clock for the extraction's time budget; tests swap in a fake one."""
    return time.monotonic


def _utc_now() -> datetime:
    return datetime.now(UTC)


def get_profile_now() -> Callable[[], datetime]:
    return _utc_now


def limit_resume_uploads(user: ProfileUser, limiter: Annotated[RateLimiter, Depends(get_resume_limiter)]) -> None:
    """Checked before the body is read: every upload is a parse and a model call."""
    retry_after = limiter.hit(str(user.id))
    if retry_after is not None:
        raise RateLimitedError(
            "Too many résumé uploads. Wait a moment and try again.", headers={"Retry-After": str(retry_after)}
        )


def get_profile_service(
    db: Annotated[Session, Depends(get_db)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_profile_clock)],
    now: Annotated[Callable[[], datetime], Depends(get_profile_now)],
) -> ProfileService:
    return ProfileService(ProfileRepository(db), llm, max_tokens=settings.llm_max_tokens, clock=clock, now=now)


def get_profile_controller(service: Annotated[ProfileService, Depends(get_profile_service)]) -> ProfileController:
    return ProfileController(service)


ProfileControllerDep = Annotated[ProfileController, Depends(get_profile_controller)]
