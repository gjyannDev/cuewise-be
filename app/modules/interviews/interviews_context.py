"""What the interview LLM calls send: the tasks and strategies registered with the core context manager.

`interviewer_turn` writes the next question. `window_ledger` (the default) keeps the input bounded: a stable prefix,
the last few turns in full, older turns as a ledger of question lines with the model's running note. `full_history`
is today's send-everything payload, never trimmed: the honest baseline and the fallback default.
`job_description_summary` condenses a long job description once, at interview start.
`follow_up_decision` judges the latest answer within its thread (the main question and its follow-ups): follow up or
move on. Both it and window_ledger keep the current thread whole.
"""

import json
from collections.abc import Mapping, Sequence
from typing import NamedTuple

from app.core.ai.context import ContextManager, StrategyOutput, Task
from app.core.ai.provider import ChatMessage

from .interviews_constants import (
    DECISION_PROMPT_VERSION,
    DECISION_TASK,
    FULL_HISTORY,
    INTERVIEWER_PROMPT_VERSION,
    INTERVIEWER_TASK,
    INTERVIEWER_V4_PROMPT_VERSION,
    MAX_FOLLOW_UPS,
    SUMMARY_PROMPT_VERSION,
    SUMMARY_TASK,
    TRUNCATION_MARKER,
    WINDOW_ANSWER_CAP,
    WINDOW_INPUT_LIMIT,
    WINDOW_LEDGER,
    WINDOW_TURNS,
    FollowUpAction,
    FollowUpGap,
    InterviewType,
    JobRole,
    Level,
    QuestionKind,
)
from .interviews_utils import (
    QuestionTurn,
    build_interviewer_messages,
    job_description_block,
    load_prompt,
    main_numbers,
    neutralize_app_tags,
    render_decision_prompt,
    render_interviewer_prompt,
    render_interviewer_v2_prompt,
    render_summary_prompt,
    thread_start,
)

SUMMARY = "summary"
DECIDE = "decide"


class InterviewerInputs(NamedTuple):
    """Plain values for one interviewer or decide call."""

    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    # The effective one: the stored summary when there is one, else the original.
    job_description: str | None
    # Every answered question (main and follow-up), oldest first.
    turns: Sequence[QuestionTurn]
    summary_used: bool = False
    # Write calls only: what to write, set by the code after the decision and its limits.
    mode: FollowUpAction = FollowUpAction.next_question
    gap: FollowUpGap | None = None


class SummaryInputs(NamedTuple):
    job_description: str


class FullHistory:
    # Never trimmed: the honest baseline. Annotated so it matches the Strategy protocol's `int | None`.
    limit: int | None = None

    def __init__(self, version: str = INTERVIEWER_PROMPT_VERSION):
        self.version = version
        self.template = load_prompt(version)

    def droppable(self, inputs: InterviewerInputs) -> int:
        return 0

    def build(self, inputs: InterviewerInputs, dropped: int) -> StrategyOutput:
        system = render_interviewer_prompt(
            role=inputs.role,
            level=inputs.level,
            interview_type=inputs.interview_type,
            question_number=len([t for t in inputs.turns if t.kind == QuestionKind.main]) + 1,
            question_count=inputs.question_count,
            template=self.template,
        )
        messages = build_interviewer_messages(
            system, inputs.job_description, inputs.turns
        )
        return StrategyOutput(
            messages,
            self.version,
            _counts(len(inputs.turns), 0, 0, inputs.summary_used),
        )


class WindowLedger:
    def __init__(
        self,
        version: str = INTERVIEWER_V4_PROMPT_VERSION,
        *,
        window: int = WINDOW_TURNS,
        cap: int = WINDOW_ANSWER_CAP,
        limit: int | None = WINDOW_INPUT_LIMIT,
    ):
        self.version = version
        self.template = load_prompt(version)
        self.window = window
        self.cap = cap
        self.limit = limit

    def droppable(self, inputs: InterviewerInputs) -> int:
        # Everything older than the current thread: the model must see the whole thread it is writing for.
        return thread_start(inputs.turns)

    def build(self, inputs: InterviewerInputs, dropped: int) -> StrategyOutput:
        turns = inputs.turns
        numbered = list(zip(main_numbers(turns), turns, strict=True))
        # The window never starts inside a thread: it moves back to that thread's main question.
        cut = thread_start(turns, len(turns) - self.window) if len(turns) > self.window else 0
        older, recent = numbered[:cut], numbered[cut:]
        # Oldest first: ledger lines, then window turns.
        from_older = min(dropped, len(older))
        ledger, recent = older[from_older:], recent[dropped - from_older :]

        system = render_interviewer_v2_prompt(
            role=inputs.role,
            level=inputs.level,
            interview_type=inputs.interview_type,
            question_count=inputs.question_count,
            template=self.template,
        )
        # System prompt and the job-description message never change during an interview: a cacheable prefix.
        messages = build_interviewer_messages(system, inputs.job_description, [])
        for i, (_, turn) in enumerate(recent, start=len(turns) - len(recent)):
            answer = neutralize_app_tags(turn.answer)
            if i != len(turns) - 1 and len(answer) > self.cap:
                answer = answer[: self.cap] + TRUNCATION_MARKER
            replay = {"question": turn.question}
            # A follow-up was written without a category (it inherits its main question's).
            if turn.kind == QuestionKind.main:
                replay["category"] = turn.category
            messages.append(ChatMessage(role="assistant", content=json.dumps(replay)))
            messages.append(ChatMessage(role="user", content=answer))
        if numbered:
            status = self._status(inputs, numbered[-1][0], ledger)
            messages[-1] = ChatMessage(
                role="user", content=f"{messages[-1].content}\n\n{status}"
            )

        notes = sum(1 for _, turn in ledger if turn.note)
        return StrategyOutput(
            messages,
            self.version,
            _counts(len(recent), len(ledger), notes, inputs.summary_used),
        )

    @staticmethod
    def _status(
        inputs: InterviewerInputs, current: int, ledger: Sequence[tuple[int, QuestionTurn]]
    ) -> str:
        total = inputs.question_count
        if inputs.mode == FollowUpAction.follow_up:
            used = len(inputs.turns) - 1 - thread_start(inputs.turns)
            lines = [
                f"Write follow-up {used + 1} of at most {MAX_FOLLOW_UPS} on question {current} of {total}.",
                f"The gap in the latest answer: {inputs.gap}.",
            ]
        else:
            lines = [f"You are about to ask question {current + 1} of {total}."]
            if current + 1 == total:
                lines.append("This is the final question.")
        return _status_block(lines, ledger, "Earlier questions no longer shown in full:")


