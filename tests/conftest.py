import logging
import os

# Tests must not depend on a developer's .env; engine creation doesn't connect.
os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://test:test@localhost:5432/test")
os.environ.setdefault("JWT_SECRET_KEY", "test-secret-key-" + "x" * 64)

import pytest
from fastapi import APIRouter
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.errors import ConflictError, TokenExpiredError
from app.core.logging import RequestIdFilter
from app.core.security import hash_password
from app.core.tokens import create_token
from app.db import models  # noqa: F401  (registers every model on Base.metadata)
from app.db.session import Base, get_db
from app.main import app
from app.modules.auth.auth_constants import Role
from app.modules.auth.auth_model import User

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


@pytest.fixture
def client():
    return TestClient(app, raise_server_exceptions=False)


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


@pytest.fixture
def app_logs(caplog):
    """Capture records from the non-propagating 'app' logger, with request_id like production handlers."""
    logger = logging.getLogger("app")
    request_id_filter = RequestIdFilter()
    caplog.handler.addFilter(request_id_filter)
    logger.addHandler(caplog.handler)
    caplog.set_level(logging.DEBUG, logger="app")
    yield caplog
    logger.removeHandler(caplog.handler)
    caplog.handler.removeFilter(request_id_filter)
