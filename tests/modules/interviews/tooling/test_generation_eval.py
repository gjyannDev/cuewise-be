"""`run_generation` as Langfuse experiment runs (langfuse-experiments Step 11; AC16, AC22, EC4, EC14, EC15).

Each arm (A no notes, B filter notes, C vector notes) is one run of the dataset of setups per repeat. The fake writer
answers every main question with a new, valid question in the interview's category, so the blind sheet is complete.
A one-note corpus gives the backend setups reference notes; the other setups get none.
"""

import json
from argparse import Namespace
from contextlib import nullcontext

import pytest

from app.core.ai.fake import FakeEmbedder
from app.core.ai.provider import LLMResult, LLMServerError
from app.core.ai.tracing import Tracer
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V5_PROMPT_VERSION,
    INTERVIEWER_V7_PROMPT_VERSION,
    RETRIEVAL_MIN_SIMILARITY,
)
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.services.interviews_knowledge_service import ingest_corpus
from app.modules.interviews.tooling import interviews_rag_evals as rag_module
from app.modules.interviews.tooling.interviews_rag_evals import (
    ARMS,
    GENERATION_KEYWORDS_PATH,
    run_generation,
)
from app.modules.interviews.utils.interviews_knowledge_utils import parse_note
from tests.fake_langfuse import FakeLangfuse

SETUPS = json.loads(GENERATION_KEYWORDS_PATH.read_text(encoding="utf-8"))["setups"]
SETUP_IDS = sorted(SETUPS)
BACKEND = ("long-history-backend-senior", "strong-backend-mid")


class Writer:
    """A fake LLM: a new, valid main question per call; it can fail every call that carries reference notes."""

    def __init__(self, fail_with_notes=False):
        self.fail_with_notes, self.count = fail_with_notes, 0

    def complete(self, messages, **_):
        if self.fail_with_notes and any("<reference_notes>" in m.content for m in messages):
            raise LLMServerError("down", status_code=503)
        self.count += 1
        category = "behavioral" if "mock behavioral interview" in messages[0].content else "technical"
        text = f"CATEGORY: {category}\nHow would you handle situation number {self.count}?"
        return LLMResult(text=text, model="fake", prompt_tokens=200, completion_tokens=12, latency_ms=5, finish_reason="stop", attempts=1)


@pytest.fixture
def corpus(db):
    text = "---\nroles: backend\nlevels: mid, senior\nsource: user\n---\n## API design\nProbe versioning and errors.\n"
    ingest_corpus(parse_note("api.md", text).chunks, FakeEmbedder(), KnowledgeRepository(db))


@pytest.fixture
def lf(monkeypatch):
    monkeypatch.setattr(rag_module, "git_commit", lambda: "abc1234")
    return FakeLangfuse()


def quiet(client):
    return Tracer(client, propagate=lambda **_: nullcontext())


def run(db, tracer, sheet, provider=None, **overrides):
    args = Namespace(**({"repeat": 1, "pause_seconds": 0, "sheet": str(sheet), "seed": 8, "note": None} | overrides))
    return run_generation(args, provider or Writer(), FakeEmbedder(), KnowledgeRepository(db), 400, tracer=tracer, model="m")


def test_each_arm_is_one_run_of_the_setups(db, corpus, lf, tmp_path):  # AC16
    assert run(db, quiet(lf), tmp_path / "blind.md", note="v6 notes block") == 0

    runs = lf.experiments
    assert [r["metadata"]["arm"] for r in runs] == list(ARMS)
    assert all(r["item_ids"] == [f"generation:{s}" for s in SETUP_IDS] for r in runs)
    prompts = {"A": INTERVIEWER_V5_PROMPT_VERSION, "B": INTERVIEWER_V7_PROMPT_VERSION, "C": INTERVIEWER_V7_PROMPT_VERSION}
    for r in runs:
        arm = r["metadata"]["arm"]
        assert r["run_name"].startswith(f"generation/{prompts[arm]}/m/") and r["run_name"].endswith(f"/r1/arm-{arm}")
        assert r["metadata"]["prompt.interviewer"] == prompts[arm] and r["metadata"]["note"] == "v6 notes block"
        assert r["metadata"]["threshold"] == str(RETRIEVAL_MIN_SIMILARITY) and r["metadata"]["notes_fingerprint"]
    stored = lf.datasets["interviews-eval/generation"]
    first = stored[f"generation:{SETUP_IDS[0]}"]
    assert "setup" in first["input"] and first["metadata"]["skills"] == SETUPS[SETUP_IDS[0]]


