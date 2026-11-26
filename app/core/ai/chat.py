"""The LangChain call layer's public face (U3a): the `ChatModel` type services are given, and the helpers that run one
model call under our rules.

Services type their chat model as `ChatModel` from here, so they never import `langchain*` themselves
(`tests/test_layers.py`). Feature `ai/` folders build the prompt (a `ChatPromptTemplate` from the versioned `.md`
prompt) and call `complete_chat` or `complete_structured`, which add what LangChain doesn't do our way:
- the time budget: nothing is sent once it is spent, and each attempt's timeout is the time left, capped by
  `LLM_TIMEOUT_SECONDS`;
- transport retries through the U2 `RetryPolicy` (timeouts, 429, 5xx only; full jitter; never sooner than
  Retry-After; `retry_wait`/`retry_giveup` events with the caller's task). `.with_retry()` can't do these (see
  docs/features/u3a-langchain-foundation/learnings.md), so the vendor SDK's own retries are off;
- one Langfuse generation per call (`chat_tracing.ChatTrace`), with the caller's labels;
- vendor errors mapped to our LLMError types (`chat_errors.to_llm_error`), and the reply returned as our
  `LLMResult`, so the callers' logging (`log_result`, `log_llm_call`) stays as it is.
"""

import time
from collections.abc import Callable, Mapping, Sequence
from typing import Any, NamedTuple

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from app.core.config import settings
from app.core.logging import get_logger

from .chat_errors import to_llm_error
from .chat_tracing import ChatTrace, TracerHandle
from .provider import (
    ChatMessage,
    LLMBadResponseError,
    LLMError,
    LLMResult,
    LLMTimeoutError,
)
from .retry import RetryPolicy
from .tracing import TraceLabels

# Any LangChain chat model the factory builds (Gemini today; `FakeChatModel` in tests).
type ChatModel = BaseChatModel

logger = get_logger("app.llm")

# Vendor finish reasons in the old layer's words: code and evals look for "length" (cut off by max tokens).
_FINISH_REASONS = {"STOP": "stop", "MAX_TOKENS": "length"}


class Structured[T](NamedTuple):
    """A structured call's outcome: the parsed object, or None with `error` saying why the reply didn't fit the schema
    (the model answered; that is a content problem, for the caller's own attempt loop). `result` has the usage."""

    value: T | None
    error: str | None
    result: LLMResult


_MESSAGE_TYPES: dict[str, type[BaseMessage]] = {"system": SystemMessage, "user": HumanMessage, "assistant": AIMessage}


def fixed_prompt(messages: Sequence[ChatMessage]) -> ChatPromptTemplate:
    """A prompt of already-built messages (our context manager's output), sent exactly as they are.

    Message objects, not `("role", "text")` tuples: a tuple is parsed as a template, so a `{` inside a job description
    or résumé would be read as a variable. With message objects nothing is substituted; the prompt takes no inputs.
    """
    return ChatPromptTemplate.from_messages([_MESSAGE_TYPES[m.role](content=m.content) for m in messages])


def complete_chat(
    model: ChatModel,
    prompt: Runnable[Any, Any],
    inputs: Mapping[str, Any],
    *,
    max_tokens: int,
    budget_seconds: float,
    labels: TraceLabels,
    temperature: float | None = None,
    timeout_seconds: float | None = None,
    max_retries: int | None = None,
    clock: Callable[[], float] = time.perf_counter,
    sleep: Callable[[float], None] = time.sleep,
) -> LLMResult:
    """Run `prompt | model` once under the rules above; raises an LLMError when no usable text came back."""
    _output, result = _run(
        model,
        prompt,
        inputs,
        lambda bound: bound,
        max_tokens=max_tokens,
        budget_seconds=budget_seconds,
        labels=labels,
        temperature=temperature,
        timeout_seconds=timeout_seconds,
        max_retries=max_retries,
        clock=clock,
        sleep=sleep,
    )
    return result


def complete_structured[T](
    model: ChatModel,
    prompt: Runnable[Any, Any],
    inputs: Mapping[str, Any],
    schema: type[T],
    *,
    max_tokens: int,
    budget_seconds: float,
    labels: TraceLabels,
    temperature: float | None = None,
    timeout_seconds: float | None = None,
    max_retries: int | None = None,
    clock: Callable[[], float] = time.perf_counter,
    sleep: Callable[[float], None] = time.sleep,
) -> Structured[T]:
    """`prompt | model.with_structured_output(schema)` (Gemini's native JSON schema). A reply that doesn't fit the
    schema is returned as `Structured(None, error, result)`, never raised; transport failures raise as LLMErrors."""
    output, result = _run(
        model,
        prompt,
        inputs,
        lambda bound: bound.with_structured_output(schema, method="json_schema", include_raw=True),
        max_tokens=max_tokens,
        budget_seconds=budget_seconds,
        labels=labels,
        temperature=temperature,
        timeout_seconds=timeout_seconds,
        max_retries=max_retries,
        clock=clock,
        sleep=sleep,
    )
    parsing_error = output.get("parsing_error")
    if parsing_error is not None:
        # The class name only: the parser's message quotes the reply, which may be personal data (a résumé).
        return Structured(None, f"schema:{type(parsing_error).__name__}", result)
    return Structured(output["parsed"], None, result)


