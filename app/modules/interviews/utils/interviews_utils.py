import json
import math
import random
import re
from collections.abc import AsyncGenerator, Collection, Mapping, Sequence
from contextlib import aclosing
from itertools import chain, groupby, zip_longest
from pathlib import Path
from typing import NamedTuple

from pydantic import TypeAdapter, ValidationError

from app.core.ai.provider import ChatMessage
from app.core.errors import NotEnoughQuestionsError

from ..constants.interviews_constants import (
    AUDIO_CONTENT_TYPES,
    CATEGORY_CRITERIA,
    CLOSING_REACTIONS,
    DECISION_PROMPT_VERSION,
    FEEDBACK_ITEM_MAX_LENGTH,
    FEEDBACK_NOTE_MAX_LENGTH,
    FEEDBACK_RUBRIC_PATH,
    FEEDBACK_SCORE_PROMPT_VERSION,
    FEEDBACK_SUMMARY_MAX_LENGTH,
    FEEDBACK_TONE,
    FEEDBACK_WRITE_PROMPT_VERSION,
    GENERAL_ROLE,
    IMPROVEMENTS_COUNT,
    INTERVIEWER_PROMPT_VERSION,
    INTERVIEWER_V2_PROMPT_VERSION,
    LEVEL_GROUPS,
    LEVEL_GUIDANCE,
    MAX_FOLLOW_UPS,
    NEXT_STEPS_COUNT,
    PROMPTS_DIR,
    QUESTION_BANK_PATH,
    QUOTE_MAX_LENGTH,
    QUOTE_MIN_LENGTH,
    REACTION_POOLS,
    REASON_MAX_LENGTH,
    SCORE_MAX,
    SCORE_MIN,
    STRENGTHS_COUNT,
    SUMMARY_MAX_LENGTH,
    SUMMARY_MAX_WORDS,
    SUMMARY_PROMPT_VERSION,
    AudioContainer,
    InterviewType,
    JobRole,
    Level,
    MessageKind,
    MessageRole,
    QuestionCategory,
    QuestionKind,
    SessionStatus,
)
from ..models.interviews_model import InterviewMessage, InterviewQuestion
from ..schemas.interviews_schema import (
    BankQuestion,
    QuestionBank,
    Rubric,
    StreamEventOut,
    TranscriptItemOut,
)

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
        of_question = {"question_id": q.id, "position": q.position, "question_kind": q.kind, "main_number": q.main_number}
        items.append(
            TranscriptItemOut(
                id=q.id,
                role=MessageRole.interviewer,
                kind=MessageKind.question,
                text=q.text,
                created_at=None,
                **of_question,
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
                        role=role,
                        kind=kind,
                        text=message.content,
                        created_at=message.created_at,
                        **of_question,
                    )
                )
    return items


_PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")
# Matches an opening or closing tag the app uses to fence data, in any case, so untrusted text can't close its own
# block or fake the app's status block.
APP_TAG = re.compile(
    r"<\s*/?\s*(job_description|interview_status|question_thread|answer|feedback_scores)\s*>", re.IGNORECASE
)


def neutralize_app_tags(text: str) -> str:
    return APP_TAG.sub("[tag removed]", text)


# Loaded at import like the bank: a missing prompt file stops the app at startup, not mid-interview.
INTERVIEWER_PROMPT = load_prompt(INTERVIEWER_PROMPT_VERSION)
INTERVIEWER_V2_PROMPT = load_prompt(INTERVIEWER_V2_PROMPT_VERSION)
SUMMARY_PROMPT = load_prompt(SUMMARY_PROMPT_VERSION)
DECISION_PROMPT = load_prompt(DECISION_PROMPT_VERSION)
FEEDBACK_SCORE_PROMPT = load_prompt(FEEDBACK_SCORE_PROMPT_VERSION)
FEEDBACK_WRITE_PROMPT = load_prompt(FEEDBACK_WRITE_PROMPT_VERSION)


