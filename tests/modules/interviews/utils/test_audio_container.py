import pytest

from app.modules.interviews.constants.interviews_constants import AudioContainer
from app.modules.interviews.utils.interviews_utils import audio_container

WEBM = b"\x1a\x45\xdf\xa3" + b"\x00" * 32
OGG = b"OggS" + b"\x00" * 32
MP4 = b"\x00\x00\x00\x20ftypisom" + b"\x00" * 24
WAV = b"RIFF\x24\x00\x00\x00WAVEfmt " + b"\x00" * 24


@pytest.mark.parametrize(
    ("declared", "head", "expected"),
    [
        ("audio/webm", WEBM, AudioContainer.webm),
        ("audio/ogg", OGG, AudioContainer.ogg),
        ("audio/mp4", MP4, AudioContainer.mp4),
        ("audio/x-m4a", MP4, AudioContainer.mp4),
        ("audio/wav", WAV, AudioContainer.wav),
        ("audio/x-wav", WAV, AudioContainer.wav),
    ],
)
def test_each_allowed_type_with_its_signature_is_accepted(declared, head, expected):  # voice AC4
    assert audio_container(declared, head) == expected


@pytest.mark.parametrize("declared", ["audio/webm;codecs=opus", "Audio/WebM; codecs=opus", " audio/webm "])
def test_codec_parameters_case_and_spaces_are_ignored(declared):  # MediaRecorder sends `audio/webm;codecs=opus`
    assert audio_container(declared, WEBM) == AudioContainer.webm


@pytest.mark.parametrize("declared", ["video/webm", "audio/mpeg", "application/octet-stream", "text/plain", ""])
def test_a_type_outside_the_allowlist_is_refused(declared):  # voice AC4, EC15
    assert audio_container(declared, WEBM) is None


@pytest.mark.parametrize(
    ("declared", "head"),
    [("audio/webm", WAV), ("audio/wav", WEBM), ("audio/mp4", OGG), ("audio/ogg", b"<html><body>")],
)
def test_a_signature_that_does_not_match_the_declared_type_is_refused(declared, head):  # voice AC4, EC15
    assert audio_container(declared, head) is None


@pytest.mark.parametrize("head", [b"", b"\x1a\x45", b"RIFF\x00\x00"])
def test_a_head_too_short_to_hold_the_signature_is_refused(head):  # inferred: truncated upload
    assert audio_container("audio/webm", head) is None
    assert audio_container("audio/wav", head) is None
