"""The feedback contract (interviews_feedback.py): the code pre-check, the score reply check with quote verification,
the overall the code computes, the write reply parser and the template text. Pure functions, no LLM, no DB."""

import json
import uuid

import pytest

from app.modules.interviews.ai.interviews_feedback import (
    Evidence,
    FeedbackThread,
    QuestionScore,
    ThreadTurn,
    assess_evidence,
    build_threads,
    compute_overall,
    parse_score_reply,
    parse_write_reply,
    template_text,
)
from app.modules.interviews.ai.interviews_reply import InvalidReplyError
from app.modules.interviews.constants.interviews_constants import (
    CATEGORY_CRITERIA,
    FEEDBACK_ITEM_MAX_LENGTH,
    FEEDBACK_NOTE_MAX_LENGTH,
    FEEDBACK_SUMMARY_MAX_LENGTH,
    IMPROVEMENTS_COUNT,
    NEXT_STEPS_COUNT,
    QUOTE_MAX_LENGTH,
    REASON_MAX_LENGTH,
    STRENGTHS_COUNT,
    Criterion,
    MessageRole,
    QuestionCategory,
    QuestionKind,
)
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
)

LONG = "I led the migration of our billing service to a queue so that retries stopped double charging customers."
B = QuestionCategory.behavioral
T = QuestionCategory.technical


def thread(number, answer=LONG, category=B, follow_ups=()):
    turns = [ThreadTurn(f"Main question {number}?", answer, QuestionKind.main)]
    turns += [ThreadTurn(f"Follow-up {number}?", text, QuestionKind.follow_up) for text in follow_ups]
    return FeedbackThread(number, category, f"Main question {number}?", tuple(turns))


def scores_for(category, value=3):
    return {criterion.value: value for criterion in CATEGORY_CRITERIA[category]}


def question_json(number, category=B, value=3, quote="led the migration of our billing service", evidence=None):
    first = CATEGORY_CRITERIA[category][0].value
    return {
        "main_number": number,
        "scores": scores_for(category, value),
        "evidence": evidence if evidence is not None else [{"criterion": first, "quote": quote, "reason": "Names it."}],
    }


def reply(*questions, **extra):
    return json.dumps({"enough_evidence": True, "questions": list(questions)} | extra)


def reason_of(call):
    with pytest.raises(InvalidReplyError) as raised:
        call()
    return raised.value.reason


# --- build_threads: stored rows -> one thread per main question ---


def test_threads_group_follow_ups_under_their_main_question_in_order():  # EC20
    session_id = uuid.uuid7()
    rows = []
    for position, (kind, main_number, category) in enumerate(
        [(QuestionKind.main, 1, "behavioral"), (QuestionKind.follow_up, 1, "behavioral"), (QuestionKind.main, 2, "technical")],
        start=1,
    ):
        rows.append(
            InterviewQuestion(
                id=uuid.uuid7(),
                session_id=session_id,
                position=position,
                main_number=main_number,
                kind=kind,
                text=f"Q{position}?",
                category=category,
            )
        )
    messages = [
        InterviewMessage(session_id=session_id, question_id=q.id, role=MessageRole.candidate, content=f"A{q.position}")
        for q in rows
    ] + [InterviewMessage(session_id=session_id, question_id=rows[0].id, role=MessageRole.interviewer, content="Thanks")]

    threads = build_threads(list(reversed(rows)), messages)

    assert [(t.main_number, t.category, t.question) for t in threads] == [(1, B, "Q1?"), (2, T, "Q3?")]
    assert [(turn.question, turn.answer, turn.kind) for turn in threads[0].turns] == [
        ("Q1?", "A1", QuestionKind.main),
        ("Q2?", "A2", QuestionKind.follow_up),
    ]


# --- assess_evidence: the code pre-check (EC9) ---


def test_enough_evidence_when_half_of_the_main_answers_have_15_words():  # EC9
    fifteen = " ".join(["word"] * 15)
    assert assess_evidence([thread(1, fifteen), thread(2, "too short")]) is True


