"""Step 3 of the feedback plan: the rubric (data) and the two prompts. Structure only; whether the wording scores well
is what the feedback evals measure."""

import json
import re

import pytest

from app.modules.interviews.ai.interviews_feedback import SECTION_LABELS
from app.modules.interviews.constants.interviews_constants import (
    CATEGORY_CRITERIA,
    FEEDBACK_ITEM_MAX_LENGTH,
    FEEDBACK_NOTE_MAX_LENGTH,
    FEEDBACK_RUBRIC_PATH,
    FEEDBACK_RUBRIC_VERSION,
    FEEDBACK_SCORE_PROMPT_VERSION,
    FEEDBACK_SUMMARY_MAX_LENGTH,
    FEEDBACK_WRITE_PROMPT_VERSION,
    PROMPTS_DIR,
    QUOTE_MAX_LENGTH,
    QUOTE_MIN_LENGTH,
    REASON_MAX_LENGTH,
    Criterion,
    InterviewType,
    JobRole,
    Level,
    LevelGroup,
    QuestionCategory,
)
from app.modules.interviews.utils.interviews_utils import (
    FEEDBACK_RUBRIC,
    load_prompt,
    load_rubric,
    render_feedback_score_prompt,
    render_feedback_write_prompt,
)

SECTIONS = ["# Role", "# Task", "# Input", "# Output", "# Constraints", "# Capabilities"]


@pytest.mark.parametrize("version", [FEEDBACK_SCORE_PROMPT_VERSION, FEEDBACK_WRITE_PROMPT_VERSION])
def test_feedback_prompts_have_the_six_sections_in_order(version):
    headings = [line for line in load_prompt(version).splitlines() if re.match(r"^# \w", line)]

    assert headings == SECTIONS


def test_every_prompt_has_its_own_role_line():  # the test fakes route calls by it (conftest)
    role_lines = [p.read_text(encoding="utf-8").splitlines()[1].split("{{")[0] for p in PROMPTS_DIR.glob("*.md")]
    feedback = [load_prompt(v).splitlines()[1].split("{{")[0] for v in (FEEDBACK_SCORE_PROMPT_VERSION, FEEDBACK_WRITE_PROMPT_VERSION)]

    for marker in feedback:
        assert len(marker) > 20 and role_lines.count(marker) == 1


def test_the_rubric_anchors_five_levels_for_every_criterion_and_both_level_groups():
    assert FEEDBACK_RUBRIC.version == FEEDBACK_RUBRIC_VERSION
    assert set(FEEDBACK_RUBRIC.criteria) == set(Criterion)
    for criterion, entry in FEEDBACK_RUBRIC.criteria.items():
        assert criterion in CATEGORY_CRITERIA[entry.category]
        assert sorted(entry.levels) == [1, 2, 3, 4, 5] and all(text.strip() for text in entry.levels.values())
        assert set(entry.expectations) == set(LevelGroup)


@pytest.mark.parametrize(
    "broken",
    [
        lambda r: r["criteria"]["structure"]["levels"].pop("5"),
        lambda r: r["criteria"].pop("clarity"),
        lambda r: r["criteria"]["depth"].update(category="behavioral"),
        lambda r: r["criteria"]["outcome"]["expectations"].pop("early"),
    ],
)
def test_a_broken_rubric_file_fails_loudly_at_load(tmp_path, broken):  # stops the app at startup, like the bank
    data = json.loads(FEEDBACK_RUBRIC_PATH.read_text(encoding="utf-8"))
    broken(data)
    path = tmp_path / "rubric.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(ValueError, match="rubric"):
        load_rubric(path)


@pytest.mark.parametrize("level", list(Level))
@pytest.mark.parametrize("interview_type", list(InterviewType))
def test_the_score_prompt_renders_fully_with_only_the_interviews_criteria(level, interview_type):
    text = render_feedback_score_prompt(role=JobRole.backend, level=level, interview_type=interview_type)

    categories = list(QuestionCategory) if interview_type == InterviewType.mixed else [QuestionCategory(interview_type)]
    wanted = {c for category in categories for c in CATEGORY_CRITERIA[category]}
    assert "{{" not in text
    assert all(f'"{c.value}"' in text for c in wanted)
    assert all(f'"{c.value}"' not in text for c in set(Criterion) - wanted)
    group = {Level.intern: LevelGroup.early, Level.junior: LevelGroup.early}.get(level, LevelGroup.experienced)
    for c in wanted:
        assert FEEDBACK_RUBRIC.criteria[c].expectations[group] in text
        assert FEEDBACK_RUBRIC.criteria[c].levels[5] in text


def test_the_score_prompt_states_the_contract_the_parser_enforces():
    text = render_feedback_score_prompt(role=JobRole.data, level=Level.mid, interview_type=InterviewType.mixed)

    assert '"enough_evidence"' in text and '"main_number"' in text and '"evidence"' in text
    assert f"{QUOTE_MIN_LENGTH} to {QUOTE_MAX_LENGTH} characters" in text
    assert f"at most {REASON_MAX_LENGTH} characters" in text
    assert "<question_thread>" in text and "<answer>" in text and "<job_description>" in text
    assert "filler" in text  # voice transcripts are judged on content (EC19)
    assert "total" in text.lower()  # no total wanted: the code computes it


@pytest.mark.parametrize("level", list(Level))
def test_the_write_prompt_renders_fully_and_states_every_label_and_limit(level):
    text = render_feedback_write_prompt(role=JobRole.mobile, level=level, interview_type=InterviewType.behavioral)

    assert "{{" not in text
    assert all(f"{label}:" in text for label in SECTION_LABELS)
    assert f"at most {FEEDBACK_SUMMARY_MAX_LENGTH} characters" in text
    assert f"at most {FEEDBACK_ITEM_MAX_LENGTH} characters" in text
    assert f"at most {FEEDBACK_NOTE_MAX_LENGTH} characters" in text
    assert "<feedback_scores>" in text
