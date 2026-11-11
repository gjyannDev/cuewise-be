# Implementation: Split interviews_dependencies.py by responsibility

## Status
Ready for review (Step 7 of 7). Not committed: the user reviews and commits.

## Completed Steps
- [x] 1. Baseline: 1411 passed, 6 skipped, 2 known failures (listed below)
- [x] 2. `interviews_shared_dependencies.py` (59 lines)
- [x] 3. `interviews_start_dependencies.py` (70 lines)
- [x] 4. `interviews_answer_dependencies.py` (52 lines)
- [x] 5. `interviews_transcription_dependencies.py` (54 lines), `interviews_feedback_dependencies.py` (82 lines)
- [x] 6. Route, 5 test files and the `tests/test_layers.py` label repointed; `interviews_dependencies.py` deleted
- [x] 7. Verified (see Test Results)

## Changes Made
Not committed. Suggested message:

    refactor(interviews): split interviews_dependencies.py by use case, no behavior change

    One shared file (app.state lookups and small providers) and one file per use case (start, answer,
    transcription, feedback); each rate limiter sits with its guard. Importers repointed, no re-export facade.

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

## Test Results
- Full suite: 1411 passed, 6 skipped, 2 failed. Identical to the baseline.
- `tests/test_layers.py` + `tests/modules/interviews/routes`: 322 passed.
- Ruff on the dependencies, routes, interviews tests and `tests/test_layers.py`: clean. The first run flagged 5
  import-order issues (I001) that this change introduced; fixed with `ruff check --select I001 --fix` on those files.
- No reference to `interviews_dependencies` left in `app/` or `tests/`.
- `graphify update .` run.

## Tests Pending
- None. Pure move: the existing suite is the check.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 7 | Full suite matches the baseline | spec | G1 | pass |
| T2 | 7 | Layer rules hold for the new files | spec | G3 | pass |
| T3 | 7 | Every importer resolves; old module name gone | spec | G4, G5 | pass |

## Open Questions
- None.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (pre-existing)
- `tests/modules/interviews/utils/test_shipped_corpus.py::test_at_least_a_third_of_the_shipped_notes_are_not_drafted`
  (Slice 8a Step 11 gate, red until the corpus has own or posting notes)

## Known Issues
- None.

## Deviations from Plan
- None. All file names, contents and importers as planned. The feedback file is 82 lines, slightly over the
  "about 80" target in G2; it holds one use case, so it was left whole.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | ponytail | Pure move: no renames, no facade, no new tests |
| 6 | lean-ctx | Importer search and verification commands |
| 7 | graphify | Graph updated after the change |

## Links
- Plan: docs/features/split-interviews-dependencies/plan.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite green apart from the 2 listed baseline failures
- [x] Every goal (G1-G5) met and checked
- [x] Open Questions resolved
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [x] learnings.md written
- [ ] Commits documented (user commits)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md naming, layers, no re-exports)
- [x] No unresolved plan deviations