def test_each_setup_carries_the_generation_scores_and_each_arm_its_means(db, corpus, lf, tmp_path):  # AC16
    run(db, quiet(lf), tmp_path / "blind.md")

    run_a = lf.experiments[0]["run_name"]
    for setup in SETUP_IDS:
        names = {s["name"] for s in lf.item_scores(run_a) if s["trace_id"].endswith(f"generation:{setup}")}
        assert {"valid_share", "distinct_competencies", "prompt_tokens", "start_ms", "errored"} <= names
        assert ("skill_coverage" in names) == bool(SETUPS[setup])
    means = {s["name"] for s in lf.run_scores if s["run_name"] == run_a}
    assert {"valid_share_mean", "distinct_competencies_mean", "skill_coverage_mean", "prompt_tokens_mean",
            "start_ms_mean", "errored_count"} <= means
    assert lf.run_score(run_a, "valid_share_mean")["value"] == 1.0


def test_retrieval_runs_inside_the_b_and_c_results_only(db, corpus, lf, tmp_path):
    run(db, quiet(lf), tmp_path / "blind.md")

    steps = [o for o in lf.observations if o.get("as_type") == "chain" and o.get("name") == "retrieval"]
    assert len(steps) == 2 * len(SETUP_IDS)


def table_without_timings(out):
    """The console with each arm row's start_ms (wall-clock time) dropped, and without the last line."""
    lines = out.rstrip("\n").splitlines()[:-1]
    return [line.rsplit(maxsplit=1)[0] if line[:2] in ("A ", "B ", "C ") else line for line in lines]


def test_the_console_sheet_and_key_are_the_same_with_and_without_langfuse(db, corpus, lf, tmp_path, capsys):  # AC7, AC16
    sheet = tmp_path / "blind.md"
    run(db, Tracer(None), sheet)
    keyless = capsys.readouterr().out
    keyless_sheet, keyless_key = sheet.read_text(encoding="utf-8"), sheet.with_suffix(".key.json").read_text(encoding="utf-8")
    run(db, quiet(lf), sheet)
    keyed = capsys.readouterr().out

    assert table_without_timings(keyless) == table_without_timings(keyed)
    assert sheet.read_text(encoding="utf-8") == keyless_sheet
    assert sheet.with_suffix(".key.json").read_text(encoding="utf-8") == keyless_key
    assert keyless.rstrip("\n").splitlines()[-1] == "Langfuse: not recorded (no LANGFUSE keys set)."
    assert keyed.rstrip("\n").splitlines()[-1].startswith("Langfuse runs: generation/")
    assert "rank the sheet before opening these runs" in keyed.rstrip("\n").splitlines()[-1].lower()


def test_the_traces_file_maps_each_setup_and_arm_to_its_result(db, corpus, lf, tmp_path):  # AC16
    run(db, quiet(lf), tmp_path / "blind.md")

    traces = json.loads((tmp_path / "blind.traces.json").read_text(encoding="utf-8"))
    names = {r["metadata"]["arm"]: r["run_name"] for r in lf.experiments}
    assert traces == {s: {arm: f"trace-{names[arm]}-generation:{s}" for arm in ARMS} for s in SETUP_IDS}


def test_without_keys_no_traces_file_is_written_and_a_stale_one_is_removed(db, corpus, tmp_path):  # EC14
    sheet = tmp_path / "blind.md"
    stale = sheet.with_suffix(".traces.json")
    stale.write_text('{"old": {"A": "trace-from-an-earlier-run"}}', encoding="utf-8")

    run(db, Tracer(None), sheet)

    assert sheet.exists() and sheet.with_suffix(".key.json").exists() and not stale.exists()


