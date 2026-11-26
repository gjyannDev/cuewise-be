# Implementation Plan: U2 — One tenacity retry policy for the AI call layer

## Overview
Replace the hand-written transport retry loops in `app/core/ai/` with one tenacity-based `RetryPolicy` (built per vendor), and share the attempt header of the four interviews reply loops through one iterator, with retry and give-up log events, a call-budget test and a real fault check.

## Architecture & Design
Two layers, each centralized, kept separate:
- **Transport retries** (`app/core/ai/retry.py`): a `RetryPolicy` class wraps tenacity's `Retrying` / `AsyncRetrying` and uses its built-ins wherever they fit: `retry_if_exception` (the three transient `LLMError` types), `stop_after_attempt` combined with `stop_before_delay` (stop on max retries or when the wait won't fit the budget), `wait_random_exponential` with a multiplier of 0.5 (full jitter), and `before_sleep` for the log event. The only custom rule is a thin wait wrapper that raises the wait to the vendor's `Retry-After`. Each adapter builds its own policy in its constructor from the arguments it already takes, so constructors keep their `clock` and `sleep` arguments (the unused `rng` argument goes). The adapters still use their own clock to give each attempt its remaining time and to stamp latency; in tests one fixture points tenacity's time at the same fake clock. The policy is shared by concurrent requests, so it holds only configuration; every call creates its own tenacity object and its own per-attempt state. The stream retries only an "open and read the first chunk" step. The module docstring names both layers and the worst-case call count.
- **Content retries** (`app/modules/interviews/ai/interviews_reply_attempts.py`): an iterator that yields each attempt with its remaining time and stops on max attempts or too little time. decide, write, write-stream and feedback keep their own call/parse/log bodies. No tenacity here.

## Approaches Considered
Spec.md settled the behaviour and the centralization choices (A: one policy object; C: shared reply-attempt gate). Open design choices:

| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. `RetryPolicy` class per vendor; stream retries only open + first chunk | Rules, injected time, logging and stamping in one class; adapters shrink; constructors unchanged | **Yes** — leanest design meeting every AC (ponytail); the shape U3 copies |
| B. `@retry` decorators on each vendor method | Fewer lines per caller, but injected clock/sleep/rng, stamping and the stream don't fit a decorator | No |
| C. Stream retried by `async for attempt in AsyncRetrying` around the whole generator | One loop shape, but tenacity's attempt context swallows exceptions, including `GeneratorExit` and cancellation, inside an async generator | No — fragile |
| D. Keep today's exact wait formula as a custom wait | Waits and tests unchanged, but one more custom rule and an `rng` argument kept only for it | No — user chose built-in full jitter (`wait_random_exponential`), the style U3's `.with_retry()` uses |
| E. Reply loops as one callback helper (`run(call, parse, ...)`) | Fewest lines, but the stream's `Reset`s and cancellation logging and feedback's tracer checks force many hooks | No — share only the attempt header |
| F. Reply attempt iterator in `core/ai` | Reusable, but `core` would import interview constants and know interview rules | No — it lives in the interviews `ai/` folder (project layering) |

## Spec Requirements -> Implementation
- Tenacity verified, dependency added -> Step 1
- `RetryPolicy` rules, stamping, per-call state, docstring -> Step 2
- Events, cancellation, report unaffected -> Step 3
- Adapters build and use the policy -> Steps 4, 5, 6, 7
- Embedder retries as a setting -> Step 7
- Old transport code deleted -> Step 8
- Reply attempt iterator and the four loops -> Steps 9, 10, 11, 12
- Call-budget test -> Step 13
- Reasoning recorded, docs updated -> Step 14
- Evals vs baseline, real fault check -> Step 15

## Implementation Steps
Checkpoint interval: every 3 steps (this touches the LLM call path and four working loops; pause after steps 3, 6, 9 and 12).
Suggested commit groups for the user (never committed by Claude): steps 1; 2-8 (transport); 9-12 (reply iterator); 13-15 (tests, docs, graph).

