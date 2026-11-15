"""The startup prompt check (prompt-registry AC8, EC5, EC6): every routed version loads and renders."""

import pytest

from app.modules.interviews.constants.interviews_prompt_registry import (
    DECISION_VERSION,
    INTERVIEWER_JSON,
    Data,
)
from app.modules.interviews.utils.interviews_prompt_utils import (
    PromptCheckError,
    check_prompts,
)
from app.modules.interviews.utils.interviews_utils import load_prompt


def loader(missing: frozenset[str] = frozenset(), extra: dict[str, str] | None = None):
    """The real files, except versions that are missing or get extra text appended."""

    def load(version: str) -> str:
        if version in missing:
            raise FileNotFoundError(f"prompts/{version}.md")
        return load_prompt(version) + (extra or {}).get(version, "")

    return load


def test_the_real_prompts_pass():  # AC8
    check_prompts()


def test_a_missing_routed_file_is_named():  # EC5
    version = INTERVIEWER_JSON[Data.profile]
    with pytest.raises(PromptCheckError, match=f"{version}: file not found"):
        check_prompts(loader(missing=frozenset({version})))


def test_a_placeholder_the_renderer_does_not_supply_is_named():  # EC6
    with pytest.raises(PromptCheckError, match=r"follow_up_decision_v1: no value for \{\{shoe_size\}\}"):
        check_prompts(loader(extra={DECISION_VERSION: "{{shoe_size}}"}))


def test_every_problem_is_reported_in_one_error():
    with pytest.raises(PromptCheckError) as raised:
        check_prompts(
            loader(missing=frozenset({INTERVIEWER_JSON[Data.plain]}), extra={DECISION_VERSION: "{{shoe_size}}"})
        )
    assert str(raised.value).count("\n") == 2  # a heading line, then one line per problem
