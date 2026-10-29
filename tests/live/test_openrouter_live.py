"""Opt-in: one real call to OpenRouter. Costs a tiny amount of money, so it never runs by default.

Run it with:  LLM_LIVE_TEST=1 uv run pytest tests/live -q -s
(needs OPENROUTER_API_KEY and LLM_MODEL in .env). It confirms the response-shape assumptions in the spec.
"""

import os

import pytest

from app.core.ai.factory import build_provider
from app.core.config import settings
from app.modules.interviews.interviews_constants import JobRole, Level
from app.modules.interviews.interviews_utils import Turn, build_llm_messages, render_reaction_prompt

pytestmark = pytest.mark.skipif(
    os.getenv("LLM_LIVE_TEST") != "1" or not settings.llm_configured,
    reason="real LLM call: set LLM_LIVE_TEST=1 and configure OPENROUTER_API_KEY + LLM_MODEL",
)


def test_real_reaction_has_text_usage_and_finish_reason():  # AC19
    provider = build_provider(settings)
    assert provider is not None
    messages = build_llm_messages(
        render_reaction_prompt(JobRole.backend, Level.junior),
        [
            Turn(
                "Tell me about a time you disagreed with a teammate.",
                "We argued about REST vs GraphQL, so I built two small prototypes and we compared them.",
                None,
            )
        ],
    )
    try:
        result = provider.complete(messages, max_tokens=settings.llm_max_tokens)
    finally:
        provider.close()

    reply = (
        f"model={result.model} tokens={result.prompt_tokens}/{result.completion_tokens} finish={result.finish_reason}"
    )
    print(f"\n{reply} latency_ms={result.latency_ms}\nreply={result.text!r}")
    assert result.text.strip()
    assert result.prompt_tokens and result.completion_tokens
    assert result.finish_reason in {"stop", "length"}
