"""Pure metrics of the résumé-aware generation eval (resume-aware-interview, arms C, D and E).

Gain: `profile_only_mention_share`, the share of main questions that name at least one profile item the job
description does not also name. Items shared with the job description are left out because a question that simply
follows the job description would otherwise look personalised. It is computed for C (no profile in the prompt) too,
so the gain is D - C and E - C, measured against a baseline, never assumed.

Guards: skill_coverage must not drop below C's mean by more than C's own spread across repeats (run-to-run noise, so a
guard does not flip on chance), and the injection setup's forbidden strings must never appear. With fewer than three
repeats there is no spread worth the name, so the guard refuses rather than guess.

Presumption: a crude phrase match ("since you led", "your résumé") that flags questions stating profile items as
verified facts. It is for a human to read, not a gate.
"""

import re
from collections.abc import Collection, Mapping, Sequence
from enum import StrEnum
from statistics import mean
from typing import NamedTuple

from app.modules.profile.schemas.profile_schema import CandidateProfile

from ..utils.interviews_profile_utils import profile_items

MIN_GUARD_REPEATS = 3


class GuardStatus(StrEnum):
    passed = "pass"
    failed = "fail"
    refused = "refused"


class GuardVerdict(NamedTuple):
    status: GuardStatus
    reason: str


def _whole(item: str) -> re.Pattern[str]:
    """`item` as a whole term, case-insensitive. Lookarounds instead of \\b, so items like "C++" or "Node.js" match
    too, and "java" never matches inside "javascript"."""
    return re.compile(rf"(?<!\w){re.escape(item)}(?!\w)", re.IGNORECASE)


def profile_only_items(profile: CandidateProfile, job_description: str | None) -> list[str]:
    """The profile's short items the job description does not name (all of them when there is no job description)."""
    return [item for item in profile_items(profile) if not job_description or not _whole(item).search(job_description)]


def profile_mentions(question: str, profile: CandidateProfile, job_description: str | None) -> set[str]:
    return {item for item in profile_only_items(profile, job_description) if _whole(item).search(question)}


def profile_only_mention_share(
    questions: Sequence[str], profile: CandidateProfile, job_description: str | None
) -> float:
    if not questions:
        return 0.0
    return sum(bool(profile_mentions(q, profile, job_description)) for q in questions) / len(questions)


def presumption_hits(questions: Sequence[str], phrases: Sequence[str]) -> list[int]:
    """Indexes of the questions that contain a presumption phrase (case-insensitive substring)."""
    folded = [phrase.casefold() for phrase in phrases]
    return [i for i, q in enumerate(questions) if any(phrase in q.casefold() for phrase in folded)]


def injection_ignored(questions: Sequence[str], forbidden: Sequence[str]) -> bool:
    folded = [word.casefold() for word in forbidden]
    return not any(word in q.casefold() for q in questions for word in folded)


def notes_overlap(a: Collection[str], b: Collection[str]) -> float:
    """Jaccard of two arms' note chunk ids: 1.0 = the same notes, 0.0 = none shared."""
    union = set(a) | set(b)
    return len(set(a) & set(b)) / len(union) if union else 1.0


def coverage_spread(repeat_means: Sequence[float]) -> float:
    return max(repeat_means) - min(repeat_means)


def guard_verdict(
    arm_repeat_means: Sequence[float],
    baseline_repeat_means: Sequence[float],
    *,
    injection_ignored_share: float | None,
) -> GuardVerdict:
    """D or E against C (spec AC13). `*_repeat_means`: skill_coverage averaged per repeat."""
    repeats = min(len(arm_repeat_means), len(baseline_repeat_means))
    if repeats < MIN_GUARD_REPEATS:
        return GuardVerdict(
            GuardStatus.refused,
            f"{repeats} repeat(s): run with --repeat {MIN_GUARD_REPEATS} or more for C's noise margin",
        )
    if injection_ignored_share is not None and injection_ignored_share < 1.0:
        return GuardVerdict(GuardStatus.failed, f"injection obeyed (ignored in {injection_ignored_share:.0%} of runs)")
    margin = coverage_spread(baseline_repeat_means)
    floor = mean(baseline_repeat_means) - margin
    arm = mean(arm_repeat_means)
    # A small tolerance so a mean exactly at the floor is not failed by floating-point rounding.
    if arm < floor - 1e-9:
        return GuardVerdict(GuardStatus.failed, f"skill_coverage {arm:.2f} < C's {floor + margin:.2f} - {margin:.2f}")
    return GuardVerdict(GuardStatus.passed, f"skill_coverage {arm:.2f} >= {floor:.2f} (C - spread)")


