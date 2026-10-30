"""What the interview LLM calls send: the tasks and strategies registered with the core context manager.

`interviewer_turn` writes the next question. `window_ledger` (the default) keeps the input bounded: a stable prefix,
the last few turns in full, older turns as a ledger of question lines with the model's running note. `full_history`
is today's send-everything payload, never trimmed: the honest baseline and the fallback default.
`job_description_summary` condenses a long job description once, at interview start.
"""

import json
from collections.abc import Mapping, Sequence
from typing import NamedTuple

from app.core.ai.context import ContextManager, StrategyOutput, Task
from app.core.ai.provider import ChatMessage

from .interviews_constants import (
    FULL_HISTORY,
    INTERVIEWER_PROMPT_VERSION,
    INTERVIEWER_TASK,
    INTERVIEWER_V2_PROMPT_VERSION,
    SUMMARY_PROMPT_VERSION,
    SUMMARY_TASK,
    TRUNCATION_MARKER,
    WINDOW_ANSWER_CAP,
    WINDOW_INPUT_LIMIT,
    WINDOW_LEDGER,
    WINDOW_TURNS,
    InterviewType,
    JobRole,
    Level,
)
from .interviews_utils import (
    QuestionTurn,
    build_interviewer_messages,
    job_description_block,
    load_prompt,
    neutralize_app_tags,
    render_interviewer_prompt,
    render_interviewer_v2_prompt,
    render_summary_prompt,
)

SUMMARY = "summary"


class InterviewerInputs(NamedTuple):
    """Plain values for one interviewer call; the next question is number len(turns) + 1."""

    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    # The effective one: the stored summary when there is one, else the original.
    job_description: str | None
    # Every answered question, oldest first.
    turns: Sequence[QuestionTurn]
    summary_used: bool = False


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
            question_number=len(inputs.turns) + 1,
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
        version: str = INTERVIEWER_V2_PROMPT_VERSION,
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
        # Everything but the latest turn: the model must see the answer it is reacting to.
        return max(len(inputs.turns) - 1, 0)

    def build(self, inputs: InterviewerInputs, dropped: int) -> StrategyOutput:
        numbered = list(enumerate(inputs.turns, start=1))
        older, recent = numbered[: -self.window], numbered[-self.window :]
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
        for number, turn in recent:
            answer = neutralize_app_tags(turn.answer)
            if number != len(numbered) and len(answer) > self.cap:
                answer = answer[: self.cap] + TRUNCATION_MARKER
            messages.append(
                ChatMessage(
                    role="assistant",
                    content=json.dumps(
                        {"question": turn.question, "category": turn.category}
                    ),
                )
            )
            messages.append(ChatMessage(role="user", content=answer))
        if numbered:
            status = self._status(len(numbered) + 1, inputs.question_count, ledger)
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
        next_number: int, total: int, ledger: Sequence[tuple[int, QuestionTurn]]
    ) -> str:
        lines = [f"You are about to ask question {next_number} of {total}."]
        if next_number == total:
            lines.append("This is the final question.")
        if ledger:
            lines.append("Earlier questions no longer shown in full:")
            for number, turn in ledger:
                line = f"{number}. {neutralize_app_tags(turn.question)}"
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
                        prompts.get(WINDOW_LEDGER, INTERVIEWER_V2_PROMPT_VERSION)
                    ),
                    FULL_HISTORY: FullHistory(
                        prompts.get(FULL_HISTORY, INTERVIEWER_PROMPT_VERSION)
                    ),
                },
            ),
            SUMMARY_TASK: Task(
                default=SUMMARY, strategies={SUMMARY: JobDescriptionSummary()}
            ),
        }
    )


# Built once at import: prompt files are read at startup, like the question bank.
CONTEXT_MANAGER = build_context_manager()
