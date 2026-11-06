# Implementation: Interview Feedback and Scoring (Slice 6)

## Status
In Progress: Steps 1-8 done; **stopped at Step 9, the user review gate** (rubric anchors, both prompts, expected bands). Step 10 (real-model runs, the Postgres migration check, learnings.md) follows the review.

## Completed Steps
- [x] 1. Constants, settings, errors, permission
- [x] 2. Pure contract (`interviews_feedback.py`)
- [x] 3. Rubric and prompts (data)
- [x] 4. Context tasks
- [x] 5. LLM steps (`interviews_feedback_turn.py`), log summary, `turns_of`
- [x] 6. Model, migration, repository (the hand check of the migration on Postgres is still open, see Tests Pending)
- [x] 7. Controller, schemas, routes, dependencies
- [x] 8. Evals (`interviews_feedback_evals.py`, `--task feedback`)
- [ ] 9. Review gate (user)
- [ ] 10. Measure, tune, document

## Current Step
### 9. Review gate (user)
- To review: `app/modules/interviews/data/feedback_rubric_v1.json` (anchors and level expectations), `prompts/feedback_score_v1.md`, `prompts/feedback_write_v1.md`, and the bands in `data/feedback_eval_cases.json`.
- No real-model call has been made.

## Changes Made
- Nothing committed (the user commits). Suggested message, once Step 10 is done:
  `feat(interviews): end-of-interview feedback with rubric scores, verified quotes and a template fallback`

## Test Results
- Full suite: 1172 passed, 1 skipped, 1 failed (the baseline failure below, unrelated).
- New feedback tests: 142 in five new files (contract 48, prompts and rubric 25, context 8, endpoints 40, evals 21), plus one in `test_interview_report.py` and the two updated permission tests.
- Lint: no new findings in the touched files (`uv run --with ruff ruff check`; ruff is not a project dependency, so `--with` runs it without adding one). Pre-existing findings remain in `tracing.py`, older migrations and a few test files; the new migration follows the same Alembic template as the others.

## Tests Pending
- Step 6 (Test: after): `uv run alembic upgrade head`, delete an interview and see its feedback row go, then `uv run alembic downgrade -1` on the local Postgres. Needs the user's go-ahead (it changes the dev database).
- Step 10: `uv run python -m app.modules.interviews.interviews_evals --task feedback --repeat 5 --model gemini-3.5-flash-lite`, a maximum-size interview against the provider limits, and the disconnect check (EC15) by hand.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 2 | pre-check thresholds, half rule, main answer only | spec | EC9 | pass |
| T2 | 2 | score reply: not JSON, fence, extra field, range, strict int, missing/repeated/reordered question, wrong criteria | spec | EC10, AC7 | pass |
| T3 | 2 | evidence: wrong criterion, duplicate, none; quote missing, length, other thread, case/space, follow-up answer, full answer | spec | AC8, EC11, EC20, EC23 | pass |
| T4 | 2 | `enough_evidence=false`; a stated overall accepted and ignored | spec | EC29, AC9, EC16 | pass |
| T5 | 2 | overall = mean, rounded half up (3.25 -> 3.3) | spec | AC9 | pass |
| T6 | 2 | write parser: counts, notes, lengths, markdown, tags, format; template within limits and round-trips | spec | AC15, AC13 | pass |
| T7 | 3 | six sections, unique role lines, rubric complete, broken rubric fails at load, prompts render per level/type | spec | plan 3 | pass |
| T8 | 4 | score input fenced, tags neutralised, no JD case, truncation counted and quotes still verify, too large raises, maximum fits | spec | AC14, AC21, EC17, EC18, EC22, EC23 | pass |
| T9 | 4 | write input has no answers or JD; tags in quotes neutralised | spec | AC14, EC18 | pass |
| T10 | 7 | 401/403/404/409 access, no row, no call | spec | AC1, AC2, EC1-EC4 | pass |
| T11 | 7 | happy path body, excluded fields, usage stored, temperature and max tokens | spec | AC1, AC7, AC9 | pass |
| T12 | 7 | second POST 200 same body; insufficient (code and model) | spec | AC3, AC6, EC5, EC9, EC29 | pass |
| T13 | 7 | retry then 502, provider error, no time for a retry, context too large, regenerate after failure | spec | AC10, AC11, AC17, EC10-EC12, EC22, EC26 | pass |
| T14 | 7 | scores stored before write; template on write failure or no time | spec | AC12, AC13, EC13 | pass |
| T15 | 7 | fresh generating 409, race 409, insert race 409, stale takeover with/without scores, lost claim stores nothing | spec | AC4, AC5, EC6-EC8, EC14, EC30 | pass |
| T16 | 7 | 429, 503, LLM off still returns a generated feedback, GET states | spec | AC16, AC18, EC25, EC27, EC28 | pass |
| T17 | 7 | injection cannot move the overall; fencing; follow-up threads; mixed categories | spec | AC9, AC14, EC16-EC21 | pass |
| T18 | 7 | no private text in logs, one summary line; trace ids-only input, metadata output, two scores | spec | AC20, plan 5 | pass |
| T19 | 6 | foreign key declares the cascade, session_id unique | code-derived | AC19, EC24 | pass |
| T20 | 5 | a feedback request is not listed as a failed turn in interview_report | code-derived | plan 5 | pass |
| T21 | 8 | cases cover every kind, labels validated, bands and criteria checks, insufficient by code, template and error reporting | spec | AC22 | pass |
| T22 | 8 | summary, spread, dataset items, trace input/output, scores, main with repeats, Langfuse outage | spec | AC22, plan 8 | pass |

