from uuid import UUID

from app.modules.auth.auth_constants import Role


def _uuid7(value):
    parsed = UUID(value)
    assert parsed.version == 7
    return parsed


def test_registered_user_gets_a_uuid7_id(client, db):  # R1, R4
    r = client.post("/api/v1/auth/register", json={"email": "new@example.com", "password": "password123"})

    assert r.status_code == 201
    _uuid7(r.json()["id"])


def test_me_returns_the_uuid7_id(client, make_user, auth_header):  # R1, R4
    user = make_user()

    body = client.get("/api/v1/auth/me", headers=auth_header(user)).json()

    assert _uuid7(body["id"]) == user.id


def test_users_list_ids_are_uuid7_in_creation_order(client, make_user, auth_header):  # R4, R5, E3
    admin = make_user(email="admin@example.com", role=Role.admin)
    created = [admin] + [make_user(email=f"u{i}@example.com") for i in range(5)]

    items = client.get("/api/v1/users", headers=auth_header(admin)).json()["items"]

    assert [_uuid7(item["id"]) for item in items] == [u.id for u in created]
