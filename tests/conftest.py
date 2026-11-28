import io
import json
import logging
import os
import tempfile
from pathlib import Path

# Tests must not depend on a developer's .env; engine creation doesn't connect.
os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://test:test@localhost:5432/test")
os.environ.setdefault("JWT_SECRET_KEY", "test-secret-key-" + "x" * 64)
# Nor on their real LLM config (from the shell or .env): an env var beats .env, so these set a dummy Google provider
# (the app refuses to start without one; no call is made with it: tests use the fake chat model). Live tests
# (LLM_LIVE_TEST=1) keep the configured provider list.
for _name in ("OPENROUTER_API_KEY", "LLM_MODEL", "LLM_BASE_URL"):
    os.environ[_name] = ""
if os.getenv("LLM_LIVE_TEST") != "1":
    os.environ["LLM_PROVIDERS"] = "google"
    os.environ["LLM_GOOGLE_API_KEY"] = "test-key-not-real"
    os.environ["LLM_GOOGLE_MODEL"] = "gemini-test"
    os.environ["LLM_GOOGLE_THINKING_BUDGET"] = ""
# Same for speech (to text and to speech): tests never call the real Deepgram API, except the opt-in live speech tests
# (SPEECH_LIVE_TEST=1), which keep the configured key.
if os.getenv("SPEECH_LIVE_TEST") != "1":
    os.environ["DEEPGRAM_API_KEY"] = ""

import pytest
import structlog
from fastapi import APIRouter
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.ai.chat_fake import FakeChatModel
from app.core.ai.dependencies import get_chat_model
from app.core.config import settings
from app.core.errors import ConflictError, TokenExpiredError
from app.core.logging import RECORD_KEYS, setup_logging
from app.core.security import hash_password
from app.core.tokens import create_token
from app.db import models  # noqa: F401  (registers every model on Base.metadata)
from app.db.session import Base, get_db
from app.main import app
from app.modules.auth.constants.auth_constants import Role
from app.modules.auth.models.auth_model import User

test_router = APIRouter(prefix="/_test")


@test_router.get("/conflict")
def raise_conflict():
    raise ConflictError("Thing already exists", {"field": "name"})


@test_router.get("/expired")
def raise_expired():
    raise TokenExpiredError("Access token has expired")


@test_router.get("/integrity")
def raise_integrity():
    raise IntegrityError("INSERT ...", {}, Exception('duplicate key value violates unique constraint "ix_users_email"'))


@test_router.get("/db-down")
def raise_db_down():
    raise OperationalError("SELECT 1", {}, Exception("connection refused: secret-host:5432"))


@test_router.get("/crash")
def raise_crash():
    raise RuntimeError("kaboom internal detail")


app.include_router(test_router)

# Tests never write the developer's real logs/app.log: a busy suite would rotate it and delete old log files.
TEST_LOG_FILE = Path(tempfile.mkdtemp(prefix="cuewise-test-logs-")) / "app.log"
setup_logging(settings.debug, log_file=TEST_LOG_FILE)


@pytest.fixture
def client():
    return TestClient(app, raise_server_exceptions=False)


@pytest.fixture(autouse=True)
def default_chat_model():
    """The app has no LLM-off mode: every request gets a chat model. Tests that script the LLM override this."""
    app.dependency_overrides[get_chat_model] = lambda: FakeChatModel()
    yield
    app.dependency_overrides.pop(get_chat_model, None)


@pytest.fixture
def db():
    """Fresh in-memory SQLite DB per test, wired into the app's get_db dependency."""
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    with Session(engine) as session:

        def override_get_db():
            yield session

        app.dependency_overrides[get_db] = override_get_db
        yield session
        app.dependency_overrides.pop(get_db, None)
    engine.dispose()


@pytest.fixture
def make_user(db):
    """Insert a user straight into the test DB; password defaults to 'password123'."""

    def _make(email="user@example.com", password="password123", role=Role.user, is_active=True):
        user = User(email=email, password_hash=hash_password(password), role=role, is_active=is_active)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    return _make


@pytest.fixture
def auth_header():
    """Bearer header for a user; pass role to mint a token whose role claim differs from the DB."""

    def _header(user, role=None):
        return {"Authorization": f"Bearer {create_token(user.id, role or user.role)}"}

    return _header


class LogCapture:
    """What the real logging pipeline wrote during a test: the file's JSON lines and the console text."""

    def __init__(self, path: Path, console: io.StringIO):
        self.path = path
        self._console = console

    def lines(self) -> list[dict]:
        if not self.path.exists():
            return []
        return [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines()]

    def events(self, event: str) -> list[dict]:
        return [line for line in self.lines() if line["event"] == event]

    def console(self) -> str:
        return self._console.getvalue()


@pytest.fixture
def capture_logs(tmp_path):
    """Start the real logging pipeline into a temp file and an in-memory console: `capture_logs(debug=True)`."""

    def _start(debug: bool = False, log_file: Path | None = None) -> LogCapture:
        console = io.StringIO()
        path = log_file or tmp_path / "logs" / "app.log"
        setup_logging(debug, log_file=path, stream=console)
        return LogCapture(path, console)

    yield _start
    structlog.contextvars.clear_contextvars()
    setup_logging(settings.debug, log_file=TEST_LOG_FILE)


@pytest.fixture
def log_lines(capture_logs) -> LogCapture:
    return capture_logs()


def _shown(value: object) -> str:
    if value is None:
        return "-"
    return str(value).lower() if isinstance(value, bool) else str(value)


class LoggedLine:
    """One JSON line of the log file, read the way older tests read a log record: `name`, `levelno`, `request_id`,
    `fields`, and `getMessage()` as `event key=value ...` (null shown as `-`)."""

    def __init__(self, line: dict):
        self.line = line
        self.name: str = line["logger"]
        self.levelno: int = logging.getLevelNamesMapping()[line["level"].upper()]
        self.levelname: str = line["level"].upper()
        self.request_id: str = line["request_id"]
        # The formatted traceback, when the line logged an exception.
        self.exc_info: str | None = line.get("exception")
        self.fields = {key: value for key, value in line.items() if key not in (*RECORD_KEYS, "exception")}

    def getMessage(self) -> str:
        return " ".join([str(self.line["event"]), *(f"{key}={_shown(value)}" for key, value in self.fields.items())])


class AppLogs:
    def __init__(self, capture: LogCapture):
        self._capture = capture

    @property
    def records(self) -> list[LoggedLine]:
        return [LoggedLine(line) for line in self._capture.lines()]

    @property
    def text(self) -> str:
        return self._capture.path.read_text(encoding="utf-8") if self._capture.path.exists() else ""

    def json_lines(self) -> list[str]:
        return self.text.splitlines()


@pytest.fixture
def app_logs(capture_logs) -> AppLogs:
    """Every line the real pipeline wrote (after redaction), at DEBUG for the app's loggers."""
    return AppLogs(capture_logs(debug=True))
