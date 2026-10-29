import json

import httpx
import pytest

from app.core.ai.openrouter import OpenRouterProvider
from app.core.ai.provider import (
    ChatMessage,
    LLMBadResponseError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)

API_KEY = "test-key-123"

MESSAGES = [
    ChatMessage(role="system", content="You are an interviewer."),
    ChatMessage(role="assistant", content="Tell me about a conflict."),
    ChatMessage(role="user", content="We argued about REST vs GraphQL."),
]


def completion(content="Nice, a prototype settles it.", finish_reason="stop", usage=True, model="vendor/model-x"):
    """A chat-completions body in the OpenAI-compatible shape OpenRouter returns."""
    body = {
        "id": "gen-1",
        "model": model,
        "choices": [{"message": {"role": "assistant", "content": content}, "finish_reason": finish_reason}],
    }
    if usage:
        body["usage"] = {"prompt_tokens": 212, "completion_tokens": 18, "total_tokens": 230}
    return body


class Clock:
    """Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant."""

    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def make_provider(clock):
    """Provider whose HTTP layer is a scripted list of responses (or exceptions), one per attempt."""

    def _make(*script, max_retries=2, budget=30.0, timeout=15.0):
        requests: list[httpx.Request] = []
        steps = list(script)

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            step = steps.pop(0)
            if isinstance(step, Exception):
                raise step
            if callable(step):
                return step(request)
            return step

        provider = OpenRouterProvider(
            api_key=API_KEY,
            model="vendor/model-x",
            base_url="https://llm.test/api/v1",
            timeout_seconds=timeout,
            max_retries=max_retries,
            total_budget_seconds=budget,
            transport=httpx.MockTransport(handler),
            sleep=clock.sleep,
            clock=clock,
        )
        return provider, requests

    return _make


def test_success_returns_text_model_usage_and_finish_reason(make_provider):  # AC12 (happy path), concept 1
    provider, _ = make_provider(httpx.Response(200, json=completion()))

    result = provider.complete(MESSAGES, max_tokens=150)

    assert result.text == "Nice, a prototype settles it."
    assert result.model == "vendor/model-x"
    assert (result.prompt_tokens, result.completion_tokens) == (212, 18)
    assert result.finish_reason == "stop"
    assert result.attempts == 1


def test_request_is_an_openai_compatible_chat_completion(make_provider):  # AC13, concept 1
    provider, requests = make_provider(httpx.Response(200, json=completion()))

    provider.complete(MESSAGES, max_tokens=150)

    [request] = requests
    assert request.method == "POST"
    assert str(request.url) == "https://llm.test/api/v1/chat/completions"
    assert request.headers["Authorization"] == f"Bearer {API_KEY}"
    body = json.loads(request.content)
    assert body == {
        "model": "vendor/model-x",
        "max_tokens": 150,
        "messages": [{"role": m.role, "content": m.content} for m in MESSAGES],
    }


def test_temperature_is_sent_only_when_given(make_provider):  # learning experiment hook
    provider, requests = make_provider(httpx.Response(200, json=completion()))

    provider.complete(MESSAGES, max_tokens=50, temperature=0.0)

    assert json.loads(requests[0].content)["temperature"] == 0.0


def test_missing_usage_gives_none_token_counts(make_provider):  # EC17
    provider, _ = make_provider(httpx.Response(200, json=completion(usage=False)))

    result = provider.complete(MESSAGES, max_tokens=150)

    assert (result.prompt_tokens, result.completion_tokens) == (None, None)


def test_reply_cut_by_max_tokens_is_returned_as_received(make_provider):  # EC16
    provider, _ = make_provider(
        httpx.Response(200, json=completion(content="Building a proto", finish_reason="length"))
    )

    result = provider.complete(MESSAGES, max_tokens=4)

    assert (result.text, result.finish_reason) == ("Building a proto", "length")


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(200, json=completion(content="   ")),
        httpx.Response(200, json=completion(content=None)),
        httpx.Response(200, json={"choices": []}),
        httpx.Response(200, json={"error": {"message": "upstream failed"}}),
        httpx.Response(200, text="<html>not json</html>"),
    ],
    ids=["blank", "null-content", "no-choices", "error-body", "not-json"],
)
def test_unusable_reply_raises_bad_response_without_retry(make_provider, response):  # EC15
    provider, requests = make_provider(response)

    with pytest.raises(LLMBadResponseError) as exc:
        provider.complete(MESSAGES, max_tokens=150)

    assert len(requests) == 1
    assert exc.value.attempts == 1


def test_rate_limit_then_success_retries_once_with_backoff(make_provider, clock):  # EC13, AC12
    provider, requests = make_provider(httpx.Response(429), httpx.Response(200, json=completion()))

    result = provider.complete(MESSAGES, max_tokens=150)

    assert result.text == "Nice, a prototype settles it."
    assert result.attempts == 2
    assert len(requests) == 2
    [delay] = clock.sleeps
    assert 0.5 <= delay <= 0.75  # 0.5s base plus up to 50% jitter


