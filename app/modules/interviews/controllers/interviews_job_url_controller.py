"""Job posting links and pasted pages: request -> JobUrlService, job text -> JobUrlOut."""

from app.modules.auth.models.auth_model import User

from ..schemas.interviews_schema import JobTextIn, JobUrlIn, JobUrlOut
from ..services.interviews_job_url_service import JobUrlService


class JobUrlController:
    def __init__(self, service: JobUrlService):
        self.service = service

    def import_job_text(self, user: User, data: JobUrlIn) -> JobUrlOut:
        result = self.service.import_job_text(user, data.url)
        return JobUrlOut(text=result.text, truncated=result.truncated)

    def import_pasted_text(self, user: User, data: JobTextIn) -> JobUrlOut:
        result = self.service.import_pasted_text(user, data.content, data.format)
        return JobUrlOut(text=result.text, truncated=result.truncated)
