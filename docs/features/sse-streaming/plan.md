# Implementation Plan: SSE Streaming of the Interview Turn (Slice 4)

## Overview
A new `POST /interviews/{id}/messages/stream` sends one answer turn as Server-Sent Events over `sse-starlette`.
- Phase A sends progress events and the saved turn.
- Phase B adds an async provider `stream()` and `interviewer_v5`, so the next question types out word by word.

The turn rules and the atomic save are the same code the JSON endpoint uses.

## Architecture & Design
- **Shared turn logic.** `Interviewer.answer_turn` (sync) is split into shared pieces:
  - `_decide`, which already exists;
  - `plan_write`: applies the limits and builds the write inputs;
  - `settle`: applies the fallback, sums the usage and writes the summary log.

  A new async generator, `Interviewer.stream_turn`, uses the same pieces and yields typed turn events. The decide call runs in a worker thread. The write call runs in a thread in Phase A and as an async provider stream in Phase B.
- **Controller split.** `answer()` becomes three methods:
  - `prepare_answer`: checks, a plain-value read and `release()`; it raises normal `AppError`s;
  - `finish_answer`: the reaction, `record_turn` and `AnswerOut`;
  - `stream_answer`: an async generator wrapping `stream_turn`. It maps turn events to SSE events and calls `finish_answer` in a thread.
- **Thin route.** The route is `async def`. It runs `prepare_answer` in the threadpool, so 401, 403, 404, 409 and 422 stay JSON. Then it returns `EventSourceResponse`.
- **Provider.**
  - `OpenRouterProvider` is renamed to a vendor-neutral `OpenAICompatibleProvider`. It already talks to Google AI Studio's OpenAI-compatible endpoint.
  - It gains `stream()` on an `httpx.AsyncClient`.
  - The contract says a provider may retry, or later switch to a fallback provider, **only before the first chunk**. That is the seam for the planned fallback chain.

## Spec Requirements -> Implementation
- Rename to a vendor-neutral provider and config (user note, post-spec) → Step 0
- New dependency, endpoint, pre-stream JSON errors, headers, heartbeat (AC1, AC2, EC1–EC4, EC19) → Steps 1, 7
- Event contract and terminal rule (AC3, AC8, AC21) → Steps 2, 6, 7
- Same outcomes and rows as the JSON endpoint, one atomic save (AC4, AC5, AC9, EC12–EC16) → Steps 3, 4, 5, 6
- Disconnect: nothing saved, usage logged (AC6, AC15, EC6) → Steps 6, 13
- Concurrent submits, `record_turn` failure, unexpected errors (AC7, AC8, EC5, EC17, EC18) → Step 6
- Per-turn timings and terminal logging (AC10, AC17) → Steps 6, 13
- Async provider `stream()` and the before-first-chunk retry rule (AC11) → Steps 9, 10, 11
- `interviewer_v5`, header line, checks, the category kept out of deltas (AC12, AC13, EC11) → Step 12
- Reset → retry → bank on an invalid draft, a provider failure or the deadline (AC14, EC7–EC10) → Step 13
- The event loop stays free (AC16) → Steps 5, 7, 14
- v4 vs v5 evals, live time to first token, learnings, progress line (AC18–AC20) → Steps 15, 16

## Implementation Steps

### Step 0: Rename the provider to a vendor-neutral name
- Move `app/core/ai/openrouter.py` → `openai_compatible.py`, and rename the class `OpenAICompatibleProvider`. The module docstring and comments say "OpenAI-compatible chat completions (Google AI Studio, OpenRouter, Groq …)".
- **Config by vendor, with the order set separately**, so later fallbacks never rename keys:
  - `LLM_PROVIDERS`: a comma-separated, ordered list (primary first). Empty means the LLM is off and the bank is used, as today.
  - One typed block per supported vendor: `LLM_GOOGLE_API_KEY` (secret), `LLM_GOOGLE_MODEL` and `LLM_GOOGLE_BASE_URL`. Only `google` exists in this slice. Adding a vendor later means adding its three fields.
  - The limits stay global and unchanged (`LLM_TIMEOUT_SECONDS`, `LLM_MAX_RETRIES`, `LLM_TOTAL_BUDGET_SECONDS`, `LLM_MAX_TOKENS`).
  - `Settings` exposes the listed providers as a list of plain provider configs (name, key, model, base URL), in order.