1. Verify tenacity, then add it — Files: `pyproject.toml`, `uv.lock`; a throwaway check script in the scratchpad, not the repo — Verify: `uv run python -c "import tenacity"` + the throwaway script showing, on the installed version and Python 3.14: whether `stop_before_delay` sees the upcoming wait (including a `Retry-After`-raised one) when it decides, the range `wait_random_exponential(multiplier=0.5)` gives per attempt, that an injected sync and async `sleep` is used, how tenacity's clock can be pointed at a fake one and the global `random` seeded, that a `CancelledError` and a non-matching exception are re-raised unretried, and that `before_sleep` sees the next wait; then `uv run pytest tests/core/ai -q` — Test: skip (dependency and a fact-finding spike; results are noted for `learnings.md`). If `stop_before_delay` can't be driven by a fake clock or doesn't see the upcoming wait, step 2 falls back to a five-line custom stop that reads the adapter's clock; any other failed assumption updates step 2 before building.
2. Build `RetryPolicy` core in `retry.py` (nothing calls it yet; old functions stay until step 8): retryable types (built-in `retry_if_exception`), full-jitter waits (built-in `wait_random_exponential`, multiplier 0.5) raised to `Retry-After` by a thin wrapper, the attempt stop (built-in `stop_after_attempt`) plus a five-line budget stop on the adapter's clock (user decision after the step 1 spike: tenacity's own clock can only be faked by patching a private module attribute), stamping of `attempts` and `latency_ms`, the give-up reason derived after the failure, and the two-layer module docstring. All per-call state (the tenacity object) is created inside each call, never on the policy. No tenacity time fixture: tenacity's clock makes no decision; tests that check wait bounds seed `random` themselves. Port every old assertion into `tests/core/ai/test_retry.py` (a bound check instead of the old backoff range, Retry-After minimum, budget give-up, max retries, attempts/latency stamping, no attempt past the budget) — Files: `app/core/ai/retry.py`, `tests/core/ai/test_retry.py` — Verify: `uv run pytest tests/core/ai/test_retry.py -q` + gate commands — Test: first. Seam: `RetryPolicy`'s sync and async calls (user-confirmed: the shared policy + the public vendor methods). Slices, one behaviour each: (a) each wait lies between 0 and `0.5 x 2^(attempt-1)` with a seeded `random`, and a larger `Retry-After` replaces it (AC3, EC4, EC21); (b) only the three transient types are retried, others raised at once (AC2, EC8, EC9); (c) `max_retries=0` and the max-retries stop (EC5); (d) deadline stop, including `Retry-After` longer than the remaining budget and an almost-over budget (AC4, EC3, EC6, EC7); (e) attempts and latency stamped on the error and the result (AC6); (f) two concurrent calls on one policy keep separate attempts and waits (EC19).
3. Events and cancellation — Files: `app/core/ai/retry.py`, `tests/core/ai/test_retry.py`, `tests/modules/interviews/tooling/test_interview_report_formats.py` plus its fixture log in `tests/modules/interviews/tooling/data/` — Verify: `uv run pytest tests/core/ai/test_retry.py tests/modules/interviews/tooling -q` + gate commands — Test: first. Seams: `RetryPolicy` calls (events observed with the U1 `capture_logs` fixture), and the public report entry the golden-file test already uses. Slices: (a) a `retry_wait` event before each wait with task, attempt, wait seconds and error class, on the vendor's logger (AC7); (b) a `retry_giveup` event with attempts, elapsed, error class and `reason` = `max_attempts` | `deadline` | `not_retryable` (AC7, EC1, EC5); (c) no payload in either event (EC12); (d) async cancellation propagates at once and logs no give-up (EC10); (e) the report output is identical with retry events present in the log (AC15, EC20).
4. Move Deepgram — Files: `app/core/ai/deepgram.py`, `tests/core/ai/test_deepgram.py` — Verify: `uv run pytest tests/core/ai/test_deepgram.py tests/core/ai/test_speech_contracts.py -q` + gate commands — Test: skip (wiring; the existing tests are the proof). One assertion on wait length changes (`test_a_503_is_retried_after_backoff_then_succeeds`: 0.5-0.75 s becomes 0 to 0.5 s); the unused `rng` argument is removed.
5. Move `complete` — Files: `app/core/ai/openai_compatible.py`, `tests/core/ai/test_openai_compatible.py` — Verify: `uv run pytest tests/core/ai/test_openai_compatible.py -q` + gate commands — Test: skip (wiring; the existing tests are the proof). Two assertions on wait length change: "rate limit then success" (0.5-0.75 s becomes 0 to 0.5 s) and "second wait longer than the first" (becomes a check that each wait is within its own cap, because full jitter can shrink); the unused `rng` argument is removed.
6. Move `stream` to retry only the open + first-chunk step, close the abandoned generator after a failed open, and stamp `attempts`, `latency_ms` and `after_output=True` on a later failure — Files: `app/core/ai/openai_compatible.py`, `tests/core/ai/test_openai_compatible_stream.py` — Verify: `uv run pytest tests/core/ai/test_openai_compatible_stream.py -q` + gate commands — Test: first. Seam: `OpenAICompatibleProvider.stream`. Slices: (a) failure before the first chunk is retried and nothing was yielded (EC2); (b) failure after a chunk is raised with `after_output=True`, no retry, no wait (AC5, EC1); (c) the final `LLMResult` carries the attempt count of the successful open (AC6).
7. Embedder: setting, wiring, move — Files: `app/core/config.py`, `.env.example`, `app/core/ai/factory.py`, `app/core/ai/google_embedder.py`, `tests/core/test_config.py`, `tests/core/ai/test_google_embedder.py`, `tests/core/ai/test_factory.py` — Verify: `uv run pytest tests/core -q` + gate commands — Test: first. Seam: `Settings` (new `embedding_max_retries`: default 1, `ge=0`, listed in `.env.example`) and `GoogleEmbedder.embed`. Slices: (a) default 1, negative rejected (AC8, EC13); (b) the factory passes the setting through, and the class argument defaults to 1 so its existing tests stay unchanged; (c) `embed` retries through the policy, `MAX_RETRIES` is gone and the unused `rng` argument is removed.
8. Delete the old transport code — Files: `app/core/ai/retry.py`, and unused imports in `openai_compatible.py`, `google_embedder.py`, `deepgram.py` — Verify: `ctx_search` for `retry_delay|backoff_seconds|run_with_retries|_retry_delay|BACKOFF_BASE` in `app tests` returns nothing, then `uv run pytest -q` + gate commands — Test: skip (deletion; the full suite is the proof).
9. Build the reply attempt iterator and its tests — Files: `app/modules/interviews/ai/interviews_reply_attempts.py` (new), `tests/modules/interviews/ai/test_interviews_reply_attempts.py` (new) — Verify: `uv run pytest tests/modules/interviews/ai/test_interviews_reply_attempts.py -q` + gate commands — Test: first. Seam: the iterator's public interface (the loops are observed through their public functions). Slices: (a) stops at `MAX_REPLY_ATTEMPTS`; (b) each attempt receives the time left; (c) after the first attempt it stops when less than `MIN_SECONDS_FOR_RETRY` remains and says it stopped for time (EC16); (d) no time before the first attempt means no attempt (EC17); (e) cancellation raised in the loop body is not swallowed (EC18).
10. Move decide and write onto the iterator — Files: `app/modules/interviews/ai/interviews_decide.py`, `app/modules/interviews/ai/interviews_write.py` — Verify: `uv run pytest tests/modules/interviews/ai -q` + gate commands — Test: skip (wiring; the existing decide and write tests, unchanged, are the proof). Decide's time left is `end - clock()`; write's is the deadline's. If an existing test shows the write loop must not stop on zero time at its first attempt (EC17), keep today's rule there and say so.
11. Move write-stream onto the iterator — Files: `app/modules/interviews/ai/interviews_write_stream.py` — Verify: `uv run pytest tests/modules/interviews -q -k "stream"` then `uv run pytest tests/modules/interviews -q` + gate commands — Test: skip (wiring; existing tests, unchanged). Keep its `Reset`, `cancelled` and `after_output` handling exactly (EC18); read its tests first and say if cancellation is untested.
12. Move the feedback turn onto the iterator — Files: `app/modules/interviews/ai/interviews_feedback_turn.py` — Verify: `uv run pytest tests/modules/interviews -q` + gate commands — Test: skip (wiring; existing tests, unchanged). It reads the iterator's "stopped for time" answer to record `no_time` / `retry_skipped:no_time`.
13. Pin the call budget — Files: `tests/core/ai/test_retry_budget.py` (new) — Verify: `uv run pytest tests/core/ai/test_retry_budget.py -q` + gate commands — Test: first. Seams: the public `decide` function with a real `OpenAICompatibleProvider` on a mock transport (transport failures plus malformed replies: total HTTP calls never exceed `(llm_max_retries + 1) x MAX_REPLY_ATTEMPTS`; a transport error stops the reply loop), and `GoogleEmbedder.embed` / Deepgram `transcribe` for their per-vendor maximum (AC10, EC14, EC15). Numbers come from the live config and constants, not literals. The `decide` seam is unconfirmed until its signature is read; tell the user if a different entry is needed.
14. Learnings and docs — Files: `docs/features/u2-tenacity/learnings.md` (new), `docs/ai-engineering-upgrade-path.md` (U2 section: three callers, the `RetryPolicy` and iterator design) — Verify: files exist; `uv run pytest -q` + gate commands — Test: skip (docs). Learnings cover: transport vs content retries and why the reply layer stays out of tenacity (AC11), the 3 x 2 = 6 budget, why a stream retries only before its first chunk, why tenacity checks stop before wait, why state is per call, why full jitter was deferred, what the iterator does and doesn't share, and the step 1 spike results.
15. Evals, fault check and graph — Files: `docs/evals/baselines.md` (only if a score is kept on purpose), `graphify-out/` (via `graphify update .`) — Verify: (a) run the eval tasks that cover the four reply loops (the ones `docs/evals/baselines.md` lists for decide/write/feedback), same model, at least 2 repeats, compare through Langfuse; a difference within the noise margin is no change; (b) a real fault check: with the dev server stopped, one interview with `LLM_TIMEOUT_SECONDS` set very low, confirm `retry_wait` and `retry_giveup` lines in the log and that `uv run python -m app.scripts.interview_report --last 1` still reports normally — Test: after (real model and real log; evals only guard the loops, since a healthy provider never retries).

