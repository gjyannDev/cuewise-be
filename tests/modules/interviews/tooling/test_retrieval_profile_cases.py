"""Profile cases in the retrieval eval (resume-aware-interview Step 9c; seam S5).

A profile case's query is what `profile_query_text` sends: a candidate's short items (skills, technologies, titles,
project names), never sentences. The runner scores them apart from the job-description cases, so the job-description
numbers stay comparable with earlier runs and the profile half gets its own baseline.
"""

import pytest

from app.modules.interviews.constants.interviews_constants import JobRole, Level
from app.modules.interviews.tooling.interviews_rag_evals import (
    RetrievalCase,
    RetrievalRow,
    _retrieval_cases,
    case_set_problems,
    retrieval_run_scores,
)


def case(case_id="p1", kind="profile", query="Python, PostgreSQL, Redis, Backend Engineer, refunds-service"):
    return RetrievalCase(
        id=case_id, kind=kind, role=JobRole.backend, level=Level.mid, query=query, expected=["n.md#Note"]
    )


def row(c, vector_recall, vector_rr):
    return RetrievalRow(c, [], vector_recall, vector_rr, 0.2, 0.1, error=None)


def test_the_shipped_case_set_has_profile_cases_and_no_problems():
    cases = _retrieval_cases()

    assert sum(c.kind == "profile" for c in cases) >= 3
    assert case_set_problems(cases) == []


@pytest.mark.parametrize(
    "query",
    [
        "Built a refunds service and its retry queue.",  # a sentence (a summary), not short items
        "Python",  # one item: not a profile's query
        "Python, a very long item that is really a description of a whole project",  # an item too long to be short
    ],
)
def test_a_profile_case_must_be_short_items(query):
    problems = case_set_problems([*_retrieval_cases(), case("bad-profile", query=query)])

    assert any("bad-profile" in p and "short items" in p for p in problems)


def test_job_description_averages_leave_the_profile_cases_out():
    jd = [row(case("j1", kind="plain", query="Backend role."), 1.0, 1.0), row(case("j2", kind="plain"), 0.0, 0.5)]
    profile = [row(case("p1"), 0.5, 0.25)]

    scores = dict(retrieval_run_scores([*jd, *profile]))

    assert scores["vector_recall_at_5"] == 0.5 and scores["vector_mrr"] == 0.75  # job-description cases only
    assert scores["profile_vector_recall_at_5"] == 0.5 and scores["profile_vector_mrr"] == 0.25


def test_without_profile_cases_the_run_scores_are_todays():
    names = [name for name, _ in retrieval_run_scores([row(case("j1", kind="plain"), 1.0, 1.0)])]

    assert names == ["vector_recall_at_5", "vector_mrr", "filter_recall_at_5", "filter_mrr", "errored_count"]
