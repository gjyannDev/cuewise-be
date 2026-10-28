import random
from itertools import chain, zip_longest
from pathlib import Path

from pydantic import TypeAdapter, ValidationError

from app.core.errors import NotEnoughQuestionsError

from .interviews_constants import GENERAL_ROLE, QUESTION_BANK_PATH, InterviewType, JobRole, Level, QuestionCategory
from .interviews_schema import BankQuestion, QuestionBank

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