def load_rubric(path: Path) -> Rubric:
    """Read and validate a feedback rubric file; a bad one fails loudly at startup, like the bank."""
    try:
        return Rubric.model_validate_json(path.read_bytes())
    except ValidationError as exc:
        raise ValueError(f"Invalid feedback rubric {path.name}: {exc}") from exc


FEEDBACK_RUBRIC = load_rubric(FEEDBACK_RUBRIC_PATH)

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
    # The model's running note about this answer, when it wrote a usable one (window_ledger shows it for old turns).
    note: str | None = None
    kind: str = QuestionKind.main


def main_numbers(turns: Sequence[QuestionTurn]) -> list[int]:
    """The main-question number of each turn: a follow-up shares the number of the main question it digs into."""
    numbers, count = [], 0
    for turn in turns:
        count += turn.kind == QuestionKind.main
        numbers.append(count)
    return numbers


def thread_start(turns: Sequence[QuestionTurn], index: int | None = None) -> int:
    """Index of the main question whose thread holds turn `index` (default: the latest turn)."""
    index = len(turns) - 1 if index is None else index
    return max((i for i in range(index + 1) if turns[i].kind == QuestionKind.main), default=0)


def render_template(template: str, values: Mapping[str, object]) -> str:
    """Fill {{name}} placeholders in one pass: inserted values are never scanned again, and a missing one fails.

    Plain str.format would choke on the literal JSON braces in the prompt.
    """
    return _PLACEHOLDER.sub(lambda m: str(values[m.group(1)]), template)


def render_interviewer_prompt(
    *,
    role: JobRole,
    level: Level,
    interview_type: InterviewType,
    question_number: int,
    question_count: int,
    template: str = INTERVIEWER_PROMPT,
) -> str:
    """Only trusted values go in here; the job description and answers never enter the system prompt."""
    return render_template(
        template,
        {
            "role": role.value,
            "level": level.value,
            "interview_type": interview_type.value,
            "question_number": question_number,
            "question_count": question_count,
            "category_rule": _CATEGORY_RULES[interview_type],
        },
    )


def render_interviewer_v2_prompt(
    *,
    role: JobRole,
    level: Level,
    interview_type: InterviewType,
    question_count: int,
    template: str = INTERVIEWER_V2_PROMPT,
) -> str:
    """Per-interview constants only, so the text is identical on every call of an interview (a cacheable prefix)."""
    return render_template(
        template,
        {
            "role": role.value,
            "level": level.value,
            "interview_type": interview_type.value,
            "question_count": question_count,
            "category_rule": _CATEGORY_RULES[interview_type],
            "level_guidance": LEVEL_GUIDANCE[level],
        },
    )


def render_summary_prompt() -> str:
    return render_template(SUMMARY_PROMPT, {"max_words": SUMMARY_MAX_WORDS, "max_length": SUMMARY_MAX_LENGTH})


def render_decision_prompt(*, role: JobRole, level: Level, interview_type: InterviewType) -> str:
    """Per-interview constants only, like v2: the decide call's system prompt never changes during an interview."""
    return render_template(
        DECISION_PROMPT,
        {
            "role": role.value,
            "level": level.value,
            "interview_type": interview_type.value,
            "level_guidance": LEVEL_GUIDANCE[level],
            "max_follow_ups": MAX_FOLLOW_UPS,
        },
    )


def interview_categories(interview_type: InterviewType) -> list[QuestionCategory]:
    """The question categories an interview of this type can hold (mixed: both)."""
    if interview_type == InterviewType.mixed:
        return list(QuestionCategory)
    return [QuestionCategory(interview_type)]


def render_rubric(rubric: Rubric, categories: Sequence[QuestionCategory], level: Level) -> str:
    """The anchors of the criteria this interview can be scored on, with this level group's expectation each."""
    group = LEVEL_GROUPS[level]
    lines: list[str] = []
    for category in categories:
        for criterion in CATEGORY_CRITERIA[category]:
            entry = rubric.criteria[criterion]
            lines.append(f'"{criterion.value}" ({category.value}): {entry.question}')
            lines += [f"  {score}: {entry.levels[score]}" for score in sorted(entry.levels)]
            lines.append(f"  Expected at this level: {entry.expectations[group]}")
    return "\n".join(lines)


