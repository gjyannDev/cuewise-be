"""Interviewer.stream_turn: the streamed answer turn yields what it is doing, streams the question as it is written,
and ends with the same outcome as the JSON turn (sse-streaming Steps 5 and 13; AC4, AC13-AC15, EC7-EC15)."""

import json
import uuid

import pytest

from app.core.ai.fake import FakeStream
from app.core.ai.provider import LLMServerError
from app.modules.interviews.ai.interviews_context import (
    CONTEXT_MANAGER,
    InterviewerInputs,
)
from app.modules.interviews.ai.interviews_turn import Interviewer
from app.modules.interviews.ai.interviews_turn_types import (
    ActionKnown,
    Delta,
    PhaseChanged,
    Reset,
    Settled,
    TurnAction,
)
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V5_PROMPT_VERSION,
    InterviewType,
    JobRole,
    Level,
    TurnPhase,
)
from app.modules.interviews.utils.interviews_utils import QuestionTurn

pytestmark = pytest.mark.anyio

SESSION = uuid.uuid7()
TURN = QuestionTurn("Tell me about a conflict with a teammate?", "behavioral", "We talked it out.")
GOOD = "CATEGORY: behavioral\nTell me about a project you led from start to finish?"


def make_interviewer(llm, clock) -> Interviewer:
    return Interviewer(llm, CONTEXT_MANAGER, max_tokens=800, budget_seconds=30, clock=clock)


def inputs(*turns: QuestionTurn) -> InterviewerInputs:
    return InterviewerInputs(
        role=JobRole.backend,
        level=Level.junior,
        interview_type=InterviewType.behavioral,
        question_count=3,
        job_description=None,
        turns=list(turns or [TURN]),
    )


async def collect(interviewer: Interviewer, *, last_main: bool = False) -> list:
    return [event async for event in interviewer.stream_turn(SESSION, inputs(), last_main=last_main)]


def kinds(events: list) -> list[str]:
    """Event kinds in order, a run of deltas shown once as "Delta"."""
    shown = {PhaseChanged: lambda e: e.phase.value, ActionKnown: lambda e: f"action:{e.action.value}"}
    out: list[str] = []
    for event in events:
        kind = shown.get(type(event), lambda e: type(e).__name__)(event)
        if not (kind == "Delta" and out and out[-1] == "Delta"):
            out.append(kind)
    return out


def streamed_text(events: list) -> list[str]:
    """The question text of each draft (a Reset starts a new one)."""
    drafts = [""]
    for event in events:
        if isinstance(event, Reset):
            drafts.append("")
        elif isinstance(event, Delta):
            drafts[-1] += event.text
    return drafts


def follow_up_json(question="What was the result for the team?") -> str:
    return json.dumps({"question": question})


# --- Step 5: the turn's progress and outcome ---


async def test_a_move_on_turn_reports_deciding_its_action_writing_and_the_question(llm, clock):
    events = await collect(make_interviewer(llm, clock))

    assert kinds(events) == [TurnPhase.deciding, "action:next_question", TurnPhase.writing, "Delta", "Settled"]
    outcome = events[-1].outcome
    assert outcome.action == TurnAction.next_question
    assert outcome.written is not None and outcome.written.reply is not None
    assert outcome.written.prompt_version == INTERVIEWER_V5_PROMPT_VERSION


async def test_a_follow_up_is_reported_only_after_its_write_succeeds(llm, clock, decision_json):  # EC13
    llm.script_decide(decision_json("follow_up", "missing_result"))
    llm.script(follow_up_json())

    events = await collect(make_interviewer(llm, clock))

    assert kinds(events) == [TurnPhase.deciding, TurnPhase.writing, "Delta", "action:follow_up", "Settled"]
    assert events[-1].outcome.written.reply.question == "What was the result for the team?"


async def test_a_follow_up_whose_write_fails_moves_on_instead(llm, clock, decision_json):  # EC14
    llm.script_decide(decision_json("follow_up", "missing_result"))
    llm.script('{"broken": ', '{"still broken": ')

    events = await collect(make_interviewer(llm, clock))

    assert kinds(events)[-2:] == ["action:next_question", "Settled"]
    assert TurnPhase.writing in kinds(events)
    assert events[-1].outcome.written is None


async def test_the_last_threads_end_completes_without_writing(llm, clock):  # EC15
    events = await collect(make_interviewer(llm, clock), last_main=True)

    assert kinds(events) == [TurnPhase.deciding, "action:complete", "Settled"]
    assert events[-1].outcome.action == TurnAction.complete
    assert llm.fake.calls == []


async def test_a_failed_decide_call_falls_back_to_the_next_question(llm, clock):  # EC12
    llm.script_decide(LLMServerError("provider down"))

    events = await collect(make_interviewer(llm, clock))

    assert kinds(events) == [TurnPhase.deciding, "action:next_question", TurnPhase.writing, "Delta", "Settled"]
    assert events[-1].outcome.written is not None


