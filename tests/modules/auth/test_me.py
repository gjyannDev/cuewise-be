import pytest

from app.main import app
from app.modules.auth.auth_constants import Role

ME = "/api/v1/auth/me"
INTERVIEW_PERMISSIONS = {"interviews:create", "interviews:read_self", "interviews:answer"}


@pytest.mark.parametrize(
    ("role", "permissions"),
    [
        (Role.admin, {"users:read", "users:read_self"} | INTERVIEW_PERMISSIONS),
        (Role.user, {"users:read_self"} | INTERVIEW_PERMISSIONS),
    ],
)
def test_me_returns_profile_with_resolved_permissions(client, make_user, auth_header, role, permissions):  # AC5, AC17
    user = make_user(email="ana@example.com", role=role)

    r = client.get(ME, headers=auth_header(user))

    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"id", "email", "role", "permissions"}
    assert body["id"] == str(user.id)
    assert body["email"] == "ana@example.com"
    assert body["role"] == role
    assert set(body["permissions"]) == permissions
    assert "argon2" not in r.text


def test_me_without_token_is_401(client, db):  # AC4 on a real route
    r = client.get(ME)

    assert r.status_code == 401
    assert r.json()["error"]["code"] == "TOKEN_MISSING"


def test_me_for_unmapped_role_is_403(client, make_user, auth_header):  # EC21 on a real route
    user = make_user(role="superuser")

    assert client.get(ME, headers=auth_header(user)).status_code == 403


def test_unversioned_auth_paths_are_gone_and_health_stays(client, db):  # AC10
    assert client.post("/auth/register", json={"email": "a@example.com", "password": "password123"}).status_code == 404
    assert client.post("/auth/login", json={"email": "a@example.com", "password": "password123"}).status_code == 404
    assert client.get("/health").status_code == 200


@pytest.mark.parametrize(
    ("path", "method", "statuses"),
    [
        ("/api/v1/auth/login", "post", {"401", "422", "500"}),
        ("/api/v1/auth/me", "get", {"401", "403", "500"}),
    ],
)
def test_auth_routes_document_error_responses(path, method, statuses):  # AC13
    responses = app.openapi()["paths"][path][method]["responses"]

    for status in statuses:
        assert responses[status]["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorResponse")
