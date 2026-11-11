"""The shipped reference-note corpus (data/knowledge/): valid, broad enough, and not only model-drafted (AC5).

`test_at_least_a_third_of_the_shipped_notes_are_not_drafted` stays red until the supplied or approved material
(skills from real postings, your own level expectations) is in: that is the Step 11 review gate.
"""

import pytest

from app.modules.interviews.constants.interviews_constants import (
    GENERAL_ROLE,
    KNOWLEDGE_DIR,
    RETRIEVAL_TOP_K,
    JobRole,
    Level,
)
from app.modules.interviews.utils.interviews_knowledge_utils import (
    load_corpus,
    source_share_problem,
)

CORPUS = load_corpus(KNOWLEDGE_DIR)


def test_every_shipped_note_is_valid_and_raises_no_warning():  # AC4, AC5
    assert CORPUS.chunks
    assert CORPUS.warnings == []


@pytest.mark.parametrize("level", list(Level))
@pytest.mark.parametrize("role", list(JobRole))
def test_every_role_and_level_has_enough_notes_for_filter_mode(role, level):  # inferred: filter mode can fill 6
    eligible = [c for c in CORPUS.chunks if (role in c.roles or GENERAL_ROLE in c.roles) and level in c.levels]

    assert len(eligible) >= RETRIEVAL_TOP_K


def test_at_least_a_third_of_the_shipped_notes_are_not_drafted():  # AC5: the review gate
    assert source_share_problem(CORPUS.notes) is None
