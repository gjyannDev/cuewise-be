"""What the interview LLM calls send: the tasks and strategies registered with the core context manager.

`interviewer_turn` writes the next question. `window_ledger` (the default) keeps the input bounded: a stable prefix,
the last few turns in full, older turns as a ledger of question lines with the model's running note. `full_history`
is today's send-everything payload, never trimmed: the honest baseline and the fallback default.
`job_description_summary` condenses a long job description once, at interview start.
`follow_up_decision` judges the latest answer within its thread (the main question and its follow-ups): follow up or
move on. Both it and window_ledger keep the current thread whole.
`interviewer_stream` is the streamed turn's write call: window_ledger on interviewer_v5, whose plain-text reply can be
shown while it streams.
Both write tasks are wrapped by `WithInterviewData`: a main question of an interview with reference notes gets the v7
prompts and the notes; one with the candidate's profile gets the v8 prompts, the profile and any notes. Every other
call is unchanged.
"""

import json
from collections.abc import Mapping, Sequence
from typing import NamedTuple

from app.core.ai.context import BuiltContext, ContextManager, StrategyOutput, Task
from app.core.ai.provider import ChatMessage
from app.core.ai.tracing import REDACT_LABEL
from app.modules.profile.schemas.profile_schema import CandidateProfile

from ..ai.interviews_feedback import FeedbackThread, StoredResult
from ..constants.interviews_constants import (
    DECISION_PROMPT_VERSION,
    DECISION_TASK,
    FEEDBACK_ANSWER_CAP,
    FEEDBACK_SCORE_INPUT_LIMIT,
    FEEDBACK_SCORE_PROMPT_VERSION,
    FEEDBACK_SCORE_TASK,
    FEEDBACK_WRITE_PROMPT_VERSION,
    FEEDBACK_WRITE_TASK,
    FULL_HISTORY,
    INTERVIEWER_PROMPT_VERSION,
    INTERVIEWER_STREAM_TASK,
    INTERVIEWER_TASK,
    INTERVIEWER_V4_PROMPT_VERSION,
    INTERVIEWER_V5_PROMPT_VERSION,
    INTERVIEWER_V7_JSON_PROMPT_VERSION,
    INTERVIEWER_V7_PROMPT_VERSION,
    INTERVIEWER_V8_JSON_PROMPT_VERSION,
    INTERVIEWER_V8_PROMPT_VERSION,
    MAX_FOLLOW_UPS,
    PROFILE_TOKEN_ALLOWANCE,
    REFERENCE_NOTES_TOKEN_ALLOWANCE,
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
from ..utils.interviews_knowledge_utils import ReferenceNote
from ..utils.interviews_profile_utils import candidate_profile_block
from ..utils.interviews_utils import (
    QuestionTurn,
    build_interviewer_messages,
    job_description_block,
    load_prompt,
    main_numbers,
    neutralize_app_tags,
    render_decision_prompt,
    render_feedback_score_prompt,
    render_feedback_write_prompt,
    render_interviewer_prompt,
    render_interviewer_v2_prompt,
    render_summary_prompt,
    thread_start,
)

SUMMARY = "summary"
DECIDE = "decide"
SCORE = "score"
WRITE = "write"


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
    # The interview's stored notes, rank order. Only main-question writes render them (not decide, not follow-ups).
    reference_notes: Sequence[ReferenceNote] = ()
    # The owner's profile, read live this turn; None when the interview did not opt in or the profile is gone.
    # Main-question writes only, like the notes.
    candidate_profile: CandidateProfile | None = None


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
        # Earlier questions are replayed in the format the prompt asks for: JSON (v2-v4), or v5's streamable text.
        text_replies: bool = False,
        # The v7/v8 prompts: put the interview's reference notes after the job description (WithInterviewData decides).
        with_notes: bool = False,
        # The v8 prompts: put the candidate profile after the job description and notes (WithInterviewData decides).
        with_profile: bool = False,
    ):
        self.version = version
        self.template = load_prompt(version)
        self.window = window
        self.cap = cap
        self.limit = limit
        self.text_replies = text_replies
        self.with_notes = with_notes
        self.with_profile = with_profile

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
        # System prompt and the job-description message never change during an interview: a cacheable prefix. The
        # reference notes are fixed per interview too, so they sit in that prefix; so does the profile, which changes
        # only if the candidate replaces it mid-interview.
        notes = inputs.reference_notes if self.with_notes else ()
        profile = inputs.candidate_profile if self.with_profile else None
        profile_block = candidate_profile_block(profile) if profile is not None else None
        messages = build_interviewer_messages(system, inputs.job_description, [], notes, profile_block)
        for i, (_, turn) in enumerate(recent, start=len(turns) - len(recent)):
            answer = neutralize_app_tags(turn.answer)
            if i != len(turns) - 1 and len(answer) > self.cap:
                answer = answer[: self.cap] + TRUNCATION_MARKER
            messages.append(ChatMessage(role="assistant", content=self._replay(turn)))
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

    def _replay(self, turn: QuestionTurn) -> str:
        """An earlier question as the model would have written it. A follow-up was written without a category (it
        inherits its main question's)."""
        main = turn.kind == QuestionKind.main
        if self.text_replies:
            return f"CATEGORY: {turn.category}\n{turn.question}" if main else turn.question
        replay = {"question": turn.question}
        if main:
            replay["category"] = turn.category
        return json.dumps(replay)

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


