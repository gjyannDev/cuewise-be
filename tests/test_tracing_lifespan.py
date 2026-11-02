"""The app lifespan builds the tracer once and flushes it on shutdown (langfuse-tracing AC10, EC10)."""

from fastapi.testclient import TestClient

from app import main
from app.core.ai.tracing import Tracer


class RecordingClient:
    def __init__(self, fail=False):
        self.calls, self.fail = [], fail

    def flush(self):
        self.calls.append("flush")
        if self.fail:
            raise RuntimeError("down")

    def shutdown(self):
        self.calls.append("shutdown")


def _run_app(monkeypatch, client):
    tracer = Tracer(client, propagate=lambda **_: None)
    monkeypatch.setattr(main, "build_tracer", lambda _settings: tracer)
    with TestClient(main.app) as http:
        assert http.get("/health").status_code == 200
        assert main.app.state.tracer is tracer
        assert client.calls == []


def test_shutdown_flushes_then_stops_the_tracer(monkeypatch):  # AC10
    client = RecordingClient()

    _run_app(monkeypatch, client)

    assert client.calls == ["flush", "shutdown"]


def test_shutdown_completes_even_when_the_flush_fails(monkeypatch):  # AC10, EC10
    client = RecordingClient(fail=True)

    _run_app(monkeypatch, client)

    assert client.calls == ["flush", "shutdown"]
