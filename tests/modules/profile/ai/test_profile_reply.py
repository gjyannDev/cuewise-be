"""parse_profile_reply: the model's JSON -> a capped, cleaned CandidateProfile, or a refusal (resume-upload AC5, AC7,
AC13; EC15, EC19, EC20). Malformed replies raise InvalidReplyError (the extractor retries once); a valid reply with no
skills and no roles raises EmptyProfileError (no retry: the résumé, not the reply, is the problem)."""

import json

import pytest

from app.core.ai.json_reply import InvalidReplyError
from app.modules.profile.ai.profile_reply import EmptyProfileError, parse_profile_reply
from app.modules.profile.constants.profile_constants import (
    MAX_PROJECTS,
    MAX_ROLES,
    MAX_SKILLS,
    MAX_TECHNOLOGIES,
    PROFILE_MAX_JSON_CHARS,
    SUMMARY_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)

VALID = {
    "skills": ["Python", "FastAPI", "PostgreSQL"],
    "roles": [
        {
            "title": "Senior Backend Engineer",
            "organization": "Acme Payments",
            "period": "2021-2024",
            "summary": "Rebuilt the payments API.",
        }
    ],
    "projects": [{"name": "Ledger", "description": "A double-entry ledger service.", "technologies": ["Go", "Kafka"]}],
}


def reply(data) -> str:
    return json.dumps(data)


def test_a_valid_reply_becomes_the_profile():
    profile = parse_profile_reply(reply(VALID))

    assert profile.skills == ["Python", "FastAPI", "PostgreSQL"]
    assert profile.roles[0].title == "Senior Backend Engineer" and profile.roles[0].period == "2021-2024"
    assert profile.projects[0].technologies == ["Go", "Kafka"]


def test_a_fenced_reply_is_read():
    assert parse_profile_reply(f"```json\n{reply(VALID)}\n```").skills[0] == "Python"


@pytest.mark.parametrize(("raw", "reason"), [("not json", "not_json"), ("[1, 2]", "not_object"), ("Sure! {}", "not_json")])
def test_a_reply_that_is_not_one_json_object_is_invalid(raw, reason):  # EC18
    with pytest.raises(InvalidReplyError) as raised:
        parse_profile_reply(raw)

    assert raised.value.reason == reason


@pytest.mark.parametrize(
    "data",
    [
        {**VALID, "name": "Ana Cruz"},  # an unknown field: no place for PII or a verdict
        {**VALID, "skills": "Python, Go"},  # wrong type
        {**VALID, "roles": [{"title": 42}]},
        {**VALID, "roles": [{**VALID["roles"][0], "rating": "10/10"}]},
    ],
)
def test_a_reply_outside_the_schema_is_invalid(data):  # EC18, EC39: the schema cannot hold an instruction's effect
    with pytest.raises(InvalidReplyError) as raised:
        parse_profile_reply(reply(data))

    assert raised.value.reason == "schema"


def test_too_many_items_are_cut_to_the_caps():  # EC19
    data = {
        "skills": [f"Skill{i}" for i in range(40)],
        "roles": [{**VALID["roles"][0], "title": f"Engineer {i}"} for i in range(9)],
        "projects": [{"name": f"P{i}", "description": "d", "technologies": [f"T{j}" for j in range(12)]} for i in range(7)],
    }

    profile = parse_profile_reply(reply(data))

    assert len(profile.skills) == MAX_SKILLS and profile.skills[0] == "Skill0"
    assert len(profile.roles) == MAX_ROLES and profile.roles[0].title == "Engineer 0"  # most recent first is kept
    assert len(profile.projects) == MAX_PROJECTS
    assert all(len(p.technologies) == MAX_TECHNOLOGIES for p in profile.projects)


def test_too_long_text_is_cut_on_a_word_boundary():  # EC19
    long_summary = "Led the platform team " * 40
    data = {**VALID, "roles": [{**VALID["roles"][0], "title": "Staff " * 30, "summary": long_summary}]}

    role = parse_profile_reply(reply(data)).roles[0]

    assert len(role.title) <= TITLE_MAX_LENGTH and len(role.summary) <= SUMMARY_MAX_LENGTH
    assert set(role.summary.split()) <= {"Led", "the", "platform", "team"}  # whole words only, none cut in half
    assert role.summary == role.summary.strip()


def test_duplicate_skills_are_merged_ignoring_case_and_the_first_spelling_kept():  # EC20
    data = {**VALID, "skills": ["Python", "python", " PYTHON ", "Go", "go"]}

    assert parse_profile_reply(reply(data)).skills == ["Python", "Go"]


def test_blank_items_are_dropped_and_spacing_is_tidied():
    data = {
        "skills": ["  ", "Machine   learning", ""],
        "roles": [{"title": "  ", "organization": "X"}, {"title": " Data  Engineer ", "organization": "Initech"}],
        "projects": [{"name": "", "description": "no name"}, {"name": "Pipeline", "technologies": ["", "Airflow"]}],
    }

    profile = parse_profile_reply(reply(data))

    assert profile.skills == ["Machine learning"]
    assert [r.title for r in profile.roles] == ["Data Engineer"]
    assert [p.name for p in profile.projects] == ["Pipeline"] and profile.projects[0].technologies == ["Airflow"]


def test_missing_optional_fields_default_to_empty():
    profile = parse_profile_reply(reply({"skills": ["Go"]}))

    assert profile.roles == [] and profile.projects == []


@pytest.mark.parametrize(
    "data",
    [{}, {"skills": [], "roles": []}, {"skills": ["  "], "roles": [{"title": " "}], "projects": [{"name": "Only a project"}]}],
)
def test_no_skills_and_no_roles_is_an_empty_profile_not_a_bad_reply(data):  # EC15
    with pytest.raises(EmptyProfileError):
        parse_profile_reply(reply(data))


def test_the_worst_case_profile_stays_under_the_size_bound():  # AC13
    long = "word " * 200
    data = {
        "skills": [long] * 50,
        "roles": [{"title": long, "organization": long, "period": long, "summary": long}] * 10,
        "projects": [{"name": long, "description": long, "technologies": [long] * 20}] * 10,
    }
    data["skills"] = [f"{i} {long}" for i in range(50)]  # distinct, so de-duplication cannot shrink them

    profile = parse_profile_reply(reply(data))

    assert len(profile.model_dump_json()) < PROFILE_MAX_JSON_CHARS