## Affected Files & Patterns
- `app/core/ai/retry.py` — `RetryPolicy`, events, two-layer docstring; keeps `Attempted`, `parse_retry_after`, `raise_for_status`; loses the three old functions.
- `app/core/ai/openai_compatible.py` — `complete` and `stream` call the policy; `_retry_delay` and the `start/attempt` bookkeeping go; `_stream_attempt` stays.
- `app/core/ai/deepgram.py` — `_with_retries` calls the policy; adapters unchanged.
- `app/core/ai/google_embedder.py`, `factory.py`, `config.py`, `.env.example` — embedder retries from settings.
- `app/modules/interviews/ai/interviews_reply_attempts.py` (new) and the four loop files (`interviews_decide.py`, `interviews_write.py`, `interviews_write_stream.py`, `interviews_feedback_turn.py`) — the attempt header only.
- `pyproject.toml`, `uv.lock` — `tenacity`; `docs/ai-engineering-upgrade-path.md` — U2 section updated.
- Patterns to follow: injected `clock`/`sleep`/`rng` as in the current adapters; U1 `get_logger` events with fixed field names (no payloads) on each vendor's logger (`app.llm`, `app.rag`, `app.stt`, `app.tts`); the `*_max_retries` settings style; the interviews `interviews_` file prefix and mirrored test folders.
- Risks:
  - Per-call state: the policy is shared by concurrent requests (and `complete` runs in worker threads), so waits and attempt counts must never live on it (step 2 slice f).
  - Tenacity uses its own clock and the global `random`. Tests point its time at the fake clock and seed `random` through one fixture; the adapters' clock and tenacity's clock must agree in tests (in production both are monotonic real clocks). If the fixture can't be made reliable, step 2 falls back to the custom stop on the adapter's clock.
  - Full jitter can give a near-zero wait on a 429 with no `Retry-After`; the retry count (default 2) still bounds the extra calls, and a `Retry-After`, when sent, is always honoured.
  - A failed stream open must close its generator, or the HTTP stream leaks.
  - Tenacity is not installed yet; step 1 checks its behaviour and Python 3.14 support before anything is built on it.
  - The new events must not change `interview_report` output (step 3 slice e).
  - The four reply loops differ in small ways (write has no zero-time check on the first attempt; decide bounds time by its own `end`; feedback records why it stopped). The iterator must reproduce each; existing loop tests are the guard, and a loop that differs keeps its own rule.
  - The `decide` signature is unread (step 13).

