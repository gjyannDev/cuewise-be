# Implementation: Résumé-aware interview (Slice 8d)

## Status
**Code complete; waiting on your gate** (Steps 1–9c, 11, 12 done). Pending: Step 10, the real-model eval runs (yours, opt-in keys). Not "ready for PR" until their numbers are recorded in learnings §7 and the AC13 decision rule is applied.

## Completed Steps
- [x] 1. Flag on the session + migration (applied by you: `alembic current` = `667c6bd6bf94 (head)` on local `cuewise`)
- [x] 2. Profile → text, pure (`interviews_profile_utils.py`)
- [x] 3. `interviewer_v8.md` + `interviewer_v8_json.md` (rendering tested; behaviour pending the eval)
- [x] 4a. Context routing (`WithInterviewData`)
- [x] 4b. Token allowance and drop order
- [x] 5. Redact profile-carrying calls
- [x] 6. Start flow (409 `PROFILE_REQUIRED`, live read)
- [x] 7. Answer turns (live read before release)
- [x] 8. Retrieval quota merge
- [x] 9a. Eval plumbing: arms D and E (`--arms`)
- [x] 9b. Eval data and metrics (`interviews_profile_eval_metrics.py`, `generation_eval_profiles.json`)
- [x] 9c. Profile cases for the `retrieval` eval (5 cases, scored apart)
- [ ] 10. Real-model runs (yours)
- [x] 11. Docs (learning path §8d, new-interview-roles, evaluation guide, learnings.md)
- [x] 12. Verify

## Current Step
### Gate: Step 10, real-model runs (yours)
1. `uv run python -m app.modules.interviews.tooling.interviews_evals --task generation --arms C,D,E --repeat 3 --sheet blind_8d.md --note "8d baseline"`; rank `blind_8d.md` **before** opening the Langfuse runs, then `--task ranking --sheet blind_8d.md`.
2. `uv run python -m app.modules.interviews.tooling.interviews_evals --task retrieval --note "8d profile cases"`: job-description recall@5 / MRR must equal the last run; `profile cases` is the profile half's first baseline.
3. `--task write` on the two injection JD cases with the 8b injection page text (closes job-url AC12).
4. Decision rule (spec AC13): `guard D` and `guard E` must say `pass`; if E fails a guard D passes, set `RETRIEVAL_PROFILE_SLOTS = 0` and record why. Read every presumption flag by hand.
5. Paste the summary lines into learnings §7 (eval log).

## Changes Made
- Uncommitted. Suggested commits (see the final summary for the `git add` lists):
  1. `feat(interviews): use_profile opt-in flag on the interview session`
  2. `feat(interviews): résumé-aware interviewer_v8 with the candidate profile in main-question writes`
  3. `feat(interviews): profile half of the retrieval query by quota merge`
  4. `feat(interviews): generation eval arms D and E with profile metrics and guards; profile retrieval cases`
  5. `docs(interviews): résumé-aware interview task, learnings, eval guide and learning path`

## Test Results
- Step 1 red: 4 failed for the right reasons (`KeyError: 'use_profile'`, `AttributeError` on the model, 422 for the unknown field, response key set).
- Step 1 green: `test_create_interview.py` + `test_list_interviews.py` 93 passed. Strictness checked directly: `"true"`, `1`, `"yes"` refused as `bool_type`, not as an unknown field.
- Steps 2–9c: each slice red for the right reason first, then green (counts per step in the chat log); no step needed a second attempt.
- **Final full suite:** `uv run pytest`: 2343 passed, 6 skipped, 1 failed (baseline `test_config`). `test_turn_budget` passed this run.
- `tests/test_layers.py`: green (interviews reach the profile through `ProfileService` only).
- `ruff check` on all 40 changed/new Python files: clean.
- `uv run alembic upgrade head --sql`: 13 migrations, the new one is only `ADD COLUMN use_profile BOOLEAN DEFAULT false NOT NULL`.

