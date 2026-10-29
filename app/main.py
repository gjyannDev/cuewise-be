from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from app.core.ai.factory import build_provider
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import RequestContextMiddleware
from app.modules.auth.auth_route import router as auth_router
from app.modules.interviews.interviews_route import router as interviews_router
from app.modules.users.users_route import router as users_router

setup_logging(settings.debug)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # One LLM client for the whole app (connection reuse); None when no key is configured.
    provider = build_provider(settings)
    app.state.llm_provider = provider
    try:
        yield
    finally:
        if provider is not None:
            provider.close()


app = FastAPI(title="Cuewise API", version="1.0.0", lifespan=lifespan)

app.add_middleware(RequestContextMiddleware)
register_exception_handlers(app)

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(auth_router)
api_v1.include_router(users_router)
api_v1.include_router(interviews_router)
app.include_router(api_v1)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
