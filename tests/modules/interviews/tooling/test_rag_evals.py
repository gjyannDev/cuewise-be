"""The knowledge-base RAG evals' pure parts (knowledge-base-rag Step 10; AC23-AC25, EC24, EC25).

The real-model runs (retrieval against the ingested corpus, three generation arms, the blind sheet) are opt-in; these
tests pin the metrics, the sheet and its parser, and one generation arm on the fake provider.
"""

import json
import uuid
from argparse import Namespace
from contextlib import contextmanager
from contextvars import ContextVar
from types import SimpleNamespace

import pytest

from app.core.ai.fake import FakeEmbedder, FakeProvider
from app.core.ai.tracing import Tracer
from app.modules.interviews.constants.interviews_constants import (
    InterviewType,
    JobRole,
    Level,
)
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.tooling.interviews_rag_evals import (
    ARMS,
    GENERATION_KEYWORDS_PATH,
    CaseKind,
    RetrievalCase,
    SheetError,
    WrittenQuestion,
    _run_generation,
    build_sheet,
    case_set_problems,
    competencies_of,
    filter_baseline,
    read_rankings,
    recall_at_k,
    reciprocal_rank,
    run_scores,
    simulate_main_questions,
    skill_coverage,
    summarize_arm,
    threshold_sweep,
)
from app.modules.interviews.utils.interviews_knowledge_utils import ReferenceNote


def case(i: int, kind: CaseKind = "plain") -> RetrievalCase:
    return RetrievalCase(id=f"c{i}", kind=kind, role=JobRole.backend, level=Level.mid, query="q", expected=["a.md#A"])


# --- retrieval metrics (AC23) ---


@pytest.mark.parametrize(
    ("ranked", "expected", "k", "recall"),
    [
        (["a", "b", "c"], {"a"}, 5, 1.0),
        (["x", "y", "a", "b"], {"a", "b"}, 3, 0.5),
        (["x", "y"], {"a"}, 5, 0.0),
        (["x", "y", "z", "w", "v", "a"], {"a"}, 5, 0.0),  # sixth place is outside recall@5
    ],
)
def test_recall_at_k(ranked, expected, k, recall):
    assert recall_at_k(ranked, expected, k) == recall


@pytest.mark.parametrize(
    ("ranked", "expected", "rr"),
    [(["a", "b"], {"a"}, 1.0), (["x", "b", "a"], {"a", "b"}, 0.5), (["x", "y", "a"], {"a"}, 1 / 3), (["x"], {"a"}, 0.0)],
)
def test_reciprocal_rank_is_one_over_the_first_relevant_position(ranked, expected, rr):
    assert reciprocal_rank(ranked, expected) == pytest.approx(rr)


def test_the_filter_baseline_is_an_average_over_fixed_seeded_orderings():  # AC23: stable for a fixed seed set
    eligible = [f"n{i}" for i in range(12)]
    seeds = [uuid.UUID(int=i) for i in range(1, 21)]

    first = filter_baseline(eligible, {"n3"}, seeds, k=5)
    again = filter_baseline(eligible, {"n3"}, seeds, k=5)

    assert first == again
    recall, mrr = first
    # One relevant note out of 12, five picked at random: about 5/12 on average.
    assert 0.2 < recall < 0.7 and 0 < mrr < 1


def test_the_threshold_sweep_reports_recall_and_kept_count_per_threshold():  # Step 12 picks the threshold from it
    scored = [[("a", 0.9), ("b", 0.6), ("c", 0.3)], [("x", 0.55), ("a", 0.5)]]
    expected = [{"a"}, {"a"}]

    rows = threshold_sweep(scored, expected, [0.0, 0.52, 0.95], k=5)

    assert rows == [(0.0, 1.0, 2.5), (0.52, 0.5, 1.5), (0.95, 0.0, 0.0)]


def test_the_labelled_set_needs_15_queries_with_the_required_kinds():  # AC23
    good = [case(i) for i in range(10)] + [case(10 + i, "synonym") for i in range(3)]
    good += [case(13, "vague"), case(14, "role_boundary")]

    assert case_set_problems(good) == []
    problems = case_set_problems(good[:12])
    assert any("15" in p for p in problems) and any("synonym" in p for p in problems)
    assert any("duplicate" in p for p in case_set_problems([*good, case(0)]))


# --- generation metrics and one arm on the fake provider (AC24) ---

KEYWORDS = {"API design": ["api", "endpoint"], "Caching": ["cache"], "Testing": ["test"]}


def test_competencies_and_skill_coverage_are_keyword_rules():  # AC24 (a known limitation: wording games them)
    questions = ["How would you design an API endpoint for refunds?", "When would a cache hurt you?"]

    assert competencies_of(questions[0], KEYWORDS) == {"API design"}
    assert skill_coverage(questions, ["Python", "cache", "endpoint"]) == pytest.approx(2 / 3)
    assert skill_coverage(questions, []) is None


