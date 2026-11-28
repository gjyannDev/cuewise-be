"""`build_chat_model`: the provider chain, one LangChain chat model per listed provider (spec FR1, AC1; U3c)."""

import os

import pytest
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, ValidationError

from app.core.ai import factory
from app.core.ai.chat_chain import ChatChain
from app.core.ai.chat_fake import FakeChatModel
from app.core.ai.factory import build_chat_model
from app.core.config import ProviderConfig, Settings

GOOGLE = {
    "LLM_PROVIDERS": "google",
    "LLM_GOOGLE_API_KEY": "test-key-123",
    "LLM_GOOGLE_MODEL": "gemini-test-model",
}


@pytest.fixture
def settings_with(monkeypatch):
    def _settings(**env):
        for name in list(os.environ):
            if name.upper().startswith("LLM_"):
                monkeypatch.delenv(name, raising=False)
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        return Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    return _settings


def primary(chain: ChatChain):
    return chain.members[0][1]


def test_an_empty_provider_list_cannot_build_a_chat_model(settings_with):  # U3c EC9: Settings refuses it first
    with pytest.raises(ValidationError):
        settings_with()


def test_google_builds_the_native_gemini_model_from_config(settings_with, app_logs):  # AC1
    chain = build_chat_model(settings_with(**GOOGLE, LLM_TIMEOUT_SECONDS="12"))

    [(name, model)] = chain.members
    assert name == "google"
    assert isinstance(model, ChatGoogleGenerativeAI)
    assert model.model == "models/gemini-test-model"  # the integration adds the "models/" prefix itself
    assert model.google_api_key is not None and model.google_api_key.get_secret_value() == "test-key-123"
    assert model.timeout == 12
    # The OpenAI-compatible base URL belongs to the old provider; the native client uses Google's own endpoint.
    assert model.base_url is None
    assert all("test-key-123" not in r.getMessage() for r in app_logs.records)


def test_every_listed_provider_gets_a_model_in_order_and_the_override_changes_only_the_primary(
    settings_with, monkeypatch
):  # U3c FR chain; AC1
    configs = [
        ProviderConfig(name=name, api_key=SecretStr("k"), model=f"{name}-model")
        for name in ("a", "b")
    ]
    monkeypatch.setattr(Settings, "llm_provider_configs", property(lambda self: configs))
    for name in ("a", "b"):
        monkeypatch.setitem(
            factory._CHAT_MODELS, name, lambda config, settings, model: FakeChatModel(default=model)
        )

    chain = build_chat_model(settings_with(**GOOGLE), model="override")

    assert [(name, member.default) for name, member in chain.members] == [("a", "override"), ("b", "b-model")]  # pyright: ignore[reportAttributeAccessIssue]


def test_the_model_override_replaces_the_configured_model(settings_with):  # evals --model
    model = primary(build_chat_model(settings_with(**GOOGLE), model="gemini-other"))
    assert isinstance(model, ChatGoogleGenerativeAI) and model.model == "models/gemini-other"


def test_the_sdks_own_retries_are_off(settings_with):  # FR3, AC4: RetryPolicy is the only retry owner
    model = primary(build_chat_model(settings_with(**GOOGLE, LLM_MAX_RETRIES="5")))
    assert isinstance(model, ChatGoogleGenerativeAI)
    assert model.max_retries == 1  # the SDK counts attempts: 1 = a single call (test_langchain_behaviour.py)


def test_no_thinking_setting_leaves_the_model_default(settings_with):  # today's calls send none
    model = primary(build_chat_model(settings_with(**GOOGLE)))
    assert isinstance(model, ChatGoogleGenerativeAI) and model.thinking_budget is None


def test_the_vendors_thinking_budget_comes_from_config(settings_with):
    model = primary(build_chat_model(settings_with(**GOOGLE, LLM_GOOGLE_THINKING_BUDGET="256")))
    assert isinstance(model, ChatGoogleGenerativeAI) and model.thinking_budget == 256


def test_the_chat_params_table_reads_only_what_the_vendor_supports(settings_with):
    settings = settings_with(**GOOGLE, LLM_GOOGLE_THINKING_BUDGET="0")
    assert settings.llm_chat_params("google") == {"thinking_budget": 0}
    assert settings_with(**GOOGLE).llm_chat_params("google") == {}
