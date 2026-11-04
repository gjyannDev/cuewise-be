"""The speech-to-text contract features code against, separate from the text-only `LLMProvider`.

Failures raise the `LLMError` subclasses from `provider.py`: despite the name they describe any vendor call (timeout,
rate limit, server, rejected request, unusable response), and reusing them keeps one set of retry rules (`retry.py`).
"""

from collections.abc import Sequence
from typing import Protocol

from pydantic import BaseModel


class TranscriptionResult(BaseModel):
    """What the vendor heard. `text` may be blank (silence); the caller decides what that means."""

    text: str
    # Seconds of audio the vendor reports; None when it reports none (never guessed).
    duration_seconds: float | None
    model: str
    latency_ms: int
    attempts: int


class Transcriber(Protocol):
    async def transcribe(
        self, audio: bytes, *, content_type: str, keyterms: Sequence[str] = ()
    ) -> TranscriptionResult:
        """`audio` is a whole recording in a container the vendor detects itself (WebM, OGG, MP4, WAV). `keyterms` are
        words to favour (names of tools, domain phrases) for this recording; vendors that can't use them ignore them."""
        ...

    async def aclose(self) -> None: ...
