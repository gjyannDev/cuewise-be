import json

import pytest

from app.modules.interviews.interviews_constants import (
    QUESTION_BANK_PATH,
    JobRole,
    Level,
    QuestionCategory,
)
from app.modules.interviews.interviews_utils import load_bank


def _entry(**overrides):
    return {
        "id": "q1",
        "text": "Tell me about a time you disagreed with a teammate.",
        "type": "behavioral",
        "roles": ["general"],
        "levels": ["junior"],
    } | overrides


def _write(tmp_path, entries):
    path = tmp_path / "questions.json"
    path.write_text(json.dumps(entries), encoding="utf-8")
    return path


def test_valid_bank_loads_typed_entries(tmp_path):  # AC14
    path = _write(tmp_path, [_entry(), _entry(id="q2", type="technical", roles=["backend"], levels=["mid", "senior"])])

    bank = load_bank(path)

    assert [q.id for q in bank] == ["q1", "q2"]
    assert bank[1].type == QuestionCategory.technical
    assert bank[1].roles == [JobRole.backend]
    assert bank[1].levels == [Level.mid, Level.senior]


@pytest.mark.parametrize(
    "bad_entries",
    [
        pytest.param([_entry(), _entry()], id="duplicate-id"),
        pytest.param([_entry(text="")], id="empty-text"),
        pytest.param([_entry(text="   ")], id="whitespace-text"),
        pytest.param([_entry(roles=["devops"])], id="unknown-role"),
        pytest.param([_entry(levels=["principal"])], id="unknown-level"),
        pytest.param([_entry(type="system_design")], id="unknown-type"),
        pytest.param([_entry(roles=[])], id="empty-roles"),
        pytest.param([_entry(levels=[])], id="empty-levels"),
        pytest.param([_entry(difficulty=3)], id="unknown-field"),  # inferred: typo'd key silently ignored
        pytest.param([], id="empty-bank"),  # inferred: every request would 409
    ],
)
def test_invalid_bank_raises_clear_error(tmp_path, bad_entries):  # AC14, EC17
    path = _write(tmp_path, bad_entries)

    with pytest.raises(ValueError, match="Invalid question bank"):
        load_bank(path)


def test_shipped_bank_covers_every_type_role_and_level():  # AC14
    bank = load_bank(QUESTION_BANK_PATH)

    assert {q.type for q in bank} == set(QuestionCategory)
    assert {role for q in bank for role in q.roles} >= set(JobRole)
    assert {level for q in bank for level in q.levels} == set(Level)
