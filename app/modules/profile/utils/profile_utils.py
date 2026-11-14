"""Pure helpers of the profile feature: contact scrubbing, résumé reading, grounding."""

import re

from ..ai.profile_reply import EmptyProfileError
from ..schemas.profile_schema import CandidateProfile

# Local part, @, a domain with at least one dot. Broad on purpose: a false positive costs a word, a miss leaks PII.
_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
# A run of digits joined by spaces, dots, dashes or brackets on one line, optionally starting with +. Whether it is a
# phone number is decided by its digit count (below), so years, ranges and versions are left alone.
_PHONE_CANDIDATE = re.compile(r"(?<![\w.])\+?\(?\d[\d \t().-]*\d(?![\w])")
_PHONE_MIN_DIGITS = 9


def _phone_or_keep(match: re.Match[str]) -> str:
    text = match.group(0)
    return "[phone]" if sum(ch.isdigit() for ch in text) >= _PHONE_MIN_DIGITS else text


def scrub_contacts(text: str) -> str:
    """The text with email addresses and phone numbers replaced by placeholders; nothing else changes."""
    return _PHONE_CANDIDATE.sub(_phone_or_keep, _EMAIL.sub("[email]", text))


def _normalized(text: str) -> str:
    return " ".join(text.casefold().split())


def _appears(item: str, source: str) -> bool:
    """`item` occurs in `source` as a whole word or phrase, ignoring case and spacing ("Pay" is not in "Payments")."""
    return re.search(rf"(?<!\w){re.escape(_normalized(item))}(?!\w)", source) is not None


def ground_profile(profile: CandidateProfile, source_text: str) -> tuple[CandidateProfile, int]:
    """The profile with every short item the source text does not contain dropped, and how many were dropped.

    Skills, role titles, organizations and project technologies are checked; a role whose title is not in the text
    is dropped whole, an organization that is not is blanked. Summaries, descriptions and project names are free text
    (paraphrases) and are not checked. Nothing usable left raises EmptyProfileError."""
    source = _normalized(source_text)
    dropped = 0

    def keep(item: str) -> bool:
        nonlocal dropped
        found = _appears(item, source)
        dropped += not found
        return found

    skills = [s for s in profile.skills if keep(s)]
    roles = [
        r.model_copy(update={"organization": r.organization if not r.organization or keep(r.organization) else ""})
        for r in profile.roles
        if keep(r.title)
    ]
    projects = [p.model_copy(update={"technologies": [t for t in p.technologies if keep(t)]}) for p in profile.projects]
    if not skills and not roles:
        raise EmptyProfileError
    return CandidateProfile(skills=skills, roles=roles, projects=projects), dropped
