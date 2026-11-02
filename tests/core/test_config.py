import os

import pytest
from pydantic import ValidationError

from app.core.config import ProviderConfig, Settings

GOOGLE = {
    "LLM_GOOGLE_API_KEY": "google-test-secret",
    "LLM_GOOGLE_MODEL": "gemini-test",
    "LLM_GOOGLE_BASE_URL": "https://google.test/v1beta/openai/",
}


@pytest.fixture
def no_llm_env(monkeypatch):
    """Settings built from a clean environment, so a developer's real key never leaks into these tests."""
    for name in list(os.environ):
        if name.upper().startswith(("LLM_", "OPENROUTER_")):
            monkeypatch.delenv(name, raising=False)
    return monkeypatch


def _settings() -> Settings:
    return Settings(_env_file=None)  # pyright: ignore[reportCallIssue]


def _google(env, **overrides):
    env.setenv("LLM_PROVIDERS", "google")
    for name, value in {**GOOGLE, **overrides}.items():
        env.setenv(name, value)


def test_settings_refuse_missing_jwt_secret(monkeypatch):  # AC12, EC18
    monkeypatch.delenv("JWT_SECRET_KEY", raising=False)

    with pytest.raises(ValidationError) as exc:
        _settings()

    assert "jwt_secret_key" in str(exc.value)


def test_settings_refuse_short_jwt_secret(monkeypatch):  # AC12, inferred: weak key
    monkeypatch.setenv("JWT_SECRET_KEY", "too-short")

    with pytest.raises(ValidationError):
        _settings()


def test_env_example_lists_every_jwt_setting():  # AC12
    with open(".env.example", encoding="utf-8") as f:
        keys = {line.split("=", 1)[0] for line in f if "=" in line and not line.startswith("#")}

    assert {
        "JWT_SECRET_KEY",
        "JWT_ALGORITHM",
        "JWT_ISSUER",
        "JWT_AUDIENCE",
        "ACCESS_TOKEN_EXPIRE_MINUTES",
    } <= keys


def test_llm_settings_default_to_off_with_documented_limits(no_llm_env):  # interviewer-reaction AC16, EC18
    s = _settings()

    assert s.llm_providers == []
    assert s.llm_provider_configs == []
    assert s.llm_configured is False
    assert (s.llm_timeout_seconds, s.llm_max_retries, s.llm_total_budget_seconds, s.llm_max_tokens) == (15, 2, 30, 800)


def test_listed_provider_with_its_block_is_configured(no_llm_env):  # sse-streaming Step 0
    _google(no_llm_env)

    s = _settings()

    assert s.llm_configured is True
    [config] = s.llm_provider_configs
    assert isinstance(config, ProviderConfig)
    assert (config.name, config.model, config.base_url) == ("google", "gemini-test", GOOGLE["LLM_GOOGLE_BASE_URL"])
    assert config.api_key.get_secret_value() == "google-test-secret"


def test_provider_list_is_trimmed_lowercased_and_ignores_blanks(no_llm_env):  # inferred: hand-edited .env
    _google(no_llm_env)
    no_llm_env.setenv("LLM_PROVIDERS", " Google , ")

    assert _settings().llm_providers == ["google"]


@pytest.mark.parametrize("blank", ["", "  ", " , "])
def test_blank_provider_list_means_llm_off(no_llm_env, blank):  # EC18: .env.example may ship it blank
    no_llm_env.setenv("LLM_PROVIDERS", blank)

    assert _settings().llm_configured is False


def test_a_vendor_block_that_is_not_listed_is_ignored(no_llm_env):  # inferred: the list decides, not the keys
    for name, value in GOOGLE.items():
        no_llm_env.setenv(name, value)

    s = _settings()

    assert s.llm_configured is False
    assert s.llm_provider_configs == []


@pytest.mark.parametrize("missing", list(GOOGLE))
def test_a_listed_provider_needs_its_key_model_and_url(no_llm_env, missing):  # Step 0: names the variable
    _google(no_llm_env)
    no_llm_env.delenv(missing)

    with pytest.raises(ValidationError) as exc:
        _settings()

    assert missing in str(exc.value)


