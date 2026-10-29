from typing import Self

from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    debug: bool = False

    # No default: the app must not start with a guessable signing key.
    jwt_secret_key: str = Field(min_length=32)
    jwt_algorithm: str = "HS256"
    jwt_issuer: str = "cuewise-api"
    jwt_audience: str = "cuewise-client"
    access_token_expire_minutes: int = Field(default=60, gt=0)

    # LLM (OpenRouter, OpenAI-compatible chat completions). Key and model unset = LLM off, reactions are null.
    openrouter_api_key: SecretStr | None = None
    llm_model: str | None = None
    llm_base_url: str = "https://openrouter.ai/api/v1"
    llm_timeout_seconds: float = Field(default=15, gt=0)
    llm_max_retries: int = Field(default=2, ge=0)
    llm_total_budget_seconds: float = Field(default=30, gt=0)
    llm_max_tokens: int = Field(default=150, gt=0)

    model_config = SettingsConfigDict(env_file=".env")

    @field_validator("openrouter_api_key", "llm_model", mode="before")
    @classmethod
    def _blank_is_unset(cls, value: object) -> object:
        # .env.example ships these blank; an empty value means "not configured", not "empty key".
        return None if isinstance(value, str) and not value.strip() else value

    @model_validator(mode="after")
    def _key_and_model_together(self) -> Self:
        # Half a config would silently run with every reaction null; fail at startup instead.
        if (self.openrouter_api_key is None) != (self.llm_model is None):
            raise ValueError("Set OPENROUTER_API_KEY and LLM_MODEL together, or leave both unset")
        return self

    @property
    def llm_configured(self) -> bool:
        return self.openrouter_api_key is not None and self.llm_model is not None


# Values come from env vars / .env at runtime, which Pyright can't see.
settings = Settings()  # pyright: ignore[reportCallIssue]