## Open Questions
- Step 9: the rubric anchors, the two prompts and the expected bands are drafts -> needs review from: the user.
- Step 6/10: may the migration be applied to (and rolled back on) the local Postgres, and may the opt-in eval run spend real calls? -> needs decision from: the user.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: expects `llm_max_tokens` default 800, `config.py` says 4000 (`.env.example` says 800). Pre-existing, not touched by this feature.

## Known Issues
- EC15 (a client that disconnects during generation): expected to finish and store, since Starlette does not cancel a sync route's threadpool work; not yet checked by hand (Step 10).
- A sync POST holds a threadpool worker for up to the feedback budget (60 s); the per-user limit (3 per minute) does not cap load across users.
- Langfuse, when enabled, receives the score call's prompt (answers and job description), as it already does for interview turns.

## Deviations from Plan
- Finding: `tests/modules/auth/test_me.py` also hard-codes the interview permissions -> updated with Step 1 -> plan.md updated.
- Finding: labelling feedback requests in `turns_of` would add their cost to the report's turn totals (feedback cost in reports is out of scope) -> they are left out instead -> plan.md updated.
- Finding: the section labels must be importable by the prompt renderer without a cycle -> they live in `interviews_constants.py` -> plan.md updated.
- Finding: the feedback eval task has its own case and result types, so the shared runner loop would need a branch at every step -> `interviews_feedback_evals.py` holds the cases, checks, summary, spread and Langfuse helpers; `interviews_evals.main` hands `--task feedback` to it; the other tasks are untouched -> plan.md updated.
- Finding: only a `generated` row shows scores and text -> a half-written or stale `generating` row never shows partial scores (consistent with AC10).
- Steps tagged `first` were run as red -> green per seam (all of a seam's slices red together, then the code), not one slice at a time; every test was seen failing for the right reason first.
- Added on request (2026-11-05): clearer Langfuse traces. `Tracer.step` (a `chain` per call: score, write) and `Tracer.check` (a `guardrail` per reply with the code's verdict) in `app/core/ai/tracing.py`; every generation now records `model_parameters` (max_tokens, temperature) and its attempt number; the feedback trace has the tag `feedback`, the rubric version as metadata and an explicit `outcome`. Tests: 5 in `tests/core/ai/test_tracing.py`, 3 in `test_feedback_endpoint.py`, eval trace shape in `test_feedback_evals.py`. Full suite after: 1180 passed, 1 skipped, the same baseline failure.
- Added on request (2026-11-05): hints like the decide and write evals. `hint_for(code)` in `interviews_feedback_turn.py` (one hint per reason code, provider error and budget failure) on every rejected check and failed step of a live trace; `feedback_hints_for` in eval trace outputs and under failing cases in the console; `write_failure` kept on eval results so a template caused by a rate limit is told apart from a bad text. Tests: `test_feedback_hints.py` (code-derived: every reason code the contract raises must have a hint), plus endpoint, eval and tracing assertions. Full suite after: 1198 passed, 1 skipped, the same baseline failure.
- Eval finding (2026-11-06): in `mixed-strong-and-weak` the score call failed with `invalid_reply:quote_length` on both attempts. The Langfuse trace showed the `structure` quote was the whole 458-character answer, because structure spans the answer and no single sentence shows it. The fix is a new prompt `feedback_score_v2.md`: quotes are one sentence or part of one, with no evidence item when no single sentence shows a criterion. The role line says "completed" instead of "finished", so every prompt keeps its own role line. `FEEDBACK_SCORE_PROMPT_VERSION` now points at v2, v1 is kept, and the two endpoint tests read the constant. Interview tests: 917 passed. **Pending:** the eval with `--repeat 3`, to keep v2 or go back to v1 (see `docs/evaluation-guide.md`, section 8).
- Eval finding (2026-11-06): `same-answer-senior` was outside its expected range (2–3.5) in 5 of 5 scored runs: 4.4, 3.9, 4.3, 3.6, 4.0. The junior scored 4.5 every time. Langfuse showed two causes:
  - **Quality:** the model applies the soft experienced lines unevenly, sometimes within one call. In one run, Q1 depth was 3 ("without deep internals") and Q2 depth was 4 ("internals like resource sharing").
  - **Label:** the 3.6 run applied the lines exactly and still failed.

  Labels changed:
  - The senior's overall range is now 2.5–4.0. With depth and trade-offs at 3 and correctness and clarity at 4 or 5, a fair overall is 3.5–4.0.
  - New per-criterion ranges cap depth and trade-offs at 3 on both questions, which tests the experienced lines directly.
  - New eval check `level_gap`: a case with `lower_than` must score at least `LEVEL_GAP` = 0.5 below its earlier paired case in the same repeat. The case loader rejects a `lower_than` that doesn't name an earlier case. The check is skipped when either case has no overall, since that failure is reported separately.

  Replayed on the 5 runs, the new labels fail 4 of them and name the criterion that's too high; only the 3.6 run passes. 6 new tests in `test_feedback_evals.py`; interview tests: 923 passed. **Next:** rubric v2, with the depth and trade-off experienced lines worded as caps. Do it after the v2 prompt decision.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| setup | find-skills | Searched for LLM-judge, rubric, structured-output and Alembic skills; nothing above the quality bar beyond the installed ones (the only 1K+ match, `refoundai/lenny-skills@ai-evals`, is product strategy, not code), so none installed |
| all | lean-ctx | reads, searches, edits (ctx_patch), test and lint runs |
| 7 | graphify | `graphify update .` after the code changes |

## Links
- Spec: docs/features/interview-feedback/spec.md
- Plan: docs/features/interview-feedback/plan.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete (9 and 10 open)
- [x] Full test suite green apart from the recorded baseline failure
- [ ] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (AC19's delete on Postgres and AC22's real-model results are open)
- [x] Open Questions surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [x] learnings.md written (pending measurements marked, matching Tests Pending)
- [ ] Commits documented (the user commits)
- [ ] No open blockers (the review gate)
- [x] Code follows project rules (CLAUDE.md; no `.claude/rules/`)
- [x] No unresolved plan deviations
