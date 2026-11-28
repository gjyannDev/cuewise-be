"""Langfuse tracing for the LangChain call layer, through our own `Tracer` (U3a, plan Approach A).

A LangChain *callback handler* is an object the framework notifies as a run happens (`on_chat_model_start`, ...);
it is how LangChain lets you observe a call without wrapping it. We use one handler per call to see the exact
messages LangChain sends to the model, and open the Langfuse generation from them. The call helper (`chat.py`) then
closes the generation once, with the final `LLMResult` or `LLMError`. That records:
one generation per call (retries are its `attempts`), the same labels, the same redaction and usage, nested under
the request's trace. Langfuse's own LangChain handler isn't used: it would be a second writer of generations and
couldn't reuse our redaction (see plan.md, Approaches Considered).
"""

from collections.abc import Mapping, Sequence
from typing import Any

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage

from .provider import ChatMessage, LLMError, LLMResult
from .tracing import Generation, TraceLabels, Tracer

_ROLES = {"system": "system", "human": "user", "ai": "assistant"}


class TracerHandle(BaseCallbackHandler):
    """Carries the app's Tracer on a chat model (`build_chat_model(..., tracer=)` attaches it), the way
    The factory attaches it to every model: services and feature code never pass a tracer around.
    It observes nothing itself; the call helper reads it to start each call's `ChatTrace`."""

    def __init__(self, tracer: Tracer):
        self.tracer = tracer


class ChatTrace(BaseCallbackHandler):
    """One traced call: started by the first model run it sees, finished by the call helper."""

    def __init__(self, tracer: Tracer, labels: TraceLabels, model_parameters: Mapping[str, int | float]):
        self._tracer = tracer
        self._labels = labels
        self._params = model_parameters
        self._generation: Generation | None = None

    def on_chat_model_start(self, serialized: dict[str, Any], messages: list[list[BaseMessage]], **_: Any) -> None:
        # A retried call runs the model again: the first run opens the one generation, later ones add nothing.
        if self._generation is None:
            self._start(_chat_messages(messages[0]) if messages else [])

    def succeed(self, result: LLMResult) -> None:
        self._started().succeed(result)

    def fail(self, error: LLMError, partial_text: str = "") -> None:
        # `partial_text`: what a stream had sent before it failed (shown to the user, so kept in the trace).
        self._started().fail(error, partial_text)

    def cancel(self, partial_text: str) -> None:
        """A stream closed before it finished (client left, or the turn's deadline ran out). No-op once ended."""
        self._started().cancel(partial_text)

    def _started(self) -> Generation:
        # A call that never reached the model (no budget left) still shows up, as today, with no input.
        return self._generation or self._start([])

    def _start(self, messages: Sequence[ChatMessage]) -> Generation:
        self._generation = self._tracer.start_generation(messages, self._labels, self._params)
        return self._generation


def _chat_messages(messages: Sequence[BaseMessage]) -> list[ChatMessage]:
    """LangChain messages in our own shape, so the trace reads as role + text."""
    return [
        ChatMessage(role=_ROLES.get(m.type, "user"), content=m.content if isinstance(m.content, str) else m.text)  # type: ignore[arg-type]
        for m in messages
    ]
