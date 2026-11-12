"""The run helpers shared by every eval task moved onto Langfuse experiments (langfuse-experiments Steps 2 and 3).

Pure helpers (git state, metadata, names, fingerprint, the run description, the final console line) and `run_cases`,
which runs the cases as one Langfuse experiment run or locally. The fake Langfuse client records what the SDK would be
told; no test touches the network or git itself.
"""

import subprocess
from contextlib import nullcontext
from types import SimpleNamespace

import pytest

from app.core.ai.tracing import ExperimentRun, Tracer
from app.modules.interviews.tooling.interviews_eval_runs import (
    final_line,
    git_commit,
    notes_fingerprint,
    run_cases,
    run_description,
    run_metadata,
    run_name,
)
from tests.fake_langfuse import FakeLangfuse

# --- run metadata (AC2) -----------------------------------------------------------------------------------------


def test_metadata_values_are_all_strings_and_a_missing_value_is_a_dash():  # AC2
    meta = run_metadata(
        task="decide", commit="abc1234", model=None, prompts={"decision": "follow_up_decision_v1"}, repeat=2,
        flags={"reasoning_effort": None, "notes": "on"}, extra={"threshold": 0.55, "dimensions": 768},
    )

    assert meta == {
        "task": "decide", "commit": "abc1234", "model": "-", "prompt.decision": "follow_up_decision_v1", "repeat": "2",
        "flag.reasoning_effort": "-", "flag.notes": "on", "threshold": "0.55", "dimensions": "768",
    }
    assert all(isinstance(v, str) for v in meta.values())


# --- git state (EC10) -------------------------------------------------------------------------------------------


def fake_git(head="abc1234\n", status="", fail=None):
    calls = []

    def run(args, **kwargs):
        calls.append((args, kwargs))
        if fail is not None:
            raise fail
        out = head if "rev-parse" in args else status
        return subprocess.CompletedProcess(args, 0, stdout=out, stderr="")

    return run, calls


def test_a_clean_tree_gives_the_short_hash_read_without_touching_the_index():  # AC2
    run, calls = fake_git()

    assert git_commit(run=run) == "abc1234"
    assert all(args[:2] == ["git", "--no-optional-locks"] for args, _ in calls)
    assert all(kwargs.get("shell") is not True for _, kwargs in calls)


def test_uncommitted_changes_mark_the_commit_dirty():  # EC10
    run, _ = fake_git(status=" M app/x.py\n")

    assert git_commit(run=run) == "abc1234-dirty"


@pytest.mark.parametrize(
    "fail",
    [FileNotFoundError("git"), subprocess.CalledProcessError(128, "git"), subprocess.TimeoutExpired("git", 5)],
)
def test_git_missing_or_failing_gives_unknown(fail):  # EC10
    run, _ = fake_git(fail=fail)

    assert git_commit(run=run) == "unknown"


# --- names, fingerprint, description (EC5, EC20, EC21) ----------------------------------------------------------


def test_each_repeat_gets_its_own_run_name_so_langfuse_never_merges_them():  # EC5
    names = {run_name("decide", "20261112-101500", repeat) for repeat in (1, 2, 3)}

    assert len(names) == 3
    assert run_name("generation", "20261112-101500", 1, "C") != run_name("generation", "20261112-101500", 1, "A")


def test_a_run_name_says_what_was_tested_before_when_it_ran():  # Step 7 finding: names were only a time
    name = run_name("decide", "20261112-143059", 1, label="follow_up_decision_v2/gemini-3.5-flash-lite")

    assert name == "decide/follow_up_decision_v2/gemini-3.5-flash-lite/20261112-143059/r1"


def test_the_notes_fingerprint_changes_when_one_note_changes_but_not_with_order():
    first = notes_fingerprint(["h1", "h2", "h3"])

    assert first == notes_fingerprint(["h3", "h1", "h2"])
    assert first != notes_fingerprint(["h1", "h2", "hX"])
    assert len(first) == 12


def test_a_blank_note_gives_no_description():  # EC20
    assert run_description(None) is None
    assert run_description("   ") is None


def test_a_long_note_is_cut_to_300_characters():  # EC21
    note = run_description("x" * 400)

    assert note is not None and len(note) == 300 and note.endswith("…")
    assert run_description("  keep me  ") == "keep me"


# --- run_cases (EC1, EC2, AC3) ----------------------------------------------------------------------------------

CASES = [SimpleNamespace(id="a"), SimpleNamespace(id="b"), SimpleNamespace(id="c")]


