"""Deepgram over plain httpx: pre-recorded speech-to-text (`POST /v1/listen`, Nova models) and Aura text-to-speech
(`POST /v1/speak`).

Deliberately no SDK: the requests and the response fields read here are all visible. For
speech-to-text the audio is sent exactly as recorded; Deepgram detects the container (WebM, OGG, MP4, WAV), so no
`encoding` is passed. Both adapters only build their request and parse their response; the attempt loop is the
adapter's `RetryPolicy`.
"""

import time
from collections.abc import Awaitable, Callable, Sequence
from typing import Any

import anyio
import httpx

from app.core.config import SpeechEncoding
from app.core.logging import get_logger

from .provider import LLMBadResponseError, LLMServerError, LLMTimeoutError
from .retry import Attempted, RetryPolicy, raise_for_status
from .synthesizer import SynthesisResult
from .transcriber import TranscriptionResult

LISTEN_PATH = "v1/listen"
SPEAK_PATH = "v1/speak"
# Aura `encoding` -> the media type its audio is, used only when the response doesn't say (Aura's default containers).
# Keyed by the settings' `SpeechEncoding`, so the two lists can't drift (a test checks they match).
SPEAK_CONTENT_TYPES: dict[SpeechEncoding, str] = {
    "mp3": "audio/mpeg",
    "opus": "audio/ogg",
    "aac": "audio/aac",
    "flac": "audio/flac",
    "linear16": "audio/wav",
}


class _DeepgramAdapter:
    """What both Deepgram adapters share: one authenticated client, the retry policy and the mapping of request
    failures to `LLMError`s. Each adapter only builds its request and parses its response.

    Each adapter keeps its own client (connection pool): they are built, closed and timed out independently, and a
    second pool to the same host costs a couple of idle connections at most.
    """

    # The retry events' task label and logger; each adapter sets its own.
    _task: str
    _logger_name: str

    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        base_url: str,
        timeout_seconds: float,
        max_retries: int,
        total_budget_seconds: float,
        # Injected so tests can script responses and run retries without real waiting.
        transport: httpx.AsyncBaseTransport | None = None,
        sleep: Callable[[float], Awaitable[None]] = anyio.sleep,
        clock: Callable[[], float] = time.perf_counter,
    ):
        self._model = model
        self._timeout = timeout_seconds
        self._budget = total_budget_seconds
        self._retry = RetryPolicy(
            max_retries=max_retries, task=self._task, logger=get_logger(self._logger_name), clock=clock, async_sleep=sleep
        )
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/") + "/",
            headers={"Authorization": f"Token {api_key}"},
            transport=transport,
        )

    @property
    def model(self) -> str:
        return self._model

    async def aclose(self) -> None:
        await self._client.aclose()

    async def _with_retries[T](self, attempt: Callable[[float], Awaitable[T]]) -> Attempted[T]:
        return await self._retry.acall(attempt, budget=self._budget)

    async def _post(self, path: str, what: str, *, remaining: float, **request: Any) -> httpx.Response:
        """One POST that never waits past the total budget; a non-2xx or failed request becomes a typed `LLMError`."""
        try:
            response = await self._client.post(path, timeout=min(self._timeout, remaining), **request)
        except httpx.TimeoutException as exc:
            raise LLMTimeoutError(f"{what} request timed out") from exc
        # Every other request failure (a dropped connection, a body that can't be decoded, ...), not only transport
        # ones: anything unmapped would escape the gateway as an unhandled 500.
        except httpx.RequestError as exc:
            raise LLMServerError(f"{what} request failed") from exc
        raise_for_status(response.status_code, response.headers.get("retry-after"))
        return response


class DeepgramTranscriber(_DeepgramAdapter):
    _task, _logger_name = "transcribe", "app.stt"

    def __init__(self, *, model: str, **adapter: Any):
        super().__init__(model=model, **adapter)
        # `mip_opt_out` is not sent: v1 stays in Deepgram's Model Improvement Program (opting out costs more).
        # A tuple, not a list: httpx's params type accepts it (tuples are covariant, lists aren't).
        self._params: tuple[tuple[str, str], ...] = (
            ("model", model),
            ("language", "en"),
            ("smart_format", "true"),
            ("filler_words", "false"),
        )

    async def transcribe(
        self, audio: bytes, *, content_type: str, keyterms: Sequence[str] = ()
    ) -> TranscriptionResult:
        # Keyterms (Nova-3 only) go on the URL, one repeated `keyterm` param per term; none sends none.
        params = (*self._params, *(("keyterm", term) for term in keyterms))

        async def attempt(remaining: float) -> tuple[str, float | None]:
            response = await self._post(
                LISTEN_PATH,
                "Transcription",
                remaining=remaining,
                params=params,
                content=audio,
                headers={"Content-Type": content_type},
            )
            return _parse(response)

        done = await self._with_retries(attempt)
        text, duration = done.value
        return TranscriptionResult(
            text=text,
            duration_seconds=duration,
            model=self._model,
            latency_ms=done.latency_ms,
            attempts=done.attempts,
        )


def _parse(response: httpx.Response) -> tuple[str, float | None]:
    """The first channel's best transcript (blank for silence) and the reported audio duration."""
    try:
        data: dict[str, Any] = response.json()
        transcript = data["results"]["channels"][0]["alternatives"][0]["transcript"]
    except (ValueError, KeyError, IndexError, TypeError) as exc:
        raise LLMBadResponseError("Transcription response has no usable transcript") from exc
    if not isinstance(transcript, str):
        raise LLMBadResponseError("Transcription response has no usable transcript")
    duration = (data.get("metadata") or {}).get("duration")
    return transcript.strip(), float(duration) if isinstance(duration, int | float) else None


class DeepgramSynthesizer(_DeepgramAdapter):
    """Aura text-to-speech: the text goes in a JSON body, the voice (`model`) and `encoding` on the URL, and the
    whole clip comes back as the response body (buffered: the caller needs it whole for its replay cache)."""

    _task, _logger_name = "synthesize", "app.tts"

    def __init__(self, *, model: str, encoding: SpeechEncoding, **adapter: Any):
        super().__init__(model=model, **adapter)
        self._fallback_type = SPEAK_CONTENT_TYPES[encoding]
        self._params: tuple[tuple[str, str], ...] = (("model", model), ("encoding", encoding))

    async def synthesize(self, text: str) -> SynthesisResult:
        async def attempt(remaining: float) -> tuple[bytes, str]:
            response = await self._post(SPEAK_PATH, "Speech", remaining=remaining, params=self._params, json={"text": text})
            content_type = response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
            content_type = content_type or self._fallback_type
            # A 200 that isn't audio (an error page, JSON) or has no body would play as silence or noise: not retried.
            if not response.content or not content_type.startswith("audio/"):
                raise LLMBadResponseError("Speech response has no usable audio")
            return response.content, content_type

        done = await self._with_retries(attempt)
        audio, content_type = done.value
        return SynthesisResult(
            audio=audio,
            content_type=content_type,
            model=self._model,
            characters=len(text),
            latency_ms=done.latency_ms,
            attempts=done.attempts,
        )
