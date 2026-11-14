"""The candidate profile as interview input: a fenced prompt block and a short retrieval query (resume-aware-interview).

Both are data minimization. The block drops organization and period (the question needs what the candidate did, not
where or when). The query uses short items only: they match note headings, and they are less personal than summaries.
"""

from app.modules.profile.schemas.profile_schema import CandidateProfile

from .interviews_utils import neutralize_app_tags


def candidate_profile_block(profile: CandidateProfile) -> str:
    """The profile fenced as data, like the job description. Summaries and descriptions are candidate-written and not
    grounding-checked, so every value has its tags neutralised: nothing inside can close the block or open another."""
    lines = []
    if profile.skills:
        lines.append(f"Skills: {', '.join(profile.skills)}")
    if profile.roles:
        lines.append("Roles:")
        lines.extend(f"- {role.title}: {role.summary}" if role.summary else f"- {role.title}" for role in profile.roles)
    if profile.projects:
        lines.append("Projects:")
        for project in profile.projects:
            line = f"- {project.name}: {project.description}" if project.description else f"- {project.name}"
            if project.technologies:
                line += f" (technologies: {', '.join(project.technologies)})"
            lines.append(line)
    body = neutralize_app_tags("\n".join(lines))
    return f"<candidate_profile>\n{body}\n</candidate_profile>"


def profile_items(profile: CandidateProfile) -> list[str]:
    """The profile's short items: skills and technologies first (closest to note headings), then role titles and
    project names. Deduped case-insensitively, first spelling kept. The retrieval query and the eval's mention metric
    both read the profile this way."""
    items = [
        *profile.skills,
        *(tech for project in profile.projects for tech in project.technologies),
        *(role.title for role in profile.roles),
        *(project.name for project in profile.projects),
    ]
    unique: dict[str, str] = {}
    for item in items:
        unique.setdefault(item.casefold(), item)
    return list(unique.values())


def profile_query_text(profile: CandidateProfile) -> str | None:
    """The profile's short items as one retrieval query. None: nothing to embed."""
    return ", ".join(profile_items(profile)) or None