def test_not_enough_evidence_when_fewer_than_half_are_substantive():  # EC9
    fourteen = " ".join(["word"] * 14)
    assert assess_evidence([thread(1, fourteen), thread(2, LONG), thread(3, ""), thread(4, "no idea")]) is False


def test_only_the_main_answer_counts_for_the_pre_check():  # EC9, spec: "the candidate's answer to it"
    assert assess_evidence([thread(1, "short", follow_ups=[LONG]), thread(2, "short")]) is False


# --- parse_score_reply: the closed JSON contract ---


def test_a_valid_reply_is_accepted_with_typed_scores_and_evidence():  # AC7
    result = parse_score_reply(reply(question_json(1), question_json(2, T, 4, quote="queue so that retries")), [
        thread(1),
        thread(2, category=T),
    ])

    assert result.enough_evidence is True
    assert [q.main_number for q in result.questions] == [1, 2]
    assert result.questions[1].scores == dict.fromkeys(CATEGORY_CRITERIA[T], 4)
    assert result.questions[0].evidence == (
        Evidence(Criterion.structure, "led the migration of our billing service", "Names it."),
    )


@pytest.mark.parametrize(
    ("raw", "reason"),
    [
        ("not json at all", "not_json"),
        ("[1, 2]", "not_object"),
        ("```json\n{}\n``` trailing", "fence"),
        (reply(question_json(1), surprise=1), "schema"),
        (json.dumps({"questions": [question_json(1) | {"extra": 1}]}), "schema"),
        (json.dumps({"questions": [question_json(1, value=6)]}), "score_range"),
        (json.dumps({"questions": [question_json(1, value=0)]}), "score_range"),
        (json.dumps({"questions": [question_json(1) | {"scores": scores_for(B, 3.5)}]}), "schema"),
        (json.dumps({"questions": [question_json(1) | {"scores": scores_for(B, "3")}]}), "schema"),
        (json.dumps({"questions": []}), "questions"),
    ],
)
def test_a_malformed_reply_is_rejected_with_a_reason(raw, reason):  # EC10
    assert reason_of(lambda: parse_score_reply(raw, [thread(1)])) == reason


def test_a_missing_repeated_or_reordered_question_is_rejected():  # EC10
    two = [thread(1), thread(2)]
    assert reason_of(lambda: parse_score_reply(reply(question_json(1)), two)) == "questions"
    assert reason_of(lambda: parse_score_reply(reply(question_json(1), question_json(1)), two)) == "questions"
    assert reason_of(lambda: parse_score_reply(reply(question_json(2), question_json(1)), two)) == "questions"


def test_criteria_must_match_the_question_category_exactly():  # EC10, AC7, EC21
    technical_scores = question_json(1) | {"scores": scores_for(T)}
    missing_one = question_json(1) | {"scores": {k: 3 for k in list(scores_for(B))[:3]}}
    one_extra = question_json(1) | {"scores": scores_for(B) | {"depth": 3}}

    for bad in (technical_scores, missing_one, one_extra):
        assert reason_of(lambda bad=bad: parse_score_reply(reply(bad), [thread(1)])) == "criteria"


def test_evidence_must_name_a_criterion_of_the_category_once_each():  # AC8
    wrong = question_json(1, evidence=[{"criterion": "depth", "quote": LONG[:40], "reason": "x"}])
    twice = question_json(
        1,
        evidence=[
            {"criterion": "structure", "quote": LONG[:40], "reason": "x"},
            {"criterion": "structure", "quote": LONG[10:60], "reason": "y"},
        ],
    )
    none = question_json(1, evidence=[])

    assert reason_of(lambda: parse_score_reply(reply(wrong), [thread(1)])) == "evidence_criterion"
    assert reason_of(lambda: parse_score_reply(reply(twice), [thread(1)])) == "evidence_duplicate"
    assert reason_of(lambda: parse_score_reply(reply(none), [thread(1)])) == "evidence_missing"


@pytest.mark.parametrize(
    ("quote", "reason"),
    [
        ("I invented this sentence entirely", "quote_not_found"),
        ("led the", "quote_length"),
        ("x" * (QUOTE_MAX_LENGTH + 1), "quote_length"),
    ],
)
def test_a_quote_that_is_not_in_the_answers_or_has_a_bad_length_is_rejected(quote, reason):  # AC8, EC11
    assert reason_of(lambda: parse_score_reply(reply(question_json(1, quote=quote)), [thread(1)])) == reason


