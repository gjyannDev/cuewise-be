"""End-of-interview feedback: what the score and write calls must return, and the code's checks around them.

The model judges and writes; the code decides the rest. It decides whether there is enough to score (the pre-check),
whether a score reply is valid (closed JSON, exactly the category's criteria, every quote really in that question's
answers), the overall (the model's is never used), and the text when the write call fails (the template). Pure: no LLM
and no database. A reply that fails raises InvalidReplyError with a reason code, which is logged; its text never is.
"""

import re
from collections.abc import Sequence
from decimal import ROUND_HALF_UP, Decimal
from typing import NamedTuple

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    ValidationError,
)

from ..ai.interviews_reply import InvalidReplyError, load_object
from ..constants.interviews_constants import (
    CATEGORY_CRITERIA,
    CRITERION_LABELS,
    CRITERION_TIPS,
    FEEDBACK_ITEM_MAX_LENGTH,
    FEEDBACK_NOTE_MAX_LENGTH,
    FEEDBACK_SUMMARY_MAX_LENGTH,
    IMPROVEMENTS_COUNT,
    IMPROVEMENTS_LABEL,
    NEXT_STEPS_COUNT,
    NEXT_STEPS_LABEL,
    NOTES_LABEL,
    QUOTE_MAX_LENGTH,
    QUOTE_MIN_LENGTH,
    REASON_MAX_LENGTH,
    SCORE_MAX,
    SCORE_MIN,
    SECTION_LABELS,
    STRENGTHS_COUNT,
    STRENGTHS_LABEL,
    SUBSTANTIVE_ANSWER_WORDS,
    SUBSTANTIVE_SHARE,
    SUMMARY_LABEL,
    Criterion,
    MessageRole,
    QuestionCategory,
    QuestionKind,
)
from ..models.interviews_model import InterviewMessage, InterviewQuestion
from ..utils.interviews_utils import APP_TAG

# --- The interview as the score call reads it ---


class ThreadTurn(NamedTuple):
    question: str
    answer: str
    kind: QuestionKind


class FeedbackThread(NamedTuple):
    """One main question with its follow-ups and every answer: what one set of scores is about."""

    main_number: int
    category: QuestionCategory
    question: str
    turns: tuple[ThreadTurn, ...]


def build_threads(
    questions: Sequence[InterviewQuestion], messages: Sequence[InterviewMessage]
) -> list[FeedbackThread]:
    """Stored rows as plain values, one thread per main question in interview order (a follow-up joins the thread of
    the main question before it). Interviewer reactions are app copy and are left out."""
    answers = {
        m.question_id: m.content for m in messages if m.role == MessageRole.candidate
    }
    threads: list[FeedbackThread] = []
    for q in sorted(questions, key=lambda q: q.position):
        turn = ThreadTurn(q.text, answers.get(q.id, ""), QuestionKind(q.kind))
        if turn.kind == QuestionKind.main or not threads:
            threads.append(
                FeedbackThread(
                    q.main_number, QuestionCategory(q.category), q.text, (turn,)
                )
            )
        else:
            threads[-1] = threads[-1]._replace(turns=(*threads[-1].turns, turn))
    return threads


def assess_evidence(threads: Sequence[FeedbackThread]) -> bool:
    """The pre-check, before any LLM call: enough main questions have a real answer to be worth scoring."""
    substantive = sum(
        1 for t in threads if len(t.turns[0].answer.split()) >= SUBSTANTIVE_ANSWER_WORDS
    )
    return bool(threads) and substantive >= SUBSTANTIVE_SHARE * len(threads)


# --- The score call's reply ---


class Evidence(NamedTuple):
    criterion: Criterion
    # Verified: it appears in the candidate's answers of its own thread.
    quote: str
    reason: str


class QuestionScore(NamedTuple):
    main_number: int
    # Exactly the criteria of the question's category, in CATEGORY_CRITERIA order.
    scores: dict[Criterion, int]
    evidence: tuple[Evidence, ...]


class ScoreResult(NamedTuple):
    enough_evidence: bool
    questions: tuple[QuestionScore, ...]