def render_feedback_score_prompt(
    *,
    role: JobRole,
    level: Level,
    interview_type: InterviewType,
    template: str = FEEDBACK_SCORE_PROMPT,
    rubric: Rubric = FEEDBACK_RUBRIC,
) -> str:
    """Per-interview constants and the rubric only: no answer or job-description text ever enters the system prompt."""
    categories = interview_categories(interview_type)
    criteria = "\n".join(
        f"  {category.value}: " + ", ".join(f'"{c.value}"' for c in CATEGORY_CRITERIA[category]) for category in categories
    )
    return render_template(
        template,
        {
            "role": role.value,
            "level": level.value,
            "interview_type": interview_type.value,
            "level_group": LEVEL_GROUPS[level].value,
            "criteria": criteria,
            "rubric": render_rubric(rubric, categories, level),
            "score_min": SCORE_MIN,
            "score_max": SCORE_MAX,
            "quote_min": QUOTE_MIN_LENGTH,
            "quote_max": QUOTE_MAX_LENGTH,
            "reason_max": REASON_MAX_LENGTH,
        },
    )


def render_feedback_write_prompt(
    *, role: JobRole, level: Level, interview_type: InterviewType, template: str = FEEDBACK_WRITE_PROMPT
) -> str:
    """Counts and limits come from the constants the write parser checks; a test checks the labels match too."""

    def count(fewest_most: tuple[int, int]) -> str:
        fewest, most = fewest_most
        return f"{fewest} to {most}" if most - fewest > 1 else f"{fewest} or {most}"

    return render_template(
        template,
        {
            "role": role.value,
            "level": level.value,
            "interview_type": interview_type.value,
            "tone": FEEDBACK_TONE[LEVEL_GROUPS[level]],
            "summary_max": FEEDBACK_SUMMARY_MAX_LENGTH,
            "item_max": FEEDBACK_ITEM_MAX_LENGTH,
            "note_max": FEEDBACK_NOTE_MAX_LENGTH,
            "strengths_count": count(STRENGTHS_COUNT),
            "improvements_count": count(IMPROVEMENTS_COUNT),
            "next_steps_count": count(NEXT_STEPS_COUNT),
        },
    )


def job_description_block(job_description: str | None) -> str:
    """Untrusted text, fenced as data. Tags inside it are neutralised so it can't close its own block."""
    if not job_description:
        return "No job description was provided."
    return f"<job_description>\n{neutralize_app_tags(job_description)}\n</job_description>"


def interviewer_history(
    questions: Sequence[InterviewQuestion], messages: Sequence[InterviewMessage]
) -> list[QuestionTurn]:
    """Answered questions with their answers (and the model's note on each), in interview order.

    Stored reactions are left out on purpose.
    """
    answers = {m.question_id: m for m in messages if m.role == MessageRole.candidate}
    return [
        QuestionTurn(q.text, q.category, answers[q.id].content, answers[q.id].note, q.kind)
        for q in sorted(questions, key=lambda q: q.position)
    ]


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


