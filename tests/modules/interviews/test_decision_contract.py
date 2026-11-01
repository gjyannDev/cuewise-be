"""The decide call's contract: {action, gap, note}, closed lists, gap present exactly when following up."""

import json

import pytest

from app.modules.interviews.interviews_constants import FollowUpAction, FollowUpGap
from app.modules.interviews.interviews_reply import InvalidReplyError, parse_decision_reply


def decision(action="follow_up", gap="no_tradeoff", **extra) -> str:
    return json.dumps({"action": action, "gap": gap, **extra})


def test_a_follow_up_with_a_gap_is_parsed():  # AC1
    result = parse_decision_reply(decision(note="Named Redis but gave no reason for it."))

    assert result.action == FollowUpAction.follow_up
    assert result.gap == FollowUpGap.no_tradeoff
    assert result.note == "Named Redis but gave no reason for it."


def test_next_question_with_a_null_gap_is_parsed():  # AC1
    result = parse_decision_reply(decision("next_question", None))

    assert (result.action, result.gap, result.note) == (FollowUpAction.next_question, None, None)


def test_a_fenced_decision_is_accepted():
    assert parse_decision_reply("```json\n" + decision() + "\n```").gap == FollowUpGap.no_tradeoff


@pytest.mark.parametrize(
    ("raw", "reason"),
    [
        ("follow up please", "not_json"),
        ("[]", "not_object"),
        (decision(extra="x"), "schema"),
        (decision("ask_more"), "schema"),
        (decision(gap="too_short"), "schema"),
        (json.dumps({"gap": "no_how"}), "schema"),
        (decision("next_question", "no_how"), "unexpected_gap"),
        (decision("follow_up", None), "missing_gap"),
        (json.dumps({"action": "follow_up"}), "missing_gap"),
    ],
    ids=[
        "not-json",
        "not-object",
        "extra-key",
        "unknown-action",
        "unknown-gap",
        "missing-action",
        "gap-on-next-question",
        "null-gap-on-follow-up",
        "no-gap-key-on-follow-up",
    ],
)
def test_every_other_shape_is_rejected_with_a_reason_code(raw, reason):  # AC1, EC3
    with pytest.raises(InvalidReplyError) as exc:
        parse_decision_reply(raw)

    assert exc.value.reason == reason


def test_a_bad_note_is_dropped_and_the_decision_kept():  # AC1, EC18
    result = parse_decision_reply(decision(note="x" * 500))

    assert result.action == FollowUpAction.follow_up
    assert (result.note, result.note_dropped) == (None, "too_long")
