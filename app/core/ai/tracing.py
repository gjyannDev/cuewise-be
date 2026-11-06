"""Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/` imports the SDK.

Two pieces:
- `Tracer`: the one object that talks to Langfuse. Every SDK call is guarded, so a Langfuse outage, a wrong key or an
  SDK bug is logged (class name only, never content) and the request carries on. Without keys it is a no-op.
- `TracingProvider`: wraps any LLMProvider and records one *generation* per `complete()` / `stream()` call. A call that
  retried is still one generation (attempts is metadata), which keeps Hobby-plan usage low.

Why a wrapper: the provider speaks plain httpx, so Langfuse's OpenAI drop-in cannot see it; and a wrapper traces any
future provider (or fallback chain) without touching its code.
Full prompt and reply text is sent on purpose (owner's decision, see docs/features/langfuse-tracing/spec.md).
"""

import logging
from collections.abc import AsyncGenerator, Callable, Iterator, Mapping, Sequence
from contextlib import AbstractContextManager, ExitStack, aclosing, contextmanager
from typing import Any

from .provider import ChatMessage, LLMError, LLMProvider, LLMResult, ReasoningEffort

logger = logging.getLogger("app.llm")

# What the interviews code tells us about a call (task, prompt_version, budget_left_ms); recorded as metadata.
TraceLabels = Mapping[str, str | int | None]

DEFAULT_GENERATION_NAME = "llm-call"


