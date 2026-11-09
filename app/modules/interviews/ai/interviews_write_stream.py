"""The streamed write step (interviewer_v5): the question is shown as it is written, and a failed draft is taken back."""

import logging
import uuid
from collections.abc import AsyncGenerator, Callable, Mapping, Sequence
from contextlib import aclosing

from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import (
    ChatMessage,
    LLMError,
    LLMProvider,
    LLMResult,
    LLMTimeoutError,
)

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_reply import InvalidReplyError, parse_streamed_reply, split_header
from ..ai.interviews_turn_limits import Deadline
from ..ai.interviews_turn_log import log_llm_call, log_llm_error, log_result
from ..ai.interviews_turn_types import Delta, Draft, Reset, Written
from ..constants.interviews_constants import (
    INTERVIEWER_STREAM_TASK,
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
    QuestionCategory,
)


async def stream_write(
    llm: LLMProvider,
    context: ContextManager,
    session_id: uuid.UUID,
    inputs: InterviewerInputs,
    deadline: Deadline,
    *,
    follow_up_category: QuestionCategory | None,
    max_tokens: int,
    clock: Callable[[], float],
) -> AsyncGenerator[Delta | Reset | Written]:
    """`write` for interviewer_v5, streamed: question text as Deltas, then the Written (last). The same attempts
    and checks; but a draft was already shown, so one that fails is taken back (Reset) before the retry, and a
    provider failure after some text is retried too (the provider couldn't: it had already sent text).
    """
    try:
        built = context.build(INTERVIEWER_STREAM_TASK, inputs)
    except ContextTooLargeError:
        log_llm_call(
            logging.WARNING, session_id, "context_too_large", task=INTERVIEWER_STREAM_TASK, latency_ms=0, attempts=0
        )
        yield Written(None, [], None)
        return
    version = built.prompt_version
    earlier = [turn.question for turn in inputs.turns]
    results: list[LLMResult] = []
    for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
        remaining = deadline.remaining()
        if attempt > 1 and remaining < MIN_SECONDS_FOR_RETRY:
            break
        budget_left_ms = round(remaining * 1000)
        shown = False
        attempt_start = clock()
        finished: Draft | None = None
        try:
            labels = {"task": INTERVIEWER_STREAM_TASK, "prompt_version": version, "budget_left_ms": budget_left_ms}
            draft = stream_draft(
                llm, built.messages, remaining, deadline, follow_up_category, labels, max_tokens=max_tokens
            )
            async with aclosing(draft) as chunks:
                async for item in chunks:
                    if isinstance(item, Draft):
                        finished = item
                    else:
                        shown = True
                        yield Delta(item)
        except LLMError as exc:
            log_llm_error(session_id, exc, INTERVIEWER_STREAM_TASK, version, budget_left_ms)
            if shown:
                yield Reset()
            if exc.after_output:
                continue
            # Before any text, the provider already retried what was worth retrying.
            break
        except InvalidReplyError as exc:
            # A missing or broken CATEGORY line: nothing of it was shown.
            log_llm_call(
                logging.WARNING,
                session_id,
                f"invalid_reply:{exc.reason}",
                task=INTERVIEWER_STREAM_TASK,
                prompt_version=version,
                latency_ms=0,
                attempts=1,
                budget_left_ms=budget_left_ms,
            )
            continue
        except BaseException as exc:
            if isinstance(exc, Exception):
                raise
            # The client left mid-call (closed or cancelled): the call stops, so no more tokens are generated. Its
            # usage is unknown (it comes at the end of a stream), so the line records that it was cut off.
            log_llm_call(
                logging.INFO,
                session_id,
                "cancelled",
                task=INTERVIEWER_STREAM_TASK,
                prompt_version=version,
                latency_ms=round((clock() - attempt_start) * 1000),
                attempts=attempt,
                budget_left_ms=budget_left_ms,
            )
            raise
        # `stream_draft` ends with its Draft unless it raised, and every raise above leaves the attempt.
        assert finished is not None
        result = finished.result
        results.append(result)
        try:
            reply = parse_streamed_reply(
                finished.text,
                interview_type=inputs.interview_type,
                earlier_questions=earlier,
                category=finished.category,
            )
        except InvalidReplyError as exc:
            log_result(
                logging.WARNING,
                session_id,
                f"invalid_reply:{exc.reason}",
                result,
                INTERVIEWER_STREAM_TASK,
                version,
                budget_left_ms,
            )
            if shown:
                yield Reset()
            continue
        log_result(logging.INFO, session_id, "ok", result, INTERVIEWER_STREAM_TASK, version, budget_left_ms)
        yield Written(reply, results, version)
        return
    yield Written(None, results, version)


async def stream_draft(
    llm: LLMProvider,
    messages: Sequence[ChatMessage],
    remaining: float,
    deadline: Deadline,
    follow_up_category: QuestionCategory | None,
    trace_labels: Mapping[str, str | int | None],
    *,
    max_tokens: int,
) -> AsyncGenerator[str | Draft]:
    """One streamed attempt: the question's text chunks (never the CATEGORY line), then the finished Draft.
    Raises InvalidReplyError for a bad CATEGORY line before any text, and LLMTimeoutError when the turn's deadline
    runs out mid-stream."""
    buffer, category, text = "", follow_up_category, ""
    result: LLMResult | None = None
    stream = llm.stream(
        messages, max_tokens=max_tokens, budget_seconds=remaining, trace_labels=trace_labels
    )
    async with aclosing(stream) as items:
        async for item in items:
            if isinstance(item, LLMResult):
                result = item
                continue
            if category is None:
                buffer += item
                split = split_header(buffer)
                if split is None:
                    continue
                category, item = split.category, split.text
            if item:
                text += item
                yield item
            if deadline.remaining() <= 0:
                exc = LLMTimeoutError("the turn's time ran out mid-question")
                exc.after_output = bool(text)
                raise exc
    if category is None:
        # The reply ended inside its first line.
        split = split_header(buffer, final=True)
        assert split is not None
        category, text = split.category, split.text
    assert result is not None
    yield Draft(category, text, result)
