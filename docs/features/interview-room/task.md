# Implementation: Interview Room (backend)

## Status
Ready for review (all 10 steps done; the backend half of the feature; the FE plan comes next)
Health Check: missing: caveman -> fallback: normal chat; missing: verification-before-completion -> fallback: the gate-command rule. Review: missing: verification-before-completion -> fallback: gate commands and results listed in Review.
Branch: `feat/rag-integration` (current branch, as the user asked; no new branch)

## Completed Steps
- [x] 1. Layer rule: `core` never imports `modules`. `check_core` plus 3 tests in `tests/test_layers.py`; 12 passed. Suggested commit: `test(layers): forbid app/core from importing feature modules`
- [x] 2. Shared async retry helper + `Transcriber` contract test. `run_with_retries` / `Attempted` in `core/ai/retry.py`; `DeepgramTranscriber` uses it; 5 helper tests and 4 contract tests (fake + Deepgram); `tests/core/ai` 202 passed, `test_deepgram.py` unchanged. Suggested commit: `refactor(ai): share one async retry loop across Deepgram adapters; add speech contract tests`
- [x] 3. Move audio rules and limiters into `core/speech`. New `core/speech/{audio,limits}.py`; `get_transcriber` is now in `core/ai/dependencies.py` (re-exported); the test moved to `tests/core/speech/test_audio.py` (imports only). Suggested commit: `refactor(speech): move audio rules and the transcription limiter into core/speech`
- [x] 4. Gateway `transcribe`. `core/speech/gateway.py` (checks, 503 mapping, generic `log_fields`, one `app.stt` line); the service only passes keyterms, the cap and its ids; 15 gateway tests; `test_transcribe.py` passes unchanged (one import line). Suggested commit: `refactor(speech): add the speech gateway; interviews only passes its own rules`
- [x] 5. Rename to `interviews_voice_*`. `VoiceService` / `VoiceController` / `VoiceControllerDep`; no old names left. Suggested commit: `refactor(interviews): rename the transcription adapter to interviews_voice`
- [x] 6. `SpeechSynthesizer`, Aura adapter, grouped speech settings. `core/ai/synthesizer.py`; `DeepgramSynthesizer` (`v1/speak`, retry helper, content type from the response with an encoding fallback, empty or non-audio → bad response); `FakeSynthesizer`; the `Settings.speech` group (env names unchanged); `build_synthesizer`, `get_synthesizer`, lifespan; `.env.example`. Suggested commit: `feat(ai): add the SpeechSynthesizer protocol and the Deepgram Aura adapter with grouped speech settings`
- [x] 7. Phase 0 spike: `tests/live/test_deepgram_aura_live.py` (opt-in `SPEECH_LIVE_TEST=1`). Results below; the default voice is now `aura-asteria-en` (the user's choice). Suggested commit: `test(live): add the opt-in Aura speech spike; default to the faster Aura 1 voice`
- [x] 8. Gateway `synthesize`, `SPEECH_UNAVAILABLE`, speech limiter. `gateway.synthesize` (None or vendor error → 503, one `app.tts` line from generic fields, never the text); `SpeechUnavailableError`; `SPEECH_PER_MINUTE = 30` / `SPEECH_LIMITER`; 9 new gateway tests. Suggested commit: `feat(speech): add gateway synthesize, SPEECH_UNAVAILABLE and the speech rate limiter`
- [x] 9. Speech routes + interview voice adapter.
  - `get_shown_question` / `get_interviewer_reaction` (repository); `VoiceService.question_text` / `reaction_text` / `speak` (uniform 404, no status check, the text only from the DB); `VoiceController.speak` (media type from the result, `Cache-Control: private, no-store`); `limit_speech` / `get_speech_limiter`.
  - Two `GET .../speech` routes; the `tts` / `speak` fixtures; 20 route tests.
  - Suggested commit: `feat(interviews): speak stored questions and reactions through two speech routes`
- [x] 10. Final gates + graph. Full suite 2445 passed / 7 skipped / 1 baseline failure; ruff 18 (one existing error fixed); the decoupling greps are clean; `graphify update .` run.

## Current Step
### Done. Next: `/review-feature`

## Changes Made
- (the user commits manually; a suggested message is given per step)

## Test Results
Baseline: 2366 passed, 6 skipped, 1 failed (see Baseline Failures).
After Step 5: 2393 passed, 6 skipped, 1 failed (the same baseline test); ruff 19 errors (unchanged from the baseline).
After Step 8: 2427 passed, 7 skipped (+ the opt-in live test), 1 failed (the same baseline test); ruff 19 errors.
Final (Step 10): 2445 passed, 7 skipped, 1 failed (the same baseline test); ruff 18 errors (the `interviews_repository.py` I001 was fixed). The live Aura test passed with `SPEECH_LIVE_TEST=1`.
Ruff cleanup (2026-11-15, the user's request before review): **0 errors**. 9× BLE001 in `tracing.py` annotated with the repo's `# noqa: BLE001  <reason>` convention (the catches are the module's deliberate fail-open design); `test_tracing.py` C408/SIM117 rewritten; 7 import-order and quote fixes by `ruff --fix`. Full suite unchanged: 2445 passed, 7 skipped, 1 baseline failure. Suggested commit: `chore(lint): clear the remaining ruff errors (annotate tracing's fail-open catches)`

## Phase 0 spike results (2026-11-15, real Deepgram key, from this machine)
Command: `SPEECH_LIVE_TEST=1 uv run pytest tests/live/test_deepgram_aura_live.py -q -s` (adapter, buffered), plus a throwaway time-to-first-byte script (not committed).

| Voice / encoding | 43 chars | 72 chars | 114 chars (longest bank question) | Notes |
|---|---|---|---|---|
| `aura-2-thalia-en` mp3, adapter, cold start | 1597 ms | 2112 ms | 3199 ms | the first call includes opening the connection |
| `aura-2-thalia-en` mp3, warm, whole clip | 805 / 900 ms | — | 2129 / 1950 ms | MP3 arrives all at once (first byte ≈ whole clip), so streaming wouldn't help |
| `aura-2-thalia-en` linear16, warm | first byte 303 ms, whole clip 984 ms | — | first byte 307 ms, whole clip 2127 ms | streams, but ~8× bigger (322 KB) |
| `aura-asteria-en` mp3, warm, whole clip | 336 / 329 ms | — | 339 / 535 ms | **chosen** |
| `aura-asteria-en` mp3, adapter, cold start | 1049 ms (includes connecting) | 512 ms | 328 ms | the spec target holds (under 1 s typical, 2 s max) |

- Format: `audio/mpeg` (mp3) confirmed in the response `Content-Type`; clips are 14–36 KB.
- The default voice changed from the planned `aura-2-thalia-en` to `aura-asteria-en` (the user's decision; Aura 2 missed the 2 s target for the longest questions). Switching back is one env var: `DEEPGRAM_TTS_MODEL`.
- The `tests/conftest.py` guard now keeps the Deepgram key only when `SPEECH_LIVE_TEST=1`, mirroring `LLM_LIVE_TEST`.

## Tests Pending
- Step 7, user checks (can't be done from here): play the three clips in Chrome and Safari (including iOS); confirm Aura's price per character against the starter credit and Deepgram's data-use terms for TTS input; set a usage alert in the Deepgram console.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | core importing `app.modules` is reported; the real core is clean | spec | AC17 | pass |
| T2 | 2 | retry helper: one attempt, retry then success, non-retryable, max retries, budget | spec | plan Step 2 | pass |
| T3 | 2, 6 | fake and real adapter pass the same contract (STT + TTS) | spec | AC17 / Decoupling rules | pass |
| T4 | 4 | gateway transcribe: cap/trim, unavailable, each vendor error, no speech, too long, bad upload, one log line | spec | voice-answers (unchanged) | pass |
| T5 | 6 | Aura request shape, content type from the response or the encoding, retries, 4xx, timeout, non-audio 200 | spec | Phase 1 | pass |
| T6 | 6 | the `speech` settings group, defaults, bounds, `.env.example` | spec | Decoupling rules | pass |
| T7 | 8 | gateway synthesize: result, unavailable, each vendor error, one log line with no text | spec | AC11, EC3 | pass |
| T8 | 9 | question / follow-up / reaction spoken from the stored text; media type from the result | spec | AC11 | pass |
| T9 | 9 | a finished interview can still be replayed | spec | EC13 | pass |
| T10 | 9 | every miss is the same 404 (stranger, unknown, other session, not shown, candidate answer, wrong route) | spec | EC22 | pass |
| T11 | 9 | 503 with no synthesizer or on a vendor failure; 429 + Retry-After shared by both routes, separate from STT; 401 | spec | EC3, EC4 | pass |
| T12 | 9 | client-sent text is ignored; no line text in the logs | inferred | security: text only from the DB | pass |
| T13 | 7 | live Aura: three lines, `audio/mpeg` | spec | Phase 0 | pass (opt-in) |

## Open Questions
- none

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: expects `llm_max_tokens == 800`, the default is 4000. Unrelated to this feature.
- ruff: 19 existing errors (in `tracing.py`, `interviews_repository.py` I001, and several test files). Gate = **no new ruff errors**. All of them were cleared after Step 10 at the user's request (see Test Results).
- Flaky (intermittent, order-dependent, outside speech code): `tests/modules/interviews/routes/test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` (failed alone once, then passed alone and in two module-level runs); `tests/modules/profile/utils/test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table` (failed once in a full run, passes alone). Neither touches retry, Deepgram or speech code.

## Known Issues
- none

## Deviations from Plan
- Step 3: the plan listed `tests/core/speech/__init__.py`, but `tests/core/` has no `__init__.py` files (rootdir imports), so none was added. No behaviour impact.
- Step 3: `git mv` staged the test move; it was unstaged at once with `git restore --staged` (the repo rule: never stage). Later moves use plain `mv`.
- Step 7: the default voice is `aura-asteria-en` (Aura 1), not the planned `aura-2-thalia-en`. The spike measured Aura 2 at ~2 s for the longest question (warm), which misses the spec's 2 s target; Aura 1 takes ~0.3–0.5 s. Approved by the user (2026-11-15). The plan said "to be confirmed in Step 7", so this is the confirmation; plan.md is updated.
- Step 7: `tests/conftest.py` blanks `DEEPGRAM_API_KEY` for every test unless `SPEECH_LIVE_TEST=1` (the plan didn't foresee that the existing guard would block the opt-in live test).
- Step 9: the "question not shown yet" test inserts the upcoming row by hand. Today each question is stored only when it is shown, so the API can't create one; the guard (`position <= current_position`) is kept as the spec's no-leak rule. The assertion is unchanged.
- Step 9: the speech responses carry `Cache-Control: private, no-store` (not in the plan): the clip is one user's interview data, and the FE keeps its own in-memory replay cache.

## Debug Log

## Review
Written by `/review-feature` (2026-11-15). Scope: the uncommitted working tree against `HEAD` on `feat/rag-integration`. That's this feature only; the branch's 34 earlier commits vs `main` belong to other features. `graphify-out/` was excluded. Health Check: missing: verification-before-completion -> fallback: each gate command and its real result shown below.

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | should-fix | code-review (verified) | app/modules/interviews/services/interviews_voice_service.py:72 | `question_text` / `reaction_text` read the DB but never call `repo.release()`, so the read transaction and its pooled connection stay open while Deepgram synthesizes (up to the 10 s budget). The answer, feedback and start services release before their vendor calls. Under concurrent playback this can exhaust the pool and stall unrelated requests. (`prepare_transcription` has the same gap from before this feature.) | fixed |
| R2 | should-fix | manual (plan Step 9 slice f) | app/modules/interviews/services/interviews_voice_service.py:29 | The 404 bodies differ: a session miss returns "Interview not found" (from `owned_session`), a line miss returns "Interview line not found". The plan says every miss has the same generic body; the tests compare only the code, so they missed it. The leak is small (it only separates "your session, wrong line" from "no such session of yours"), but it contradicts the contract. | fixed |
| R3 | should-fix | code-review | app/modules/interviews/routes/interviews_route.py:317 | The route gets the text from `ctrl.question_text` and hands it back into `ctrl.speak`. `VoiceService.speak` accepts any `text`, so "never speak request text" is a convention held by the route, not a rule enforced by the service. One service method per line kind (look up, release, synthesize) would enforce it, and also fixes R1. | fixed |
| R4 | should-fix | code-review (verified) | app/core/ai/deepgram.py:211 | Only `TimeoutException` / `TransportError` are mapped to `LLMError`. Other httpx `RequestError`s (e.g. `DecodingError`, which isn't a `TransportError`, verified) escape the gateway as an unhandled 500 instead of `SPEECH_UNAVAILABLE`. The transcriber has the same gap. | fixed |
| R5 | nit | code-review | app/core/speech/gateway.py:100 | `outcome` changes only in `except AppError`, so an unexpected exception logs `outcome=ok` (both `transcribe` and `synthesize`; the pattern came from the old service). | fixed |
| R6 | nit | code-review | app/core/ai/retry.py:41 | With 8 s per attempt and a 10 s budget, a retry after a timeout gets only about 1.2 s. That's enough for Aura 1 (~0.3–0.5 s), but it can be a wasted paid call for slower voices. `retry_delay` doesn't check that enough time remains for a useful attempt. | open |
| R7 | nit | code-review | app/modules/interviews/routes/interviews_route.py:303 | `limit_speech` runs before the ownership check and the "no synthesizer" 503, so 404s and 503s count against the quota. That matches the existing transcription design ("checked before anything that costs money") and is kept by intent. | open |
| R8 | nit | code-review | app/modules/interviews/routes/interviews_route.py:295 | The OpenAPI 200 response lists only `audio/mpeg`; the real type follows `DEEPGRAM_TTS_ENCODING`. The description says to read the Content-Type. | open |
| R9 | nit | code-review / simplify | app/modules/interviews/dependencies/interviews_voice_dependencies.py:50 | `limit_speech` is a near copy of `limit_transcriptions` (and of the job-import limiter); one small factory would remove the copies. | fixed |
| R10 | nit | code-review / simplify | app/core/ai/deepgram.py:141 | `DeepgramSynthesizer` repeats `DeepgramTranscriber`'s constructor and opens a second `AsyncClient` to the same host. | fixed |
| R11 | nit | code-review | app/modules/interviews/controllers/interviews_voice_controller.py:37 | `Cache-Control: private, no-store` stops browser caching, so a reload or new tab re-synthesizes (and re-bills) lines that never change. `private, max-age=…` or a small server-side cache would avoid that; the spec only requires one fetch per visit. | open |
| R12 | nit | simplify | tests/live/test_deepgram_aura_live.py:26 | `EXPECTED_TYPES` duplicates `SPEAK_CONTENT_TYPES`, and `SpeechEncoding` (config) and `SPEAK_CONTENT_TYPES` (deepgram) list the encodings twice with nothing keeping them in step. | fixed |
| R13 | should-fix | traceability (AC16) | tests/core/test_config.py:70, tests/modules/interviews/routes/test_turn_budget.py:133 | AC16 requires "BE tests pass", but 2 existing tests fail: `test_llm_settings_default_to_off_with_documented_limits` (expects `llm_max_tokens == 800`, the default is 4000; needs the user's call) and `test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`. The second reads the real clock, so it asserts `budget_left_ms=30000` and gets 29998 whenever ≥1 ms passes; now deterministic on this machine. Both predate this feature and are outside its code, but they block a green suite. **Fix pass:** the config test now expects 4000 (the user's decision). The turn-budget test wasn't selected and stays timing-fragile: it passed in the post-fix full run, but needs the fake clock to be reliable. | open (partly fixed) |

Fix pass (2026-11-15, the user selected R1, R2, R3, R4, R5, R9, R10, R12 and the R13 config test):
- R1 + R3: `VoiceService.prepare_question_speech` / `prepare_reaction_speech` check access, copy the text into a `SpeakableLine` and call `repo.release()`; `speak(user, line)` accepts nothing else. `prepare_transcription` releases too. Regression test: `test_the_lookup_ends_its_db_transaction_before_the_slow_synthesis`.
- R2: every miss says "Interview not found" (the same as `owned_session`). Regression test: `test_every_miss_has_the_same_body`.
- R4: both adapters map every `httpx.RequestError` to `LLMServerError` (in the shared `_post`). Regression tests: `test_any_other_request_failure_is_a_server_error_not_a_crash`, `test_any_other_speak_request_failure_is_a_server_error_not_a_crash`.
- R5: unexpected exceptions log `cause=<type> outcome=error` and are re-raised. Regression test: `test_an_unexpected_error_is_logged_as_an_error_and_still_raised`.
- R9: `_per_user_limit(get_limiter, message)` builds `limit_transcriptions` and `limit_speech` (the job-import limiter is outside this feature and was left as is).
- R10: the `_DeepgramAdapter` base holds the client, retry knobs, the retry loop and the request-error mapping; each adapter keeps only its request and parsing. Two clients stay, by design (independent lifecycle; noted in the docstring).
- R12: `SPEAK_CONTENT_TYPES` is keyed by `SpeechEncoding`, the live test imports it, and `test_every_configurable_encoding_has_a_media_type` keeps the two in step.
- Left open by choice: R6, R7 (intended), R8, R11, and R13's turn-budget test.
- Gates after the fixes: `uv run pytest -q` -> **2453 passed, 7 skipped, 0 failed**; `ruff check app tests` -> All checks passed!; the live Aura test (`SPEECH_LIVE_TEST=1`) passed with the refactored adapter (asteria: 2140 ms cold, 337 / 373 ms warm).
- Suggested commit: `fix(speech): release the DB before synthesis, one 404 body, map all request errors; share Deepgram adapter setup`

Security pass (applied directly; the `security-review` skill reviews the cwd repo's branch, which is the FE): text only from the DB ✓, ownership in the service ✓, a uniform 404 code (body: R2), no upcoming-question leak ✓ (`test_a_question_not_shown_yet_is_not_found`), per-user limit ✓, no text/audio/key in logs ✓, secrets from env with `SecretStr` ✓. No other findings beyond R1–R4.
LLM-security: not run, no LLM call or prompt changed. TTS input is stored interviewer text only (questions, predefined reactions); no candidate data goes to Deepgram's speak endpoint.

Project-rules checklist (CLAUDE.md): layer direction ✓ (`tests/test_layers.py`, plus the new `core` rule); UUID ids ✓; structured errors ✓; no PII in logs ✓; rate limiting ✓; config/secrets from env, `.env.example` updated ✓; provider abstraction ✓; vendor mocked in unit tests, live test opt-in ✓; no new dependency ✓; no migration needed ✓; `response_model` on every route: the speech routes use `response_class=Response`, since a binary body can't have a Pydantic model (compliant in spirit; see R8).

Traceability: AC11 ✓ (T7, T8, T10, T11); AC17 BE half ✓ (T1, T3, the decoupling greps); EC3 ✓, EC4 ✓, EC13 ✓, EC22 ✓ (code only; body: R2); AC16 BE half ✗ → R13. FE-only IDs are out of scope for this repo.

Check results:
- `uv run pytest -q` -> 2444 passed, 7 skipped, 2 failed (R13; both predate this feature)
- `uv run --with ruff ruff check app tests` -> pass (All checks passed!)
- `tests/test_layers.py` (layer + core rules) -> pass
- type checker -> not run: no pyright/mypy in the project or its venv (installing one needs the user's permission)
- static security scan -> not run: no bandit/semgrep available
- dependency audit -> not run: no dependency changed (`pyproject.toml` / `uv.lock` untouched)
- migration round-trip -> not run: no model or Alembic change
- live Aura (`SPEECH_LIVE_TEST=1`) -> pass (run during Step 7, and again after the fix pass)

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1–5 | tdd / test | Red → green per slice at the confirmed seams (`check_core`, `run_with_retries`, the protocol contract, gateway `transcribe`) |
| 1–5 | ponytail | Gateway as functions; no extra `__init__` files; the retry helper limited to the Deepgram adapters |
| 1–5 | lean-ctx / graphify | Exploration reused from plan.md (graphify STT cluster); shell runs through ctx_shell |
| 6–9 | tdd / test | Red → green at the confirmed seams (`DeepgramSynthesizer`, the contract, gateway `synthesize`, the HTTP routes) |
| 9 | security-review (applied directly) | Text only from the DB, uniform 404, no upcoming-question leak, per-user limit, no text in logs, `no-store` |
| — | find-skills | Not needed: every step used installed skills and existing project patterns |

## Validation (backend half)
- [x] All plan.md steps complete
- [x] Full suite green apart from the recorded baseline failure; no build step for this repo
- [x] Gates green on every step (ruff never above the baseline)
- [x] No `/debug` invocations needed
- [x] BE ACs met: AC11 (T7, T8, T10, T11), AC16 BE half (Step 10), AC17 BE half (T1, T3, the greps); EC3, EC4, EC13, EC22 covered
- [x] No skipped, deleted or loosened tests (the one test-setup fix is in Deviations)
- [x] learnings.md written; the pending items match Tests Pending (user browser and pricing checks)
- [ ] Commits: the user commits manually (suggested messages per step above)

## Links
- Spec: ../cuewise-fe/docs/features/interview-room/spec.md
- Plan: docs/features/interview-room/plan.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete
- [ ] Full test suite + build green (not just per-step tests)
- [ ] Gate commands green on every step (or `gate: none found` recorded)
- [ ] Every `/debug` invocation logged in Debug Log; no step left `blocked`
- [ ] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (or verification noted)
- [ ] Open Questions resolved or explicitly surfaced to the user
- [ ] No skipped, deleted, or loosened tests; baseline failures listed separately
- [ ] task.md fully updated
- [ ] learnings.md written; pending measurements marked and matching Tests Pending
- [ ] Commits documented
- [ ] No open blockers
- [ ] Code follows project rules (or N/A)
- [ ] No unresolved plan deviations
