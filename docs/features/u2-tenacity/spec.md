# Feature: U2 — One tenacity retry policy for the AI call layer

## Problem
The AI call layer retries failed network calls with hand-written code in four places:
- `openai_compatible.py`: `complete` (sync) and `stream` (async), two near-identical loops.
- `google_embedder.py`: `embed` (sync), a third copy of the loop with a hard-coded `MAX_RETRIES = 1`.
- `deepgram.py`: through `run_with_retries` in `core/ai/retry.py`.
- `retry.py` itself holds `backoff_seconds`, `retry_delay` and `run_with_retries`.

Separately, the four reply loops in `app/modules/interviews/ai/` (decide, write, write stream, feedback turn) each repeat the same attempt header: count to `MAX_REPLY_ATTEMPTS`, work out the time left, and skip a retry when less than `MIN_SECONDS_FOR_RETRY` remains.

The developer maintains the same rules in several places, and the logs don't say when a retry happened or why a call stopped retrying (attempts ran out, the turn's time ran out, or the error was not retryable).

## Goal
Centralize both kinds of retry, each in one place, and add the missing visibility:
- **Transport retries** (a 503, a timeout): one `RetryPolicy` object on tenacity, built by every vendor adapter, behaving as today except the wait, which becomes tenacity's built-in full jitter (same retryable errors, `Retry-After`, the turn's deadline, no retry after the first streamed chunk).
- **Content retries** (the model answered, but the answer was malformed): one shared attempt iterator for the four reply loops, behaving as today. It is not tenacity: the two kinds of retry stay separate layers.
- A log event for every retry wait and every give-up (with its reason), and a test that pins the worst-case number of HTTP calls one logical call can cause across both layers.

This is a learning slice (upgrade path U2): the policy it builds is the one U3 copies when LLM transport retries move to LangChain's `.with_retry()`.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project), `docs/ai-engineering-upgrade-path.md` (U2 section), U1 logging spec (`docs/features/u1-structlog/`).
- Constraints:
  - Transport retry code lives in `app/core/ai/`. The reply-attempt iterator lives in the interviews feature's `ai/` folder (it knows interview constants and the reply loops; `core` must not). Nothing else sees tenacity.
  - Feature file naming: files in the interviews module are prefixed `interviews_`; tests mirror the layer folders.
  - Vendor errors are mapped to the `LLMError` types before they leave `core/ai`; the policy only reads those types.
  - Logging goes through `app.core.logging` (`get_logger`), never structlog directly; events carry `request_id` and `session` automatically (U1).
  - Never log request/response payloads, prompts or user text; retry events carry attempt, wait, error class and task only.
  - No new dependency without saying why: `tenacity` is the one new dependency, and it is the subject of the slice. Settings come from `core/config.py` (no hard-coded retry counts).
  - Tests mock the LLM (deterministic, injected `clock`/`sleep`/`rng`); no real-model calls in unit tests.
  - CLAUDE.md: after a change in `core/ai` or a feature `ai/` folder, run the covering evals (same model, at least 2 repeats) and compare with `docs/evals/baselines.md` through Langfuse.
  - Never commit, stage or push; run `graphify update .` when code changes are done.

## User Flow
There is no end-user flow; the developer and the running app are the "users".
1. A service asks the LLM, the embedder or Deepgram for something.
2. The call fails with a retryable error (timeout, 429, 5xx, connection failure mapped to those).
3. The vendor's `RetryPolicy` waits (backoff plus jitter, at least `Retry-After`), logs the retry, and tries again, as long as attempts and the turn's time budget allow.
4. On success the result carries `attempts` and `latency_ms`; on final failure the raised error carries them, and one log event says why retrying stopped.
5. If the model's reply comes back malformed, the reply loop (decide, write, write stream, feedback) asks again through the shared attempt iterator, while attempts and time allow.

## Requirements

