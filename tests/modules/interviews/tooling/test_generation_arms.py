"""The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).

C: interviewer_v7 with job-description vector notes, no profile (the baseline). D: interviewer_v8 with the setup's
synthetic profile and the same job-description notes (the prompt change only). E: v8 with the profile and quota-merged
notes (prompt and query). `--arms` picks which run; the blind sheet labels any number of arms.
"""

# `corpus` and `lf` are pytest fixtures imported from test_generation_eval.py: using them as test parameters is how
# pytest injects them, not a redefinition.
# ruff: noqa: F811

import argparse
import json

import pytest

from app.core.ai.fake import FakeEmbedder
from app.core.ai.provider import LLMResult
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V7_PROMPT_VERSION,
    INTERVIEWER_V8_PROMPT_VERSION,
    RETRIEVAL_PROFILE_SLOTS,
)
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.tooling.interviews_rag_evals import (
    ALL_ARMS,
    DEFAULT_ARMS,
    GENERATION_PROFILES_PATH,
    SheetError,
    build_sheet,
    load_generation_profiles,
    parse_arms,
    read_rankings,
    run_generation,
)
from tests.modules.interviews.tooling.test_generation_eval import (
    SETUP_IDS,
    corpus,  # noqa: F401 (a fixture)
    lf,  # noqa: F401 (a fixture)
    quiet,
)


class RecordingWriter:
    """A fake LLM that keeps every prompt, answering each main question with a new valid one."""

    def __init__(self):
        self.prompts: list[list] = []

    def complete(self, messages, **_):
        self.prompts.append(messages)
        category = "behavioral" if "mock behavioral interview" in messages[0].content else "technical"
        text = f"CATEGORY: {category}\nHow would you handle situation number {len(self.prompts)}?"
        return LLMResult(
            text=text, model="fake", prompt_tokens=200, completion_tokens=12, latency_ms=5, finish_reason="stop", attempts=1
        )


# --- --arms ---


def test_the_arms_and_the_default_run():
    assert ALL_ARMS == ("A", "B", "C", "D", "E")
    assert DEFAULT_ARMS == ("A", "B", "C")  # today's run, unchanged unless D or E is asked for


@pytest.mark.parametrize(
    ("text", "arms"),
    [("C,D,E", ("C", "D", "E")), ("e, c", ("C", "E")), ("A,B,C,D,E", ALL_ARMS)],
)
def test_arms_are_parsed_case_insensitively_in_a_fixed_order(text, arms):
    assert parse_arms(text) == arms


@pytest.mark.parametrize("text", ["C,F", "C,C", "C", "", "C,,D"])
def test_unknown_repeated_or_single_arms_are_refused(text):
    with pytest.raises(argparse.ArgumentTypeError):
        parse_arms(text)


# --- the sheet for any number of arms ---


@pytest.mark.parametrize("arms", [("C", "D", "E"), ALL_ARMS, ("C", "D")])
def test_the_sheet_labels_every_selected_arm_once_and_keeps_the_key_apart(arms):
    sets = {"s1": {arm: [f"{arm} question?"] for arm in arms}}

    sheet = build_sheet(sets, seed=8, arms=arms)

    [mapping] = sheet.key.values()
    assert sorted(mapping.values()) == sorted(arms) and len(mapping) == len(arms)
    for arm in arms:
        assert f"{arm} question?" in sheet.text
    assert not any(f"### {arm}\n" in sheet.text for arm in arms if arm not in mapping)
    assert f"rank the {len(arms)} question sets" in sheet.text


def test_a_ranking_must_name_every_label_of_its_setup():
    key = {"s1": {"X": "C", "Y": "D", "Z": "E", "V": "A", "W": "B"}}

    with pytest.raises(SheetError, match="rank all five"):
        read_rankings("## Setup s1\nRanking: X > Y > Z\n", key)
    report = read_rankings("## Setup s1\nRanking: W > X > Y > Z > V\n", key)
    assert report.first == {"A": 0, "B": 1, "C": 0, "D": 0, "E": 0}


# --- a run with --arms C,D,E ---


def test_every_existing_setup_has_a_valid_synthetic_profile():
    profiles = load_generation_profiles()

    assert set(SETUP_IDS) <= set(profiles)


def run(db, tracer, sheet, writer, embedder, arms):
    args = argparse.Namespace(
        repeat=1, pause_seconds=0, sheet=str(sheet), seed=8, note=None, arms=arms
    )
    return run_generation(args, writer, embedder, KnowledgeRepository(db), 400, tracer=tracer, model="m")