class _RawEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    criterion: Criterion
    quote: str
    reason: str


class _RawQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    main_number: StrictInt
    # Keys are plain strings so a wrong criterion is a "criteria" reason, not a generic schema error. Strict: 3.5 or
    # "3" is not a score.
    scores: dict[str, StrictInt]
    evidence: list[_RawEvidence]


class _RawScoreReply(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enough_evidence: StrictBool = True
    questions: list[_RawQuestion] = Field(default_factory=list)
    # Models like to add a total. Accepted so it costs no retry, and ignored: the code computes the overall.
    overall: object = None


def parse_score_reply(raw: str, threads: Sequence[FeedbackThread]) -> ScoreResult:
    """The score call's closed JSON, checked against the interview it scored. Raises InvalidReplyError."""
    try:
        reply = _RawScoreReply.model_validate(load_object(raw))
    except ValidationError as exc:
        raise InvalidReplyError("schema") from exc
    if not reply.enough_evidence:
        return ScoreResult(False, ())
    if [q.main_number for q in reply.questions] != [t.main_number for t in threads]:
        raise InvalidReplyError("questions")
    return ScoreResult(
        True,
        tuple(
            _question_score(q, t) for q, t in zip(reply.questions, threads, strict=True)
        ),
    )


def _question_score(raw: _RawQuestion, thread: FeedbackThread) -> QuestionScore:
    criteria = CATEGORY_CRITERIA[thread.category]
    if set(raw.scores) != {c.value for c in criteria}:
        raise InvalidReplyError("criteria")
    if any(not SCORE_MIN <= value <= SCORE_MAX for value in raw.scores.values()):
        raise InvalidReplyError("score_range")
    if not raw.evidence:
        raise InvalidReplyError("evidence_missing")
    # Against the full stored answers, so a quote from a part the call only saw shortened still counts.
    answers = [_normalized(turn.answer) for turn in thread.turns]
    evidence: list[Evidence] = []
    for item in raw.evidence:
        if item.criterion not in criteria:
            raise InvalidReplyError("evidence_criterion")
        if any(e.criterion == item.criterion for e in evidence):
            raise InvalidReplyError("evidence_duplicate")
        quote = item.quote.strip()
        if not QUOTE_MIN_LENGTH <= len(quote) <= QUOTE_MAX_LENGTH:
            raise InvalidReplyError("quote_length")
        if not any(_normalized(quote) in answer for answer in answers):
            raise InvalidReplyError("quote_not_found")
        reason = item.reason.strip()
        if not reason or len(reason) > REASON_MAX_LENGTH or _has_markup(reason):
            raise InvalidReplyError("reason")
        evidence.append(Evidence(item.criterion, quote, reason))
    return QuestionScore(
        thread.main_number, {c: raw.scores[c.value] for c in criteria}, tuple(evidence)
    )


def _normalized(text: str) -> str:
    """Case and whitespace don't make a quote different; anything else (words, punctuation) does."""
    return " ".join(text.casefold().split())


def compute_overall(questions: Sequence[QuestionScore]) -> float:
    """The mean of every criterion score of every main question, rounded half up to one decimal.

    Decimal, not round(): round(3.25, 1) gives 3.2, because Python rounds a half to the even digit.
    """
    values = [value for q in questions for value in q.scores.values()]
    mean = Decimal(sum(values)) / Decimal(len(values))
    return float(mean.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


# --- The write call's reply: plain text in labelled sections ---

_HEADER = re.compile(rf"^({'|'.join(SECTION_LABELS)}):\s*(.*)$")
_ITEM = re.compile(r"^-\s+(.+)$")
_NOTE = re.compile(r"^(\d+)\s*:\s*(.+)$")
# The client shows plain strings: bold, code, headings and links would arrive as raw symbols.
_MARKDOWN = re.compile(r"\*\*|__|`|(?:^|\s)#{1,6}\s|\[[^\]]*\]\([^)]*\)")
_LISTS = {
    STRENGTHS_LABEL: STRENGTHS_COUNT,
    IMPROVEMENTS_LABEL: IMPROVEMENTS_COUNT,
    NEXT_STEPS_LABEL: NEXT_STEPS_COUNT,
}


class WriteText(NamedTuple):
    summary: str
    strengths: tuple[str, ...]
    improvements: tuple[str, ...]
    next_steps: tuple[str, ...]
    # Main question number -> its note.
    notes: dict[int, str]

    def render(self) -> str:
        """The labelled text the write call is asked for (the parser reads it back unchanged)."""
        lines = [f"{SUMMARY_LABEL}: {self.summary}"]
        for label, items in (
            (STRENGTHS_LABEL, self.strengths),
            (IMPROVEMENTS_LABEL, self.improvements),
            (NEXT_STEPS_LABEL, self.next_steps),
        ):
            lines += [f"{label}:", *(f"- {item}" for item in items)]
        lines += [
            f"{NOTES_LABEL}:",
            *(f"{n}: {note}" for n, note in sorted(self.notes.items())),
        ]
        return "\n".join(lines)


def parse_write_reply(raw: str, main_numbers: Sequence[int]) -> WriteText:
    """The write call's text, slot by slot: every section once and in order, list sizes, one note per main question,
    length limits, no markup. Raises InvalidReplyError."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in (line.strip() for line in raw.strip().splitlines()):
        if not line:
            continue
        header = _HEADER.match(line)
        if header:
            current = header.group(1)
            if current in sections:
                raise InvalidReplyError("format")
            sections[current] = [header.group(2)] if header.group(2) else []
        elif current is None:
            raise InvalidReplyError("format")
        else:
            sections[current].append(line)
    if list(sections) != list(SECTION_LABELS):
        raise InvalidReplyError("format")

    lists: dict[str, tuple[str, ...]] = {}
    for label, (fewest, most) in _LISTS.items():
        items = [_ITEM.match(line) for line in sections[label]]
        if not all(items):
            raise InvalidReplyError("format")
        lists[label] = tuple(m.group(1).strip() for m in items if m)
        if not fewest <= len(lists[label]) <= most:
            raise InvalidReplyError("count")

    notes: dict[int, str] = {}
    for line in sections[NOTES_LABEL]:
        match = _NOTE.match(line)
        if match is None:
            raise InvalidReplyError("format")
        number = int(match.group(1))
        if number in notes:
            raise InvalidReplyError("notes")
        notes[number] = match.group(2).strip()
    if sorted(notes) != sorted(main_numbers):
        raise InvalidReplyError("notes")

    text = WriteText(
        " ".join(sections[SUMMARY_LABEL]),
        lists[STRENGTHS_LABEL],
        lists[IMPROVEMENTS_LABEL],
        lists[NEXT_STEPS_LABEL],
        notes,
    )
    _check_lengths(text)
    if any(_has_markup(slot) for slot in _slots(text)):
        raise InvalidReplyError("markup")
    return text


def _check_lengths(text: WriteText) -> None:
    if not 0 < len(text.summary) <= FEEDBACK_SUMMARY_MAX_LENGTH:
        raise InvalidReplyError("length")
    if any(
        len(item) > FEEDBACK_ITEM_MAX_LENGTH
        for item in (*text.strengths, *text.improvements, *text.next_steps)
    ):
        raise InvalidReplyError("length")
    if any(len(note) > FEEDBACK_NOTE_MAX_LENGTH for note in text.notes.values()):
        raise InvalidReplyError("length")


def _slots(text: WriteText) -> list[str]:
    return [
        text.summary,
        *text.strengths,
        *text.improvements,
        *text.next_steps,
        *text.notes.values(),
    ]


def _has_markup(text: str) -> bool:
    return bool(APP_TAG.search(text) or _MARKDOWN.search(text))


# --- The template: the text the code writes itself when the write call fails ---


def template_text(questions: Sequence[QuestionScore], overall: float) -> WriteText:
    """Plain, stiff, always valid: built from the stored scores and the score call's verified evidence reasons, under
    the same limits the write call must meet."""
    order = {c: i for i, c in enumerate(Criterion)}
    values: dict[Criterion, list[int]] = {}
    reasons: dict[Criterion, str] = {}
    for q in questions:
        for criterion, value in q.scores.items():
            values.setdefault(criterion, []).append(value)
        for e in q.evidence:
            reasons.setdefault(e.criterion, e.reason)
    means = {c: sum(v) / len(v) for c, v in values.items()}
    ranked = sorted(means, key=lambda c: (-means[c], order[c]))
    strongest = ranked[: STRENGTHS_COUNT[0]]
    weakest = [c for c in reversed(ranked) if c not in strongest][
        : IMPROVEMENTS_COUNT[0]
    ]

    def scored(c: Criterion) -> str:
        return f"{CRITERION_LABELS[c]} ({means[c]:.1f}/5)"

    count = len(questions)
    summary = (
        f"Your overall score is {overall:.1f} out of 5 across {count} question{'s' if count != 1 else ''}. "
        f"Your strongest area was {CRITERION_LABELS[strongest[0]].lower()}; the area to work on first is "
        f"{CRITERION_LABELS[weakest[0]].lower()}."
    )
    return WriteText(
        summary=summary,
        strengths=tuple(
            f"{scored(c)}: {reasons.get(c, 'a consistent strength in your answers.')}"
            for c in strongest
        ),
        improvements=tuple(f"{scored(c)}: {CRITERION_TIPS[c]}" for c in weakest),
        next_steps=(
            f"In your next practice interview, focus on {CRITERION_LABELS[weakest[0]].lower()}.",
        ),
        notes={q.main_number: _template_note(q, order) for q in questions},
    )


def _template_note(question: QuestionScore, order: dict[Criterion, int]) -> str:
    ranked = sorted(question.scores, key=lambda c: (-question.scores[c], order[c]))
    best, worst = ranked[0], ranked[-1]
    return (
        f"Strongest: {CRITERION_LABELS[best]} ({question.scores[best]}/5). "
        f"To improve: {CRITERION_LABELS[worst]} ({question.scores[worst]}/5)."
    )


# --- What is stored: the feedback row's JSON result ---


class StoredEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    criterion: Criterion
    quote: str
    reason: str


class StoredQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    main_number: int
    category: QuestionCategory
    # The main question's text: the write call and the client need it, the answers they never get.
    question: str
    scores: dict[Criterion, int]
    evidence: list[StoredEvidence]
    note: str | None = None


class StoredResult(BaseModel):
    """The scores and evidence from the score call, then the text. Read back through this model, so a row that no
    longer fits the contract fails loudly instead of reaching the client."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    questions: list[StoredQuestion]
    summary: str | None = None
    strengths: list[str] = Field(default_factory=list)
    improvements: list[str] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)

    def question_scores(self) -> list[QuestionScore]:
        return [
            QuestionScore(
                q.main_number,
                dict(q.scores),
                tuple(Evidence(e.criterion, e.quote, e.reason) for e in q.evidence),
            )
            for q in self.questions
        ]

    def with_text(self, text: WriteText) -> StoredResult:
        return StoredResult(
            questions=[q.model_copy(update={"note": text.notes.get(q.main_number)}) for q in self.questions],
            summary=text.summary,
            strengths=list(text.strengths),
            improvements=list(text.improvements),
            next_steps=list(text.next_steps),
        )


def stored_scores(threads: Sequence[FeedbackThread], scores: Sequence[QuestionScore]) -> StoredResult:
    """The validated scores with their questions' text and category, ready to store before the write call runs."""
    by_number = {t.main_number: t for t in threads}
    return StoredResult(
        questions=[
            StoredQuestion(
                main_number=s.main_number,
                category=by_number[s.main_number].category,
                question=by_number[s.main_number].question,
                scores=s.scores,
                evidence=[StoredEvidence(criterion=e.criterion, quote=e.quote, reason=e.reason) for e in s.evidence],
            )
            for s in scores
        ]
    )
