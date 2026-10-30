import uuid

from app.modules.interviews.interviews_model import InterviewQuestion
from app.modules.interviews.interviews_utils import build_usage_report

S1, S2 = uuid.UUID(int=1), uuid.UUID(int=2)


def q(session, position, prompt=None, completion=None, source="llm", latency=None, version="interviewer_v1"):
    return InterviewQuestion(
        session_id=session,
        position=position,
        text=f"Secret question text {position}?",
        category="technical",
        source=source,
        prompt_version=version if source == "llm" else None,
        prompt_tokens=prompt,
        completion_tokens=completion,
        latency_ms=latency,
    )


def test_prints_tokens_per_position_and_interview_totals():  # AC12 part 2
    report = build_usage_report([q(S1, 1, 100, 10, latency=900), q(S1, 2, 250, 20, latency=1100)])

    assert f"interview {S1} questions=2 llm=2 bank=0" in report
    assert "  q1 prompt=100 completion=10 latency_ms=900 source=llm prompt_version=interviewer_v1" in report
    assert "  q2 prompt=250 completion=20 latency_ms=1100 source=llm prompt_version=interviewer_v1" in report
    assert "  total prompt=350 completion=30" in report


def test_missing_usage_is_a_dash_and_left_out_of_the_sums():  # EC14
    report = build_usage_report([q(S1, 1, source="bank"), q(S1, 2, 200, 15)])

    assert "  q1 prompt=- completion=- latency_ms=- source=bank prompt_version=-" in report
    assert "  total prompt=200 completion=15" in report
    assert "llm=1 bank=1" in report


def test_interviews_are_reported_separately():
    report = build_usage_report([q(S1, 1, 100, 10), q(S2, 1, 300, 30)])

    assert report.index(f"interview {S1}") < report.index(f"interview {S2}")
    assert report.count("  total prompt=") == 2
    assert (
        "interviews=2 llm_interviews=2 avg_prompt_per_llm_interview=200 avg_completion_per_llm_interview=20" in report
    )


def test_an_empty_database_prints_an_empty_report():  # EC15
    assert build_usage_report([]) == "interviews=0 llm_interviews=0"


def test_the_report_never_contains_question_text():  # privacy
    assert "Secret question" not in build_usage_report([q(S1, 1, 100, 10)])
