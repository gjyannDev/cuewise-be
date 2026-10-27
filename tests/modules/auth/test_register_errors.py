from unittest.mock import create_autospec

import pytest

from app.main import app
from app.modules.auth.auth_controller import AuthController
from app.modules.auth.auth_dependencies import get_controller
from app.modules.auth.auth_repository import AuthRepository


@pytest.fixture
def existing_email():
    repo = create_autospec(AuthRepository, instance=True)
    repo.get_by_email.return_value = object()
    app.dependency_overrides[get_controller] = lambda: AuthController(repo)
    yield
    app.dependency_overrides.pop(get_controller)


@pytest.mark.usefixtures("existing_email")
def test_duplicate_email_returns_conflict_on_email_field(client):  # AC14
    r = client.post("/api/v1/auth/register", json={"email": "taken@example.com", "password": "password123"})

    assert r.status_code == 409
    assert r.json()["error"]["code"] == "CONFLICT"
    assert r.json()["error"]["details"] == {"field": "email"}


def test_register_documents_error_responses():  # AC15
    responses = app.openapi()["paths"]["/api/v1/auth/register"]["post"]["responses"]

    for status in ("409", "422", "500"):
        schema_ref = responses[status]["content"]["application/json"]["schema"]["$ref"]
        assert schema_ref.endswith("/ErrorResponse")
