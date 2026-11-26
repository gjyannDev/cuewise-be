"""Pins the LangChain and langchain-google-genai behavior the U3a call layer relies on (the step 1 spike).

No network: the Gemini model gets a scripted SDK client (`generate_content` returns a canned response or raises a
`google.api_core` exception), and the generic Runnable behavior is checked on small hand-made chat models. If one of
these fails after a dependency upgrade, the call layer's assumptions (`app/core/ai/chat*.py`) need a second look.
"""

import inspect
from collections.abc import Iterator
from typing import Any

import pytest
from google.ai.generativelanguage_v1beta.types import GenerateContentResponse
from google.api_core import exceptions as gx
from google.protobuf import duration_pb2
from google.rpc import error_details_pb2
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from pydantic import BaseModel


class _Reply(BaseModel):
    name: str
    skills: list[str]


class _ScriptedClient:
    """Stands in for the SDK's `GenerativeServiceClient`: each call pops the next outcome (a response or an
    exception) and records the keyword arguments it was given."""

    def __init__(self, *outcomes: GenerateContentResponse | Exception):
        self.outcomes = list(outcomes)
        self.calls: list[dict[str, Any]] = []

    def generate_content(self, **kwargs: Any) -> GenerateContentResponse:
        self.calls.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def _response(text: str, *, prompt: int = 5, candidates: int = 3, thoughts: int = 0) -> GenerateContentResponse:
    return GenerateContentResponse(
        candidates=[{"content": {"parts": [{"text": text}], "role": "model"}, "finish_reason": "STOP"}],
        usage_metadata={
            "prompt_token_count": prompt,
            "candidates_token_count": candidates,
            "thoughts_token_count": thoughts,
            "total_token_count": prompt + candidates + thoughts,
        },
    )


def _gemini(client: _ScriptedClient, **fields: Any) -> ChatGoogleGenerativeAI:
    model = ChatGoogleGenerativeAI(model="gemini-test", google_api_key="test-key", **fields)
    # The model is a pydantic object; the client is built in its validator, so swap it in after construction.
    object.__setattr__(model, "client", client)
    return model


# --- Gemini integration -------------------------------------------------------------------------------------------


def test_the_sdk_max_retries_counts_attempts_so_one_means_a_single_call():
    # The SDK's own tenacity loop uses stop_after_attempt(max_retries): 1 is "no retries", not "one retry".
    client = _ScriptedClient(gx.ServiceUnavailable("down"), _response("never reached"))
    with pytest.raises(gx.ServiceUnavailable):
        _gemini(client, max_retries=1).invoke("hi")
    assert len(client.calls) == 1


def test_the_sdk_retries_every_google_api_error_by_default_even_a_4xx(monkeypatch: pytest.MonkeyPatch):
    # Its retry predicate includes the GoogleAPIError base class, so a 403 would be retried too: one more reason to
    # turn it off and keep one retry owner with our rules.
    monkeypatch.setattr("time.sleep", lambda _seconds: None)  # the SDK's backoff waits at least 1 s
    client = _ScriptedClient(gx.PermissionDenied("no"), _response("ok"))
    assert _gemini(client, max_retries=2).invoke("hi").content == "ok"
    assert len(client.calls) == 2


def test_a_per_call_timeout_and_generation_config_reach_the_request_through_bind():
    client = _ScriptedClient(_response("ok"))
    model = _gemini(client, max_retries=1, timeout=15)
    model.bind(timeout=2.5, generation_config={"temperature": 0.2, "max_output_tokens": 50}).invoke("hi")
    call = client.calls[0]
    assert call["timeout"] == 2.5  # the per-call value wins over the model's
    assert call["request"].generation_config.temperature == pytest.approx(0.2)
    assert call["request"].generation_config.max_output_tokens == 50


def test_the_model_timeout_is_used_when_the_call_sets_none():
    client = _ScriptedClient(_response("ok"))
    _gemini(client, max_retries=1, timeout=15).invoke("hi")
    assert client.calls[0]["timeout"] == 15


def test_thinking_budget_becomes_the_requests_thinking_config():
    client = _ScriptedClient(_response("ok"))
    _gemini(client, max_retries=1, thinking_budget=128).invoke("hi")
    assert client.calls[0]["request"].generation_config.thinking_config.thinking_budget == 128


