import logging

import pytest

from app.core.ai.factory import build_provider
from app.core.ai.fake import FakeProvider
from app.core.ai.openrouter import OpenRouterProvider
from app.core.ai.provider import ChatMessage, LLMResult, LLMTimeoutError
from app.core.config import Settings


@pytest.fixture
def settings_with(monkeypatch):
    def _settings(**env):
        for name in ("OPENROUTER_API_KEY", "LLM_MODEL"):
            monkeypatch.delenv(name, raising=False)
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        return Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    return _settings


def test_no_key_and_model_means_no_provider_and_one_warning(settings_with, app_logs):  # EC18, AC16
    provider = build_provider(settings_with())

    assert provider is None
    [warning] = [r for r in app_logs.records if r.name == "app.llm"]
    assert warning.levelno == logging.WARNING
    assert "reactions will be null" in warning.getMessage()


def test_key_and_model_build_the_openrouter_provider(settings_with, app_logs):  # AC13, AC16
    provider = build_provider(settings_with(OPENROUTER_API_KEY="test-key-123", LLM_MODEL="vendor/model-x"))

    assert isinstance(provider, OpenRouterProvider)
    assert not [r for r in app_logs.records if r.name == "app.llm"]
    assert all("test-key-123" not in r.getMessage() for r in app_logs.records)
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