def _run(
    model: ChatModel,
    prompt: Runnable[Any, Any],
    inputs: Mapping[str, Any],
    finish: Callable[[Any], Runnable[Any, Any]],
    *,
    max_tokens: int,
    budget_seconds: float,
    labels: TraceLabels,
    temperature: float | None,
    timeout_seconds: float | None,
    max_retries: int | None,
    clock: Callable[[], float],
    sleep: Callable[[float], None],
) -> tuple[Any, LLMResult]:
    per_call_timeout = timeout_seconds if timeout_seconds is not None else settings.llm_timeout_seconds
    policy = RetryPolicy(
        max_retries=settings.llm_max_retries if max_retries is None else max_retries,
        task="chat",
        logger=logger,
        clock=clock,
        sleep=sleep,
    )
    tracer = _tracer_of(model)
    params: dict[str, int | float] = {"max_tokens": max_tokens} | ({"temperature": temperature} if temperature is not None else {})
    trace = ChatTrace(tracer, labels, params) if tracer is not None else None
    config = {"callbacks": [trace]} if trace is not None else None
    temperature_update = {"temperature": temperature} if temperature is not None else {}

    def attempt(remaining: float) -> tuple[Any, AIMessage]:
        if remaining <= 0:
            raise LLMTimeoutError("LLM call has no time left")
        # Per-call limits are set on a copy of the shared model (one model serves every request; a pydantic copy
        # shares the vendor client, so it is cheap), never with `.bind()`: `with_structured_output` on a bound model
        # drops the bound kwargs (test_langchain_behaviour.py). The timeout never runs past the time left.
        # `max_output_tokens` is the Gemini integration's name for the token cap.
        limited = model.model_copy(
            update={"timeout": min(per_call_timeout, remaining), "max_output_tokens": max_tokens} | temperature_update
        )
        try:
            output = (prompt | finish(limited)).invoke(dict(inputs), config=config)  # type: ignore[arg-type]
        except Exception as exc:  # every vendor/framework error leaves core/ai as an LLMError
            raise to_llm_error(exc) from exc
        message = output["raw"] if isinstance(output, dict) else output
        if not isinstance(message, AIMessage) or not message.text.strip():
            finish_reason = message.response_metadata.get("finish_reason") if isinstance(message, AIMessage) else None
            raise LLMBadResponseError("LLM returned an empty message", finish_reason=_finish_reason(finish_reason))
        return output, message

    task = labels.get("task")
    try:
        done = policy.call(attempt, budget=budget_seconds, task=task if isinstance(task, str) else None)
    except LLMError as exc:
        if trace is not None:
            trace.fail(exc)
        raise
    output, message = done.value
    result = _result(message, model, attempts=done.attempts, latency_ms=done.latency_ms)
    if trace is not None:
        trace.succeed(result)
    return output, result


def _tracer_of(model: ChatModel):
    """The tracer the factory attached to the model (`build_chat_model(..., tracer=)`), if any."""
    callbacks = model.callbacks if isinstance(model.callbacks, list) else []
    handle = next((c for c in callbacks if isinstance(c, TracerHandle)), None)
    return handle.tracer if handle is not None and handle.tracer.enabled else None


def _result(message: AIMessage, model: ChatModel, *, attempts: int, latency_ms: int) -> LLMResult:
    usage = message.usage_metadata or {}
    output_details = usage.get("output_token_details") or {}
    input_details = usage.get("input_token_details") or {}
    meta = message.response_metadata
    return LLMResult(
        text=message.text.strip(),
        model=str(meta.get("model_name") or getattr(model, "model", "") or "unknown"),
        prompt_tokens=usage.get("input_tokens"),
        # Includes the thinking tokens, as the old layer's completion_tokens did; reasoning_tokens is that part.
        completion_tokens=usage.get("output_tokens"),
        reasoning_tokens=output_details.get("reasoning"),
        cached_tokens=input_details.get("cache_read"),
        latency_ms=latency_ms,
        finish_reason=_finish_reason(meta.get("finish_reason")),
        attempts=attempts,
    )


def _finish_reason(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    return _FINISH_REASONS.get(value, value.lower())