class WithInterviewData:
    """A main-question write that carries the interview's own data: reference notes (v7) and/or the candidate's profile
    (v8, with any notes too). Any other write (neither, or a follow-up) is the plain strategy, unchanged, so interviews
    without notes or a profile send exactly what they sent before either feature.

    The notes and the profile each get their own token allowance on top of the plain limit. When even that is not
    enough, older history is trimmed first (as always), then the profile block (the unproven personalisation), then
    the notes (their depth guidance is measured, 8a), before the input would count as too large: neither block must
    ever be the reason a question falls back to the bank.
    """

    def __init__(
        self,
        plain: WindowLedger,
        notes_version: str,
        profile_version: str,
        *,
        allowance: int = REFERENCE_NOTES_TOKEN_ALLOWANCE,
        profile_allowance: int = PROFILE_TOKEN_ALLOWANCE,
    ):
        self.plain = plain
        self.with_notes = self._ledger(notes_version, with_profile=False)
        self.with_profile = self._ledger(profile_version, with_profile=True)
        self.allowance = allowance
        self.profile_allowance = profile_allowance
        self.limit = plain.limit

    def _ledger(self, version: str, *, with_profile: bool) -> WindowLedger:
        plain = self.plain
        return WindowLedger(
            version,
            window=plain.window,
            cap=plain.cap,
            limit=plain.limit,
            text_replies=plain.text_replies,
            with_notes=True,
            with_profile=with_profile,
        )

    def limit_for(self, inputs: InterviewerInputs) -> int | None:
        if self.limit is None:
            return None
        return (
            self.limit
            + self.allowance * self._uses_notes(inputs)
            + self.profile_allowance * self._uses_profile(inputs)
        )

    def droppable(self, inputs: InterviewerInputs) -> int:
        # After all older history, one step per block: the profile, then the notes.
        return self.plain.droppable(inputs) + self._uses_profile(inputs) + self._uses_notes(inputs)

    def build(self, inputs: InterviewerInputs, dropped: int) -> StrategyOutput:
        uses_notes, uses_profile = self._uses_notes(inputs), self._uses_profile(inputs)
        if not (uses_notes or uses_profile):
            return self.plain.build(inputs, dropped)
        history = self.plain.droppable(inputs)
        if dropped > history and uses_profile:
            # The profile is the first block to go: past the history, the next step drops it.
            uses_profile, dropped = False, dropped - 1
        if dropped > history:
            uses_notes = False
        if uses_profile:
            output = self.with_profile.build(inputs, dropped)
        elif uses_notes:
            output = self.with_notes.build(inputs, dropped)
        else:
            output = self.plain.build(inputs, history)
        return self._counted(output, inputs, notes=uses_notes, profile=uses_profile)

    @staticmethod
    def _counted(output: StrategyOutput, inputs: InterviewerInputs, *, notes: bool, profile: bool) -> StrategyOutput:
        """How many notes and whether the profile went into this write (numbers only, for the log and the redact rule).
        A key appears only when the interview has that data, so the log of an interview without it is unchanged."""
        counts = dict(output.counts)
        if inputs.reference_notes:
            counts["reference_notes"] = len(inputs.reference_notes) if notes else 0
        if inputs.candidate_profile is not None:
            counts["profile"] = int(profile)
        return output._replace(counts=counts)

    @staticmethod
    def _uses_notes(inputs: InterviewerInputs) -> bool:
        return bool(inputs.reference_notes) and inputs.mode == FollowUpAction.next_question

    @staticmethod
    def _uses_profile(inputs: InterviewerInputs) -> bool:
        return inputs.candidate_profile is not None and inputs.mode == FollowUpAction.next_question


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