class FollowUpDecision:
    """The decide call: the current thread in full (it judges the latest answer within it), older questions as notes.

    No job description: judging an answer doesn't need it, and leaving it out keeps it from steering the decision.
    """

    def __init__(self, *, limit: int | None = WINDOW_INPUT_LIMIT):
        self.limit = limit

    def droppable(self, inputs: InterviewerInputs) -> int:
        return thread_start(inputs.turns)

    def build(self, inputs: InterviewerInputs, dropped: int) -> StrategyOutput:
        turns = inputs.turns
        start = thread_start(turns)
        ledger = list(zip(main_numbers(turns), turns, strict=True))[dropped:start]
        messages = [
            ChatMessage(
                role="system",
                content=render_decision_prompt(
                    role=inputs.role, level=inputs.level, interview_type=inputs.interview_type
                ),
            )
        ]
        for turn in turns[start:]:
            messages.append(ChatMessage(role="assistant", content=turn.question))
            messages.append(ChatMessage(role="user", content=neutralize_app_tags(turn.answer)))
        left = MAX_FOLLOW_UPS - (len(turns) - 1 - start)
        status = _status_block(
            [f"Follow-ups left for this question: {left} of {MAX_FOLLOW_UPS}."], ledger, "Earlier questions:"
        )
        messages[-1] = ChatMessage(role="user", content=f"{messages[-1].content}\n\n{status}")
        notes = sum(1 for _, turn in ledger if turn.note)
        return StrategyOutput(
            messages,
            DECISION_PROMPT_VERSION,
            _counts(len(turns) - start, len(ledger), notes, inputs.summary_used),
        )


def _status_block(lines: list[str], ledger: Sequence[tuple[int, QuestionTurn]], heading: str) -> str:
    """App data at the end of the last user message; untrusted parts (questions, notes) have their tags neutralised."""
    if ledger:
        lines = [*lines, heading]
        for number, turn in ledger:
            label = f"{number}." if turn.kind == QuestionKind.main else f"{number} (follow-up)."
            line = f"{label} {neutralize_app_tags(turn.question)}"
            if turn.note:
                line += f" | Note on the answer: {neutralize_app_tags(turn.note)}"
            lines.append(line)
    return "<interview_status>\n" + "\n".join(lines) + "\n</interview_status>"


class JobDescriptionSummary:
    limit: int | None = None

    def droppable(self, inputs: SummaryInputs) -> int:
        return 0

    def build(self, inputs: SummaryInputs, dropped: int) -> StrategyOutput:
        messages = [
            ChatMessage(role="system", content=render_summary_prompt()),
            ChatMessage(
                role="user", content=job_description_block(inputs.job_description)
            ),
        ]
        return StrategyOutput(
            messages,
            SUMMARY_PROMPT_VERSION,
            {"job_description_chars": len(inputs.job_description)},
        )


def _counts(full: int, ledger: int, notes: int, summary_used: bool) -> dict[str, int]:
    return {
        "turns_full": full,
        "ledger": ledger,
        "notes": notes,
        "summary": int(summary_used),
    }


def build_context_manager(prompts: Mapping[str, str] | None = None) -> ContextManager:
    """`prompts` maps a strategy name to a prompt version (the eval runner's --prompt, for ablations)."""
    prompts = prompts or {}
    return ContextManager(
        {
            INTERVIEWER_TASK: Task(
                default=WINDOW_LEDGER,
                strategies={
                    WINDOW_LEDGER: WindowLedger(
                        prompts.get(WINDOW_LEDGER, INTERVIEWER_V4_PROMPT_VERSION)
                    ),
                    FULL_HISTORY: FullHistory(
                        prompts.get(FULL_HISTORY, INTERVIEWER_PROMPT_VERSION)
                    ),
                },
            ),
            DECISION_TASK: Task(default=DECIDE, strategies={DECIDE: FollowUpDecision()}),
            SUMMARY_TASK: Task(
                default=SUMMARY, strategies={SUMMARY: JobDescriptionSummary()}
            ),
        }
    )


# Built once at import: prompt files are read at startup, like the question bank.
CONTEXT_MANAGER = build_context_manager()
