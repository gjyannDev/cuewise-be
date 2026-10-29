"""Opt-in: real calls to OpenRouter. Costs a tiny amount of money, so it never runs by default.

Run it with:  LLM_LIVE_TEST=1 uv run pytest tests/live -q -s
(needs OPENROUTER_API_KEY and LLM_MODEL in .env). It confirms the response-shape assumptions in the spec and that the
configured model can follow the interviewer's JSON contract.
"""

import os

import pytest

from app.core.ai.factory import build_provider
from app.core.config import settings
from app.modules.interviews.interviews_constants import InterviewType, JobRole, Level
from app.modules.interviews.interviews_reply import parse_interviewer_reply
from app.modules.interviews.interviews_utils import QuestionTurn, build_interviewer_messages, render_interviewer_prompt

pytestmark = pytest.mark.skipif(
    os.getenv("LLM_LIVE_TEST") != "1" or not settings.llm_configured,
    reason="real LLM call: set LLM_LIVE_TEST=1 and configure OPENROUTER_API_KEY + LLM_MODEL",
)


def test_real_model_writes_a_valid_next_question():  # llm-interviewer AC20
    provider = build_provider(settings)
    assert provider is not None
    asked = "Tell me about a time you disagreed with a teammate."
    system = render_interviewer_prompt(
        role=JobRole.backend,
        level=Level.junior,
        interview_type=InterviewType.mixed,
        question_number=2,
        question_count=5,
    )
    messages = build_interviewer_messages(
        system,
        "Backend developer for a payments API in Python.",
        [QuestionTurn(asked, "behavioral", "We argued about REST vs GraphQL, so I built two prototypes.")],
    )
    try:
        result = provider.complete(messages, max_tokens=settings.llm_max_tokens)
    finally:
        provider.close()

    usage = (
        f"model={result.model} tokens={result.prompt_tokens}/{result.completion_tokens} finish={result.finish_reason}"
    )
    print(f"\n{usage} latency_ms={result.latency_ms}\nraw={result.text!r}")
    assert result.prompt_tokens and result.completion_tokens
    reply = parse_interviewer_reply(result.text, interview_type=InterviewType.mixed, earlier_questions=[asked])
    print(f"question={reply.question!r} category={reply.category}")
