# Implementation: U2 — One tenacity retry policy for the AI call layer

## Status
Code complete, ready for `/review-feature`. Step 15 done: evals no change vs. baseline (`docs/evals/u2-tenacity-vs-baseline.md`), fault check passed.
Health Check: all present (caveman was installed by the user at the start of the session; a skills search for tenacity found nothing worth installing, every match under 100 installs). Review: all present, level: low

## Completed Steps
- [x] 1. Verify tenacity, then add it
- [x] 2. Build `RetryPolicy` core
- [x] 3. Events and cancellation
- [x] 4. Move Deepgram
- [x] 5. Move `complete`
- [x] 6. Move `stream`
- [x] 7. Embedder: setting, wiring, move
- [x] 8. Delete the old transport code
- [x] 9. Reply attempt iterator
- [x] 10. Move decide and write
- [x] 11. Move write-stream
- [x] 12. Move the feedback turn
- [x] 13. Pin the call budget
- [x] 14. Learnings and docs
- [x] 15. Evals, fault check and graph

## Current Step
### 15. Evals, fault check and graph
- `graphify update .` done.
- Evals: the user ran write, stream, decide and feedback (2 repeats, 2026-11-26, note "u3 tenacity vs baseline"); all inside the baseline margins, compared in `docs/evals/u2-tenacity-vs-baseline.md`. The eval job Claude believed cancelled had in fact run all four (14:34-14:40); those runs hit the provider's rate limit and are listed there but not used for the verdict.
- Fault check (2026-11-26, user, `LLM_TIMEOUT_SECONDS=0.05`; 1 s never timed out because httpx times each read, not the whole call): 12 retry events over 2 answer turns. Every `LLMTimeoutError` got a `retry_wait` (first waits 0.047-0.474 s, cap 0.5; second 0.092-0.832 s, cap 1.0), every call gave up after 3 attempts with `retry_giveup` reason `max_attempts`, the reply loop did not re-ask after a transport error (EC14), the turn fell back to the bank (`write_failed=2`, `bank=2`), events carry `request_id` and `session` and no payload, and `interview_report --last 1` printed normally (AC12, AC15).

## Spike Results (step 1)
tenacity 9.2.1 on Python 3.14.7 (scratchpad script, not in the repo):
- `wait` runs before `stop` (`_post_retry_check_actions`), so `stop_before_delay` sees `upcoming_sleep`, including a wait raised to `Retry-After`. A `Retry-After` of 50 s with a 10 s budget stopped after 1 call with no sleep.
- `stop_before_delay` reads `seconds_since_start`, built from `tenacity.time.monotonic()`. Replacing the module attribute `tenacity.time` with a namespace whose `monotonic` is the fake clock drives it fully. No custom stop needed.
- `wait_random_exponential(multiplier=0.5)` uses the global `random.uniform(0, 0.5 * 2^(n-1))`; `random.seed` makes it repeatable.
- An injected sync `sleep` (`Retrying`) and async `sleep` (`AsyncRetrying`) are the only sleeps used.
- A non-matching exception (`ValueError`) and `asyncio.CancelledError` are re-raised at once, unretried (with `reraise=True`).
- `before_sleep` sees `attempt_number` and `upcoming_sleep` of the coming wait.

