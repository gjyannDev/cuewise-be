"""The contract for the profile-extraction reply, and the check that enforces it.

Model output is untrusted. A reply that is not one JSON object in the expected shape raises InvalidReplyError (the
extractor retries once). A well-formed reply is then cleaned deterministically: text trimmed and cut on a word
boundary, blanks dropped, skills merged ignoring case, lists cut to their caps. A reply with no skills and no roles
raises EmptyProfileError: the résumé held nothing usable, and asking again would not help.
"""

from pydantic import BaseModel, ConfigDict, ValidationError

from app.core.ai.json_reply import InvalidReplyError, load_object

from ..constants.profile_constants import (
    DESCRIPTION_MAX_LENGTH,
    MAX_PROJECTS,
    MAX_ROLES,
    MAX_SKILLS,
    MAX_TECHNOLOGIES,
    ORGANIZATION_MAX_LENGTH,
    PERIOD_MAX_LENGTH,
    PROJECT_NAME_MAX_LENGTH,
    SKILL_MAX_LENGTH,
    SUMMARY_MAX_LENGTH,
    TECHNOLOGY_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)
from ..schemas.profile_schema import CandidateProfile, Project, Role


class EmptyProfileError(Exception):
    """No skills and no roles: not a résumé we can use (refused as unreadable, nothing stored)."""


# The raw shapes: types and known fields only. Lengths and counts are cut afterwards, not refused (spec EC19).
class _RawRole(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    title: str = ""
    organization: str = ""
    period: str = ""
    summary: str = ""


class _RawProject(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    name: str = ""
    description: str = ""
    technologies: list[str] = []


class _RawProfile(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    skills: list[str] = []
    roles: list[_RawRole] = []
    projects: list[_RawProject] = []


def fit(text: str, max_length: int) -> str:
    """Whitespace tidied, then cut to `max_length` on a word boundary (a single over-long word is cut hard)."""
    text = " ".join(text.split())
    if len(text) <= max_length:
        return text
    cut = text[: max_length + 1].rsplit(" ", 1)[0] if " " in text[: max_length + 1] else text[:max_length]
    return cut[:max_length].rstrip()


def _unique(items: list[str], max_length: int, cap: int) -> list[str]:
    """Tidied, blanks dropped, duplicates merged ignoring case (the first spelling wins), cut to `cap`."""
    seen: set[str] = set()
    kept = []
    for item in items:
        value = fit(item, max_length)
        if value and value.casefold() not in seen:
            seen.add(value.casefold())
            kept.append(value)
    return kept[:cap]


def parse_profile_reply(raw: str) -> CandidateProfile:
    try:
        reply = _RawProfile.model_validate(load_object(raw))
    except ValidationError as exc:
        raise InvalidReplyError("schema") from exc

    roles = [
        Role(
            title=title,
            organization=fit(r.organization, ORGANIZATION_MAX_LENGTH),
            period=fit(r.period, PERIOD_MAX_LENGTH),
            summary=fit(r.summary, SUMMARY_MAX_LENGTH),
        )
        for r in reply.roles
        if (title := fit(r.title, TITLE_MAX_LENGTH))
    ][:MAX_ROLES]
    projects = [
        Project(
            name=name,
            description=fit(p.description, DESCRIPTION_MAX_LENGTH),
            technologies=_unique(p.technologies, TECHNOLOGY_MAX_LENGTH, MAX_TECHNOLOGIES),
        )
        for p in reply.projects
        if (name := fit(p.name, PROJECT_NAME_MAX_LENGTH))
    ][:MAX_PROJECTS]
    profile = CandidateProfile(skills=_unique(reply.skills, SKILL_MAX_LENGTH, MAX_SKILLS), roles=roles, projects=projects)
    if not profile.skills and not profile.roles:
        raise EmptyProfileError
    return profile
