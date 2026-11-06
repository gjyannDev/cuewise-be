"""The two LLM calls of end-of-interview feedback: score (closed JSON), then write (plain text).

The score call reads the whole interview and is the expensive one, so a failed write call never repeats it: the
controller stores the scores as soon as they validate, then asks for the text, and falls back to the template if the
write call fails. One deadline is shared by both calls; each call is also still capped by the provider's own limits.
Every call logs one metadata line (llm_call), and every generation one summary line; never answer, quote or text.
"""

import logging
import uuid
from collections.abc import Callable, Sequence
from typing import NamedTuple, TypeVar

from app.core.ai.context import BuiltContext, ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMProvider, LLMResult
from app.core.ai.tracing import Tracer

from .interviews_constants import (
    FEEDBACK_CHECKS,
    FEEDBACK_RUBRIC_VERSION,
    FEEDBACK_SCORE_STEP,
    FEEDBACK_SCORE_TASK,
    FEEDBACK_WRITE_STEP,
    FEEDBACK_WRITE_TASK,
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
    TextSource,
)
from .interviews_context import FeedbackScoreInputs, FeedbackWriteInputs
from .interviews_feedback import (
    ScoreResult,
    WriteText,
    parse_score_reply,
    parse_write_reply,
)
from .interviews_reply import InvalidReplyError
from .interviews_turn import (
    Deadline,
    llm_logger,
    log_llm_call,
    log_llm_error,
    log_result,
    sum_known,
)

T = TypeVar("T")

# Where to look first when a feedback call fails, by reason code: rules of thumb shown in Langfuse next to the failure
# (the checks and steps of live traces, and the eval traces). They narrow the search; they are not a diagnosis.
_REPLY_HINTS = {
    # The score call's closed JSON
    "fence": "Text around the JSON fence: the prompt's Output section asks for the JSON object only.",
    "not_json": "The reply isn't JSON: read the generation's output; if it stops mid-way, max_tokens cut it (finish).",
    "not_object": "The reply is JSON but not one object: the Output section shows the exact shape.",
    "schema": "A field is missing, extra or of the wrong type (a score as 3.5 or \"3\"): compare with the Output shape.",
    "truncated": "Cut off by max_tokens (finish=length): raise the call's max tokens or ask for shorter reasons.",
    "questions": "A main question is missing, repeated or out of order: one entry per thread, in the order given.",
    "criteria": "Scores don't use exactly the thread's category criteria: check the criteria list rendered in the prompt.",
    "score_range": "A score outside 1-5: check the scale line of the Task section.",
    "evidence_missing": "A question has no evidence item: the prompt asks for at least one per thread.",
    "evidence_criterion": "Evidence names a criterion of the other category: compare with the thread's category.",
    "evidence_duplicate": "Two evidence items for one criterion: the prompt allows at most one per criterion.",
    "quote_length": "A quote is under 10 or over 200 characters: ask for one exact sentence, not a word or a paragraph.",
    "quote_not_found": (
        "The quote isn't in that question's answers: compare it with the generation's input. A paraphrase, a quote "
        "from a question or the job description, or one from another thread all fail."
    ),
    "reason": "A reason is empty, over 120 characters or contains markup: see the evidence rule of the Task section.",
    # The write call's labelled text
    "format": "The sections aren't exactly SUMMARY, STRENGTHS, IMPROVEMENTS, NEXT STEPS, NOTES, in order, nothing else.",
    "count": "A list has too few or too many items: compare with the counts in the prompt's Output section.",
    "notes": "The NOTES don't have exactly one line per main question number.",
    "length": "A slot is over its length limit: the limits are in the prompt's Output section.",
    "markup": "Markdown (bold, headings, code, links) or an app tag in the text: the client shows plain strings.",
}
_FAILURE_HINTS = {
    "empty_reply": "No text came back: often a reasoning model spending all of max_tokens; check finish and tokens.",
    "no_time": "The feedback budget was spent before this call could start: look at the earlier calls' latency.",
    "retry_skipped:no_time": "A retry was due but under 5 s of budget was left: the first attempt was slow.",
    "context_too_large": "The interview is over the score call's input limit: no call was made; check the limit.",
    "LLMRateLimitError": "The provider's rate limit, not a quality problem: wait, or pace the calls (free tier ~25/min).",
    "LLMTimeoutError": "The provider didn't answer in time, not a quality problem: check latency and the timeouts.",
}
_PROVIDER_HINT = "The provider call failed, not a quality problem: check the provider, key and model, then retry."


def hint_for(code: str | None) -> str | None:
    """The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a provider error's class name...)."""
    if code is None:
        return None
    reason = code.removeprefix("invalid_reply:")
    if code != reason:
        return _REPLY_HINTS.get(reason)
    if code in _FAILURE_HINTS:
        return _FAILURE_HINTS[code]
    return _PROVIDER_HINT if code.startswith("LLM") and code.endswith("Error") else None