- **Validation at startup:**
  - an unknown name in `LLM_PROVIDERS` is an error;
  - a listed provider with a missing key, model or base URL is an error;
  - duplicate names are an error.

  The messages name the missing variable, never its value.
- **Clean break.** `OPENROUTER_API_KEY`, `LLM_MODEL` and `LLM_BASE_URL` are removed, with no aliases. If `OPENROUTER_API_KEY` is still set, startup fails with a message pointing to the new names, so a stale `.env` can't silently turn the LLM off.
- **The factory builds only the first listed provider** (minimal). The fallback chain over the rest is the later multi-provider work; the factory's docstring says so. `llm_configured` and the "LLM disabled" warning follow the new names.
- **Docs and tests.**
  - `.env.example` documents the new shape, with Google AI Studio filled in and a commented example of a second vendor block plus the order line.
  - Your local `.env` must be migrated by hand: `LLM_PROVIDERS=google`, then the three `LLM_GOOGLE_*` values from today's key, model and URL. This goes in the summary.
  - The tests `tests/core/ai/test_openrouter.py` and `tests/live/test_openrouter_live.py` are renamed to match. `test_factory.py`, `test_config.py` and any test or script that sets the old variables are updated. The eval runner's `--model` override applies to the first provider.
- **Test: first.** Seam: `Settings` and `build_provider` (user-confirmed via the config discussion). Slices:
  1. Empty `LLM_PROVIDERS` → the LLM is off and the factory returns `None`.
  2. `google` complete → one config, and the factory builds an `OpenAICompatibleProvider` with its key, model and URL.
  3. A listed provider missing its key, model or URL → an error naming the variable.
  4. An unknown provider name → an error.
  5. A duplicate name → an error.
  6. A leftover `OPENROUTER_API_KEY` → an error that points to the new names.
  7. No secret value appears in any error message.

  The existing provider tests pass unchanged in behaviour.

### Phase A: plumbing and progress events

### Step 1: Add the dependency
- `uv add sse-starlette` (3.6.0 resolves).
- The reason goes in the PR description: the route returns the stream explicitly, so the checks fail before any byte is sent; disconnects are explicit; the ping interval can be configured.
- A named constant for the ping interval (15 s) in `interviews_constants.py`.
- **Test: skip** (config).

### Step 2: Event contract
- **Constants:** `TurnPhase` (`received`, `deciding`, `writing`) and the event names (`status`, `reaction`, `question.delta`, `reset`, `done`, `error`).
- **Schema:** one Pydantic model per event payload (`extra="forbid"`). `done` reuses `AnswerOut`; `error` reuses the `ErrorBody` fields (`code`, `message`, `request_id`).
- **Utils:** a pure helper that turns an event into the dict `sse-starlette` sends (`event` plus the JSON `data`).
- The contract is documented on the route's OpenAPI `responses` (200 `text/event-stream` with the event list, order and terminal rule) for the Next.js side. No extra doc file.
- **Test: after**, through the endpoint seam in Steps 6–7 (AC21 checked by reading the OpenAPI output).

### Step 3: Extract the shared turn pieces in `interviews_turn.py`
- `plan_write` (`apply_limits`, the time check, the write inputs and the follow-up category) and `settle` (the fallback-to-move-on rule, the source, the summary log and the `TurnOutcome`) are taken out of `answer_turn`. `answer_turn` becomes `_decide` → `plan_write` → `_write` → `settle`, with the same behaviour.
- **Test: after.** It is a pure refactor, guarded by the unchanged `test_follow_ups.py`, `test_turn_budget.py`, `test_answer_llm.py` and `test_answer_guards.py`.

### Step 4: Split the controller
- `prepare_answer` returns a frozen `TurnContext`:
  - the setup, history and thread;
  - `last_main` and the used bank ids;
  - the stored next question and the previous reaction;
  - the pending answer message.

  It holds the same checks and the read-then-`release()` order as today.
- `finish_answer(ctx, outcome)` picks the reaction, builds the new question (`_llm_question`, bank), calls `record_turn`, raises `QuestionNotCurrentError` when it loses the race, and returns `AnswerOut`.
- `answer()` = `prepare_answer` → `answer_turn` → `finish_answer`.
- A small `reaction_is_certain(action)` rule says the reaction is known once the action is move on or complete and no follow-up is pending.
- **Test: after.** The JSON endpoint suite runs unchanged.

