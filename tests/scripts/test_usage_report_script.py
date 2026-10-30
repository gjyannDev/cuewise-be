import uuid

from app.modules.interviews.interviews_model import InterviewQuestion
from app.scripts.usage_report import main


def test_reports_stored_questions_grouped_by_interview(db):
    first, second = uuid.uuid7(), uuid.uuid7()
    db.add_all(
        [
            InterviewQuestion(session_id=second, position=1, text="Q?", category="technical", prompt_tokens=5),
            InterviewQuestion(session_id=first, position=2, text="Q?", category="technical", prompt_tokens=7),
            InterviewQuestion(session_id=first, position=1, text="Q?", category="technical", prompt_tokens=3),
        ]
    )
    db.commit()

    report = main(db)

    assert report.index(f"interview {first}") < report.index(f"interview {second}")
    assert report.index("  q1 prompt=3") < report.index("  q2 prompt=7")
    assert report.endswith("interviews=2 llm_interviews=0")


def test_an_empty_database(db):  # EC15
    assert main(db) == "interviews=0 llm_interviews=0"
