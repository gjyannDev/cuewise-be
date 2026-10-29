import pytest
from pydantic import ValidationError

from app.core.config import Settings

LLM_ENV = ("OPENROUTER_API_KEY", "LLM_MODEL")


@pytest.fixture
def no_llm_env(monkeypatch):
    """Settings built from a clean environment, so a developer's real key never leaks into these tests."""
    for name in LLM_ENV:
        monkeypatch.delenv(name, raising=False)
    return monkeypatch


def test_settings_refuse_missing_jwt_secret(monkeypatch):  # AC12, EC18
    monkeypatch.delenv("JWT_SECRET_KEY", raising=False)

    with pytest.raises(ValidationError) as exc:
        Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    assert "jwt_secret_key" in str(exc.value)


def test_settings_refuse_short_jwt_secret(monkeypatch):  # AC12, inferred: weak key
    monkeypatch.setenv("JWT_SECRET_KEY", "too-short")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)  # pyright: ignore[reportCallIssue]


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
    s = Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    assert s.openrouter_api_key is None
    assert s.llm_model is None
    assert s.llm_configured is False
    assert s.llm_base_url.startswith("https://")
    assert (s.llm_timeout_seconds, s.llm_max_retries, s.llm_total_budget_seconds, s.llm_max_tokens) == (15, 2, 30, 150)


def test_llm_settings_with_key_and_model_are_configured(no_llm_env):  # AC16
    no_llm_env.setenv("OPENROUTER_API_KEY", "sk-or-test-secret")
    no_llm_env.setenv("LLM_MODEL", "some/model")

    s = Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    assert s.llm_configured is True
    assert s.openrouter_api_key is not None
    assert s.openrouter_api_key.get_secret_value() == "sk-or-test-secret"
    assert s.llm_model == "some/model"


@pytest.mark.parametrize("only", LLM_ENV)
def test_llm_settings_refuse_key_without_model_and_model_without_key(no_llm_env, only):  # EC19
    no_llm_env.setenv(only, "something")

    with pytest.raises(ValidationError) as exc:
        Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    assert "OPENROUTER_API_KEY and LLM_MODEL" in str(exc.value)


def test_blank_llm_settings_count_as_unset(no_llm_env):  # EC18, inferred: .env.example ships them blank
    no_llm_env.setenv("OPENROUTER_API_KEY", "")
    no_llm_env.setenv("LLM_MODEL", "  ")

    s = Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    assert s.llm_configured is False


def test_api_key_never_shows_in_repr(no_llm_env):  # AC16
    no_llm_env.setenv("OPENROUTER_API_KEY", "sk-or-very-secret")
    no_llm_env.setenv("LLM_MODEL", "some/model")

    s = Settings(_env_file=None)  # pyright: ignore[reportCallIssue]

    assert "sk-or-very-secret" not in repr(s)
    assert "sk-or-very-secret" not in str(s.model_dump())


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
        Settings(_env_file=None)  # pyright: ignore[reportCallIssue]


def test_env_example_lists_every_llm_setting():  # AC16
    with open(".env.example", encoding="utf-8") as f:
        keys = {line.split("=", 1)[0] for line in f if "=" in line and not line.startswith("#")}

    assert {
        "OPENROUTER_API_KEY",
        "LLM_MODEL",
        "LLM_BASE_URL",
        "LLM_TIMEOUT_SECONDS",
        "LLM_MAX_RETRIES",
        "LLM_TOTAL_BUDGET_SECONDS",
        "LLM_MAX_TOKENS",
    } <= keys
