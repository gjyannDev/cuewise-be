"""The provider chain (U3c step 1): `complete_chat`, `complete_structured` and `stream_chat` try the models of a
`ChatChain` in order. Only transport errors (timeout, 429, 5xx) move a call to the next provider; the turn deadline
bounds the whole chain; a stream commits to the provider that gave its first chunk. Spec AC1-AC3, AC5, EC1-EC7."""

import pytest
from google.api_core import exceptions as gx
from pydantic import BaseModel

from app.core.ai.chat import complete_structured
from app.core.ai.chat_chain import ChatChain
from app.core.ai.chat_fake import FakeChatModel, fake_chunks, fake_reply
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.provider import (
    LLMError,
    LLMRequestError,
    LLMResult,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.ai.tracing import Tracer
from tests.core.ai.test_chat import INPUTS, LABELS, PROMPT, call, slow
from tests.core.ai.test_chat_stream import run as run_stream
from tests.core.ai.test_retry import Clock
from tests.core.ai.test_tracing import FakeClient


def chain(*named: tuple[str, FakeChatModel]) -> ChatChain:
    return ChatChain(named)


def switches(app_logs):
    return [r for r in app_logs.records if r.getMessage().startswith("llm_provider_switch")]


# --- a blocking call ----------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "failure",
    [TimeoutError("slow"), gx.ResourceExhausted("429"), gx.ServiceUnavailable("503")],
    ids=["timeout", "rate_limit", "server_error"],
)
def test_a_transport_error_hands_the_call_to_the_next_provider(failure, app_logs):  # AC1, EC1, EC2
    first, second = FakeChatModel([failure]), FakeChatModel([fake_reply("From B.")])

    result = call(chain(("a", first), ("b", second)))

    assert result.text == "From B." and result.provider == "b"
    assert len(first.calls) == 1 and len(second.calls) == 1
    [switch] = switches(app_logs)
    assert switch.fields["from_provider"] == "a" and switch.fields["to_provider"] == "b"
    assert switch.fields["reason"] == type(failure).__name__ or switch.fields["reason"].startswith("LLM")
    assert "From B." not in str(switch.fields)  # names and error classes only, never text


def test_the_provider_that_answered_is_in_the_result_and_the_trace():  # AC1
    client = FakeClient()
    first, second = FakeChatModel([TimeoutError("slow")]), FakeChatModel([fake_reply("ok")])
    first.callbacks = [TracerHandle(Tracer(client))]

    call(chain(("a", first), ("b", second)))

    [generation] = client.generations
    assert generation.final["metadata"]["provider"] == "b"


def test_the_first_provider_that_answers_ends_the_call():
    first, second = FakeChatModel(["From A."]), FakeChatModel(["From B."])
    result = call(chain(("a", first), ("b", second)))
    assert result.provider == "a" and second.calls == []


def test_a_request_error_does_not_switch_so_a_bad_key_is_not_hidden():
    first, second = FakeChatModel([gx.PermissionDenied("bad key")]), FakeChatModel(["From B."])
    with pytest.raises(LLMRequestError):
        call(chain(("a", first), ("b", second)))
    assert second.calls == []


class Reply(BaseModel):
    name: str


def test_an_invalid_reply_never_switches_provider():  # AC3, EC3
    first, second = FakeChatModel(['{"nope": 1}']), FakeChatModel(['{"name": "Ada"}'])

    outcome = complete_structured(
        chain(("a", first), ("b", second)),
        PROMPT,
        INPUTS,
        Reply,
        max_tokens=100,
        budget_seconds=30,
        labels=LABELS,
        max_retries=2,
    )

    assert outcome.value is None and outcome.result.provider == "a"
    assert second.calls == []


def test_when_every_provider_fails_the_whole_chain_is_retried_then_the_last_error_raises():  # EC4, EC11
    down = [gx.ServiceUnavailable("503")] * 2
    first, second = FakeChatModel(down), FakeChatModel(down)

    with pytest.raises(LLMServerError):
        call(chain(("a", first), ("b", second)), max_retries=1)

    assert len(first.calls) == len(second.calls) == 2  # (1 + max_retries) rounds over the chain


def test_a_single_provider_chain_behaves_like_a_bare_model():  # EC11
    with pytest.raises(LLMServerError):
        call(chain(("a", FakeChatModel([gx.ServiceUnavailable("503")] * 3))), max_retries=2)


def test_the_next_provider_gets_only_the_time_left():  # AC5, EC7
    clock = Clock()
    first = slow([TimeoutError("slow")], clock, cost=12)
    second = FakeChatModel(["ok"])

    call(chain(("a", first), ("b", second)), clock, budget_seconds=20, timeout_seconds=15, max_retries=0)

    assert first.calls[0][1]["timeout"] == 15
    assert second.calls[0][1]["timeout"] == pytest.approx(8)  # 20 s budget - 12 s spent, under the 15 s cap


def test_no_time_left_starts_no_further_provider():  # AC5, EC7
    clock = Clock()
    first = slow([TimeoutError("slow")], clock, cost=20)
    second = FakeChatModel(["never"])

    with pytest.raises(LLMTimeoutError):
        call(chain(("a", first), ("b", second)), clock, budget_seconds=20, timeout_seconds=15, max_retries=0)

    assert second.calls == []


# --- a stream -----------------------------------------------------------------------------------------------------


@pytest.mark.anyio
async def test_a_stream_that_fails_before_its_first_chunk_switches_provider():  # AC2, EC6
    first = FakeChatModel([fake_chunks(gx.ServiceUnavailable("503"))])
    second = FakeChatModel([fake_chunks("How would ", "you shard it?")])

    *chunks, result = await run_stream(chain(("a", first), ("b", second)))

    assert chunks == ["How would ", "you shard it?"]
    assert isinstance(result, LLMResult) and result.provider == "b"


@pytest.mark.anyio
async def test_a_stream_that_fails_after_its_first_chunk_does_not_switch():  # AC2, EC5
    first = FakeChatModel([fake_chunks("How would ", gx.ServiceUnavailable("503"))])
    second = FakeChatModel([fake_chunks("never")])

    *chunks, error = await run_stream(chain(("a", first), ("b", second)))

    assert chunks == ["How would "]
    assert isinstance(error, LLMError) and error.after_output
    assert second.calls == []


@pytest.mark.anyio
async def test_a_stream_with_every_provider_down_raises_the_last_error():  # EC4
    down = [fake_chunks(gx.ServiceUnavailable("503"))] * 3
    first, second = FakeChatModel(down), FakeChatModel(down)

    [error] = await run_stream(chain(("a", first), ("b", second)))

    assert isinstance(error, LLMServerError) and not error.after_output
