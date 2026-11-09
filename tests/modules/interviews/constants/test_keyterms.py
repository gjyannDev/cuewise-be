import pytest

from app.modules.interviews.constants.interviews_constants import (
    ROLE_KEYTERMS,
    SHARED_KEYTERMS,
    JobRole,
)

# Deepgram caps keyterm prompting at 500 tokens per request. A word is at least one token, so half that in words
# leaves room for terms that split into several tokens.
MAX_WORDS_PER_REQUEST = 250


def test_every_role_has_keyterms():  # spike 2026-11-04
    assert set(ROLE_KEYTERMS) == set(JobRole)


@pytest.mark.parametrize("role", list(JobRole))
def test_each_role_list_includes_the_shared_terms_once(role):  # inferred: duplicates waste the token budget
    terms = ROLE_KEYTERMS[role]

    assert set(SHARED_KEYTERMS) <= set(terms)
    assert len(terms) == len(set(terms))


@pytest.mark.parametrize("role", list(JobRole))
def test_each_role_list_stays_well_under_deepgrams_keyterm_limit(role):  # Deepgram: 500 tokens
    assert sum(len(term.split()) for term in ROLE_KEYTERMS[role]) <= MAX_WORDS_PER_REQUEST


@pytest.mark.parametrize("role", list(JobRole))
def test_terms_are_plain_text(role):  # Deepgram: plain terms only, no weights, commas or line breaks
    for term in ROLE_KEYTERMS[role]:
        assert term == term.strip() and term
        assert not any(char in term for char in ",;:\n")