def test_the_simulator_writes_main_questions_only_and_records_usage():  # AC24
    llm = FakeProvider(
        [
            "CATEGORY: technical\nHow would you design an API endpoint for refunds?",
            "CATEGORY: technical\nWhen would a cache make an API slower?",
        ]
    )
    notes = (ReferenceNote(uuid.uuid7(), "API design", "Probe versioning.", 1, 0.9),)

    written = simulate_main_questions(
        llm,
        role=JobRole.backend,
        level=Level.mid,
        interview_type=InterviewType.technical,
        question_count=2,
        job_description="Payments APIs.",
        notes=notes,
        max_tokens=400,
    )

    assert [w.question for w in written] == [
        "How would you design an API endpoint for refunds?",
        "When would a cache make an API slower?",
    ]
    assert all(w.prompt_tokens and w.prompt_tokens > 0 for w in written)
    assert all("<reference_notes>" in call[1].content for call in llm.calls)


def test_an_invalid_reply_counts_as_a_failed_question_not_a_crash():  # EC24 feeds on this
    llm = FakeProvider(["not a question at all", "CATEGORY: technical\nHow do you test a payment flow?"])

    written = simulate_main_questions(
        llm,
        role=JobRole.backend,
        level=Level.mid,
        interview_type=InterviewType.technical,
        question_count=2,
        job_description=None,
        notes=(),
        max_tokens=400,
    )

    assert [w.question for w in written] == [None, "How do you test a payment flow?"]


def test_an_arm_summary_pools_its_interviews():  # AC24
    llm = FakeProvider(default="CATEGORY: technical\nHow would you cache an API endpoint?")
    runs = [
        simulate_main_questions(
            llm,
            role=JobRole.backend,
            level=Level.mid,
            interview_type=InterviewType.technical,
            question_count=2,
            job_description="APIs",
            notes=(),
            max_tokens=400,
        )
        for _ in range(2)
    ]

    summary = summarize_arm(runs, KEYWORDS, skills=[["cache"], ["python"]], start_ms=[0, 0])

    # The second question repeats the first, so the code-side repeat check rejects it.
    assert summary.questions == 4 and summary.valid == 2
    assert summary.distinct_competencies == 2.0  # API design and Caching in each interview
    assert summary.skill_coverage == 0.5
    assert summary.prompt_tokens > 0 and summary.start_ms == 0


def test_run_scores_are_the_keyword_rules_for_one_interview():
    run = [
        WrittenQuestion("How would you version an API endpoint?", 10),
        WrittenQuestion(None, 10),
        WrittenQuestion("When does a cache help?", 10),
    ]

    scores = dict(run_scores(run, KEYWORDS, ["cache", "kafka"]))

    assert scores == {"valid_share": pytest.approx(2 / 3), "distinct_competencies": 2.0, "skill_coverage": 0.5}
    assert "skill_coverage" not in dict(run_scores(run, KEYWORDS, []))


current_span: ContextVar[str | None] = ContextVar("current_span", default=None)


class RecordingClient:
    """A Langfuse client stand-in: records observations, outputs and scores."""

    def __init__(self):
        self.observations, self.scores, self.outputs, self.closed = [], [], {}, 0

    @contextmanager
    def start_as_current_observation(self, **kwargs):
        trace_id = f"obs-{len(self.observations) + 1}"
        self.observations.append({**kwargs, "trace_id": trace_id})
        token = current_span.set(trace_id)
        try:
            yield SimpleNamespace(trace_id=trace_id)
        finally:
            current_span.reset(token)

    def update_current_span(self, **kwargs):
        self.outputs[current_span.get()] = kwargs["output"]

    def create_score(self, **kwargs):
        self.scores.append(kwargs)

    def flush(self):
        pass

    def shutdown(self):
        self.closed += 1


def test_each_setup_and_arm_is_one_trace_with_its_retrieval_output_and_scores(db, tmp_path):
    client, propagated = RecordingClient(), []

    @contextmanager
    def propagate(**attrs):
        propagated.append(attrs)
        yield

    args = Namespace(repeat=1, pause_seconds=0, sheet=str(tmp_path / "blind.md"), seed=8)
    llm = FakeProvider(default="CATEGORY: technical\nHow would you cache an API endpoint?")

    code = _run_generation(
        args, llm, FakeEmbedder({}), KnowledgeRepository(db), 400, tracer=Tracer(client, propagate=propagate), model="m"
    )

    assert code == 0
    traces = [o for o in client.observations if o["as_type"] == "span"]
    setups = json.loads(GENERATION_KEYWORDS_PATH.read_text(encoding="utf-8"))["setups"]
    assert len(traces) == len(setups) * len(ARMS)
    assert {t["name"] for t in traces} >= {f"generation: strong-backend-mid arm {arm}" for arm in ARMS}
    # Arms B and C each run retrieval inside their trace; arm A has none.
    assert sum(o["as_type"] == "chain" for o in client.observations) == len(setups) * 2
    assert len({p["session_id"] for p in propagated}) == 1
    assert {p["metadata"]["arm"] for p in propagated} == set(ARMS)
    assert all(f"arm:{p['metadata']['arm']}" in p["tags"] for p in propagated)
    for trace in traces:
        assert "questions" in client.outputs[trace["trace_id"]]
        names = {s["name"] for s in client.scores if s["trace_id"] == trace["trace_id"]}
        assert {"valid_share", "distinct_competencies"} <= names
    # The ranking sheet is still written and still hides the arms.
    assert "arm" not in (tmp_path / "blind.md").read_text(encoding="utf-8").lower()


