from fastapi import APIRouter, FastAPI

from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import RequestContextMiddleware
from app.modules.auth.auth_route import router as auth_router
from app.modules.interviews.interviews_route import router as interviews_router
from app.modules.users.users_route import router as users_router

setup_logging(settings.debug)

app = FastAPI(title="Cuewise API", version="1.0.0")

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
