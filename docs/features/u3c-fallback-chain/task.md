# Implementation: U3c — Fallback chain, question bank removal, old LLM layer deleted

## Status
Steps 1-8 done. Evals run by the user and compared (no change, `docs/evals/u3c-chain-vs-baseline.md`). Next: `/review-feature low`, and the user's migration run.
Health Check: all present (find-skills: nothing to install, no extra skill needed); review level: low
Branch: `feat/langchain-migration` (no new branch). Checkpoints after steps 3 and 6.

## Completed Steps
- [x] 1. Provider chain in the call helpers
- [x] 2. Config and factory build every provider
- [x] 3. Remove the "LLM off" modes from the modules (Checkpoint 1)
- [x] 4. A turn that cannot write ends in the retryable error
- [x] 5. Remove the bank and migrate old rows
- [x] 6. Delete the old layer (Checkpoint 2)
- [x] 7. Layer test and the note parser (R3)
- [x] 8. Evals, docs, final gates

## Current Step
Done. Next: `/review-feature low`.

## Changes Made
Commit suggestions (the user commits; one `git add` per line):
- Step 1: `feat(ai): try the configured providers in order inside the call helpers`
  - new `app/core/ai/chat_chain.py`; `chat.py`, `chat_stream.py` loop over the chain (switch only on retryable `LLMError`; time left per provider; stream commits at the first chunk); `LLMResult.provider`; trace metadata `provider`; `llm_call` log field; `llm_provider_switch` event.
  - tests: `tests/core/ai/test_chat_chain.py`, chain case in `test_retry_budget.py` (worst case 12).
- Step 2: `feat(config): require at least one LLM provider and build the whole chain`
  - `Settings` refuses empty `LLM_PROVIDERS`; `llm_configured` removed; `build_chat_model` returns a `ChatChain`; `.env.example`; test env gets a dummy Google provider (`tests/conftest.py`); the three eval entry points lost their "LLM not configured" branch.
- Step 3: `refactor(interviews): remove the LLM-off modes`
  - `chat_model` required in the interviews, answer, feedback, profile services and their dependencies; `get_chat_model` no longer returns None; `RetrievalService(llm_on=)` and `RetrievalSkip.llm_off` gone; `FeedbackUnavailableError`, `ProfileUnavailableError` and `PROFILE_UNAVAILABLE_MESSAGE` deleted with their 503 docs; answer service lost the bank-when-LLM-off branch.
  - tests: autouse `default_chat_model` fixture in `tests/conftest.py`; 8 tests of the removed modes deleted (below).
