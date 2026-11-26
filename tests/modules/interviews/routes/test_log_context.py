"""Log context on real interview requests (U1 structlog, AC4): `session` and `user` reach every line of a request
without any log call passing them, in the plain and the streamed answer turn."""

import pytest

INTERVIEW_LOGGERS = {"app.llm", "app.llm.context", "app.rag"}


@pytest.fixture
def started(make_user, start_interview, llm):
    owner = make_user(email="owner@example.com")
    created = start_interview(owner, question_count=3).json()
    return owner, created["session"]["id"], created["current_question"]


def _request_lines(app_logs, path_end: str, method: str = "POST") -> list[dict]:
    """Every line of the one request whose access line ends with `path_end`."""
    lines = [record.line for record in app_logs.records]
    [access] = [
        line for line in lines
        if line["event"] == "http_request" and line["method"] == method and line["path"].endswith(path_end)
    ]  # fmt: skip
    return [line for line in lines if line["request_id"] == access["request_id"]]


def test_a_start_request_logs_the_new_session_and_the_user_on_every_line(make_user, start_interview, llm, app_logs):
    owner = make_user(email="owner@example.com")

    created = start_interview(owner, question_count=3).json()

    lines = _request_lines(app_logs, "/interviews")
    interview_lines = [line for line in lines if line["logger"] in INTERVIEW_LOGGERS]
    assert {line["event"] for line in interview_lines} >= {"llm_call", "context_build"}
    assert {line["session"] for line in interview_lines} == {created["session"]["id"]}
    assert {line["user"] for line in lines} == {str(owner.id)}


def test_an_answer_turn_logs_its_session_and_user_on_every_line(started, answer, app_logs):
    owner, session_id, q1 = started

    assert answer(owner, session_id, q1["id"]).status_code == 201

    lines = _request_lines(app_logs, f"/{session_id}/messages")
    assert {line["event"] for line in lines} >= {"llm_call", "turn_summary", "http_request"}
    assert {line["session"] for line in lines} == {session_id}
    assert {line["user"] for line in lines} == {str(owner.id)}


def test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream(started, stream_answer, app_logs):
    owner, session_id, q1 = started

    turn = stream_answer(owner, session_id, q1["id"])

    assert turn.names()[-1] == "done"
    lines = _request_lines(app_logs, f"/{session_id}/messages/stream")
    # stream_turn_summary is written by the SSE generator, after the endpoint itself has returned.
    assert {line["event"] for line in lines} >= {"llm_call", "turn_summary", "stream_turn_summary"}
    assert {line["session"] for line in lines} == {session_id}
    assert {line["user"] for line in lines} == {str(owner.id)}


def test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(started, make_user, answer, app_logs):
    _, session_id, q1 = started
    stranger = make_user(email="stranger@example.com")

    assert answer(stranger, session_id, q1["id"]).status_code == 404

    lines = _request_lines(app_logs, f"/{session_id}/messages")
    assert {line["user"] for line in lines} == {str(stranger.id)}
    assert {line["session"] for line in lines} == {session_id}
