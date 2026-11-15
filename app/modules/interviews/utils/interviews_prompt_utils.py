"""The startup prompt check: every routed prompt version loads and renders through its real renderer.

Rendering with sample values catches what reading alone would not: a {{placeholder}} the renderer has no value for.
`app/main.py` runs it before the first request, so a broken prompt stops the app instead of failing mid-interview.
"""

from collections.abc import Callable

from ..constants.interviews_constants import InterviewType, JobRole, Level
from ..constants.interviews_prompt_registry import INTERVIEWER_ROUTES, SINGLE_ROUTES
from .interviews_utils import (
    load_prompt,
    render_decision_prompt,
    render_feedback_score_prompt,
    render_feedback_write_prompt,
    render_interviewer_prompt,
    render_interviewer_v2_prompt,
    render_summary_prompt,
)

_SETUP = {"role": JobRole.backend, "level": Level.senior, "interview_type": InterviewType.mixed}

# Each route's renderer, called with sample values: the template is the only thing that varies.
_RENDERERS: dict[str, Callable[[str], str]] = {
    "full_history": lambda t: render_interviewer_prompt(**_SETUP, question_number=1, question_count=5, template=t),
    "follow_up_decision": lambda t: render_decision_prompt(**_SETUP, template=t),
    "job_description_summary": lambda t: render_summary_prompt(t),
    "feedback_score": lambda t: render_feedback_score_prompt(**_SETUP, template=t),
    "feedback_write": lambda t: render_feedback_write_prompt(**_SETUP, template=t),
}


def _interviewer(template: str) -> str:
    return render_interviewer_v2_prompt(**_SETUP, question_count=5, template=template)


class PromptCheckError(Exception):
    """One or more routed prompts cannot be sent; the message lists each one."""


def _routed() -> list[tuple[str, Callable[[str], str]]]:
    routed = [(version, _interviewer) for table in INTERVIEWER_ROUTES.values() for version in table.values()]
    return routed + [(version, _RENDERERS[task]) for task, version in SINGLE_ROUTES.items()]


def check_prompts(load: Callable[[str], str] = load_prompt) -> None:
    """Raises PromptCheckError naming every routed version whose file is missing or has an unsupplied placeholder."""
    problems: list[str] = []
    for version, render in dict(_routed()).items():
        try:
            render(load(version))
        except FileNotFoundError:
            problems.append(f"{version}: file not found")
        except KeyError as missing:
            problems.append(f"{version}: no value for {{{{{missing.args[0]}}}}}")
    if problems:
        raise PromptCheckError("Prompt check failed:\n" + "\n".join(problems))
