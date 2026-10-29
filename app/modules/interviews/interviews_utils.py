import json
import random
import re
from collections.abc import Collection, Mapping, Sequence
from itertools import chain, zip_longest
from pathlib import Path
from typing import NamedTuple

from pydantic import TypeAdapter, ValidationError

from app.core.ai.provider import ChatMessage
from app.core.errors import NotEnoughQuestionsError

from .interviews_constants import (
    CLOSING_REACTIONS,
    GENERAL_ROLE,
    INTERVIEWER_PROMPT_VERSION,
    LEVEL_GROUPS,
    PROMPTS_DIR,
    QUESTION_BANK_PATH,
    REACTION_POOLS,
    InterviewType,
    JobRole,
    Level,
    MessageKind,
    MessageRole,
    QuestionCategory,
)
from .interviews_model import InterviewMessage, InterviewQuestion
from .interviews_schema import BankQuestion, QuestionBank, TranscriptItemOut

_bank_adapter = TypeAdapter(QuestionBank)


def load_bank(path: Path) -> list[BankQuestion]:
    """Read and validate a question bank file; a bad file fails loudly instead of at request time."""
    try:
        return _bank_adapter.validate_json(path.read_bytes())
    except ValidationError as exc:
        raise ValueError(f"Invalid question bank {path.name}: {exc}") from exc