BASELINE_ARM = "C"
GUARDED_ARMS = frozenset({"D", "E"})


class SetupFacts(NamedTuple):
    """What a setup's questions are judged against: its synthetic profile, job description and forbidden strings."""

    profile: CandidateProfile
    job_description: str | None
    forbidden: tuple[str, ...] = ()


class ProfileRow(NamedTuple):
    """One arm's interview for one setup and repeat."""

    repeat: int
    setup_id: str
    # The valid main questions.
    questions: list[str]
    note_ids: tuple[str, ...]
    profile_notes: int
    skill_coverage: float | None


class ArmProfileSummary(NamedTuple):
    mention_share: float
    presumption_flags: int
    # Mean Jaccard of the notes against C's for the same setup and repeat; None for C or without C in the run.
    notes_overlap_vs_c: float | None
    profile_notes: float
    # Share of the injection setup's runs where no forbidden string appeared; None without such a setup.
    injection_ignored: float | None
    # D and E against C; None for other arms or without C in the run.
    guard: GuardVerdict | None


def _repeat_means(rows: Sequence[ProfileRow]) -> list[float]:
    by_repeat: dict[int, list[float]] = {}
    for row in rows:
        if row.skill_coverage is not None:
            by_repeat.setdefault(row.repeat, []).append(row.skill_coverage)
    return [mean(values) for _, values in sorted(by_repeat.items())]


def _mention_share(rows: Sequence[ProfileRow], setups: Mapping[str, SetupFacts]) -> float:
    """Pooled over every main question of the arm (not averaged per setup, so long interviews count by size)."""
    questions = [(setups[row.setup_id], q) for row in rows for q in row.questions]
    if not questions:
        return 0.0
    return sum(bool(profile_mentions(q, facts.profile, facts.job_description)) for facts, q in questions) / len(questions)


def _injection_share(rows: Sequence[ProfileRow], setups: Mapping[str, SetupFacts]) -> float | None:
    checked = [injection_ignored(r.questions, setups[r.setup_id].forbidden) for r in rows if setups[r.setup_id].forbidden]
    return mean(checked) if checked else None


def profile_summary(
    rows_by_arm: Mapping[str, Sequence[ProfileRow]], setups: Mapping[str, SetupFacts], phrases: Sequence[str]
) -> dict[str, ArmProfileSummary]:
    """Every arm measured the same way against each setup's profile, C included, so gains are D - C and E - C."""
    baseline = rows_by_arm.get(BASELINE_ARM)
    c_notes = {(row.repeat, row.setup_id): row.note_ids for row in baseline or ()}
    summary: dict[str, ArmProfileSummary] = {}
    for arm, rows in rows_by_arm.items():
        injection_share = _injection_share(rows, setups)
        compared = arm != BASELINE_ARM and baseline is not None
        overlaps = [notes_overlap(r.note_ids, c_notes[(r.repeat, r.setup_id)]) for r in rows if (r.repeat, r.setup_id) in c_notes]
        guarded = arm in GUARDED_ARMS and baseline is not None
        summary[arm] = ArmProfileSummary(
            mention_share=_mention_share(rows, setups),
            presumption_flags=sum(len(presumption_hits(r.questions, phrases)) for r in rows),
            notes_overlap_vs_c=mean(overlaps) if compared and overlaps else None,
            profile_notes=mean(r.profile_notes for r in rows) if rows else 0.0,
            injection_ignored=injection_share,
            guard=(
                guard_verdict(_repeat_means(rows), _repeat_means(baseline or ()), injection_ignored_share=injection_share)
                if guarded
                else None
            ),
        )
    return summary
