"""Audio rules every speech feature shares: which recording containers are accepted, and how big or long a clip may be.

Interview-agnostic on purpose: nothing here knows about sessions, questions or roles (the layer tests forbid `core`
from importing `app.modules`).
"""

from enum import StrEnum


class AudioContainer(StrEnum):
    """Recording containers an upload may arrive in (what browsers' MediaRecorder produces, plus WAV)."""

    webm = "webm"
    ogg = "ogg"
    mp4 = "mp4"
    wav = "wav"


# Declared upload type (without codec parameters) -> the container it must really be.
AUDIO_CONTENT_TYPES = {
    "audio/webm": AudioContainer.webm,
    "audio/ogg": AudioContainer.ogg,
    "audio/mp4": AudioContainer.mp4,
    "audio/x-m4a": AudioContainer.mp4,
    "audio/m4a": AudioContainer.mp4,
    "audio/wav": AudioContainer.wav,
    "audio/x-wav": AudioContainer.wav,
    "audio/wave": AudioContainer.wav,
}
# Compressed audio can't be measured without decoding, so size bounds a clip (and its cost): 120 s of browser Opus or
# AAC is about 1-2 MB. The web app also stops recording at 120 s.
TRANSCRIPTION_MAX_BYTES = 3 * 1024 * 1024
# Checked against the duration the vendor reports; a little over the web app's 120 s for encoder rounding.
TRANSCRIPTION_MAX_SECONDS = 125


def _has_signature(container: AudioContainer, head: bytes) -> bool:
    match container:
        case AudioContainer.webm:
            return head[:4] == b"\x1a\x45\xdf\xa3"  # EBML header
        case AudioContainer.ogg:
            return head[:4] == b"OggS"
        case AudioContainer.mp4:
            return head[4:8] == b"ftyp"
        case AudioContainer.wav:
            return head[:4] == b"RIFF" and head[8:12] == b"WAVE"


def audio_container(declared_type: str, head: bytes) -> AudioContainer | None:
    """The container of an uploaded recording, or None when its declared type isn't allowed or its first bytes don't
    match that type. Checked before anything is sent to the vendor, so junk never costs a transcription."""
    container = AUDIO_CONTENT_TYPES.get(declared_type.split(";", 1)[0].strip().lower())
    if container is None or not _has_signature(container, head):
        return None
    return container
