"""interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode only) read before any text is shown,
then plain question text checked like v4's once complete (sse-streaming Step 12; AC12, EC11)."""

import pytest

from app.modules.interviews.interviews_constants import (
    INTERVIEWER_V5_PROMPT_VERSION,
    MAX_QUESTION_LENGTH,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
)
from app.modules.interviews.interviews_reply import (
    InvalidReplyError,
    parse_interviewer_reply,
    parse_streamed_reply,
    split_header,
)
from app.modules.interviews.interviews_utils import (
    load_prompt,
    render_interviewer_v2_prompt,
)

# --- split_header: the category line, read incrementally ---


def test_no_header_is_known_until_its_line_ends():
    assert split_header("CATEGORY: tech") is None
    assert split_header("") is None


def test_a_header_split_across_chunks_is_read_once_its_line_ends():
    buffer = ""
    for chunk in ["CATEG", "ORY: beha", "vioral\nTell me ", "about a time"]:
        buffer += chunk
        split = split_header(buffer)
    assert split is not None
    assert split.category == QuestionCategory.behavioral
    assert split.text == "Tell me about a time"


@pytest.mark.parametrize("line", ["CATEGORY: technical", "category:technical", "  Category :  Technical  "])
def test_the_header_is_case_and_space_tolerant(line):
    split = split_header(f"{line}\nHow would you shard it?")

    assert split is not None
    assert (split.category, split.text) == (QuestionCategory.technical, "How would you shard it?")


@pytest.mark.parametrize(
    "buffer",
    [
        "How would you design a rate limiter?\n",
        "CATEGORY: managerial\nHow do you lead?",
        '{"question": "Why?", "category": "technical"}\n',
        "```\nCATEGORY: technical\n",
    ],
    ids=["no-header", "unknown-category", "json", "fenced"],
)
def test_a_missing_or_unknown_header_is_an_invalid_reply(buffer):  # EC11
    with pytest.raises(InvalidReplyError) as exc:
        split_header(buffer)

    assert exc.value.reason == "header"


def test_a_long_first_line_is_no_header_without_waiting_for_its_end():  # EC11: fail before streaming any text
    with pytest.raises(InvalidReplyError) as exc:
        split_header("Tell me about a time you had to deliver bad news to a stakeholder")

    assert exc.value.reason == "header"


def test_at_the_end_of_the_reply_a_header_needs_no_newline():
    with pytest.raises(InvalidReplyError):
        split_header("How would you scale it?", final=True)
    split = split_header("CATEGORY: technical", final=True)
    assert split is not None and split.text == ""


# --- parse_streamed_reply: the finished text, the same checks as v4 ---


def parse(text, *, interview_type=InterviewType.technical, earlier=(), category=QuestionCategory.technical):
    return parse_streamed_reply(text, interview_type=interview_type, earlier_questions=list(earlier), category=category)


def test_a_valid_streamed_question_is_returned_trimmed():
    reply = parse("  How would you design a rate limiter for a public API?  \n")

    assert reply.question == "How would you design a rate limiter for a public API?"
    assert reply.category == QuestionCategory.technical
    assert reply.note is None


@pytest.mark.parametrize(
    ("text", "kwargs", "reason"),
    [
        ("What is a queue? And a stack?", {}, "multiple_questions"),
        ("Tell me about a conflict?", {"category": QuestionCategory.behavioral}, "category"),
        ("how would you design a  rate limiter?", {"earlier": ["How would you design a rate limiter?"]}, "repeat"),
        ("   ", {}, "schema"),
        ("x" * (MAX_QUESTION_LENGTH + 1) + "?", {}, "schema"),
        ('{"question": "Why this design?"}', {}, "not_text"),
    ],
    ids=["two-questions", "wrong-category", "repeat", "blank", "too-long", "json"],
)
def test_a_streamed_question_breaking_v4s_rules_is_rejected_with_the_same_reason(text, kwargs, reason):
    with pytest.raises(InvalidReplyError) as exc:
        parse(text, **kwargs)

    assert exc.value.reason == reason


def test_mixed_interviews_accept_either_category():
    reply = parse("Tell me about a conflict?", interview_type=InterviewType.mixed, category=QuestionCategory.behavioral)

    assert reply.category == QuestionCategory.behavioral


def test_the_json_parser_is_unchanged():
    reply = parse_interviewer_reply(
        '{"question": "How would you cache it?", "category": "technical"}',
        interview_type=InterviewType.technical,
        earlier_questions=[],
    )

    assert (reply.question, reply.category) == ("How would you cache it?", QuestionCategory.technical)


# --- the prompt ---


def test_v5_has_the_six_sections_in_order():  # AC12
    headings = [line for line in load_prompt(INTERVIEWER_V5_PROMPT_VERSION).splitlines() if line.startswith("# ")]

    assert headings == ["# Role", "# Task", "# Input", "# Output", "# Constraints", "# Capabilities"]


def test_v5_renders_fully_and_asks_for_the_header_and_plain_text():  # AC12
    text = render_interviewer_v2_prompt(
        role=JobRole.backend,
        level=Level.junior,
        interview_type=InterviewType.mixed,
        question_count=5,
        template=load_prompt(INTERVIEWER_V5_PROMPT_VERSION),
    )

    assert "{{" not in text and "<interview_status>" in text
    assert "CATEGORY: behavioral" in text and "CATEGORY: technical" in text
    assert "no JSON" in text
    assert '"note"' not in text
