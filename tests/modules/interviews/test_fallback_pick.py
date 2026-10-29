import random

import pytest

from app.core.errors import NotEnoughQuestionsError
from app.modules.interviews.interviews_constants import InterviewType, JobRole, Level, QuestionCategory
from app.modules.interviews.interviews_utils import pick_fallback_question


@pytest.fixture
def fixture_bank(make_bank_question):
    return [
        make_bank_question("b1"),
        make_bank_question("b2"),
        make_bank_question("b-senior", levels=["senior"]),
        make_bank_question("t1", "technical"),
        make_bank_question("t2", "technical"),
        make_bank_question("t-frontend", "technical", roles=["frontend"]),
    ]


def pick(
    bank,
    *,
    role=JobRole.backend,
    level=Level.junior,
    interview_type=InterviewType.technical,
    position=1,
    used=frozenset(),
    seed=1,
):
    return pick_fallback_question(bank, role, level, interview_type, position, used, random.Random(seed))


def test_picks_an_eligible_question_of_the_interview_type(fixture_bank):  # AC8
    for seed in range(20):
        q = pick(fixture_bank, seed=seed)
        assert q.type == QuestionCategory.technical
        assert q.id in {"t1", "t2"}  # never the frontend-only one for a backend role


def test_general_and_role_specific_questions_are_both_eligible(fixture_bank):  # AC8
    ids = {pick(fixture_bank, role=JobRole.frontend, seed=s).id for s in range(40)}

    assert ids == {"t1", "t2", "t-frontend"}


def test_level_must_match(fixture_bank):  # AC8
    ids = {pick(fixture_bank, interview_type=InterviewType.behavioral, seed=s).id for s in range(40)}

    assert ids == {"b1", "b2"}


def test_used_bank_questions_are_never_picked_again(fixture_bank):  # AC8, EC4
    assert pick(fixture_bank, used={"t1"}).id == "t2"


@pytest.mark.parametrize(
    ("position", "category"), [(1, "behavioral"), (2, "technical"), (3, "behavioral"), (4, "technical")]
)
def test_mixed_alternates_starting_with_behavioral(fixture_bank, position, category):  # AC8
    assert pick(fixture_bank, interview_type=InterviewType.mixed, position=position).type == category


def test_same_seed_same_pick(fixture_bank):
    assert pick(fixture_bank, seed=7).id == pick(fixture_bank, seed=7).id


def test_nothing_left_raises(fixture_bank):
    with pytest.raises(NotEnoughQuestionsError):
        pick(fixture_bank, used={"t1", "t2"})
