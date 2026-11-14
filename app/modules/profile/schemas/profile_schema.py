"""The candidate profile: what a résumé becomes, what is stored, and what the API returns.

The schema is the data minimization: there is no field for a name, email, phone, address, date of birth or photo,
and every text field and list is capped so 8d can put the whole profile in every interview prompt.
"""

from datetime import datetime
from typing import Annotated

from fastapi import UploadFile
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

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


def _text(max_length: int, min_length: int = 0) -> type[str]:
    return Annotated[str, StringConstraints(min_length=min_length, max_length=max_length)]  # type: ignore[return-value]


class Role(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: _text(TITLE_MAX_LENGTH, 1)
    organization: _text(ORGANIZATION_MAX_LENGTH) = ""
    # Free text such as "2021-2024": dates a model extracts are error-prone, so no fake precision.
    period: _text(PERIOD_MAX_LENGTH) = ""
    summary: _text(SUMMARY_MAX_LENGTH) = ""


class Project(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: _text(PROJECT_NAME_MAX_LENGTH, 1)
    description: _text(DESCRIPTION_MAX_LENGTH) = ""
    technologies: list[_text(TECHNOLOGY_MAX_LENGTH, 1)] = Field(default_factory=list, max_length=MAX_TECHNOLOGIES)


class CandidateProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    skills: list[_text(SKILL_MAX_LENGTH, 1)] = Field(default_factory=list, max_length=MAX_SKILLS)
    roles: list[Role] = Field(default_factory=list, max_length=MAX_ROLES)  # most recent first
    projects: list[Project] = Field(default_factory=list, max_length=MAX_PROJECTS)


class ProfileOut(CandidateProfile):
    updated_at: datetime


class ResumeUploadIn(BaseModel):
    """The multipart upload: exactly one part, `file`. Extra form fields are refused."""

    model_config = ConfigDict(extra="forbid")

    file: UploadFile