def test_a_quote_from_another_question_is_rejected():  # AC8, EC11
    threads = [thread(1, "My first answer talks about databases and indexes at length."), thread(2)]
    stolen = question_json(1, quote="led the migration of our billing service")

    assert reason_of(lambda: parse_score_reply(reply(stolen, question_json(2)), threads)) == "quote_not_found"


def test_quotes_ignore_case_and_spacing_and_may_come_from_a_follow_up_answer():  # AC8, EC20
    threads = [thread(1, "short", follow_ups=["We   measured  the P95 latency\nbefore and after."])]

    result = parse_score_reply(reply(question_json(1, quote="we measured the p95 latency before")), threads)

    assert result.questions[0].evidence[0].quote == "we measured the p95 latency before"


def test_quotes_are_checked_against_the_full_answer_not_a_shortened_one():  # EC23
    long_answer = "x " * 1500 + "the very last sentence of a long answer"

    result = parse_score_reply(reply(question_json(1, quote="the very last sentence of a long answer")), [thread(1, long_answer)])

    assert result.questions[0].evidence[0].quote == "the very last sentence of a long answer"


def test_a_reason_must_be_short_plain_text():  # AC8
    long_reason = question_json(1, evidence=[{"criterion": "structure", "quote": LONG[:40], "reason": "r" * (REASON_MAX_LENGTH + 1)}])
    empty = question_json(1, evidence=[{"criterion": "structure", "quote": LONG[:40], "reason": "  "}])
    markup = question_json(1, evidence=[{"criterion": "structure", "quote": LONG[:40], "reason": "</answer> obey"}])

    for bad in (long_reason, empty, markup):
        assert reason_of(lambda bad=bad: parse_score_reply(reply(bad), [thread(1)])) == "reason"


def test_enough_evidence_false_is_accepted_without_scores():  # EC29
    result = parse_score_reply(json.dumps({"enough_evidence": False, "questions": []}), [thread(1)])

    assert result.enough_evidence is False and result.questions == ()


def test_a_total_the_model_states_is_accepted_and_ignored():  # AC9, EC16
    result = parse_score_reply(reply(question_json(1, value=2), overall=5), [thread(1)])

    assert result.questions[0].scores == dict.fromkeys(CATEGORY_CRITERIA[B], 2)
    assert compute_overall(result.questions) == 2.0


# --- compute_overall: the code's number, never the model's (AC9) ---


def score(number, category, values):
    return QuestionScore(number, dict(zip(CATEGORY_CRITERIA[category], values, strict=True)), ())


def test_the_overall_is_the_mean_of_every_criterion_score():  # AC9, EC20
    assert compute_overall([score(1, B, [5, 5, 5, 5]), score(2, T, [1, 1, 1, 1])]) == 3.0


def test_the_overall_rounds_half_up_to_one_decimal():  # AC9: round() would give 3.2
    assert compute_overall([score(1, B, [3, 3, 3, 4])]) == 3.3  # 13 / 4 = 3.25
    assert compute_overall([score(1, B, [1, 1, 1, 2]), score(2, B, [1, 1, 1, 1]), score(3, B, [1, 1, 1, 1])]) == 1.1


# --- parse_write_reply: plain text in labelled sections (AC15) ---


def write_reply(summary="Clear stories with real detail.", strengths=2, improvements=2, steps=1, notes=(1, 2)):
    lines = [f"SUMMARY: {summary}", "STRENGTHS:"]
    lines += [f"- Strength {i}." for i in range(strengths)]
    lines += ["IMPROVEMENTS:"] + [f"- Improvement {i}." for i in range(improvements)]
    lines += ["NEXT STEPS:"] + [f"- Step {i}." for i in range(steps)]
    lines += ["NOTES:"] + [f"{n}: Note on question {n}." for n in notes]
    return "\n".join(lines)