def test_thinking_level_is_not_supported_by_the_bundled_sdk():
    # The field exists on the LangChain model, but google-ai-generativelanguage's ThinkingConfig has no such field
    # yet, so building the request fails. The config table may only use thinking_budget for now.
    client = _ScriptedClient(_response("ok"))
    with pytest.raises(ValueError, match="thinking_level"):
        _gemini(client, max_retries=1, thinking_level="low").invoke("hi")
    assert client.calls == []


def test_no_thinking_setting_sends_no_thinking_config():
    client = _ScriptedClient(_response("ok"))
    _gemini(client, max_retries=1).invoke("hi")
    assert "thinking_config" not in client.calls[0]["request"].generation_config


def test_a_gemini_3_model_defaults_to_temperature_1_like_the_vendor_default():
    # Today's OpenAI-compatible call sends no temperature for the summary, so Gemini uses its own default (1.0).
    assert ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", google_api_key="k").temperature == 1.0


def test_usage_metadata_counts_thinking_tokens_inside_output_tokens():
    client = _ScriptedClient(_response("ok", prompt=10, candidates=4, thoughts=6))
    message = _gemini(client, max_retries=1).invoke("hi")
    assert message.usage_metadata is not None
    assert message.usage_metadata["input_tokens"] == 10
    assert message.usage_metadata["output_tokens"] == 10  # candidates + thoughts
    assert message.usage_metadata.get("output_token_details") == {"reasoning": 6}
    assert message.response_metadata["finish_reason"] == "STOP"


def test_a_response_with_no_candidates_is_an_empty_message_not_an_error():
    client = _ScriptedClient(GenerateContentResponse(prompt_feedback={"block_reason": "SAFETY"}))
    assert _gemini(client, max_retries=1).invoke("hi").content == ""


def test_invalid_argument_is_wrapped_but_keeps_the_google_error_as_its_cause():
    client = _ScriptedClient(gx.InvalidArgument("bad"))
    with pytest.raises(ChatGoogleGenerativeAIError) as info:
        _gemini(client, max_retries=1).invoke("hi")
    assert isinstance(info.value.__cause__, gx.InvalidArgument)


def test_google_errors_carry_the_http_status_and_retry_after_as_a_retry_info_detail():
    delay = error_details_pb2.RetryInfo(retry_delay=duration_pb2.Duration(seconds=7, nanos=500_000_000))
    exc = gx.ResourceExhausted("quota", details=[delay])
    assert exc.code == 429
    assert not hasattr(exc, "retry_after")  # so the SDK's own "sleep retry_after" branch never runs
    assert exc.details[0].retry_delay.ToTimedelta().total_seconds() == 7.5
    assert gx.DeadlineExceeded("slow").code == 504
    assert gx.ServiceUnavailable("down").code == 503


def test_structured_output_with_include_raw_returns_a_parsing_error_instead_of_raising():
    client = _ScriptedClient(_response('{"name": "Ada"}'))  # skills missing
    runnable = _gemini(client, max_retries=1).with_structured_output(_Reply, method="json_schema", include_raw=True)
    out = runnable.invoke("hi")
    assert isinstance(out, dict)  # include_raw=True: {"raw", "parsed", "parsing_error"}
    assert out["parsed"] is None
    assert out["parsing_error"] is not None
    assert isinstance(out["raw"], AIMessage)  # the raw reply (and its usage) survives a parse failure
    assert client.calls[0]["request"].generation_config.response_mime_type == "application/json"


def test_structured_output_parses_a_valid_reply():
    client = _ScriptedClient(_response('{"name": "Ada", "skills": ["python"]}'))
    out = _gemini(client, max_retries=1).with_structured_output(_Reply, method="json_schema", include_raw=True).invoke("hi")
    assert isinstance(out, dict)
    assert out["parsed"] == _Reply(name="Ada", skills=["python"])
    assert out["parsing_error"] is None


def test_structured_output_on_a_bound_model_drops_the_bound_kwargs():
    # A RunnableBinding forwards `with_structured_output` to the model it wraps, which builds a new chain from itself:
    # the per-call `timeout` bound before is lost. So per-call limits are set on a model copy instead (chat.py).
    client = _ScriptedClient(_response('{"name": "Ada", "skills": []}'))
    model = _gemini(client, max_retries=1, timeout=15)
    model.bind(timeout=2.5).with_structured_output(_Reply, method="json_schema", include_raw=True).invoke("hi")
    assert client.calls[0]["timeout"] == 15


