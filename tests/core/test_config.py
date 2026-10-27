import pytest
from pydantic import ValidationError

from app.core.config import Settings


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
