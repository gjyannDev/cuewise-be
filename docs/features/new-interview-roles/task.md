# Implementation: Three New Interview Roles (designer, qa, devops)

## Status
Ready for your review. All 6 steps built and tested; nothing committed.

## Completed Steps
- [x] 1. Add the roles and their voice terms: `JobRole.designer/qa/devops`; a keyterm tuple each (14-15 terms, none repeating `SHARED_KEYTERMS`).
- [x] 2. Bank questions: `des-tech-01/02`, `qa-tech-01/02`, `devops-tech-01/02` in `data/questions.json` (01: intern-mid, 02: mid-senior). **Please review the wording.**
- [x] 3. API acceptance: no schema change needed; route tests added.
- [x] 4. Retag the notes: `qa-testing-fundamentals.md` -> qa, `devops-platform.md` -> devops, `ux-design-collaboration.md` -> designer; `note-guide.md` and `note-template.md` updated.
- [x] 5. Fill the missing band: `qa-test-strategy.md` (qa, mid/senior), `devops-fundamentals.md` (devops, intern/junior), `designer-fundamentals.md` (designer, intern/junior), all `source: drafted`, 5 sections each. **Please review.**
- [x] 6. Wrap-up: full suite, ruff, `graphify update .`, learnings.md.

## Changes Made
Not committed (you commit). Suggested message:

    feat(interviews): add designer, qa and devops interview roles

    Candidates can now practise as a UI/UX designer, a quality engineer or a DevOps engineer. Each role gets
    voice keyterms, two technical bank questions covering every level, and reference notes for every level:
    one note from real job postings and one drafted note per role. The role columns are plain strings, so no
    migration. Prompts still say "{{role}} developer role" until interviewer_v8 (8d, profile interviews only).

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

## Test Results
- Baseline before Step 1: `uv run pytest tests/modules/interviews tests/test_layers.py -q`: 1097 passed, 5 skipped, 1 failed (corpus gate).
- Step 1: red: `test_keyterms.py` `KeyError` for the three roles (and `set(ROLE_KEYTERMS) != set(JobRole)`); green after the keyterms.
- Step 2: red: `test_every_role_has_its_own_technical_question_at_every_level` failed for exactly the 12 new role/level pairs and `test_shipped_bank_covers_every_type_role_and_level`; green after the 6 questions (177 passed in constants + bank + select tests).
- Step 3: 42 passed in `test_create_interview.py` (9 new cases). Red shown before Step 1: the old unknown-role test sent `devops` and got 422.
- Step 4: red: the new retrieval test failed "no designer/qa note covers <level>" for all 12 cases; after retagging, the 6 covered bands passed and the 6 missing bands failed (Step 5's work).
- Step 5: `test_retrieval_service.py`, `test_shipped_corpus.py`, `test_knowledge_utils.py`: 108 passed, 1 failed (the 8a gate).
- Final: `uv run pytest`: **1520 passed, 6 skipped, 3 failed**: the 2 baseline failures plus `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` (see Known Issues: environment-dependent, not this feature).
- `uv run --with ruff ruff check` on the touched Python files: all checks passed.

## Tests Pending
- E3 (by hand, yours): after `alembic upgrade head` and the next ingest on the dev database, the three retagged notes count as changed (roles are part of the hash), old rows retired, new rows embedded.
- Real-model check of how the new roles read with the "developer role" prompt wording (one start per role).

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | every role, new ones included, has keyterms: shared terms once, under Deepgram's limit, plain text | spec | G4 | pass |
| T2 | 2 | the shipped bank covers every role | spec | G2 | pass |
| T3 | 2 | every role has its own technical question at every level | spec | G2 | pass |
| T4 | 2, 3 | an unknown role (`sre`) is refused by the bank loader and by the API | spec | G1, E5 | pass |
| T5 | 3 | a new role starts a technical interview from the shipped bank (intern and senior) | spec | G1, G2 | pass |
| T6 | 3 | a new role is echoed by get and list | spec | G1 | pass |
| T7 | 4, 5 | a new role gets role or general notes only, never another new role's, at every level | spec | G3, E4 | pass |
| T8 | 4, 5 | each new role has a role-specific note at every level | spec | G3 | pass |
| T9 | 5 | every role and level still has at least 6 eligible notes (existing test) | spec | E2 | pass |
| T10 | 4 | corpus loads with no warning after retagging (existing test) | spec | G3 | pass |
| T11 | - | no migration needed: `role` columns are `String(32)` | code-derived | E1 | verified by reading the models |

## Open Questions
- None blocking. Bank question and drafted-note wording await your review.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (older, unrelated).
- `tests/modules/interviews/utils/test_shipped_corpus.py::test_at_least_a_third_of_the_shipped_notes_are_not_drafted` (8a gate; now 3 of 21 non-drafted, 7 needed).

## Known Issues
- `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` fails on this machine (`budget_left_ms=29998`, expected `30000`). It uses the real clock, not the `clock` fixture, so it needs under 0.5 ms between deadline and decide call. Checked: the same code and tests (this whole diff) pass 3/3 on a clean `git archive` copy without the local `.env`; `DEBUG=false` and blank Langfuse keys did not change it. Passed in this morning's baseline run. Not caused by this feature; fix separately by giving the test the `clock` fixture.
- Prompts say "{{level}} {{role}} developer role" (accepted; `interviewer_v8`, Slice 8d, for profile interviews).

## Deviations from Plan
- Finding (Step 1): `test_question_bank.py` (unknown-role case) and `test_create_interview.py` (unknown-role case) used `devops` as their sample unknown role. -> Sample changed to `sre`; the assertion (unknown role refused) is unchanged, so no test was loosened. -> Approved by: pending your review.
- Finding (Step 2): a per-role, per-level technical-question test was added for every role, not only the new ones; the existing five roles already satisfied it. -> plan Step 2 slice (b) implemented as that test plus the route test at intern and senior.
- Finding (Steps 4-5): the "role-specific note at every level" check lives in the retrieval test (`eligible_own`) rather than a separate shipped-corpus test, so one test covers scoping and coverage. The test also asserts headings are unique across notes, because it maps picked notes back by heading.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | implement, lean-ctx, graphify | workflow, reads/edits/shell, dependency map and `graphify update .` |

## Links
- Plan: docs/features/new-interview-roles/plan.md (no spec.md, approved)
- Learnings: docs/features/new-interview-roles/learnings.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [ ] Full test suite green: 2 baseline failures + 1 environment-dependent timing test (Known Issues)
- [x] Every goal met by actual code and covered by a passing test (E1 verified by reading the models; E3 pending by hand)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [x] learnings.md written; pending measurements marked and matching Tests Pending
- [ ] Commits documented (yours)
- [x] No open blockers
- [x] Code follows project rules
- [ ] No unresolved plan deviations (one awaits your OK)
