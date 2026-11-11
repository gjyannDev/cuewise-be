from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.ai.transcriber import Transcriber
from app.core.errors import RateLimitedError
from app.core.rate_limit import RateLimiter
from app.db.session import get_db
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import TRANSCRIPTIONS_PER_MINUTE
from ..controllers.interviews_transcription_controller import TranscriptionController
from ..dependencies.interviews_shared_dependencies import get_transcriber
from ..repositories.interviews_repository import InterviewsRepository
from ..services.interviews_transcription_service import TranscriptionService

# One per process: every request shares the counts (see core/rate_limit.py for the multi-instance caveat).
TRANSCRIPTION_LIMITER = RateLimiter(limit=TRANSCRIPTIONS_PER_MINUTE, window_seconds=60)


def get_transcription_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return TRANSCRIPTION_LIMITER


def limit_transcriptions(
    user: Annotated[User, require_permissions(Permission.interviews_answer)],
    limiter: Annotated[RateLimiter, Depends(get_transcription_limiter)],
) -> None:
    """Per-user cap on transcriptions, checked before the upload goes anywhere that costs money."""
    retry_after = limiter.hit(str(user.id))
    if retry_after is not None:
        raise RateLimitedError(
            "Too many recordings. Wait a moment and try again.", headers={"Retry-After": str(retry_after)}
        )


def get_transcription_service(
    db: Annotated[Session, Depends(get_db)],
    transcriber: Annotated[Transcriber | None, Depends(get_transcriber)],
) -> TranscriptionService:
    return TranscriptionService(InterviewsRepository(db), transcriber)


def get_transcription_controller(
    service: Annotated[TranscriptionService, Depends(get_transcription_service)],
) -> TranscriptionController:
    return TranscriptionController(service)


TranscriptionControllerDep = Annotated[TranscriptionController, Depends(get_transcription_controller)]
