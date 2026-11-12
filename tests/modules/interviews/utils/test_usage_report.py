import uuid

from app.modules.interviews.dependencies.models.interviews_model import InterviewQuestion
from app.modules.interviews.utils.interviews_utils import build_usage_report

S1, S2 = uuid.UUID(int=1), uuid.UUID(int=2)


def q(session, position, prompt=None, completion=None, source="llm", latency=None, version="interviewer_v1", kind="main"):
    return InterviewQuestion(
        session_id=session,
        position=position,
        kind=kind,
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


def test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind():  # follow-ups AC10
    report = build_usage_report(
        [q(S1, 1, 100, 10), q(S1, 2, 300, 30, kind="follow_up"), q(S1, 3, 500, 50, kind="follow_up"), q(S2, 1, 200, 20)]
    )

    assert f"interview {S1} questions=3 llm=3 bank=0 follow_ups=2" in report
    assert "  q2 prompt=300 completion=30" in report and "kind=follow_up" in report
    assert "tokens main prompt=300 completion=30 follow_up prompt=800 completion=80 follow_ups=2" in report


def test_the_llm_time_per_turn_shows_p50_and_p95():  # follow-ups AC19
    rows = [q(S1, i, 10, 1, latency=ms) for i, ms in enumerate(range(100, 2100, 100), start=1)]  # 100..2000 ms

    report = build_usage_report([*rows, q(S1, 21, source="bank")])

    assert "turn_llm_ms p50=1000 p95=1900 turns=20" in report


def test_no_percentiles_without_llm_turns():
    assert "turn_llm_ms" not in build_usage_report([q(S1, 1, source="bank")])
