# Implementation: SSE Streaming of the Interview Turn (Slice 4)

## Status
Code complete and tested (Steps 0-15). Step 16 partly done: the learnings are written and one real-model eval repeat was
run; the 3-repeat v4 vs v5 comparison and a live-interview measurement are left to the user (see Open Questions).

## Completed Steps
- [x] 0. Rename the provider (`OpenAICompatibleProvider`); per-vendor config (`LLM_PROVIDERS`, `LLM_GOOGLE_*`)
- [x] 1. Add `sse-starlette` (3.6.0)
- [x] 2. Event contract (`TurnPhase`, `StreamEvent`, event schemas, `sse_frame`/`sse_frames`)
- [x] 3. Extract the shared turn pieces (`plan_write`, `settle`)
- [x] 4. Split the controller (`prepare_answer`, `finish_answer`, `choose_reaction`)
- [x] 5. `Interviewer.stream_turn`
- [x] 6. `InterviewsController.stream_answer`
- [x] 7. Stream route `POST /interviews/{id}/messages/stream` (OpenAPI documents the events)
- [x] 8. Streaming test helpers (`stream_answer` fixture, SSE parser, `anyio_backend`)
- [x] 9. Provider stream contract (`stream`, `aclose`, `after_output`)
- [x] 10. `OpenAICompatibleProvider.stream`
- [x] 11. `FakeProvider.stream` (`FakeStream`, `cancelled`, `stream_format`)
- [x] 12. `interviewer_v5`, the `interviewer_stream` task, `split_header` / `parse_streamed_reply`
- [x] 13. Streamed write step (deltas, reset, retry or bank, cancellation)
- [x] 14. The event loop stays free (AC16 test)
- [x] 15. Evals: `--task stream` (v5, time to first token)
- [ ] 16. Measure, document, finish: learnings, progress line, lint, full suite and `graphify update .` done. The 3-repeat comparison and the live interview are still open.

## Changes Made
- Not committed (the user commits manually). Suggested commits, in order:
  1. `refactor(ai): vendor-neutral OpenAICompatibleProvider and LLM_PROVIDERS / LLM_<VENDOR>_* config`
  2. `feat(interviews): stream an answer turn as SSE with progress events (sse-starlette)`
  3. `feat(interviews): stream the question token by token with interviewer_v5 and an async provider stream()`

## Test Results
- Baseline before Step 0: 701 passed, 1 skipped, 2 failed (see Baseline Failures).
- After Phase A: 754 passed, 1 skipped, 1 failed (baseline).
- Final: **812 passed, 1 skipped, 1 failed**. The failure is the baseline `llm_max_tokens` default; the `.env.example`
  baseline failure is fixed by Step 0.
- Lint: `uvx ruff check` is clean on every changed file. The repo has no ruff config, and 7 untouched files still have
  their earlier import-order findings plus one RUF012 in `app/core/errors.py`. `ruff format` was not run: it would rewrap
  the whole repo to 88 columns.
- Real model (`gemini-3.5-flash-lite`): one live `stream()` call confirmed that usage arrives with
  `stream_options.include_usage`. `--task stream --repeat 1` passed 19/19, with an average time to first token of 2,001 ms.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 0 | listed provider with its block is configured; unknown / duplicate / incomplete refused; removed names refused, no secret in errors | spec | Step 0 | pass |
