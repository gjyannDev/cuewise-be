from urllib.parse import parse_qs

import httpx
import pytest

from app.core.ai.deepgram import DeepgramTranscriber
from app.core.ai.provider import (
    LLMBadResponseError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)

pytestmark = pytest.mark.anyio

API_KEY = "dg-test-key-123"
AUDIO = b"\x1a\x45\xdf\xa3" + b"\x00" * 64


@pytest.fixture
def anyio_backend():
    return "asyncio"


def listen_body(
    transcript="I would use a queue.", duration: float | None = 12.5
) -> dict:
    """A pre-recorded /v1/listen response, trimmed to the fields the transcriber reads."""
    metadata = {"request_id": "req-1", "channels": 1}
    if duration is not None:
        metadata["duration"] = duration
    return {
        "metadata": metadata,
        "results": {
            "channels": [
                {"alternatives": [{"transcript": transcript, "confidence": 0.98}]}
            ]
        },
    }


class Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    async def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def make_transcriber(clock):
    """Transcriber whose HTTP layer is a scripted list of responses (or exceptions), one per attempt."""

    def _make(*script, max_retries=2, budget=20.0, timeout=15.0):
        requests: list[httpx.Request] = []
        steps = list(script)

        async def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            step = steps.pop(0)
            if isinstance(step, Exception):
                raise step
            return step

        transcriber = DeepgramTranscriber(
            api_key=API_KEY,
            model="nova-3",
            base_url="https://dg.test/",
            timeout_seconds=timeout,
            max_retries=max_retries,
            total_budget_seconds=budget,
            transport=httpx.MockTransport(handler),
            sleep=clock.sleep,
            clock=clock,
        )
        return transcriber, requests

    return _make


def ok(**kwargs) -> httpx.Response:
    return httpx.Response(200, json=listen_body(**kwargs))


async def test_posts_the_raw_audio_with_its_type_the_key_and_the_options(
    make_transcriber,
):  # AC8
    transcriber, requests = make_transcriber(ok())

    await transcriber.transcribe(AUDIO, content_type="audio/webm;codecs=opus")

    [request] = requests
    assert request.method == "POST"
    assert request.url.path == "/v1/listen"
    assert parse_qs(request.url.query.decode()) == {
        "model": ["nova-3"],
        "language": ["en"],
        "smart_format": ["true"],
        "filler_words": ["false"],
    }
    assert request.headers["authorization"] == f"Token {API_KEY}"
    assert request.headers["content-type"] == "audio/webm;codecs=opus"
    assert request.content == AUDIO


async def test_keyterms_are_sent_per_call_as_repeated_params(
    make_transcriber,
):  # AC8; spike 2026-11-04: keyterms fix most tool names
    transcriber, requests = make_transcriber(ok(), ok())

    await transcriber.transcribe(AUDIO, content_type="audio/webm", keyterms=("useEffect", "row-level security"))
    await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert parse_qs(requests[0].url.query.decode())["keyterm"] == [
        "useEffect",
        "row-level security",
    ]
    assert "keyterm" not in parse_qs(requests[1].url.query.decode())


async def test_mip_opt_out_is_not_sent(make_transcriber):  # spec decision 2026-11-04
    transcriber, requests = make_transcriber(ok())

    await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert "mip_opt_out" not in parse_qs(requests[0].url.query.decode())


async def test_returns_the_trimmed_transcript_duration_model_and_attempts(
    make_transcriber,
):  # AC8
    transcriber, _ = make_transcriber(
        ok(transcript="  I would use a queue.  ", duration=31.2)
    )

    result = await transcriber.transcribe(AUDIO, content_type="audio/mp4")

    assert result.text == "I would use a queue."
    assert result.duration_seconds == 31.2
    assert result.model == "nova-3"
    assert result.attempts == 1


async def test_silence_comes_back_as_blank_text_not_an_error(
    make_transcriber,
):  # EC6: the controller decides
    transcriber, _ = make_transcriber(ok(transcript=""))

    assert (await transcriber.transcribe(AUDIO, content_type="audio/ogg")).text == ""


async def test_a_missing_duration_is_none_not_guessed(make_transcriber):
    transcriber, _ = make_transcriber(ok(duration=None))

    assert (
        await transcriber.transcribe(AUDIO, content_type="audio/webm")
    ).duration_seconds is None


async def test_a_503_is_retried_after_backoff_then_succeeds(
    make_transcriber, clock
):  # AC8, EC13
    transcriber, requests = make_transcriber(httpx.Response(503), ok())

    result = await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 2
    assert result.attempts == 2
    assert len(clock.sleeps) == 1 and 0.5 <= clock.sleeps[0] <= 0.75


async def test_a_429_is_retried(
    make_transcriber,
):  # Deepgram's 429 = too many concurrent requests
    transcriber, requests = make_transcriber(httpx.Response(429), ok())

    await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 2


async def test_gives_up_after_max_retries(make_transcriber):  # AC8
    transcriber, requests = make_transcriber(
        *(httpx.Response(500) for _ in range(3)), max_retries=2
    )

    with pytest.raises(LLMServerError) as caught:
        await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 3
    assert caught.value.attempts == 3


async def test_does_not_start_a_retry_past_the_budget(make_transcriber, clock):  # AC8
    transcriber, requests = make_transcriber(httpx.Response(503), ok(), budget=0.4)

    with pytest.raises(LLMServerError):
        await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 1
    assert clock.sleeps == []


@pytest.mark.parametrize("status", [400, 401, 402, 403])
async def test_other_4xx_are_not_retried(
    make_transcriber, status
):  # bad key, exhausted credit, bad request
    transcriber, requests = make_transcriber(httpx.Response(status))

    with pytest.raises(LLMRequestError) as caught:
        await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 1
    assert caught.value.status_code == status


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(200, content=b"not json"),
        httpx.Response(200, json={"metadata": {}}),
        httpx.Response(200, json={"results": {"channels": []}}),
        httpx.Response(
            200,
            json={"results": {"channels": [{"alternatives": [{"transcript": None}]}]}},
        ),
    ],
)
async def test_an_unusable_200_is_a_bad_response_and_not_retried(
    make_transcriber, response
):
    transcriber, requests = make_transcriber(response)

    with pytest.raises(LLMBadResponseError):
        await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 1


async def test_a_timeout_is_retried_then_raised_as_a_timeout(make_transcriber):  # AC8
    transcriber, requests = make_transcriber(
        *(httpx.ReadTimeout("slow") for _ in range(3))
    )

    with pytest.raises(LLMTimeoutError):
        await transcriber.transcribe(AUDIO, content_type="audio/webm")

    assert len(requests) == 3


async def test_a_dropped_connection_is_a_server_error(make_transcriber):
    transcriber, _ = make_transcriber(
        *(httpx.ConnectError("refused") for _ in range(3))
    )

    with pytest.raises(LLMServerError):
        await transcriber.transcribe(AUDIO, content_type="audio/webm")
