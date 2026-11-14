"""merge_note_rankings: the quota merge of the job-description and profile rankings (resume-aware-interview Step 8, S2).

Job-description notes come first and keep the topic; the profile adds at most `profile_slots` notes the job description
didn't already pick. A short job-description side never lets the profile take over (EC17).
"""

import uuid

from app.modules.interviews.constants.interviews_constants import (
    RETRIEVAL_PROFILE_SLOTS,
    RETRIEVAL_TOP_K,
)
from app.modules.interviews.utils.interviews_knowledge_utils import (
    ReferenceNote,
    merge_note_rankings,
)

IDS = {name: uuid.UUID(int=i) for i, name in enumerate("abcdefghijklmnop", start=1)}


def ranked(names: str, top: float = 0.9) -> list[ReferenceNote]:
    """Notes named by single letters, ranked in the given order with falling scores."""
    return [
        ReferenceNote(IDS[name], f"Competency {name}", f"Text {name}", rank, round(top - rank / 100, 4))
        for rank, name in enumerate(names, start=1)
    ]


def names(notes: list[ReferenceNote]) -> str:
    return "".join(next(k for k, v in IDS.items() if v == note.chunk_id) for note in notes)


def test_the_shipped_quota_is_two_of_six():
    assert (RETRIEVAL_PROFILE_SLOTS, RETRIEVAL_TOP_K) == (2, 6)


def test_job_description_notes_come_first_and_the_profile_adds_at_most_its_slots():  # AC15
    merged, from_profile = merge_note_rankings(ranked("abcdefgh"), ranked("klmn"), k=6, profile_slots=2)

    assert names(merged) == "abcdkl" and from_profile == 2


def test_ranks_are_renumbered_and_each_note_keeps_its_own_score():
    jd, profile = ranked("abcdef", top=0.9), ranked("kl", top=0.7)

    merged, _ = merge_note_rankings(jd, profile, k=6, profile_slots=2)

    assert [note.rank for note in merged] == [1, 2, 3, 4, 5, 6]
    assert [note.score for note in merged] == [*(n.score for n in jd[:4]), *(n.score for n in profile)]


def test_a_profile_note_the_job_description_already_picked_is_not_repeated():
    merged, from_profile = merge_note_rankings(ranked("abcdef"), ranked("bkl"), k=6, profile_slots=2)

    assert names(merged) == "abcdkl" and from_profile == 2
    assert len({note.chunk_id for note in merged}) == len(merged)


def test_unused_profile_slots_go_back_to_the_job_description():  # the profile found nothing new
    merged, from_profile = merge_note_rankings(ranked("abcdefgh"), ranked("ab"), k=6, profile_slots=2)

    assert names(merged) == "abcdef" and from_profile == 0


def test_a_short_job_description_side_never_lets_the_profile_take_over():  # EC17
    merged, from_profile = merge_note_rankings(ranked("ab"), ranked("klmn"), k=6, profile_slots=2)

    assert names(merged) == "abkl" and from_profile == 2


def test_a_job_description_fill_note_also_in_the_profile_side_is_kept_once():
    merged, from_profile = merge_note_rankings(ranked("abcdefg"), ranked("kf"), k=6, profile_slots=2)

    # f is also in the job-description ranking, but past its share: it counts as one of the profile's notes.
    assert names(merged) == "abcdkf" and from_profile == 2


def test_zero_profile_slots_is_exactly_the_job_description_top_k():  # the switch-off (AC13 decision rule)
    jd = ranked("abcdefgh")

    assert merge_note_rankings(jd, ranked("klmn"), k=6, profile_slots=0) == (jd[:6], 0)


def test_no_profile_ranking_is_exactly_the_job_description_top_k():  # AC15: flag off unchanged
    jd = ranked("abcdefgh")

    assert merge_note_rankings(jd, [], k=6, profile_slots=2) == (jd[:6], 0)
