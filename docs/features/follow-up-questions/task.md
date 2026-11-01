# Implementation: Follow-up Questions (decide / write split)

## Status
Steps 1-11 done and tested. Step 12 waits on real-model runs (opt-in, real API calls), so not ready for PR yet.

## Completed Steps
- [x] 1. Constants and enums (`QuestionKind`, `FollowUpAction`, `FollowUpGap`, cap, budget constants, task and prompt names)
- [x] 2. Decision parser (`parse_decision_reply`, shared `_load_object`)
- [x] 3. Write parser modes (`follow_up_category`: question only, inherited category)
- [x] 4. Prompts (`follow_up_decision_v1.md`, `interviewer_v4.md`; v1-v3 untouched)
- [x] 5. Context tasks (thread-aware `WindowLedger`, `FollowUpDecision`, `follow_up_decision` task, v4 as the live default)
- [x] 6. Data and API (model columns, migration `e3b8f41a6c27`, `question_kind`/`main_number`, optional reaction)
- [x] 7. Task-routing test double (`llm.decide`, `llm.script_decide`, `decision_json`)
- [x] 8. Turn module (`interviews_turn.py`: `Deadline`, `apply_limits`, decide and write steps, per-call and per-turn logs)
- [x] 9. Controller wiring (`answer()` and `start()` on the turn module; follow-up rows; reaction only when moving on)
- [x] 10. Usage report (follow-up counts, tokens by kind, `turn_llm_ms p50/p95`)
- [x] 11. Evals (`expect` labels on 15 cases, `--task decide|write`, accuracy, over- and under-probing, per gap)
- [ ] 12. Measure, tune, document: learnings written with predictions and the measured context sizes; the real-model numbers are pending

## Current Step
### 12. Measure, tune, document
- Needs the user (real API calls, free-tier rate limit about 25 calls; pause between runs):
  - `uv run python -m app.modules.interviews.interviews_evals --task decide --repeat 3 --model gemini-3.5-flash-lite`
  - `uv run python -m app.modules.interviews.interviews_evals --repeat 3 --model gemini-3.5-flash-lite`
  - one live interview, then `uv run python -m app.scripts.interview_report --html` (cost, effectiveness and efficiency of the newest interview, with the checks that compare the log to the database; prints the text report and saves the designed HTML page as `logs/reports/report_<session id>.html`, one file per interview; `--session <id>` for another, `--last 10` to pool the newest ten) and `uv run python -m app.scripts.usage_report` (totals and p50/p95 across all interviews)
- Then: fill the *pending* Observed lines in `learnings.md`, tune `DECIDE_MAX_SECONDS` / `MIN_SECONDS_FOR_WRITE` if p95 says so, tick the learning-path line.

## Changes Made
- Nothing committed (the user commits by hand). Suggested message:
  `feat(interviews): ask follow-up questions with a decide call, a code-enforced cap and one turn deadline`

## Test Results
- Full suite: 649 passed, 1 skipped, 2 failed (the 2 baseline failures below, unchanged).
- Interview tests: 475 passed.
- Lint: `ruff check --select F,E9,B` clean on `app`, `tests`, `alembic` (ruff is not a project dependency; run with `uv run --with ruff`).
- Migration by hand on Postgres 18 (scratch database, created and dropped): upgrade backfills `kind=main`, `main_number=position`; a follow-up row with the self foreign key inserts; downgrade drops the columns and keeps the rows; re-upgrade works.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 2 | follow_up with gap / next_question with null gap / fence | spec | AC1 | pass |
| T2 | 2 | 9 invalid shapes, one reason code each | spec | AC1, EC3 | pass |
| T3 | 2 | bad note dropped, decision kept | spec | EC18 | pass |
| T4 | 3 | follow-up without category inherits the parent's; model category rejected | spec | EC15 | pass |
| T5 | 3 | repeat of an earlier follow-up rejected; one question mark | spec | EC14 | pass |
| T6 | 4 | six sections; every action and gap value in the decide prompt; v4 has no note | spec | AC9 | pass |
| T7 | 5 | window never starts inside a thread; guard never drops the current thread | spec | AC12, EC16 | pass |
| T8 | 5 | decide messages: thread whole, older questions as notes, follow-ups left | spec | AC12, EC1 | pass |
| T9 | 5 | untrusted text only in user messages (decide) | spec | AC11, EC10 | pass |
| T10 | 5 | maximum interview with maximum follow-ups fits both tasks | spec | AC12 | pass |
| T11 | 6 | transcript and QuestionOut expose `question_kind` and `main_number` | spec | AC8 | pass |
| T12 | 6 | migration upgrade, backfill, downgrade (by hand, Postgres) | spec | AC16, EC19 | pass |
| T13 | 9 | LLM off: no follow-ups, every answer gets a reaction | spec | AC14, EC12 | pass |
| T14 | 9 | follow-up stored with parent, kind, category, no reaction; note from the decision | spec | AC6, AC8 | pass |
| T15 | 9 | always follow_up: exactly 2 per main question; `override=cap_reached` | spec | AC2, AC20, EC1, EC2, EC8 | pass |
| T16 | 9 | last main question followed up, completes when its thread ends | spec | AC5, EC9 | pass |
| T17 | 9 | failed follow-up write: bank main question / completion on the last; `source=bank fallback=write_failed` | spec | AC4, AC20, EC5 | pass |
| T18 | 9 | garbage and provider-error decisions: interview completes, no notes | spec | AC3, EC3, EC4 | pass |
| T19 | 9 | injected answer and job description: cap holds, no system-prompt leak | spec | AC11, EC10 | pass |
| T20 | 9 | second submit: 409, no second follow-up row | spec | AC7, EC11 | pass |
| T21 | 9 | session with stored questions: no decide call | spec | AC14, EC13 | pass |
| T22 | 8 | decide capped at `DECIDE_MAX_SECONDS`; write keeps the rest | spec | AC18, EC20 | pass |
| T23 | 8 | decide budget shrinks to keep the write reserve | spec | AC18 | pass |
| T24 | 8 | failed decide not retried with the last seconds | spec | AC18, EC21 | pass |
| T25 | 8 | no write below `MIN_SECONDS_FOR_WRITE`: bank, `override=no_time` | spec | AC13, AC20, EC6 | pass |
| T26 | 8 | write retry skipped below `MIN_SECONDS_FOR_RETRY` | spec | AC13 | pass |
| T27 | 8 | usage of decide + write summed; log lines carry task, `budget_left_ms`, action/gap, no text | spec | AC10, AC19 | pass |
| T28 | 10 | follow-up counts and tokens by kind; p50/p95 per turn | spec | AC10, AC19 | pass |
| T29 | 11 | ≥10 labelled cases incl. both injections and an at-cap thread | spec | AC15 | pass |
| T30 | 11 | check_decision, run_decide_case, summarize_decisions, `--task decide` | spec | AC15 | pass |

