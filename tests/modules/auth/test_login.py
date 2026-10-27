from app.core.config import settings
from app.core.tokens import decode_token
from app.modules.auth.auth_constants import Role

LOGIN = "/api/v1/auth/login"
REGISTER = "/api/v1/auth/register"


def test_valid_login_returns_bearer_token_for_the_user(client, make_user):  # AC2
    user = make_user(email="ana@example.com", role=Role.admin)

    r = client.post(LOGIN, json={"email": "ana@example.com", "password": "password123"})

    assert r.status_code == 200
    body = r.json()
    assert body["token_type"] == "bearer"
    claims = decode_token(body["access_token"])
    assert claims["sub"] == str(user.id)
    assert claims["role"] == "admin"
    assert claims["exp"] - claims["iat"] == settings.access_token_expire_minutes * 60


def _login_error(client, email, password):
    r = client.post(LOGIN, json={"email": email, "password": password})
    assert r.status_code == 401
    assert r.headers["www-authenticate"] == "Bearer"
    error = r.json()["error"]
    error.pop("request_id")
    return error


def test_unknown_email_wrong_password_and_inactive_user_fail_identically(client, make_user):  # AC3, EC9, EC10
    make_user(email="active@example.com")
    make_user(email="inactive@example.com", is_active=False)

    unknown = _login_error(client, "nobody@example.com", "password123")
    wrong_password = _login_error(client, "active@example.com", "wrong-password")
    inactive = _login_error(client, "inactive@example.com", "password123")

    assert unknown["code"] == "INVALID_CREDENTIALS"
    assert unknown == wrong_password == inactive


def test_unknown_email_still_runs_a_password_check(client, db, monkeypatch):  # AC3, timing parity
    calls = []
    from app.modules.auth import auth_controller as controller

    real_verify = controller.verify_password
    monkeypatch.setattr(controller, "verify_password", lambda *a: calls.append(1) or real_verify(*a))

    client.post(LOGIN, json={"email": "nobody@example.com", "password": "password123"})

    assert calls == [1]


def test_login_with_malformed_email_or_missing_fields_is_422(client, db):  # EC16
    bad_email = client.post(LOGIN, json={"email": "nope", "password": "password123"})
    missing = client.post(LOGIN, json={"email": "a@example.com"})

    assert bad_email.status_code == missing.status_code == 422
    assert bad_email.json()["error"]["code"] == "VALIDATION_ERROR"


def test_register_rejects_a_role_field(client, db):  # AC9, EC13
    r = client.post(REGISTER, json={"email": "x@example.com", "password": "password123", "role": "admin"})

    assert r.status_code == 422
    assert {d["field"] for d in r.json()["error"]["details"]} == {"body.role"}


def test_registered_user_is_a_plain_active_user(client, db):  # AC9
    r = client.post(REGISTER, json={"email": "new@example.com", "password": "password123"})
    login = client.post(LOGIN, json={"email": "new@example.com", "password": "password123"})

    assert r.status_code == 201
    assert decode_token(login.json()["access_token"])["role"] == "user"


def test_login_never_logs_password_or_token(client, make_user, app_logs):  # AC14
    make_user(email="ana@example.com", password="s3cret-pass-123")

    ok = client.post(LOGIN, json={"email": "ana@example.com", "password": "s3cret-pass-123"})
    client.post(LOGIN, json={"email": "ana@example.com", "password": "wrong-pass-456"})

    logged = "\n".join(r.getMessage() for r in app_logs.records)
    assert "s3cret-pass-123" not in logged
    assert "wrong-pass-456" not in logged
    assert ok.json()["access_token"] not in logged
    assert "$argon2" not in logged
