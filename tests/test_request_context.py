import re

import pytest


def test_generated_request_id_matches_header_and_body(client):  # AC9
    r = client.get("/_test/conflict")

    request_id = r.headers["x-request-id"]
    assert re.fullmatch(r"[0-9a-f]{32}", request_id)
    assert r.json()["error"]["request_id"] == request_id


def test_safe_client_request_id_is_reused(client):  # AC10
    r = client.get("/_test/conflict", headers={"X-Request-ID": "frontend-abc_123"})

    assert r.headers["x-request-id"] == "frontend-abc_123"
    assert r.json()["error"]["request_id"] == "frontend-abc_123"


@pytest.mark.parametrize("unsafe", ["has space", "semi;colon", "a" * 65, ""])
def test_unsafe_client_request_id_is_replaced(client, unsafe):  # AC11
    r = client.get("/_test/conflict", headers={"X-Request-ID": unsafe})

    assert r.headers["x-request-id"] != unsafe
    assert re.fullmatch(r"[0-9a-f]{32}", r.headers["x-request-id"])


@pytest.mark.parametrize("path", ["/health", "/_test/conflict", "/does-not-exist", "/_test/crash"])
def test_request_id_header_sent_exactly_once(client, path):  # AC12, EC1
    r = client.get(path)

    assert len(r.headers.get_list("x-request-id")) == 1
    if r.status_code >= 400:
        assert r.json()["error"]["request_id"] == r.headers["x-request-id"]


def test_one_access_log_line_per_request(client, app_logs):  # AC13
    r = client.get("/health")

    access = [rec for rec in app_logs.records if rec.name == "app.request"]
    assert len(access) == 1
    assert "GET /health -> 200" in access[0].getMessage()
    assert access[0].request_id == r.headers["x-request-id"]


def test_crash_log_carries_the_real_request_id(client, app_logs):  # AC16
    r = client.get("/_test/crash")

    crash = next(rec for rec in app_logs.records if rec.name == "app.errors")
    assert crash.request_id == r.json()["error"]["request_id"] != "-"