class FeedbackScoreInputs(NamedTuple):
    """Plain values for the score call: the whole interview, read once the interview is completed."""

    role: JobRole
    level: Level
    interview_type: InterviewType
    # The effective one: the stored summary when there is one, else the original.
    job_description: str | None
    threads: Sequence[FeedbackThread]
    summary_used: bool = False


class FeedbackWriteInputs(NamedTuple):
    """Plain values for the write call: the stored scores and evidence, never the answers or the job description."""

    role: JobRole
    level: Level
    interview_type: InterviewType
    # Computed by the code; the model is told it, never asked for it.
    overall: float
    result: StoredResult


class FeedbackScore:
    """The score call: every thread whole, nothing droppable. Over its own limit it fails rather than score a part."""

    def __init__(
        self,
        version: str = FEEDBACK_SCORE_PROMPT_VERSION,
        *,
        cap: int = FEEDBACK_ANSWER_CAP,
        limit: int | None = FEEDBACK_SCORE_INPUT_LIMIT,
    ):
        self.version = version
        self.template = load_prompt(version)
        self.cap = cap
        self.limit = limit

    def droppable(self, inputs: FeedbackScoreInputs) -> int:
        return 0

    def build(self, inputs: FeedbackScoreInputs, dropped: int) -> StrategyOutput:
        system = render_feedback_score_prompt(
            role=inputs.role, level=inputs.level, interview_type=inputs.interview_type, template=self.template
        )
        parts = [job_description_block(inputs.job_description)]
        truncated = 0
        for thread in inputs.threads:
            lines = ["<question_thread>", f"Main question {thread.main_number} ({thread.category.value})"]
            for turn in thread.turns:
                label = "Question" if turn.kind == QuestionKind.main else "Follow-up"
                answer = neutralize_app_tags(turn.answer)
                if len(answer) > self.cap:
                    answer = answer[: self.cap] + TRUNCATION_MARKER
                    truncated += 1
                lines += [f"{label}: {neutralize_app_tags(turn.question)}", "<answer>", answer, "</answer>"]
            lines.append("</question_thread>")
            parts.append("\n".join(lines))
        parts.append(f"Score all {len(inputs.threads)} question threads above.")
        messages = [ChatMessage(role="system", content=system), ChatMessage(role="user", content="\n\n".join(parts))]
        counts = {
            "threads": len(inputs.threads),
            "answers": sum(len(t.turns) for t in inputs.threads),
            "truncated": truncated,
            "summary": int(inputs.summary_used),
        }
        return StrategyOutput(messages, self.version, counts)


