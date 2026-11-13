from typing import Annotated

from fastapi import Depends

from app.core.errors import RateLimitedError
from app.core.rate_limit import RateLimiter
from app.core.safe_fetch import SafeFetcher
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import (
    JOB_URL_ALLOWED_PORTS,
    JOB_URL_CONNECT_SECONDS,
    JOB_URL_MAX_BYTES,
    JOB_URL_MAX_REDIRECTS,
    JOB_URL_TOTAL_SECONDS,
    JOB_URLS_PER_MINUTE,
)
from ..controllers.interviews_job_url_controller import JobUrlController
from ..services.interviews_job_url_service import JobUrlService

# One per process: every request shares the counts (see core/rate_limit.py for the multi-instance caveat).
JOB_URL_LIMITER = RateLimiter(limit=JOB_URLS_PER_MINUTE, window_seconds=60)
# Stateless (each fetch opens its own client), so one serves every request.
PAGE_FETCHER = SafeFetcher(
    allowed_ports=JOB_URL_ALLOWED_PORTS,
    max_bytes=JOB_URL_MAX_BYTES,
    max_redirects=JOB_URL_MAX_REDIRECTS,
    total_seconds=JOB_URL_TOTAL_SECONDS,
    connect_seconds=JOB_URL_CONNECT_SECONDS,
)


def get_job_url_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return JOB_URL_LIMITER


def get_page_fetcher() -> SafeFetcher:
    """Tests swap in a fetcher with a fake resolver and transport: no network."""
    return PAGE_FETCHER


def limit_job_imports(
    user: Annotated[User, require_permissions(Permission.interviews_create)],
    limiter: Annotated[RateLimiter, Depends(get_job_url_limiter)],
) -> None:
    """One per-user budget for links and pastes together, checked before any work: a link makes the server contact
    a host someone else chose, and a paste can be a megabyte of HTML to parse."""
    retry_after = limiter.hit(str(user.id))
    if retry_after is not None:
        raise RateLimitedError(
            "Too many job imports. Wait a moment and try again.", headers={"Retry-After": str(retry_after)}
        )


def get_job_url_service(fetcher: Annotated[SafeFetcher, Depends(get_page_fetcher)]) -> JobUrlService:
    return JobUrlService(fetcher)


def get_job_url_controller(service: Annotated[JobUrlService, Depends(get_job_url_service)]) -> JobUrlController:
    return JobUrlController(service)


JobUrlControllerDep = Annotated[JobUrlController, Depends(get_job_url_controller)]