class CallUsage(NamedTuple):
    """One call's cost, summed over its attempts (what the feedback row stores)."""

    model: str | None
    prompt_tokens: int | None
    completion_tokens: int | None
    latency_ms: int

    @classmethod
    def of(cls, results: Sequence[LLMResult]) -> CallUsage:
        return cls(
            results[-1].model if results else None,
            sum_known([r.prompt_tokens for r in results]),
            sum_known([r.completion_tokens for r in results]),
            sum(r.latency_ms for r in results),
        )


class Scored(NamedTuple):
    # None = failed: no partial scores, ever.
    result: ScoreResult | None
    # Every attempt that came back, valid or not (their usage is stored).
    results: list[LLMResult]
    prompt_version: str | None
    # A reason code when `result` is None: no_time, context_too_large, empty_reply, invalid_reply:<reason>, or the
    # provider error's class name.
    failure: str | None
    quotes_rejected: int
    # Answers shortened in the call (a count, never text).
    truncated: int


class WriteOutcome(NamedTuple):
    # None = the controller uses the template.
    text: WriteText | None
    results: list[LLMResult]
    prompt_version: str | None
    failure: str | None


class _Attempts(NamedTuple):
    parsed: object | None
    results: list[LLMResult]
    failure: str | None
    reasons: list[str]
    # One outcome per attempt (ok, invalid_reply:<reason>, empty_reply, a provider error's class name), plus
    # `retry_skipped:no_time` when a retry was due but the budget was too low. Shown on the step in Langfuse.
    outcomes: list[str]


