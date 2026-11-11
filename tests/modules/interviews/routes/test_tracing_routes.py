"""Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2, AC3, AC11, EC11).

A recording tracer replaces the real one, so nothing leaves the process.
"""

from contextlib import contextmanager

import pytest

from app.core.ai.tracing import Tracer
from app.main import app
from app.modules.interviews.dependencies.interviews_shared_dependencies import (
    get_tracer,
)


class RecordingClient:
    def __init__(self):
        self.traces = []

    @contextmanager
    def start_as_current_observation(self, **kwargs):
        self.traces.append(kwargs)
        yield

    def start_observation(self, **kwargs):  # pragma: no cover - generations are covered in tests/core/ai
        raise AssertionError("route tests do not wrap the provider")


@pytest.fixture
def traces():
    client, propagated = RecordingClient(), []

    @contextmanager
    def propagate(**attrs):
        propagated.append(attrs)
        yield

    app.dependency_overrides[get_tracer] = lambda: Tracer(client, propagate=propagate)
    yield type("Traces", (), {"spans": client.traces, "attrs": propagated})
    app.dependency_overrides.pop(get_tracer, None)


def test_start_opens_one_trace_with_user_session_and_setup(start_interview, make_user, traces):  # AC1
    owner = make_user()

    created = start_interview(owner).json()

    [span] = traces.spans
    assert span["name"] == "start-interview"
    assert span["input"]["role"] == "backend"
    assert traces.attrs == [{"user_id": str(owner.id), "session_id": created["session"]["id"]}]


def test_answer_opens_one_trace_with_the_answer_as_input(start_interview, make_user, answer, traces):  # AC2
    owner = make_user()
    created = start_interview(owner).json()
    traces.spans.clear(), traces.attrs.clear()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"], text="I fixed the race.")

    assert r.status_code == 201
    [span] = traces.spans
    assert span["name"] == "answer-turn"
    assert span["input"] == {"question_id": created["current_question"]["id"], "answer": "I fixed the race."}
    assert traces.attrs == [{"user_id": str(owner.id), "session_id": created["session"]["id"]}]


def test_streamed_answer_opens_one_trace(start_interview, make_user, stream_answer, traces):  # AC3
    owner = make_user()
    created = start_interview(owner).json()
    traces.spans.clear(), traces.attrs.clear()

    turn = stream_answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert turn.status_code == 200
    [span] = traces.spans
    assert span["name"] == "answer-turn"
    assert traces.attrs == [{"user_id": str(owner.id), "session_id": created["session"]["id"]}]


def test_a_rejected_answer_opens_no_trace(start_interview, make_user, answer, traces):  # AC11
    owner = make_user()
    created = start_interview(owner).json()
    traces.spans.clear()

    r = answer(owner, created["session"]["id"], "00000000-0000-0000-0000-000000000000")

    assert r.status_code == 409
    assert traces.spans == []


def test_read_routes_open_no_trace(start_interview, make_user, client, auth_header, traces):  # AC11
    owner = make_user()
    created = start_interview(owner).json()
    traces.spans.clear()
    session_id = created["session"]["id"]

    assert client.get(f"/api/v1/interviews/{session_id}", headers=auth_header(owner)).status_code == 200
    assert client.get(f"/api/v1/interviews/{session_id}/messages", headers=auth_header(owner)).status_code == 200
    assert client.get("/health").status_code == 200

    assert traces.spans == []


def test_two_users_get_their_own_ids(start_interview, make_user, traces):  # EC11
    first, second = make_user("a@example.com"), make_user("b@example.com")

    a = start_interview(first).json()
    b = start_interview(second).json()

    assert traces.attrs == [
        {"user_id": str(first.id), "session_id": a["session"]["id"]},
        {"user_id": str(second.id), "session_id": b["session"]["id"]},
    ]