def test_an_arm_failing_for_a_setup_leaves_it_off_the_sheet_but_recorded(db, corpus, lf, tmp_path, capsys):  # EC4, EC15
    run(db, quiet(lf), tmp_path / "blind.md", provider=Writer(fail_with_notes=True))

    out = capsys.readouterr().out
    assert "left out (an arm failed): " + ", ".join(BACKEND) in out
    run_b = lf.experiments[1]["run_name"]
    failed = {s["name"]: s["value"] for s in lf.item_scores(run_b) if s["trace_id"].endswith(f"generation:{BACKEND[1]}")}
    assert failed["errored"] == 1.0
    sheet = (tmp_path / "blind.md").read_text(encoding="utf-8")
    assert all(f"## Setup {s}" not in sheet for s in BACKEND)


def test_generation_stops_before_any_call_when_no_notes_are_ingested(db, lf, tmp_path, capsys):  # EC8 (generation too)
    writer = Writer()

    assert run(db, quiet(lf), tmp_path / "blind.md", provider=writer) == 1

    assert "ingest" in capsys.readouterr().out.lower() and writer.count == 0 and lf.experiments == []


# --- ranking posts your judgement onto each arm's result (Step 12; AC17, AC23, EC12, EC13, EC16, EC17, EC23, EC24) ---


def generated(db, lf, tmp_path):
    """A recorded generation run: its sheet, key and traces file in tmp_path."""
    sheet = tmp_path / "blind.md"
    run(db, quiet(lf), sheet)
    return sheet


def fill(sheet, ranking="X > Y > Z", extra=None):
    """Ranks every setup; `extra` maps (setup, label) to lines put right after that set's empty Rating/Note lines."""
    out, setup, label = [], None, None
    for line in sheet.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Setup "):
            setup = line.removeprefix("## Setup ").strip()
        elif line.startswith("### "):
            label = line.removeprefix("### ").strip()
        if line == "Ranking:":
            line = f"Ranking: {ranking}"
        elif line in ("Rating:", "Note:") and extra and (setup, label) in extra:
            line = extra[(setup, label)].get(line, line)
        out.append(line)
    sheet.write_text("\n".join(out), encoding="utf-8")


def arm_of(sheet, setup, label):
    return json.loads(sheet.with_suffix(".key.json").read_text(encoding="utf-8"))[setup][label]


def trace_for(sheet, setup, arm):
    return json.loads(sheet.with_suffix(".traces.json").read_text(encoding="utf-8"))[setup][arm]


def posted(lf, name):
    return [s for s in lf.scores if s.get("name") == name and "run_name" not in s]


def test_ranking_posts_each_arms_position_with_a_stable_id(db, corpus, lf, tmp_path, capsys):  # AC17
    sheet = generated(db, lf, tmp_path)
    fill(sheet, "Y > X > Z")

    assert rag_module.run_ranking(sheet, tracer=quiet(lf)) == 0

    ranks = posted(lf, "human_rank")
    assert len(ranks) == 3 * len(SETUP_IDS)
    for setup in SETUP_IDS:
        for label, position in (("Y", 1), ("X", 2), ("Z", 3)):
            trace_id = trace_for(sheet, setup, arm_of(sheet, setup, label))
            [score] = [s for s in ranks if s["trace_id"] == trace_id]
            assert (score["value"], score["score_id"]) == (float(position), f"human_rank-{trace_id}")
    out = capsys.readouterr().out
    assert f"graded setups: {len(SETUP_IDS)}" in out and f"posted {3 * len(SETUP_IDS)} ranks" in out


