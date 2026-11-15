"""The interview voice adapter, HTTP side: request -> VoiceService, domain result -> response."""

import uuid

from fastapi import Response

from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import JobRole
from ..schemas.interviews_schema import TranscriptionOut
from ..services.interviews_voice_service import SpeakableLine, VoiceService


class VoiceController:
    def __init__(self, service: VoiceService):
        self.service = service

    def prepare_transcription(self, user: User, session_id: uuid.UUID) -> JobRole:
        return self.service.prepare_transcription(user, session_id)

    async def transcribe(
        self, user: User, session_id: uuid.UUID, role: JobRole, audio: bytes, content_type: str
    ) -> TranscriptionOut:
        return TranscriptionOut(text=await self.service.transcribe(user, session_id, role, audio, content_type))

    def prepare_question_speech(self, user: User, session_id: uuid.UUID, question_id: uuid.UUID) -> SpeakableLine:
        return self.service.prepare_question_speech(user, session_id, question_id)

    def prepare_reaction_speech(self, user: User, session_id: uuid.UUID, message_id: uuid.UUID) -> SpeakableLine:
        return self.service.prepare_reaction_speech(user, session_id, message_id)

    async def speak(self, user: User, line: SpeakableLine) -> Response:
        """The clip with the media type the synthesizer reported, never a hardcoded one. `private`: it is this user's
        interview, so shared caches must not keep it."""
        spoken = await self.service.speak(user, line)
        return Response(
            content=spoken.audio, media_type=spoken.content_type, headers={"Cache-Control": "private, no-store"}
        )
