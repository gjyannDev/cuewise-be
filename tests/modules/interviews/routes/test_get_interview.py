import pytest

from app.main import app

INTERVIEWS = "/api/v1/interviews"


@pytest.fixture
def started(start_interview, make_user):
    """An owner with one started 3-question interview; returns (owner, POST response body)."""
    owner = make_user(email="owner@example.com")
    return owner, start_interview(owner).json()


def test_owner_gets_session_and_first_question(client, auth_header, started):  # AC10
    owner, created = started

    r = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(owner))

    assert r.status_code == 200
    assert r.json() == created


def test_abandoned_session_is_still_readable(client, auth_header, start_interview, started):  # AC10, EC13
    owner, created = started
    start_interview(owner)

    r = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(owner))

    assert r.status_code == 200
    assert r.json()["session"]["status"] == "abandoned"
    assert r.json()["current_question"] == created["current_question"]


def test_missing_and_foreign_sessions_are_the_same_404(client, auth_header, make_user, started):  # AC11, EC18, EC19
    _, created = started
    stranger = make_user(email="stranger@example.com")
    missing = "01890a5d-ac96-774b-bcce-b302099a8057"

    foreign_r = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(stranger))
    missing_r = client.get(f"{INTERVIEWS}/{missing}", headers=auth_header(stranger))

    assert foreign_r.status_code == missing_r.status_code == 404
    foreign_error, missing_error = foreign_r.json()["error"], missing_r.json()["error"]
    assert foreign_error["code"] == "NOT_FOUND"
    del foreign_error["request_id"], missing_error["request_id"]
    assert foreign_error == missing_error


def test_admin_cannot_read_another_users_session(client, auth_header, make_user, started):  # AC11, EC21
    _, created = started
    admin = make_user(email="admin@example.com", role="admin")

    r = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(admin))

    assert r.status_code == 404


def test_malformed_session_id_is_422(client, auth_header, make_user, db):  # AC11, EC20
    r = client.get(f"{INTERVIEWS}/not-a-uuid", headers=auth_header(make_user()))

    assert r.status_code == 422


def test_get_without_token_is_401(client, started):  # AC12, EC1
    _, created = started

    r = client.get(f"{INTERVIEWS}/{created['session']['id']}")

    assert r.status_code == 401
    assert r.json()["error"]["code"] == "TOKEN_MISSING"


def test_get_without_permission_is_403(client, auth_header, make_user, started):  # AC12, EC2
    _, created = started

    r = client.get(f"{INTERVIEWS}/{created['session']['id']}", headers=auth_header(make_user(role="superuser")))

    assert r.status_code == 403


@pytest.mark.parametrize(
    ("path", "method", "statuses"),
    [
        (INTERVIEWS, "post", {"401", "403", "409", "422", "500"}),
        (INTERVIEWS + "/{session_id}", "get", {"401", "403", "404", "422", "500"}),
    ],
)
def test_interview_routes_document_error_responses(path, method, statuses):  # AC16
    responses = app.openapi()["paths"][path][method]["responses"]

    for status in statuses:
        assert responses[status]["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorResponse")
