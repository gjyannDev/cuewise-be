"""Print stored LLM usage per interview: tokens per question position and per interview. Numbers and ids only.

Usage: uv run python -m app.scripts.usage_report
"""

from sqlalchemy.orm import Session

from app.db import models  # noqa: F401  (registers every model before the session is used)
from app.db.session import SessionLocal
from app.modules.interviews.interviews_repository import InterviewsRepository
from app.modules.interviews.interviews_utils import build_usage_report


def main(db: Session) -> str:
    return build_usage_report(InterviewsRepository(db).list_all_questions())


if __name__ == "__main__":
    with SessionLocal() as session:
        print(main(session))