| T2 | 0 | factory builds `OpenAICompatibleProvider`; `--model` override | spec | Step 0 | pass |
| T3 | 5, 13 | stream_turn order, follow-up action after its write, fallback, completion, decide failure, parity with `answer_turn` | spec | AC4, EC12-EC15 | pass |
| T4 | 6, 7 | stream headers; JSON route unchanged | spec | AC1 | pass |
| T5 | 7 | 401/403/404/409/422 as JSON before the stream | spec | AC2, EC1-EC4 | pass |
| T6 | 6 | event order, one terminal event, `done` equals the JSON body, same saved rows | spec | AC3-AC5, AC9 | pass |
| T7 | 6 | two tabs race: one `done`, one `error QUESTION_NOT_CURRENT` | spec | AC7, EC5 | pass |
| T8 | 6 | failed save / crash: one generic error event, nothing saved, no text leaked | spec | AC8, EC17, EC18 | pass |
| T9 | 6 | first event before any LLM call returns; summary is metadata only | spec | AC10, AC17 | pass |
| T10 | 6, 13 | leaving during deciding / writing saves nothing; provider stream cancelled and logged | spec | AC6, AC15, EC6 | pass |
| T11 | 7 | heartbeat comments during a long wait | spec | EC19 | pass |
| T12 | 10 | provider stream: order, usage, retry only before the first chunk, after-output flag, error chunk, timeout, budget, blank, 4xx, bad JSON | spec | AC11 | pass |
| T13 | 12 | header split across chunks, tolerant header, missing/unknown/JSON/fenced header, early fail, v4 reasons, prompt sections | spec | AC12, EC11 | pass |
| T14 | 13 | deltas join to the saved question, no category; reset then retry or bank; failure before text needs no reset | spec | AC13, AC14, EC7-EC11 | pass |
| T15 | 14 | `/health` served while a stream waits | spec | AC16 | pass |
| T16 | 15 | streamed eval checks, first token, summary average, `--task stream` | spec | AC18 | pass |
| T17 | 12 | `CATEGORY:` header tolerates case and spaces | inferred | risk: model formatting | pass |
| T18 | 0 | blank `LLM_PROVIDERS` and blank old names mean LLM off, not an error | inferred | risk: hand-edited .env | pass |

## Open Questions
- AC18: run the 3-repeat comparison (`--task write --repeat 3` for v4, `--task stream --repeat 3` for v5), pausing
  between runs for the free-tier rate limit, and record it in `learnings.md`. -> needs: the user (real API quota).
- AC19: the time to first token in a live interview through the stream endpoint. The eval measured 2,001 ms on average
  against the 1 s target (7/19 under it). With a ~30-token question, time to first token is mostly queueing and prefill,
  not generation. -> needs a decision from the user: accept the progress events as the latency fix, or tune the
  input/model.
- `llm_max_tokens` default: the code says 4000 and the test expects 800 (baseline failure). -> needs a decision from the
  user: which is intended.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: it expects `llm_max_tokens` to
  default to 800, but the code default is 4000. Still failing; not changed by this feature.
- (fixed by Step 0) `test_env_example_lists_every_llm_setting`: `.env.example` listed `GROQ_API_KEY`.

## Known Issues
- **Your `.env` must be migrated before the app starts.** Add `LLM_PROVIDERS=google`, then rename
  `OPENROUTER_API_KEY` → `LLM_GOOGLE_API_KEY`, `LLM_MODEL` → `LLM_GOOGLE_MODEL` and `LLM_BASE_URL` →
  `LLM_GOOGLE_BASE_URL`. The old names now refuse to start, with a message naming the new ones.
- The shell that launched this session exports the old LLM variables (process level only). A new shell that loads
  `.env` will need the new names too.
- The `reasoning` request field is OpenRouter's syntax; Google's endpoint may ignore or reject it. This is unchanged here
  and noted for the multi-provider work.
- Google's mid-stream error format was not observed live; both an error chunk and a dropped connection are handled and tested.

## Deviations from Plan
- Recorded in `plan.md` → "Deviations Found During Implementation":
  - `--task stream` instead of `--prompt v5`;
  - `WindowLedger(text_replies=True)` for v5;
  - no partial usage on errors after output;
  - `FakeProvider(stream_format=...)`;
  - the test conftest blanks the developer's LLM variables;
  - `Cache-Control: no-store`.
- Approved by: implementation findings, within the spec's requirements; flagged to the user in the summary.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | lean-ctx | reads, searches, patches, test runs |
| 1, 7 | (source reading) sse-starlette 3.6 | verified disconnect → generator cancel + `aclose`, its headers and ping |
| 6 | (source reading) FastAPI 0.162 routing | verified `get_db` (request-scoped yield dependency) closes after the streamed response |
| 16 | graphify | `graphify update .` after the code changes |

## Links
- Spec: docs/features/sse-streaming/spec.md
- Plan: docs/features/sse-streaming/plan.md
- Learnings: docs/features/sse-streaming/learnings.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete (Step 16's 3-repeat eval and live interview are open)
- [x] Full test suite green apart from the recorded baseline failure (no build step in this project)
- [x] Every spec.md acceptance criterion is met by code and covered by a passing test, except AC18 and AC19, which need real runs (see Open Questions)
- [x] Open Questions surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [x] Commits documented (suggested; none made)
- [ ] No open blockers (the `.env` migration is required before running the app)
- [x] Code follows project rules (root `CLAUDE.md`)
- [x] Plan deviations recorded in plan.md and task.md
