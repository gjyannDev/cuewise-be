"""The `llm` fixture (U3b1): the chat model the app gets serves every task, blocking or streamed, from the scripted
fakes, routed by system prompt."""

import anyio
import pytest
from langchain_core.messages import HumanMessage, SystemMessage

from app.core.ai.provider import LLMResult, LLMTimeoutError
from tests.modules.interviews.conftest import (
    _DECISION_MARKER,
    _SCORE_MARKER,
    _SUMMARY_MARKER,
    _WRITE_MARKER,
)

MESSAGES = [SystemMessage("You are the interviewer. rest of the prompt"), HumanMessage("the answer")]


def _ask(llm, system: str, **limits):
    model = llm.chat.model_copy(update=limits) if limits else llm.chat
    return model.invoke([SystemMessage(system + " rest of the prompt"), HumanMessage("the answer")])


async def _streamed(llm) -> str:
    return "".join([chunk.text async for chunk in llm.chat.astream(MESSAGES)])


def test_one_write_script_serves_blocking_and_streamed_calls_in_order(llm):
    llm.script("First.", "Second.")
    assert _ask(llm, "You are the interviewer.").text == "First."
    assert anyio.run(_streamed, llm) == "Second."
    assert len(llm.fake.calls) == 2
    assert llm.fake.calls[0][1].content == "the answer"


@pytest.mark.parametrize(
    ("marker", "script", "name"),
    [(_DECISION_MARKER, "script_decide", "decide"), (_SCORE_MARKER, "script_score", "score"), (_WRITE_MARKER, "script_write", "write")],
)
def test_the_chat_model_routes_by_system_prompt(llm, marker, script, name):
    getattr(llm, script)("Routed.")
    assert _ask(llm, marker).text == "Routed."
    assert len(getattr(llm, name).calls) == 1 and llm.fake.calls == []


def test_the_summary_goes_to_its_own_chat_fake(llm):
    llm.script_summary("A summary.")
    assert _ask(llm, _SUMMARY_MARKER, timeout=7).text == "A summary."
    [(_messages, kwargs)] = llm.summary.calls
    assert kwargs["timeout"] == 7 and llm.fake.calls == []


def test_a_scripted_error_reaches_the_chat_model_caller_unchanged(llm):
    error = LLMTimeoutError("slow")
    llm.script(error)
    with pytest.raises(LLMTimeoutError) as info:
        _ask(llm, "You are the interviewer.")
    assert info.value is error


def test_usage_finish_reason_and_budget_cross_over(llm):
    llm.script(LLMResult(text="Cut", model="m1", prompt_tokens=11, completion_tokens=4, latency_ms=0, finish_reason="length", attempts=1))
    message = _ask(llm, "You are the interviewer.", timeout=3.5)
    assert (message.usage_metadata["input_tokens"], message.usage_metadata["output_tokens"]) == (11, 4)
    assert message.response_metadata["finish_reason"] == "MAX_TOKENS" and message.response_metadata["model_name"] == "m1"
    assert llm.fake.budgets == [3.5]