def harness(fail_on=None, crash_on=None):
    ran: list[str] = []

    def run_one(case):
        ran.append(case.id)
        if crash_on == case.id:
            raise KeyError("a bug, not a provider error")
        return SimpleNamespace(id=case.id, ok=case.id != fail_on)

    return ran, {
        "dataset": "interviews-eval/test",
        "cases": CASES,
        "item_of": lambda case: {"id": f"test:{case.id}", "input": {"case": case.id}},
        "run_one": run_one,
        "output_of": lambda case, result: {"verdict": "PASS" if result.ok else "FAIL"},
        "scores_of": lambda result: [("case_passed", result.ok, None), ("tokens", 3, "three")],
        "run_scores_of": lambda results: [("pass_rate", sum(r.ok for r in results) / len(results))],
        "name": "test",
        "run_name": "test/r1",
        "metadata": {"task": "test"},
        "description": "why",
    }


def quiet(client):
    return Tracer(client, propagate=lambda **_: nullcontext())


def test_without_keys_every_case_runs_locally_with_no_sdk_call():  # EC1, AC8
    ran, fields = harness()

    results, record = run_cases(Tracer(None), **fields)

    assert ran == ["a", "b", "c"] and [r.id for r in results] == ["a", "b", "c"] and record is None


def test_with_keys_the_cases_become_one_run_with_their_scores():  # AC1, AC3
    lf = FakeLangfuse()
    ran, fields = harness(fail_on="b")

    _, record = run_cases(quiet(lf), **fields)

    assert ran == ["a", "b", "c"] and isinstance(record, ExperimentRun)
    [run] = lf.experiments
    assert run["description"] == "why" and run["metadata"] == {"task": "test"}
    passed = [s for s in lf.item_scores("test/r1") if s["name"] == "case_passed"]
    assert [(s["value"], s["data_type"]) for s in passed] == [(1.0, "BOOLEAN"), (0.0, "BOOLEAN"), (1.0, "BOOLEAN")]
    tokens = [s for s in lf.item_scores("test/r1") if s["name"] == "tokens"]
    assert tokens[0] == {**tokens[0], "value": 3.0, "data_type": "NUMERIC", "comment": "three"}
    assert lf.run_score("test/r1", "pass_rate")["value"] == pytest.approx(2 / 3)


def test_the_item_output_in_langfuse_is_the_readable_output_with_its_scores():  # AC3
    lf = FakeLangfuse()
    _, fields = harness(fail_on="b")

    _, record = run_cases(quiet(lf), **fields)

    assert record is not None
    output = lf.outputs[record.trace_ids["test:b"]]
    assert output["verdict"] == "FAIL"
    assert output["scores"] == {"case_passed": False, "tokens": 3}


@pytest.mark.parametrize("client", [FakeLangfuse(fail_after=1), FakeLangfuse(fail_upsert=True), FakeLangfuse(fail_run=True)])
def test_when_langfuse_fails_every_case_still_runs_exactly_once(client):  # EC2, EC3: no repeated LLM calls
    ran, fields = harness()

    results, record = run_cases(quiet(client), **fields)

    assert ran == ["a", "b", "c"] and [r.id for r in results] == ["a", "b", "c"] and record is None


def test_a_bug_in_a_case_still_stops_the_run_as_it_does_locally():  # a crash is never swallowed into a score
    ran, fields = harness(crash_on="b")

    with pytest.raises(KeyError):
        run_cases(quiet(FakeLangfuse()), **fields)

    assert ran == ["a", "b"]  # the crashing case ran once, and nothing after it


# --- the final console line (Step 3, AC7) -----------------------------------------------------------------------


def test_the_final_line_names_each_recorded_run_with_its_link():
    records = [ExperimentRun("decide/1", "e1", "https://lf/1", {}), ExperimentRun("decide/2", "e2", None, {})]

    assert final_line(records, enabled=True) == "Langfuse runs: decide/1 (https://lf/1); decide/2"


def test_the_final_line_says_why_nothing_was_recorded():
    assert final_line([None], enabled=False) == "Langfuse: not recorded (no LANGFUSE keys set)."
    assert final_line([None, None], enabled=True) == (
        "Langfuse: not recorded (Langfuse failed or the dataset could not be synced; see the warnings above)."
    )
    assert final_line([ExperimentRun("decide/1", "e1", None, {}), None], enabled=True) == (
        "Langfuse runs: decide/1; 1 of 2 runs not recorded (see the warnings above)."
    )