## Testing Strategy
- Framework & command: `pytest` — `uv run pytest <path> -q` per step; full run `uv run pytest`.
- Gate commands (after every step): `uv run pytest` (includes `tests/test_layers.py`), `uv run --with ruff ruff check app tests`.
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 8 | skip | grep for the old names returns nothing; full suite |
| AC2 | 2, 4, 5, 6, 7 | first | policy tests plus unchanged vendor tests |
| AC3 | 2 | first | seeded `random`, bound check |
| AC4 | 2 | first | almost-over budget; no new attempt |
| AC5 | 6 | first | after-output stream failure |
| AC6 | 2, 6 | first | stamps on error and result |
| AC7 | 3 | first | events captured with U1 `capture_logs` |
| AC8 | 7 | first | config default, validation, `.env.example` |
| AC9 | 2-8, 10-12 | first / skip | `test_retry.py` ported; three wait-length assertions in vendor tests updated (steps 4, 5); the rest unchanged |
| AC10 | 13 | first | call-budget test |
| AC11 | 10, 11, 12, 14 | skip | loops use the iterator, no tenacity in `app/modules/` (grep); learnings written |
| AC12 | 8, 12, 15 | after | full suite, ruff, eval comparison |
| AC13 | 9 | first | iterator tests |
| AC14 | 2 | first | concurrent calls on one policy |
| AC15 | 3, 15 | first / after | golden report test with retry events; real report run |
| EC1 | 3, 6 | first | |
| EC2 | 6 | first | |
| EC3, EC4, EC5, EC6 | 2 | first | EC5 reason in step 3 |
| EC21 | 2 | first | near-zero wait still retries |
| EC7 | 2, 5 | first | policy and `complete` with a tiny budget |
| EC8, EC9 | 2 | first | |
| EC10, EC12 | 3 | first | EC10 async only |
| EC11 | 8 | skip | existing `parse_retry_after` tests stay green |
| EC13 | 7 | first | |
| EC14, EC15 | 13 | first | transport error stops the reply loop |
| EC16, EC17 | 9 | first | plus loops' existing tests in steps 10-12 |
| EC18 | 9, 11 | first / skip | iterator test; write-stream's existing cancellation test unchanged |
| EC19 | 2 | first | |
| EC20 | 3 | first | |