### Step 5: `Interviewer.stream_turn` (async generator)
- It yields typed turn events:
  - `Phase(deciding)`;
  - `ActionKnown(action)`, as soon as `plan_write` fixes the action;
  - `Phase(writing)`;
  - in Phase B, `Delta` and `Reset`;
  - a final `Outcome(TurnOutcome)`.
- `_decide` and (in Phase A) `_write` run with `anyio.to_thread.run_sync` against the shared `Deadline`. The JSON path's injectable clock is reused.
- **Test: first.** Seam: `Interviewer.stream_turn` (user-confirmed). Slices:
  1. A move-on turn yields deciding → action → writing → outcome.
  2. A follow-up turn's action is reported only after its write succeeds (EC13).
  3. A follow-up write failure turns into move on (EC14).
  4. The last thread completes with no writing (EC15).
  5. The decide call failing falls back to `next_question` (EC12).
  6. The outcome equals `answer_turn`'s for the same script (AC4).

### Step 6: `InterviewsController.stream_answer` (async generator)
- It yields `status: received` at once, then maps turn events:
  - `ActionKnown` → a `reaction` event when the reaction is certain;
  - phases → `status`.
- Then `finish_answer` runs in a thread, and `done` is sent.
- Sessions without an LLM, and pre-stored sessions, skip `stream_turn`: `received` → `reaction` → `done` (EC16).
- Error handling:
  - `QuestionNotCurrentError` from `finish_answer` → an `error` event with that code (EC5, EC18).
  - Any other exception → `INTERNAL_ERROR` with a generic message and the `request_id` from the logging context; the details are logged only (EC17).
  - Cancellation (a disconnect) logs `cancelled` and is re-raised. Nothing is saved because `finish_answer` never ran (EC6).
- One `stream_turn_summary` log line per turn, with no text:
  - the time to first event and the time to first token;
  - the total time and the number of resets;
  - whether it was cancelled, and the terminal event.
- **Test: first.** Seam: the stream endpoint via `TestClient.stream` (user-confirmed). Slices:
  1. Event order and exactly one terminal event (AC3).
  2. `done` validates as `AnswerOut` and equals the JSON endpoint's body for the same script (AC4).
  3. The saved rows equal the JSON path's (AC5).
  4. The reaction and writing rules (AC9, EC13–EC16).
  5. A lost race → `error QUESTION_NOT_CURRENT`, with one saved turn (AC7, EC5). Simulated by saving the turn through the JSON endpoint inside the fake's `on_call` hook, mid-stream.
  6. `record_turn` raising and an unexpected crash → one `error`, with no exception, LLM or answer text (AC8, EC17, EC18).
  7. The time to first event is under 1 s and logged (AC10).
  8. The summary log carries no text (AC17).

### Step 7: Route
- An `async def` handler on `POST /{session_id}/messages/stream`, with the same `AnswerIn`, `require_permissions(Permission.interviews_answer)` and controller dependency.
- It awaits `run_in_threadpool(ctrl.prepare_answer, …)`, so EC1–EC4 come back as JSON through the existing exception handlers.
- It returns `EventSourceResponse` over `stream_answer` mapped by the Step 2 helper, with the ping constant and `Cache-Control: no-cache` / `X-Accel-Buffering: no` (sse-starlette sets most of these; the plan checks which).
- `responses=` documents 404, 409 and the 200 event stream.
- **Test: first.** Seam: the stream endpoint (user-confirmed). Slices:
  1. The content type and headers on success (AC1).
  2. 401, 403, 404 (not owned and unknown, the same body), 409 not in progress, 409 not current, and 422 return JSON with no stream body (AC2, EC1–EC4).
  3. `POST /messages` is unchanged (AC1).
  4. A heartbeat comment appears during a slow fake wait. Uses a short ping override and must not create a data event (EC19).

