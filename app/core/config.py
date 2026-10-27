from pydantic import Field
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

    model_config = SettingsConfigDict(env_file=".env")


# Values come from env vars / .env at runtime, which Pyright can't see.
settings = Settings()  # pyright: ignore[reportCallIssue]