def test_a_rating_posts_the_rubric_scores_and_their_mean_and_a_note_becomes_the_comment(db, corpus, lf, tmp_path):  # AC23
    sheet = generated(db, lf, tmp_path)
    setup = SETUP_IDS[0]
    fill(sheet, extra={
        (setup, "X"): {"Rating:": "Rating: 4 5 3 4", "Note:": "Note: clear, but two questions overlap"},
        (setup, "Y"): {"Rating:": "Rating: 2, -, 3, 1"},
    })

    rag_module.run_ranking(sheet, tracer=quiet(lf))

    x_trace = trace_for(sheet, setup, arm_of(sheet, setup, "X"))
    y_trace = trace_for(sheet, setup, arm_of(sheet, setup, "Y"))
    on = {s["name"]: s for s in lf.scores if s.get("trace_id") == x_trace and "run_name" not in s}
    assert [on[n]["value"] for n in ("human_fit", "human_relevance", "human_variety", "human_specificity")] == [4, 5, 3, 4]
    assert on["human_score"]["value"] == 4.0 and on["human_score"]["score_id"] == f"human_score-{x_trace}"
    assert on["human_rank"]["comment"] == "clear, but two questions overlap"
    on_y = {s["name"]: s["value"] for s in lf.scores if s.get("trace_id") == y_trace and "run_name" not in s}
    assert "human_relevance" not in on_y and on_y["human_score"] == pytest.approx(2.0)  # "-" is left out
    z_trace = trace_for(sheet, setup, arm_of(sheet, setup, "Z"))
    assert {s["name"] for s in lf.scores if s.get("trace_id") == z_trace and "run_name" not in s} == {"human_rank"}  # EC24


def test_reading_the_sheet_twice_posts_the_same_score_ids(db, corpus, lf, tmp_path):  # EC13
    sheet = generated(db, lf, tmp_path)
    fill(sheet)

    rag_module.run_ranking(sheet, tracer=quiet(lf))
    first = sorted(s["score_id"] for s in posted(lf, "human_rank"))
    rag_module.run_ranking(sheet, tracer=quiet(lf))

    assert sorted({s["score_id"] for s in posted(lf, "human_rank")}) == first


@pytest.mark.parametrize("rating", ["Rating: 4 5 3", "Rating: 6 5 3 4", "Rating: 4 5 three 4", "Rating: - 5 3 4"])
def test_a_malformed_rating_refuses_the_sheet_and_posts_nothing(db, corpus, lf, tmp_path, capsys, rating):  # EC23
    sheet = generated(db, lf, tmp_path)
    fill(sheet, extra={(SETUP_IDS[0], "X"): {"Rating:": rating}})

    assert rag_module.run_ranking(sheet, tracer=quiet(lf)) == 1

    assert "grading file refused: line" in capsys.readouterr().out and posted(lf, "human_rank") == []


def test_without_a_traces_file_or_langfuse_the_tally_still_prints(db, corpus, lf, tmp_path, capsys):  # EC12
    sheet = generated(db, lf, tmp_path)
    fill(sheet)

    assert rag_module.run_ranking(sheet, tracer=Tracer(None)) == 0
    assert "nothing posted (no LANGFUSE keys set)" in capsys.readouterr().out
    sheet.with_suffix(".traces.json").unlink()
    assert rag_module.run_ranking(sheet, tracer=quiet(lf)) == 0

    out = capsys.readouterr().out
    assert "arm A ranked first" in out and "no traces file" in out and posted(lf, "human_rank") == []


def test_an_arm_without_a_recorded_result_is_skipped_and_counted(db, corpus, lf, tmp_path, capsys):  # EC16
    sheet = generated(db, lf, tmp_path)
    fill(sheet)
    traces_path = sheet.with_suffix(".traces.json")
    traces = json.loads(traces_path.read_text(encoding="utf-8"))
    del traces[SETUP_IDS[0]]["A"]
    traces_path.write_text(json.dumps(traces), encoding="utf-8")

    rag_module.run_ranking(sheet, tracer=quiet(lf))

    assert len(posted(lf, "human_rank")) == 3 * len(SETUP_IDS) - 1
    assert "1 not posted (no recorded result)" in capsys.readouterr().out


def test_a_rejected_post_lets_the_rest_go_on_and_is_counted(db, corpus, tmp_path, monkeypatch, capsys):  # EC17
    monkeypatch.setattr(rag_module, "git_commit", lambda: "abc1234")
    sheet = generated(db, FakeLangfuse(), tmp_path)
    fill(sheet)

    assert rag_module.run_ranking(sheet, tracer=quiet(FakeLangfuse(fail_scores=True))) == 0

    out = capsys.readouterr().out
    assert "arm A ranked first" in out and f"{3 * len(SETUP_IDS)} not posted (Langfuse rejected them;" in out