def test_blank_vendor_values_count_as_missing(no_llm_env):  # EC18: blank is unset, never an empty key
    _google(no_llm_env, LLM_GOOGLE_API_KEY="  ")

    with pytest.raises(ValidationError) as exc:
        _settings()

    assert "LLM_GOOGLE_API_KEY" in str(exc.value)


def test_unknown_provider_name_is_refused(no_llm_env):  # Step 0
    _google(no_llm_env)
    no_llm_env.setenv("LLM_PROVIDERS", "google,mystery")

    with pytest.raises(ValidationError) as exc:
        _settings()

    assert "mystery" in str(exc.value)


def test_duplicate_provider_name_is_refused(no_llm_env):  # Step 0
    _google(no_llm_env)
    no_llm_env.setenv("LLM_PROVIDERS", "google,google")

    with pytest.raises(ValidationError) as exc:
        _settings()

    assert "more than once" in str(exc.value)


@pytest.mark.parametrize("old", ["OPENROUTER_API_KEY", "LLM_MODEL", "LLM_BASE_URL"])
def test_removed_llm_settings_refuse_to_start_and_point_to_the_new_ones(no_llm_env, old):  # Step 0: clean break
    no_llm_env.setenv(old, "left-over-value")

    with pytest.raises(ValidationError) as exc:
        _settings()

    message = str(exc.value)
    assert old in message
    assert "LLM_PROVIDERS" in message
    assert "left-over-value" not in message


@pytest.mark.parametrize("old", ["OPENROUTER_API_KEY", "LLM_MODEL", "LLM_BASE_URL"])
def test_blank_removed_settings_are_tolerated(no_llm_env, old):  # inferred: a cleared line in an old .env
    no_llm_env.setenv(old, "")

    assert _settings().llm_configured is False


def test_api_key_never_shows_in_repr_or_errors(no_llm_env):  # AC16, Step 0
    _google(no_llm_env)

    s = _settings()

    assert "google-test-secret" not in repr(s)
    assert "google-test-secret" not in str(s.model_dump())
    assert "google-test-secret" not in repr(s.llm_provider_configs)

    no_llm_env.delenv("LLM_GOOGLE_MODEL")
    with pytest.raises(ValidationError) as exc:
        _settings()
    assert "google-test-secret" not in str(exc.value)


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("LLM_TIMEOUT_SECONDS", "0"),
        ("LLM_MAX_RETRIES", "-1"),
        ("LLM_TOTAL_BUDGET_SECONDS", "0"),
        ("LLM_MAX_TOKENS", "0"),
    ],
)
def test_llm_limits_must_be_positive(
    no_llm_env, name, value
):  # inferred: a zero timeout or budget would disable the LLM
    no_llm_env.setenv(name, value)

    with pytest.raises(ValidationError):
        _settings()


def test_env_example_lists_every_llm_setting():  # AC16, sse-streaming Step 0
    with open(".env.example", encoding="utf-8") as f:
        keys = {line.split("=", 1)[0] for line in f if "=" in line and not line.startswith("#")}

    assert {
        "LLM_PROVIDERS",
        "LLM_GOOGLE_API_KEY",
        "LLM_GOOGLE_MODEL",
        "LLM_GOOGLE_BASE_URL",
        "LLM_TIMEOUT_SECONDS",
        "LLM_MAX_RETRIES",
        "LLM_TOTAL_BUDGET_SECONDS",
        "LLM_MAX_TOKENS",
    } <= keys
    assert not keys & {"OPENROUTER_API_KEY", "LLM_MODEL", "LLM_BASE_URL"}


def test_env_example_explains_the_reasoning_model_token_cap():  # llm-interviewer AC18
    with open(".env.example", encoding="utf-8") as f:
        text = f.read()

    assert "LLM_MAX_TOKENS=800" in text
    assert "reasoning" in text.lower()
