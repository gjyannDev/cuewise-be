"""The extraction call: scrubbed résumé text in, a validated profile out (resume-upload AC7, AC8).

The résumé is fenced as data inside <resume> markers, the input is capped, and the call is labelled `redact` so its
content never reaches Langfuse. One retry on a malformed reply, inside one total time budget; any provider error or
timeout ends the extraction (the caller maps it to PROFILE_EXTRACTION_FAILED).

On the LangChain layer since U3a: the model is given `ModelProfile` (every field required) as a JSON schema (`.with_structured_output`, through
`complete_structured`), so Gemini answers in that shape natively instead of being asked for JSON in prose. A reply
that still misses the schema, or an empty one, is a malformed reply and gets the second attempt, as before; the
clean-up (caps, dedupe, the empty-profile check) is the same `clean_profile` as for a JSON-text reply.
"""

import re
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

from app.core.ai.chat import ChatModel, complete_structured, fixed_prompt
from app.core.ai.prompts import load_prompt
from app.core.ai.provider import ChatMessage, LLMBadResponseError, LLMError, LLMResult
from app.core.ai.tracing import REDACT_LABEL

from ..constants.profile_constants import (
    PROFILE_INPUT_MAX_CHARS,
    PROFILE_PROMPT_VERSION,
    PROFILE_TASK,
    PROFILE_TEMPERATURE,
    PROFILE_TOTAL_SECONDS,
)
from ..schemas.profile_schema import CandidateProfile
from .profile_reply import ModelProfile, clean_profile

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"
MAX_ATTEMPTS = 2
# Anything that could close or reopen the fence is removed from the résumé text, so it stays inside the markers.
_FENCE_MARKER = re.compile(r"</?\s*resume\s*>", re.IGNORECASE)


class ExtractionFailedError(Exception):
    """No valid profile: `reason` is invalid_reply, empty_reply, no_time or the provider error's class (logged)."""

    def __init__(self, reason: str, results: list[LLMResult]):
        super().__init__(reason)
        self.reason = reason
        self.results = results


class Extraction(NamedTuple):
    profile: CandidateProfile
    model_input: str  # the text the model was given: grounding checks against exactly this
    cut: bool  # the input was over the cap and its end was cut
    results: list[LLMResult]  # one per attempt (tokens and latency are logged)


def build_messages(text: str) -> tuple[list[ChatMessage], str, bool]:
    """The messages, the fenced text, and whether it was cut to the cap (the first part is kept)."""
    text = _FENCE_MARKER.sub(" ", text)
    cut = len(text) > PROFILE_INPUT_MAX_CHARS
    if cut:
        # Keep the line breaks (the model reads the layout); drop the word the cap fell inside.
        head = text[:PROFILE_INPUT_MAX_CHARS]
        text = re.sub(r"\s+\S*$", "", head) or head
    messages = [
        ChatMessage(role="system", content=load_prompt(PROMPTS_DIR, PROFILE_PROMPT_VERSION)),
        ChatMessage(role="user", content=f"<resume>\n{text}\n</resume>"),
    ]
    return messages, text, cut


def extract_profile(
    model: ChatModel, text: str, *, max_tokens: int, clock: Callable[[], float]
) -> Extraction:
    """Raises ExtractionFailedError, or EmptyProfileError when a valid reply holds no skills and no roles."""
    messages, model_input, cut = build_messages(text)
    prompt = fixed_prompt(messages)
    end = clock() + PROFILE_TOTAL_SECONDS
    results: list[LLMResult] = []
    reason = "no_time"
    for _ in range(MAX_ATTEMPTS):
        left = end - clock()
        if left <= 0:
            reason = "no_time"
            break
        try:
            outcome = complete_structured(
                model,
                prompt,
                {},
                ModelProfile,
                max_tokens=max_tokens,
                temperature=PROFILE_TEMPERATURE,
                budget_seconds=left,
                labels={"task": PROFILE_TASK, "prompt_version": PROFILE_PROMPT_VERSION, REDACT_LABEL: True},
            )
        except LLMBadResponseError:
            # The model answered with nothing: a malformed reply (spec EC9), so the next attempt gets a chance.
            reason = "empty_reply"
            continue
        except LLMError as exc:
            raise ExtractionFailedError(type(exc).__name__, results) from exc
        results.append(outcome.result)
        if outcome.value is None:
            reason = "invalid_reply:schema"
            continue
        return Extraction(clean_profile(outcome.value), model_input, cut, results)
    raise ExtractionFailedError(reason, results)