def select_questions(
    bank: list[BankQuestion],
    role: JobRole,
    level: Level,
    interview_type: InterviewType,
    count: int,
    rng: random.Random,
) -> list[BankQuestion]:
    """Pick `count` distinct questions for the setup, in interview order.

    The single seam a later story can wrap or replace with an LLM-driven source.
    `mixed` is split evenly (extra one behavioral) and interleaved, starting behavioral.
    Raises NotEnoughQuestionsError rather than returning fewer than asked.
    """

    def eligible(category: QuestionCategory) -> list[BankQuestion]:
        return [
            q for q in bank if q.type == category and level in q.levels and (role in q.roles or GENERAL_ROLE in q.roles)
        ]

    if interview_type != InterviewType.mixed:
        pool = eligible(QuestionCategory(interview_type))
        if len(pool) < count:
            raise NotEnoughQuestionsError(
                "Not enough questions for this setup", {"requested": count, "available": len(pool)}
            )
        return rng.sample(pool, count)

    behavioral, technical = eligible(QuestionCategory.behavioral), eligible(QuestionCategory.technical)
    # Largest count whose split (ceil half behavioral, floor half technical) both pools can cover.
    available = min(2 * len(behavioral), 2 * len(technical) + 1)
    if count > available:
        raise NotEnoughQuestionsError(
            "Not enough questions for this setup", {"requested": count, "available": available}
        )
    picked_b = rng.sample(behavioral, (count + 1) // 2)
    picked_t = rng.sample(technical, count // 2)
    return [q for q in chain.from_iterable(zip_longest(picked_b, picked_t)) if q is not None]


# Loaded once at import so a broken bank stops the app at startup (same idea as `settings`).
QUESTION_BANK = load_bank(QUESTION_BANK_PATH)


def load_prompt(version: str) -> str:
    return (PROMPTS_DIR / f"{version}.md").read_text(encoding="utf-8")


def build_transcript(
    questions: Sequence[InterviewQuestion], messages: Sequence[InterviewMessage]
) -> list[TranscriptItemOut]:
    """The chat as the user saw it: each question, then its answer and reaction when they exist.

    Same stored data as build_interviewer_messages, different view: every question, answer and reaction as shown.
    """
    by_question = {(m.question_id, m.role): m for m in messages}
    items: list[TranscriptItemOut] = []
    for q in sorted(questions, key=lambda q: q.position):
        items.append(
            TranscriptItemOut(
                id=q.id,
                question_id=q.id,
                position=q.position,
                role=MessageRole.interviewer,
                kind=MessageKind.question,
                text=q.text,
                created_at=None,
            )
        )
        for role, kind in (
            (MessageRole.candidate, MessageKind.answer),
            (MessageRole.interviewer, MessageKind.reaction),
        ):
            if message := by_question.get((q.id, role)):
                items.append(
                    TranscriptItemOut(
                        id=message.id,
                        question_id=q.id,
                        position=q.position,
                        role=role,
                        kind=kind,
                        text=message.content,
                        created_at=message.created_at,
                    )
                )
    return items


_PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")
# Matches an opening or closing job_description tag in any case, so the data block can't be closed early.
_JOB_DESCRIPTION_TAG = re.compile(r"<\s*/?\s*job_description\s*>", re.IGNORECASE)

# Loaded at import like the bank: a missing prompt file stops the app at startup, not mid-interview.
INTERVIEWER_PROMPT = load_prompt(INTERVIEWER_PROMPT_VERSION)

_CATEGORY_RULES = {
    InterviewType.behavioral: 'Every question is behavioral (past experience, teamwork, decisions): use "category": "behavioral".',
    InterviewType.technical: 'Every question is technical (concepts, design, debugging, code): use "category": "technical".',
    InterviewType.mixed: 'Mix behavioral and technical questions across the interview; set "category" to match the question.',
}


class QuestionTurn(NamedTuple):
    """One answered question as the interviewer LLM sees it (reactions are app copy, never sent to the model)."""

    question: str
    category: str
    answer: str


def render_template(template: str, values: Mapping[str, object]) -> str:
    """Fill {{name}} placeholders in one pass: inserted values are never scanned again, and a missing one fails.

    Plain str.format would choke on the literal JSON braces in the prompt.
    """
    return _PLACEHOLDER.sub(lambda m: str(values[m.group(1)]), template)


def render_interviewer_prompt(
    *, role: JobRole, level: Level, interview_type: InterviewType, question_number: int, question_count: int
) -> str:
    """Only trusted values go in here; the job description and answers never enter the system prompt."""
    return render_template(
        INTERVIEWER_PROMPT,
        {
            "role": role.value,
            "level": level.value,
            "interview_type": interview_type.value,
            "question_number": question_number,
            "question_count": question_count,
            "category_rule": _CATEGORY_RULES[interview_type],
        },
    )


def job_description_block(job_description: str | None) -> str:
    """Untrusted text, fenced as data. Tags inside it are neutralised so it can't close its own block."""
    if not job_description:
        return "No job description was provided."
    return f"<job_description>\n{_JOB_DESCRIPTION_TAG.sub('[tag removed]', job_description)}\n</job_description>"


def interviewer_history(
    questions: Sequence[InterviewQuestion], messages: Sequence[InterviewMessage]
) -> list[QuestionTurn]:
    """Answered questions with their answers, in interview order. Stored reactions are left out on purpose."""
    answers = {m.question_id: m.content for m in messages if m.role == MessageRole.candidate}
    return [QuestionTurn(q.text, q.category, answers[q.id]) for q in sorted(questions, key=lambda q: q.position)]


def build_interviewer_messages(
    system_prompt: str, job_description: str | None, turns: Sequence[QuestionTurn]
) -> list[ChatMessage]:
    """The full input for one call (the model has no memory, so the whole interview is resent every time).

    The job description opens the conversation as user data; earlier questions are replayed as the same JSON the
    model must answer with, which keeps it in format. Roles alternate system, user, assistant, user, ...
    """
    messages = [
        ChatMessage(role="system", content=system_prompt),
        ChatMessage(role="user", content=f"{job_description_block(job_description)}\n\nPlease ask the first question."),
    ]
    for turn in turns:
        messages.append(
            ChatMessage(role="assistant", content=json.dumps({"question": turn.question, "category": turn.category}))
        )
        messages.append(ChatMessage(role="user", content=turn.answer))
    return messages


def pick_fallback_question(
    bank: Sequence[BankQuestion],
    role: JobRole,
    level: Level,
    interview_type: InterviewType,
    position: int,
    used_bank_ids: Collection[str],
    rng: random.Random,
) -> BankQuestion:
    """One unused bank question for `position`, used when the LLM is off or its reply is unusable.

    `mixed` alternates by position, behavioral first, matching the split the start-time coverage check guarantees.
    """
    if interview_type == InterviewType.mixed:
        category = QuestionCategory.behavioral if position % 2 else QuestionCategory.technical
    else:
        category = QuestionCategory(interview_type)
    pool = [
        q
        for q in bank
        if q.type == category
        and level in q.levels
        and (role in q.roles or GENERAL_ROLE in q.roles)
        and q.id not in used_bank_ids
    ]
    if not pool:
        raise NotEnoughQuestionsError("Not enough questions for this setup", {"requested": position, "available": 0})
    return rng.choice(pool)


def pick_reaction(
    category: QuestionCategory, level: Level, *, final: bool, previous: str | None, rng: random.Random
) -> str:
    """A predefined, neutral acknowledgement for the answer just given; never the same as the last one."""
    group = LEVEL_GROUPS[level]
    pool = CLOSING_REACTIONS[group] if final else REACTION_POOLS[(category, group)]
    return rng.choice([r for r in pool if r != previous] or list(pool))
