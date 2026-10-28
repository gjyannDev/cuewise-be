# Import every module's models here so Alembic autogenerate can see them.
from app.modules.auth.auth_model import User  # noqa: F401
from app.modules.interviews.interviews_model import InterviewQuestion, InterviewSession  # noqa: F401
