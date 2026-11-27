"""End-of-interview feedback on the LangChain call layer (U3b1 step 16, FR8, AC8, AC10).

`FeedbackGenerator.score` sends the `ModelScore` schema through `complete_structured`, and `parse_score_reply` still
checks the reply text (quotes, criteria, caps); `.write` goes through `complete_chat` and `parse_write_reply`. Attempt
limits, `retry_skipped:no_time`, the failure codes and the Tracer steps are unchanged. Fake chat model, fake clock.
"""

import json
import uuid

from google.api_core import exceptions as gx
from pydantic import PrivateAttr

from app.core.ai.chat_fake import FakeChatModel, fake_reply
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.tracing import Tracer
from app.core.config import settings
from app.modules.interviews.ai.interviews_context import (
    CONTEXT_MANAGER,
    FeedbackScoreInputs,
    FeedbackWriteInputs,
)
from app.modules.interviews.ai.interviews_feedback import (
    FeedbackThread,
    ThreadTurn,
    WriteText,
    compute_overall,
    stored_scores,
)
from app.modules.interviews.ai.interviews_feedback_turn import FeedbackGenerator
from app.modules.interviews.ai.interviews_model_schemas import ModelScore
from app.modules.interviews.constants.interviews_constants import (
    CATEGORY_CRITERIA,
    FEEDBACK_SCORE_STEP,
    FEEDBACK_SCORE_TASK,
    FEEDBACK_WRITE_TASK,
    MIN_SECONDS_FOR_RETRY,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
    QuestionKind,
)
from tests.core.ai.test_tracing import FakeClient

B = QuestionCategory.behavioral
ANSWER = "I led the migration of our billing service to a queue so that retries stopped double charging customers."
QUOTE = "led the migration of our billing service"
THREADS = tuple(
    FeedbackThread(n, B, f"Main question {n}?", (ThreadTurn(f"Main question {n}?", ANSWER, QuestionKind.main),))
    for n in (1, 2)
)


def score_json(quote=QUOTE, **extra) -> str:
    questions = [
        {
            "main_number": t.main_number,
            "scores": {c.value: 3 for c in CATEGORY_CRITERIA[B]},
            "evidence": [{"criterion": CATEGORY_CRITERIA[B][0].value, "quote": quote, "reason": "Names the change."}],
        }
        for t in THREADS
    ]
    return json.dumps({"enough_evidence": True, "questions": questions} | extra)


def write_text() -> str:
    return WriteText(
        "You told clear stories with real results.",
        ("You named the change you made.", "You gave a measured result."),
        ("Say more about the trade-offs.", "Keep the context shorter."),
        ("Practise two stories out loud.",),
        {1: "Good story; add a number.", 2: "Clear; add the result."},
    ).render()


class Clock:
    def __init__(self):
        self.now = 0.0

    def __call__(self) -> float:
        return self.now


def generator(model, clock=None, tracer=None) -> FeedbackGenerator:
    return FeedbackGenerator(
        model,
        CONTEXT_MANAGER,
        score_max_tokens=4000,
        write_max_tokens=1500,
        score_temperature=0.2,
        clock=clock or Clock(),
        tracer=tracer,
    )


def score_inputs() -> FeedbackScoreInputs:
    return FeedbackScoreInputs(JobRole.backend, Level.junior, InterviewType.behavioral, None, THREADS)


def score(model, *, seconds=60.0, clock=None, tracer=None):
    gen = generator(model, clock, tracer)
    return gen.score(uuid.uuid7(), score_inputs(), gen.deadline(seconds))


def write(model, *, seconds=60.0):
    gen = generator(model)
    scored = generator(FakeChatModel([score_json()])).score(uuid.uuid7(), score_inputs(), gen.deadline(60))
    assert scored.result is not None
    stored = stored_scores(THREADS, scored.result.questions)
    inputs = FeedbackWriteInputs(
        JobRole.backend, Level.junior, InterviewType.behavioral, compute_overall(scored.result.questions), stored
    )
    return gen.write(uuid.uuid7(), inputs, [1, 2], gen.deadline(seconds))


def test_the_score_schema_requires_every_field():  # FR8: required fields (the U3a lesson)
    schema = ModelScore.model_json_schema()
    assert set(schema["required"]) == {"enough_evidence", "questions"}
    question = schema["$defs"]["ModelQuestionScore"]
    assert set(question["required"]) == {"main_number", "scores", "evidence"}
    assert set(schema["$defs"]["ModelEvidence"]["required"]) == {"criterion", "quote", "reason"}