## Tests Pending
- Step 10 real-model runs: `generation --arms C,D,E --repeat 3` (gain, guards, presumption flags, blind ranking), `retrieval` (JD unchanged + profile baseline), `write` injection JD cases. Numbers **pending** in learnings §7.
- AC7 / EC5 / EC6 / EC12 behaviour (the model ignores the injection, follows the JD on a mismatch, doesn't chase strengths): only the real-model eval can show it; unit tests cover the fence.
- Google AI Studio data terms before real users (not a code task).

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | flag omitted → stored and returned false | spec | AC1, AC3, EC2 | pass |
| T2 | 1 | flag false → stored and returned false | spec | AC1, AC3 | pass |
| T3 | 1 | `"true"`, `1`, `"yes"` → 422, nothing created | spec | AC1 | pass |
| T4 | 1 | flag plus an unknown field → 422 | spec | AC1 | pass |
| T5 | 1 | row inserted without the column reads false (server default) | spec | AC3, EC11 | pass |
| T6 | 1 | session response key set includes `use_profile` | spec | AC3 | pass |
| T7 | 2 | block: every kept field in order; org/period never sent | spec | AC4, AC7 | pass |
| T8 | 2 | fake `</candidate_profile>`, `<job_description>`, `<reference_notes>` neutralised; block closes once | spec | AC7, EC5 | pass |
| T9 | 2 | skills-only, roles-only, project name-only/tech-only blocks, no placeholders | spec | EC8 | pass |
| T10 | 2 | query text: short items only, stable order, case-insensitive dedupe, None when empty | spec + inferred | AC15, AC16 | pass |
| T11 | 3 | v8/v8_json: six sections, every placeholder filled (all roles × levels × types), no "developer", role line differs from v7, profile rules present, JSON example parses, only reply format differs | spec | AC4, EC6, EC7, EC12 | pass |
| T12 | 4a | golden: 28 no-profile builds (JSON, stream, decide × notes × turns × mode) byte-identical to before v8 | spec | AC5, EC2, AC13 | pass |
| T13 | 4a | profile → v8, block after JD (and after notes), data-only rule, counts profile=1 | spec | AC4, EC13 | pass |
| T14 | 4a | follow-up writes and decide never carry the profile; byte-identical to no-profile | spec | AC6 | pass |
| T15 | 4b | allowance covers the max-size profile; largest interview + 6 max notes + max profile keeps both | spec | plan 4b | pass |
| T16 | 4b | drop order history → profile → notes; neither block can make the input too large | spec | plan 4b | pass |
| T17 | 5 | traced main write with profile: input/output redacted, version and usage kept; without profile / follow-up: full | spec | AC10, AC6 | pass |
| T18 | 6 | flag on, no profile → 409 PROFILE_REQUIRED, no row, no LLM or embed call; in-progress interview untouched | spec + inferred | AC2, EC1 | pass |
| T19 | 6 | another user's profile doesn't count; two users each get only their own | spec | AC8, EC10 | pass |
| T20 | 6 | stored profile that no longer validates → treated as none, metadata-only warning | inferred | plan risk | pass |
| T21 | 6 | flag on → first write v8 with the block, no organization; flag off never reads/sends it; LLM off → bank, nothing stored | spec | AC4, EC2, EC9 | pass |
| T22 | 6, 7 | no profile marker in logs or responses | spec | AC10 | pass |
| T23 | 7 | each turn reads live: deleted → profile-free v4; replaced → new markers; stream route too | spec | AC9, EC3, EC4 | pass |
| T24 | 7 | follow-up turn and its decide call carry no profile | spec | AC6 | pass |
| T25 | 8 | merge: cap, dedupe, unused slots back to JD, short JD never profile-led, 0 slots = today | spec | AC15, EC17 | pass |
| T26 | 8 | retrieve: one batched embed with both queries; no-JD profile alone with full k; JD below threshold → filter; embed error → filter | spec | AC15, EC7, EC14, EC16 | pass |
| T27 | 8 | trace/log: profile_notes count and ids, never the query | spec | AC16 | pass |
| T28 | 8 | route: start embeds [JD, profile] in one call; notes unchanged after profile delete; flag off = [JD] | spec | AC15, EC15 | pass |
| T29 | 9a | `--arms` parsing (case, order, unknown, repeated, single); N-label sheet and key; ranking must name every label | spec + inferred | AC12 | pass |
| T30 | 9a | `--arms C,D,E` run: one Langfuse run per arm, v7/v8/v8, profile only in D and E, E's retrieval embeds 2 texts; no `--arms` = today's A,B,C | spec | AC12 | pass |
| T31 | 9b | profile-only mentions (JD overlap excluded, whole terms, `java` ≠ `javascript`, `C++`, `Node.js`); presumption phrases; injection; Jaccard; spread | spec | AC12 | pass |
| T32 | 9b | guard: within / at / beyond C's spread; injection obeyed fails; refused below 3 repeats | spec | AC13 | pass |
| T33 | 9b | run: extra setups only with D/E; every arm (C too) scored; console table and refused guards at 1 repeat | spec | AC12, AC13 | pass |
| T34 | 9c | shipped profile cases valid; non-short-item queries refused; JD averages exclude profile cases; no profile cases = today's scores | spec + inferred | AC12 | pass |

## Open Questions
- None.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`
- `tests/modules/interviews/routes/test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` (real clock; passed in this step's run)

## Known Issues
- None.

## Deviations from Plan
- Step 8: `merge_note_rankings` returns `(notes, profile_count)` instead of only the notes. Counting profile notes afterwards is ambiguous (a note can be in both rankings), and the count is needed for the log/trace (AC16). Plan intent unchanged.
- Step 4a: `build_interviewer_messages` takes the rendered `profile_block` string, not the profile, to avoid a circular import (`interviews_profile_utils` → `interviews_utils`). Same output.
- Step 6/7: interviews services take `profiles: ProfileService | None` (None = no profile source, used by direct-construction tests and evals); DI always passes it.
- Step 9a: `--arms` defaults to `A,B,C` (today's run), not all five: keeps cost and the existing runs unchanged; 8d runs pass `--arms C,D,E`. `ARMS` became `DEFAULT_ARMS` (two test imports aliased).
- Step 9b: the plan's three new setups became two (injection, mismatch). The no-job-description case (EC7) is already covered by `near-empty-data-intern` and `complete-behavioral-junior`. The extra setups live in `generation_eval_profiles.json` (not the shared `eval_cases.json`, which would change the write/decide evals) and run only with D or E.
- Step 9c: retrieval run scores average job-description cases and profile cases apart (`profile_vector_*`), and the threshold sweep stays JD-only, so the JD numbers stay comparable with earlier runs.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 0 | find-skills | Installed set already covers the slice; `timescale/pg-aiguide@pgvector-semantic-search` (1K installs) seen, not installed: retrieval SQL is reused unchanged |
| 1 | tdd | Red → green at seam S4 |
| 1 | sqlalchemy-alembic-expert-best-practices-code-review | Migration review |
| 3 | (plan's llm-security / prompt-engineering findings applied, not reloaded) | v8 rules: data-only block, no presumption, no quoting |
| 9a–9c | (plan's llm-evaluation findings applied) | Baseline arm measured the same way, noise margin, deterministic flags |

## Links
- Spec: docs/features/resume-aware-interview/spec.md
- Plan: docs/features/resume-aware-interview/plan.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete
- [ ] Full test suite + build green (not just per-step tests)
- [ ] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (or verification noted)
- [ ] Open Questions resolved or explicitly surfaced to the user
- [ ] No skipped, deleted, or loosened tests; baseline failures listed separately
- [ ] task.md fully updated
- [ ] learnings.md written; pending measurements marked and matching Tests Pending
- [ ] Commits documented
- [ ] No open blockers
- [ ] Code follows project rules
- [ ] No unresolved plan deviations
