import logging
import os

# Tests must not depend on a developer's .env; engine creation doesn't connect.
os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://test:test@localhost:5432/test")

import pytest
from fastapi import APIRouter
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError, OperationalError

from app.core.errors import ConflictError, TokenExpiredError
from app.core.logging import RequestIdFilter
from app.main import app

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
