import os

import pytest
from pydantic import ValidationError

from app.core.config import ProviderConfig, Settings
from app.modules.interviews.constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE

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


@pytest.fixture
def no_langfuse_env(monkeypatch):
    for name in list(os.environ):
        if name.upper().startswith(("LANGFUSE_", "APP_ENV")):
            monkeypatch.delenv(name, raising=False)
    return monkeypatch


def test_langfuse_off_and_env_defaults_when_unset(no_langfuse_env):  # AC8, EC1
    settings = _settings()

    assert settings.langfuse_enabled is False
    assert settings.app_env == "development"


def test_langfuse_blank_keys_count_as_unset(no_langfuse_env):  # AC8, EC1
    for name in ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_BASE_URL"):
        no_langfuse_env.setenv(name, "")

    assert _settings().langfuse_enabled is False


def test_langfuse_on_only_with_both_keys(no_langfuse_env):  # AC8, EC2
    no_langfuse_env.setenv("LANGFUSE_PUBLIC_KEY", "pk-test")
    assert _settings().langfuse_enabled is False

    no_langfuse_env.setenv("LANGFUSE_SECRET_KEY", "sk-test")
    assert _settings().langfuse_enabled is True


def test_langfuse_secret_key_is_not_echoed(no_langfuse_env):  # AC14
    no_langfuse_env.setenv("LANGFUSE_SECRET_KEY", "sk-very-secret")

    assert "sk-very-secret" not in repr(_settings())


def test_env_example_lists_langfuse_and_app_env():  # AC14
    with open(".env.example", encoding="utf-8") as f:
        text = f.read()

    for name in ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_BASE_URL", "APP_ENV"):
        assert name in text


@pytest.fixture
def no_stt_env(monkeypatch):
    """Settings without a developer's real Deepgram key or transcription limits."""
    for name in list(os.environ):
        if name.upper().startswith(("DEEPGRAM_", "TRANSCRIPTION_")):
            monkeypatch.delenv(name, raising=False)
    return monkeypatch


def test_transcription_is_off_without_a_key_with_documented_defaults(no_stt_env):  # voice AC6, EC22
    s = _settings()

    assert s.deepgram_api_key is None
    assert s.transcription_configured is False
    assert (s.deepgram_model, s.deepgram_base_url) == ("nova-3", "https://api.deepgram.com/")
    assert (s.transcription_timeout_seconds, s.transcription_max_retries, s.transcription_total_budget_seconds) == (
        15,
        1,
        20,
    )


def test_a_blank_deepgram_key_counts_as_unset(no_stt_env):  # EC22: .env.example ships it blank
    no_stt_env.setenv("DEEPGRAM_API_KEY", "  ")

    assert _settings().transcription_configured is False


def test_a_deepgram_key_turns_transcription_on_and_never_shows(no_stt_env):  # voice AC8, AC9
    no_stt_env.setenv("DEEPGRAM_API_KEY", "dg-very-secret")

    s = _settings()

    assert s.transcription_configured is True
    assert "dg-very-secret" not in repr(s)
    no_stt_env.setenv("TRANSCRIPTION_TIMEOUT_SECONDS", "0")
    with pytest.raises(ValidationError) as exc:
        _settings()
    assert "dg-very-secret" not in str(exc.value)


@pytest.mark.parametrize(
    ("name", "value"),
    [
        ("TRANSCRIPTION_TIMEOUT_SECONDS", "0"),
        ("TRANSCRIPTION_MAX_RETRIES", "-1"),
        ("TRANSCRIPTION_TOTAL_BUDGET_SECONDS", "0"),
    ],
)
def test_transcription_limits_must_be_positive(no_stt_env, name, value):  # inferred: a zero budget disables voice
    no_stt_env.setenv(name, value)

    with pytest.raises(ValidationError):
        _settings()


def test_env_example_lists_every_transcription_setting():  # voice AC8
    with open(".env.example", encoding="utf-8") as f:
        keys = {line.split("=", 1)[0] for line in f if "=" in line and not line.startswith("#")}

    assert {
        "DEEPGRAM_API_KEY",
        "DEEPGRAM_MODEL",
        "DEEPGRAM_BASE_URL",
        "TRANSCRIPTION_TIMEOUT_SECONDS",
        "TRANSCRIPTION_MAX_RETRIES",
        "TRANSCRIPTION_TOTAL_BUDGET_SECONDS",
    } <= keys


@pytest.fixture
def no_embedding_env(no_llm_env):
    for name in list(os.environ):
        if name.upper().startswith("EMBEDDING_"):
            no_llm_env.delenv(name, raising=False)
    return no_llm_env


def test_embedding_defaults_and_off_without_the_google_key(no_embedding_env):  # knowledge-base-rag AC27
    s = _settings()

    assert s.embedding_configured is False
    assert (s.embedding_model, s.embedding_dimensions, s.embedding_base_url, s.embedding_timeout_seconds) == (
        "gemini-embedding-001",
        768,
        "https://generativelanguage.googleapis.com/v1beta/",
        10,
    )


def test_embedding_dimensions_match_the_vector_column():  # AC27, EC14: a mismatch needs a migration
    assert Settings.model_fields["embedding_dimensions"].default == KNOWLEDGE_VECTOR_SIZE


def test_embeddings_use_the_google_key_and_a_blank_one_is_unset(no_embedding_env):  # AC27: no second secret
    no_embedding_env.setenv("LLM_GOOGLE_API_KEY", "  ")
    assert _settings().embedding_configured is False

    no_embedding_env.setenv("LLM_GOOGLE_API_KEY", "google-test-secret")
    assert _settings().embedding_configured is True


@pytest.mark.parametrize(("name", "value"), [("EMBEDDING_DIMENSIONS", "0"), ("EMBEDDING_TIMEOUT_SECONDS", "0")])
def test_embedding_limits_must_be_positive(no_embedding_env, name, value):  # inferred: a zero size or timeout
    no_embedding_env.setenv(name, value)

    with pytest.raises(ValidationError):
        _settings()


def test_env_example_lists_every_embedding_setting():  # AC27
    with open(".env.example", encoding="utf-8") as f:
        keys = {line.split("=", 1)[0] for line in f if "=" in line and not line.startswith("#")}

    assert {"EMBEDDING_MODEL", "EMBEDDING_DIMENSIONS", "EMBEDDING_BASE_URL", "EMBEDDING_TIMEOUT_SECONDS"} <= keys
    assert "EMBEDDING_API_KEY" not in keys

