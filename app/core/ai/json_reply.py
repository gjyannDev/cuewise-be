"""Reading a model's JSON reply: one optional ```json fence around one JSON object, nothing else.

Model output is untrusted. A reply that is not a single JSON object raises InvalidReplyError with a short
machine-readable reason (logged, never shown to users). Each feature validates the object's fields itself.
"""

import json
import re

# One optional ```json fence around the whole reply; anything before or after it makes the reply invalid.
_FENCE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.DOTALL)


class InvalidReplyError(Exception):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


def load_object(raw: str) -> dict:
    """The reply as a JSON object: one optional fence around it, nothing else before or after."""
    text = raw.strip()
    if text.startswith("```"):
        fenced = _FENCE.match(text)
        if fenced is None:
            raise InvalidReplyError("fence")
        text = fenced.group(1)
    try:
        data = json.loads(text)
    except ValueError as exc:
        raise InvalidReplyError("not_json") from exc
    if not isinstance(data, dict):
        raise InvalidReplyError("not_object")
    return data
