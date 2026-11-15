"""One contract per speech protocol, run against the fake AND the real adapter (on a scripted transport).

Route tests only ever see the fakes. If an adapter changed what it returns or raises and its fake did not, those tests
would keep passing while production broke; these checks fail instead.
"""

from collections.abc import Callable

import httpx
import pytest

from app.core.ai.deepgram import DeepgramSynthesizer, DeepgramTranscriber
from app.core.ai.fake import FakeSynthesizer, FakeTranscriber
from app.core.ai.provider import LLMError, LLMServerError
from app.core.ai.synthesizer import SpeechSynthesizer, SynthesisResult
from app.core.ai.transcriber import Transcriber, TranscriptionResult

pytestmark = pytest.mark.anyio

AUDIO = b"\x1a\x45\xdf\xa3" + b"\x00" * 64
LISTEN_OK = {
    "metadata": {"duration": 3.0},
    "results": {
        "channels": [{"alternatives": [{"transcript": "I would add an index."}]}]
    },
}


@pytest.fixture
def anyio_backend():
    return "asyncio"


async def _no_wait(_: float) -> None:
    pass


def _deepgram(*responses: httpx.Response) -> DeepgramTranscriber:
    queue = list(responses)
    return DeepgramTranscriber(
        api_key="dg-test",
        model="nova-3",
        base_url="https://dg.test/",
        timeout_seconds=5,
        max_retries=1,
        total_budget_seconds=10,
        transport=httpx.MockTransport(lambda _: queue.pop(0)),
        sleep=_no_wait,
    )


# Each entry builds (a transcriber that succeeds, a transcriber whose vendor fails).
TRANSCRIBERS: dict[str, Callable[[], tuple[Transcriber, Transcriber]]] = {
    "fake": lambda: (
        FakeTranscriber(["I would add an index."]),
        FakeTranscriber([LLMServerError("down")]),
    ),
    "deepgram": lambda: (
        _deepgram(httpx.Response(200, json=LISTEN_OK)),
        _deepgram(httpx.Response(503), httpx.Response(503)),
    ),
}


@pytest.fixture(params=sorted(TRANSCRIBERS))
def transcribers(request) -> tuple[Transcriber, Transcriber]:
    return TRANSCRIBERS[request.param]()


async def test_a_transcription_fills_every_result_field(transcribers):
    ok, _ = transcribers

    result = await ok.transcribe(AUDIO, content_type="audio/webm", keyterms=("index",))

    assert isinstance(result, TranscriptionResult)
    assert result.text == "I would add an index."
    assert result.model
    assert result.latency_ms >= 0
    assert result.attempts >= 1
    await ok.aclose()


async def test_a_vendor_failure_is_an_llm_error_with_its_attempts(transcribers):
    _, failing = transcribers

    with pytest.raises(LLMError) as exc:
        await failing.transcribe(AUDIO, content_type="audio/webm")

    assert exc.value.attempts >= 1
    await failing.aclose()


# --- SpeechSynthesizer ---

MP3 = b"ID3\x04\x00" + b"\xff\xfb" * 32


def _aura(*responses: httpx.Response) -> DeepgramSynthesizer:
    queue = list(responses)
    return DeepgramSynthesizer(
        api_key="dg-test",
        model="aura-2-thalia-en",
        encoding="mp3",
        base_url="https://dg.test/",
        timeout_seconds=5,
        max_retries=1,
        total_budget_seconds=10,
        transport=httpx.MockTransport(lambda _: queue.pop(0)),
        sleep=_no_wait,
    )


SYNTHESIZERS: dict[str, Callable[[], tuple[SpeechSynthesizer, SpeechSynthesizer]]] = {
    "fake": lambda: (FakeSynthesizer(), FakeSynthesizer([LLMServerError("down")])),
    "deepgram": lambda: (
        _aura(httpx.Response(200, content=MP3, headers={"content-type": "audio/mpeg"})),
        _aura(httpx.Response(503), httpx.Response(503)),
    ),
}


@pytest.fixture(params=sorted(SYNTHESIZERS))
def synthesizers(request) -> tuple[SpeechSynthesizer, SpeechSynthesizer]:
    return SYNTHESIZERS[request.param]()


async def test_a_synthesis_fills_every_result_field(synthesizers):
    ok, _ = synthesizers

    result = await ok.synthesize("Tell me about a time you disagreed.")

    assert isinstance(result, SynthesisResult)
    assert result.audio
    assert result.content_type.startswith("audio/")
    assert result.model
    assert result.characters == len("Tell me about a time you disagreed.")
    assert result.latency_ms >= 0
    assert result.attempts >= 1
    await ok.aclose()


async def test_a_synthesis_vendor_failure_is_an_llm_error_with_its_attempts(
    synthesizers,
):
    _, failing = synthesizers

    with pytest.raises(LLMError) as exc:
        await failing.synthesize("Hi.")

    assert exc.value.attempts >= 1
    await failing.aclose()
