# Implementation: U3b1 Interview calls on LangChain

## Status
Ready for PR (all 20 steps done; next: `/review-feature`)
Health Check: all present (implement); review: all present, level: low

## Completed Steps
- [x] 1. Stream spike live test (`tests/live/test_chat_stream_live.py`); skipped without `LLM_LIVE_TEST=1`; the user runs it at Stop 1
- [x] 2. Streaming `FakeChatModel` (`fake_chunks`, `_astream`; contract test covers Gemini and the fake)
- [x] 3. Dual-backed `llm` fixture (`_RoutedChatModel` routes to the same `FakeProvider`s; `llm.chat`)
- [x] 4. `--blocking` mode on the generation eval (`BLOCKING_ARM_PROMPTS`, `simulate_main_questions(blocking=True)`)
- [x] 5. `write()` on `complete_chat`; `Interviewer`, both services and the answer dependency take `chat_model`
- [x] 6. Eval tooling for write and generation on the chat model (`run_case`, `simulate_main_questions`, `run_generation`, `run_rag_task`)
- [x] 7. Stop 2: write + generation evals -> no change (`docs/evals/u3b1-write-vs-baseline.md`)
- [x] 8. `ModelDecision` (`interviews_model_schemas.py`) and `decide()` on `complete_structured` + `parse_decision_reply`; `decide` takes `sleep`; budget test ported (pins 6 calls)
- [x] 9. Eval tooling for decide: `run_decide_case` on the chat model with `ModelDecision`
- [x] 10. Stop 3: decide eval -> better (0.933 x 3 vs 0.800 / 0.867); new decide baseline row
- [x] 11. Spike findings meet FR1 (decision recorded in learnings.md)
- [x] 12. `stream_chat` helper (`app/core/ai/chat_stream.py`); `ChatTrace.fail(partial_text)` / `cancel`; `FakeChatModel.chunk_delay`
- [x] 13. `stream_write` / `stream_draft` on `stream_chat`; `Interviewer.stream_turn` uses the chat model; `ProviderChatModel` streams from `FakeProvider.stream`
- [x] 14. Eval tooling for stream: `run_stream_case` on `stream_chat`
- [x] 15. Stop 4: stream eval -> no change in quality (1.00 x 3), first token ~300-600 ms faster; "stream (current latency)" row
- [x] 16. `ModelScore` (nested, required fields; top level ignores extras like `_RawScoreReply`); `FeedbackGenerator.score` on `complete_structured` + `parse_score_reply`, `.write` on `complete_chat` + `parse_write_reply`; feedback service and dependency take `chat_model`
- [x] 17. Eval tooling for feedback: `run_feedback_case` / `run_feedback` on the chat model
- [x] 18. Stop 5: feedback eval -> no change (0.90 / 1.00 / 0.90; content scores held; generations nest under steps)
- [x] 19. Provider wiring removed: `get_llm_provider`, `app.state.llm_provider` and the provider build/close in `app/main.py`; `Interviewer` and both interview services take only the chat model (in the old `llm` positional slot); the eval runner builds only the chat model and drops `--reasoning-effort`; the fixture's old-provider half removed. AC11 search finds nothing outside `app/core/ai/`.
- [x] 20. learnings.md finished, upgrade path updated (U3b1 ticked, review pending), `graphify update .` run

