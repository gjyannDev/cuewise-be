# Implementation: Context Management for the Interview LLM Calls

## Status
Code complete (steps 1-7, 9-11, 13). Open: steps 8 and 12 need real-model runs (the configured free model was rate limited), so AC13 part 2, AC18 part 2 and AC19 are not met yet. Not ready for PR until they are recorded. Branch: `feat/interviews` (no new branch, per user).

## Completed Steps
- [x] 1. Context core: `app/core/ai/context.py` (manager, per-strategy limit, oldest-first trimming, too-large error, metadata-only log line on `app.llm.context`); `CHARS_PER_TOKEN` moved here from `fake.py`.
- [x] 2. Provider reasoning option: optional `reasoning_effort` sent as OpenRouter `reasoning: {effort}` only when given; `LLMResult` also reads `cached_tokens` and `reasoning_tokens` when reported.
- [x] 3. Constants, prompts, validation: context constants and `LEVEL_GUIDANCE`; `interviewer_v2` and `job_description_summary_v1` loaded at import; `render_interviewer_v2_prompt`, `render_summary_prompt`; `validate_note`, `validate_summary`.
- [x] 4. Reply contract with optional note: `InterviewerReply` is a NamedTuple with `note` and `note_dropped`; a bad note never rejects the question; unknown fields still rejected.
- [x] 5. Strategies: `interviews_context.py` (`FullHistory`, `WindowLedger`, `JobDescriptionSummary`, `build_context_manager`, `CONTEXT_MANAGER`); `QuestionTurn.note`; `neutralize_app_tags` for `job_description` and `interview_status` tags.
- [x] 6. Baseline report: `build_usage_report`, `InterviewsRepository.list_all_questions`, `app/scripts/usage_report.py`; ran on the dev DB (numbers in learnings.md).
- [x] 7. Eval runner: `--strategy --prompt --model --reasoning-effort --notes --summary --repeat`; finish reason, cached and reasoning tokens, `finish=length` count, note check, per-run and aggregate pass rate, review lines for long histories; 3 new eval cases.
- [ ] 8. "Before" snapshot (real model): attempted, blocked by 429s on the free model; deferred to the user.
- [x] 9. Migration `c7d41e2a9b03`: nullable `interview_sessions.job_description_summary` and `interview_messages.note`. Upgrade, downgrade and upgrade again on the dev Postgres; `alembic check` reports no drift.
- [x] 10. Controller: builds every interviewer call through the manager (`window_ledger` live, `interviewer_v2` stored and logged), stores the note on the answer it describes, logs dropped notes without text, falls back to the bank on `context_too_large`; `get_context_manager` dependency; `interviewer_history` fills notes.
- [x] 11. Job-description summary at start: one call through the manager with a 10 s cap when the description is over 600 characters; validated; stored on the session; used in every interviewer call; any failure keeps the original; usage logged with its own prompt version.
- [ ] 12. Comparison and learnings (real model): for the user, after step 8; `learnings.md` has the checkpoints and commands.
- [x] 13. Finish: full suite, ruff (changed files), `graphify update .`, learning-path progress line.