@pytest.mark.parametrize(
    ("failure", "error"),
    [
        (lambda: httpx.Response(503), LLMServerError),
        (lambda: httpx.Response(500), LLMServerError),
        (lambda: httpx.Response(429), LLMRateLimitError),
        (lambda: httpx.ReadTimeout("slow"), LLMTimeoutError),
        (lambda: httpx.ConnectError("refused"), LLMServerError),
    ],
    ids=["503", "500", "429", "timeout", "connect-error"],
)
def test_transient_failure_on_every_attempt_gives_up_after_max_retries(make_provider, clock, failure, error):  # EC11
    provider, requests = make_provider(failure(), failure(), failure(), max_retries=2)

    with pytest.raises(error) as exc:
        provider.complete(MESSAGES, max_tokens=150)

    assert len(requests) == 3  # first try + 2 retries
    assert exc.value.attempts == 3
    assert len(clock.sleeps) == 2
    assert clock.sleeps[1] > clock.sleeps[0]  # exponential: ~0.5s then ~1s


@pytest.mark.parametrize("status", [400, 401, 403, 404, 422])
def test_client_errors_are_never_retried(make_provider, clock, status):  # EC12
    provider, requests = make_provider(httpx.Response(status, json={"error": {"message": "bad key"}}))

    with pytest.raises(LLMRequestError) as exc:
        provider.complete(MESSAGES, max_tokens=150)

    assert len(requests) == 1
    assert exc.value.status_code == status
    assert clock.sleeps == []


def test_retries_stop_when_the_total_budget_would_be_exceeded(make_provider, clock):  # EC14
    provider, requests = make_provider(*[httpx.Response(503)] * 6, max_retries=5, budget=1.0)

    with pytest.raises(LLMServerError):
        provider.complete(MESSAGES, max_tokens=150)

    # ~0.5s wait fits in the 1s budget, the next ~1s wait does not: 2 attempts, not 6.
    assert len(requests) == 2
    assert clock.now < 1.0


def test_each_attempt_waits_no_longer_than_the_remaining_budget(
    make_provider,
):  # EC14, inferred: last attempt can't overrun
    seen = []

    def record_timeout(request):
        seen.append(request.extensions["timeout"]["read"])
        return httpx.Response(200, json=completion())

    provider, _ = make_provider(record_timeout, timeout=15.0, budget=10.0)

    provider.complete(MESSAGES, max_tokens=150)

    assert seen == [10.0]


def test_slow_but_successful_call_is_just_slow(make_provider, clock):  # EC24
    def slow(request):
        clock.now += 12.0
        return httpx.Response(200, json=completion())

    provider, _ = make_provider(slow)

    result = provider.complete(MESSAGES, max_tokens=150)

    assert (result.attempts, result.latency_ms) == (1, 12000)


def test_error_messages_never_carry_the_response_body(make_provider):  # inferred: privacy, error text may reach logs
    provider, _ = make_provider(httpx.Response(401, json={"error": {"message": "key sk-or-abc is invalid"}}))

    with pytest.raises(LLMRequestError) as exc:
        provider.complete(MESSAGES, max_tokens=150)

    assert "sk-or-abc" not in str(exc.value)


def test_empty_reply_error_carries_the_finish_reason(make_provider):  # llm-interviewer EC16
    body = completion(content=None, finish_reason="length")
    provider, requests = make_provider(httpx.Response(200, json=body))

    with pytest.raises(LLMBadResponseError) as exc:
        provider.complete(MESSAGES, max_tokens=150)

    assert exc.value.finish_reason == "length"
    assert len(requests) == 1


def test_a_smaller_budget_argument_caps_retries(make_provider, clock):  # llm-interviewer AC7
    provider, requests = make_provider(*[httpx.Response(503)] * 6, max_retries=5, budget=30.0)

    with pytest.raises(LLMServerError):
        provider.complete(MESSAGES, max_tokens=150, budget_seconds=1.0)

    assert len(requests) == 2
    assert clock.now < 1.0


def test_a_larger_budget_argument_never_raises_the_configured_budget(make_provider, clock):  # llm-interviewer AC7
    provider, requests = make_provider(*[httpx.Response(503)] * 6, max_retries=5, budget=1.0)

    with pytest.raises(LLMServerError):
        provider.complete(MESSAGES, max_tokens=150, budget_seconds=100.0)

    assert len(requests) == 2


def test_the_attempt_timeout_follows_the_budget_argument(make_provider):  # llm-interviewer AC7
    seen = []

    def record_timeout(request):
        seen.append(request.extensions["timeout"]["read"])
        return httpx.Response(200, json=completion())

    provider, _ = make_provider(record_timeout, timeout=15.0, budget=30.0)

    provider.complete(MESSAGES, max_tokens=150, budget_seconds=4.0)

    assert seen == [4.0]
