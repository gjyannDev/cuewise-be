import itertools
import random

import pytest

from app.core.errors import NotEnoughQuestionsError
from app.modules.interviews.interviews_constants import (
    QUESTION_BANK_PATH,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
)
from app.modules.interviews.interviews_schema import BankQuestion
from app.modules.interviews.interviews_utils import load_bank, select_questions

ALL_LEVELS = list(Level)


def _q(qid, category="behavioral", roles=("general",), levels=ALL_LEVELS):
    return BankQuestion(id=qid, text=f"Question {qid}?", type=category, roles=list(roles), levels=list(levels))


def _bank(behavioral=5, technical=5):
    return [_q(f"b{i}") for i in range(behavioral)] + [_q(f"t{i}", "technical") for i in range(technical)]


def _select(bank, interview_type=InterviewType.behavioral, count=3, role=JobRole.backend, level=Level.junior, seed=1):
    return select_questions(bank, role, level, interview_type, count, random.Random(seed))


# --- single type ---


@pytest.mark.parametrize("category", [InterviewType.behavioral, InterviewType.technical])
def test_single_type_returns_count_questions_of_that_type(category):  # AC2, AC3
    picked = _select(_bank(), category, count=4)

    assert len(picked) == 4
    assert {q.type for q in picked} == {QuestionCategory(category)}


# --- eligibility ---


def test_only_questions_for_the_role_or_general_are_eligible():  # AC3, EC11
    bank = [_q("frontend-only", roles=["frontend"]), _q("backend-only", roles=["backend"]), _q("general")]

    picked = _select(bank, count=2, role=JobRole.backend)

    assert {q.id for q in picked} == {"backend-only", "general"}


def test_general_question_is_eligible_for_every_role():  # EC11
    bank = [_q("general")]

    for role in JobRole:
        assert [q.id for q in _select(bank, count=1, role=role)] == ["general"]


def test_only_questions_for_the_level_are_eligible():  # AC3
    bank = [_q("senior-only", levels=["senior"]), _q("junior-ok", levels=["intern", "junior"])]

    picked = _select(bank, count=1, level=Level.junior)

    assert [q.id for q in picked] == ["junior-ok"]


# --- no repeats ---


def test_never_picks_the_same_question_twice():  # AC3, EC12
    picked = _select(_bank(behavioral=5), count=5)

    assert len({q.id for q in picked}) == 5


# --- mixed ---


def test_mixed_with_one_question_is_behavioral():  # AC4, EC9
    picked = _select(_bank(), InterviewType.mixed, count=1)

    assert [q.type for q in picked] == [QuestionCategory.behavioral]


def test_mixed_splits_evenly_extra_behavioral_and_interleaves():  # AC4, EC9
    picked = _select(_bank(), InterviewType.mixed, count=5)

    assert [q.type for q in picked] == ["behavioral", "technical", "behavioral", "technical", "behavioral"]


def test_mixed_even_count_is_an_exact_split():  # AC4, inferred: even counts
    picked = _select(_bank(), InterviewType.mixed, count=4)

    assert [q.type for q in picked] == ["behavioral", "technical", "behavioral", "technical"]


# --- shortage ---


def test_not_enough_questions_reports_how_many_are_available():  # AC5, EC8
    with pytest.raises(NotEnoughQuestionsError) as exc_info:
        _select(_bank(behavioral=3), InterviewType.behavioral, count=4)

    assert exc_info.value.status_code == 409
    assert exc_info.value.code == "NOT_ENOUGH_QUESTIONS"
    assert exc_info.value.details == {"requested": 4, "available": 3}


def test_mixed_short_on_one_type_is_rejected_without_rebalancing():  # AC4, EC10
    # 10 questions in total, but 4 mixed needs 2 technical and only 1 exists.
    with pytest.raises(NotEnoughQuestionsError) as exc_info:
        _select(_bank(behavioral=9, technical=1), InterviewType.mixed, count=4)

    # 1 technical supports at most B,T,B = 3 questions.
    assert exc_info.value.details == {"requested": 4, "available": 3}


# --- determinism ---


def test_same_seed_gives_same_selection():  # AC15
    first = _select(_bank(behavioral=10), count=5, seed=42)
    second = _select(_bank(behavioral=10), count=5, seed=42)

    assert [q.id for q in first] == [q.id for q in second]


# --- shipped mock bank ---


@pytest.mark.parametrize(
    ("role", "level", "interview_type"),
    list(itertools.product(JobRole, Level, InterviewType)),
)
def test_shipped_bank_supports_a_five_question_session(role, level, interview_type):  # AC14
    bank = load_bank(QUESTION_BANK_PATH)

    assert len(select_questions(bank, role, level, interview_type, 5, random.Random(0))) == 5