### Step 8: Streaming test helpers in `tests/modules/interviews/conftest.py`
- A `stream_answer` fixture that posts with `client.stream`, parses SSE frames into `(event, data)` pairs, and returns them with the status code. An `anyio_backend` fixture set to `asyncio` (anyio's pytest plugin ships with anyio; no new dependency).
- **Test: skip** (test infrastructure). It is verified by Steps 6–7.

### Phase B: streaming the question text

### Step 9: The provider contract in `app/core/ai/provider.py`
- `LLMProvider` gains:
  - `stream(messages, *, max_tokens, temperature, budget_seconds, reasoning_effort)`, an async iterator of text chunks that finishes with a final `LLMResult` (the joined text and usage, the same fields as `complete()`);
  - `aclose()`.
- The docstring states the rule: retries (and a future fallback chain) may only happen before the first chunk. After a chunk, a failure raises an `LLMError` flagged `after_output` with the partial usage, and the caller decides what to do.
- The lifespan in `main.py` calls `aclose()` on shutdown.
- **Test: skip** (a contract). It is exercised by Steps 10, 11 and 13.

### Step 10: `OpenAICompatibleProvider.stream`
- An `httpx.AsyncClient` request with `stream: true` and `stream_options.include_usage`. It parses `data:` lines, handles `[DONE]`, maps error chunks and statuses to the existing `LLMError` types, and keeps the per-call timeout and total budget (`anyio.fail_after`).
- It retries with backoff via `anyio.sleep` only before the first chunk. Cancellation closes the HTTP stream.
- **Test: first.** Seam: `OpenAICompatibleProvider.stream` with an async `httpx.MockTransport` (user-confirmed). Slices:
  1. Chunks are yielded in order, and the final result joins them with usage.
  2. No usage chunk gives `None` usage, never a guess.
  3. A 429 or 5xx before the first chunk is retried.
  4. A failure after the first chunk is not retried and is flagged as after-output.
  5. An error chunk mid-stream.
  6. A timeout within the budget.
  7. Blank output → `LLMBadResponseError`.

### Step 11: `FakeProvider.stream`
- Scripted chunk lists, a scripted mid-stream `LLMError`, per-chunk delays (`anyio.sleep`), and a `cancelled` flag set when the iterator is closed early.
- The `llm` fixture's router sends `stream` calls to the write fake.
- **Test: skip** (test double). It is exercised by Step 13.

### Step 12: `interviewer_v5` and the streamed-reply parser
- **The prompt.** `prompts/interviewer_v5.md` has the six parts, the same placeholders and the same data-not-instructions line as v4. Its Output section says:
  - next-question mode: a first line `CATEGORY: <value>`, then the question text;
  - follow-up mode: the question text only;
  - no JSON and no fence.
- **The task.** A constant for v5 and an `interviewer_stream` task registered in `build_context_manager` with a `window_ledger` on v5. The JSON task stays on v4.
- **The parser.** In `interviews_reply.py`:
  - the existing question checks (one question mark, category for non-mixed, repeat) are moved into a shared private check used by both parsers;
  - `split_header` is a pure, incremental function: given the chunks so far, it returns the category once the first newline arrives (or "invalid header" when it doesn't match), with the rest as text;
  - `parse_streamed_reply(header, text, …)` returns the same `InterviewerReply`.
- **Test: first.** Seam: `split_header` and `parse_streamed_reply` (user-confirmed). Slices:
  1. A header split across chunks.
  2. A missing header or an unknown category → invalid (EC11).
  3. Follow-up mode has no header.
  4. Two question marks, wrong category, repeat → the same reason codes as v4.
  5. `parse_interviewer_reply` behaviour is unchanged.
- The prompt structure uses the six-heading check in `test_context_prompts.py`; v1–v4 are checked byte-for-byte unchanged against git (AC12).

### Step 13: The streamed write step in `stream_turn`
- In Phase B `_write` is replaced on the stream path by an async streamed write over `interviewer_stream`:
  - It buffers until the header is read (next-question mode), then yields `Delta`s, so the category is never sent.
  - It parses on completion.
  - An invalid reply, an after-output `LLMError` or the deadline running out (`anyio.fail_after(deadline.remaining())`) yields `Reset` only if a delta was sent. It retries when `MIN_SECONDS_FOR_RETRY` is left; otherwise it hands the bank signal to `settle`.
  - It records the time to first token from the write start, and the number of resets.
- Cancellation propagates into `provider.stream`, and the partial usage is logged with outcome `cancelled`.
- **Test: first.** Seam: `Interviewer.stream_turn` (user-confirmed), plus the endpoint for the end-to-end slices. Slices:
  1. A multi-chunk reply → two or more deltas whose joined text equals the saved question, with no category text (AC13).
  2. An invalid draft with time left → reset, then the retry streams (EC7).
  3. With no time → reset, then the bank (EC8).
  4. A mid-stream error or the deadline → reset, then retry or bank, and the turn saved (EC9).
  5. An error before any text → no reset (EC10).
  6. A bad header → no deltas for that attempt (EC11).
  7. `aclose()` during writing → the fake records the cancellation, nothing is saved, and the usage is logged cancelled (AC15, AC6).
  8. The summary includes the time to first token and resets (AC17).

### Step 14: The event loop stays free
- A test with `httpx.AsyncClient` plus `ASGITransport`: a stream request against a fake with a slow chunk, and a concurrent `GET /health` that finishes first.
- **Test: first.** Seam: the stream endpoint (user-confirmed) (AC16).

### Step 15: Evals
- `interviews_evals.py` gets a v5 write mode (`--prompt v5`) that runs the cases through `stream()` and `parse_streamed_reply`. It reports the same valid-reply and injection results as v4, plus the time to first token per call.
- The default runs stay unchanged.
- **Test: first** for the check and summary functions with the fake (seam: the runner's public functions in `test_evals.py`). **After** for the real-model runs (opt-in, never in pytest).

### Step 16: Measure, document, finish
- Run the v4 vs v5 evals with 3 repeats on `gemini-3.5-flash-lite` (pause between runs; the free tier rate limits).
- Do one live interview through the stream endpoint and read the time to first token, and the time to first event, from the logs.
- Write `docs/features/sse-streaming/learnings.md` (Predict / Observed / Why / Proof, including concept 7's Proof). Tick the Slice 4 progress line.
- Run `uv run ruff check . && uv run ruff format .`, `uv run pytest`, then `graphify update .`.
- **Test: after** (AC18–AC20).

## Affected Files & Patterns
- **`app/core/ai/`:**
  - `openrouter.py` → `openai_compatible.py`: rename, plus `stream`, `aclose`.
  - `provider.py`: `stream`, `aclose`, the after-output flag.
  - `fake.py`: `stream`.
  - `factory.py`: the new names.
- **Config and app:** `app/core/config.py` (`LLM_PROVIDERS`, the `LLM_GOOGLE_*` block, the provider config list, the validation, and the error for the old variables), `app/main.py` (lifespan `aclose`), `.env.example`, `pyproject.toml` / `uv.lock` (`sse-starlette`).
- **`app/modules/interviews/`:**
  - `interviews_turn.py`: `plan_write`, `settle`, `stream_turn`, the streamed write, the summary log;
  - `interviews_controller.py`: `prepare_answer`, `finish_answer`, `stream_answer`;
  - `interviews_route.py`: the stream route;
  - `interviews_schema.py`: the event models;
  - `interviews_constants.py`: phases, event names, ping, v5 and the stream task;
  - `interviews_context.py`: the `interviewer_stream` task;
  - `interviews_reply.py`: the shared checks, `split_header`, `parse_streamed_reply`;
  - `interviews_utils.py`: the SSE event helper;
  - `interviews_evals.py`;
  - `prompts/interviewer_v5.md` (new).
- **Tests:**
  - new: `test_answer_stream.py` (endpoint), `test_stream_turn.py`, `test_streamed_reply.py`, `test_openai_compatible_stream.py`;
  - renamed: `test_openai_compatible.py`, `tests/live/test_openai_compatible_live.py`;
  - extended: `conftest.py`, `test_context_prompts.py`, `test_evals.py`, `test_config.py`, `test_factory.py`.
- **Docs:** `docs/features/sse-streaming/learnings.md` (new), the learning-path progress line.
- **Patterns to follow:**
  - the compare-and-swap in `record_turn`;
  - read-then-`release()` before LLM calls;
  - the strict parser and reason codes in `interviews_reply.py`;
  - the context `Task` registration in `interviews_context.py`;
  - the scripted `FakeProvider` with an injectable clock;
  - the `MockTransport` tests in `test_openrouter.py`;
  - the pure ASGI middleware, which already doesn't buffer streams.
- **Risks:**
  - The Step 3–4 refactor touches the busiest code. It lands with the full suite green before any streaming code.
  - The sync SQLAlchemy `Session` is used from threadpool threads one after another, never at the same time.
  - The `get_db` session lives until the response ends. That's harmless, because `release()` ends the transaction, but it needs checking.
  - The `reasoning` body field is OpenRouter's syntax. Google's endpoint may ignore it or reject it. It is unchanged here, and it's noted for the multi-provider work.

## Testing Strategy
- **Framework and commands:**
  - pytest with `TestClient`, plus anyio's pytest plugin for async seams;
  - `uv run pytest tests/modules/interviews tests/core/ai` while working, `uv run pytest` before finishing;
  - lint with `uv run ruff check . && uv run ruff format .`;
  - real-model evals: `uv run python -m app.modules.interviews.interviews_evals --prompt v5 --repeat 3 --model gemini-3.5-flash-lite`, and the v4 baseline the same way (opt-in).
- **Coverage map:**

| Spec ID | Step | Test mode | Notes |
|---|---|---|---|
| AC1 | 7 | first | headers, JSON route unchanged |
| AC2 | 7 | first | all pre-stream codes |
| AC3 | 6 | first | order and a single terminal event |
| AC4 | 5, 6 | first | equal to the JSON path |
| AC5 | 6 | first | DB rows equal |
| AC6 | 6, 13 | first | `aclose` before `done` |
| AC7 | 6 | first | race via the `on_call` hook |
| AC8 | 6 | first | generic error event |
| AC9 | 6 | first | reaction and writing rules |
| AC10 | 6 | first | time to first event under 1 s with the fake |
| AC11 | 9, 10 | first | MockTransport |
| AC12 | 12 | first | six headings; v1–v4 unchanged |
| AC13 | 13 | first | deltas join to the saved text |
| AC14 | 13 | first | EC7–EC11 |
| AC15 | 13 | first | the fake records the cancellation |
| AC16 | 14 | first | AsyncClient concurrency |
| AC17 | 6, 13 | first | `caplog`, no text |
| AC18 | 15, 16 | first / after | runner fns / real model |
| AC19 | 16 | after | live time to first token |
| AC20 | 16 | after | learnings and progress line |
| AC21 | 2, 7 | after | OpenAPI description |
| EC1–EC4 | 7 | first | JSON errors, no stream |
| EC5 | 6 | first | |
| EC6 | 6, 13 | first | |
| EC7–EC11 | 12, 13 | first | |
| EC12–EC16 | 5, 6 | first | |
| EC17, EC18 | 6 | first | |
| EC19 | 7 | first | short ping override |

- **Must verify, not assume:**
  - Google AI Studio's OpenAI-compatible streaming honours `stream_options.include_usage` and how it reports a mid-stream error. Check with a live call before finishing Step 10; until then, missing usage is `None`.
  - `sse-starlette` 3.6 cancels the generator on a client disconnect, so `finally` and cancellation logging run. It must also behave under `TestClient` without event-loop reuse errors across tests.
  - FastAPI 0.162 tears down `yield` dependencies (`get_db`) after a streaming response ends.
  - The `request_id` contextvar is visible inside the streaming generator.
  - The Next.js proxy doesn't buffer `text/event-stream` (client side).
- **Open questions:** none. Every EC has a stated outcome.
- **Known baseline failures:** none seen. The suite is run once before Step 0 to confirm a green baseline.

## Blockers & Resolutions
- The live provider is Google AI Studio, but the key sits in `OPENROUTER_API_KEY` → Step 0 renames the class to a vendor-neutral name and moves the config to `LLM_PROVIDERS` plus per-vendor `LLM_GOOGLE_*` settings, ready for Cloudflare and others later. Streaming is OpenAI-style SSE against Google's compatible endpoint.
- The future fallback providers replace the bank → a seam now, the chain later:
  - `stream()` allows a retry or provider switch only before the first chunk;
  - a future `FallbackProvider` wraps several providers behind `LLMProvider` at the factory, with no turn changes;
  - the bank stays the last resort until then.
- Errors before the stream starts must stay JSON → `prepare_answer` runs before `EventSourceResponse` is built.
- Sync DB inside an async route → the repository work runs in the threadpool; there is no async engine in this slice (spec constraint).
- The follow-up reaction ordering (EC13/EC14) → `ActionKnown` is emitted only once `settle` can't flip the action, so a reaction is never sent and then contradicted.

## Trade-offs & Rationale
- **Shared turn pieces, not an async copy** (user choice): the decide, cap, deadline and fallback rules live once. The cost is a refactor of `answer_turn` and `answer()` before any streaming code.
- **Phase A runs the write in a thread** → the plumbing, event contract and save rule can be tested before the prompt changes. Phase B only swaps the write step.
- **A separate `interviewer_stream` task on v5** → the JSON path keeps v4 and its cache prefix, and the eval comparison is clean.
- **The header line rather than incremental JSON parsing** (spec decision) → a small pure splitter instead of a partial-JSON parser.
- **A disconnect saves nothing** (spec decision) → no "half turn" state, and no regenerate endpoint.
- **Config named by vendor, with the order set separately** (user choice) → rather than numbered names like `PROVIDER_1_*`:
  - reordering the fallbacks is one line, and no keys are renamed;
  - each block says whose key it is;
  - each vendor has its own model and URL.

  It is done before `stream()` is added, so the new code lands on the final names. There are no aliases: a clean break with a clear startup error, at the cost of migrating `.env` once by hand. Only the first provider is built now (YAGNI), and the chain comes later.
- **No extra contract doc** → the event contract lives in the route's OpenAPI `responses` (three-file discipline).

## Project Rules Applied
- `CLAUDE.md` (root):
  - router → controller → repository: the route is thin, and the controller owns the orchestration with no HTTP objects;
  - the `interviews_` prefix;
  - a Pydantic schema for every event;
  - structured errors with generic client messages;
  - no PII in logs;
  - a new dependency justified;
  - the provider abstraction, and prompts as versioned data;
  - LLM output validated with a retry and a fallback;
  - async clients, timeouts, and logged usage and latency;
  - mocked LLM in tests;
  - `graphify update .` after; no commit or push.
- `docs/ai-engineering-learning-path.md`: Slice 4 deliverables and concept 7's Proof in `learnings.md`.

## Skills Consulted
| Skill | Contribution |
|---|---|
| lean-ctx | Mapped `interviews_turn`/`controller`/`route`, the provider and fake, the factory/config (Google via the OpenAI-compatible URL), the test fixtures (`TestClient`, SQLite `StaticPool`, task-routing `llm` fake), and the pure ASGI middleware |
| graphify | Answer-turn flow: `Interviewer` → `InterviewsController.answer` → `record_turn`; tests that guard it |
| grill-me (via `AskUserQuestion`) | Fallback seam vs chain, rename, shared turn pieces, the four confirmed test seams |
| fastapi (knowledge) | Built-in `fastapi.sse` vs `sse-starlette`; `yield`-dependency teardown with streaming (to verify) |
| ponytail | Kept no async DB, no extra doc, no fallback chain, no new test dependency (anyio plugin) |
| security-review (checklist) | Auth and ownership before the stream, a generic error event, no text in logs, untrusted text unchanged |

## Deviations Found During Implementation
- **Step 15:** the eval runner gets `--task stream` instead of `--prompt v5`. `--prompt` swaps the prompt for the JSON write call, but v5 needs `stream()`, its own parser and the `interviewer_stream` task. `--task write` stays v4, so the two compare on the same table.
- **Step 12:** `WindowLedger` gets `text_replies`, so earlier questions are replayed to v5 in v5's own format (a `CATEGORY:` line plus text) instead of v4's JSON.
- **Step 9:** an error after output carries only the `after_output` flag. A streamed call's usage arrives only at its end, so a call cut off mid-stream has no partial usage to report. Its log line records `cancelled` or the error, with latency.
- **Step 11:** `FakeProvider` gets an optional `stream_format` hook. The tests' write fake uses it to stream a scripted v4 JSON reply as v5 text, so existing scripts work on both paths.
- **Step 0:** `tests/conftest.py` blanks the old LLM variables and `LLM_PROVIDERS`, because a developer's shell or `.env` would otherwise trip the clean-break check. The provider exposes `model`, and `build_provider` takes a `model` override for the eval runner.
- **Step 7:** sse-starlette sends `Cache-Control: no-store` (stricter than no-cache). Kept.

## Ready to Implement
- Every spec requirement is mapped to a step; every AC and EC is in the coverage map.
- Every step has a Test tag; the `first` steps name a user-confirmed seam with ordered slices.
- The affected files are identified; the risks and verifications are listed.
- Deviation from the spec, approved by the user after the spec was written: Step 0 (the provider rename, and the move to config named by vendor with the order set separately, building only the first provider) and the fallback seam wording. The spec's "OpenRouter is the only real provider" now reads as "one OpenAI-compatible provider (Google AI Studio), configured through `LLM_PROVIDERS`".
