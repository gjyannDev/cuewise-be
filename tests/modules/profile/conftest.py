import pytest

from app.core.ai.dependencies import get_llm_provider
from app.core.rate_limit import RateLimiter
from app.main import app
from app.modules.profile.constants.profile_constants import RESUME_UPLOADS_PER_MINUTE
from app.modules.profile.dependencies.profile_dependencies import get_resume_limiter
from tests.modules.profile.profile_fixtures import ProfileLLM


@pytest.fixture
def profile_llm():
    handle = ProfileLLM()
    app.dependency_overrides[get_llm_provider] = lambda: handle.provider
    yield handle
    app.dependency_overrides.pop(get_llm_provider, None)


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