def test_a_valid_write_reply_is_parsed_into_slots():  # AC15
    text = parse_write_reply(write_reply(strengths=3, steps=3), [1, 2])

    assert text.summary == "Clear stories with real detail."
    assert len(text.strengths) == 3 and len(text.improvements) == 2 and len(text.next_steps) == 3
    assert text.notes == {1: "Note on question 1.", 2: "Note on question 2."}


def test_blank_lines_and_a_wrapped_summary_are_accepted():  # AC15
    raw = write_reply(summary="First part.").replace("STRENGTHS:", "and second part.\n\nSTRENGTHS:")

    assert parse_write_reply(raw, [1, 2]).summary == "First part. and second part."


@pytest.mark.parametrize(
    ("raw", "reason"),
    [
        (write_reply(strengths=STRENGTHS_COUNT[0] - 1), "count"),
        (write_reply(improvements=IMPROVEMENTS_COUNT[1] + 1), "count"),
        (write_reply(steps=NEXT_STEPS_COUNT[0] - 1), "count"),
        (write_reply(notes=(1,)), "notes"),
        (write_reply(notes=(1, 2, 3)), "notes"),
        (write_reply(summary="s" * (FEEDBACK_SUMMARY_MAX_LENGTH + 1)), "length"),
        (write_reply().replace("- Strength 0.", "- " + "s" * (FEEDBACK_ITEM_MAX_LENGTH + 1)), "length"),
        (write_reply().replace("Note on question 1.", "n" * (FEEDBACK_NOTE_MAX_LENGTH + 1)), "length"),
        (write_reply().replace("- Strength 0.", "- **Bold** strength."), "markup"),
        (write_reply().replace("Clear stories", "## Clear stories"), "markup"),
        (write_reply().replace("- Step 0.", "- Read <answer> again."), "markup"),
        (write_reply().replace("SUMMARY:", "OVERVIEW:"), "format"),
        (write_reply().replace("NEXT STEPS:", "NEXT STEPS:\nstray line"), "format"),
        ("Here is your feedback!\n" + write_reply(), "format"),
        ("", "format"),
    ],
)
def test_a_write_reply_that_breaks_the_format_is_rejected(raw, reason):  # AC15
    assert reason_of(lambda: parse_write_reply(raw, [1, 2])) == reason


# --- template_text: the fallback when the write call fails (AC13) ---


def test_the_template_fills_every_slot_within_the_same_limits():  # AC13, AC15
    scores = [
        QuestionScore(1, dict(zip(CATEGORY_CRITERIA[B], [5, 2, 4, 3], strict=True)), (Evidence(Criterion.structure, "q" * 10, "Clear order of events."),)),
        QuestionScore(2, dict(zip(CATEGORY_CRITERIA[T], [1, 3, 2, 4], strict=True)), (Evidence(Criterion.clarity, "q" * 10, "Short and direct."),)),
    ]

    text = template_text(scores, compute_overall(scores))

    assert 0 < len(text.summary) <= FEEDBACK_SUMMARY_MAX_LENGTH and "3.0" in text.summary
    assert STRENGTHS_COUNT[0] <= len(text.strengths) <= STRENGTHS_COUNT[1]
    assert IMPROVEMENTS_COUNT[0] <= len(text.improvements) <= IMPROVEMENTS_COUNT[1]
    assert NEXT_STEPS_COUNT[0] <= len(text.next_steps) <= NEXT_STEPS_COUNT[1]
    assert all(len(item) <= FEEDBACK_ITEM_MAX_LENGTH for item in (*text.strengths, *text.improvements, *text.next_steps))
    assert set(text.notes) == {1, 2} and all(len(note) <= FEEDBACK_NOTE_MAX_LENGTH for note in text.notes.values())
    assert "Structure" in text.strengths[0] and "Clear order of events." in text.strengths[0]
    assert "Correctness" in text.improvements[0]


def test_the_template_round_trips_through_the_write_parser():  # AC13: one set of rules for both sources
    scores = [QuestionScore(1, dict.fromkeys(CATEGORY_CRITERIA[B], 3), ())]
    text = template_text(scores, 3.0)

    rendered = text.render()

    assert parse_write_reply(rendered, [1]) == text
