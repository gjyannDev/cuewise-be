import pytest

from app.main import app
from app.modules.auth.auth_constants import Role

USERS = "/api/v1/users"


@pytest.fixture
def admin(make_user):
    return make_user(email="admin@example.com", role=Role.admin)


def test_admin_gets_paginated_envelope(client, admin, auth_header):  # AC6
    r = client.get(USERS, headers=auth_header(admin))

    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"items", "total", "limit", "offset"}
    assert body["items"] == [{"id": str(admin.id), "email": "admin@example.com", "role": "admin", "is_active": True}]
    assert "argon2" not in r.text


def test_plain_user_is_forbidden(client, make_user, auth_header):  # AC6, EC11
    user = make_user(role=Role.user)

    r = client.get(USERS, headers=auth_header(user))

    assert r.status_code == 403
    assert r.json()["error"]["code"] == "FORBIDDEN"


def test_anonymous_request_is_401(client, db):  # AC4 on a real route
    assert client.get(USERS).status_code == 401


def test_defaults_order_by_id_and_report_total(client, admin, make_user, auth_header):  # AC7
    for i in range(24):
        make_user(email=f"u{i:02}@example.com")

    body = client.get(USERS, headers=auth_header(admin)).json()

    assert body["limit"] == 20
    assert body["offset"] == 0
    assert body["total"] == 25
    ids = [item["id"] for item in body["items"]]
    assert len(ids) == 20
    assert ids == sorted(ids)
    assert ids[0] == str(admin.id)


def test_limit_and_offset_select_the_requested_window(client, admin, make_user, auth_header):  # AC7
    others = [make_user(email=f"u{i}@example.com") for i in range(5)]

    body = client.get(USERS, params={"limit": 2, "offset": 2}, headers=auth_header(admin)).json()

    assert [item["id"] for item in body["items"]] == [str(others[1].id), str(others[2].id)]
    assert body["total"] == 6


@pytest.mark.parametrize("params", [{"limit": 101}, {"limit": 0}, {"offset": -1}])
def test_out_of_range_pagination_is_422(client, admin, auth_header, params):  # AC7, EC14
    r = client.get(USERS, params=params, headers=auth_header(admin))

    assert r.status_code == 422
    assert r.json()["error"]["code"] == "VALIDATION_ERROR"


def test_limit_100_is_allowed(client, admin, auth_header):  # AC7 boundary
    assert client.get(USERS, params={"limit": 100}, headers=auth_header(admin)).status_code == 200


def test_offset_past_the_end_returns_empty_items(client, admin, auth_header):  # EC15
    body = client.get(USERS, params={"offset": 50}, headers=auth_header(admin)).json()

    assert body["items"] == []
    assert body["total"] == 1


def test_users_route_documents_error_responses():  # AC13
    responses = app.openapi()["paths"][USERS]["get"]["responses"]

    for status in ("401", "403", "422", "500"):
        assert responses[status]["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorResponse")
