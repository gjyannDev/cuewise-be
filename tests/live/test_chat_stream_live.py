"""Opt-in spike (U3b1 FR1): how the real Gemini chat model streams through LangChain's `astream`. Real calls, so it
never runs by default.

Run it with:  LLM_LIVE_TEST=1 uv run pytest tests/live/test_chat_stream_live.py -q -s
(PowerShell:  $env:LLM_LIVE_TEST = "1"; uv run pytest tests/live/test_chat_stream_live.py -q -s)
(needs LLM_PROVIDERS and LLM_GOOGLE_* in .env). Each test prints its findings; record them in
docs/features/u3b1-interview-calls/learnings.md. What it settles before write-stream moves (stage 3):
- a stream's merged usage and finish reason, next to a blocking call of the same prompt;
- a failure before the first chunk (a tiny timeout) and how `to_llm_error` maps it;
- whether the model `timeout` is one deadline for the whole stream (a stream cut after some chunks).
"""

import asyncio
import os
import time

import pytest
from langchain_core.messages import AIMessageChunk, HumanMessage, SystemMessage

from app.core.ai.chat_errors import to_llm_error
from app.core.ai.factory import build_chat_model
from app.core.config import settings

pytestmark = pytest.mark.skipif(
    os.getenv("LLM_LIVE_TEST") != "1",
    reason="real LLM call: set LLM_LIVE_TEST=1 (LLM_PROVIDERS + its LLM_<VENDOR>_* settings come from the environment)",
)

SHORT = [
    SystemMessage("You are an interviewer. Reply with one interview question for a junior backend developer."),
    HumanMessage("Ask the next question."),
]
LONG = [
    SystemMessage("You write long, detailed answers."),
    HumanMessage("Explain HTTP caching in about 800 words: headers, validation, CDNs and common mistakes."),
]


def _model(**update):
    model = build_chat_model(settings).members[0][1]
    return model.model_copy(update=update)


async def _stream(model, messages) -> tuple[list[AIMessageChunk], float | None]:
    chunks: list[AIMessageChunk] = []
    start = time.perf_counter()
    first_ms = None
    async for chunk in model.astream(messages):
        if first_ms is None:
            first_ms = (time.perf_counter() - start) * 1000
        chunks.append(chunk)
    return chunks, first_ms


def test_stream_usage_and_finish_reason_match_a_blocking_call():
    model = _model(max_output_tokens=settings.llm_max_tokens)
    chunks, first_ms = asyncio.run(_stream(model, SHORT))
    merged = chunks[0]
    for chunk in chunks[1:]:
        merged = merged + chunk
    blocking = model.invoke(SHORT)

    print(f"\nchunks={len(chunks)} first_chunk_ms={first_ms:.0f}")
    print(f"per-chunk usage={[c.usage_metadata for c in chunks]}")
    print(f"last chunk metadata={chunks[-1].response_metadata}")
    print(f"stream usage={merged.usage_metadata} finish={merged.response_metadata.get('finish_reason')}")
    print(f"blocking usage={blocking.usage_metadata} finish={blocking.response_metadata.get('finish_reason')}")
    assert merged.text.strip()
    assert merged.usage_metadata and blocking.usage_metadata
    # Same prompt: the input side must match; the output side differs per reply, so it is printed, not compared.
    assert merged.usage_metadata["input_tokens"] == blocking.usage_metadata["input_tokens"]
    assert merged.response_metadata.get("finish_reason") == "STOP"


def test_tiny_timeout_fails_before_the_first_chunk():
    model = _model(timeout=0.001)
    chunks: list[AIMessageChunk] = []

    async def run():
        async for chunk in model.astream(SHORT):
            chunks.append(chunk)

    with pytest.raises(Exception) as info:
        asyncio.run(run())
    mapped = to_llm_error(info.value)
    print(f"\nraw={type(info.value).__module__}.{type(info.value).__name__} mapped={type(mapped).__name__}")
    assert chunks == []


def test_whether_the_timeout_bounds_the_whole_stream():
    # Long enough for the first chunk, too short for an ~800-word reply if the deadline covers the whole stream.
    timeout = float(os.getenv("LLM_STREAM_SPIKE_TIMEOUT", "3"))
    model = _model(timeout=timeout, max_output_tokens=2048)
    chunks: list[AIMessageChunk] = []
    start = time.perf_counter()
    error: BaseException | None = None

    async def run():
        async for chunk in model.astream(LONG):
            chunks.append(chunk)

    try:
        asyncio.run(run())
    except Exception as exc:  # noqa: BLE001 - the finding is which error, and after how many chunks
        error = exc
    elapsed = time.perf_counter() - start
    text_chars = sum(len(c.text) for c in chunks)
    raw = f"{type(error).__module__}.{type(error).__name__}" if error else None
    mapped = type(to_llm_error(error)).__name__ if error else None
    print(
        f"\ntimeout={timeout}s elapsed={elapsed:.1f}s chunks={len(chunks)} chars={text_chars} "
        f"error={raw} mapped={mapped}"
    )
    print("finding: " + ("timeout cut the stream after text (one deadline for the whole call)" if error and chunks
          else "stream finished past the timeout (per-read deadline)" if not error and elapsed > timeout
          else "inconclusive: raise LLM_STREAM_SPIKE_TIMEOUT or lengthen the prompt"))
