"""OpenAI-compatible chat completions over plain httpx (Google AI Studio, OpenRouter, Groq, ...).

Deliberately no SDK: the request body and the response shape are all visible here; the retry rules are in `retry.py`.
"""

import json
import time
from collections.abc import AsyncGenerator, Awaitable, Callable, Mapping, Sequence
from typing import Any

import anyio
import httpx

from app.core.logging import get_logger

from .provider import (
    ChatMessage,
    LLMBadResponseError,
    LLMError,
    LLMResult,
    LLMServerError,
    LLMTimeoutError,
    ReasoningEffort,
)
from .retry import RetryPolicy, raise_for_status

# The SSE line prefix of a streamed chunk, and the sentinel that ends the stream.
_DATA = "data:"
_DONE = "[DONE]"


class OpenAICompatibleProvider:
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
        async_transport: httpx.AsyncBaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
        async_sleep: Callable[[float], Awaitable[None]] = anyio.sleep,
        clock: Callable[[], float] = time.perf_counter,
    ):
        self._model = model
        self._timeout = timeout_seconds
        self._budget = total_budget_seconds
        self._clock = clock
        self._retry = RetryPolicy(
            max_retries=max_retries,
            task="chat",
            logger=get_logger("app.llm"),
            clock=clock,
            sleep=sleep,
            async_sleep=async_sleep,
        )
        base = base_url.rstrip("/") + "/"
        headers = {"Authorization": f"Bearer {api_key}"}
        self._client = httpx.Client(base_url=base, headers=headers, transport=transport)
        # A second client for streaming: the async one keeps the event loop free while chunks trickle in.
        self._async_client = httpx.AsyncClient(base_url=base, headers=headers, transport=async_transport)

    @property
    def model(self) -> str:
        return self._model

    def close(self) -> None:
        self._client.close()

    async def aclose(self) -> None:
        await self._async_client.aclose()

    def complete(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
        # Labels for tracing only (task, prompt_version, ...); providers ignore them, TracingProvider records them.
        trace_labels: Mapping[str, str | int | None] | None = None,
    ) -> LLMResult:
        body = self._body(messages, max_tokens, temperature, reasoning_effort)
        done = self._retry.call(
            lambda remaining: self._attempt(body, remaining=remaining),
            budget=self._budget_for(budget_seconds),
            task=_task_label(trace_labels),
        )
        return done.value.model_copy(update={"attempts": done.attempts, "latency_ms": done.latency_ms})

    async def stream(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
        # Labels for tracing only (task, prompt_version, ...); providers ignore them, TracingProvider records them.
        trace_labels: Mapping[str, str | int | None] | None = None,
    ) -> AsyncGenerator[str | LLMResult]:
        """Same request with `stream: true`: chunks as they arrive, then the final LLMResult. The same retry rules as
        `complete`, but only until the first chunk was yielded (the caller may have shown it): after that a failure
        is raised with `after_output` set."""
        body = self._body(messages, max_tokens, temperature, reasoning_effort) | {
            "stream": True,
            # Usage arrives in one last chunk; without this, OpenAI-compatible endpoints send none when streaming.
            "stream_options": {"include_usage": True},
        }
        budget = self._budget_for(budget_seconds)
        task = _task_label(trace_labels)
        start = self._clock()

        async def open_stream(remaining: float) -> tuple[AsyncGenerator[str | LLMResult], str | LLMResult]:
            # The retried step: open the stream and read its first chunk. A failed open has already ended its
            # generator (the exception closed it), so nothing is left open.
            chunks = self._stream_attempt(body, end=self._clock() + remaining)
            return chunks, await anext(chunks)

        opened = await self._retry.acall(open_stream, budget=budget, task=task)
        chunks, item = opened.value
        try:
            while not isinstance(item, LLMResult):
                yield item
                item = await anext(chunks)
        except LLMError as exc:
            # After output: never retried, the caller may already have shown the text.
            exc.attempts, exc.latency_ms, exc.after_output = opened.attempts, self._elapsed_ms(start), True
            self._retry.log_giveup(exc, task=task)
            raise
        finally:
            await chunks.aclose()  # also when the caller stops reading early: release the HTTP stream
        yield item.model_copy(update={"attempts": opened.attempts, "latency_ms": self._elapsed_ms(start)})

    def _body(
        self,
        messages: Sequence[ChatMessage],
        max_tokens: int,
        temperature: float | None,
        reasoning_effort: ReasoningEffort | None,
    ) -> dict[str, Any]:
        body: dict[str, Any] = {
            "model": self._model,
            "messages": [m.model_dump() for m in messages],
            "max_tokens": max_tokens,
        }
        if temperature is not None:
            body["temperature"] = temperature
        if reasoning_effort is not None:
            # OpenRouter's unified reasoning option; other endpoints (e.g. Google's) may ignore or reject it.
            body["reasoning"] = {"effort": reasoning_effort}
        return body

    def _budget_for(self, budget_seconds: float | None) -> float:
        return self._budget if budget_seconds is None else min(self._budget, budget_seconds)

    def _attempt(self, body: dict[str, Any], *, remaining: float) -> LLMResult:
        try:
            # Never wait past the total budget, even on the last attempt.
            response = self._client.post("chat/completions", json=body, timeout=min(self._timeout, remaining))
        except httpx.TimeoutException as exc:
            raise LLMTimeoutError("LLM request timed out") from exc
        except httpx.TransportError as exc:
            raise LLMServerError("LLM connection failed") from exc
        raise_for_status(response.status_code, response.headers.get("retry-after"))
        return self._parse(response)

    async def _stream_attempt(self, body: dict[str, Any], *, end: float) -> AsyncGenerator[str | LLMResult]:
        """One streamed request, ending by `end` on the clock: its text chunks, then an LLMResult (attempts and
        latency set by the caller)."""
        parts: list[str] = []
        usage: dict[str, Any] = {}
        model, finish = None, None
        try:
            # httpx's timeout bounds each read; the clock check below bounds the whole stream.
            timeout = min(self._timeout, end - self._clock())
            async with self._async_client.stream("POST", "chat/completions", json=body, timeout=timeout) as response:
                if response.status_code != 200:
                    await response.aread()
                    raise_for_status(response.status_code, response.headers.get("retry-after"))
                async for line in response.aiter_lines():
                    if not line.startswith(_DATA):
                        continue  # blank separators and SSE comments (keep-alives)
                    payload = line[len(_DATA) :].strip()
                    if payload == _DONE:
                        break
                    try:
                        data = json.loads(payload)
                    except ValueError as exc:
                        raise LLMBadResponseError("LLM stream sent a malformed chunk") from exc
                    if "error" in data:
                        # An error that arrived after the 200: the status line can't carry it any more.
                        raise_for_status(_int_or_none((data["error"] or {}).get("code")) or 500)
                    model = data.get("model") or model
                    usage = data.get("usage") or usage
                    for choice in data.get("choices") or []:
                        finish = choice.get("finish_reason") or finish
                        text = (choice.get("delta") or {}).get("content")
                        if text:
                            parts.append(text)
                            yield text
                    if self._clock() > end:
                        raise LLMTimeoutError("LLM stream ran past its time budget")
        except httpx.TimeoutException as exc:
            raise LLMTimeoutError("LLM request timed out") from exc
        except httpx.TransportError as exc:
            raise LLMServerError("LLM connection failed") from exc

        text = "".join(parts)
        if not text.strip():
            raise LLMBadResponseError("LLM returned an empty message", finish_reason=finish)
        yield LLMResult(
            text=text.strip(), model=model or self._model, latency_ms=0, finish_reason=finish, attempts=1, **_usage(usage)
        )

    def _parse(self, response: httpx.Response) -> LLMResult:
        try:
            data = response.json()
            choice = data["choices"][0]
            text = choice["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            raise LLMBadResponseError("LLM response has no usable message") from exc
        if not isinstance(text, str) or not text.strip():
            raise LLMBadResponseError("LLM returned an empty message", finish_reason=choice.get("finish_reason"))

        return LLMResult(
            text=text.strip(),
            model=data.get("model") or self._model,
            latency_ms=0,
            finish_reason=choice.get("finish_reason"),
            attempts=1,
            **_usage(data.get("usage") or {}),
        )

    def _elapsed_ms(self, start: float) -> int:
        return round((self._clock() - start) * 1000)


def _task_label(trace_labels: Mapping[str, str | int | None] | None) -> str | None:
    """The caller's task (e.g. `follow_up_decision`) for the retry events, so they name the same task as `llm_call`."""
    task = (trace_labels or {}).get("task")
    return task if isinstance(task, str) else None


def _usage(usage: dict[str, Any]) -> dict[str, int | None]:
    """The token counts an OpenAI-compatible usage object reports; None for any it leaves out (never guessed)."""
    return {
        "prompt_tokens": _int_or_none(usage.get("prompt_tokens")),
        "completion_tokens": _int_or_none(usage.get("completion_tokens")),
        "cached_tokens": _int_or_none((usage.get("prompt_tokens_details") or {}).get("cached_tokens")),
        "reasoning_tokens": _int_or_none((usage.get("completion_tokens_details") or {}).get("reasoning_tokens")),
    }


def _int_or_none(value: object) -> int | None:
    return value if isinstance(value, int) else None
