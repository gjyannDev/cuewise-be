# Implementation Plan: Split interviews_dependencies.py by responsibility

> No spec.md exists for this refactor (the user said that is fine). The goals below (G1-G5) stand in for spec
> requirements, so the plan stays traceable. Size: small (a pure move of ~240 lines, 7 importer files).

## Overview
`dependencies/interviews_dependencies.py` has grown to 241 lines holding five unrelated concerns, so it is hard to
read and every new feature adds to it. Split it into small files by responsibility, with no behavior change.

## Goals (standing in for the spec)
- G1: No behavior change. Every route, response, status code and rate limit works exactly as before.
- G2: Each new file holds one responsibility and stays under about 80 lines.
- G3: Project rules hold: `interviews_<what>_dependencies.py` naming, empty `__init__.py`, no re-export facade, layers
  only call downward, features don't import each other's repositories (`tests/test_layers.py`).
- G4: Every importer (one route, five test files, one layer-test label) points at the new home of what it uses.
- G5: The old `interviews_dependencies.py` is gone, so nothing can quietly keep importing it.

## Architecture & Design
The file is the app's composition root: it builds each request's service and controller from shared parts. Split it
into one **shared** file (startup lookups and small providers every use case needs) and one file **per use case**
(start, answer, transcription, feedback). A rate limiter and the guard that uses it live together in the use case that
owns them. Dependencies point one way only: use-case files import the shared file; the shared file imports none of
them, so no import cycle can form.

## Spec Requirements -> Implementation
- G1 -> Steps 1-6, proved by Step 7 (full suite compared with the baseline)
- G2 -> Steps 1-5
- G3 -> Steps 1-5, checked in Step 7 (`tests/test_layers.py`, ruff)
- G4 -> Step 6
- G5 -> Step 6

## Implementation Steps
1. **Record the baseline.** Run the full suite and ruff on the touched folders before moving anything; save the
   pass/fail counts and the expected failures in task.md. Nothing changes in the code. — Test: skip
2. **Create `interviews_shared_dependencies.py`.** Move: `get_bank`, `get_llm_provider`, `get_transcriber`,
   `get_embedder`, `get_tracer`, `get_clock`, `get_now` (with `_utc_now`), `get_context_manager`. Keep docstrings
   unchanged. — Test: skip
3. **Create `interviews_start_dependencies.py`.** Move: `get_retrieval_service`, `get_interviews_service`,
   `get_interviews_controller`, `InterviewsControllerDep`. Imports the shared file. — Test: skip
4. **Create `interviews_answer_dependencies.py`.** Move: `get_answer_service`, `get_answer_controller`,
   `AnswerControllerDep`. — Test: skip
5. **Create the two limiter-owning files.**
   `interviews_transcription_dependencies.py`: `TRANSCRIPTION_LIMITER`, `get_transcription_limiter`,
   `limit_transcriptions`, transcription service, controller, `TranscriptionControllerDep`.
   `interviews_feedback_dependencies.py`: `FEEDBACK_LIMITER`, `get_feedback_limiter`, `limit_feedback`, feedback
   service, controller, `FeedbackServiceDep`, `FeedbackControllerDep`. The limiter singletons stay module-level, one
   instance per process, as now. — Test: skip
6. **Repoint every importer, then delete the old file.** Route, `tests/modules/interviews/conftest.py`, the three
   route tests and the label in `tests/test_layers.py` (see Affected Files). Then remove
   `interviews_dependencies.py`. No facade: the project forbids re-exports in layer folders. — Test: after
   (the existing tests are the check; no new test is needed for a move)
7. **Verify.** Full suite equals the baseline, `tests/test_layers.py` green, ruff clean on the new files and
   importers, no remaining reference to the old module name in `app/` or `tests/`, `graphify update .`. — Test: after

## Affected Files & Patterns
New (all in `app/modules/interviews/dependencies/`):
- `interviews_shared_dependencies.py` — startup lookups from `app.state` and small providers
- `interviews_start_dependencies.py` — retrieval service, interviews service, controller
- `interviews_answer_dependencies.py` — answer service, controller
- `interviews_transcription_dependencies.py` — limiter, guard, service, controller
- `interviews_feedback_dependencies.py` — limiter, guard, service, controller

Deleted: `interviews_dependencies.py`.

Importers to change (names each one uses, from a search of `app/` and `tests/`):
- `routes/interviews_route.py:22` — the four `*ControllerDep` aliases (one per new use-case file) plus
  `limit_feedback` and `limit_transcriptions`
- `tests/modules/interviews/conftest.py:17` — `get_bank`, `get_clock`, `get_llm_provider`, `get_transcriber` (shared)
  and `get_transcription_limiter` (transcription file)