def test_per_call_limits_set_on_a_model_copy_survive_structured_output():
    client = _ScriptedClient(_response('{"name": "Ada", "skills": []}'))
    model = _gemini(client, max_retries=1, timeout=15)
    copy = model.model_copy(update={"timeout": 2.5, "max_output_tokens": 50, "temperature": 0.2})
    copy.with_structured_output(_Reply, method="json_schema", include_raw=True).invoke("hi")
    call = client.calls[0]
    assert call["timeout"] == 2.5 and call["request"].generation_config.max_output_tokens == 50
    assert call["request"].generation_config.temperature == pytest.approx(0.2)
    assert model.timeout == 15  # the shared model is untouched


def test_structured_output_still_raises_a_transport_error():
    client = _ScriptedClient(gx.ServiceUnavailable("down"))
    runnable = _gemini(client, max_retries=1).with_structured_output(_Reply, method="json_schema", include_raw=True)
    with pytest.raises(gx.ServiceUnavailable):
        runnable.invoke("hi")


# --- Generic Runnable behavior (with_retry, with_fallbacks, streaming) --------------------------------------------


class _Flaky(BaseChatModel):
    """Fails its first `failures` calls; `fail_after_first_chunk` makes a stream fail after one chunk instead."""

    failures: int = 0
    fail_after_first_chunk: bool = False
    calls: int = 0
    reply: str = "ok"

    @property
    def _llm_type(self) -> str:
        return "flaky"

    def _generate(self, messages: list[BaseMessage], stop: Any = None, run_manager: Any = None, **kw: Any) -> ChatResult:
        self.calls += 1
        if self.calls <= self.failures:
            raise TimeoutError("flaky")
        return ChatResult(generations=[ChatGeneration(message=AIMessage(self.reply))])

    def _stream(
        self, messages: list[BaseMessage], stop: Any = None, run_manager: Any = None, **kw: Any
    ) -> Iterator[ChatGenerationChunk]:
        self.calls += 1
        if self.calls <= self.failures and not self.fail_after_first_chunk:
            raise TimeoutError("flaky")
        yield ChatGenerationChunk(message=AIMessageChunk(content=self.reply[0]))
        if self.calls <= self.failures:
            raise TimeoutError("flaky after output")
        yield ChatGenerationChunk(message=AIMessageChunk(content=self.reply[1:]))


def test_with_retry_offers_only_exception_type_jitter_and_attempt_count():
    # No Retry-After, no deadline stop and no before-sleep hook: the U2 rules can't be expressed on it.
    params = set(inspect.signature(Runnable.with_retry).parameters) - {"self"}
    assert params == {"retry_if_exception_type", "wait_exponential_jitter", "exponential_jitter_params", "stop_after_attempt"}


def test_with_retry_retries_invoke():
    model = _Flaky(failures=1)
    assert model.with_retry(stop_after_attempt=2, wait_exponential_jitter=False).invoke("hi").content == "ok"
    assert model.calls == 2


def test_with_retry_does_not_retry_a_stream_at_all():
    # RunnableRetry doesn't override stream, so a stream that fails before its first chunk is not retried (U3b note).
    model = _Flaky(failures=1)
    with pytest.raises(TimeoutError):
        list(model.with_retry(stop_after_attempt=3, wait_exponential_jitter=False).stream("hi"))
    assert model.calls == 1


def test_with_fallbacks_switches_a_stream_that_fails_before_its_first_chunk():
    primary, backup = _Flaky(failures=1), _Flaky(reply="bk")
    chunks = [str(c.content) for c in primary.with_fallbacks([backup]).stream("hi")]
    assert "".join(chunks) == "bk"


def test_with_fallbacks_raises_a_stream_that_fails_after_its_first_chunk():
    primary, backup = _Flaky(failures=1, fail_after_first_chunk=True), _Flaky(reply="bk")
    seen: list[str] = []
    with pytest.raises(TimeoutError):
        for chunk in primary.with_fallbacks([backup]).stream("hi"):
            seen.append(str(chunk.content))
    assert seen == ["o"] and backup.calls == 0


def test_a_human_message_list_is_accepted_as_model_input():
    assert _Flaky().invoke([HumanMessage("hi")]).content == "ok"
