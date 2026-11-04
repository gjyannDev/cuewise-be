import logging
import os

import pytest

from app.core.ai.deepgram import DeepgramTranscriber
from app.core.ai.factory import build_provider, build_transcriber
from app.core.ai.fake import FakeProvider
from app.core.ai.openai_compatible import OpenAICompatibleProvider
from app.core.ai.provider import ChatMessage, LLMResult, LLMTimeoutError
from app.core.config import Settings


@pytest.fixture
def settings_with(monkeypatch):
    def _settings(**env):
        for name in list(os.environ):
            if name.upper().startswith(("LLM_", "OPENROUTER_", "DEEPGRAM_", "TRANSCRIPTION_")):
                monkeypatch.delenv(name, raising=False)
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        return Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    return _settings


@pytest.fixture
def anyio_backend():
    return "asyncio"


def test_no_deepgram_key_means_no_transcriber_and_one_warning(settings_with, app_logs):  # voice AC6, EC22
    assert build_transcriber(settings_with()) is None

    [warning] = [r for r in app_logs.records if r.name == "app.stt"]
    assert warning.levelno == logging.WARNING
    assert "voice answers are off" in warning.getMessage()


@pytest.mark.anyio
async def test_a_deepgram_key_builds_a_deepgram_transcriber(settings_with, app_logs):  # voice AC8
    transcriber = build_transcriber(settings_with(DEEPGRAM_API_KEY="dg-secret-123", DEEPGRAM_MODEL="nova-3-medical"))

    assert isinstance(transcriber, DeepgramTranscriber)
    assert transcriber.model == "nova-3-medical"
    assert not [r for r in app_logs.records if r.name == "app.stt"]
    assert all("dg-secret-123" not in r.getMessage() for r in app_logs.records)
    await transcriber.aclose()


def test_no_key_and_model_means_no_provider_and_one_warning(settings_with, app_logs):  # EC18, AC16
    provider = build_provider(settings_with())

    assert provider is None
    [warning] = [r for r in app_logs.records if r.name == "app.llm"]
    assert warning.levelno == logging.WARNING
    assert "questions will come from the question bank" in warning.getMessage()


GOOGLE = {
    "LLM_PROVIDERS": "google",
    "LLM_GOOGLE_API_KEY": "test-key-123",
    "LLM_GOOGLE_MODEL": "vendor/model-x",
    "LLM_GOOGLE_BASE_URL": "https://google.test/v1beta/openai/",
}


def test_listed_provider_builds_an_openai_compatible_provider(settings_with, app_logs):  # AC13, AC16, Step 0
    provider = build_provider(settings_with(**GOOGLE))

    assert isinstance(provider, OpenAICompatibleProvider)
    assert provider.model == "vendor/model-x"
    assert not [r for r in app_logs.records if r.name == "app.llm"]
    assert all("test-key-123" not in r.getMessage() for r in app_logs.records)
    provider.close()


def test_model_override_replaces_the_primary_providers_model(settings_with):  # evals --model, Step 0
    provider = build_provider(settings_with(**GOOGLE), model="vendor/other")

    assert isinstance(provider, OpenAICompatibleProvider)
    assert provider.model == "vendor/other"
    provider.close()


def test_fake_records_messages_and_returns_scripted_replies():  # test double used by endpoint tests
    fake = FakeProvider(["First.", LLMTimeoutError("slow")])
    messages = [ChatMessage(role="user", content="hello there")]

    first = fake.complete(messages, max_tokens=10)
    with pytest.raises(LLMTimeoutError):
        fake.complete(messages, max_tokens=10)
    default = fake.complete(messages, max_tokens=10)

    assert isinstance(first, LLMResult)
    assert first.text == "First."
    assert first.prompt_tokens and first.prompt_tokens > 0
    assert default.text == FakeProvider.DEFAULT_REPLY
    assert fake.calls == [messages, messages, messages]


def test_fake_runs_the_on_call_hook_at_call_time():
    seen = []
    fake = FakeProvider(on_call=lambda: seen.append("called"))

    fake.complete([ChatMessage(role="user", content="hi")], max_tokens=10)

    assert seen == ["called"]


def test_fake_records_the_budget_it_was_given():  # llm-interviewer AC7
    fake = FakeProvider()

    fake.complete([ChatMessage(role="user", content="hi")], max_tokens=10, budget_seconds=12.5)
    fake.complete([ChatMessage(role="user", content="hi")], max_tokens=10)

    assert fake.budgets == [12.5, None]


def test_fake_records_the_reasoning_effort():  # context-management AC18
    fake = FakeProvider()

    fake.complete([ChatMessage(role="user", content="hi")], max_tokens=10, reasoning_effort="high")
    fake.complete([ChatMessage(role="user", content="hi")], max_tokens=10)

    assert fake.reasoning_efforts == ["high", None]


def test_enabled_tracer_wraps_the_provider_and_a_disabled_one_does_not(settings_with):  # AC1, AC8
    from app.core.ai.tracing import Tracer, TracingProvider

    wrapped = build_provider(settings_with(**GOOGLE), tracer=Tracer(object(), propagate=lambda **_: None))
    plain = build_provider(settings_with(**GOOGLE), tracer=Tracer(None))

    assert isinstance(wrapped, TracingProvider)
    assert isinstance(plain, OpenAICompatibleProvider)