## Changes Made
Not committed; the user commits manually. Suggested commits:
- `feat(core): add a context manager and an optional reasoning effort to the LLM provider` (app/core/ai/*, tests/core/ai/*)
- `feat(interviews): build interviewer calls with window_ledger, running notes and a job-description summary` (interviews module, prompts, migration, tests)
- `feat(interviews): add eval runner flags, long-history cases and a usage report script` (interviews_evals.py, eval_cases.json, app/scripts/usage_report.py, tests)
- `docs(context-management): add spec, plan, task and learnings`

## Test Results
- Full suite: `uv run pytest` -> 548 passed, 1 skipped, 1 failed (the baseline failure below only).
- Lint: `uvx ruff check --line-length 120` on changed app and test paths -> all checks passed. The new migration keeps the Alembic template style (same 5 UP/I findings as every existing migration).
- Format: new and changed files formatted at 120 columns; `interviews_controller.py` kept at its existing 88-column formatting.

## Tests Pending
- Step 8 (user): `uv run python -m app.modules.interviews.interviews_evals --strategy full_history --repeat 3 --model <model that is not rate limited>`, then the 5-point manual checklist on the `review:` lines; record in learnings.md Checkpoint C.
- Step 12 (user): the comparison runs in learnings.md Checkpoint D (also confirms AC18: which models accept `reasoning_effort`, and whether `cached=` is ever non-zero).

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | estimate is characters / 4 | spec | plan step 1 | pass |
| T2 | 1 | default strategy builds; named strategy overrides | spec | AC2 | pass |
| T3 | 1 | unknown task or strategy names the valid ones | spec | EC18 | pass |
| T4 | 1 | no limit = never trimmed | spec | EC26 | pass |
| T5 | 1 | over the limit drops oldest until it fits | spec | AC7, EC6 | pass |
| T6 | 1 | required parts over the limit raise and still log | spec | EC7 | pass |
| T7 | 1 | log line has counts, no text | spec | AC11 | pass |
| T8 | 1 | a second task leaves the first alone | spec | AC12 | pass |
| T9 | 2 | reasoning effort sent only when given (OpenRouter + fake) | spec | AC18 | pass |
| T10 | 2 | cached and reasoning tokens read when reported, else None | code-derived | plan step 12 | pass |
| T11 | 3 | both new prompts have the six sections in order | spec | plan step 3 | pass |
| T12 | 3 | v2 renders for every level and type with no placeholder left | spec | AC20 | pass |
| T13 | 3 | v2 has no question number and asks for a note | spec | AC5 | pass |
| T14 | 3 | summary and note validation | spec | EC10, EC20 | pass |
| T15 | 4 | note kept / absent / dropped with reason; unknown field rejected | spec | AC15, EC19, EC20, EC23, EC24 | pass |
| T16 | 5 | full_history equals today's payload | spec | AC1, EC2 | pass |
| T17 | 5 | full_history never trimmed | spec | EC26 | pass |
| T18 | 5 | window layout: first call, short history, ledger with notes, cap, prefix identity, final flag | spec | AC3-AC5, EC1-EC4, EC17, EC25, EC27 | pass |
| T19 | 5 | untrusted text only in user messages; fake status tags neutralised | spec | AC10, AC17, EC12, EC21 | pass |
| T20 | 5 | max interview under 5,000 and below full_history from question 5 | spec | AC6, EC5 | pass |
| T21 | 5 | trimming order: ledger, then window, never the latest | spec | AC7 | pass |
| T22 | 6 | report per position and totals; dashes; empty; no text; script wiring | spec | AC12, EC14, EC15 | pass |
| T23 | 7 | runner flags, notes, summary, note check, finish=length, too large, repeats, bad flags, main | spec | AC13, AC18, EC18 | pass |
| T24 | 10 | live default is window + v2; older answers not resent | spec | AC2, AC3 | pass |
| T25 | 10 | note stored on its answer and shown in later ledgers | spec | AC16, AC17 | pass |
| T26 | 10 | bad note dropped, question kept, no retry, logged without text | spec | AC15, EC20 | pass |
| T27 | 10 | no note after a bank fallback or for the final answer | spec | EC22 | pass |
| T28 | 10 | too-large context -> bank question, no LLM call, logged | spec | AC7, EC7 | pass |
| T29 | 10 | LLM off builds no context; notes in no response or log | spec | EC16, AC16 | pass |
| T30 | 11 | long description summarised once and used everywhere; 10 s cap | spec | AC8, EC9 | pass |
| T31 | 11 | short or missing description: no extra call | spec | EC8 | pass |
| T32 | 11 | timeout / empty / not shorter / too long keep the original; garbage still completes an interview | spec | AC9, EC10, EC11 | pass |
| T33 | 11 | summary never returned or logged; usage logged with its own prompt version; LLM off makes none | spec | AC10, AC11, EC16 | pass |

## Open Questions
- None blocking the code. Real-model results (steps 8 and 12) decide whether `window_ledger`, notes and the summary stay the live defaults.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: expects `llm_max_tokens == 800`, but `core/config.py` defaults to 2000. Pre-existing, outside this feature.

## Known Issues
- The configured model `google/gemma-4-26b-a4b-it:free` returned 429 on 26 of 27 eval calls (free-tier limits); real-model steps need a model that is not rate limited.
- The OpenRouter `reasoning: {effort}` request shape and the `prompt_tokens_details.cached_tokens` / `completion_tokens_details.reasoning_tokens` usage fields follow the OpenAI-compatible schema; not yet confirmed on a live call (step 12).
- With `question_count = 1` there is no status block at all (the first call never has one, so the prefix stays identical), so EC27's "final question" flag only appears from question 2 on; the system prompt states the total.

## Deviations from Plan
- Step 8 deferred and steps 9-11 done before it -> user chose "continue code, run 8 later" after the free model was rate limited. Stored rows keep their `prompt_version` and `full_history` stays runnable from the eval runner, so the snapshot can still be taken; record it before relying on the new live default.
- AC6 crossover: with the fuller `interviewer_v2` prompt, `window_ledger` is smaller than `full_history` from question 5, not 3 -> spec AC6 and plan step 5 updated.
- `interviewer_history` fills notes in step 10, not step 5 (the column exists only after step 9) -> plan step 5 updated.
- `validate_note` and `validate_summary` live in `interviews_reply.py` (the module that validates model output), not `interviews_utils.py`.
- `LLMResult` also reads `cached_tokens` and `reasoning_tokens`: needed in step 12 to verify caching and diagnose `finish=length`.
- The usage report averages over interviews that used the LLM only (the dev DB has 14 bank-only interviews).
- `job_description_block` now neutralises `interview_status` tags as well as `job_description` tags, so the v1 payload differs only for a job description that contains that literal tag.
- Tests were written per step (red, then green), not strictly one slice at a time.
- Summary prompt bumped to `job_description_summary_v2` after a live Groq run (`openai/gpt-oss-120b`) returned `summary_invalid:too_long`: models count tokens, not characters, so v2 asks for at most `SUMMARY_MAX_WORDS` (60) words and states the 500-character cap. v1 is kept for rows that already reference it.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| setup | find-skills | Searched OpenRouter, Alembic and prompt-caching skills; installed `affaan-m/ecc@prompt-caching-strategy` (repo 292K stars, ~1.2K installs) after reading it; skipped `wispbit-ai/skills` (8 stars) and unrelated OpenRouter hits. |
| all | ponytail | Smallest version per step: no block framework, no tokenizer, no env settings, experiments behind runner flags. |
| setup, 13 | graphify | Mapped call paths before coding; `graphify update .` at the end. |
| 2 | prompt-caching-strategy | Cached reads are `usage.prompt_tokens_details.cached_tokens` in Chat Completions; no saving claimed without those counters. |
| 3 | prompt-engineering-patterns | Six-section prompt structure, examples of form only, a self-check. |

## Links
- Spec: docs/features/context-management/spec.md
- Plan: docs/features/context-management/plan.md
- Learnings: docs/features/context-management/learnings.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete (8 and 12 open: real-model runs)
- [x] Full test suite + build green (not just per-step tests), apart from the listed baseline failure
- [ ] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (AC13 part 2, AC18 part 2 and AC19 need the real-model runs)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [ ] Commits documented (user commits)
- [ ] No open blockers (real-model access)
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations
