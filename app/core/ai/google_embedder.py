"""Gemini embeddings through Google's native `batchEmbedContents` endpoint, over plain httpx (no SDK).

The native endpoint, not the OpenAI-compatible one the chat calls use: only the native one was shown to accept the
retrieval task types (`RETRIEVAL_QUERY` / `RETRIEVAL_DOCUMENT`) and a reduced vector size (`outputDimensionality`).
Below the model's full 3072 numbers the vectors are not normalised to length 1; cosine similarity ignores length, so
that doesn't matter for ranking.

The key goes in the `x-goog-api-key` header, never the URL (httpx logs request URLs). Nothing here logs: callers log
the result's metadata, never the input text.
"""

import random
import time
from collections.abc import Callable, Sequence
from typing import Any

import httpx

from .embedder import EmbeddingKind, EmbeddingResult, EmbeddingSizeError
from .provider import LLMBadResponseError, LLMError, LLMServerError, LLMTimeoutError
from .retry import raise_for_status, retry_delay

TASK_TYPES = {EmbeddingKind.query: "RETRIEVAL_QUERY", EmbeddingKind.document: "RETRIEVAL_DOCUMENT"}
# One retry, for a 429 or 5xx: at interview start the whole call has a 5-second cap, so more would rarely fit.
MAX_RETRIES = 1


class GoogleEmbedder:
    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        dimensions: int,
        base_url: str,
        timeout_seconds: float,
        # Injected so tests can script responses and run retries without real waiting.
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.perf_counter,
        rng: random.Random | None = None,
    ):
        self._model = model
        self._dimensions = dimensions
        self._timeout = timeout_seconds
        self._sleep = sleep
        self._clock = clock
        self._rng = rng or random.Random()
        self._path = f"models/{model}:batchEmbedContents"
        self._client = httpx.Client(
            base_url=base_url.rstrip("/") + "/", headers={"x-goog-api-key": api_key}, transport=transport
        )

    @property
    def model(self) -> str:
        return self._model

    @property
    def dimensions(self) -> int:
        return self._dimensions

    def close(self) -> None:
        self._client.close()

    def embed(
        self, texts: Sequence[str], *, kind: EmbeddingKind, budget_seconds: float | None = None
    ) -> EmbeddingResult:
        body = {
            "requests": [
                {
                    "model": f"models/{self._model}",
                    "content": {"parts": [{"text": text}]},
                    "taskType": TASK_TYPES[kind],
                    "outputDimensionality": self._dimensions,
                }
                for text in texts
            ]
        }
        budget = self._timeout if budget_seconds is None else budget_seconds
        start = self._clock()
        attempt = 0
        while True:
            attempt += 1
            try:
                vectors = self._attempt(body, len(texts), remaining=budget - (self._clock() - start))
            except LLMError as exc:
                exc.attempts, exc.latency_ms = attempt, self._elapsed_ms(start)
                delay = retry_delay(
                    exc,
                    attempt=attempt,
                    max_retries=MAX_RETRIES,
                    elapsed=self._clock() - start,
                    budget=budget,
                    rng=self._rng,
                )
                if delay is None:
                    raise
                self._sleep(delay)
                continue
            return EmbeddingResult(
                vectors=vectors,
                model=self._model,
                input_tokens=None,
                latency_ms=self._elapsed_ms(start),
                attempts=attempt,
            )

    def _attempt(self, body: dict[str, Any], count: int, *, remaining: float) -> list[list[float]]:
        try:
            # Never wait past the caller's budget, even on the last attempt.
            response = self._client.post(self._path, json=body, timeout=min(self._timeout, remaining))
        except httpx.TimeoutException as exc:
            raise LLMTimeoutError("Embedding request timed out") from exc
        except httpx.TransportError as exc:
            raise LLMServerError("Embedding connection failed") from exc
        raise_for_status(response.status_code, response.headers.get("retry-after"))
        return self._parse(response, count)

    def _parse(self, response: httpx.Response, count: int) -> list[list[float]]:
        try:
            vectors = [item["values"] for item in response.json()["embeddings"]]
        except (ValueError, KeyError, TypeError) as exc:
            raise LLMBadResponseError("Embedding response has no usable vectors") from exc
        if len(vectors) != count or not all(
            isinstance(v, list) and all(isinstance(x, int | float) and not isinstance(x, bool) for x in v)
            for v in vectors
        ):
            raise LLMBadResponseError("Embedding response has no usable vectors")
        if any(len(v) != self._dimensions for v in vectors):
            raise EmbeddingSizeError("Embedding has a different size than configured")
        return [[float(x) for x in v] for v in vectors]

    def _elapsed_ms(self, start: float) -> int:
        return round((self._clock() - start) * 1000)
