from app.core.config import settings


def error_of(response):
    return response.json()["error"]


# --- AppError ---


def test_app_error_returns_standard_shape(client):  # AC1
    r = client.get("/_test/conflict")

    assert r.status_code == 409
    assert set(error_of(r)) == {"code", "message", "details", "request_id"}
    assert error_of(r)["code"] == "CONFLICT"
    assert error_of(r)["message"] == "Thing already exists"
    assert error_of(r)["details"] == {"field": "name"}


def test_auth_error_sends_bearer_challenge_and_specific_code(client):  # AC2
    r = client.get("/_test/expired")

    assert r.status_code == 401
    assert r.headers["www-authenticate"] == "Bearer"
    assert error_of(r)["code"] == "TOKEN_EXPIRED"


# --- Validation ---


def test_validation_error_lists_each_broken_field(client):  # AC3
    r = client.post("/auth/register", json={"email": "not-an-email", "password": "short"})

    assert r.status_code == 422
    assert error_of(r)["code"] == "VALIDATION_ERROR"
    fields = {d["field"] for d in error_of(r)["details"]}
    assert fields == {"body.email", "body.password"}
    for d in error_of(r)["details"]:
        assert set(d) == {"field", "issue", "type"}


def test_validation_error_never_echoes_submitted_values(client):  # AC4
    r = client.post("/auth/register", json={"email": "not-an-email", "password": "s3cr"})

    assert "s3cr" not in r.text
    assert "not-an-email" not in r.text


def test_malformed_json_returns_readable_validation_error(client):  # EC3
    raw = '{"email": "leak@example.com", "password": '
    r = client.post("/auth/register", content=raw, headers={"Content-Type": "application/json"})

    assert r.status_code == 422
    assert error_of(r)["code"] == "VALIDATION_ERROR"
    assert error_of(r)["details"][0]["field"].startswith("body")
    assert "leak@example.com" not in r.text


# --- Framework HTTP errors ---


def test_unknown_route_and_wrong_method_use_standard_shape(client):  # AC5
    not_found = client.get("/does-not-exist")
    wrong_method = client.delete("/health")

    assert not_found.status_code == 404
    assert error_of(not_found)["code"] == "NOT_FOUND"
    assert wrong_method.status_code == 405
    assert error_of(wrong_method)["code"] == "METHOD_NOT_ALLOWED"


# --- Database ---


def test_integrity_error_returns_generic_conflict(client):  # AC6
    r = client.get("/_test/integrity")

    assert r.status_code == 409
    assert error_of(r)["code"] == "CONFLICT"
    assert "ix_users_email" not in r.text
    assert "duplicate key" not in r.text


def test_database_unreachable_returns_503(client):  # AC19
    r = client.get("/_test/db-down")

    assert r.status_code == 503
    assert error_of(r)["code"] == "DATABASE_UNAVAILABLE"
    assert "secret-host" not in r.text


# --- Unhandled exceptions ---


def test_crash_returns_generic_500_without_details(client, monkeypatch):  # AC7
    monkeypatch.setattr(settings, "debug", False)
    r = client.get("/_test/crash")

    assert r.status_code == 500
    assert error_of(r)["code"] == "INTERNAL_ERROR"
    assert error_of(r)["details"] is None
    assert "kaboom" not in r.text


def test_crash_details_shown_only_in_debug(client, monkeypatch):  # AC8
    monkeypatch.setattr(settings, "debug", True)
    r = client.get("/_test/crash")

    assert r.status_code == 500
    assert error_of(r)["details"] == {"type": "RuntimeError", "message": "kaboom internal detail"}


# --- Log content ---


def test_app_error_log_names_where_it_was_raised(client, app_logs):  # AC17
    client.get("/_test/conflict")

    line = next(rec.getMessage() for rec in app_logs.records if rec.name == "app.errors")
    assert "conftest.py:" in line
    assert "raise_conflict" in line
