# Implementation: Layered Modules (route -> controller -> service -> repository)

## Status
Ready for review (all 10 plan steps done). Not committed: you commit when you're happy with it.

## Completed Steps
- [x] 1. Baseline: 1207 collected; 1205 passed, 1 skipped, 1 failed (known); ruff 77 errors; OpenAPI (11 paths) and `Base.metadata` (5 tables) snapshotted.
- [x] 2. `CLAUDE.md` rules (tree, naming, layer direction, cross-feature entry is the service, ownership in services, lint command); `core/errors.py` and `core/ai/provider.py` docstrings.
- [x] 3. `tests/test_layers.py`: `check_layers` built test first (red: 7 rule tests failed against a stub returning `[]`; green after the implementation).
- [x] 4. `auth` and `users`: layer folders, `AuthService`/`UsersService`, thin `AuthController`/`UsersController`, `users/dependencies/` (the providers left the route), `create_admin` calls the service.
- [x] 5. `interviews` pure moves into `routes/ controllers/ services/ repositories/ schemas/ models/ dependencies/ utils/ constants/ ai/ tooling/`; `MODULE_DIR` replaces the five `Path(__file__).parent` loaders.
- [x] 6. `utils/interviews_session_utils.py`: `InterviewSetup`, `Thread`, `owned_session`, `interviewer_inputs`, `bank_question`, `llm_question` (the feedback service's duplicate owned-session check is gone).
- [x] 7. Split into `InterviewsService`, `AnswerService`, `TranscriptionService`, `FeedbackService`; services return domain values (`InterviewState`, `HistoryPage`, `Transcript`, `TurnResult`, `Reaction`, stream events, the feedback row).
- [x] 8. Four controllers (`InterviewsController`, `AnswerController`, `TranscriptionController`, `FeedbackController`) build every `*Out`, SSE frame and `feedback_out`; one `APIRouter` on four `*ControllerDep`.
- [x] 9. Tests mirror the layers: `tests/modules/<feature>/{routes,controllers,ai,tooling,utils,constants}/`; `conftest.py` stays at the module root.
- [x] 10. `docs/evaluation-guide.md` paths; stale "controller" wording in `ai/` docstrings; `graphify update .` run.

## Changes Made
Nothing committed. Suggested commit message:

    refactor(modules): layer folders and route -> controller -> service -> repository

    Every feature module gets one folder per layer. The old controllers become services (business rules,
    ownership, LLM orchestration, repository calls) behind thin controllers that build the response schemas
    and SSE frames. The 728-line interviews controller is split into lifecycle, answer, transcription and
    feedback services. A stdlib-ast test enforces the import direction. No API, schema or behavior change.

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

## Test Results
`uv run pytest`: 1214 passed, 1 skipped, 1 failed (the baseline failure below); 1216 collected = 1207 + 9 layer tests.
`uv run --with ruff ruff check .`: 64 errors (baseline 77; only import sorting and one unused import fixed in touched files).

## Tests Pending
- None. (Optional manual check: one live interview through the client, streamed answer included.)

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 3 | clean layer imports give no violations | spec | AC7 | pass |
| T2 | 3 | route importing a service or repository | spec | AC3, EC5 | pass |
| T3 | 3 | controller importing a repository, `app.core.ai` or the DB session | spec | AC3, EC5 | pass |
| T4 | 3 | service importing a controller or route | spec | AC3, EC5 | pass |
| T5 | 3 | service importing an `*Out` schema | spec | AC3 (approved extra rule) | pass |
| T6 | 3 | repository importing a service, controller or route | spec | EC5 | pass |
| T7 | 3 | feature importing another feature's repository | spec | EC5, EC6 | pass |
| T8 | 3 | layer file left at a module root | spec | AC1, AC2 | pass |
| T9 | 3-8 | real tree of auth, users, interviews follows the rules | spec | AC1, AC3, EC10 | pass |
| T10 | 1, 10 | OpenAPI and `Base.metadata` snapshot identical before/after | spec | AC9, EC3 | pass (byte-identical JSON) |
| T11 | 10 | `alembic check`: no new upgrade operations | spec | EC3 | pass (local DB) |
| T12 | 5, 10 | new evals CLI runs `--help`; old path fails "No module named" | spec | AC10, EC2 | pass |
| T13 | all | existing suite unchanged in assertions | spec | AC8, EC1, EC4, EC7, EC8, EC12 | pass |

## Open Questions
- None.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: expects `llm_max_tokens` 800, the default is 4000. Unrelated to this feature; left as is.

## Known Issues
- `tests/test_layers.py` defines `check_layers` inside the test module (it is test tooling, not app code).
- Three test files changed beyond import paths, wiring only: `test_register_errors` (builds service, then controller), `test_login` (patches `verify_password` in the service module), `test_stream_answer` (builds `AnswerController(AnswerService(...))`).

## Deviations from Plan
- Finding: after `record_turn` commits, the session and next-question rows are expired, and the streamed `done` response used to be built in the worker thread. -> Added `InterviewsRepository.refresh(*rows)`, called by `AnswerService.finish_answer` in that thread, so the controller maps loaded values on the event loop (the same two SELECTs, now explicit). Covers risk R1. -> plan.md design decision "services return fully loaded values" already required this; no plan text change needed.
- Finding: the users route defined its own `get_controller` with a DB session. -> Moved to a new `users/dependencies/users_dependencies.py`, so the route imports no session.
- Finding: tests also import with `from app.modules.<feature> import <module>`. -> The move script handles that form; one auth test was fixed by hand.
- Step 3 slices: all eight rule tests were written against a stub first and confirmed red together, then the checker was written once (not one slice at a time).

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| setup | find-skills | searched for refactor / FastAPI layering skills: none with meaningful installs (all under 30), none installed |
| all | lean-ctx | reads, searches, patches, shell |
| 10 | graphify | `graphify update .` after the change |

## Links
- Spec: docs/features/layered-modules/spec.md
- Plan: docs/features/layered-modules/plan.md
- Learnings: docs/features/layered-modules/learnings.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite green against the baseline (1 known unrelated failure)
- [x] Every spec.md acceptance criterion met by actual code and covered by a passing test or a recorded verification
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [x] learnings.md written
- [ ] Commits documented (you commit)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md updated by this feature)
- [x] No unresolved plan deviations