## Current Step
### Done
- Next: `/review-feature low` (the user's default), then commits.

## Changes Made
- Nothing committed (the user commits).
- Suggested commit for step 1: `test(ai): add the opt-in live stream spike for the Gemini chat model`
- Suggested commit for step 2: `test(ai): let FakeChatModel stream and cover streaming in the chat contract test`
- Suggested commit for step 3: `test(interviews): serve the chat model from the llm fixture's scripts (dual-backed)`
- Suggested commit for step 4: `feat(evals): add --blocking to the generation eval (JSON writer arms)`
- Suggested commit for step 5: `refactor(ai): move the blocking interview write onto LangChain`
- Suggested commit for step 6: `refactor(evals): run the write and generation evals on the chat model`
- Suggested commit for step 8: `refactor(ai): move the follow-up decision onto LangChain with a required-fields schema`
- Suggested commit for step 9: `refactor(evals): run the decide eval on the chat model`
- Suggested commit for steps 12-14: `refactor(ai): stream the interviewer's question through LangChain (stream_chat)`
- Suggested commit for steps 16-17: `refactor(ai): move end-of-interview feedback onto LangChain (score schema, write text)`
- Suggested commit for step 19: `refactor(interviews): drop the LLMProvider wiring now that every call runs on the chat model`
- Suggested commit for step 20 and the eval files: `docs(u3b1): learnings, eval comparisons and upgrade-path progress`

## Test Results
- Step 1: `uv run pytest tests/live/test_chat_stream_live.py -q` -> 3 skipped; gate `uv run pytest -q` -> 2707 passed, 10 skipped; `ruff check app tests` -> pass
- Step 2: `uv run pytest tests/core/ai/test_chat_contract.py -q` -> 29 passed; gate -> 2716 passed, 1 failed (`test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table`, passes alone: the known flaky test), ruff pass
- Step 3: `uv run pytest tests/modules/interviews -q` -> 1825 passed, 5 skipped; gate -> 2724 passed, 10 skipped, ruff pass
- Step 4: `uv run pytest tests/modules/interviews/tooling -q` -> 356 passed; gate -> 2727 passed, 10 skipped, ruff pass; `graphify update .` done (end of stage 0)
- Step 5: `uv run pytest tests/modules/interviews/ai/test_write.py -q` -> 11 passed; gate -> 2738 passed, 10 skipped, ruff pass (one earlier full run had `test_turn_budget.py::test_usage_of_both_calls_is_summed...` fail once; it passed in the next full run and in 3 interview-suite runs, so it is watched, not fixed)
- Step 6: `uv run pytest tests/modules/interviews/tooling -q` -> 356 passed; gate -> 2737 passed, 1 failed (the known flaky docx test, passes alone), 10 skipped, ruff pass; `graphify update .` done (end of stage 1)
- Step 8: `uv run pytest tests/modules/interviews/ai/test_decide.py -q` -> 10 failed before the code (red), 11 passed after; `tests/core/ai/test_retry_budget.py` -> 5 passed; gate -> 2749 passed, 10 skipped, ruff pass
- Step 9: `uv run pytest tests/modules/interviews/tooling -q` -> 356 passed; gate -> 2749 passed, 10 skipped, ruff pass; `graphify update .` done (end of stage 2)
- Step 12: `uv run pytest tests/core/ai/test_chat_stream.py -q` -> red (module missing), then 13 passed (3 runs in a row); first green run found a real bug (a finished stream's generation was ended as `cancelled` before `succeed`), fixed; gate -> 2762 passed, 10 skipped, ruff pass
- Step 13: `uv run pytest tests/modules/interviews -q` -> 5 failed first (scripted 503 now retried; client-left tests read `cancelled` at once; streamed redaction on the old tracer), fixed; gate -> 2763 passed, 10 skipped, ruff pass
- Step 14: `uv run pytest tests/modules/interviews/tooling -q` -> 356 passed; gate -> 2763 passed, 10 skipped, ruff pass; `graphify update .` done (end of stage 3)
- Step 16: `uv run pytest tests/modules/interviews/ai/test_feedback_turn.py -q` -> 10 failed before the code (red), 12 passed after; route feedback tests -> 66 passed with the decide and feedback-turn files; gate after step 17
- Step 17: `uv run pytest tests/modules/interviews/tooling -q` -> 356 passed; gate -> 2775 passed, 10 skipped, ruff pass; `graphify update .` done (end of stage 4)
- Step 19: first run 3 failed (the fixture test of the old-provider half; the summary-eval hint text; the known flaky docx test), fixed the first two; gate -> 2775 passed, 10 skipped, ruff pass; `tests/test_layers.py` -> 34 passed; AC11 search (`LLMProvider|get_llm_provider|\bllm_provider\b|build_provider` in `app/` outside `app/core/ai/`) -> none; pyright on the changed files -> 0 errors except `interviews_feedback.py:266` (pre-existing, file unchanged)
- Final (step 20): `uv run pytest -q` -> 2775 passed, 10 skipped; `uv run --with ruff ruff check app tests` -> pass; `graphify update .` done

## Tests Pending
- Stop 1: done 2026-11-27 (live spike in learnings.md; blocking baseline rows in baselines.md, 3 repeats: `130930` r1-r2 + `132414` r1)
- Stop 2: done 2026-11-27 -> no change (2 of 3 repeats reached Langfuse for each run; `141604` left out, rate-limited)
- Stop 3: decide run `20261127-153726` -> accuracy 0.933 / 0.933 vs 0.800 / 0.867, over-probing 0 / 0 vs 2 / 1: better (`docs/evals/u3b1-decide-vs-baseline.md`). Confirmed by `20261127-155824` (0.933); recorded as the new "decide (current)" row in `baselines.md`.
- Stop 4 (after step 14): stream `--repeat 3` (user)
- Stop 5 (after step 17): feedback `--repeat 3` (user)
- Stage 4 rewrites (EC17): `test_feedback_endpoint.py` (the temperature/budget spy reads `FakeProvider.complete`, the trace-label lines replaced by a check that each call reached its task's script; enough scripted 503s), tooling `test_feedback_evals.py` (the grader wrapped in `ProviderChatModel` through `run_feedback_case` / `main` wrappers).
- Stage 3 rewrites (EC17): `test_stream_turn.py` (enough scripted 503s for the call layer; `closed_soon` before the `cancelled` check), `test_stream_answer.py` (`closed_soon`), `test_profile_redaction.py` (streamed write traced through `TracerHandle`), tooling `test_evals.py` (`run_stream_case` wrapper; enough 503s).
- Open: every `--repeat 3` run today before the stream run reached Langfuse with only 2 repeats; the stream run (`163159`) had all 3. Cause not found; looks intermittent.
- Stage 2 rewrites (EC17): the fixture's `decision_json` now always carries `note` (null when none), as the schema makes Gemini reply; `test_answer_llm.py` (one hand-written decide reply gets `"note": null`), `test_turn_budget.py` (latency of both calls measured), tooling `test_evals.py` (`run_decide_case` wrapper; `--reasoning-effort` dropped from the decide run; console comparison ignores measured latency; the all-errors case uses a non-retryable error).

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | stream merged usage and finish reason vs blocking call | spec | FR1, AC1 | pass (live, 2026-11-27) |
| T2 | 1 | tiny timeout fails before the first chunk, mapped by `to_llm_error` | spec | FR1, AC1 | pass (live: DeadlineExceeded -> LLMTimeoutError) |
| T3 | 1 | model timeout bounds the whole stream or not | spec | FR1, AC1 | pass (live: one deadline, cut at 3.0 s after 29 chunks) |
| T4 | 2 | a stream yields its text in order with the total usage (Gemini + fake) | spec | FR2, AC2 | pass |
| T5 | 2 | a stream fails before its first chunk, mapped to our error | spec | FR2, AC2 | pass |
| T6 | 2 | a stream fails after some text, mapped to our error | spec | FR2, AC2 | pass |
| T7 | 2 | the per-call timeout reaches a stream | spec | FR2, AC2 | pass |
| T8 | 2 | a fake stream without usage reports none; plain text streams, a stream script works blocking | inferred | fake parity | pass |
| T9 | 3 | one write script serves the chat model and the old provider in order | spec | FR3, AC3 | pass |
| T10 | 3 | the chat model routes decide, score and feedback-write by system prompt | spec | FR3 | pass |
| T11 | 3 | the summary goes to `llm.summary` with its limits | spec | FR3 | pass |
| T12 | 3 | a scripted error reaches the chat caller unchanged; usage, finish reason, budget cross over | code-derived | router conversions | pass |
| T13 | 4 | blocking mode writes with the JSON writer (plain and notes), rejects the streamed format | spec | FR4, AC4 | pass |
| T14 | 4 | blocking arms use v4 / v7_json / v8_json; `--blocking` flag parses | spec | FR4, AC12 | pass |
| T15 | 5 | a valid reply is the question with its usage; log line metadata only | spec | FR5, AC5, AC10 | pass |
| T16 | 5 | an invalid reply is retried once, then used; two invalid replies give no question | spec | EC2 | pass |
| T17 | 5 | a repeated question is an invalid reply | spec | FR5 | pass |
| T18 | 5 | an empty reply (`LLMBadResponseError`) is not retried | spec | EC2 | pass |
| T19 | 5 | a transport error is retried by the call layer only; a rejected request is not retried | spec | EC3 | pass |
| T20 | 5 | no call without time left; no call when the context is too large | spec | EC10, EC13 | pass |
| T21 | 5 | a follow-up takes the main question's category | spec | FR5 | pass |
| T22 | 5 | one generation per call with the write labels; profile writes stay redacted | spec | FR10, AC10 | pass |
| T23 | 6 | `--reasoning-effort` is refused for the write task | code-derived | the chat path has no per-call effort | pass |
| T24 | 8 | `ModelDecision` requires every field (gap, note nullable) | spec | FR6 | pass |
| T25 | 8 | a valid decision is used with its usage; log has action and gap, never the note | spec | FR6, AC6, AC10 | pass |
| T26 | 8 | a reply that breaks the schema is retried | spec | EC2 | pass |
| T27 | 8 | a schema-valid reply the parser rejects (gap rules) is retried; two give no decision | spec | EC14 | pass |
| T28 | 8 | a bad note is dropped, the decision kept, `note_dropped` logged | spec | EC14 | pass |
| T29 | 8 | an empty reply is not retried; a transport error is retried by the call layer only | spec | EC2, EC3 | pass |
| T30 | 8 | no call with only the write reserve left; never past the decide cap; no call when the context is too large | spec | EC10, EC13, FR6 | pass |
| T31 | 8 | one generation per call with the decide labels | spec | FR10, AC10 | pass |
| T32 | 8 | worst case 6 calls on the chat model; a transport error stops the reply loop | spec | FR12, AC9 | pass |
| T33 | 12 | text chunks, then the result with merged usage and finish reason | spec | FR7 | pass |
| T34 | 12 | a failure before the first chunk is retried; one that persists is ours, not `after_output` | spec | EC4 | pass |
| T35 | 12 | a failure after text is never retried and is flagged `after_output` | spec | EC5 | pass |
| T36 | 12 | the first chunk must come within its limit; a stream may run past that limit | spec | EC7 | pass |
| T37 | 12 | the vendor timeout is the time left in the turn (not LLM_TIMEOUT_SECONDS) | spec | spike, FR7 | pass |
| T38 | 12 | no call without time left; an empty stream is a bad response; a stream without usage still succeeds | spec | EC10, EC2, EC12 | pass |
| T39 | 12 | one generation per call with labels and usage; partial text on failure; `cancelled` when closed early | spec | FR10, AC10, EC8 | pass |
| T40 | 13 | closing early closes the Gemini stream too (within a few loop turns) | code-derived | LangChain doesn't close the inner stream | pass |
| T41 | 16 | `ModelScore` requires every field at every level | spec | FR8 | pass |
| T42 | 16 | a valid score reply is used with the score temperature and token cap | spec | FR8, AC8 | pass |
| T43 | 16 | a schema-breaking reply is retried; a made-up quote is rejected by the parser (second check) | spec | EC2, FR8 | pass |
| T44 | 16 | a cut-off reply is `truncated`; an empty reply keeps the `empty_reply` code | spec | EC2 | pass |
| T45 | 16 | a transport error is retried by the call layer, then fails | spec | EC3 | pass |
| T46 | 16 | `retry_skipped:no_time` on the score step; no call without time | spec | EC10 | pass |
| T47 | 16 | a valid write reply is used; two bad ones leave the template to the service | spec | FR8 | pass |
| T48 | 16 | generations carry task, attempt, prompt version, budget | spec | FR10, AC10 | pass |

Rewritten for the call layer (EC17), behavior kept: `test_start_llm.py` (transient errors now retried by the call layer; per-attempt timeout cap; blank reply logged as `LLMBadResponseError`; latency measured by the helper), `test_answer_llm.py` (enough scripted 503s for the retries), `test_turn_budget.py` (write budget read from its log line), `test_stream_answer.py` / `test_stream_turn.py` / `test_reference_note_context.py` (`chat_model=llm.chat`), `test_profile_redaction.py` (write traced through `TracerHandle`), `test_write_expired_deadline.py` (fake chat model), tooling `test_evals.py` / `test_rag_evals.py` / `test_generation_eval.py` / `test_generation_arms.py` (writer wrapped in `ProviderChatModel`; the error that every case hits is a non-retryable one, so the tests don't sit in backoff waits).

## Open Questions
- none blocking. Surfaced for the review: (1) the eval runners make one call per case through the app's call helpers rather than calling the app's `write()` / `decide()` / `stream_write()` loops (AC12 wording), so a retry can't hide an invalid reply from the score; (2) AC10's "feedback generations nest in their steps" was verified in Langfuse on the real run, not by a unit test (the fake tracer client doesn't model nesting); (3) AC4 and AC13: the baselines and several stage runs had 2 repeats in Langfuse instead of 3 (accepted, noted in each comparison file); (4) decide didn't "match" its baseline, it beat it, and became the new baseline row.

## Baseline Failures
- none

## Known Issues
- ctx_patch multi-line replaces silently do nothing on CRLF files (most of this repo's files); edits there use native Edit.
- Route tests that script a transient error now wait through the call layer's real backoff (up to ~1.5 s each); the suite went from ~58 s to ~63-66 s.

## Deviations from Plan
- Step 3 (how, not what): instead of feeding each `llm.script(...)` into two parallel fakes, the chat model delegates to the same scripted `FakeProvider` the old route uses. Same effect (one script serves both routes, `.calls` stays a plain list), less temporary code, and `.budgets` / `on_call` keep working. The bridge lives in `tests/provider_chat.py` (`ProviderChatModel`) so the tooling tests reuse it; it goes with the old classes. plan.md unchanged.
- Step 5 (wiring): `Interviewer` is built only when both models are present (`llm` and `chat_model`), not per task. Both come from the same LLM config, so they are on or off together; EC1 (LLM off: every task falls back) holds.
- Step 5 (logging, superseded by review R3): the `empty_reply` branch of `write` is gone. The call helper raises `LLMBadResponseError` for an empty reply, so it is logged as `outcome=LLMBadResponseError` with its finish reason. That is what production logged before too (the old provider raised the same error); only the `FakeProvider` ever reached the old branch.
- Step 6 (evals): `run_case` makes one `complete_chat` call per case rather than calling `write()`, because `write()`'s reply loop would retry an invalid reply and hide it from the score. The call path (chat model, call helper, tracing) is the app's. `--reasoning-effort` is refused for `--task write` (the chat model's thinking setting comes from the config).
- Step 8: `ModelDecision.note` is required but nullable (the prompt asks for a note every time; null keeps "no note" valid, as the parser allows). No `strict=True` (unlike `ModelProfile`): strict pydantic rejects the enum values as plain strings when the parser validates a dict. The old-style decide fake stays in the fixture as the router's backend (same reason as step 3); it goes in step 19.
- Step 9 (evals): `run_decide_case` keeps one call per case with the run's 30 s budget (the old provider's), not the app's 10 s decide cap, so timeouts don't skew the comparison with the baseline. `--reasoning-effort` is refused for `--task decide` too.
- Step 13 (EC8): LangChain's `astream` doesn't close the model's own stream when the caller stops early; asyncio's async-generator finalizer does, a few event-loop turns later (measured ~13 with the fake, ~15 with the Gemini integration). The old layer closed its HTTP stream at once. The outcome EC8 asks for holds (the vendor stream is closed, no more tokens), only a few loop turns later. The two client-left tests wait for it with a bounded `closed_soon` (`tests/provider_chat.py`) before their unchanged assertion, and `test_chat_stream.py::test_closing_early_closes_the_gemini_stream_too` pins it on the Gemini integration. Not chosen: calling the model's private `_astream` (deterministic close, but skips LangChain's metadata merge and callbacks).
- Step 13: the stream route keeps its retries before the first chunk in the call layer (`stream_chat`), so tests scripting one 503 before any text now script `1 + LLM_MAX_RETRIES` of them.
- Step 14 (evals): `run_stream_case` streams through `stream_chat` with the run's 30 s budget; `--reasoning-effort` is refused for `--task stream`.
- Steps 8 and 16 (order of checks): the parser runs first, then the schema check (`outcome.value is None` -> `invalid_reply:schema`). Running the schema first turned a non-JSON reply's precise `not_json` (and its hint) into `schema`. A reply the parser accepts but the schema doesn't still counts as invalid (FR6, FR8).
- Step 16: `ModelScore`'s top level ignores extra keys instead of refusing them, as `_RawScoreReply` ignores a stated `overall` (the code computes it); the nested models still forbid extras. The `empty_reply` failure code is kept for feedback (it is the stored failure reason and the hint's key), now raised by the call layer as `LLMBadResponseError`; the write and decide calls log that class instead (step 5). The feedback service drops `llm` entirely (it only fed the generator), one step before step 19.
- Step 19: `chat_model` takes the old `llm` positional slot in `InterviewsService` / `AnswerService` (the separate `chat_model=` keyword is gone), so call sites keep their order. `--reasoning-effort` is removed from the eval CLI rather than refused (no task can use it). The test bridge `tests/provider_chat.py` (`ProviderChatModel`, `closed_soon`) stays: the interview tests still script `FakeProvider`s through it; it goes with the old classes in U3c.

## Debug Log

## Review
Written by `/review-feature low` (2026-11-27). Scope: the uncommitted working tree against HEAD (the U3b1 work); the U3a commits already on this branch had their own review.

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | should-fix | project rules (guides cover all tasks) | docs/evaluation-guide.md:81 | The evaluation guide still lists `--reasoning-effort` as a flag of the interviews runner, but step 19 removed it from the CLI. Anyone following the guide gets an "unrecognized arguments" error. The row should go, or say that the chat model's thinking setting now comes from the config. | fixed |
| R2 | nit | reflection (stale text) | app/modules/interviews/tooling/interviews_evals.py:11 | The module docstring says the checks are unit-tested "with the fake provider"; since U3b1 they run on a fake chat model (`FakeChatModel`, or `ProviderChatModel` over scripted fakes). | fixed |
| R3 | nit | traceability (FR10) | app/modules/interviews/ai/interviews_write.py, interviews_decide.py | FR10 keeps the `empty_reply` log outcome, but write and decide now log an empty reply as `outcome=LLMBadResponseError` (with its finish reason); only feedback keeps `empty_reply`. Recorded as a deviation (it matches what production logged on the old provider), but reports that count `empty_reply` per task would undercount write and decide. | fixed |

Check results:
- `uv run --with ruff ruff check app tests` -> pass
- `uv run pytest -q` -> not re-run at level low: task.md records a green full-suite run on the final diff (2775 passed, 10 skipped, step 20)
- type checker, security scan, dependency audit, migration round-trip -> not run: low level (no migration in this diff; pyright on the changed files was run in step 19: 0 errors except a pre-existing one in an unchanged file)
- `code-review` (level low) -> no findings; partial coverage: it read the tracked diff of `app/` only, so the two new untracked files (`app/core/ai/chat_stream.py`, `app/modules/interviews/ai/interviews_model_schemas.py`) and the tests were not in it. Both new files were read by hand in this review: no finding.
- `security-review` -> not run: low level, and the diff adds no auth, permission, secret or new user-data surface
- `llm-security` (manual pass, LLM call code changed, no prompt file changed) -> no finding: the one new log line is metadata only; vendor errors leave as fixed-text `LLMError`s; partial stream text in traces honours the `redact` label; replies are still validated by schema and parser
- `simplify` -> not run: low level
- Project rules (layers, LangChain only in `core/ai/` and feature `ai/`, prompts in files, LLM output validated, evals for AI changes, no new dependency) -> pass except R1
- Traceability (AC1-AC15, EC1-EC17) -> every item has a passing test or a recorded verification (Test Cases table, Open Questions); R3 was the only wording gap

Fixes applied (2026-11-27, the user selected R1, R2 and R3): R1 removed the `--reasoning-effort` row from `docs/evaluation-guide.md`, added the `--blocking` row and a note that thinking comes from the config; R2 updated the docstring; R3 made `log_llm_error` (`app/modules/interviews/ai/interviews_turn_log.py`) log an `LLMBadResponseError` as `outcome=empty_reply` at WARNING, for write, decide and the streamed write (3 test assertions updated). After the fixes: `uv run --with ruff ruff check app tests` -> pass; `uv run pytest -q` -> 2775 passed, 10 skipped.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | ponytail, caveman | user request |
| 2, 5, 8, 12, 16 | tdd / test | `Test: first` steps: red before green at the plan's seams |
| stops | langfuse | reading runs, scores and observation nesting for the comparison files |

## Links
- Spec: docs/features/u3b1-interview-calls/spec.md
- Plan: docs/features/u3b1-interview-calls/plan.md
- Learnings: docs/features/u3b1-interview-calls/learnings.md
- Comparisons: docs/evals/u3b1-write-vs-baseline.md, u3b1-decide-vs-baseline.md, u3b1-stream-vs-baseline.md, u3b1-feedback-vs-baseline.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite + build green (2775 passed, 10 skipped; ruff pass)
- [x] Gate commands green on every step (the known flaky docx test failed twice in full runs and passed alone)
- [x] Every `/debug` invocation logged in Debug Log; no step left `blocked` (none was needed)
- [x] Every spec.md acceptance criterion met by code and covered by a passing test, or verified otherwise (AC1 live spike; AC10 nesting and AC13 evals in Langfuse)
- [x] Open Questions surfaced to the user (see Open Questions)
- [x] No skipped, deleted, or loosened tests; rewrites listed per stage (EC17)
- [x] task.md fully updated
- [x] learnings.md written; no pending measurements left
- [ ] Commits documented (the user commits; suggested messages above)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md: layers, LangChain only in `core/ai/` and feature `ai/`, no new dependency)
- [x] No unresolved plan deviations (all recorded in Deviations from Plan)
