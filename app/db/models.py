# Import every module's models here so Alembic autogenerate can see them.
from app.modules.auth.models.auth_model import User  # noqa: F401
from app.modules.interviews.dependencies.models.interviews_knowledge_model import (  # noqa: F401
    InterviewSessionChunk,
    KnowledgeChunk,
    KnowledgeChunkScope,
)
from app.modules.interviews.dependencies.models.interviews_model import (  # noqa: F401
    InterviewFeedback,
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
