"""The decide call on the LangChain call layer with structured output (U3b1 step 8, FR6, AC6, AC9, AC10).

The model gets `ModelDecision` as a JSON schema through `complete_structured`; `parse_decision_reply` still checks the
reply text, so the gap and note rules keep their one home. Same loop, cap and fallback as before. Fake chat model and
a fake clock: no network, no real waits.
"""

import json
import uuid
from types import SimpleNamespace

from google.api_core import exceptions as gx

from app.core.ai.chat_fake import FakeChatModel, fake_reply
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.context import ContextTooLargeError
from app.core.ai.tracing import Tracer
from app.core.config import settings
from app.modules.interviews.ai.interviews_context import (
    CONTEXT_MANAGER,
    InterviewerInputs,
)
from app.modules.interviews.ai.interviews_decide import decide
from app.modules.interviews.ai.interviews_model_schemas import ModelDecision
from app.modules.interviews.ai.interviews_turn_limits import Deadline
from app.modules.interviews.constants.interviews_constants import (
    DECIDE_MAX_SECONDS,
    DECISION_PROMPT_VERSION,
    DECISION_TASK,
    NOTE_MAX_LENGTH,
    WRITE_RESERVE_SECONDS,
    FollowUpAction,
    FollowUpGap,
    InterviewType,
    JobRole,
    Level,
)
from app.modules.interviews.utils.interviews_utils import QuestionTurn
from tests.core.ai.test_retry import Clock
from tests.core.ai.test_tracing import FakeClient


def decision(action="next_question", gap=None, note="Covered sharding by user id.") -> str:
    return json.dumps({"action": action, "gap": gap, "note": note})


def inputs() -> InterviewerInputs:
    return InterviewerInputs(
        role=JobRole.backend,
        level=Level.mid,
        interview_type=InterviewType.technical,
        question_count=5,
        job_description=None,
        turns=[QuestionTurn("How would you shard it?", "technical", "By user id.", None)],
    )


def run(model, *, seconds: float = 30, context=CONTEXT_MANAGER):
    clock = Clock()
    return decide(
        model,
        context,
        uuid.uuid7(),
        inputs(),
        Deadline(clock, seconds),
        max_tokens=200,
        clock=clock,
        sleep=clock.sleep,
    )


def call_lines(app_logs):
    return [r.getMessage() for r in app_logs.records if r.name == "app.llm" and r.getMessage().startswith("llm_call")]


def outcomes(app_logs):
    return [line.split("outcome=")[1].split()[0] for line in call_lines(app_logs)]


def test_the_schema_requires_every_field():  # FR6: required fields, nullable where "none" is valid
    schema = ModelDecision.model_json_schema()
    assert set(schema["required"]) == {"action", "gap", "note"}


def test_a_valid_decision_is_used_with_its_usage(app_logs):  # FR6, AC6
    model = FakeChatModel([fake_reply(decision("follow_up", "no_tradeoff"), input_tokens=300, output_tokens=20)])

    found, results, version = run(model)

    assert found is not None and (found.action, found.gap) == (FollowUpAction.follow_up, FollowUpGap.no_tradeoff)
    assert found.note == "Covered sharding by user id."
    [result] = results
    assert (result.prompt_tokens, result.completion_tokens) == (300, 20) and version == DECISION_PROMPT_VERSION
    [line] = call_lines(app_logs)
    assert "outcome=ok" in line and "action=follow_up" in line and "gap=no_tradeoff" in line
    assert "sharding" not in line  # the note never reaches the log


def test_a_reply_that_breaks_the_schema_is_retried(app_logs):  # EC2
    model = FakeChatModel([json.dumps({"action": "dance"}), decision()])

    found, results, _ = run(model)

    assert found is not None and found.action == FollowUpAction.next_question and len(results) == 2
    assert outcomes(app_logs) == ["invalid_reply:schema", "ok"]


def test_a_schema_valid_reply_the_parser_rejects_is_retried(app_logs):  # EC14: the parser is the second check
    model = FakeChatModel([decision("follow_up", None), decision("next_question", "no_how"), decision()])

    found, results, _ = run(model)

    # Two attempts at most: both broke a gap rule the schema can't express.
    assert found is None and len(results) == 2
    assert outcomes(app_logs) == ["invalid_reply:missing_gap", "invalid_reply:unexpected_gap"]


def test_a_bad_note_is_dropped_and_the_decision_kept(app_logs):  # EC14
    model = FakeChatModel([decision(note="x" * (NOTE_MAX_LENGTH + 1))])

    found, _, _ = run(model)

    assert found is not None and found.note is None and found.note_dropped == "too_long"
    assert any("note_dropped" in r.getMessage() for r in app_logs.records)


def test_an_empty_reply_is_not_retried(app_logs):  # EC2
    model = FakeChatModel([fake_reply("", finish_reason="MAX_TOKENS"), decision()])

    found, results, _ = run(model)

    assert found is None and results == [] and len(model.calls) == 1
    assert outcomes(app_logs) == ["empty_reply"]


def test_a_transport_error_is_retried_by_the_call_layer_only(app_logs):  # EC3, AC9
    model = FakeChatModel([gx.ServiceUnavailable("down")] * (1 + settings.llm_max_retries) + [decision()])

    found, results, _ = run(model)

    assert found is None and results == [] and len(model.calls) == 1 + settings.llm_max_retries
    assert outcomes(app_logs) == ["LLMServerError"]


def test_no_call_when_only_the_write_reserve_is_left():  # EC10
    model = FakeChatModel([decision()])

    found, results, _ = run(model, seconds=WRITE_RESERVE_SECONDS)

    assert (found, results, model.calls) == (None, [], [])


def test_the_call_never_runs_past_the_decide_cap():  # FR6: cap DECIDE_MAX_SECONDS, write reserve kept
    model = FakeChatModel([decision()])

    run(model, seconds=30)

    [(_, kwargs)] = model.calls
    assert kwargs["timeout"] <= DECIDE_MAX_SECONDS


def test_a_context_too_large_makes_no_call(app_logs):  # EC13
    def build(*_):
        raise ContextTooLargeError(SimpleNamespace(task=DECISION_TASK))  # pyright: ignore[reportArgumentType]

    model = FakeChatModel([decision()])

    found, _, _ = run(model, context=SimpleNamespace(build=build))

    assert found is None and model.calls == []
    assert outcomes(app_logs) == ["context_too_large"]


def test_one_generation_per_call_with_the_decide_labels():  # FR10, AC10
    client = FakeClient()
    model = FakeChatModel([decision()])
    model.callbacks = [TracerHandle(Tracer(client))]

    run(model)

    [generation] = client.generations
    metadata = generation.kwargs["metadata"]
    assert (metadata["task"], metadata["prompt_version"]) == (DECISION_TASK, DECISION_PROMPT_VERSION)
    assert metadata["budget_left_ms"] == 30000
