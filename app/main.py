from fastapi import FastAPI

from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import RequestContextMiddleware
from app.modules.auth.route import router as auth_router

setup_logging(settings.debug)

app = FastAPI(title="Cuewise API", version="1.0.0")

app.add_middleware(RequestContextMiddleware)
register_exception_handlers(app)

app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
