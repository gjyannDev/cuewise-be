import random
from collections.abc import Sequence
from itertools import chain, zip_longest
from pathlib import Path
from typing import NamedTuple

from pydantic import TypeAdapter, ValidationError

from app.core.ai.provider import ChatMessage
from app.core.errors import NotEnoughQuestionsError

from .interviews_constants import (
    GENERAL_ROLE,
    PROMPTS_DIR,
    QUESTION_BANK_PATH,
    REACTION_PROMPT_VERSION,
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


class Turn(NamedTuple):
    """One question of the conversation as the model sees it; `reaction` is None when none was saved."""

    question: str
    answer: str
    reaction: str | None


def load_prompt(version: str) -> str:
    return (PROMPTS_DIR / f"{version}.md").read_text(encoding="utf-8")


# Loaded at import like the bank: a missing prompt file stops the app at startup, not mid-interview.
REACTION_PROMPT = load_prompt(REACTION_PROMPT_VERSION)


def render_reaction_prompt(role: JobRole, level: Level) -> str:
    """Only trusted enum values go in here; candidate text never enters the system prompt."""
    return REACTION_PROMPT.format(role=role.value, level=level.value)


def history_turns(questions: Sequence[InterviewQuestion], messages: Sequence[InterviewMessage]) -> list[Turn]:
    """Already-answered questions with their answer and (if saved) reaction, in interview order."""
    by_question = {(m.question_id, m.role): m.content for m in messages}
    return [
        Turn(q.text, by_question[(q.id, MessageRole.candidate)], by_question.get((q.id, MessageRole.interviewer)))
        for q in sorted(questions, key=lambda q: q.position)
    ]


def build_llm_messages(system_prompt: str, turns: Sequence[Turn]) -> list[ChatMessage]:
    """The full input for one call: the model has no memory, so the whole conversation is resent every time.

    Roles strictly alternate (assistant, user, ...) because providers handle that most predictably,
    so a saved reaction is merged with the question that followed it into one assistant turn.
    """
    messages = [ChatMessage(role="system", content=system_prompt)]
    pending_reaction: str | None = None
    for turn in turns:
        interviewer = turn.question if pending_reaction is None else f"{pending_reaction}\n\n{turn.question}"
        messages.append(ChatMessage(role="assistant", content=interviewer))
        messages.append(ChatMessage(role="user", content=turn.answer))
        pending_reaction = turn.reaction
    return messages


def build_transcript(
    questions: Sequence[InterviewQuestion], messages: Sequence[InterviewMessage]
) -> list[TranscriptItemOut]:
    """The chat as the user saw it: each question, then its answer and reaction when they exist.

    Same stored data as build_llm_messages, different view: no system prompt, no merged turns.
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
