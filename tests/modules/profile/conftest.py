import pytest

from app.core.ai.dependencies import get_chat_model
from app.core.config import settings
from app.core.rate_limit import RateLimiter
from app.main import app
from app.modules.profile.constants.profile_constants import RESUME_UPLOADS_PER_MINUTE
from app.modules.profile.dependencies.profile_dependencies import get_resume_limiter
from tests.modules.profile.profile_fixtures import ProfileLLM


@pytest.fixture
def profile_llm(monkeypatch):
    # Transport retries are RetryPolicy's (tests/core/ai): here a scripted error must end the extraction at once,
    # not be retried into the fake's default (valid) reply.
    monkeypatch.setattr(settings, "llm_max_retries", 0)
    handle = ProfileLLM()
    app.dependency_overrides[get_chat_model] = lambda: handle.model
    yield handle
    app.dependency_overrides.pop(get_chat_model, None)


@pytest.fixture(autouse=True)
def fresh_limiter():
    limiter = RateLimiter(limit=RESUME_UPLOADS_PER_MINUTE, window_seconds=60)
    app.dependency_overrides[get_resume_limiter] = lambda: limiter
    yield limiter
    app.dependency_overrides.pop(get_resume_limiter, None)


@pytest.fixture
def upload(client, auth_header):
    def _upload(user, data: bytes, *, name="resume.pdf", content_type="application/pdf", **extra_form):
        return client.post(
            "/api/v1/profile/resume",
            headers=auth_header(user),
            files={"file": (name, data, content_type)},
            data=extra_form or None,
        )

    return _upload