def build_usage_report(questions: Sequence[InterviewQuestion]) -> str:
    """Stored LLM usage per interview and question position: numbers and ids only, never question text.

    Expects rows ordered by session, then position. Usage the provider didn't report (or bank questions) shows as
    `-` and is left out of the sums. A question's usage is its whole turn (the decide call too), so tokens by
    question kind answer "what does a follow-up cost"; decide-only tokens are in the per-call log lines.
    """

    def shown(value: object) -> str:
        return "-" if value is None else str(value)

    lines: list[str] = []
    prompt_sums: list[int] = []
    completion_sums: list[int] = []
    for session_id, rows in groupby(questions, key=lambda q: q.session_id):
        rows = list(rows)
        llm = sum(1 for q in rows if q.source == "llm")
        follow_ups = sum(1 for q in rows if q.kind == QuestionKind.follow_up)
        lines.append(
            f"interview {session_id} questions={len(rows)} llm={llm} bank={len(rows) - llm} follow_ups={follow_ups}"
        )
        for q in rows:
            lines.append(
                f"  q{q.position} prompt={shown(q.prompt_tokens)} completion={shown(q.completion_tokens)} "
                f"latency_ms={shown(q.latency_ms)} source={q.source} prompt_version={shown(q.prompt_version)} "
                f"kind={q.kind}"
            )
        prompt, completion = sum(q.prompt_tokens or 0 for q in rows), sum(q.completion_tokens or 0 for q in rows)
        lines.append(f"  total prompt={prompt} completion={completion}")
        if llm:
            prompt_sums.append(prompt)
            completion_sums.append(completion)

    interviews = len({q.session_id for q in questions})
    used = len(prompt_sums)
    summary = f"interviews={interviews} llm_interviews={used}"
    if used:
        # Averaged over interviews that used the LLM: bank-only ones (LLM off) would hide the real cost.
        summary += (
            f" avg_prompt_per_llm_interview={round(sum(prompt_sums) / used)}"
            f" avg_completion_per_llm_interview={round(sum(completion_sums) / used)}"
        )
    lines.append(summary)
    if used:
        by_kind = " ".join(
            f"{kind} prompt={sum(q.prompt_tokens or 0 for q in questions if q.kind == kind)}"
            f" completion={sum(q.completion_tokens or 0 for q in questions if q.kind == kind)}"
            for kind in QuestionKind
        )
        follow_ups = sum(1 for q in questions if q.kind == QuestionKind.follow_up)
        lines.append(f"tokens {by_kind} follow_ups={follow_ups}")
    # A stored question's latency is the LLM time of the turn that produced it: does the turn budget fit?
    turn_ms = sorted(q.latency_ms for q in questions if q.source == "llm" and q.latency_ms is not None)
    if turn_ms:
        lines.append(f"turn_llm_ms p50={percentile(turn_ms, 50)} p95={percentile(turn_ms, 95)} turns={len(turn_ms)}")
    return "\n".join(lines)


def percentile(ordered: Sequence[int], p: int) -> int:
    """Nearest rank: a value that was really measured, which reads better than an interpolated one for few turns."""
    return ordered[max(math.ceil(p / 100 * len(ordered)) - 1, 0)]


def sse_frame(event: StreamEventOut) -> dict[str, str]:
    """One streamed-turn event as the dict sse-starlette encodes: the event name, and its data as one line of JSON."""
    return {"event": event.event.value, "data": event.data.model_dump_json()}


async def sse_frames(events: AsyncGenerator[StreamEventOut]) -> AsyncGenerator[dict[str, str]]:
    """The controller's events as SSE frames. Closing this (a client that left) closes the turn right away, so its
    cleanup runs now and not whenever the event loop collects the abandoned generator."""
    async with aclosing(events):
        async for event in events:
            yield sse_frame(event)


def _has_signature(container: AudioContainer, head: bytes) -> bool:
    match container:
        case AudioContainer.webm:
            return head[:4] == b"\x1a\x45\xdf\xa3"  # EBML header
        case AudioContainer.ogg:
            return head[:4] == b"OggS"
        case AudioContainer.mp4:
            return head[4:8] == b"ftyp"
        case AudioContainer.wav:
            return head[:4] == b"RIFF" and head[8:12] == b"WAVE"


def audio_container(declared_type: str, head: bytes) -> AudioContainer | None:
    """The container of an uploaded recording, or None when its declared type isn't allowed or its first bytes don't
    match that type. Checked before anything is sent to the vendor, so junk never costs a transcription."""
    container = AUDIO_CONTENT_TYPES.get(declared_type.split(";", 1)[0].strip().lower())
    if container is None or not _has_signature(container, head):
        return None
    return container


def answered_main_questions(status: SessionStatus, question_count: int, current_main_number: int | None) -> int:
    """Main questions finished ("answered 2 of 5"): every one once completed, else every one before the question the
    interview waits on. A pending follow-up belongs to a main question that isn't finished yet; follow-ups never count.
    """
    if status == SessionStatus.completed:
        return question_count
    if current_main_number is None:
        return 0
    return max(0, min(current_main_number - 1, question_count))
