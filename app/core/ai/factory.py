import logging

from app.core.config import Settings

from .openrouter import OpenRouterProvider
from .provider import LLMProvider

logger = logging.getLogger("app.llm")


def build_provider(settings: Settings) -> LLMProvider | None:
    """The one place that picks the implementation; swapping vendor or model is a config change."""
    if settings.openrouter_api_key is None or settings.llm_model is None:
        logger.warning("LLM disabled (OPENROUTER_API_KEY and LLM_MODEL unset): interviewer reactions will be null")
        return None
    return OpenRouterProvider(
        api_key=settings.openrouter_api_key.get_secret_value(),
        model=settings.llm_model,
        base_url=settings.llm_base_url,
        timeout_seconds=settings.llm_timeout_seconds,
        max_retries=settings.llm_max_retries,
        total_budget_seconds=settings.llm_total_budget_seconds,
    )