### Functional
- **`RetryPolicy` (transport):** one class in `app/core/ai/retry.py`, built on `tenacity`. It holds the vendor's `max_retries`, total budget, injected `clock`, `sleep` (sync) and `async_sleep`, plus a task label and a logger. It offers a sync call (used by `complete` and `embed`) and an async call (used by `stream` and Deepgram). Each adapter builds its own policy in its constructor from the arguments it already takes, so adapter constructors keep their `clock` and `sleep` arguments (the `rng` argument is no longer used and is removed; any test that passes it is updated). The three hand-written loops and `run_with_retries`, `backoff_seconds`, `retry_delay` are deleted.
- **What is retried:** `LLMTimeoutError`, `LLMRateLimitError`, `LLMServerError` (the errors whose `retryable` is true). Everything else (4xx rejections, bad responses, non-`LLMError` exceptions) is raised at once.
- **Wait:** tenacity's built-in `wait_random_exponential` with a multiplier of 0.5 (full jitter): a random wait from 0 up to `0.5 * 2^(attempt-1)` seconds. If the error carries `retry_after`, the wait is the larger of the two (a thin wrapper; the only custom wait rule). This replaces today's formula (0.5 s doubling plus up to 50% jitter), by the user's decision to use built-ins.
- **Stop:** after `max_retries` retries (so `max_retries + 1` attempts), or when the wait would not fit in the remaining budget (`elapsed + wait >= budget`). If `retry_after` alone exceeds the remaining budget, give up immediately without sleeping. Built from tenacity's `stop_after_attempt` and `stop_before_delay` where the first plan step shows they fit; otherwise a short custom stop on the adapter's clock.
- **Streaming:** only the step that opens the stream and reads the first chunk is retried. Once a chunk has been yielded, a failure is raised with `after_output=True` and never retried.
- **Stamping:** the final raised `LLMError` keeps `attempts` and `latency_ms`; a success keeps returning `attempts` and `latency_ms` as today. The per-attempt time limit stays `min(timeout, remaining budget)`.
- **Events:** two fixed names, so a later report can read them.
  - `retry_wait`, before each wait: `task`, `attempt`, `wait_seconds`, `error_class` (no payload);
  - `retry_giveup`, when the call fails for good: `task`, `attempts`, `elapsed_ms`, `error_class`, `reason` = `max_attempts` | `deadline` | `not_retryable`;
  - both are logged on the vendor's own logger (`app.llm`, `app.rag`, `app.stt`, `app.tts`) through U1 structlog, so they join the `llm_call` / `embedding_call` events by `request_id`;
  - they must not change what `interview_report` prints.
