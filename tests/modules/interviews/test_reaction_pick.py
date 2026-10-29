import random
import re

import pytest

from app.modules.interviews.interviews_constants import (
    CLOSING_REACTIONS,
    REACTION_POOLS,
    LevelGroup,
    QuestionCategory,
)
from app.modules.interviews.interviews_utils import pick_reaction

ALL_POOLS = {
    **{f"{c}/{g}": p for (c, g), p in REACTION_POOLS.items()},
    **{f"closing/{g}": p for g, p in CLOSING_REACTIONS.items()},
}
# Words that would judge the answer; a predefined reaction must stay neutral because the app can't tell good from bad.
JUDGING = {
    "great",
    "excellent",
    "perfect",
    "amazing",
    "awesome",
    "impressive",
    "brilliant",
    "correct",
    "incorrect",
    "wrong",
    "weak",
    "poor",
    "bad",
    "score",
    "grade",
    "rating",
}


def test_every_category_and_level_group_has_a_pool():  # AC23
    assert set(REACTION_POOLS) == {(c, g) for c in QuestionCategory for g in LevelGroup}
    assert set(CLOSING_REACTIONS) == set(LevelGroup)


@pytest.mark.parametrize("name", sorted(ALL_POOLS))
def test_pool_follows_the_neutral_reaction_rules(name):  # AC23
    pool = ALL_POOLS[name]

    assert len(pool) >= 5 and len(set(pool)) == len(pool)
    for reaction in pool:
        assert 0 < len(reaction) <= 120
        assert "?" not in reaction
        assert not re.search(r"\d", reaction)
        assert not set(re.findall(r"[a-z]+", reaction.lower())) & JUDGING, reaction


def pick(category=QuestionCategory.technical, level="junior", *, final=False, previous=None, seed=1):
    return pick_reaction(category, level, final=final, previous=previous, rng=random.Random(seed))


@pytest.mark.parametrize(
    ("category", "level", "group"),
    [
        ("technical", "intern", "early"),
        ("technical", "senior", "experienced"),
        ("behavioral", "junior", "early"),
        ("behavioral", "mid", "experienced"),
    ],
)
def test_pool_follows_category_and_level_group(category, level, group):  # AC24
    for seed in range(10):
        assert pick(QuestionCategory(category), level, seed=seed) in REACTION_POOLS[(category, group)]


@pytest.mark.parametrize(("level", "group"), [("intern", "early"), ("senior", "experienced")])
def test_final_answer_uses_the_closing_pool(level, group):  # AC24, EC11
    assert pick(level=level, final=True) in CLOSING_REACTIONS[group]


def test_seeded_pick_is_repeatable():  # AC24
    assert pick(seed=3) == pick(seed=3)


def test_never_repeats_the_previous_reaction():  # AC24
    pool = REACTION_POOLS[(QuestionCategory.technical, LevelGroup.early)]

    for previous in pool:
        for seed in range(10):
            assert pick(previous=previous, seed=seed) != previous


def test_a_one_entry_pool_still_works(monkeypatch):  # EC23
    only = ("Thanks for that.",)
    monkeypatch.setitem(REACTION_POOLS, (QuestionCategory.technical, LevelGroup.early), only)

    assert pick(previous="Thanks for that.") == "Thanks for that."


def test_previous_text_from_an_old_llm_reaction_is_fine():  # EC25
    assert pick(previous="That was a practical way to settle it, written by the old LLM reaction.")
