"""Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over plain httpx.

Deliberately no SDK, like `openai_compatible.py`: the request (raw audio body, options as query params) and the
response fields read here are all visible. The audio is sent exactly as recorded; Deepgram detects the container
(WebM, OGG, MP4, WAV), so no `encoding` is passed.
"""

import random
import time
from collections.abc import Awaitable, Callable, Sequence
from typing import Any

import anyio
import httpx

from .provider import LLMBadResponseError, LLMError, LLMServerError, LLMTimeoutError
from .retry import raise_for_status, retry_delay
from .transcriber import TranscriptionResult

LISTEN_PATH = "v1/listen"


class DeepgramTranscriber:
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
        rng: random.Random | None = None,
    ):
        self._model = model
        self._timeout = timeout_seconds
        self._max_retries = max_retries
        self._budget = total_budget_seconds
        self._sleep = sleep
        self._clock = clock
        self._rng = rng or random.Random()
        # `mip_opt_out` is not sent: v1 stays in Deepgram's Model Improvement Program (opting out costs more).
        # A tuple, not a list: httpx's params type accepts it (tuples are covariant, lists aren't).
        self._params: tuple[tuple[str, str], ...] = (
            ("model", model),
            ("language", "en"),
            ("smart_format", "true"),
            ("filler_words", "false"),
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

    async def transcribe(
        self, audio: bytes, *, content_type: str, keyterms: Sequence[str] = ()
    ) -> TranscriptionResult:
        # Keyterms (Nova-3 only) go on the URL, one repeated `keyterm` param per term; none sends none.
        params = (*self._params, *(("keyterm", term) for term in keyterms))
        start = self._clock()
        attempt = 0
        while True:
            attempt += 1
            try:
                remaining = self._budget - (self._clock() - start)
                text, duration = await self._attempt(audio, content_type, params, remaining=remaining)
            except LLMError as exc:
                exc.attempts, exc.latency_ms = attempt, self._elapsed_ms(start)
                delay = retry_delay(
                    exc,
                    attempt=attempt,
                    max_retries=self._max_retries,
                    elapsed=self._clock() - start,
                    budget=self._budget,
                    rng=self._rng,
                )
                if delay is None:
                    raise
                await self._sleep(delay)
                continue
            return TranscriptionResult(
                text=text,
                duration_seconds=duration,
                model=self._model,
                latency_ms=self._elapsed_ms(start),
                attempts=attempt,
            )

    async def _attempt(
        self, audio: bytes, content_type: str, params: tuple[tuple[str, str], ...], *, remaining: float
    ) -> tuple[str, float | None]:
        try:
            # Never wait past the total budget, even on the last attempt.
            response = await self._client.post(
                LISTEN_PATH,
                params=params,
                content=audio,
                headers={"Content-Type": content_type},
                timeout=min(self._timeout, remaining),
            )
        except httpx.TimeoutException as exc:
            raise LLMTimeoutError("Transcription request timed out") from exc
        except httpx.TransportError as exc:
            raise LLMServerError("Transcription connection failed") from exc
        raise_for_status(response.status_code, response.headers.get("retry-after"))
        return _parse(response)

    def _elapsed_ms(self, start: float) -> int:
        return round((self._clock() - start) * 1000)


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
