from unittest.mock import create_autospec

import pytest

from app.main import app
from app.modules.auth.controller import AuthController
from app.modules.auth.repository import AuthRepository
from app.modules.auth.route import get_controller


@pytest.fixture
def existing_email():
    repo = create_autospec(AuthRepository, instance=True)
    repo.get_by_email.return_value = object()
    app.dependency_overrides[get_controller] = lambda: AuthController(repo)
    yield
    app.dependency_overrides.pop(get_controller)


@pytest.mark.usefixtures("existing_email")
def test_duplicate_email_returns_conflict_on_email_field(client):  # AC14
    r = client.post("/auth/register", json={"email": "taken@example.com", "password": "password123"})

    assert r.status_code == 409
    assert r.json()["error"]["code"] == "CONFLICT"
    assert r.json()["error"]["details"] == {"field": "email"}


def test_register_documents_error_responses():  # AC15
    responses = app.openapi()["paths"]["/auth/register"]["post"]["responses"]

    for status in ("409", "422", "500"):
        schema_ref = responses[status]["content"]["application/json"]["schema"]["$ref"]
        assert schema_ref.endswith("/ErrorResponse")
