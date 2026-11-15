from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.ai.synthesizer import SpeechSynthesizer
from app.core.ai.transcriber import Transcriber
from app.core.errors import RateLimitedError
from app.core.rate_limit import RateLimiter
from app.core.speech.limits import SPEECH_LIMITER, TRANSCRIPTION_LIMITER
from app.db.session import get_db
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions
from app.modules.auth.models.auth_model import User

from ..controllers.interviews_voice_controller import VoiceController
from ..dependencies.interviews_shared_dependencies import (
    get_synthesizer,
    get_transcriber,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..services.interviews_voice_service import VoiceService

# The limiter instances are generic (core/speech); these dependencies apply them, because they need the signed-in user
# from auth and core never imports app.modules.


def get_transcription_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return TRANSCRIPTION_LIMITER


def get_speech_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return SPEECH_LIMITER


def _per_user_limit(get_limiter: Callable[[], RateLimiter], message: str) -> Callable[..., None]:
    """A route dependency that charges the signed-in user one hit on `get_limiter()`'s limiter, checked before anything
    that costs money; over the limit it is a 429 with Retry-After."""

    def dependency(
        user: Annotated[User, require_permissions(Permission.interviews_answer)],
        limiter: Annotated[RateLimiter, Depends(get_limiter)],
    ) -> None:
        retry_after = limiter.hit(str(user.id))
        if retry_after is not None:
            raise RateLimitedError(message, headers={"Retry-After": str(retry_after)})

    return dependency


limit_transcriptions = _per_user_limit(get_transcription_limiter, "Too many recordings. Wait a moment and try again.")
# Shared by both speech routes.
limit_speech = _per_user_limit(get_speech_limiter, "Too many replays. Wait a moment and try again.")


def get_voice_service(
    db: Annotated[Session, Depends(get_db)],
    transcriber: Annotated[Transcriber | None, Depends(get_transcriber)],
    synthesizer: Annotated[SpeechSynthesizer | None, Depends(get_synthesizer)],
) -> VoiceService:
    return VoiceService(InterviewsRepository(db), transcriber, synthesizer)


def get_voice_controller(
    service: Annotated[VoiceService, Depends(get_voice_service)],
) -> VoiceController:
    return VoiceController(service)


VoiceControllerDep = Annotated[VoiceController, Depends(get_voice_controller)]
