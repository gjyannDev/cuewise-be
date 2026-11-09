"""GET /api/v1/interviews: the candidate's interview history, newest first, paginated (spec: interview-history)."""

import json

import pytest
from sqlalchemy import event

from app.modules.interviews.models.interviews_model import (
    InterviewQuestion,
    InterviewSession,
)

INTERVIEWS = "/api/v1/interviews"
ITEM_FIELDS = {
    "id",
    "role",
    "level",
    "interview_type",
    "status",
    "question_count",
    "answered_count",
    "created_at",
}


def history(client, auth_header, user, **params):
    return client.get(INTERVIEWS, params=params, headers=auth_header(user))


def started_ids(start_interview, user, n):
    """Start `n` interviews in a row; returns their ids newest first (each start abandons the previous one)."""
    return [start_interview(user).json()["session"]["id"] for _ in range(n)][::-1]


@pytest.fixture
def three_statuses(start_interview, answer, make_user):
    """One interview of each status, started in this order: completed, then abandoned, then in progress."""
    owner = make_user()
    done = start_interview(owner, question_count=1).json()
    answer(owner, done["session"]["id"], done["current_question"]["id"])
    abandoned = start_interview(owner).json()["session"]["id"]
    current = start_interview(owner).json()["session"]["id"]
    return owner, {"completed": done["session"]["id"], "abandoned": abandoned, "in_progress": current}


def test_empty_history_is_an_empty_page(client, make_user, auth_header):  # AC1, AC9, EC1
    owner = make_user()

    r = history(client, auth_header, owner)

    assert r.status_code == 200
    assert r.json() == {"items": [], "total": 0, "limit": 20, "offset": 0}


def test_an_item_has_only_the_table_fields(client, make_user, auth_header, start_interview):  # AC2, EC13
    owner = make_user()
    created = start_interview(owner, job_description="Payments team at Acme Corp, Kafka heavy.").json()["session"]

    r = history(client, auth_header, owner)

    [item] = r.json()["items"]
    assert set(item) == ITEM_FIELDS
    assert item == {
        "id": created["id"],
        "role": "backend",
        "level": "junior",
        "interview_type": "behavioral",
        "status": "in_progress",
        "question_count": 3,
        "answered_count": 0,
        "created_at": created["created_at"],
    }
    assert "Acme" not in r.text
    assert "user_id" not in r.text


def test_only_the_callers_interviews_are_listed_and_counted(
    client, make_user, auth_header, start_interview
):  # AC3, EC2
    owner, other = make_user(email="owner@example.com"), make_user(email="other@example.com")
    mine = started_ids(start_interview, owner, 2)
    started_ids(start_interview, other, 3)

    body = history(client, auth_header, owner).json()

    assert [item["id"] for item in body["items"]] == mine
    assert body["total"] == 2


def test_newest_first_with_the_in_progress_interview_on_top(
    client, make_user, auth_header, start_interview
):  # AC4, EC14
    owner = make_user()
    ids = started_ids(start_interview, owner, 3)

    items = history(client, auth_header, owner).json()["items"]

    assert [item["id"] for item in items] == ids
    assert [item["status"] for item in items] == ["in_progress", "abandoned", "abandoned"]


def test_limit_and_offset_select_the_requested_window(
    client, make_user, auth_header, start_interview
):  # AC5
    owner = make_user()
    ids = started_ids(start_interview, owner, 5)

    body = history(client, auth_header, owner, limit=2, offset=2).json()

    assert [item["id"] for item in body["items"]] == ids[2:4]
    assert (body["total"], body["limit"], body["offset"]) == (5, 2, 2)


@pytest.mark.parametrize(
    "params", [{"limit": 0}, {"limit": 101}, {"limit": "abc"}, {"offset": -1}], ids=str
)
def test_out_of_range_pagination_is_422(client, make_user, auth_header, params):  # AC5, EC3
    r = history(client, auth_header, make_user(), **params)

    assert r.status_code == 422
    assert r.json()["error"]["code"] == "VALIDATION_ERROR"


def test_offset_past_the_end_is_an_empty_page_with_the_real_total(
    client, make_user, auth_header, start_interview
):  # AC5, EC4
    owner = make_user()
    started_ids(start_interview, owner, 2)

    body = history(client, auth_header, owner, offset=50).json()

    assert body["items"] == []
    assert body["total"] == 2


@pytest.mark.parametrize("status", ["completed", "abandoned", "in_progress"])
def test_the_status_filter_narrows_items_and_total(client, auth_header, three_statuses, status):  # AC6, EC6
    owner, ids = three_statuses

    body = history(client, auth_header, owner, status=status).json()

    assert [item["id"] for item in body["items"]] == [ids[status]]
    assert body["total"] == 1


def test_an_unknown_status_is_422(client, make_user, auth_header):  # AC6, EC5
    r = history(client, auth_header, make_user(), status="done")

    assert r.status_code == 422
    assert r.json()["error"]["code"] == "VALIDATION_ERROR"


