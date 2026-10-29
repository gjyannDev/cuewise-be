import json

import pytest

from app.modules.interviews.interviews_constants import InterviewType, QuestionCategory
from app.modules.interviews.interviews_reply import InvalidReplyError, parse_interviewer_reply

EARLIER = ["Tell me about a time you disagreed with a teammate.", "How do you debug a slow API?"]


def reply(question="How would you design a rate limiter for a public API?", category="technical", **extra) -> str:
    return json.dumps({"question": question, "category": category, **extra})


def parse(raw, interview_type=InterviewType.mixed, earlier=EARLIER):
    return parse_interviewer_reply(raw, interview_type=interview_type, earlier_questions=earlier)


def test_valid_reply_is_parsed():  # AC1, AC3
    result = parse(reply())

    assert result.question == "How would you design a rate limiter for a public API?"
    assert result.category == QuestionCategory.technical


def test_question_is_trimmed():
    assert parse(reply(question="  What is a race condition?  ")).question == "What is a race condition?"


def test_an_imperative_question_without_a_question_mark_is_valid():  # bank style: "Tell me about..."
    assert parse(reply(question="Walk me through how you would index a large table.")).question.startswith("Walk me")


@pytest.mark.parametrize("fence", ["```json\n{}\n```", "```\n{}\n```", "```json {} ```"])
def test_a_single_code_fence_is_accepted(fence):  # EC9, AC6
    raw = fence.replace("{}", reply())

    assert parse(raw).category == QuestionCategory.technical


@pytest.mark.parametrize(
    "raw",
    [
        "Sure! Here is the question: " + reply(),
        reply() + "\nHope this helps.",
        "```json\n" + reply() + "\n```\nExtra text",
        "```json\n" + reply(),
    ],
    ids=["text-before", "text-after", "text-after-fence", "unclosed-fence"],
)
def test_text_around_the_json_is_invalid(raw):  # EC9, AC6
    with pytest.raises(InvalidReplyError):
        parse(raw)


@pytest.mark.parametrize(
    ("raw", "reason"),
    [
        ("How would you design a rate limiter?", "not_json"),
        ("", "not_json"),
        ('["a question?"]', "not_object"),
        (reply(reaction="Nice answer!"), "schema"),
        (reply(kind="question"), "schema"),
        (json.dumps({"question": "What is a mutex?"}), "schema"),
        (json.dumps({"category": "technical"}), "schema"),
        (reply(question="   "), "schema"),
        (reply(question="x" * 499 + "?"), None),
        (reply(question="x" * 500 + "?"), "schema"),
        (reply(category="leadership"), "schema"),
        (reply(question="What is a mutex? And what is a semaphore?"), "multiple_questions"),
        (reply(question="What is a mutex？ And a semaphore？"), "multiple_questions"),
    ],
    ids=[
        "plain-text",
        "empty",
        "array",
        "old-reaction-field",
        "unknown-kind-field",
        "missing-category",
        "missing-question",
        "blank-question",
        "500-chars-ok",
        "501-chars",
        "unknown-category",
        "two-questions",
        "two-full-width-question-marks",
    ],
)
def test_each_invalid_kind_is_rejected_with_a_reason(raw, reason):  # EC6, EC8, AC5
    if reason is None:
        assert parse(raw)
        return
    with pytest.raises(InvalidReplyError) as exc:
        parse(raw)
    assert exc.value.reason == reason


@pytest.mark.parametrize(
    ("interview_type", "category", "ok"),
    [
        (InterviewType.technical, "technical", True),
        (InterviewType.technical, "behavioral", False),
        (InterviewType.behavioral, "behavioral", True),
        (InterviewType.behavioral, "technical", False),
        (InterviewType.mixed, "technical", True),
        (InterviewType.mixed, "behavioral", True),
    ],
)
def test_category_must_fit_the_interview_type(interview_type, category, ok):  # EC7
    raw = reply(category=category)

    if ok:
        assert parse(raw, interview_type=interview_type).category == category
    else:
        with pytest.raises(InvalidReplyError) as exc:
            parse(raw, interview_type=interview_type)
        assert exc.value.reason == "category"


@pytest.mark.parametrize(
    "question",
    ["How do you debug a slow API?", "  how do you DEBUG a slow   API?  ", "HOW DO YOU DEBUG A SLOW API?"],
)
def test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(question):  # EC5
    with pytest.raises(InvalidReplyError) as exc:
        parse(reply(question=question))

    assert exc.value.reason == "repeat"


def test_the_first_question_has_nothing_to_repeat():  # EC12
    assert parse(reply(question="How do you debug a slow API?"), earlier=[]).question