class FeedbackWrite:
    """The write call: scores, evidence and question texts only; small whatever the interview, so no limit."""

    limit: int | None = None

    def __init__(self, version: str = FEEDBACK_WRITE_PROMPT_VERSION):
        self.version = version
        self.template = load_prompt(version)

    def droppable(self, inputs: FeedbackWriteInputs) -> int:
        return 0

    def build(self, inputs: FeedbackWriteInputs, dropped: int) -> StrategyOutput:
        system = render_feedback_write_prompt(
            role=inputs.role, level=inputs.level, interview_type=inputs.interview_type, template=self.template
        )
        lines = ["<feedback_scores>", f"Overall: {inputs.overall:.1f} out of 5 (computed by the app)"]
        questions = inputs.result.questions
        for q in questions:
            lines.append(f"Main question {q.main_number} ({q.category.value}): {neutralize_app_tags(q.question)}")
            lines.append("Scores: " + ", ".join(f"{c.value} {value}" for c, value in q.scores.items()))
            lines += [
                f'- {e.criterion.value}: "{neutralize_app_tags(e.quote)}" ({neutralize_app_tags(e.reason)})'
                for e in q.evidence
            ]
        lines.append("</feedback_scores>")
        messages = [ChatMessage(role="system", content=system), ChatMessage(role="user", content="\n".join(lines))]
        counts = {"questions": len(questions), "evidence": sum(len(q.evidence) for q in questions)}
        return StrategyOutput(messages, self.version, counts)


def _counts(full: int, ledger: int, notes: int, summary_used: bool) -> dict[str, int]:
    return {
        "turns_full": full,
        "ledger": ledger,
        "notes": notes,
        "summary": int(summary_used),
    }


def write_trace_labels(task: str, built: BuiltContext, budget_left_ms: int) -> dict[str, str | int | None]:
    """The labels of one write call. A write whose prompt carries the candidate profile is labelled `redact`: Langfuse
    then keeps its task, prompt version, usage and latency, but not its prompt or reply text (as 8c does for the
    extraction). Follow-ups and writes without the profile are traced in full, as before."""
    labels: dict[str, str | int | None] = {
        "task": task,
        "prompt_version": built.prompt_version,
        "budget_left_ms": budget_left_ms,
    }
    if built.report.counts.get("profile"):
        labels[REDACT_LABEL] = True
    return labels


def build_context_manager(prompts: Mapping[str, str] | None = None) -> ContextManager:
    """`prompts` maps a strategy name to a prompt version (the eval runner's --prompt, for ablations)."""
    prompts = prompts or {}
    return ContextManager(
        {
            INTERVIEWER_TASK: Task(
                default=WINDOW_LEDGER,
                strategies={
                    # The JSON writer: the first question and the JSON answer route.
                    WINDOW_LEDGER: WithInterviewData(
                        WindowLedger(prompts.get(WINDOW_LEDGER, INTERVIEWER_V4_PROMPT_VERSION)),
                        INTERVIEWER_V7_JSON_PROMPT_VERSION,
                        INTERVIEWER_V8_JSON_PROMPT_VERSION,
                    ),
                    FULL_HISTORY: FullHistory(
                        prompts.get(FULL_HISTORY, INTERVIEWER_PROMPT_VERSION)
                    ),
                },
            ),
            DECISION_TASK: Task(default=DECIDE, strategies={DECIDE: FollowUpDecision()}),
            # The streamed turn's write call (v5, shown while it streams); its own task keeps v4's cache prefix intact.
            INTERVIEWER_STREAM_TASK: Task(
                default=WINDOW_LEDGER,
                strategies={
                    WINDOW_LEDGER: WithInterviewData(
                        WindowLedger(INTERVIEWER_V5_PROMPT_VERSION, text_replies=True),
                        INTERVIEWER_V7_PROMPT_VERSION,
                        INTERVIEWER_V8_PROMPT_VERSION,
                    )
                },
            ),
            SUMMARY_TASK: Task(
                default=SUMMARY, strategies={SUMMARY: JobDescriptionSummary()}
            ),
            FEEDBACK_SCORE_TASK: Task(default=SCORE, strategies={SCORE: FeedbackScore()}),
            FEEDBACK_WRITE_TASK: Task(default=WRITE, strategies={WRITE: FeedbackWrite()}),
        }
    )


# Built once at import: prompt files are read at startup, like the question bank.
CONTEXT_MANAGER = build_context_manager()
