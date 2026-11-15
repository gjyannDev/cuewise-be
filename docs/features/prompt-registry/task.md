# Implementation: Prompt Registry

## Status
Ready for PR (all 11 steps done; uncommitted, for your review). Next: `/review-feature`.
Health Check: missing: caveman -> fallback: normal chat; missing: verification-before-completion -> fallback: the gate-command rule

## Completed Steps
- [x] 1. Record the baseline
- [x] 2. Shared cached loader in core
- [x] 3. Registry module and guard tests
- [x] 4. Old names become aliases
- [x] 5. Lazy loading in `interviews_utils.py`
- [x] 6. Startup check
- [x] 7. Run the check at app start
- [x] 8. Wire the routing into `interviews_context.py`
- [x] 9. Evals read the registry
- [x] 10. Profile module uses the shared loader
- [x] 11. Final guard and close-out

## Current Step
None: finalized.

## Changes Made
- Uncommitted (branch `feat/rag-integration`, as asked). Suggested commits:
  1. `feat(core): shared cached load_prompt for versioned prompt files` — `app/core/ai/prompts.py`, `tests/core/ai/test_prompts.py`
  2. `feat(interviews): prompt registry with catalog, routing tables and guard tests` — `interviews_prompt_registry.py`, `interviews_constants.py`, `tests/modules/interviews/constants/test_prompt_registry.py`
  3. `refactor(interviews): load prompts lazily and check every routed prompt at startup` — `interviews_utils.py`, `interviews_prompt_utils.py`, `app/main.py`, `test_prompt_check.py`, `tests/test_startup_prompts.py`, `test_interviewer_messages.py`
  4. `refactor(interviews): context, evals and profile read versions from the registry` — `interviews_context.py`, the three tooling files, `profile_extract.py`, `test_generation_arms.py`
  5. `docs(interviews): prompt registry spec, plan, task and learnings` — `docs/features/prompt-registry/`
- `graphify-out/` was refreshed by `graphify update .` (commit or discard as you usually do).

## Test Results
- Step 1 baseline: `uv run pytest`: 2343 passed, 6 skipped, 1 failed (baseline, below). `ruff check .`: 66 errors, all pre-existing; the gate for this feature is "no ruff error in a touched file".
- Step 2: red (ImportError, module missing), then green: `tests/core/ai/test_prompts.py` 4 passed, `tests/test_layers.py` green, ruff clean.
- Step 3: red (ImportError, registry missing), then green: `tests/modules/interviews/constants` + layers 43 passed; ruff: one unsorted import fixed with `--fix`, then clean.
- Step 4: `tests/modules/interviews` + layers 1768 passed, 5 skipped; ruff clean on `constants/` and its tests.
- Step 5: `tests/modules/interviews tests/core tests/live tests/test_layers.py`: 2119 passed, 6 skipped, 1 failed (baseline `test_config`); the recorded no-profile fingerprints in `test_profile_context.py` pass unchanged. Ruff clean.
- Step 6: red (ModuleNotFoundError), then green: `test_prompt_check.py` + layers 13 passed; ruff: one import sort fixed, then clean.
- Step 7: `tests/test_startup_prompts.py` 2 passed, with `test_tracing_lifespan.py` and layers 13 passed; ruff: one nested `with` merged (SIM117), then clean.
- Step 8: `tests/modules/interviews/ai routes controllers` + layers 985 passed; fingerprints unchanged, no test edited; ruff clean.
- Step 9: `tests/modules/interviews/tooling` 323 passed (332 with layers); `interviews_evals --help` runs; ruff: two import sorts fixed, then clean.
- Step 10: `tests/modules/profile`, `test_profile_redaction.py`, layers: 159 passed; ruff clean.
- Step 11: `tests/modules/interviews/constants` 37 passed (AST literal scan finds none outside the registry).
- **Final full suite:** `uv run pytest`: 2366 passed, 6 skipped, 1 failed (baseline `test_config`). +23 tests vs baseline.
- `ruff check` on every changed/new Python file: clean; `ruff check .`: 66 (= baseline).
- `git diff --stat -- app/modules/interviews/prompts app/modules/profile/prompts alembic/versions`: empty (AC11).
- `graphify update .`: done.

