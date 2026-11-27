"""The blocking write on the LangChain call layer (U3b1 step 5, FR5, AC5, AC10): same reply loop, fallbacks and log
lines as before the move, the call through `complete_chat`. The fake chat model; no network."""

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
from app.modules.interviews.ai.interviews_turn_limits import Deadline
from app.modules.interviews.ai.interviews_write import write
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_TASK,
    INTERVIEWER_V4_PROMPT_VERSION,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
)
from app.modules.interviews.utils.interviews_utils import QuestionTurn
from tests.core.ai.test_tracing import FakeClient

EARLIER = "Question 1 about queues?"
QUESTION = "How would you make a payment retry safe to repeat?"


def reply(question: str = QUESTION, category: str | None = "technical") -> str:
    return json.dumps({"question": question} | ({"category": category} if category else {}))


def inputs() -> InterviewerInputs:
    return InterviewerInputs(
        role=JobRole.backend,
        level=Level.mid,
        interview_type=InterviewType.technical,
        question_count=5,
        job_description=None,
        turns=[QuestionTurn(EARLIER, "technical", "Answer 1 text.")],
    )


def run(model, *, seconds: float = 30, follow_up_category=None, context=CONTEXT_MANAGER):
    deadline = Deadline(lambda: 0.0, seconds)
    return write(
        model, context, uuid.uuid7(), inputs(), deadline, follow_up_category=follow_up_category, max_tokens=200
    )


def call_lines(app_logs):
    return [r.getMessage() for r in app_logs.records if r.name == "app.llm" and r.getMessage().startswith("llm_call")]


def test_a_valid_reply_is_the_question_with_its_usage(app_logs):  # FR5, AC5
    model = FakeChatModel([fake_reply(reply(), input_tokens=120, output_tokens=15)])

    written = run(model)

    assert written.reply is not None and (written.reply.question, written.reply.category) == (QUESTION, "technical")
    [result] = written.results
    assert (result.prompt_tokens, result.completion_tokens, result.attempts) == (120, 15, 1)
    assert written.prompt_version == INTERVIEWER_V4_PROMPT_VERSION
    [(messages, kwargs)] = model.calls
    assert messages[0].type == "system" and kwargs["max_output_tokens"] == 200
    [line] = call_lines(app_logs)
    assert "outcome=ok" in line and "prompt_tokens=120" in line and QUESTION not in line


def test_an_invalid_reply_is_retried_once_then_used(app_logs):  # EC2
    model = FakeChatModel(["Sure! What is a mutex?", reply()])

    written = run(model)

    assert written.reply is not None and len(model.calls) == 2 and len(written.results) == 2
    assert [line.split("outcome=")[1].split()[0] for line in call_lines(app_logs)] == ["invalid_reply:not_json", "ok"]


def test_two_invalid_replies_give_no_question():  # EC2: the caller asks the bank
    written = run(FakeChatModel(["not json", reply(category="behavioral")]))  # second: wrong category

    assert written.reply is None and len(written.results) == 2


def test_a_repeated_question_is_an_invalid_reply():  # the code-side repeat check, unchanged
    written = run(FakeChatModel([reply(EARLIER), reply()]))

    assert written.reply is not None and written.reply.question == QUESTION and len(written.results) == 2


def test_an_empty_reply_is_not_retried(app_logs):  # EC2: an empty reply would fail the same way
    model = FakeChatModel([fake_reply("  ", finish_reason="MAX_TOKENS")])

    written = run(model)

    assert written.reply is None and written.results == [] and len(model.calls) == 1
    [line] = call_lines(app_logs)
    assert "outcome=empty_reply" in line and "finish=length" in line


def test_a_transport_error_is_retried_by_the_call_layer_only(app_logs):  # EC3
    model = FakeChatModel([gx.ServiceUnavailable("down")] * (1 + settings.llm_max_retries) + [reply()])

    written = run(model)

    # The call layer's retries are the only ones: write itself makes no further attempt.
    assert written.reply is None and len(model.calls) == 1 + settings.llm_max_retries
    [line] = call_lines(app_logs)
    assert "outcome=LLMServerError" in line and "down" not in line


def test_a_rejected_request_is_not_retried():  # EC3
    model = FakeChatModel([gx.PermissionDenied("bad key"), reply()])

    assert run(model).reply is None and len(model.calls) == 1


def test_no_call_without_time_left():  # EC10
    model = FakeChatModel([reply()])

    assert run(model, seconds=0).reply is None and model.calls == []


def test_a_context_too_large_makes_no_call(app_logs):  # EC13
    def build(*_):
        raise ContextTooLargeError(SimpleNamespace(task=INTERVIEWER_TASK))  # pyright: ignore[reportArgumentType]

    model = FakeChatModel([reply()])

    written = run(model, context=SimpleNamespace(build=build))

    assert written.reply is None and model.calls == []
    assert "outcome=context_too_large" in call_lines(app_logs)[0]


def test_a_follow_up_takes_the_main_questions_category():  # FR5: follow-up mode unchanged
    written = run(FakeChatModel([reply(category=None)]), follow_up_category=QuestionCategory.technical)

    assert written.reply is not None and written.reply.category == "technical"


def test_one_generation_per_call_with_the_write_labels():  # FR10, AC10
    client = FakeClient()
    model = FakeChatModel([reply()])
    model.callbacks = [TracerHandle(Tracer(client))]

    run(model)

    [generation] = client.generations
    metadata = generation.kwargs["metadata"]
    assert generation.kwargs["name"] == INTERVIEWER_TASK
    assert (metadata["task"], metadata["prompt_version"]) == (INTERVIEWER_TASK, INTERVIEWER_V4_PROMPT_VERSION)
    assert metadata["budget_left_ms"] == 30000
