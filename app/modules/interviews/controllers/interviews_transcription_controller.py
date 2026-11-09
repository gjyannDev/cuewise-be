"""Voice answers: request -> TranscriptionService, text -> TranscriptionOut. The upload checks stay in the service,
inside the same try/finally as its log line, so a rejected upload is still logged."""

import uuid

from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import JobRole
from ..schemas.interviews_schema import TranscriptionOut
from ..services.interviews_transcription_service import TranscriptionService


class TranscriptionController:
    def __init__(self, service: TranscriptionService):
        self.service = service

    def prepare_transcription(self, user: User, session_id: uuid.UUID) -> JobRole:
        return self.service.prepare_transcription(user, session_id)

    async def transcribe(
        self, user: User, session_id: uuid.UUID, role: JobRole, audio: bytes, content_type: str
    ) -> TranscriptionOut:
        return TranscriptionOut(text=await self.service.transcribe(user, session_id, role, audio, content_type))
