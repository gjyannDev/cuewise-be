"""The extraction call: scrubbed résumé text in, a validated profile out (resume-upload AC7, AC8).

The résumé is fenced as data inside <resume> markers, the input is capped, and the call is labelled `redact` so its
content never reaches Langfuse. One retry on a malformed reply, inside one total time budget; any provider error or
timeout ends the extraction (the caller maps it to PROFILE_EXTRACTION_FAILED).
"""

import re
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

from app.core.ai.json_reply import InvalidReplyError
from app.core.ai.provider import ChatMessage, LLMError, LLMProvider, LLMResult
from app.core.ai.tracing import REDACT_LABEL

from ..constants.profile_constants import (
    PROFILE_INPUT_MAX_CHARS,
    PROFILE_PROMPT_VERSION,
    PROFILE_TASK,
    PROFILE_TEMPERATURE,
    PROFILE_TOTAL_SECONDS,
)
from ..schemas.profile_schema import CandidateProfile
from .profile_reply import parse_profile_reply

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


def load_prompt(version: str = PROFILE_PROMPT_VERSION) -> str:
    return (PROMPTS_DIR / f"{version}.md").read_text(encoding="utf-8")


def build_messages(text: str) -> tuple[list[ChatMessage], str, bool]:
    """The messages, the fenced text, and whether it was cut to the cap (the first part is kept)."""
    text = _FENCE_MARKER.sub(" ", text)
    cut = len(text) > PROFILE_INPUT_MAX_CHARS
    if cut:
        # Keep the line breaks (the model reads the layout); drop the word the cap fell inside.
        head = text[:PROFILE_INPUT_MAX_CHARS]
        text = re.sub(r"\s+\S*$", "", head) or head
    messages = [
        ChatMessage(role="system", content=load_prompt()),
        ChatMessage(role="user", content=f"<resume>\n{text}\n</resume>"),
    ]
    return messages, text, cut


def extract_profile(
    llm: LLMProvider, text: str, *, max_tokens: int, clock: Callable[[], float]
) -> Extraction:
    """Raises ExtractionFailedError, or EmptyProfileError when a valid reply holds no skills and no roles."""
    messages, model_input, cut = build_messages(text)
    end = clock() + PROFILE_TOTAL_SECONDS
    results: list[LLMResult] = []
    reason = "no_time"
    for _ in range(MAX_ATTEMPTS):
        left = end - clock()
        if left <= 0:
            reason = "no_time"
            break
        try:
            result = llm.complete(
                messages,
                max_tokens=max_tokens,
                temperature=PROFILE_TEMPERATURE,
                budget_seconds=left,
                trace_labels={"task": PROFILE_TASK, "prompt_version": PROFILE_PROMPT_VERSION, REDACT_LABEL: True},
            )
        except LLMError as exc:
            raise ExtractionFailedError(type(exc).__name__, results) from exc
        results.append(result)
        if not result.text.strip():
            reason = "empty_reply"
            continue
        try:
            profile = parse_profile_reply(result.text)
        except InvalidReplyError as exc:
            reason = f"invalid_reply:{exc.reason}"
            continue
        return Extraction(profile, model_input, cut, results)
    raise ExtractionFailedError(reason, results)