## Open Questions
- AC17: needs the real-model numbers (Step 12). -> needs: the user's runs.
- EC7 (empty / "I don't know" / off-topic answers move on): no code guard by design; measured by the decide evals (`near_empty`, `off_topic` cases). -> needs: the decide run.
- EC17 (server dies before the save): covered by the existing compare-and-swap tests; no new test.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: the local `.env` sets `LLM_MAX_TOKENS=2000` (the test expects the 800 default). Environment, not code.
- `tests/core/test_config.py::test_env_example_lists_every_llm_setting`: `OPENROUTER_API_KEY` is in the settings but not in `.env.example`. Pre-existing, unrelated.

## Known Issues
- `full_history` (the v1 baseline) ignores the follow-up mode; if it were made the live default, a follow-up write would fail validation and the bank would ask instead. It is only used by the evals, which write main questions.
- EC13: the last question of a session stored up front can get follow-ups (accepted limitation, pre-slice-2 development data only).
- Client (Next.js, other repo): handled in cuewise-fe `docs/features/interviews-follow-up-questions/` (nullable `reaction`, `question_kind` / `main_number`, progress by main question); its 45 s answer timeout already exceeds the 30 s turn deadline.
- The user-level ruff config also flags import order (I001) and `typing` style (UP) in files this feature did not touch; not fixed here, to keep the diff to the feature.

## Deviations from Plan
- Listed in plan.md, "Deviations Found During Implementation" (QuestionTurn without main_number, no job description in the decide call, fields on every transcript item, downgrade keeps rows, summary line for non-LLM turns, no usage on a bank replacement, window moves back to the thread start).
- Tests changed because the spec changed them (not loosened): v3 -> v4 as the live prompt (5 assertions), the new response fields (3), the decide call's usage now summed onto the question (1), the log line count per turn (1), a v3-only note eval check (1), the in-memory question helper sets `kind` (1).

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | lean-ctx | reads, searches, shell, edits |
| all | graphify | answer-turn call graph before coding; `graphify update .` at the end |
| all | ponytail | leanest version per step (derived thread numbers, no new dependency, no extra abstractions) |
| setup | find-skills | installed `sqlalchemy-alembic-expert-best-practices-code-review` (wispbit-ai, about 2K installs) |
| 6 | sqlalchemy-alembic-expert-best-practices-code-review | split-foreign-key and index rules considered; not applied (small table, no query by parent), noted here |

## Links
- Spec: docs/features/follow-up-questions/spec.md
- Plan: docs/features/follow-up-questions/plan.md
- Learnings: docs/features/follow-up-questions/learnings.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete (Step 12 waits on real-model runs)
- [x] Full test suite green apart from the 2 recorded baseline failures
- [ ] Every spec.md acceptance criterion met and covered (AC17 pending real numbers; all others covered by passing tests or the hand-run migration)
- [x] Open Questions surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [ ] Commits documented (the user commits)
- [x] No open blockers in code
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations (all written into plan.md)