def test_arms_c_d_e_are_one_run_each_with_their_prompt_and_profile(db, corpus, lf, tmp_path):  # AC12
    writer, embedder = RecordingWriter(), FakeEmbedder()

    assert run(db, quiet(lf), tmp_path / "blind.md", writer, embedder, ("C", "D", "E")) == 0

    runs = lf.experiments
    assert [r["metadata"]["arm"] for r in runs] == ["C", "D", "E"]
    versions = {r["metadata"]["arm"]: r["metadata"]["prompt.interviewer"] for r in runs}
    assert versions == {"C": INTERVIEWER_V7_PROMPT_VERSION, "D": INTERVIEWER_V8_PROMPT_VERSION, "E": INTERVIEWER_V8_PROMPT_VERSION}
    assert all(r["metadata"]["profile_slots"] == str(RETRIEVAL_PROFILE_SLOTS) for r in runs)
    with_profile = [p for p in writer.prompts if "<candidate_profile>" in p[1].content]
    without = [p for p in writer.prompts if "<candidate_profile>" not in p[1].content]
    assert len(with_profile) == 2 * len(without)  # D and E carry it, C never does
    # E's retrieval embeds the job description and the profile's short items in one call; C and D the job description.
    assert {len(call.texts) for call in embedder.calls} == {1, 2}
    key = json.loads((tmp_path / "blind.key.json").read_text(encoding="utf-8"))
    assert all(sorted(mapping.values()) == ["C", "D", "E"] for mapping in key.values())


def test_without_arms_the_run_is_todays_three_arms(db, corpus, lf, tmp_path):
    writer = RecordingWriter()
    args = argparse.Namespace(repeat=1, pause_seconds=0, sheet=str(tmp_path / "b.md"), seed=8, note=None)

    run_generation(args, writer, FakeEmbedder(), KnowledgeRepository(db), 400, tracer=quiet(lf), model="m")

    assert [r["metadata"]["arm"] for r in lf.experiments] == list(DEFAULT_ARMS)
    assert not any("<candidate_profile>" in p[1].content for p in writer.prompts)


def test_the_profiles_file_is_where_the_runner_reads_it():
    assert GENERATION_PROFILES_PATH.name == "generation_eval_profiles.json" and GENERATION_PROFILES_PATH.exists()


# --- Step 9b: the profile metrics in a run ---


def test_profile_arms_add_the_injection_and_mismatch_setups(db, corpus, lf, tmp_path):
    run(db, quiet(lf), tmp_path / "blind.md", RecordingWriter(), FakeEmbedder(), ("C", "D", "E"))

    key = json.loads((tmp_path / "blind.key.json").read_text(encoding="utf-8"))
    assert {"profile-injection-backend-mid", "profile-mismatch-backend-mid"} <= set(key)


def test_without_profile_arms_the_extra_setups_are_not_run(db, corpus, lf, tmp_path):
    run(db, quiet(lf), tmp_path / "blind.md", RecordingWriter(), FakeEmbedder(), ("A", "C"))

    key = json.loads((tmp_path / "blind.key.json").read_text(encoding="utf-8"))
    assert set(key) == set(SETUP_IDS)


def test_every_arm_including_c_is_scored_against_the_setups_profile(db, corpus, lf, tmp_path):  # AC12
    run(db, quiet(lf), tmp_path / "blind.md", RecordingWriter(), FakeEmbedder(), ("C", "D", "E"))

    per_setup = lf.item_scores()
    for arm_scores in ("profile_only_mention_share", "presumption_flags", "profile_notes"):
        assert {s["name"] for s in per_setup} >= {arm_scores}
    injection = [s for s in per_setup if s["name"] == "injection_ignored"]
    assert len(injection) == 3  # the injection setup, once per arm
    run_names = {s["name"] for s in lf.run_scores}
    assert {"profile_only_mention_share_mean", "presumption_flags_total", "profile_notes_mean"} <= run_names


def test_the_console_reports_the_profile_table_and_refuses_the_guard_below_three_repeats(
    db, corpus, lf, tmp_path, capsys
):  # AC13
    run(db, quiet(lf), tmp_path / "blind.md", RecordingWriter(), FakeEmbedder(), ("C", "D", "E"))

    out = capsys.readouterr().out
    assert "profile_only_mentions" in out and "notes_overlap_vs_C" in out
    assert "guard D: refused" in out and "guard E: refused" in out and "--repeat 3" in out
