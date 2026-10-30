from typing import NamedTuple

import pytest

from app.core.ai.context import (
    ContextManager,
    ContextTooLargeError,
    StrategyOutput,
    Task,
    estimate_tokens,
)
from app.core.ai.provider import ChatMessage


class Inputs(NamedTuple):
    system: str
    turns: list[str]
    latest: str


class Stub:
    """System prompt, then every turn still kept, then the latest one; oldest turns go first."""

    def __init__(self, limit: int | None, version: str = "stub_v1"):
        self.limit = limit
        self.version = version

    def droppable(self, inputs: Inputs) -> int:
        return len(inputs.turns)

    def build(self, inputs: Inputs, dropped: int) -> StrategyOutput:
        kept = inputs.turns[dropped:]
        messages = [ChatMessage(role="system", content=inputs.system)]
        messages += [ChatMessage(role="user", content=t) for t in [*kept, inputs.latest]]
        return StrategyOutput(messages, self.version, {"turns_sent": len(kept)})


def manager(limit: int | None = None) -> ContextManager:
    return ContextManager({"turn": Task(default="stub", strategies={"stub": Stub(limit), "other": Stub(None, "v2")})})


INPUTS = Inputs(system="s" * 40, turns=["a" * 40, "b" * 40, "c" * 40], latest="z" * 40)  # 10 tokens each


def test_estimate_is_characters_divided_by_four():
    assert estimate_tokens([ChatMessage(role="user", content="x" * 41)]) == 10


def test_builds_the_task_with_its_default_strategy():
    built = manager().build("turn", INPUTS)

    assert [m.content for m in built.messages] == [INPUTS.system, *INPUTS.turns, INPUTS.latest]
    assert built.prompt_version == "stub_v1"
    assert (built.report.task, built.report.strategy, built.report.estimated_tokens) == ("turn", "stub", 50)
    assert (built.report.system_tokens, built.report.dropped, built.report.counts) == (10, 0, {"turns_sent": 3})


def test_a_named_strategy_overrides_the_default():
    assert manager().build("turn", INPUTS, strategy="other").prompt_version == "v2"


@pytest.mark.parametrize(("task", "strategy"), [("nope", None), ("turn", "nope")])
def test_unknown_task_or_strategy_names_the_valid_ones(task, strategy):
    with pytest.raises(ValueError, match="turn|other"):
        manager().build(task, INPUTS, strategy=strategy)


def test_a_strategy_without_a_limit_is_never_trimmed():  # EC26
    big = INPUTS._replace(turns=["x" * 4000] * 10)

    built = manager(limit=None).build("turn", big)

    assert built.report.dropped == 0 and built.report.estimated_tokens > 10_000


def test_over_the_limit_drops_oldest_entries_until_it_fits():  # AC7, EC6
    built = manager(limit=30).build("turn", INPUTS)

    assert [m.content for m in built.messages] == [INPUTS.system, "c" * 40, INPUTS.latest]
    assert (built.report.dropped, built.report.estimated_tokens) == (2, 30)


def test_required_parts_alone_over_the_limit_raise_and_still_log(app_logs):  # EC7
    with pytest.raises(ContextTooLargeError) as raised:
        manager(limit=15).build("turn", INPUTS)

    assert raised.value.report.dropped == 3
    [line] = [r.getMessage() for r in app_logs.records if r.name == "app.llm.context"]
    assert "outcome=too_large" in line


def test_the_log_line_has_counts_and_sizes_but_no_text(app_logs):  # AC11
    secret = INPUTS._replace(latest="my salary is 90k and my manager is Bob")

    manager().build("turn", secret)

    [line] = [r.getMessage() for r in app_logs.records if r.name == "app.llm.context"]
    assert "task=turn" in line and "strategy=stub" in line and "est_tokens=" in line and "turns_sent=3" in line
    assert "salary" not in line and "Bob" not in line and "aaaa" not in line


def test_a_second_task_with_its_own_strategy_leaves_the_first_alone():  # AC12 part 1
    class SendEverything(Stub):
        def build(self, inputs, dropped):
            return StrategyOutput([ChatMessage(role="user", content=" | ".join(inputs.turns))], "feedback_v1", {})

    tasks = {
        "turn": Task(default="stub", strategies={"stub": Stub(30)}),
        "feedback": Task(default="all", strategies={"all": SendEverything(None)}),
    }
    context = ContextManager(tasks)

    assert context.build("feedback", INPUTS).messages[0].content == " | ".join(INPUTS.turns)
    assert context.build("turn", INPUTS).report.dropped == 2
