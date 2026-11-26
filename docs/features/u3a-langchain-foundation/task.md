# Implementation: U3a LangChain foundation + first chains

## Status
Done (all 10 steps; comparison in docs/evals/u3a-langchain-vs-baseline.md); /review-feature next
Health Check: all present (level: low)

## Completed Steps
- [x] 1. Spike: dependencies and the library behavior U3a relies on
- [x] 2. JD summary eval on the old code (baseline `20261126-185243` recorded in `docs/evals/baselines.md`)
- [x] 3. `to_llm_error()`
- [x] 4. Chat model factory
- [x] 5. Tracing callback + fake chat model
- [x] 6. Core call helper + contract test
- [x] 7. Wiring + layer rule
- [x] 8. JD summary on LangChain
- [x] 9. Profile extraction with structured output (code done; waiting on the user's comparison runs)
- [x] 10. Compare, record, close out (profile regression found, fixed with a required-fields schema, re-run matches baseline)

## Current Step
### 9 -> 10. Stop: user-run comparison evals
- The user runs, same model as the baselines:
  - `uv run python -m app.modules.interviews.tooling.interviews_evals --task summary --model gemini-3.5-flash-lite --repeat 2`
  - `uv run python -m app.modules.profile.tooling.profile_evals --model gemini-3.5-flash-lite --repeat 2`
  - `uv run python -m app.modules.interviews.tooling.interviews_evals --task write --model gemini-3.5-flash-lite` (once, sanity check of the summary inside it)
- Then Claude reads them in Langfuse and writes `docs/evals/u3a-langchain-vs-baseline.md` (Step 10).

## Changes Made
All uncommitted. Suggested commits (the user commits):
- Step 1: `git add pyproject.toml uv.lock tests/core/ai/test_langchain_behaviour.py; git commit -m "chore(ai): add langchain-core and langchain-google-genai and pin the behavior U3a relies on"`
- Step 2: `git add app/modules/interviews/data/summary_eval_cases.json app/modules/interviews/tooling/interviews_summary_evals.py tests/modules/interviews/tooling/test_summary_evals.py docs/evals/baselines.md; git commit -m "feat(evals): add the job-description summary eval (--task summary) and its baseline"`
- Steps 3-7: `git add app/core/ai/chat.py app/core/ai/chat_errors.py app/core/ai/chat_tracing.py app/core/ai/chat_fake.py app/core/ai/factory.py app/core/ai/dependencies.py app/core/config.py app/main.py .env.example tests/core/ai tests/test_layers.py; git commit -m "feat(ai): add the LangChain call layer (chat model factory, error mapping, call helper, tracing callback, fake model, contract test, layer rule)"`
- Steps 8-9: `git add app/modules tests/modules docs/features/u3a-langchain-foundation; git commit -m "refactor(ai): move the job-description summary and profile extraction onto LangChain"`

Files by step:
- 3: `app/core/ai/chat_errors.py`, `tests/core/ai/test_chat_errors.py`.
- 4: `app/core/ai/factory.py` (`build_chat_model`), `app/core/ai/chat.py` (`ChatModel`), `app/core/config.py` (`LLM_VENDOR_CHAT_PARAMS`, `llm_google_thinking_budget`, `llm_chat_params`), `.env.example`, `tests/core/ai/test_chat_factory.py`.
- 5: `app/core/ai/chat_tracing.py` (`ChatTrace`, `TracerHandle`), `app/core/ai/chat_fake.py`, `tests/core/ai/test_chat_tracing.py`.
- 6: `app/core/ai/chat.py` (`complete_chat`, `complete_structured`, `fixed_prompt`), `tests/core/ai/test_chat.py`, `tests/core/ai/test_chat_contract.py`.
- 7: `app/main.py`, `app/core/ai/dependencies.py` (`get_chat_model`), `tests/test_layers.py`.
- 8: `app/modules/interviews/ai/interviews_summary.py`, `interviews_service.py`, `interviews_start_dependencies.py`, `interviews_evals.py`, `interviews_summary_evals.py`; tests `tests/modules/interviews/ai/test_summary.py`, `routes/test_job_description_summary.py`, `tooling/test_evals.py`, `tooling/test_summary_evals.py`, `tests/modules/interviews/conftest.py` (`llm.summary`, `llm.script_summary`).
- 9: `app/modules/profile/ai/profile_extract.py`, `profile_reply.py` (`RawProfile`, `clean_profile`), `profile_service.py`, `profile_dependencies.py`, `profile_evals.py`; tests `tests/modules/profile/ai/test_profile_extract.py`, `profile_fixtures.py`, `conftest.py`, `routes/test_profile_routes.py`, `tooling/test_profile_evals.py`.

## Test Results
- Step 1: 21 spike tests; full suite 2574 passed, 7 skipped.
- Step 2: tooling 351 passed; full suite 2590 passed, 7 skipped.
- Step 3: 16 passed; full suite 2606 passed, 7 skipped.
- Steps 4-6: core/ai 362 passed; full suite 2657 passed, 7 skipped.
- Steps 7-9: layers 34 passed; interviews 1816 passed, 5 skipped; profile 157 passed; **full suite 2706 passed, 7 skipped**.
- Every step: `uv run --with ruff ruff check app tests` all checks passed; pyright 0 errors on the new/changed `core/ai` and `ai/` files (one pre-existing error in `tests/modules/profile/profile_fixtures.py::resume_pdf`, a list-variance warning in an unchanged line); `graphify update .` run.

## Tests Pending
- ~~JD summary baseline run~~ done: `summary/.../20261126-185243`, pass rate 0.67 / 0.83, noise margin 0.17.
- Comparison runs: summary, profile, write once (user, now).
- Real endpoint, verified by those runs: gRPC timeouts arrive as `DeadlineExceeded`; `gemini-3.5-flash-lite` accepts the `RawProfile` JSON schema (it has `additionalProperties: false`); native usage counts match the old layer's.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1-T9 | 1 | spike: SDK retries, per-call limits, thinking, usage, blocked reply, error classes, structured output, with_retry/with_fallbacks on streams | code-derived | spike | pass |
| T10-T14 | 2 | summary eval: case file, checks, case runner, run in Langfuse | spec | FR10, AC9, EC13 | pass |
| T15 | 3 | 429 with/without RetryInfo, timeout, 5xx, 4xx, wrapped InvalidArgument, parser error, passthrough, cause kept | spec | FR2, AC2, EC5 | pass |
| T16 | 3 | unknown exception: generic LLMError, logged by class only, no message text | spec | EC6 | pass |
| T17 | 4 | LLM off: no model + warning; Gemini from config; --model; SDK retries off; thinking table | spec | FR1, AC1, EC1 | pass |
| T18 | 5 | one generation per call (also across retries), labels, usage, redaction, failure, Langfuse down, tracer off | spec | FR5, AC8, EC14, EC15 | pass |
| T19 | 6 | text reply + usage + finish reason; no usage; empty reply; temperature per call | spec | FR4, EC16 | pass |
| T20 | 6 | spent budget sends nothing; timeout = time left; almost-spent budget cut, no retry after | spec | FR4, AC3, EC7 | pass |
| T21 | 6 | 429 waits >= Retry-After; 5xx retried to max then giveup with task; count from setting; 4xx and unknown not retried | spec | FR3, AC4, EC5, EC6 | pass |
| T22 | 6 | structured: parsed, schema miss returned (no reply text in the error), transport retried | spec | FR9 | pass |
| T23 | 6 | contract, Gemini + fake: text, structured, usage, 5 vendor errors, per-call limits (text and structured) | spec | FR7, AC5 | pass |
| T24 | 7 | layer rule: each layer importing langchain*/vendor SDKs is reported; ai/ folders and the ChatModel alias allowed | spec | AC11 | pass |
| T25 | 8 | summary: ok + usage log, app messages and time cap, braces kept as text, transport fail, invalid reply, empty, unknown, trace labels | spec | FR8, AC6, AC8, EC3, EC4, EC6 | pass |
| T26 | 8 | start interview: summary on chat model, questions on provider; short JD no call; unusable summary keeps original; LLM off | spec | AC6, EC1-EC4 | pass |
| T27 | 8 | evals call the app's summary function (write/stream summary step, --task summary) | spec | FR12 | pass |
| T28 | 9 | extraction: valid first reply, invalid then valid, two invalid (not-json, off-schema, empty), empty profile not retried, transport error, caps/dedupe, fenced JSON, redacted trace, no time | spec | FR9, AC7, AC8, EC8-EC12, EC14 | pass |
| T29 | 9 | upload route responses unchanged (existing route tests, fixture swapped to the chat model) | spec | AC7 | pass |
| T30 | 9 | regression: per-call limits reach a structured call (bind dropped them) | code-derived | found in step 9 | pass |

## Open Questions
- none

## Baseline Failures
- Flaky, pass on re-run: `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`, `test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table`, occasional WinError 10055. None showed up in these runs.

## Known Issues
- `langsmith` arrives as a transitive dependency; inactive unless `LANGSMITH_TRACING` is set.
- Two clients to Gemini exist until U3c: the old OpenAI-compatible one (unmigrated tasks) and the native one (summary, profile).
- The eval runner's summary step no longer passes `--reasoning-effort` to the summary call: the app never did, and the native model has no such option (thinking comes from `LLM_GOOGLE_THINKING_BUDGET`).

## Deviations from Plan
- Step 10 finding: profile extraction regressed because `RawProfile` marked no field required; the model now gets `ModelProfile` (all required), test added, re-run at baseline.
- Finding: `.with_retry()` can't keep the U2 rules → FR3's fallback applies: `RetryPolicy` owns LLM retries in U3a (within the spec's decision rule; recorded in learnings.md).
- Finding: `thinking_level` is not supported by the bundled SDK → plan.md Step 4 updated: the thinking table uses `thinking_budget` only, default none.
- Finding: the SDK's `max_retries` counts attempts → "SDK retries off" means `max_retries=1`.
- Step 2 files: the summary eval lives in its own module `interviews_summary_evals.py`, dispatched like the feedback task.
- Step 5/6: the tracer reaches the helper on the model itself (`TracerHandle`, attached by `build_chat_model(..., tracer=)`), the way `TracingProvider` wrapped the old provider at the factory, so services never pass a tracer. One generation per call: the callback opens it on the first model run, the helper closes it with the final result.
- Step 6/9: per-call limits (timeout, max tokens, temperature) are set on a per-attempt `model_copy`, not with `.bind()`: `with_structured_output` on a bound model drops the bound kwargs (pinned in `test_langchain_behaviour.py`, regression in `test_chat_contract.py`).
- Step 8: `summarize_job_description` returns a `SummaryOutcome` (summary, reply, error) instead of only the text, so the eval scores the model's reply even when the app would reject it and counts its tokens; the service reads `.summary`.
- Step 9: `profile_reply.py` is split into functions, not files: public `RawProfile` (the schema given to the model) and `clean_profile` (shared by structured and JSON-text replies); `parse_profile_reply` stays for text replies. An empty reply is caught as `empty_reply` and retried (spec FR9/EC9); before, the old provider raised it and the extraction failed at once.

## Debug Log
- none

## Review
Level: low. Coverage is partial: the code reviewer read about the first 700 lines of the app diff and did not reach `profile_service.py`, `profile_evals.py` and what follows; Claude read the `profile_service.py` diff by hand (a plain swap of the provider for the chat model, no finding).

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | nit | code-review | app/modules/interviews/tooling/interviews_evals.py:861-865 | The chat model is built only inside `if provider is None:`. A caller that injects `provider` without `chat_model` (tests) gets none, so `--summary on` skips condensation and `--task summary` exits 1. The real CLI path builds both, so nothing breaks in use. | won't fix: only the injected-provider test path is affected |

### Check results
| Check | Result |
|-------|--------|
| Lint (`ruff check app tests`) | pass |
| Full test suite | not re-run (low level): the last full run on the final diff gave 2706 passed, 1 flaky failure that passes on re-run (42 of 42 in its file) |
| Type checker | not run: low level (pyright was clean on the changed files in earlier steps) |
| security-review | not run: the diff touches no auth, permissions or secrets (résumé redaction is unchanged and has a test) |
| llm-security | manual check, no finding: the résumé stays fenced as data, profile traces stay redacted, the summary logs metadata only, no raw text in errors (tests pin each) |
| simplify | not run: low level |
| Project rules | pass: LangChain imports only in `core/ai` and feature `ai/` (layer test), prompts unchanged and in files, LLM output validated with Pydantic, no hardcoded model names, evals compared with the baseline |
| Traceability | AC1-AC9 and AC11 have passing tests; AC10 is the comparison file, linked from `learnings.md`; EC1-EC16 are covered by T15-T30 (EC2 by T26) |

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1 | ponytail, test | smallest spike; behavior pinned as tests |
| 2-9 | tdd, test, ponytail | tests first at the confirmed seams; smallest code per step |

## Links
- Spec: docs/features/u3a-langchain-foundation/spec.md
- Plan: docs/features/u3a-langchain-foundation/plan.md
- Learnings: docs/features/u3a-langchain-foundation/learnings.md
