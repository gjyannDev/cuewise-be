from datetime import UTC, datetime, timedelta

import jwt
import pytest
from fastapi import APIRouter

from app.core.config import settings
from app.main import app
from app.modules.auth.auth_constants import Permission, Role
from app.modules.auth.auth_dependencies import (
    CurrentUserDep,
    require_permissions,
    require_roles,
)

guards = APIRouter(prefix="/_test/guards")


@guards.get("/authenticated")
def authenticated(user: CurrentUserDep):
    return {"id": user.id}


@guards.get("/admin-role", dependencies=[require_roles(Role.admin)])
def admin_role():
    return {"ok": True}


@guards.get("/users-read", dependencies=[require_permissions(Permission.users_read)])
def users_read():
    return {"ok": True}


@guards.get(
    "/read-and-read-self",
    dependencies=[require_permissions(Permission.users_read, Permission.users_read_self)],
)
def read_and_read_self():
    return {"ok": True}


app.include_router(guards)

AUTHENTICATED = "/_test/guards/authenticated"


def _token(**overrides):
    now = datetime.now(UTC)
    claims = {
        "sub": "1",
        "role": "user",
        "iat": now,
        "exp": now + timedelta(minutes=5),
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
    } | overrides
    return jwt.encode(claims, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def _assert_401(r, code):
    assert r.status_code == 401
    assert r.headers["www-authenticate"] == "Bearer"
    assert r.json()["error"]["code"] == code


# --- Authentication (get_current_user) ---


def test_missing_header_is_token_missing(client, db):  # EC1
    _assert_401(client.get(AUTHENTICATED), "TOKEN_MISSING")


@pytest.mark.parametrize("header", ["Basic dXNlcjpwYXNz", "Bearer", "Bearer   ", "token-without-scheme"])
def test_non_bearer_or_empty_token_is_token_missing(client, db, header):  # EC2
    _assert_401(client.get(AUTHENTICATED, headers={"Authorization": header}), "TOKEN_MISSING")


def test_expired_token_is_token_expired(client, make_user):  # EC3
    user = make_user()
    past = datetime.now(UTC) - timedelta(hours=2)
    token = _token(sub=str(user.id), iat=past, exp=past + timedelta(minutes=1))

    _assert_401(client.get(AUTHENTICATED, headers={"Authorization": f"Bearer {token}"}), "TOKEN_EXPIRED")


@pytest.mark.parametrize(
    "token",
    [
        "not-a-jwt",
        _token(iss="someone-else"),
        _token(aud="someone-else"),
        jwt.encode({"sub": "1"}, "y" * 64, algorithm="HS256"),
    ],
    ids=["garbage", "wrong-iss", "wrong-aud", "wrong-key"],
)
def test_bad_tokens_are_token_invalid(client, make_user, token):  # EC4, EC5, EC6
    make_user()

    _assert_401(client.get(AUTHENTICATED, headers={"Authorization": f"Bearer {token}"}), "TOKEN_INVALID")


def test_non_integer_subject_is_token_invalid(client, db):  # EC7
    token = _token(sub="not-a-number")

    _assert_401(client.get(AUTHENTICATED, headers={"Authorization": f"Bearer {token}"}), "TOKEN_INVALID")


def test_token_for_deleted_user_is_token_invalid(client, db, make_user, auth_header):  # EC7
    user = make_user()
    headers = auth_header(user)
    db.delete(user)
    db.commit()

    _assert_401(client.get(AUTHENTICATED, headers=headers), "TOKEN_INVALID")


def test_token_for_deactivated_user_is_token_invalid(client, db, make_user, auth_header):  # EC8
    user = make_user()
    headers = auth_header(user)
    user.is_active = False
    db.commit()

    _assert_401(client.get(AUTHENTICATED, headers=headers), "TOKEN_INVALID")


def test_valid_token_resolves_the_user(client, make_user, auth_header):  # AC4 happy path
    user = make_user()

    r = client.get(AUTHENTICATED, headers=auth_header(user))

    assert r.status_code == 200
    assert r.json() == {"id": user.id}


# --- Authorization (require_roles / require_permissions) ---


@pytest.mark.parametrize(
    ("role", "path", "status"),
    [
        (Role.admin, "/_test/guards/admin-role", 200),
        (Role.user, "/_test/guards/admin-role", 403),
        (Role.admin, "/_test/guards/users-read", 200),
        (Role.user, "/_test/guards/users-read", 403),
    ],
)
def test_guards_allow_or_forbid_by_db_role(client, make_user, auth_header, role, path, status):  # AC17, AC18
    user = make_user(role=role)

    r = client.get(path, headers=auth_header(user))

    assert r.status_code == status
    if status == 403:
        assert r.json()["error"]["code"] == "FORBIDDEN"


def test_permissions_guard_requires_all_listed_permissions(client, make_user, auth_header):  # EC20
    user = make_user(role=Role.user)  # holds users:read_self but not users:read

    assert client.get("/_test/guards/read-and-read-self", headers=auth_header(user)).status_code == 403


def test_stale_admin_claim_on_demoted_user_is_ignored(client, db, make_user, auth_header):  # AC8, EC12
    user = make_user(role=Role.admin)
    headers = auth_header(user)
    user.role = Role.user
    db.commit()

    assert client.get("/_test/guards/admin-role", headers=headers).status_code == 403
    assert client.get("/_test/guards/users-read", headers=headers).status_code == 403


def test_promoted_user_gains_access_with_old_token(client, db, make_user, auth_header):  # AC8, EC12
    user = make_user(role=Role.user)
    headers = auth_header(user)
    user.role = Role.admin
    db.commit()

    assert client.get("/_test/guards/admin-role", headers=headers).status_code == 200
    assert client.get("/_test/guards/users-read", headers=headers).status_code == 200


def test_forged_admin_claim_does_not_grant_access(client, make_user, auth_header):  # AC8, inferred: claim trust
    user = make_user(role=Role.user)

    r = client.get("/_test/guards/users-read", headers=auth_header(user, role="admin"))

    assert r.status_code == 403


def test_unmapped_db_role_is_denied_everywhere(client, make_user, auth_header):  # EC21
    user = make_user(role="superuser")

    assert client.get("/_test/guards/users-read", headers=auth_header(user)).status_code == 403
    assert client.get("/_test/guards/admin-role", headers=auth_header(user)).status_code == 403


def test_guarded_requests_never_log_the_token(client, make_user, auth_header, app_logs):  # AC14
    user = make_user()
    headers = auth_header(user)

    client.get("/_test/guards/users-read", headers=headers)
    client.get(AUTHENTICATED, headers={"Authorization": "Bearer not-a-jwt"})

    logged = "\n".join(r.getMessage() for r in app_logs.records)
    assert headers["Authorization"].removeprefix("Bearer ") not in logged
    assert "not-a-jwt" not in logged
