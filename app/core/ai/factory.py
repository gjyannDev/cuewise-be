import logging

from app.core.config import Settings

from .openai_compatible import OpenAICompatibleProvider
from .provider import LLMProvider
from .tracing import Tracer, TracingProvider

logger = logging.getLogger("app.llm")


def build_provider(settings: Settings, *, model: str | None = None, tracer: Tracer | None = None) -> LLMProvider | None:
    """The one place that picks the implementation; swapping vendor or model is a config change.

    Only the primary (first listed) provider is built for now. The later ones in LLM_PROVIDERS are meant as a fallback
    chain, which comes with the multi-provider work. `model` overrides the primary's model (the eval runner's --model).
    With an enabled `tracer` the provider is wrapped so every call is recorded in Langfuse.
    """
    configs = settings.llm_provider_configs
    if not configs:
        logger.warning("LLM disabled (LLM_PROVIDERS is empty): questions will come from the question bank")
        return None
    primary = configs[0]
    provider = OpenAICompatibleProvider(
        api_key=primary.api_key.get_secret_value(),
        model=model or primary.model,
        base_url=primary.base_url,
        timeout_seconds=settings.llm_timeout_seconds,
        max_retries=settings.llm_max_retries,
        total_budget_seconds=settings.llm_total_budget_seconds,
    )
    return TracingProvider(provider, tracer) if tracer is not None and tracer.enabled else provider
