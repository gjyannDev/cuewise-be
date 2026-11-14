"""ground_profile: short items the model returned must appear in the text it was given (resume-upload AC16, EC38).
A deterministic check, no model call: it bounds both invented items and injected ones."""

import pytest

from app.modules.profile.ai.profile_reply import EmptyProfileError
from app.modules.profile.schemas.profile_schema import CandidateProfile, Project, Role
from app.modules.profile.utils.profile_utils import ground_profile

SOURCE = """Senior Backend Engineer, Acme Payments (2021-2024)
Rebuilt the payments API in Python and FastAPI.
Skills: PostgreSQL, C++, Node.js, Go
Project Ledger: double-entry ledger in Go with Kafka."""


def profile(**fields) -> CandidateProfile:
    base = {
        "skills": ["Python", "FastAPI", "PostgreSQL"],
        "roles": [Role(title="Senior Backend Engineer", organization="Acme Payments", period="2021-2024", summary="x")],
        "projects": [Project(name="Ledger", description="A ledger.", technologies=["Go", "Kafka"])],
    }
    return CandidateProfile(**(base | fields))


def test_a_profile_whose_items_all_appear_is_unchanged():
    original = profile()

    grounded, dropped = ground_profile(original, SOURCE)

    assert grounded == original and dropped == 0


def test_an_invented_skill_is_dropped_and_counted():  # EC38
    grounded, dropped = ground_profile(profile(skills=["Python", "Kubernetes", "MANGO"]), SOURCE)

    assert grounded.skills == ["Python"] and dropped == 2


def test_case_and_spacing_are_ignored():
    text = SOURCE.replace("Senior Backend Engineer", "SENIOR   backend\nEngineer")

    grounded, dropped = ground_profile(profile(skills=["postgresql", "fastapi"]), text)

    assert grounded.skills == ["postgresql", "fastapi"] and grounded.roles and dropped == 0


@pytest.mark.parametrize(("skill", "kept"), [("Go", True), ("C++", True), ("Node.js", True), ("Java", False), ("Pay", False)])
def test_an_item_matches_only_as_a_whole_word(skill, kept):  # "Pay" is inside "Payments"; "Java" nowhere
    grounded, _ = ground_profile(profile(skills=["Python", skill]), SOURCE)

    assert (skill in grounded.skills) is kept


def test_an_invented_title_drops_the_role_and_an_invented_organization_is_blanked():  # EC38
    roles = [
        Role(title="Chief Executive Officer", organization="Acme Payments", period="", summary="x"),
        Role(title="Senior Backend Engineer", organization="Google", period="", summary="x"),
    ]

    grounded, dropped = ground_profile(profile(roles=roles), SOURCE)

    assert [(r.title, r.organization) for r in grounded.roles] == [("Senior Backend Engineer", "")]
    assert dropped == 2


def test_invented_project_technologies_are_dropped():  # EC38
    projects = [Project(name="Ledger", description="A ledger.", technologies=["Go", "Rust", "Kafka"])]

    grounded, dropped = ground_profile(profile(projects=projects), SOURCE)

    assert grounded.projects[0].technologies == ["Go", "Kafka"] and dropped == 1


def test_summaries_descriptions_and_project_names_are_not_checked():  # spec: free text is a paraphrase
    roles = [Role(title="Senior Backend Engineer", organization="Acme Payments", period="2021-2024", summary="Led a team.")]
    projects = [Project(name="Payments Revamp", description="Not in the text at all.", technologies=[])]

    grounded, dropped = ground_profile(profile(roles=roles, projects=projects), SOURCE)

    assert grounded.roles[0].summary == "Led a team." and grounded.projects[0].name == "Payments Revamp" and dropped == 0


def test_nothing_left_after_grounding_is_an_empty_profile():  # AC16
    with pytest.raises(EmptyProfileError):
        ground_profile(profile(skills=["Rust"], roles=[Role(title="Pilot", organization="", period="", summary="")]), SOURCE)