def test_a_valid_score_reply_is_used_with_the_temperature_and_cap():  # FR8, AC8
    model = FakeChatModel([fake_reply(score_json(), input_tokens=900, output_tokens=120)])

    scored = score(model)

    assert scored.result is not None and len(scored.result.questions) == 2 and scored.failure is None
    assert (scored.results[0].prompt_tokens, scored.results[0].completion_tokens) == (900, 120)
    [(_, kwargs)] = model.calls
    assert (kwargs["temperature"], kwargs["max_output_tokens"]) == (0.2, 4000)


def test_a_reply_that_breaks_the_schema_is_retried():  # EC2
    model = FakeChatModel([json.dumps({"enough_evidence": True}), score_json()])

    scored = score(model)

    assert scored.result is not None and len(scored.results) == 2


def test_a_schema_valid_reply_with_a_made_up_quote_is_rejected_by_the_parser():  # the second check
    model = FakeChatModel([score_json(quote="a sentence the candidate never said"), score_json(quote="nor this one")])

    scored = score(model)

    assert scored.result is None and scored.failure == "invalid_reply:quote_not_found" and scored.quotes_rejected == 2


def test_a_cut_off_reply_is_truncated_even_if_it_parses():  # EC2: finish=length
    model = FakeChatModel([fake_reply(score_json(), finish_reason="MAX_TOKENS")] * 2)

    assert score(model).failure == "invalid_reply:truncated"


def test_an_empty_reply_keeps_its_failure_code():  # EC2: `empty_reply` is the stored reason and the hint's key
    model = FakeChatModel([fake_reply(""), score_json()])

    scored = score(model)

    assert scored.result is None and scored.failure == "empty_reply" and len(model.calls) == 1


def test_a_transport_error_is_retried_by_the_call_layer_then_fails():  # EC3
    model = FakeChatModel([gx.ServiceUnavailable("down")] * (1 + settings.llm_max_retries) + [score_json()])

    scored = score(model)

    assert scored.result is None and scored.failure == "LLMServerError"
    assert len(model.calls) == 1 + settings.llm_max_retries


class SlowFirstCall(FakeChatModel):
    """Uses up the budget on its first call, so a retry would start with less than MIN_SECONDS_FOR_RETRY left."""

    _clock: Clock = PrivateAttr(default_factory=Clock)

    def _generate(self, *args, **kwargs):
        if not self.calls:
            self._clock.now += 60 - MIN_SECONDS_FOR_RETRY + 1
        return super()._generate(*args, **kwargs)


def test_no_retry_when_too_little_time_is_left():  # EC10: retry_skipped:no_time
    model = SlowFirstCall(["not json", score_json()])
    client = FakeClient()

    scored = score(model, clock=model._clock, tracer=Tracer(client))

    assert scored.result is None and len(model.calls) == 1
    [step] = [t for t in client.traces if t.kwargs.get("name") == FEEDBACK_SCORE_STEP]
    assert step.final["output"]["attempts"] == ["invalid_reply:not_json", "retry_skipped:no_time"]


def test_no_call_without_time_left():  # EC10
    model = FakeChatModel([score_json()])

    scored = score(model, seconds=0)

    assert scored.failure == "no_time" and model.calls == []


def test_a_valid_write_reply_is_used():  # FR8
    model = FakeChatModel([write_text()])

    written = write(model)

    assert written.text is not None and written.failure is None
    [(_, kwargs)] = model.calls
    assert kwargs["temperature"] is None and kwargs["max_output_tokens"] == 1500


def test_two_bad_write_replies_leave_the_template_to_the_service():  # FR8: template fallback
    written = write(FakeChatModel(["not the sections", "still not"]))

    assert written.text is None and written.failure == "invalid_reply:format"


def test_generations_carry_the_feedback_labels():  # FR10, AC10
    client = FakeClient()
    model = FakeChatModel([score_json()])
    model.callbacks = [TracerHandle(Tracer(client))]

    score(model)

    [generation] = client.generations
    metadata = generation.kwargs["metadata"]
    assert (metadata["task"], metadata["attempt"]) == (FEEDBACK_SCORE_TASK, 1)
    assert "prompt_version" in metadata and metadata["budget_left_ms"] == 60000
    assert FEEDBACK_WRITE_TASK != FEEDBACK_SCORE_TASK
