"""OpenRouter over plain httpx (OpenAI-compatible chat completions). The only module that imports httpx.

Deliberately no SDK: the request body, the response shape and the retry rules are all visible here.
"""

import random
import time
from collections.abc import Callable, Sequence
from typing import Any

import httpx

from .provider import (
    ChatMessage,
    LLMBadResponseError,
    LLMError,
    LLMRateLimitError,
    LLMRequestError,
    LLMResult,
    LLMServerError,
    LLMTimeoutError,
)

BACKOFF_BASE_SECONDS = 0.5


class OpenRouterProvider:
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
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
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
        self._client = httpx.Client(
            base_url=base_url.rstrip("/") + "/", headers={"Authorization": f"Bearer {api_key}"}, transport=transport
        )

    def close(self) -> None:
        self._client.close()

    def complete(
        self, messages: Sequence[ChatMessage], *, max_tokens: int, temperature: float | None = None
    ) -> LLMResult:
        body: dict[str, Any] = {
            "model": self._model,
            "messages": [m.model_dump() for m in messages],
            "max_tokens": max_tokens,
        }
        if temperature is not None:
            body["temperature"] = temperature

        start = self._clock()
        attempt = 0
        while True:
            attempt += 1
            try:
                result = self._attempt(body, remaining=self._budget - (self._clock() - start))
            except LLMError as exc:
                exc.attempts, exc.latency_ms = attempt, self._elapsed_ms(start)
                if not exc.retryable or attempt > self._max_retries:
                    raise
                delay = self._backoff(attempt)
                # Give up rather than start a retry the user would wait for past the budget.
                if self._clock() - start + delay >= self._budget:
                    raise
                self._sleep(delay)
                continue
            return result.model_copy(update={"attempts": attempt, "latency_ms": self._elapsed_ms(start)})

    def _attempt(self, body: dict[str, Any], *, remaining: float) -> LLMResult:
        try:
            # Never wait past the total budget, even on the last attempt.
            response = self._client.post("chat/completions", json=body, timeout=min(self._timeout, remaining))
        except httpx.TimeoutException as exc:
            raise LLMTimeoutError("LLM request timed out") from exc
        except httpx.TransportError as exc:
            raise LLMServerError("LLM connection failed") from exc

        status = response.status_code
        if status == 429:
            raise LLMRateLimitError("LLM rate limited", status_code=status)
        if status >= 500:
            raise LLMServerError("LLM provider error", status_code=status)
        if status != 200:
            raise LLMRequestError("LLM request rejected", status_code=status)
        return self._parse(response)

    def _parse(self, response: httpx.Response) -> LLMResult:
        try:
            data = response.json()
            choice = data["choices"][0]
            text = choice["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            raise LLMBadResponseError("LLM response has no usable message") from exc
        if not isinstance(text, str) or not text.strip():
            raise LLMBadResponseError("LLM returned an empty message")

        usage = data.get("usage") or {}
        return LLMResult(
            text=text.strip(),
            model=data.get("model") or self._model,
            prompt_tokens=_int_or_none(usage.get("prompt_tokens")),
            completion_tokens=_int_or_none(usage.get("completion_tokens")),
            latency_ms=0,
            finish_reason=choice.get("finish_reason"),
            attempts=1,
        )

    def _backoff(self, attempt: int) -> float:
        # Exponential (0.5s, 1s, 2s, ...) plus jitter, so many clients don't retry in lockstep.
        delay = BACKOFF_BASE_SECONDS * 2 ** (attempt - 1)
        return delay + self._rng.uniform(0, delay / 2)

    def _elapsed_ms(self, start: float) -> int:
        return round((self._clock() - start) * 1000)


def _int_or_none(value: object) -> int | None:
    return value if isinstance(value, int) else None