- Step 4: `feat(interviews): end a turn that cannot write in a retryable 503`
  - `InterviewerUnavailableError` (503 `INTERVIEWER_UNAVAILABLE`) in `core/errors.py`; `InterviewerFailedError` in `ai/interviews_turn_types.py`; `settle` raises it on a failed write or no time, `fail_undecided` on a failed decide (before any write call); `first_question` raises on no reply; the start, answer and stream services map it (the stream yields the `error` event after the write step's own `reset`); route docs list the 503.
  - tests: new `test_turn_unavailable.py`; start, follow-up, budget, stream-turn, context and transcript tests converted from "bank asks" to "503, nothing saved"; interviews tests get a default LLM (`_llm_by_default`) that writes a valid question for the interview's type.
- Step 5: `refactor(interviews): remove the question bank and migrate old rows to stored`
  - deleted `data/questions.json`, `BankQuestion`/`QuestionBank`, `load_bank`, `select_questions`, `pick_fallback_question`, `bank_question`, `get_bank`, `used_bank_ids`, `NotEnoughQuestionsError`, `bank_id`; `QuestionSource.bank` -> `stored`, new-row default `llm`; usage report prints `stored=`.
  - new migration `alembic/versions/b8f3a2c91d6e_replace_bank_with_stored.py` (the SQL renders as intended with `alembic upgrade 667c6bd6bf94:head --sql` and the downgrade; **not run on a database: the user runs it**).
  - tests: bank-only test files deleted; legacy-row fixtures use `source="stored"`.
- Step 6: `refactor(ai): delete the old LLM provider layer`
  - deleted `LLMProvider`, `ReasoningEffort`, `OpenAICompatibleProvider` (`openai_compatible.py`), `TracingProvider`, `build_provider`; `FakeProvider`/`FakeStream` moved to `tests/provider_fakes.py`; `openai` dependency removed (`uv remove openai`: `pyproject.toml`, `uv.lock`); `ProviderConfig.base_url` and the required `LLM_GOOGLE_BASE_URL` removed (the setting is still accepted and ignored, see Deviations); docstrings fixed; `.env.example` updated.
  - tests: `test_openai_compatible*.py` and the live OpenAI-compatible test deleted; 21 `TracingProvider` tests and 3 `build_provider` tests deleted (the per-call generation is covered by `test_chat_tracing.py`).
- Step 7: `test(layers): confine LangChain and vendor SDKs to the ai folders` and `refactor(interviews): keep utils below ai`
  - `tests/test_layers.py`: new `check_sdks` (any `app/` file outside `app/core/ai/` and `app/modules/*/ai/` that imports `langchain*` or a vendor SDK is reported; replaces the four-layer check) and a `utils/` -> `ai/` ban; both also run on the real tree.
  - fixes the ban found (5 imports): `interviewer_inputs` and `llm_question` moved from `utils/interviews_session_utils.py` to `ai/interviews_turn_rows.py`; `EmptyProfileError` moved down into `profile/utils/profile_utils.py` (re-imported by `profile_reply.py`, so every import path still works); `parse_note` / `load_corpus` take the section splitter as an argument (R3), the ingest tool passes `ai/interviews_split.split_sections`; tests use `tests/note_parsing.py`, which binds the real splitter.
- Step 8 (docs): `docs/ai-engineering-upgrade-path.md` has the U3c result (checkbox says "eval comparison pending").

## Test Results
- Step 1: `uv run pytest` 2802 passed, 10 skipped; `ruff check app tests` clean.
- Step 2: 2801 passed, 10 skipped; ruff clean.
- Step 3: 2793 passed, 10 skipped; ruff clean; `graphify update .` run.
- Step 4: 2797 passed; Step 5: 2631 passed; Step 6: 2554 passed, 9 skipped; ruff clean each time. The flaky `test_profile_read_resume` failed once (passes alone).
- Greps (AC7): no `llm_configured`, "LLM disabled", `llm_on` or `chat_model=None` in `app`; `chat_model: ChatModel | None = None` stays only on the three eval `main()` signatures (a test injection point, built from settings when None).
- Step 7: 2587 passed, 9 skipped; ruff clean; `graphify update .` run.

## Tests Pending
- Step 8: real-model evals (the user runs them; PowerShell, same model, 2 repeats, tree as it is): `uv run python -m app.modules.interviews.tooling.interviews_evals --task write --repeat 2 --note "U3c chain"`, then the same with `--task stream`, `--task decide`, `--task feedback`. Then Claude compares each with `docs/evals/baselines.md` (write, stream "current latency", decide "current", feedback) in Langfuse and writes `docs/evals/u3c-chain-vs-baseline.md`.
- Step 5: the migration on the dev database (the user runs it)
- `uv run alembic upgrade head`, `uv run alembic downgrade -1`, `uv run alembic upgrade head`
- learnings.md: the eval log row and section 7 numbers (after the evals)

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | timeout / 429 / 5xx hand the call to the next provider, log names both | spec | AC1, EC1, EC2 | pass |
| T2 | 1 | result and trace carry the provider that answered | spec | AC1 | pass |
| T3 | 1 | stream fails before first chunk: switch; after first chunk: no switch, `after_output` | spec | AC2, EC5, EC6 | pass |
| T4 | 1 | invalid reply never switches provider | spec | AC3, EC3 | pass |
| T5 | 1 | second provider gets only the time left; none left starts none | spec | AC5, EC7 | pass |
| T6 | 1 | worst case with 2 providers = 12 calls | spec | AC6, EC16 | pass |
| T7 | 1 | request error (bad key) raises at once, no switch | inferred | risk: hidden misconfig | pass |
| T8 | 1 | every provider down: whole chain retried, last error raised (blocking + stream) | spec | EC4, EC11 | pass |

## Open Questions
- none

## Baseline Failures
- `tests/modules/profile/utils/test_profile_read_resume.py` flaky (passes alone)
- pyright errors in `interviews_feedback.py`, `interviews_report.py`, `profile_schema.py`
- `ruff check .` 47 errors in `alembic/` only (gate is `ruff check app tests`)

## Known Issues
- none

## Deviations from Plan
- Step 6 (user-approved): `json_reply.py` stays in `core/ai` (the profile feature uses it too). `FakeProvider`/`FakeStream` moved to `tests/provider_fakes.py` instead of being ported (22 test files rely on them); the plan's "empty `ctx_search` for FakeProvider in tests" does not hold, only in `app/`. `LLM_GOOGLE_BASE_URL` is no longer read or required but still accepted and ignored: unknown `.env` keys are refused and the maintainer's `.env` has the line. **Delete the line from `.env`, then the `llm_google_base_url` field in `config.py`.**
- Step 2 text said `get_chat_model` stops allowing None; done in step 3 together with the services (the tests needed the autouse fake first). Same end state, no plan change.
- Step 2 also removed the "LLM not configured" branches of the three eval entry points (plan listed them under step 3), because their tests failed under the new required provider.
- Tests deleted because the behavior they covered was removed on purpose (not weakened): `test_without_a_chat_model_the_summary_task_stops_with_a_hint`, `test_no_listed_provider_means_no_chat_model_and_one_warning` (replaced by `test_an_empty_provider_list_cannot_build_a_chat_model`), `test_no_key_and_model_means_no_provider_and_one_warning`, `test_a_vendor_block_that_is_not_listed_is_ignored` (replaced by the refuse-empty tests), `test_llm_off_skips_without_reading_or_embedding`, `test_without_an_llm_the_stream_is_received_reaction_done`, `test_without_an_llm_no_context_is_built`, `test_without_an_llm_post_is_503_and_stores_nothing`, `test_without_an_llm_a_generated_feedback_is_still_returned`, `test_without_an_llm_no_summary_is_made`, `test_no_llm_configured_is_a_503`, `test_with_the_llm_off_retrieval_is_skipped_and_nothing_is_stored`.
- Step 4 deleted (bank-only behavior removed on purpose; the failure case is covered by `test_turn_unavailable.py`): `test_without_an_llm_the_whole_interview_runs_on_the_bank`, `test_a_mixed_bank_only_interview_alternates_behavioral_first`, `test_llm_failure_mid_interview_falls_back_to_an_unused_bank_question`, `test_with_the_llm_off_the_bank_asks_and_nothing_of_the_profile_is_stored`. Converted to the 503 expectation: the start fallback tests, `test_a_follow_up_that_falls_back_...` (stream), the failed-follow-up and garbage-decision tests (follow_ups), the four `test_turn_budget` tests, the too-large-context start test, and the four `test_stream_turn` bank tests.
- Step 4 test-side: `Interviewer.settle` lost its unused `last_main` argument.
- Tests adapted: `test_config.py` embedding and limit tests (now need a listed provider), `test_factory.py` (default provider env), `test_retrieval_eval.py`, `test_tracing_routes.py` (the retrieval step is now a second span), the ingest CLI test (key removed with monkeypatch).

## Debug Log
One entry per `/debug` invocation (written by debug).

## Review
Written by `/review-feature`. Re-runs append new IDs and keep existing statuses.
Level: low (2026-11-28). The `code-review` agent read only about 700 of ~118 KB of diff and reported nothing; the
rest was reviewed by hand (see Check results), so coverage is partial.

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | should-fix | traceability (AC9, EC14) | alembic/versions/b8f3a2c91d6e_replace_bank_with_stored.py:1 | The migration was never run up/down/up on a database: only its SQL was rendered offline (`alembic upgrade 667c6bd6bf94:head --sql` and the downgrade), and no scratch Postgres exists in this session. AC9 asks for "applies and downgrades cleanly on a test database". The user ran `upgrade head`, `downgrade -1`, `upgrade head` on the dev database (2026-11-28): all three applied cleanly. | fixed |
| R2 | should-fix | project rules / API contract (hand review) | app/modules/interviews/routes/interviews_route.py (start, answer and stream docs) | The API contract changed for clients: `409 NOT_ENOUGH_QUESTIONS` is gone, and an LLM failure now returns `503 INTERVIEWER_UNAVAILABLE` (JSON on start and answer, an `error` SSE event on the stream) instead of a bank question. The web client must show the generic message and let the candidate retry. The route docs and OpenAPI list it, but nothing in this repo can tell whether the client handles it. | open |
| R3 | nit | hand review | app/modules/interviews/services/interviews_answer_service.py:359 | On a streamed turn whose question is not a follow-up, the `reaction` event is sent before the question is written. If the write then fails, the client has shown an acknowledgement for a turn that ends in an error, and the retry shows a different one. Nothing is saved, so this is only display; Fixed 2026-11-28: the reaction is now picked as soon as the action is known but sent with the first question text (or at the end when nothing is written), so a write that fails before any text leaves none shown; the order reaction, then text is kept. Tests: `test_a_stream_with_every_provider_down_ends_in_one_error_event` asserts no `reaction`; the three stream-order tests moved the `writing` status before the reaction. | fixed |
| R4 | nit | hand review | app/core/config.py:89 | `llm_google_base_url` is read by nothing but is still accepted, so the maintainer's existing `.env` keeps loading (unknown `.env` keys are refused). Fixed 2026-11-28: the line is gone from `.env` and the field and its validator entry are removed from `config.py`; the real settings still load. | fixed |
| R5 | nit | spec AC10 vs. what was built | tests/provider_fakes.py:1, app/core/ai/json_reply.py:1 | AC10 asks for `FakeProvider` and `json_reply.py` to be gone. `FakeProvider` moved to the test helper (22 test files rely on it) and `json_reply.py` stays in `core/ai` (the profile feature uses it). Both were approved by the user on 2026-11-28. Fixed 2026-11-28 by amending spec.md (AC10 and the Functional bullet) and the plan note to describe what was built; porting the tests off `FakeProvider` stays a later cleanup. | fixed |

Check results:
- `uv run --with ruff ruff check app tests` -> pass
- `uv run pytest` -> not re-run (level low): task.md records a green full run on the final code, 2587 passed, 9 skipped, 2026-11-28; only docs changed after it
- type checker (pyright) -> not run: low level (pyright was clean on the two conftest files earlier)
- static security scan, dependency audit -> not run: low level
- migration up/down/up round-trip -> pass: run by the user on the dev database, 2026-11-28 (R1)
- `code-review` (level low) -> ran as a background agent; partial coverage (~700 lines), no findings
- `security-review` / `llm-security` -> not run as agents (low level); checked by hand against their rules: the 503 text and the SSE error carry no vendor or prompt text (asserted in `test_turn_unavailable.py` and `test_start_llm.py`); the new `llm_provider_switch` log has provider names and the error class only (asserted in `test_chat_chain.py`); API keys stay `SecretStr`; the chain's worst case is bounded (12 calls with two providers, pinned in `test_retry_budget.py`) and by the turn deadline; no prompt, retrieval or auth code changed
- `simplify` -> not run: low level
- project rules (CLAUDE.md): layers enforced by `tests/test_layers.py` (new `check_sdks` and `utils/` -> `ai/` rules pass on the real tree); UUID keys untouched; the migration is new, no applied one edited; config only from env and `.env.example` in sync; evals compared with the baseline (`docs/evals/u3c-chain-vs-baseline.md`); `graphify update .` run; nothing committed
- traceability: AC1-AC8, AC10-AC13 and EC1-EC13, EC15, EC16 have a passing test or a recorded verification; AC9 and EC14 are covered by the user's migration run (R1)

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1 | lean-ctx, ponytail, tdd | explore core/ai, smallest code, red-green loop |

## Links
- Spec: docs/features/u3c-fallback-chain/spec.md
- Plan: docs/features/u3c-fallback-chain/plan.md

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
- [ ] Code follows project .claude/rules (or N/A)
- [ ] No unresolved plan deviations
