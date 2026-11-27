"""What the model is asked to fill on the LangChain layer's structured calls (U3b1), as JSON schemas.

Every field is required, nullable where "none" is a valid answer: with defaults the schema marks nothing required and
the model may leave fields out (the U3a profile lesson, `ModelProfile`). These shapes only steer the model. The
existing parsers still read the reply text as a second check, so the note, gap and quote rules keep one home
(`interviews_reply.py`).
"""

from pydantic import BaseModel, ConfigDict

from ..constants.interviews_constants import Criterion, FollowUpAction, FollowUpGap


class ModelDecision(BaseModel):
    """The decide call's reply (follow_up_decision_v1): `gap` is null for "next_question"."""

    model_config = ConfigDict(extra="forbid")

    action: FollowUpAction
    gap: FollowUpGap | None
    note: str | None


class ModelEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    criterion: Criterion
    quote: str
    reason: str


class ModelQuestionScore(BaseModel):
    model_config = ConfigDict(extra="forbid")

    main_number: int
    # A map from criterion to a 1-5 score: which criteria (the thread's category's) is the parser's rule.
    scores: dict[Criterion, int]
    evidence: list[ModelEvidence]


class ModelScore(BaseModel):
    """The feedback score call's reply (feedback_score_v2), same shape as `_RawScoreReply` with every field required.
    Nested, with a map for `scores`: Gemini's JSON-schema mode has to take it (checked by the feedback eval). Extra
    top-level keys are ignored, not refused, as `_RawScoreReply` ignores a stated `overall`: the code computes it."""

    enough_evidence: bool
    questions: list[ModelQuestionScore]