- **Per-call state:** the `RetryPolicy` holds only configuration. Each call creates its own tenacity object and its own per-attempt state, because one adapter (and so one policy) serves concurrent requests and `complete` runs in worker threads.
- **Embedder:** its retry count comes from settings (new field, default equal to today's value of 1) and is passed in through the factory like the other vendors' `max_retries`; the class argument defaults to 1 so its existing tests stay unchanged.
- **Reply attempts (content):** one iterator in `app/modules/interviews/ai/interviews_reply_attempts.py` replaces the attempt header repeated in the four reply loops: it counts up to `MAX_REPLY_ATTEMPTS`, hands each attempt its remaining time, and stops when no time is left or (after the first attempt) less than `MIN_SECONDS_FOR_RETRY` remains. It tells the caller whether it stopped for lack of time (the feedback turn records `no_time` / `retry_skipped:no_time`). Each loop keeps its own call, parse and logging body: they differ (the stream emits `Reset`s and logs cancellation, the feedback turn records tracer checks), so a callback-style helper would be harder to read than the loops.
- **Why reply attempts are not tenacity:** they are content retries (the model answered, but the answer was malformed or empty), not transport retries. They have no backoff, no `Retry-After` and no HTTP errors, they stop on an `LLMError` (the transport layer already retried it), and they are bounded by the turn's time. Putting them under tenacity would blur the line between the two layers. (Records the decision `u2-reply-loops`: not tenacity, but the shared attempt gate.)
- **One place that names the two layers:** the module docstring of `retry.py` states both layers and the worst-case call count, and points at the budget test.

### Non-Functional
- **Behaviour parity:** for the same inputs, the same sequence of attempts and errors as today; only the wait length changes (full jitter). The provider, Deepgram, embedder and reply-loop tests pass unchanged except three assertions on wait length (AC9); `test_retry.py` keeps every other assertion, re-pointed at `RetryPolicy`.
- **Worst-case call budget is explicit:** one logical LLM task = up to `(llm_max_retries + 1) × MAX_REPLY_ATTEMPTS` HTTP calls (today 3 × 2 = 6); embedder up to 2; Deepgram up to 2 per direction. A test pins these so a new layer can't silently multiply them.
- **No event-loop blocking:** the async call sleeps with `await`; the sync call is used only where the caller is already sync.
- **Privacy:** retry and give-up events carry no payload, prompt, response text or key; error text is the existing generic `LLMError` message.
- **Cost:** no extra calls compared with today; the eval comparison shows no score change beyond the noise margin.

## UX Requirements
Not applicable (no user interface). Error handling for end users is unchanged: the same `LLMError` types reach the same handlers.

## Constraints
- Python 3.14, `uv`; `tenacity` added as the only new dependency (standard, maintained, and what LangChain's `.with_retry()` is built on, so U3 reuses the concept).
- The adapters keep their injected `clock` and `sleep` (they give each attempt its remaining time and stamp latency). Tenacity uses its own clock and the global `random`; tests point its time at the same fake clock and seed `random` through one fixture. The `rng` argument is no longer used and is removed.
- Tenacity is not installed yet: its behaviour (stop checked before wait, injected sleep, cancellation, Python 3.14 support) is verified in the first plan step before anything is built on it; if a fact differs, the plan changes, not the behaviour.
- `interview_report` reads `logs/app.log`; the new events are additions it must ignore.
- The four reply loops must keep their externally visible behaviour: same prompts, same log lines, same `Written` / `Decision` / feedback outcomes.
- Windows dev machine; the user's `fastapi dev` server may be running and holding `logs/app.log` (don't rotate the real log in tests; use the temp test log).
- The ruff gate is `uv run --with ruff ruff check app tests`.

## Blockers
- None open. Decided with the user: built-in full jitter (`wait_random_exponential`) instead of today's formula, with tests pointing tenacity's time at the fake clock; include the embedder; include the visibility improvements; one `RetryPolicy` object per vendor (option A); a shared attempt iterator for the four reply loops (option C), not tenacity; port the `test_retry.py` assertions; run the evals.

## Edge Cases
Format: condition -> expected outcome. Vendor behaviour is marked as an assumption to verify.

- **EC1:** A stream fails after at least one chunk was yielded -> the error is raised with `after_output=True`, no retry, no retry event; the give-up event has reason `not_retryable` (a retry would duplicate output the caller may have shown).
- **EC2:** A stream fails before the first chunk with a retryable error -> retried like `complete`, and nothing was yielded to the caller.
- **EC3:** `Retry-After` is longer than the remaining budget -> give up at once, no sleep, give-up reason `deadline`, the last error is raised with its attempts stamped.
- **EC4:** `Retry-After` is shorter than the computed backoff -> the backoff wins (the vendor's value is a minimum, never a shortening).
- **EC5:** `max_retries = 0` -> exactly one attempt; a retryable failure is raised with reason `max_attempts`, no retry event.
- **EC6:** The next wait would end at or after the budget (`elapsed + wait >= budget`) -> no new attempt starts, reason `deadline`.
- **EC7:** The turn's remaining budget is already almost over when the call starts -> the first attempt still runs with a timeout of `min(timeout, remaining)`; a failure gives up at once with reason `deadline` and no new attempt starts.
- **EC8:** A non-retryable `LLMError` (4xx rejection, bad response) -> raised at once with `attempts=1` and `latency_ms` stamped; give-up reason `not_retryable`; no retry event.
- **EC9:** An exception that is not an `LLMError` (a bug) -> propagates unchanged, not retried, not stamped.
- **EC10:** The caller cancels during an async wait (client disconnects the SSE stream) -> the cancellation propagates at once, no further attempt, no give-up event claiming a retry outcome.
- **EC11:** Error text or `Retry-After` header is garbled -> `parse_retry_after` already treats it as "not said"; the normal backoff applies (unchanged).
- **EC12:** The retry events must not contain request bodies, prompts, answers, resumes or response text -> only attempt, wait, error class, task, ids.
- **EC13:** The embedder's new setting is negative -> rejected by config validation (`ge=0`), like the other `*_max_retries` settings.
- **EC14:** A reply loop gets an `LLMError` from the transport layer -> it stops and does not re-ask (unchanged), so transport and content retries never multiply on the same failure.
- **EC15:** Both layers fully used (transport retries inside each of the reply-loop attempts) -> total HTTP calls never exceed `(max_retries + 1) × MAX_REPLY_ATTEMPTS`.
- **EC16:** A reply loop's first attempt gave a malformed reply and less than `MIN_SECONDS_FOR_RETRY` remains -> no second attempt starts; the iterator reports that it stopped for lack of time (the feedback turn records `retry_skipped:no_time`).
- **EC17:** No time is left before the first reply attempt (remaining is zero or negative) -> no attempt starts; the feedback turn records `no_time`. (The write and write-stream loops today only check this from the second attempt; the turn plan already refuses to start a write with too little time, so the shared gate is the same in practice. If an existing test shows a difference, that loop keeps today's rule.)
- **EC18:** The write-stream client disconnects mid-attempt -> cancellation propagates and is logged as `cancelled` exactly as today; the iterator does not swallow it.
- **EC19:** Two requests use the same adapter at the same time, both retrying -> each keeps its own attempt count, waits and stamps; neither affects the other.
- **EC20:** The log contains `retry_wait` / `retry_giveup` lines (and old logs contain none) -> `interview_report` prints the same report as without them.
- **EC21:** Full jitter draws a near-zero wait for a 429 with no `Retry-After` -> the retry still happens after that short wait; the retry count bounds the extra calls; when `Retry-After` is sent it is always the minimum.

## Acceptance Criteria
- [ ] **AC1:** `tenacity` is a declared dependency, and no hand-written retry loop remains in `openai_compatible.py`, `google_embedder.py` or `deepgram.py`; `run_with_retries`, `backoff_seconds` and `retry_delay` no longer exist in `app/core/ai/`.
- [ ] **AC2:** `complete`, `stream`, `embed` and the Deepgram calls all retry through a `RetryPolicy` that their adapter builds from its existing constructor arguments, and only `LLMTimeoutError`, `LLMRateLimitError` and `LLMServerError` are retried (EC8, EC9).
- [ ] **AC3:** With `random` seeded, every wait lies between 0 and `0.5 * 2^(attempt-1)` seconds, and a `retry_after` larger than that wait is used instead (EC4, EC21).
- [ ] **AC4:** With an almost-over budget, or a wait that would pass the budget, no new attempt starts (a test counts attempts), including when `Retry-After` alone exceeds the remaining budget (EC3, EC6, EC7).
- [ ] **AC5:** A stream failure after the first chunk is raised with `after_output=True` and is not retried; a failure before the first chunk is retried (EC1, EC2).
- [ ] **AC6:** The raised error carries `attempts` and `latency_ms`, and a success still returns them, for all four transport callers (existing assertions unchanged).
- [ ] **AC7:** A retry event is logged before each wait (attempt, wait seconds, error class), and a give-up event is logged when a call fails for good, with `reason` one of `max_attempts`, `deadline`, `not_retryable`; both carry the request id and contain no payload (EC5, EC12).
- [ ] **AC8:** The embedder's retry count is a setting (default 1, validated `ge=0`) passed through the factory; `MAX_RETRIES` is gone from `google_embedder.py` (EC13).
- [ ] **AC9:** `test_retry.py` keeps every existing assertion (a bound check instead of the old backoff range, `Retry-After` minimum, budget give-up, max retries, attempts/latency stamping, no attempt past the budget), re-pointed at `RetryPolicy`; the `test_openai_compatible*.py`, `test_deepgram.py`, embedder and reply-loop tests pass unchanged, except the assertions on wait length: two in `test_openai_compatible.py` (the 0.5-0.75 s range and the "second wait longer than the first" check) and one in `test_deepgram.py` (the 0.5-0.75 s range), which become bound checks. (Found while building: five more existing budget tests depended on the old 0.5 s minimum wait: `test_deepgram.py::test_does_not_start_a_retry_past_the_budget`, `test_google_embedder.py::test_no_retry_starts_past_the_budget` and three in `test_openai_compatible.py`. Under full jitter the number of waits that fit a budget is random, so each now sends a fixed `Retry-After` and keeps its assertions; see task.md, Deviations.)
- [ ] **AC10:** A test pins the worst-case HTTP calls across layers: `(llm_max_retries + 1) × MAX_REPLY_ATTEMPTS` for an LLM task, and the per-vendor maximum for the embedder and Deepgram (EC14, EC15); it fails if a layer is added or a limit changes.
- [ ] **AC11:** The four reply loops (decide, write, write stream, feedback turn) take their attempt header (count, time left, minimum time for a retry) from the shared iterator and contain no tenacity; each loop's own call, parse and logging body is unchanged; the reasoning is recorded in the task's learnings.
- [ ] **AC12:** The full suite passes (`uv run pytest`), `uv run --with ruff ruff check app tests` is clean, and the evals that cover the four reply loops (same model, at least 2 repeats) compared with `docs/evals/baselines.md` through Langfuse show no drop beyond the noise margin. A healthy provider never retries, so the evals do not exercise the transport retries; a real fault check does: one interview with a very low `LLM_TIMEOUT_SECONDS` shows `retry_wait` and `retry_giveup` lines in the log, and `interview_report --last 1` still reports normally.
- [ ] **AC14:** Two concurrent calls on one `RetryPolicy` keep separate attempt counts and waits (a test runs them together) (EC19).
- [ ] **AC15:** The report's golden-file test gives the same output with `retry_wait` / `retry_giveup` lines in the log (EC20).
- [ ] **AC13:** The shared attempt iterator has its own tests: it stops at `MAX_REPLY_ATTEMPTS`, gives each attempt the time left, stops when the time left is below `MIN_SECONDS_FOR_RETRY` after the first attempt, reports that it stopped for lack of time, and does not swallow cancellation (EC16, EC17, EC18).

## Out of Scope
- **Circuit breaker / provider fallback chain:** belongs to U3.
- **Retrying 4xx or bad-response errors:** they are deterministic, so a retry only burns cost.
- **Tenacity inside the reply loops:** content retries are a different concern.
- **Merging the four loops' bodies into one callback helper:** the call, parse and log steps differ (stream `Reset`s and cancellation logging, feedback tracer checks); only the attempt header is shared.
- **Keeping today's exact wait formula:** replaced by tenacity's built-in full jitter, by the user's decision; the three wait-length assertions change.
- **A retries section in `interview_report`** (retries per call, give-up reasons; fits the cost / effectiveness / efficiency metrics goal): a separate slice. U2 only keeps the event names stable so it can be built later.
- **A shared settings group for retries:** each vendor keeps its own `*_max_retries` and budget, because the limits genuinely differ.
- **The R3 cleanup of unused `session_id`/`user` parameters** from U1: separate follow-up.
- **LangChain `.with_retry()` and SDK `max_retries`:** U3.