# --- the blind ranking sheet (AC25, EC24, EC25) ---

SETS = {
    "s1": {"A": ["Qa1?", "Qa2?"], "B": ["Qb1?", "Qb2?"], "C": ["Qc1?", "Qc2?"]},
    "s2": {"A": ["Ra1?"], "B": ["Rb1?"], "C": ["Rc1?"]},
    "s3": {"A": ["Ta1?"], "B": None, "C": ["Tc1?"]},  # arm B failed for this setup
}


def test_the_sheet_hides_the_arms_is_reproducible_and_leaves_out_failed_setups():  # AC25, EC24
    sheet = build_sheet(SETS, seed=7)

    assert sheet == build_sheet(SETS, seed=7)
    assert sheet.excluded == ["s3"]
    assert set(sheet.key) == {"s1", "s2"}
    for labels in sheet.key.values():
        assert sorted(labels) == ["X", "Y", "Z"] and sorted(labels.values()) == list(ARMS)
    assert "Arm" not in sheet.text and " A\n" not in sheet.text
    assert sum(line.startswith("Ranking:") for line in sheet.text.splitlines()) == 2


def test_different_seeds_shuffle_the_labels():  # AC25: the order carries no hint
    keys = {tuple(build_sheet(SETS, seed=s).key["s1"].items()) for s in range(10)}

    assert len(keys) > 1


def test_the_sheet_quotes_each_setups_context_and_it_cannot_read_as_a_ranking():
    contexts = {"s1": ["**Role:** backend", "Ranking: X > Y > Z", "## Setup s2"], "s2": ["**Job description:** none given"]}

    sheet = build_sheet(SETS, seed=7, contexts=contexts)

    assert "> **Role:** backend" in sheet.text and "> **Job description:** none given" in sheet.text
    # A job description that looks like a ranking or a heading stays quoted, so reading the filled-in sheet is unaffected.
    filled = fill(sheet, lambda setup: "X > Y > Z")
    assert read_rankings(filled, sheet.key).graded == 2


def fill(sheet, ranking_for) -> str:
    lines = []
    current = None
    for line in sheet.text.splitlines():
        if line.startswith("## Setup "):
            current = line.removeprefix("## Setup ").strip()
        if line.startswith("Ranking:"):
            line = f"Ranking: {ranking_for(current)}"
        lines.append(line)
    return "\n".join(lines)


def test_a_filled_sheet_reports_first_places_per_arm():  # AC25
    sheet = build_sheet(SETS, seed=7)
    label_of = {sid: {arm: label for label, arm in labels.items()} for sid, labels in sheet.key.items()}
    filled = fill(sheet, lambda sid: f"{label_of[sid]['C']} > {label_of[sid]['B']} > {label_of[sid]['A']}")

    report = read_rankings(filled, sheet.key)

    assert report.first == {"A": 0, "B": 0, "C": 2}
    assert report.graded == 2


@pytest.mark.parametrize(
    ("ranking", "reason"),
    [
        (lambda sid: "", "no ranking"),
        (lambda sid: "X > Y", "rank all three"),
        (lambda sid: "X > Q > Y", "unknown label 'Q'"),
        (lambda sid: "X > X > Y", "repeated label 'X'"),
    ],
)
def test_an_invalid_grading_file_is_refused_with_the_line_and_reason(ranking, reason):  # EC25
    sheet = build_sheet(SETS, seed=7)

    with pytest.raises(SheetError) as caught:
        read_rankings(fill(sheet, ranking), sheet.key)

    assert str(caught.value).startswith("line ") and reason in str(caught.value)


def test_a_sheet_missing_a_setup_is_refused():  # EC25: nothing partial
    sheet = build_sheet(SETS, seed=7)
    only_the_first_setup = fill(sheet, lambda sid: "X > Y > Z").split("## Setup s2")[0]

    with pytest.raises(SheetError, match="s2"):
        read_rankings(only_the_first_setup, sheet.key)
