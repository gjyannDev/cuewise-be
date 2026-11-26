"""The worst-case number of HTTP calls one logical call can make, across both retry layers (U2 AC10, EC14, EC15).

Transport retries (`RetryPolicy`, inside each vendor adapter) and content retries (`ReplyAttempts`, in the interview
reply loops) multiply: one LLM task makes at most (llm_max_retries + 1) x MAX_REPLY_ATTEMPTS HTTP calls. These tests
drive the real adapters on a mock transport, so a new retry layer, or a changed limit, makes them fail loudly.
"""

import json
import uuid

import httpx
import pytest

from app.core.ai.deepgram import DeepgramSynthesizer, DeepgramTranscriber
from app.core.ai.embedder import EmbeddingKind
from app.core.ai.google_embedder import GoogleEmbedder
from app.core.ai.openai_compatible import OpenAICompatibleProvider
from app.core.ai.provider import LLMServerError
from app.core.config import settings
from app.modules.interviews.ai.interviews_context import (
    InterviewerInputs,
    build_context_manager,
)
from app.modules.interviews.ai.interviews_decide import decide
from app.modules.interviews.ai.interviews_turn_limits import Deadline
from app.modules.interviews.constants.interviews_constants import (
    MAX_REPLY_ATTEMPTS,
    InterviewType,
    JobRole,
    Level,
)
from app.modules.interviews.utils.interviews_utils import QuestionTurn

LLM_WORST_CASE = (settings.llm_max_retries + 1) * MAX_REPLY_ATTEMPTS


@pytest.fixture
def anyio_backend():
    return "asyncio"


class Clock:
    """Fake time: only the retry waits move it, so the HTTP calls themselves are instant."""

    def __init__(self):
        self.now = 0.0

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.now += seconds

    async def async_sleep(self, seconds: float) -> None:
        self.now += seconds


def counting(responses):
    """A transport handler that answers from `responses` in turn and counts the requests."""
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return responses(len(calls))

    return handler, calls


def malformed_reply() -> httpx.Response:
    # A 200 whose text the decide parser rejects: a content failure, so the reply loop asks again.
    body = {"choices": [{"message": {"content": json.dumps({"action": "dance"})}, "finish_reason": "stop"}]}
    return httpx.Response(200, json=body)


def run_decide(handler, clock: Clock):
    provider = OpenAICompatibleProvider(
        api_key="test-key",
        model="vendor/model-x",
        base_url="https://llm.test/v1",
        timeout_seconds=settings.llm_timeout_seconds,
        max_retries=settings.llm_max_retries,
        total_budget_seconds=settings.llm_total_budget_seconds,
        transport=httpx.MockTransport(handler),
        sleep=clock.sleep,
        clock=clock,
    )
    inputs = InterviewerInputs(
        role=JobRole.backend,
        level=Level.mid,
        interview_type=InterviewType.technical,
        question_count=5,
        job_description=None,
        turns=[QuestionTurn("How would you shard it?", "technical", "By user id.", None)],
    )
    return decide(
        provider,
        build_context_manager(),
        uuid.uuid4(),
        inputs,
        Deadline(clock, settings.llm_total_budget_seconds),
        max_tokens=200,
        clock=clock,
    )


def test_both_layers_fully_used_never_exceed_the_worst_case():  # EC15
    clock = Clock()
    per_reply = settings.llm_max_retries + 1
    # Every reply attempt: transport failures until its last transport attempt, which gets a malformed reply.
    handler, calls = counting(lambda n: malformed_reply() if n % per_reply == 0 else httpx.Response(503))

    decision, results, _ = run_decide(handler, clock)

    assert decision is None
    assert len(results) == MAX_REPLY_ATTEMPTS
    assert len(calls) == LLM_WORST_CASE == 6  # 6 with today's defaults: (2 + 1) x 2


def test_a_transport_error_stops_the_reply_loop():  # EC14: the two layers never multiply on the same failure
    clock = Clock()
    handler, calls = counting(lambda n: httpx.Response(503))

    decision, results, _ = run_decide(handler, clock)

    assert decision is None and results == []
    assert len(calls) == settings.llm_max_retries + 1


def test_the_embedder_makes_at_most_its_retries_plus_one_calls():  # AC10
    clock = Clock()
    handler, calls = counting(lambda n: httpx.Response(503))
    embedder = GoogleEmbedder(
        api_key="test-key",
        model="gemini-embedding-001",
        dimensions=4,
        base_url="https://google.test/v1beta",
        timeout_seconds=settings.embedding_timeout_seconds,
        max_retries=settings.embedding_max_retries,
        transport=httpx.MockTransport(handler),
        sleep=clock.sleep,
        clock=clock,
    )

    with pytest.raises(LLMServerError):
        embedder.embed(["a"], kind=EmbeddingKind.query)

    assert len(calls) == settings.embedding_max_retries + 1 == 2


@pytest.mark.anyio
@pytest.mark.parametrize("direction", ["transcribe", "synthesize"])
async def test_deepgram_makes_at_most_its_retries_plus_one_calls_per_direction(direction):  # AC10
    clock = Clock()
    calls = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(503)

    common = {
        "api_key": "test-key",
        "base_url": "https://dg.test/",
        "transport": httpx.MockTransport(handler),
        "sleep": clock.async_sleep,
        "clock": clock,
    }
    with pytest.raises(LLMServerError):
        if direction == "transcribe":
            stt = settings.speech.stt
            adapter = DeepgramTranscriber(
                model="nova-3",
                timeout_seconds=stt.timeout_seconds,
                max_retries=stt.max_retries,
                total_budget_seconds=stt.total_budget_seconds,
                **common,
            )
            expected = stt.max_retries + 1
            await adapter.transcribe(b"audio", content_type="audio/webm")
        else:
            tts = settings.speech.tts
            adapter = DeepgramSynthesizer(
                model="aura-2-thalia-en",
                encoding="mp3",
                timeout_seconds=tts.timeout_seconds,
                max_retries=tts.max_retries,
                total_budget_seconds=tts.total_budget_seconds,
                **common,
            )
            expected = tts.max_retries + 1
            await adapter.synthesize("Hello.")

    assert len(calls) == expected == 2