def test_every_status_is_listed_without_a_filter(client, auth_header, three_statuses):  # AC7, EC9
    owner, ids = three_statuses

    body = history(client, auth_header, owner).json()

    # The abandoned one was left before any answer and is still listed.
    assert [(item["id"], item["status"]) for item in body["items"]] == [
        (ids["in_progress"], "in_progress"),
        (ids["abandoned"], "abandoned"),
        (ids["completed"], "completed"),
    ]
    assert body["total"] == 3


# --- answered_count: main questions finished, follow-ups not counted (AC8) ---


def answered(client, auth_header, user) -> list[tuple[str, int]]:
    return [(item["status"], item["answered_count"]) for item in history(client, auth_header, user).json()["items"]]


def test_answered_count_after_plain_turns(client, auth_header, make_user, start_interview, answer):  # AC8, EC8
    owner = make_user()
    done = start_interview(owner, question_count=2).json()
    current = done["current_question"]
    while current is not None:
        current = answer(owner, done["session"]["id"], current["id"]).json()["current_question"]
    going = start_interview(owner, question_count=3).json()
    answer(owner, going["session"]["id"], going["current_question"]["id"])

    assert answered(client, auth_header, owner) == [("in_progress", 1), ("completed", 2)]


def test_follow_ups_do_not_count_as_answered_questions(
    client, auth_header, make_user, start_interview, answer, llm, reply_json, decision_json
):  # AC8, EC7, EC8
    owner = make_user()
    # Main 1 moves on; main 2 (the last) gets a follow-up; answering that completes the interview.
    llm.script(
        reply_json("Tell me about a conflict on your team?", "behavioral"),
        reply_json("Tell me about a deadline you missed?", "behavioral"),
        json.dumps({"question": "What was the result for the team?"}),
    )
    llm.script_decide(decision_json(), decision_json("follow_up", "missing_result"))
    created = start_interview(owner, question_count=2).json()
    session_id, current = created["session"]["id"], created["current_question"]
    current = answer(owner, session_id, current["id"]).json()["current_question"]
    current = answer(owner, session_id, current["id"]).json()["current_question"]
    assert (current["question_kind"], current["main_number"]) == ("follow_up", 2)

    assert answered(client, auth_header, owner) == [("in_progress", 1)]

    answer(owner, session_id, current["id"])

    assert answered(client, auth_header, owner) == [("completed", 2)]


def test_answered_count_of_a_session_with_every_question_stored_up_front(
    client, auth_header, make_user, db
):  # AC8, EC10
    owner = make_user()
    session = InterviewSession(
        user_id=owner.id,
        role="backend",
        level="junior",
        interview_type="behavioral",
        question_count=4,
        status="abandoned",
        current_position=3,
    )
    db.add(session)
    db.flush()
    db.add_all(
        InterviewQuestion(session_id=session.id, position=p, text=f"Q{p}?", category="behavioral", bank_id=f"b{p}")
        for p in range(1, 5)
    )
    db.commit()

    assert answered(client, auth_header, owner) == [("abandoned", 2)]


def test_anonymous_request_is_401(client, db):  # AC10, EC11
    assert client.get(INTERVIEWS).status_code == 401


def test_without_permission_is_403(client, make_user, auth_header):  # AC10, EC11
    r = history(client, auth_header, make_user(role="superuser"))

    assert r.status_code == 403
    assert r.json()["error"]["code"] == "FORBIDDEN"


def test_the_in_progress_row_is_continued_with_the_existing_endpoints(
    client, make_user, auth_header, start_interview, answer
):  # AC11
    owner = make_user()
    created = start_interview(owner).json()
    answer(owner, created["session"]["id"], created["current_question"]["id"])

    [row] = history(client, auth_header, owner).json()["items"]
    resumed = client.get(f"{INTERVIEWS}/{row['id']}", headers=auth_header(owner))
    transcript = client.get(f"{INTERVIEWS}/{row['id']}/messages", headers=auth_header(owner))

    assert row["status"] == "in_progress"
    assert resumed.status_code == 200
    assert resumed.json()["current_question"]["position"] == 2
    assert [item["kind"] for item in transcript.json()["items"]] == ["question", "answer", "reaction", "question"]


def test_a_page_costs_the_same_queries_whatever_its_size(
    client, make_user, auth_header, start_interview, db
):  # AC12
    owner = make_user()
    started_ids(start_interview, owner, 5)
    statements: list[str] = []

    def record(conn, cursor, statement, *args):
        # Only the history's own queries: the auth user lookup runs once, then the test session's identity map has it.
        if "interview_" in statement:
            statements.append(statement)

    event.listen(db.get_bind(), "before_cursor_execute", record)
    try:
        counts = []
        for limit in (1, 5):
            statements.clear()
            assert len(history(client, auth_header, owner, limit=limit).json()["items"]) == limit
            counts.append(len(statements))
    finally:
        event.remove(db.get_bind(), "before_cursor_execute", record)

    assert counts == [2, 2]  # the page and its total


# --- sorting: sort_by / sort_dir, server-side across pages, `id desc` breaks ties ---


