# Implementation: Error Handling

## Status
Ready for PR (9 of 9 steps complete)

## Completed Steps
- [x] 1. Test tooling: pytest dev dependency, `[tool.pytest.ini_options]` (pythonpath, testpaths), `tests/conftest.py` with test-only routes, `client` and `app_logs` fixtures
- [x] 2. Settings: `debug: bool = False`; `DEBUG=true` in `.env.example`
- [x] 3. Error classes: `app/core/errors.py` (general + JWT 401 family, `ClassVar` attributes, `ErrorResponse`)
- [x] 4. Logging: `app/core/logging.py` (request ID filter, console + rotating `logs/app.log`, uvicorn access log silenced); `logs/` gitignored
- [x] 5. Exception handlers: `app/core/exception_handlers.py`
- [x] 6. Request context middleware: `app/core/middleware.py`
- [x] 7. Wire up `app/main.py` (done first, see Deviations)
- [x] 8. Auth module: `ConflictError` in the controller; `ErrorResponse` documented on the router and route
- [x] 9. Verify: full suite green; live server checked

## Test Results
25 passed (`uv run pytest`, 0.14s). Full suite run at finalize.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 5 | AppError returns standard shape | spec | AC1 | pass |
| T2 | 5 | 401 sends `WWW-Authenticate: Bearer` + specific code | spec | AC2 | pass |
| T3 | 5 | 422 lists each broken field as `{field, issue, type}` | spec | AC3 | pass |
| T4 | 5 | Validation response never echoes submitted values | spec | AC4 | pass |
| T5 | 5 | Malformed JSON → readable 422, raw body not echoed | spec | EC3 | pass |
| T6 | 5 | 404 / 405 use the standard shape | spec | AC5 | pass |
| T7 | 5 | IntegrityError → generic 409, no DB text | spec | AC6 | pass |
| T8 | 5 | OperationalError → 503 `DATABASE_UNAVAILABLE`, no DB text | spec | AC19 | pass |
| T9 | 5 | Crash → generic 500, `details` null with DEBUG off | spec | AC7 | pass |
| T10 | 5 | Crash `details` shows type + message with DEBUG on | spec | AC8 | pass |
| T11 | 5 | AppError log line names file, line and function | spec | AC17 | pass |
| T12 | 6 | Generated request ID matches header and body | spec | AC9 | pass |
| T13 | 6 | Safe client request ID is reused | spec | AC10 | pass |
| T14–17 | 6 | Unsafe client IDs (space, `;`, 65 chars, empty) are replaced | spec | AC11 | pass |
| T18–21 | 6 | `X-Request-ID` sent exactly once (200, 409, 404, 500) | spec | AC12, EC1 | pass |
| T22 | 6 | One access log line per request with request ID | spec | AC13 | pass |
| T23 | 6 | Crash log record carries the real request ID | spec | AC16 | pass |
| T24 | 8 | Duplicate email → 409 with `details.field = "email"` | spec | AC14 | pass |
| T25 | 8 | OpenAPI documents 409/422/500 as `ErrorResponse` | spec | AC15 | pass |

Verified manually in Step 9 (live uvicorn):
- AC18: lines written to `logs/app.log`; searching for a client-sent ID (`manual-check-1`) returned the error line and the access line
- EC2: server starts normally (lifespan scope passes through the middleware)
- uvicorn's own access lines no longer appear in the console

## Open Questions
- None

## Baseline Failures
- None (no tests existed before)

## Known Issues
- Running the tests also appends to `logs/app.log`, because `app.main` configures logging at import. Harmless (file is gitignored and rotated); revisit if test noise in the log becomes annoying.
- On a crash, uvicorn still prints its own traceback in addition to ours (Starlette re-raises after the 500 response). Accepted in the plan.

## Deviations from Plan
- Finding: every test imports `app.main`, which imported the deleted modules → Step 7 (wiring) done first with stub modules, then the stubs were filled test-first. Plan intent unchanged.
- Finding: AC16 (crash log request ID) needs the middleware → its test lives in `tests/test_request_context.py` (Step 6) instead of Step 5. The handler code for it was written in Step 5.
- Finding: Pylance rejects specific exception types in `add_exception_handler` (Starlette's handler type is invariant) → handlers are registered from a list typed `Any`, with a comment explaining why.
- Finding: `AppError` needs per-instance headers without touching the `ClassVar` → instances expose `response_headers` (class headers merged with per-raise headers).
- Finding: `caplog` can't see the non-propagating `app` logger and lacks the request ID filter → the `app_logs` fixture attaches caplog's handler to `app` with `RequestIdFilter`, mirroring the production handlers.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 5, 6, 8 | tdd (rules) | Red → green per slice at the confirmed HTTP + caplog seam |
| all | lean-ctx | Commands and test runs |

## Suggested Commit
feat: add structured error handling with request IDs

- AppError hierarchy (general + JWT 401 family) and ErrorResponse schema
- Exception handlers: AppError, validation (no input echo), 404/405,
  IntegrityError (409), OperationalError (503), unhandled (500, DEBUG-gated details)
- Pure-ASGI request context middleware: safe X-Request-ID reuse, one access log line
- Logging with request ID on every line, console + rotating logs/app.log
- Auth register raises ConflictError; errors documented in OpenAPI
- pytest suite (25 tests)

## Links
- Spec: none (approved by user)
- Plan: docs/features/error-handling/plan.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite green (no build step in this project)
- [x] Every acceptance criterion met by code and covered by a passing test, or verified manually (AC18, EC2)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; no baseline failures
- [x] task.md fully updated
- [ ] Commits documented (user commits manually)
- [x] No open blockers
- [x] Code follows project rules (no .claude/rules in this repo)
- [x] No unresolved plan deviations
