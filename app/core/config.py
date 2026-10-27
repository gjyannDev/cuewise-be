from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")


# Values come from env vars / .env at runtime, which Pyright can't see.
settings = Settings()  # pyright: ignore[reportCallIssue]
