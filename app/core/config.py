from typing import Annotated, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    field_validator,
    model_validator,
)
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict

# Vendors the app knows, each with an `LLM_<NAME>_API_KEY / _MODEL / _BASE_URL` block below. All speak OpenAI-compatible
# chat completions. Adding one = its name here plus its three fields.
LLM_VENDORS = ("google",)
_VENDOR_FIELDS = ("api_key", "model", "base_url")
# Replaced by LLM_PROVIDERS + the vendor blocks; still read only so a stale .env fails loudly instead of running
# without the LLM.
_REMOVED_LLM_SETTINGS = ("OPENROUTER_API_KEY", "LLM_MODEL", "LLM_BASE_URL")


class ProviderConfig(BaseModel):
    """One listed provider, resolved from its vendor block."""

    model_config = ConfigDict(frozen=True)

    name: str
    api_key: SecretStr
    model: str
    base_url: str


class Settings(BaseSettings):
    database_url: str
    debug: bool = False
    # Labels every Langfuse trace (development / production ...), so environments stay apart in one project.
    app_env: str = "development"

    # No default: the app must not start with a guessable signing key.
    jwt_secret_key: str = Field(min_length=32)
    jwt_algorithm: str = "HS256"
    jwt_issuer: str = "cuewise-api"
    jwt_audience: str = "cuewise-client"
    access_token_expire_minutes: int = Field(default=60, gt=0)

    # LLM providers in order, primary first (later ones become the fallback chain). Empty = LLM off: bank only.
    llm_providers: Annotated[list[str], NoDecode] = Field(default_factory=list)
    llm_google_api_key: SecretStr | None = None
    llm_google_model: str | None = None
    llm_google_base_url: str | None = None
    llm_timeout_seconds: float = Field(default=15, gt=0)
    llm_max_retries: int = Field(default=2, ge=0)
    llm_total_budget_seconds: float = Field(default=30, gt=0)
    llm_max_tokens: int = Field(default=4000, gt=0)

    # Speech-to-text for voice answers (Deepgram). No key = voice answers off; everything else still works.
    deepgram_api_key: SecretStr | None = None
    deepgram_model: str = "nova-3"
    deepgram_base_url: str = "https://api.deepgram.com/"
    transcription_timeout_seconds: float = Field(default=15, gt=0)
    transcription_max_retries: int = Field(default=1, ge=0)
    # Kept under the web app's 25 s forwarder timeout, so a slow transcription fails here with a clean 503.
    transcription_total_budget_seconds: float = Field(default=20, gt=0)

    # Langfuse tracing: both keys set = on, anything less = off (see `langfuse_enabled`).
    langfuse_public_key: SecretStr | None = None
    langfuse_secret_key: SecretStr | None = None
    langfuse_base_url: str | None = None

    removed_openrouter_api_key: SecretStr | None = Field(default=None, validation_alias="OPENROUTER_API_KEY")
    removed_llm_model: str | None = Field(default=None, validation_alias="LLM_MODEL")
    removed_llm_base_url: str | None = Field(default=None, validation_alias="LLM_BASE_URL")

    # Validation errors would otherwise echo every input value, API keys included.
    model_config = SettingsConfigDict(env_file=".env", hide_input_in_errors=True)

    @field_validator("llm_providers", mode="before")
    @classmethod
    def _split_providers(cls, value: object) -> object:
        if isinstance(value, str):
            return [name.strip().lower() for name in value.split(",") if name.strip()]
        return value

    @field_validator(
        "llm_google_api_key",
        "llm_google_model",
        "llm_google_base_url",
        "deepgram_api_key",
        "langfuse_public_key",
        "langfuse_secret_key",
        "langfuse_base_url",
        "removed_openrouter_api_key",
        "removed_llm_model",
        "removed_llm_base_url",
        mode="before",
    )
    @classmethod
    def _blank_is_unset(cls, value: object) -> object:
        # .env.example ships these blank; an empty value means "not configured", not "empty key".
        return None if isinstance(value, str) and not value.strip() else value

    @model_validator(mode="after")
    def _providers_are_complete(self) -> Self:
        removed = [
            name
            for name, value in zip(
                _REMOVED_LLM_SETTINGS,
                (self.removed_openrouter_api_key, self.removed_llm_model, self.removed_llm_base_url),
                strict=True,
            )
            if value is not None
        ]
        if removed:
            raise ValueError(
                f"{', '.join(removed)} no longer exist: set LLM_PROVIDERS (e.g. google) and that vendor's "
                "LLM_<VENDOR>_API_KEY, LLM_<VENDOR>_MODEL and LLM_<VENDOR>_BASE_URL instead"
            )
        unknown = [name for name in self.llm_providers if name not in LLM_VENDORS]
        if unknown:
            raise ValueError(f"LLM_PROVIDERS has unknown names {unknown}; known: {', '.join(LLM_VENDORS)}")
        if len(set(self.llm_providers)) != len(self.llm_providers):
            raise ValueError("LLM_PROVIDERS lists a provider more than once")
        missing = [
            f"LLM_{name.upper()}_{field.upper()}"
            for name in self.llm_providers
            for field in _VENDOR_FIELDS
            if getattr(self, f"llm_{name}_{field}") is None
        ]
        if missing:
            # Half a config would silently run on bank questions only; fail at startup instead.
            raise ValueError(f"LLM_PROVIDERS lists a provider whose settings are missing: {', '.join(missing)}")
        return self

    @property
    def llm_provider_configs(self) -> list[ProviderConfig]:
        return [
            ProviderConfig(name=name, **{field: getattr(self, f"llm_{name}_{field}") for field in _VENDOR_FIELDS})
            for name in self.llm_providers
        ]

    @property
    def langfuse_enabled(self) -> bool:
        return self.langfuse_public_key is not None and self.langfuse_secret_key is not None

    @property
    def llm_configured(self) -> bool:
        return bool(self.llm_providers)

    @property
    def transcription_configured(self) -> bool:
        return self.deepgram_api_key is not None


# Values come from env vars / .env at runtime, which Pyright can't see.
settings = Settings()  # pyright: ignore[reportCallIssue]
