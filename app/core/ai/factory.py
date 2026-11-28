from langchain_core.language_models import BaseChatModel

from app.core.config import ProviderConfig, Settings
from app.core.logging import get_logger

from .chat_chain import ChatChain
from .chat_tracing import TracerHandle
from .deepgram import DeepgramSynthesizer, DeepgramTranscriber
from .google_embedder import GoogleEmbedder
from .tracing import Tracer

stt_logger = get_logger("app.stt")
tts_logger = get_logger("app.tts")
rag_logger = get_logger("app.rag")


def build_chat_model(settings: Settings, *, model: str | None = None, tracer: Tracer | None = None) -> ChatChain:
    """The provider chain: one LangChain chat model per entry of `LLM_PROVIDERS`, in order, primary first.

    Retries belong to `RetryPolicy` in the call helpers (`chat.py`), so the vendor SDK's own are off. With an enabled
    `tracer`, every model carries it (`TracerHandle`) and the helper records one generation per call. `model`
    overrides the primary's model (the eval runner's --model). `Settings` guarantees at least one provider.
    """
    members = []
    for index, config in enumerate(settings.llm_provider_configs):
        chat_model = _CHAT_MODELS[config.name](config, settings, (model if index == 0 else None) or config.model)
        if tracer is not None and tracer.enabled:
            chat_model.callbacks = [TracerHandle(tracer)]
        members.append((config.name, chat_model))
    return ChatChain(tuple(members))


def _google_chat_model(config: ProviderConfig, settings: Settings, model: str) -> BaseChatModel:
    # Imported here: the vendor SDK (gRPC and all) loads only when Gemini is the configured provider.
    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(
        model=model,
        google_api_key=config.api_key,
        timeout=settings.llm_timeout_seconds,
        # The SDK counts attempts, so 1 is a single call: RetryPolicy is the only retry owner.
        max_retries=1,
        **settings.llm_chat_params(config.name),  # pyright: ignore[reportArgumentType]
    )


# One builder per vendor in LLM_VENDORS; a vendor without one fails loudly at startup instead of running without LLM.
_CHAT_MODELS = {"google": _google_chat_model}



def build_transcriber(settings: Settings) -> DeepgramTranscriber | None:
    """Speech-to-text for voice answers; None without a key. Never traced: audio and transcripts stay out of Langfuse.
    """
    speech = settings.speech
    if speech.api_key is None:
        stt_logger.warning("Transcription disabled (DEEPGRAM_API_KEY is empty): voice answers are off")
        return None
    return DeepgramTranscriber(
        api_key=speech.api_key.get_secret_value(),
        model=speech.stt.model,
        base_url=speech.base_url,
        timeout_seconds=speech.stt.timeout_seconds,
        max_retries=speech.stt.max_retries,
        total_budget_seconds=speech.stt.total_budget_seconds,
    )


def build_synthesizer(settings: Settings) -> DeepgramSynthesizer | None:
    """Text-to-speech for the interviewer's voice; None without a key (the interview still works, as text). Never
    traced, like the transcriber."""
    speech = settings.speech
    if speech.api_key is None:
        tts_logger.warning("Speech disabled (DEEPGRAM_API_KEY is empty): the interviewer voice is off")
        return None
    return DeepgramSynthesizer(
        api_key=speech.api_key.get_secret_value(),
        model=speech.tts.model,
        encoding=speech.tts.encoding,
        base_url=speech.base_url,
        timeout_seconds=speech.tts.timeout_seconds,
        max_retries=speech.tts.max_retries,
        total_budget_seconds=speech.tts.total_budget_seconds,
    )


def build_embedder(settings: Settings) -> GoogleEmbedder | None:
    """Embeddings for reference-note retrieval; None without the Google key (notes are then picked by role and level
    only). Never traced: the query is the candidate's job description."""
    key = settings.llm_google_api_key
    if key is None:
        rag_logger.warning(
            "Embeddings disabled (LLM_GOOGLE_API_KEY is empty): reference notes are picked by role and level only"
        )
        return None
    return GoogleEmbedder(
        api_key=key.get_secret_value(),
        model=settings.embedding_model,
        dimensions=settings.embedding_dimensions,
        base_url=settings.embedding_base_url,
        timeout_seconds=settings.embedding_timeout_seconds,
        max_retries=settings.embedding_max_retries,
    )