- `tests/modules/interviews/routes/test_context_controller.py:15` — `get_context_manager` (shared)
- `tests/modules/interviews/routes/test_feedback_endpoint.py:35` — `get_context_manager`, `get_llm_provider`,
  `get_now`, `get_tracer` (shared) and `get_feedback_limiter` (feedback file)
- `tests/modules/interviews/routes/test_start_reference_notes.py:14` — `get_embedder` (shared)
- `tests/modules/interviews/routes/test_tracing_routes.py:12` — `get_tracer` (shared)
- `tests/test_layers.py:152` — only a label for a synthetic file path (the check never reads it); point it at the
  start dependencies file so it names a file that exists

Patterns to follow: the `interviews_*` file naming and empty `__init__.py` rule from CLAUDE.md; the way
`interviews_turn.py` was split in Slice 8a Step 1 (pure move, one commit, delegates only where a test needed them).

Risks:
- `dependency_overrides` matches by function identity. A test that imports a function from the new module still
  overrides it correctly, but one that keeps an old import fails loudly at import time (good: no silent miss).
- A test could patch a dependency by dotted-string path. A search for the old module name found only `import`
  lines, so none do now; Step 7 re-checks.
- Import cycle: avoided by the one-way rule above (use-case files import shared, never each other, and the route
  imports use-case files).
- Mixing this with other edits hides a regression. Do it on a clean working tree, as its own commit.

## Testing Strategy
- Framework & command: `uv run pytest` (full suite), then `uv run pytest tests/test_layers.py tests/modules/interviews -q`
  for a fast loop; lint with `uv run --with ruff ruff check app/modules/interviews/dependencies app/modules/interviews/routes tests/modules/interviews tests/test_layers.py`.
- This is a behavior-preserving move, so there are no new behaviors to test first. The existing suite is the
  safety net and is compared before and after.

| Goal | Step | Test mode | Notes |
|------|------|-----------|-------|
| G1 | 1, 7 | after | Same pass, skip and expected-failure counts as the baseline |
| G2 | 2-5 | after | Check line counts of the new files in Step 7 |
| G3 | 7 | after | `tests/test_layers.py` (its real-tree test scans the new files automatically) and ruff |
| G4 | 6 | after | Route and tests import and run; no `ImportError` |
| G5 | 6, 7 | after | A search of `app/` and `tests/` finds no `interviews_dependencies` |

- Must verify, not assume: rate limiting still applies to the transcription and feedback routes (their route tests
  cover it); `app.state` lookups still return `None` when the lifespan didn't run (existing tests).
- Open questions: none.
- Known baseline failures (as of the last full run before the RAG commit; re-measure in Step 1):
  `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`, and the Step 11 gate
  `test_at_least_a_third_of_the_shipped_notes_are_not_drafted`.

## Blockers & Resolutions
- No facade allowed, so old imports can't keep working -> update all seven importers in one step (Step 6).
- Which file owns a limiter -> the use case that uses it (transcription, feedback), so each limiter and its guard
  are read together.
- A name that two use cases share (`get_tracer`, `get_clock`) -> shared file, imported by both.
- Pure move, no `Test: first` step -> no test seam to confirm; no grill-me round was needed.

## Trade-offs & Rationale
- Five files, not six: a separate "limits" file would hold two small pieces that each belong to one use case, so
  they sit with their use case instead.
- Five files, not one per function: three functions per use case (service, controller, alias) read best together.
- No `dependencies/__init__.py` re-exports: the project rule bans them and they would hide where things live.
- Move first, improve later: no renames or signature changes, so the diff is reviewable as "same code, new place".

## Project Rules Applied
- CLAUDE.md "File naming": every file prefixed `interviews_`; layer folders keep an empty `__init__.py`.
- CLAUDE.md "Layers only call downward" and `tests/test_layers.py`: wiring files may import services,
  controllers and repositories of the same feature, nothing upward.
- CLAUDE.md Git rules: leave the changes in the working tree; the user reviews and commits.
- CLAUDE.md Tooling: lean-ctx for edits (`ctx_patch`), `graphify update .` after code changes.
- Memory: `ctx_patch` decodes `\uXXXX`; none of these files needs an invisible character.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | importers and the names each one uses (search of `app/` and `tests/`) |
| graphify | confirmed the module is a hub: imported by the route and several tests; no other app module uses it |
| ponytail | kept the plan to the smallest split that fixes readability: no facade, no renames, no new tests |

## Ready to Implement
- Goals G1-G5 mapped to steps; every step has a Test tag
- Affected files and the names each importer uses are listed
- Blockers resolved; no open questions
- Trade-offs documented
- Start from a clean working tree, as a separate commit from any other change