## Tests Pending
- None. No eval run: no prompt text or payload changed (fingerprints prove it).

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 2 | returns the text of `<dir>/<version>.md` | spec | AC9 | pass |
| T2 | 2 | second call does not reread the file (cache) | spec | plan step 2 | pass |
| T3 | 2 | same version in two directories gives two texts | inferred | risk: cache key without the directory | pass |
| T4 | 2 | unknown version raises FileNotFoundError naming the path | spec | EC13 | pass |
| T5 | 3 | file without entry / entry without file named (synthetic) | spec | EC1, EC2, AC6 | pass |
| T6 | 3 | entry with no reason or wrong name named (synthetic) | spec | AC1, AC6 | pass |
| T7 | 3 | route to archived or unknown version named (synthetic) | spec | EC3, AC6 | pass |
| T8 | 3 | table missing a variant named (synthetic) | spec | EC4, AC6 | pass |
| T9 | 3 | real catalog matches the 17 files | spec | AC1, EC1, EC2 | pass |
| T10 | 3 | real entries all have status and reason | spec | AC1 | pass |
| T11 | 3 | no real route is archived | spec | EC3 | pass |
| T12 | 3 | both real interviewer tables cover every variant | spec | EC4 | pass |
| T13 | 3 | routes equal today's versions | spec | AC2 | pass |
| T14 | 4 | each old `*_PROMPT_VERSION` equals its registry value | spec | AC10, EC11 | pass |
| T15 | 6 | the real prompts pass the check | spec | AC8 | pass |
| T16 | 6 | missing routed file named | spec | EC5 | pass |
| T17 | 6 | unsupplied placeholder named with version | spec | EC6 | pass |
| T18 | 6 | several problems in one error | spec | plan step 6 | pass |
| T19 | 7 | the app starts with the shipped prompts | spec | AC8 | pass |
| T20 | 7 | a failed check stops startup before the tracer/provider is built | spec | AC8, EC5, EC6 | pass |
| T21 | 9 | arms A-E send v5, v7, v7, v8, v8 from the stream route | spec | AC5 | pass |
| T22 | 9 | `--prompt interviewer_v2` (archived) still runs and is recorded (existing test) | spec | EC7 | pass |
| T23 | 11 | a version literal is named, prose mentioning one is not (synthetic) | spec | AC3, AC6 | pass |
| T24 | 11 | no version literal in `app/` outside the registry | spec | AC3 | pass |

AC coverage: AC1-AC3, AC5, AC6, AC8-AC10 by the tests above; AC4 by the unchanged existing suite (one approved test edit); AC7 by the removed globals plus the passing prompt tests; AC11 by the empty `git diff --stat`; AC12 by the final gates. EC8-EC10 by the unchanged fingerprint and follow-up tests; EC12 by the profile tests; EC14 by `graphify update .`.

## Open Questions
- None.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (4000 != 800, unrelated config default).
- `ruff check .`: 66 pre-existing errors outside this feature's files.

## Known Issues
- The v2-style renderer still falls back to the archived `interviewer_v2` file when no template is passed (kept so behavior is unchanged, plan step 5); every app caller passes its own.
- Importing `interviews_context` still reads the routed prompts (its `CONTEXT_MANAGER` builds every strategy at import), so a missing JSON-route file fails at import before `check_prompts` runs. Spec AC7 only covers `interviews_utils`; noted in learnings §7.

## Deviations from Plan
- None beyond the two approved in the plan (one test edit in step 5; `WithInterviewData` signature unchanged, app call sites use keywords).

## Debug Log
- None (no step needed a second attempt).

## Review

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1 | lean-ctx | baseline commands; `interviewer_v6` reference search (none found) |
| 2, 3, 6 | tdd / test | red then green at the confirmed seams (`load_prompt`, the registry's public data, `check_prompts`) |
| 2-11 | ponytail | `functools.cache`; registry as plain data; no new test where an existing one covered EC7 |
| 11 | graphify | `graphify update .` |

## Links
- Spec: docs/features/prompt-registry/spec.md
- Plan: docs/features/prompt-registry/plan.md
- Learnings: docs/features/prompt-registry/learnings.md