@pytest.fixture
def sortable(make_user, db):
    """Five sessions stored directly (oldest first), with values that sort differently on every column."""
    owner = make_user()
    rows = [
        ("mobile", "senior", "technical", "abandoned"),
        ("backend", "intern", "mixed", "completed"),
        ("frontend", "senior", "behavioral", "abandoned"),
        ("backend", "mid", "technical", "in_progress"),
        ("data", "junior", "behavioral", "completed"),
    ]
    sessions = []
    for role, level, interview_type, status in rows:
        session = InterviewSession(
            user_id=owner.id, role=role, level=level, interview_type=interview_type, question_count=3, status=status
        )
        db.add(session)
        db.flush()
        sessions.append(session)
    db.commit()
    return owner, [str(s.id) for s in sessions]


def ids_of(body):
    return [item["id"] for item in body["items"]]


def test_without_sort_params_the_order_is_newest_first(client, auth_header, sortable):  # R11
    owner, ids = sortable

    assert ids_of(history(client, auth_header, owner).json()) == ids[::-1]


def test_created_at_ascending_is_oldest_first(client, auth_header, sortable):  # R11
    owner, ids = sortable

    body = history(client, auth_header, owner, sort_by="created_at", sort_dir="asc").json()

    assert ids_of(body) == ids


@pytest.mark.parametrize(
    ("column", "direction", "expected"),
    [
        # Stored values (oldest -> newest): role mobile, backend, frontend, backend, data.
        ("role", "asc", [3, 1, 4, 2, 0]),
        ("role", "desc", [0, 2, 4, 3, 1]),
        # level senior, intern, senior, mid, junior
        ("level", "asc", [1, 4, 3, 2, 0]),
        ("level", "desc", [2, 0, 3, 4, 1]),
        # interview_type technical, mixed, behavioral, technical, behavioral
        ("interview_type", "asc", [4, 2, 1, 3, 0]),
        ("interview_type", "desc", [3, 0, 1, 4, 2]),
        # status abandoned, completed, abandoned, in_progress, completed
        ("status", "asc", [2, 0, 4, 1, 3]),
        ("status", "desc", [3, 4, 1, 2, 0]),
    ],
    ids=str,
)
def test_a_column_sorts_by_its_stored_value_with_ties_newest_first(
    client, auth_header, sortable, column, direction, expected
):  # R11
    owner, ids = sortable

    body = history(client, auth_header, owner, sort_by=column, sort_dir=direction).json()

    assert ids_of(body) == [ids[i] for i in expected]


@pytest.mark.parametrize("column", ["created_at", "role", "level", "interview_type", "status"])
def test_sorted_pages_neither_overlap_nor_skip_a_row(client, auth_header, sortable, column):  # R11, R12
    owner, _ = sortable
    whole = ids_of(history(client, auth_header, owner, sort_by=column, sort_dir="asc").json())

    pages = [
        ids_of(history(client, auth_header, owner, sort_by=column, sort_dir="asc", limit=2, offset=offset).json())
        for offset in (0, 2, 4)
    ]

    assert [row for page in pages for row in page] == whole


def test_sorting_combines_with_the_status_filter(client, auth_header, sortable):  # R11
    owner, ids = sortable

    body = history(client, auth_header, owner, status="completed", sort_by="role", sort_dir="asc").json()

    assert ids_of(body) == [ids[1], ids[4]]  # backend, data
    assert body["total"] == 2


@pytest.mark.parametrize("params", [{"sort_by": "progress"}, {"sort_by": "id"}, {"sort_dir": "up"}], ids=str)
def test_an_unknown_sort_is_422(client, make_user, auth_header, params):  # R12
    r = history(client, auth_header, make_user(), **params)

    assert r.status_code == 422
    assert r.json()["error"]["code"] == "VALIDATION_ERROR"


def test_sorting_lists_only_the_callers_interviews(client, auth_header, make_user, sortable):  # R12
    owner, ids = sortable
    stranger = make_user(email="stranger@example.com")

    assert history(client, auth_header, stranger, sort_by="role", sort_dir="asc").json()["items"] == []
    assert sorted(ids_of(history(client, auth_header, owner, sort_by="role").json())) == sorted(ids)


def test_a_sorted_page_costs_the_same_queries_whatever_its_size(
    client, auth_header, sortable, db
):  # R12
    owner, _ = sortable
    statements: list[str] = []

    def record(conn, cursor, statement, *args):
        if "interview_" in statement:
            statements.append(statement)

    event.listen(db.get_bind(), "before_cursor_execute", record)
    try:
        counts = []
        for limit in (1, 5):
            statements.clear()
            body = history(client, auth_header, owner, sort_by="level", sort_dir="desc", limit=limit).json()
            assert len(body["items"]) == limit
            counts.append(len(statements))
    finally:
        event.remove(db.get_bind(), "before_cursor_execute", record)

    assert counts == [2, 2]


def test_the_list_route_documents_its_error_responses(client):  # AC10, AC13
    responses = client.app.openapi()["paths"][INTERVIEWS]["get"]["responses"]

    for status in ("401", "403", "422", "500"):
        assert responses[status]["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorResponse")