## Changes Made
- Not committed (the user commits). Suggested commit for step 1: `build: add tenacity for AI call retries`. Steps 2-8 go in one transport commit (plan's commit groups). Suggested message: `refactor(ai): move transport retries onto one tenacity RetryPolicy with retry events`. Steps 9-12: `refactor(interviews): share the reply-attempt header of the four reply loops`. Steps 13-15: `test(ai): pin the worst-case call budget; docs: U2 learnings and upgrade path`.

## Test Results
- Step 1: `uv run pytest tests/core/ai -q` -> 222 passed
- Step 2: `uv run pytest tests/core/ai/test_retry.py -q` -> 50 passed (red first: import error on `RetryPolicy`); gates: ruff clean, `uv run pytest -q` -> 2514 passed, 7 skipped
- Step 3: `uv run pytest tests/core/ai/test_retry.py tests/modules/interviews/tooling -q` -> 398 passed (red first: 13 event tests failed); gates: ruff clean, `uv run pytest -q` -> 2528 passed, 7 skipped
- Step 4: `uv run pytest tests/core/ai/test_deepgram.py tests/core/ai/test_speech_contracts.py tests/core/speech -q` -> 89 passed; gates: ruff clean, full suite 2528 passed, 7 skipped
- Step 5: `uv run pytest tests/core/ai/test_openai_compatible.py -q` -> 35 passed, 5 repeats (jitter is random); gates: ruff clean, full suite 2528 passed, 7 skipped
- Step 6: `uv run pytest tests/core/ai/test_openai_compatible_stream.py -q` -> 17 passed (red first: 3 of 4 new tests failed); gates: ruff clean, full suite 2532 passed, 7 skipped
- Step 7: `uv run pytest tests/core -q` -> 496 passed (red first: 4 new tests failed); gates: ruff clean, full suite 2535 passed + 1 baseline flake (`test_a_valid_docx_gives_its_paragraphs_then_its_table`, passed on re-run, 42 passed)
- Step 8: grep for `retry_delay|backoff_seconds|run_with_retries|_retry_delay|BACKOFF_BASE|MAX_RETRIES =` in `app tests` -> only a stale `__pycache__` .pyc; gates: ruff clean, full suite 2536 passed, 7 skipped
- Step 9: `uv run pytest tests/modules/interviews/ai/test_interviews_reply_attempts.py tests/test_layers.py -q` -> 19 passed (red first: import error); gates: ruff clean (import order fixed with `ruff --fix` on the two new files only), full suite 2543 passed, 7 skipped
- Step 10: `uv run pytest tests/modules/interviews/ai -q` -> 569 passed, existing tests unchanged (EC17: no test relied on write's missing first-attempt zero-time check, so the shared rule applies); gates: ruff clean, full suite 2543 passed, 7 skipped
- Step 11: `uv run pytest tests/modules/interviews -q -k stream` -> 116 passed (cancellation is covered by `test_stream_turn.py::test_leaving_mid_question_cancels_the_provider_call` and `test_stream_answer.py`); gates: ruff clean, full suite 2543 passed, 7 skipped
- Step 12: gates: ruff clean, full suite 2543 passed, 7 skipped; grep: no `MAX_REPLY_ATTEMPTS`/`MIN_SECONDS_FOR_RETRY` left in the four loops, no `tenacity` in `app/modules` (only a docstring mention)
- Step 13: `uv run pytest tests/core/ai/test_retry_budget.py -q` -> 5 passed (they pin behaviour built in steps 2-12, so they passed on first run; the literal `== 6` / `== 2` fails if a limit changes); gates: ruff clean (import order fixed on the new file), full suite 2547 passed + the docx baseline flake (passed on re-run)
- Step 14: docs only; also fixed a pre-existing pyright error the user reported in `tests/core/ai/test_factory.py:166` (`propagate` returned None, now `nullcontext()`; pyright 0 errors on the file). Gates: ruff clean, full suite 2548 passed, 7 skipped

## Tests Pending
- None

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 2 | first success: 1 attempt, latency stamped, full budget given (sync + async) | spec | AC6 | pass |
| T2 | 2 | each transient type retried once then succeeds; second attempt gets the rest of the budget | spec | AC2 | pass |
| T3 | 2 | each wait in [0, 0.5 x 2^(n-1)], seeded | spec | AC3, EC21 | pass |
| T4 | 2 | Retry-After 10 used as the wait; Retry-After 0 doesn't shorten the jittered wait | spec | AC3, EC4 | pass |
| T5 | 2 | 401 and bad response raised at once, attempts=1, latency stamped | spec | EC8 | pass |
| T6 | 2 | ValueError propagates unchanged and unstamped | spec | EC9 | pass |
| T7 | 2 | max retries stop; max_retries=0 means one attempt | spec | EC5 | pass |
| T8 | 2 | Retry-After past the budget (3 cases, incl. exactly equal) gives up without sleeping | spec | AC4, EC3, EC6 | pass |
| T9 | 2 | almost-over budget: first attempt runs with the remainder, then gives up | spec | EC7 | pass |
| T10 | 2 | error after 3 attempts carries attempts and the whole latency | spec | AC6 | pass |
| T11 | 2 | two concurrent `acall`s on one policy keep their own attempt counts | spec | AC14, EC19 | pass |
| T12 | 3 | `retry_wait` before each wait: attempt, wait, error class, task, vendor logger | spec | AC7 | pass |
| T13 | 3 | `retry_giveup` reason max_attempts / deadline / not_retryable, attempts, elapsed | spec | AC7, EC5 | pass |
| T14 | 3 | events carry only their fixed fields; the error text is not in the log | spec | EC12 | pass |
| T15 | 3 | a cancelled async wait propagates, no second attempt, no give-up event | spec | EC10 | pass |
| T16 | 3 | golden report unchanged with retry events in the log | spec | AC15, EC20 | pass |
| T17 | 6 | a failure before the first chunk logs one `retry_wait` | spec | EC2 | pass |
| T18 | 6 | a failure after output: no wait, no `retry_wait`, one `retry_giveup` reason not_retryable | spec | AC5, EC1 | pass |
| T19 | 6 | the result after a retry carries 2 attempts and the whole latency (wait included) | spec | AC6 | pass |
| T20 | 6 | a stream left after its first chunk closes its HTTP response | inferred | risk: leaked stream | pass |
| T21 | 7 | `embedding_max_retries` defaults to 1 and is in `.env.example` | spec | AC8 | pass |
| T22 | 7 | a negative `EMBEDDING_MAX_RETRIES` is rejected | spec | EC13 | pass |
| T23 | 7 | the factory passes the setting to the embedder | spec | AC8 | pass |
| T24 | 7 | the embedder's `max_retries` argument is honoured; its waits log on `app.rag` | spec | AC2, AC8 | pass |
| T25 | 9 | iterator stops at `MAX_REPLY_ATTEMPTS` | spec | AC13 | pass |
| T26 | 9 | each attempt gets the time left when it starts | spec | AC13 | pass |
| T27 | 9 | a retry with less than `MIN_SECONDS_FOR_RETRY` doesn't start; `stopped_at == 2` | spec | EC16 | pass |
| T28 | 9 | the first attempt runs with less than the retry minimum | code-derived | today's loops | pass |
| T29 | 9 | zero or negative time before the first attempt: no attempt, `stopped_at == 1` | spec | EC17 | pass |
| T30 | 9 | a cancellation in the loop body propagates | spec | EC18 | pass |
| T31 | 13 | `decide` with both layers fully used makes exactly (llm_max_retries + 1) x MAX_REPLY_ATTEMPTS = 6 calls | spec | AC10, EC15 | pass |
| T32 | 13 | a transport error stops the reply loop: llm_max_retries + 1 calls | spec | EC14 | pass |
| T33 | 13 | embedder at most 2 calls; Deepgram at most 2 per direction | spec | AC10 | pass |

## Open Questions
- None

## Baseline Failures
- Flaky on Windows, pass on re-run: `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`, `test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table`, an occasional WinError 10055.

## Known Issues
- `interviews_feedback_turn.py::_attempts` cognitive complexity went from 16 to 19 (lean-ctx health note): the "stopped for time" outcome moved from inside the loop to one `if` after it. Left as is (the loop body is unchanged by design); a candidate for `/simplify` in review.
- `skills-lock.json` changed in the working tree by the user's skill install, not by this slice.

## Deviations from Plan
- Finding (step 1 spike): `stop_before_delay` works, but tenacity reads time only from `tenacity.time.monotonic()`, so a fake clock means patching a private module attribute in every adapter test file. -> plan.md updated: step 2 uses built-in `stop_after_attempt` plus a five-line budget stop on the adapter's injected clock; no tenacity time fixture, no `conftest.py`. -> Approved by: user (2026-11-26)
- Finding (steps 4-5): four more existing tests depended on the old fixed waits (0.5 s minimum), beyond the three AC9 lists: `test_deepgram.py::test_does_not_start_a_retry_past_the_budget` and, in `test_openai_compatible.py`, `test_retries_stop_when_the_total_budget_would_be_exceeded`, `test_a_smaller_budget_argument_caps_retries`, `test_a_larger_budget_argument_never_raises_the_configured_budget`. With full jitter the number of waits that fit a budget is random. -> Each now sends a fixed `Retry-After` (1 s, or 0.6 s via a `busy()` helper) so the same assertion (attempt count, no sleep, clock under the budget) holds every run; nothing loosened. -> Reported to the user at the step 6 checkpoint.
- Finding (step 7): one more test of the same kind, `test_google_embedder.py::test_no_retry_starts_past_the_budget` (0.4 s budget), got the same fixed `Retry-After` (1 s). -> Reported at the step 9 checkpoint.
- Finding (step 6): a failed stream open needs no explicit close: the exception has already finished the generator. The real leak risk was a caller that stops reading after the first chunk; `stream` now closes the inner generator in a `finally` (test T20). -> plan.md step 6 wording kept; noted here.

## Debug Log

## Review
Written by `/review-feature low` (2026-11-26). Scope: the uncommitted U2 working tree against `HEAD` (the commits already on the branch ahead of `main` are U0/U1, reviewed earlier).

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | should-fix | code-review | app/modules/interviews/ai/interviews_write.py:50, interviews_write_stream.py:55 | Write and write-stream now skip the first attempt when no time is left (`left <= 0`); before, they always made one call. This is the change the spec planned (EC17: the turn plan already refuses a write with too little time, so it should be the same in practice), and with zero time the old call would have run with a timeout of zero or less. But the change is pinned only at the iterator level (T29), not in the write loops themselves. Add one test per loop: an already-expired deadline makes no LLM call and returns the fallback. | fixed: `tests/modules/interviews/ai/test_write_expired_deadline.py` (write and stream_write: no call, `Written(None, [], ...)`) |
| R2 | should-fix | fault check | app/core/ai/openai_compatible.py:53 | The retry events carry the adapter's fixed `task` label (`chat`; also `embed`, `transcribe`, `synthesize`), not the interview task that made the call (`follow_up_decision`, `interviewer_stream`, ...). They can be joined to the `llm_call` line through `request_id`, but a later retries report would be clearer with the real task. Cheap to change now (pass the caller's `trace_labels["task"]` to `call`/`acall`), harder once something reads the events. | fixed: `RetryPolicy.call`/`acall`/`log_giveup` take an optional `task` (kept on the per-call state); `complete` and `stream` pass `trace_labels["task"]`; `TracingProvider` was dropping `trace_labels` before the adapter and now passes them on. Tests: `test_the_events_name_the_callers_task_when_given`, `test_the_retry_events_carry_the_task_from_the_trace_labels`, `test_the_tracing_wrapper_passes_the_trace_labels_on` |
| R3 | nit | lean-ctx health | app/modules/interviews/ai/interviews_feedback_turn.py:332 | `_attempts` went from a cognitive complexity of 16 to 19: the "stopped for time" outcome moved from inside the loop to one `if` after it. The loop body is unchanged by design. | won't fix (user chose not to fix) |
| R4 | nit | traceability | docs/features/u2-tenacity/spec.md (AC9) | AC9 says three wait-length assertions change; five more budget tests in `test_deepgram.py`, `test_openai_compatible.py` and `test_google_embedder.py` also changed (each now sends a fixed `Retry-After` to stay stable under full jitter; same assertions). Recorded under Deviations and reported to the user; AC9's text doesn't say so. | fixed: AC9 in spec.md now lists the five tests and why |
| R5 | nit | traceability | tests/core/ai/test_retry.py | EC19 (concurrent calls on one policy) is tested for two async calls only; `complete` runs in worker threads and has no threaded test. The per-call state is the same code for both paths, so the risk is low. | won't fix (user chose not to fix) |

After the fixes: `uv run --with ruff ruff check app tests` -> pass (import order fixed with `ruff --fix` on the new test file); `uv run pytest -q` -> 2553 passed, 7 skipped.

Check results:
- `uv run --with ruff ruff check app tests` -> pass
- `uv run pytest` -> not re-run: task.md records a green full-suite run on the final code (2548 passed, 7 skipped, step 14); only docs changed since
- type checker -> not run: low level (pyright ran on `tests/core/ai/test_factory.py` only, 0 errors, when fixing the user-reported error)
- static security scan, dependency audit -> not run: low level
- migration round-trip -> not applicable: no migration in the diff
- `code-review` (low) -> 1 finding (R1)
- `security-review` -> not run: the diff touches no auth, permissions or secrets, and the new events log no user data (T14)
- `llm-security` -> not invoked (low level); its data-leak check was applied by hand: no prompt changed, the retry events carry only fixed fields and never the error text or payload (T14, fault check). No findings
- `simplify` -> not run: low level
- Project rules checklist -> pass: tenacity only in `app/core/ai/`; the iterator lives in the interviews `ai/` folder with the `interviews_` prefix and imports only interview constants; `tests/test_layers.py` passes; settings from config (`embedding_max_retries` in `.env.example`); covering evals run and compared (`docs/evals/u2-tenacity-vs-baseline.md`)
- Traceability -> every AC1-AC15 and EC1-EC21 maps to a passing test (T1-T33) or a recorded check (AC1/AC11 grep, AC12 suite + evals + fault check); gaps noted as R1, R4, R5
- Working tree hygiene (not findings): `graphify-out/cache/.gfy-replace-bak-5k8j6w_o.tmp` is a leftover temp file, and `.agents/skills/caveman/` plus `skills-lock.json` come from the user's skill install; leave them out of the U2 commits
## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1 | find-skills | user asked; no tenacity skill with enough installs |
| 2-3 | tdd, test | test-first; slices were written as one batch per step, then the code (red verified before code) |
| all | ponytail | smallest code per step |

## Links
- Spec: docs/features/u2-tenacity/spec.md
- Plan: docs/features/u2-tenacity/plan.md