@pytest.mark.parametrize(
    ("decide", "writes", "last_main"),
    [
        (("next_question",), ("{q}",), False),
        (("follow_up", "no_example"), ("{f}",), False),
        (("follow_up", "no_example"), ("{bad}", "{bad}"), False),
        (("next_question",), (), True),
    ],
)
async def test_the_streamed_outcome_equals_the_json_turns(
    llm, clock, decision_json, reply_json, decide, writes, last_main
):  # AC4
    def script():
        llm.script_decide(decision_json(*decide, note="Named the conflict, no outcome."))
        replies = {
            "{q}": reply_json("Describe a project you led?", "behavioral"),
            "{f}": follow_up_json(),
            # Invalid in both formats (two questions), so both turns fall back the same way.
            "{bad}": follow_up_json("What did you do? And why?"),
        }
        llm.script(*[replies[w] for w in writes])

    script()
    streamed = [e async for e in make_interviewer(llm, clock).stream_turn(SESSION, inputs(), last_main=last_main)]
    script()
    direct = make_interviewer(llm, clock).answer_turn(SESSION, inputs(), last_main=last_main)

    outcome = streamed[-1]
    assert isinstance(outcome, Settled)
    outcome = outcome.outcome
    assert (outcome.action, outcome.note, outcome.decision_prompt_version) == (
        direct.action,
        direct.note,
        direct.decision_prompt_version,
    )
    assert (outcome.written.reply if outcome.written else None) == (direct.written.reply if direct.written else None)
    assert len(outcome.results) == len(direct.results)


# --- Step 13: the question streamed as it is written ---


async def test_the_question_streams_in_chunks_without_its_category_line(llm, clock):  # AC13
    llm.script(FakeStream(["CATEGORY: beha", "vioral\nTell me about ", "a project ", "you led?"]))

    events = await collect(make_interviewer(llm, clock))

    deltas = [e.text for e in events if isinstance(e, Delta)]
    assert len(deltas) >= 2
    assert "".join(deltas) == "Tell me about a project you led?"
    assert not any("CATEGORY" in d or "behavioral" in d for d in deltas)
    assert events[-1].outcome.written.reply.question == "Tell me about a project you led?"


async def test_an_invalid_draft_with_time_left_is_taken_back_and_retried(llm, clock):  # EC7
    llm.script("CATEGORY: behavioral\nWhat did you build? And why?", GOOD)

    events = await collect(make_interviewer(llm, clock))

    assert kinds(events)[-4:] == ["Delta", "Reset", "Delta", "Settled"]
    assert streamed_text(events) == ["What did you build? And why?", GOOD.split("\n", 1)[1]]
    assert events[-1].outcome.written.reply.question == GOOD.split("\n", 1)[1]


async def test_an_invalid_draft_with_no_time_left_is_taken_back_and_the_bank_asks(llm, clock):  # EC8
    llm.script("CATEGORY: behavioral\nWhat did you build? And why?", GOOD, on_call=lambda: clock.advance(26))

    events = await collect(make_interviewer(llm, clock))

    assert kinds(events)[-3:] == ["Delta", "Reset", "Settled"]
    assert events[-1].outcome.written is None
    assert len(llm.fake.calls) == 1


async def test_a_provider_failure_mid_question_is_taken_back_and_retried(llm, clock):  # EC9
    llm.script(FakeStream(["CATEGORY: behavioral\n", "Tell me "], error=LLMServerError("connection dropped")), GOOD)

    events = await collect(make_interviewer(llm, clock))

    assert streamed_text(events) == ["Tell me ", GOOD.split("\n", 1)[1]]
    assert events[-1].outcome.written.reply is not None


async def test_the_deadline_running_out_mid_question_takes_it_back_and_the_bank_asks(llm, clock):  # EC9
    # The clock jumps past the deadline as the call starts; the first chunk already carries visible text.
    llm.script(FakeStream(["CATEGORY: behavioral\nTell me ", "about it?"]), on_call=lambda: clock.advance(31))

    events = await collect(make_interviewer(llm, clock))

    assert kinds(events)[-3:] == ["Delta", "Reset", "Settled"]
    assert events[-1].outcome.written is None


async def test_a_failure_before_any_text_needs_no_reset(llm, clock):  # EC10
    llm.script(LLMServerError("provider down"))

    events = await collect(make_interviewer(llm, clock))

    assert not any(isinstance(e, Delta | Reset) for e in events)
    assert events[-1].outcome.written is None


async def test_a_reply_without_a_category_line_streams_nothing_for_that_attempt(llm, clock):  # EC11
    llm.script("Tell me about a time you had to deliver bad news to a stakeholder?", GOOD)

    events = await collect(make_interviewer(llm, clock))

    assert not any(isinstance(e, Reset) for e in events)
    assert streamed_text(events) == [GOOD.split("\n", 1)[1]]
    assert len(llm.fake.calls) == 2


async def test_leaving_mid_question_cancels_the_provider_call(llm, clock):  # AC15
    llm.script(FakeStream(["CATEGORY: behavioral\n", "Tell me ", "about ", "it?"], delay=0.05))
    turn = make_interviewer(llm, clock).stream_turn(SESSION, inputs(), last_main=False)

    async for event in turn:
        if isinstance(event, Delta):
            break
    await turn.aclose()

    assert llm.fake.cancelled is True
