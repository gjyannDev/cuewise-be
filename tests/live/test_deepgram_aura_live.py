"""Opt-in: real calls to Deepgram Aura text-to-speech (interview-room Phase 0 spike). Costs real characters, so it
never runs by default.

Run it with:  SPEECH_LIVE_TEST=1 uv run pytest tests/live/test_deepgram_aura_live.py -q -s
(needs DEEPGRAM_API_KEY in .env). It confirms the voice, the encoding and its Content-Type, and prints the latency and
size of a short reaction, a typical question and the longest bank question, for the record in task.md.
"""

import os

import pytest

from app.core.ai.deepgram import SPEAK_CONTENT_TYPES
from app.core.ai.factory import build_synthesizer
from app.core.config import settings
from app.modules.interviews.constants.interviews_constants import REACTION_POOLS
from app.modules.interviews.utils.interviews_utils import QUESTION_BANK

pytestmark = [
    pytest.mark.anyio,
    pytest.mark.skipif(
        os.getenv("SPEECH_LIVE_TEST") != "1" or settings.speech.api_key is None,
        reason="real Aura call: set SPEECH_LIVE_TEST=1 and DEEPGRAM_API_KEY",
    ),
]


@pytest.fixture
def anyio_backend():
    return "asyncio"


def _lines() -> dict[str, str]:
    reaction = next(iter(REACTION_POOLS.values()))[0]
    questions = sorted((q.text for q in QUESTION_BANK), key=len)
    return {"reaction": reaction, "typical question": questions[len(questions) // 2], "longest question": questions[-1]}


async def test_aura_speaks_each_kind_of_line_in_the_configured_format():
    synthesizer = build_synthesizer(settings)
    assert synthesizer is not None
    try:
        for label, text in _lines().items():
            result = await synthesizer.synthesize(text)

            assert result.audio
            assert result.content_type == SPEAK_CONTENT_TYPES[settings.speech.tts.encoding]
            print(
                f"\n[aura] {label}: chars={result.characters} latency_ms={result.latency_ms} "
                f"bytes={len(result.audio)} attempts={result.attempts} type={result.content_type} model={result.model}"
            )
    finally:
        await synthesizer.aclose()