def _safe(action: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Run an SDK call; on any failure log what failed (not why: the message could hold content) and move on."""

    def decorate(fn: Callable[..., Any]) -> Callable[..., Any]:
        def guarded(*args: Any, **kwargs: Any) -> Any:
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                logger.warning("langfuse %s failed (%s)", action, type(exc).__name__)
                return None

        return guarded

    return decorate


class Generation:
    """One LLM call as Langfuse sees it. Ends exactly once; every method is safe to call on a dead one."""

    def __init__(self, observation: Any | None, labels: TraceLabels):
        self._obs = observation
        self._labels = dict(labels)
        self._done = observation is None

    @_safe("generation update")
    def _finish(self, **fields: Any) -> None:
        if self._done or self._obs is None:
            return
        self._done = True
        try:
            self._obs.update(**fields)
        finally:
            self._obs.end()

    def succeed(self, result: LLMResult) -> None:
        fields: dict[str, Any] = {
            "output": result.text,
            "model": result.model,
            "metadata": self._labels
            | {
                "attempts": result.attempts,
                "finish_reason": result.finish_reason,
                "latency_ms": result.latency_ms,
            },
        }
        usage = _usage_details(result)
        if usage:
            fields["usage_details"] = usage
        self._finish(**fields)

    def fail(self, error: LLMError, partial_text: str = "") -> None:
        status = f" status={error.status_code}" if error.status_code is not None else ""
        self._finish(
            level="ERROR",
            status_message=f"{type(error).__name__}{status}",
            output=partial_text or None,
            metadata=self._labels
            | {
                "attempts": error.attempts,
                "finish_reason": error.finish_reason,
                "latency_ms": error.latency_ms,
            },
        )

    def cancel(self, partial_text: str) -> None:
        """The stream was closed before it finished (client left, or the turn's deadline ran out)."""
        self._finish(
            level="WARNING",
            status_message="cancelled",
            output=partial_text,
            metadata=self._labels,
        )


class Step:
    """One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when tracing is off or failed."""

    def __init__(self, observation: Any | None):
        self._obs = observation

    @_safe("step update")
    def finish(
        self,
        *,
        output: Any,
        level: str | None = None,
        status_message: str | None = None,
    ) -> None:
        if self._obs is None:
            return
        fields: dict[str, Any] = {"output": output}
        if level is not None:
            fields["level"] = level
        if status_message is not None:
            fields["status_message"] = status_message
        self._obs.update(**fields)


def _usage_details(result: LLMResult) -> dict[str, int]:
    pairs = {
        "input": result.prompt_tokens,
        "output": result.completion_tokens,
        "input_cached_tokens": result.cached_tokens,
        "output_reasoning_tokens": result.reasoning_tokens,
    }
    return {key: value for key, value in pairs.items() if value is not None}


class Tracer:
    def __init__(
        self,
        client: Any | None,
        *,
        propagate: Callable[..., AbstractContextManager[Any]] | None = None,
    ):
        self._client = client
        if propagate is None and client is not None:
            from langfuse import propagate_attributes as propagate
        self._propagate = propagate

    @property
    def enabled(self) -> bool:
        return self._client is not None

    @contextmanager
    def trace(
        self,
        name: str,
        *,
        user_id: str,
        session_id: str,
        input: Any | None = None,
        tags: Sequence[str] | None = None,
        metadata: Mapping[str, str] | None = None,
    ) -> Iterator[str | None]:
        """One trace for one request: everything started inside it (the generations) nests under it, and carries the
        user and interview session (plus tags and metadata when given). Yields the trace id (None when tracing is
        off or failed to start) so scores can attach to it. Start/stop failures are swallowed; the body's own
        exceptions are not."""
        stack = ExitStack()
        trace_id: str | None = None
        if self._client is not None:
            attrs: dict[str, Any] = {"user_id": user_id, "session_id": session_id}
            if tags:
                attrs["tags"] = list(tags)
            if metadata:
                attrs["metadata"] = dict(metadata)
            try:
                span = stack.enter_context(
                    self._client.start_as_current_observation(
                        name=name, as_type="span", input=input
                    )
                )
                trace_id = getattr(span, "trace_id", None)
                stack.enter_context(self._propagate(**attrs))  # type: ignore[misc]
            except Exception as exc:
                logger.warning("langfuse trace start failed (%s)", type(exc).__name__)
        try:
            yield trace_id
        finally:
            try:
                stack.close()
            except Exception as exc:
                logger.warning("langfuse trace end failed (%s)", type(exc).__name__)

    @_safe("trace output")
    def set_trace_output(self, output: Any) -> None:
        """Set the output of the trace being built (call it inside `trace()`): what a reader sees in the trace list."""
        if self._client is not None:
            self._client.update_current_span(output=output)

    @_safe("score")
    def score(
        self,
        trace_id: str | None,
        name: str,
        value: bool | float,
        *,
        comment: str | None = None,
    ) -> None:
        """Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off or without a trace id."""
        if self._client is None or trace_id is None:
            return
        is_bool = isinstance(value, bool)
        self._client.create_score(
            trace_id=trace_id,
            name=name,
            value=float(value),
            data_type="BOOLEAN" if is_bool else "NUMERIC",
            comment=comment,
        )

    def upsert_dataset(self, name: str, items: Sequence[Mapping[str, Any]]) -> bool:
        """Create the dataset if needed and upsert its items (each carries its own `id`, so re-runs never duplicate).
        Returns whether everything was sent; failures are logged by class name and never raised."""
        if self._client is None:
            return False
        try:
            self._client.create_dataset(name=name)
            for item in items:
                self._client.create_dataset_item(dataset_name=name, **item)
        except Exception as exc:
            logger.warning("langfuse dataset upsert failed (%s)", type(exc).__name__)
            return False
        return True

    def start_generation(
        self,
        messages: Sequence[ChatMessage],
        labels: TraceLabels,
        model_parameters: Mapping[str, int | float] | None = None,
    ) -> Generation:
        if self._client is None:
            return Generation(None, labels)
        try:
            observation = self._client.start_observation(
                name=str(labels.get("task") or DEFAULT_GENERATION_NAME),
                as_type="generation",
                input=[m.model_dump() for m in messages],
                metadata=dict(labels),
                model_parameters=dict(model_parameters or {}),
            )
        except Exception as exc:
            logger.warning("langfuse generation start failed (%s)", type(exc).__name__)
            return Generation(None, labels)
        return Generation(observation, labels)

    @contextmanager
    def step(
        self, name: str, *, metadata: Mapping[str, Any] | None = None
    ) -> Iterator["Step"]:
        """A named step inside the current trace (a Langfuse `chain`): the generations and checks started inside it
        nest under it, so a trace reads score -> attempts -> checks instead of a flat list of calls. Start/stop
        failures are swallowed; the body's own exceptions are not."""
        stack = ExitStack()
        observation = None
        if self._client is not None:
            try:
                observation = stack.enter_context(
                    self._client.start_as_current_observation(
                        name=name, as_type="chain", metadata=dict(metadata or {})
                    )
                )
            except Exception as exc:
                logger.warning("langfuse step start failed (%s)", type(exc).__name__)
        try:
            yield Step(observation)
        finally:
            try:
                stack.close()
            except Exception as exc:
                logger.warning("langfuse step end failed (%s)", type(exc).__name__)

    @_safe("check")
    def check(
        self,
        name: str,
        *,
        passed: bool,
        verdict: str,
        metadata: Mapping[str, Any] | None = None,
        hint: str | None = None,
    ) -> None:
        """The code's verdict on one reply, as a Langfuse `guardrail` right after the generation it checked: a reply
        the model sent but the code rejected shows as a WARNING (with a hint on where to look) instead of looking like
        a success."""
        if self._client is None:
            return
        output: dict[str, Any] = {"passed": passed, "verdict": verdict}
        if hint:
            output["hint"] = hint
        fields: dict[str, Any] = {
            "name": name,
            "as_type": "guardrail",
            "output": output,
            "metadata": dict(metadata or {}),
        }
        if not passed:
            fields |= {"level": "WARNING", "status_message": verdict}
        self._client.start_observation(**fields).end()

    def close(self) -> None:
        """Send what is still buffered, then stop the background exporter. Called once at app shutdown."""
        if self._client is None:
            return
        for action in (self._client.flush, self._client.shutdown):
            try:
                action()
            except Exception as exc:
                logger.warning("langfuse shutdown step failed (%s)", type(exc).__name__)


def build_tracer(settings: Any, *, environment: str | None = None) -> Tracer:
    """On only when both keys are set. `environment` overrides APP_ENV (the eval runner passes "eval")."""
    if not settings.langfuse_enabled:
        if (
            settings.langfuse_public_key is not None
            or settings.langfuse_secret_key is not None
        ):
            logger.warning(
                "Langfuse tracing is off: set both LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY"
            )
        return Tracer(None)
    try:
        from langfuse import Langfuse

        client = Langfuse(
            public_key=settings.langfuse_public_key.get_secret_value(),
            secret_key=settings.langfuse_secret_key.get_secret_value(),
            base_url=settings.langfuse_base_url,
            environment=environment or settings.app_env,
        )
    except Exception as exc:
        logger.warning(
            "Langfuse tracing is off: client setup failed (%s)", type(exc).__name__
        )
        return Tracer(None)
    return Tracer(client)


class TracingProvider:
    def __init__(self, inner: LLMProvider, tracer: Tracer):
        self._inner = inner
        self._tracer = tracer

    def complete(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
        trace_labels: TraceLabels | None = None,
    ) -> LLMResult:
        generation = self._tracer.start_generation(
            messages, trace_labels or {}, _model_parameters(max_tokens, temperature)
        )
        try:
            result = self._inner.complete(
                messages,
                max_tokens=max_tokens,
                temperature=temperature,
                budget_seconds=budget_seconds,
                reasoning_effort=reasoning_effort,
            )
        except LLMError as exc:
            generation.fail(exc)
            raise
        except BaseException:
            generation.cancel("")
            raise
        generation.succeed(result)
        return result

    async def stream(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
        trace_labels: TraceLabels | None = None,
    ) -> AsyncGenerator[str | LLMResult]:
        generation = self._tracer.start_generation(
            messages, trace_labels or {}, _model_parameters(max_tokens, temperature)
        )
        parts: list[str] = []
        inner = self._inner.stream(
            messages,
            max_tokens=max_tokens,
            temperature=temperature,
            budget_seconds=budget_seconds,
            reasoning_effort=reasoning_effort,
        )
        try:
            async with aclosing(inner) as items:
                async for item in items:
                    if isinstance(item, LLMResult):
                        generation.succeed(item)
                    else:
                        parts.append(item)
                    yield item
        except LLMError as exc:
            generation.fail(exc, "".join(parts))
            raise
        finally:
            # No-op after succeed()/fail(); otherwise the consumer closed us (client left, deadline) mid-stream.
            generation.cancel("".join(parts))

    def close(self) -> None:
        self._inner.close()

    async def aclose(self) -> None:
        await self._inner.aclose()


def _model_parameters(
    max_tokens: int, temperature: float | None
) -> dict[str, int | float]:
    """What the call asked the model for, shown on the generation. A temperature only when one was sent."""
    return {"max_tokens": max_tokens} | (
        {} if temperature is None else {"temperature": temperature}
    )