- Must verify, not assume: tenacity's behaviour on the installed version (step 1 spike, then step 2-3 tests); the stream's connection is released after a failed open (step 6); that each loop's existing tests pass with the iterator (steps 10-12); that the report is unchanged by the new events (step 3, 15); that eval scores stay within the noise margin (step 15).
- Open questions: none; every EC has an outcome.
- Known baseline failures: flaky on Windows, pass on re-run: `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`, `test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table`, an occasional WinError 10055. `ruff check .` (whole repo) has 47 errors in applied `alembic/` migrations; the gate is `app tests` only.

## Blockers & Resolutions
- Old tests import the deleted functions -> the assertions move to `RetryPolicy` (user decision, AC9).
- Wait length changes with built-in full jitter -> three assertions updated (two in `test_openai_compatible.py`, one in `test_deepgram.py`); user decision.
- Embedder tests build `GoogleEmbedder` without `max_retries` -> the class argument defaults to 1; the factory passes the setting.
- The four loops are not identical -> the iterator shares only the header; differences stay in each loop (EC17 fallback rule).
- A running `fastapi dev` holds `logs/app.log` -> tests log to `TEST_LOG_FILE`; stop the dev server for the step 15 fault check.

## Trade-offs & Rationale
- One policy class instead of decorators or helper functions -> keeps injected time, logging and stamping together; U3 copies the same rules.
- Configuration on the policy, state per call -> safe under concurrent requests and worker threads.
- Built-in full jitter and built-in stops over today's custom formula -> shorter, idiomatic, the same style U3's `.with_retry()` uses; costs a change in the wait (0 up to the cap instead of 100-150% of the base) and three updated assertions in existing tests.
- Reason for giving up derived after failure -> one place, no tenacity callbacks to coordinate.
- Reply-loop gate shared, bodies not -> removes the repeated header without a callback maze.
- Reply iterator in the interviews `ai/` folder, not `core/ai` -> `core` stays unaware of interview constants (layer rule).
- Embedder constructor default instead of a required argument -> keeps its tests unchanged at the cost of a style difference.
- Old transport code deleted only in step 8 -> every step keeps the suite green.
- Stable event names (`retry_wait`, `retry_giveup`) -> a later report section (retries per call, give-up reasons) can read them; not built in U2.

## Project Rules Applied
- `CLAUDE.md` layers: tenacity and `RetryPolicy` live only in `app/core/ai/`; the iterator lives in a feature `ai/` folder and imports no vendor SDK or LangChain; no routes, controllers, services or repositories change.
- `CLAUDE.md` AI guidelines: timeouts, retries with backoff, logging per call without raw content; eval comparison after a change in `core/ai` or a feature `ai/` folder (step 15).
- `CLAUDE.md` Don'ts: `tenacity` is the one new dependency, justified in spec.md; settings from config, no hard-coded counts.
- `CLAUDE.md` workflow: tests and lint per step, `graphify update .`, no commit or push.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify | `/feature` query: retry callers and the `Deadline` link; reused, not re-run |
| lean-ctx | read the retry, provider, Deepgram, embedder, config, test and reply-loop files |
| ponytail | applied directly: one policy class, a header-only iterator, no new abstraction layer |
| grilling | asked directly: test seam confirmed; options A and C chosen by the user |
| tdd | seams only: named and confirmed for steps 2, 3, 6, 7, 9, 13 |
| langfuse | step 15: compare eval runs against `docs/evals/baselines.md` |

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC and EC mapped, none uncovered
- Gate commands listed
- Every step names exact files and a verification command
- Approaches Considered filled; checkpoint interval set
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented
- No deviations from spec
