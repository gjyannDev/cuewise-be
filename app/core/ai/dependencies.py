"""Request dependencies for the AI services every feature shares, built once at startup (app lifespan)."""

from fastapi import Request

from .chat import ChatModel
from .synthesizer import SpeechSynthesizer
from .tracing import Tracer
from .transcriber import Transcriber


def get_chat_model(request: Request) -> ChatModel:
    """The provider chain, built once at startup (app lifespan). Tests override this dependency."""
    return request.app.state.chat_model


def get_tracer(request: Request) -> Tracer:
    """Built once at startup (app lifespan); a disabled tracer when the lifespan didn't run."""
    return getattr(request.app.state, "tracer", None) or Tracer(None)


def get_transcriber(request: Request) -> Transcriber | None:
    """Built once at startup (app lifespan); None when no Deepgram key is configured or the lifespan didn't run."""
    return getattr(request.app.state, "transcriber", None)


def get_synthesizer(request: Request) -> SpeechSynthesizer | None:
    """Built once at startup (app lifespan); None when no Deepgram key is configured or the lifespan didn't run."""
    return getattr(request.app.state, "synthesizer", None)