class FeedbackGenerator:
    def __init__(
        self,
        llm: LLMProvider,
        context: ContextManager,
        *,
        score_max_tokens: int,
        write_max_tokens: int,
        score_temperature: float,
        clock: Callable[[], float],
        tracer: Tracer | None = None,
    ):
        self.llm = llm
        self.context = context
        self.score_max_tokens = score_max_tokens
        self.write_max_tokens = write_max_tokens
        self.score_temperature = score_temperature
        self.clock = clock
        # Langfuse steps and checks (metadata only); the generations themselves come from the TracingProvider.
        self.tracer = tracer or Tracer(None)

    def deadline(self, seconds: float) -> Deadline:
        """One budget for the whole generation, started when the request holds its claim."""
        return Deadline(self.clock, seconds)

    def score(self, session_id: uuid.UUID, inputs: FeedbackScoreInputs, deadline: Deadline) -> Scored:
        """At most two attempts; a retry only for a reply that came back but broke the contract, and only with time
        left. Any other failure ends it: the feedback fails rather than show invented or partial scores."""
        with self.tracer.step(
            FEEDBACK_SCORE_STEP,
            metadata={"rubric_version": FEEDBACK_RUBRIC_VERSION, "budget_left_ms": round(deadline.remaining() * 1000)},
        ) as step:
            try:
                built = self.context.build(FEEDBACK_SCORE_TASK, inputs)
            except ContextTooLargeError:
                log_llm_call(
                    logging.WARNING, session_id, "context_too_large", task=FEEDBACK_SCORE_TASK, latency_ms=0, attempts=0
                )
                step.finish(
                    output={"outcome": "context_too_large", "hint": hint_for("context_too_large")},
                    level="ERROR",
                    status_message="context_too_large",
                )
                return Scored(None, [], None, "context_too_large", 0, 0)
            attempts = self._attempts(
                session_id,
                FEEDBACK_SCORE_TASK,
                built,
                deadline,
                max_tokens=self.score_max_tokens,
                temperature=self.score_temperature,
                parse=lambda text: parse_score_reply(text, inputs.threads),
            )
            parsed = attempts.parsed
            assert parsed is None or isinstance(parsed, ScoreResult)
            scored = Scored(
                parsed,
                attempts.results,
                built.prompt_version,
                attempts.failure,
                sum(1 for reason in attempts.reasons if reason.startswith("quote_")),
                built.report.counts.get("truncated", 0),
            )
            output: dict[str, object] = {
                "outcome": "ok" if parsed is not None else attempts.failure,
                "prompt_version": built.prompt_version,
                "attempts": attempts.outcomes,
                "quotes_rejected": scored.quotes_rejected,
                "answers_truncated": scored.truncated,
                "estimated_input_tokens": built.report.estimated_tokens,
            }
            if parsed is not None:
                output["enough_evidence"] = parsed.enough_evidence
                output["scores"] = {f"q{q.main_number}": {c.value: v for c, v in q.scores.items()} for q in parsed.questions}
            else:
                output["hint"] = hint_for(attempts.failure)
            failed = parsed is None
            step.finish(output=output, level="ERROR" if failed else None, status_message=attempts.failure if failed else None)
            return scored

    def write(
        self, session_id: uuid.UUID, inputs: FeedbackWriteInputs, main_numbers: Sequence[int], deadline: Deadline
    ) -> WriteOutcome:
        """At most two attempts of the write call only. Failing is fine: the template writes the text instead."""
        with self.tracer.step(
            FEEDBACK_WRITE_STEP, metadata={"budget_left_ms": round(deadline.remaining() * 1000)}
        ) as step:
            built = self.context.build(FEEDBACK_WRITE_TASK, inputs)
            attempts = self._attempts(
                session_id,
                FEEDBACK_WRITE_TASK,
                built,
                deadline,
                max_tokens=self.write_max_tokens,
                temperature=None,
                parse=lambda text: parse_write_reply(text, main_numbers),
            )
            parsed = attempts.parsed
            assert parsed is None or isinstance(parsed, WriteText)
            source = TextSource.llm if parsed is not None else TextSource.template
            output = {
                "outcome": "ok" if parsed is not None else attempts.failure,
                "prompt_version": built.prompt_version,
                "attempts": attempts.outcomes,
                "text_source": source.value,
            }
            if parsed is None:
                output["hint"] = hint_for(attempts.failure)
            step.finish(
                output=output,
                level=None if parsed is not None else "WARNING",
                status_message=None if parsed is not None else f"template used ({attempts.failure})",
            )
            return WriteOutcome(parsed, attempts.results, built.prompt_version, attempts.failure)

    def _attempts(
        self,
        session_id: uuid.UUID,
        task: str,
        built: BuiltContext,
        deadline: Deadline,
        *,
        max_tokens: int,
        temperature: float | None,
        parse: Callable[[str], T],
    ) -> _Attempts:
        version = built.prompt_version
        check = FEEDBACK_CHECKS[task]
        results: list[LLMResult] = []
        reasons: list[str] = []
        outcomes: list[str] = []
        failure = "no_time"
        for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
            remaining = deadline.remaining()
            if remaining <= 0 or (attempt > 1 and remaining < MIN_SECONDS_FOR_RETRY):
                outcomes.append("retry_skipped:no_time" if attempt > 1 else "no_time")
                break
            budget_left_ms = round(remaining * 1000)
            try:
                result = self.llm.complete(
                    built.messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    budget_seconds=remaining,
                    trace_labels={
                        "task": task,
                        "prompt_version": version,
                        "attempt": attempt,
                        "budget_left_ms": budget_left_ms,
                    },
                )
            except LLMError as exc:
                # Already retried inside the provider where that makes sense (timeouts, 429, 5xx); the generation
                # itself is marked ERROR, so no check is needed.
                log_llm_error(session_id, exc, task, version, budget_left_ms)
                failure = type(exc).__name__
                outcomes.append(failure)
                break
            results.append(result)
            if not result.text.strip():
                log_result(logging.WARNING, session_id, "empty_reply", result, task, version, budget_left_ms)
                failure = "empty_reply"
                outcomes.append(failure)
                self.tracer.check(
                    check, passed=False, verdict=failure, metadata={"attempt": attempt}, hint=hint_for(failure)
                )
                break
            try:
                if result.finish_reason == "length":
                    # Cut off by max_tokens: never a complete reply, whatever it parses as.
                    raise InvalidReplyError("truncated")
                parsed = parse(result.text)
            except InvalidReplyError as exc:
                log_result(
                    logging.WARNING, session_id, f"invalid_reply:{exc.reason}", result, task, version, budget_left_ms
                )
                reasons.append(exc.reason)
                failure = f"invalid_reply:{exc.reason}"
                outcomes.append(failure)
                self.tracer.check(
                    check, passed=False, verdict=failure, metadata={"attempt": attempt}, hint=hint_for(failure)
                )
                continue
            log_result(logging.INFO, session_id, "ok", result, task, version, budget_left_ms)
            outcomes.append("ok")
            self.tracer.check(check, passed=True, verdict="ok", metadata={"attempt": attempt})
            return _Attempts(parsed, results, None, reasons, outcomes)
        return _Attempts(None, results, failure, reasons, outcomes)


def log_feedback_summary(
    session_id: uuid.UUID,
    *,
    outcome: str,
    overall: float | None = None,
    text_source: str | None = None,
    score: Sequence[LLMResult] = (),
    write: Sequence[LLMResult] = (),
    quotes_rejected: int = 0,
    truncated: int = 0,
    failure: str | None = None,
) -> None:
    """How one generation ended (generated, insufficient, failed) and what it cost. Metadata only, never text."""
    score_usage, write_usage = CallUsage.of(score), CallUsage.of(write)

    def tokens(usage: CallUsage) -> str:
        total = sum_known([usage.prompt_tokens, usage.completion_tokens])
        return "-" if total is None else str(total)

    llm_logger.info(
        "feedback_summary session=%s outcome=%s overall=%s text_source=%s score_retries=%s write_retries=%s "
        "score_tokens=%s write_tokens=%s score_ms=%s write_ms=%s quotes_rejected=%s truncated=%s failure=%s",
        session_id,
        outcome,
        "-" if overall is None else overall,
        text_source or "-",
        max(len(score) - 1, 0),
        max(len(write) - 1, 0),
        tokens(score_usage),
        tokens(write_usage),
        score_usage.latency_ms,
        write_usage.latency_ms,
        quotes_rejected,
        truncated,
        failure or "-",
    )
