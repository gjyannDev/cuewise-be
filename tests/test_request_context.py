import asyncio
import re
import time

import httpx
import pytest
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.core.logging import RECORD_KEYS, bind_log_context, get_logger
from app.core.middleware import RequestContextMiddleware


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


def test_one_access_line_per_request_with_its_fields(client, log_lines):  # AC13, AC3
    r = client.get("/health")

    [access] = log_lines.events("http_request")
    assert access["logger"] == "app.request"
    assert (access["method"], access["path"], access["status"]) == ("GET", "/health", 200)
    assert isinstance(access["duration_ms"], float)
    assert access["request_id"] == r.headers["x-request-id"]


def test_every_line_of_a_request_carries_its_request_id(client, log_lines):  # AC3
    r = client.get("/_test/conflict", headers={"X-Request-ID": "frontend-abc_123"})

    lines = log_lines.lines()
    assert {line["logger"] for line in lines} >= {"app.errors", "app.request"}
    assert {line["request_id"] for line in lines} == {r.headers["x-request-id"]} == {"frontend-abc_123"}


def test_an_unsafe_client_id_never_reaches_the_log(client, log_lines):  # EC9
    r = client.get("/_test/conflict", headers={"X-Request-ID": "has space"})

    assert {line["request_id"] for line in log_lines.lines()} == {r.headers["x-request-id"]}
    assert "has space" not in log_lines.path.read_text(encoding="utf-8")


def test_crash_log_carries_the_real_request_id(client, log_lines):  # AC16
    r = client.get("/_test/crash")

    [crash] = [line for line in log_lines.lines() if line["logger"] == "app.errors"]
    assert crash["request_id"] == r.json()["error"]["request_id"] != "-"
    assert "RuntimeError: kaboom" in crash["exception"]


def test_an_authenticated_request_logs_the_user_without_passing_it(client, log_lines, make_user, auth_header):  # AC4
    user = make_user()

    r = client.get("/api/v1/auth/me", headers=auth_header(user))

    assert r.status_code == 200
    [access] = log_lines.events("http_request")
    assert access["user"] == str(user.id)
    assert user.email not in log_lines.path.read_text(encoding="utf-8")


def test_a_log_line_after_the_request_is_outside_it(client, log_lines, make_user, auth_header):  # EC1
    client.get("/api/v1/auth/me", headers=auth_header(make_user()))

    get_logger("app.test").info("after_request")

    [after] = log_lines.events("after_request")
    assert after["request_id"] == "-"
    assert "user" not in after


def test_every_line_across_varied_requests_is_json_with_the_record_keys(client, log_lines, make_user, auth_header):  # AC2
    user = make_user()
    for path in ["/health", "/_test/conflict", "/_test/integrity", "/_test/db-down", "/_test/crash", "/does-not-exist"]:
        client.get(path)
    client.get("/api/v1/auth/me", headers=auth_header(user))
    client.post("/api/v1/auth/login", json={"email": user.email, "password": "wrong-password"})
    client.post("/api/v1/auth/login", json={"email": "not-an-email"})

    lines = log_lines.lines()  # json.loads on every line: a non-JSON line fails here
    assert len(lines) >= 9
    assert all(set(RECORD_KEYS) <= line.keys() for line in lines)
    assert all(line["request_id"] != "-" for line in lines)


# --- concurrent requests (EC4) ---


def _context_app():
    """A tiny app behind the real middleware: an SSE-style stream that logs from its generator after the endpoint
    returned, and a sync endpoint that FastAPI runs in a worker thread. Each binds its own session."""
    app = FastAPI()
    app.add_middleware(RequestContextMiddleware)
    log = get_logger("app.test")

    @app.get("/stream/{name}")
    async def stream(name: str):
        bind_log_context(session=name)

        async def chunks():
            for i in range(3):
                await asyncio.sleep(0.01)  # hands the loop to the other requests mid-stream
                log.info("stream_chunk", chunk=i)
                yield f"data: {i}\n\n"

        return StreamingResponse(chunks(), media_type="text/event-stream")

    @app.get("/plain/{name}")
    def plain(name: str):
        bind_log_context(session=name)
        time.sleep(0.01)
        log.info("plain_work")
        return {"ok": True}

    return app


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_concurrent_requests_and_streams_keep_their_own_context(log_lines):  # EC4, AC4
    transport = httpx.ASGITransport(app=_context_app())
    names = ["stream-a", "stream-b", "plain-c", "plain-d"]
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as http:
        responses = await asyncio.gather(*(http.get(f"/{name.split('-')[0]}/{name}") for name in names))

    sessions_by_request: dict[str, set[str]] = {}
    for line in log_lines.lines():
        sessions_by_request.setdefault(line["request_id"], set()).add(line["session"])
    assert sorted(sessions_by_request) == sorted(r.headers["x-request-id"] for r in responses)
    assert all(len(sessions) == 1 for sessions in sessions_by_request.values())
    assert sorted(next(iter(s)) for s in sessions_by_request.values()) == sorted(names)
    assert len(log_lines.events("stream_chunk")) == 6
