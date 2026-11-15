"""The text-to-speech contract features code against, next to the speech-to-text `Transcriber`.

Failures raise the `LLMError` subclasses from `provider.py`, like the transcriber, so one set of retry rules applies.
"""

from typing import Protocol

from pydantic import BaseModel


class SynthesisResult(BaseModel):
    """One spoken clip. `content_type` is what the vendor says the audio is: the response's media type comes from
    here, never from a hardcoded value, so a format change is a settings change."""

    audio: bytes
    content_type: str
    model: str
    characters: int
    latency_ms: int
    attempts: int


class SpeechSynthesizer(Protocol):
    async def synthesize(self, text: str) -> SynthesisResult:
        """`text` spoken in the configured voice, as one whole clip."""
        ...

    async def aclose(self) -> None: ...
