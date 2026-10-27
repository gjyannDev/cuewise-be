# Implementation Plan: Error Handling

## Overview
A single, predictable error system for cuewise-be: every failure returns one JSON shape with a request ID that links the response to the server logs, so it's obvious what broke and where.

## Architecture & Design
Controllers raise typed `AppError` subclasses (no HTTP knowledge). FastAPI exception handlers turn each kind of error into the standard body `{error: {code, message, details, request_id}}`. A pure-ASGI middleware assigns a request ID per request, echoes it in `X-Request-ID`, and writes one access log line. A logging filter adds the ID to every log line through a context variable.

Layer order at runtime, outermost first: Starlette `ServerErrorMiddleware` (unhandled → 500 handler) → `RequestContextMiddleware` (ours) → `ExceptionMiddleware` (all other handlers) → router.

## Requirements (no spec.md: requirement and edge-case IDs are defined here)
- R1 One error body shape for every error response -> Steps 3, 5
- R2 Controllers raise domain errors, never `HTTPException` -> Steps 3, 8
- R3 General errors (400, 403, 404, 409) and the JWT 401 family (`INVALID_CREDENTIALS`, `TOKEN_MISSING`, `TOKEN_EXPIRED`, `TOKEN_INVALID`); every 401 sends `WWW-Authenticate: Bearer` -> Steps 3, 5
- R4 Validation errors return 422 with a flattened per-field list (`field`, `issue`, `type`) and never echo the submitted input -> Step 5
- R5 Unknown route / wrong method use the same shape (`NOT_FOUND`, `METHOD_NOT_ALLOWED`) -> Step 5
- R6 DB unique/FK violations return a generic 409 `CONFLICT`; the DB message goes to logs only -> Step 5
- R7 Unhandled exceptions return a generic 500 `INTERNAL_ERROR`; the full traceback is logged; type and message appear in `details` only when `DEBUG=true` -> Steps 2, 5
- R8 Every response carries exactly one `X-Request-ID`; the client's ID is reused only if it matches `[A-Za-z0-9_-]{1,64}` -> Step 6
- R9 One access log line per request (method, path, status, duration, request ID); uvicorn's duplicate access log is silenced -> Steps 4, 6
- R10 Plain-text logs with the request ID on every line -> Step 4
- R11 Error responses are documented in OpenAPI via an `ErrorResponse` schema -> Steps 3, 8
- R12 The middleware stays safe for streaming responses (no `BaseHTTPMiddleware`) -> Step 6
- R13 The crash (500) log line carries the real request ID, not `-` -> Step 5
- R14 `AppError` log lines include where the error was raised (`file:line function`) -> Step 5
- R15 Logs are also written to `logs/app.log` (rotating, gitignored) so past requests can be searched by request ID -> Step 4
- R16 Database unreachable (SQLAlchemy `OperationalError`) returns 503 `DATABASE_UNAVAILABLE`; the DB message goes to logs only -> Step 5

## Implementation Steps
1. **Test tooling.** `uv add --dev pytest` (httpx is already installed for `TestClient`). Create `tests/` with a `conftest.py` that provides a `client` fixture (with `raise_server_exceptions=False`), throwaway test-only routes that raise each error type, and an auth dependency override with a fake repository so the real DB is never touched. — Test: skip (wiring)
2. **Settings.** Add `debug: bool = False` to `Settings` in `app/core/config.py`; add `DEBUG=true` to `.env.example`. Do not pass `debug` to `FastAPI()`: Starlette's debug mode replaces the 500 handler with an HTML traceback page. — Test: skip (config)
3. **Error classes.** `app/core/errors.py`: `AppError(message, details=None, headers=None)` with class attributes `status_code`, `code`, `headers`. Subclasses: `BadRequestError`, `NotFoundError`, `ConflictError`, `ForbiddenError`, and `UnauthorizedError` → `InvalidCredentialsError`, `TokenMissingError`, `TokenExpiredError`, `TokenInvalidError`. Declare the class-level `headers` as `ClassVar` (avoids Ruff RUF012); merge per-instance headers by copying, never mutate the class dict. Add Pydantic `ErrorBody` / `ErrorResponse` models. — Test: skip (declarations; behavior covered through Step 5)
4. **Logging.** `app/core/logging.py`: `request_id_ctx` ContextVar (default `-`), a `RequestIdFilter`, and `setup_logging(debug)` using `dictConfig`. Plain-text format with `[request_id]`; `app` logger at INFO (DEBUG when `debug`); `uvicorn.access` raised to WARNING. Two handlers sharing the format and filter: console, plus a stdlib `RotatingFileHandler` writing `logs/app.log` (5 MB × 3 backups, UTF-8, directory created on startup). Add `logs/` to `.gitignore`. — Test: after (log content checked via `caplog` in Step 6; the file handler is checked by eye in Step 9)
5. **Exception handlers.** `app/core/exception_handlers.py`: a shared response builder (reads `request.state.request_id`, sets the header) and handlers for `AppError`, `RequestValidationError`, Starlette `HTTPException` (status → code map), SQLAlchemy `IntegrityError`, SQLAlchemy `OperationalError` (→ 503 `DATABASE_UNAVAILABLE`, logged at ERROR with the DB message), and `Exception`; plus `register_exception_handlers(app)`. Log levels: INFO for 4xx, WARNING for IntegrityError, ERROR with traceback for 500. The `AppError` handler appends the raise location, taken from the exception's innermost traceback frame, as `(relative/path.py:line function)`. The 500 handler sets `request_id_ctx` from `request.state` for the duration of its logging and resets it afterwards, so the crash line shows the real ID. — Test: first
   - Seam (user-confirmed): HTTP responses through `TestClient` against the real app (status, JSON body, headers), plus `caplog` for the log assertions.
   - Slices, in order: AC1 → AC2 → AC3 → AC4 → EC3 → AC5 → AC6 → AC19 → AC7 → AC8 → AC16 → AC17
6. **Request context middleware.** `app/core/middleware.py`: pure ASGI class. Reads or generates the request ID, stores it in both `request_id_ctx` and `scope["state"]` (the 500 handler runs outside this middleware, after the context variable is reset), wraps `send` to capture the status and append `X-Request-ID` only if it's not already present, logs the access line in `finally` (WARNING for ≥500), and resets the context variable. Passes non-HTTP scopes straight through. — Test: first
   - Seam (user-confirmed): HTTP responses through `TestClient` plus `caplog`.
   - Slices, in order: AC9 → AC10 → AC11 → AC12 → AC13
7. **Wire up `app/main.py`.** Call `setup_logging(settings.debug)` before creating the app, then `add_middleware(RequestContextMiddleware)`, then `register_exception_handlers(app)`. `main.py` currently imports the deleted modules, so the app won't start until this step is done. — Test: skip (wiring, covered by Steps 5–6)
8. **Migrate the auth module.** `controller.py`: replace `HTTPException(409)` with `ConflictError("Email already registered", {"field": "email"})`. `route.py`: router-level `responses` for 422/500 and route-level 409, all using `ErrorResponse`. — Test: first
   - Seam (user-confirmed): `POST /auth/register` through `TestClient` with the fake-repo override.
   - Slices: AC14 → AC15
9. **Verify.** Run `uv run pytest`; start the server and check `/docs` shows `ErrorResponse` for 409/422/500; trigger one error manually and grep the logs for its request ID. — Test: skip (manual check)

## Affected Files & Patterns
- `app/core/errors.py` — new: error classes and response schema
- `app/core/exception_handlers.py` — new: handlers and the registration function
- `app/core/middleware.py` — new: request ID and access log
- `app/core/logging.py` — new: logging configuration
- `app/core/config.py` — add `debug`
- `app/main.py` — currently broken (imports deleted modules); rewired in Step 7
- `app/modules/auth/controller.py`, `route.py` — use the new errors and OpenAPI docs
- `.env.example` — add `DEBUG`
- `.gitignore` — add `logs/`
- `pyproject.toml` — pytest dev dependency
- `tests/conftest.py`, `tests/test_error_handling.py`, `tests/test_request_context.py`, `tests/modules/auth/test_register_errors.py` — new
- Pattern to follow: new modules raise `app.core.errors` classes from controllers; routes declare their error statuses with `ErrorResponse`
- Conventions (apply in this feature and every later module):
  - When translating a library exception, chain it: `raise NotFoundError(...) from exc`, so the original cause stays in the logged traceback
  - Never put secrets, tokens, passwords or raw user content in `message` or `details`: both are returned to the client and written to the logs
- Risks: none for existing behavior; the only API change is the 409 body shape (`{"detail": ...}` → `{"error": {...}}`)

## Testing Strategy
- Framework & command: pytest with FastAPI `TestClient`; `uv run pytest`
- Isolation: throwaway routes and `app.dependency_overrides` only; no database writes

| ID | Behavior | Step | Mode |
|----|----------|------|------|
| AC1 | An `AppError` subclass returns its status, code, message, details and request_id in the standard shape | 5 | first |
| AC2 | A 401 auth error carries `WWW-Authenticate: Bearer` and its specific code (e.g. `TOKEN_EXPIRED`) | 5 | first |
| AC3 | A bad body returns 422 `VALIDATION_ERROR` with one `{field, issue, type}` entry per broken field | 5 | first |
| AC4 | The validation response never contains the submitted values (e.g. the password string) | 5 | first |
| AC5 | Unknown path → 404 `NOT_FOUND`; wrong method → 405 `METHOD_NOT_ALLOWED`, same shape | 5 | first |
| AC6 | `IntegrityError` → 409 `CONFLICT` with a generic message; the DB text is not in the body | 5 | first |
| AC7 | Unhandled exception → 500 `INTERNAL_ERROR`, generic message, `details` null when DEBUG is off | 5 | first |
| AC8 | With DEBUG on, the 500 `details` include the exception type and message | 5 | first |
| AC9 | A response without a client ID gets a generated `X-Request-ID` matching the body's `request_id` | 6 | first |
| AC10 | A safe client `X-Request-ID` is reused in the header and body | 6 | first |
| AC11 | An unsafe client ID (newline, over 64 chars) is replaced with a generated one | 6 | first |
| AC12 | `X-Request-ID` appears exactly once, including on 500 responses | 6 | first |
| AC13 | One access log line per request with method, path, status and the request ID | 6 | first |
| AC14 | Duplicate email → 409 `CONFLICT` with `details.field = "email"` | 8 | first |
| AC15 | OpenAPI for `/auth/register` lists 409, 422 and 500 using `ErrorResponse` | 8 | first |
| AC16 | The crash (500) log record's request ID equals the response's `request_id` (not `-`) | 5 | first |
| AC17 | An `AppError` log line contains the raising function's file, line and name | 5 | first |
| AC18 | Log lines are also written to `logs/app.log` | 4 | after (check by eye in Step 9) |
| AC19 | `OperationalError` → 503 `DATABASE_UNAVAILABLE`; the DB message is not in the body (raised from a test route, no real DB needed) | 5 | first |
| EC1 | A crash during a request: the 500 handler still finds the request ID (via `scope["state"]`) | 6 | first (covered by AC12) |
| EC2 | Non-HTTP scopes (lifespan) pass through the middleware untouched | 6 | after (app startup in Step 9) |
| EC3 | A malformed JSON body (e.g. `{"email": `) returns 422 `VALIDATION_ERROR` with a readable `body` entry and does not echo the raw body | 5 | first |

- Must verify, not assume: Starlette layer order (500 handler outside user middleware) — confirmed by AC12; uvicorn access-log silencing — check by eye in Step 9
- Open questions: none
- Known baseline failures: none (no tests exist yet)

## Blockers & Resolutions
- The 500 handler runs outside our middleware, after the context variable is reset → store the request ID in `scope["state"]` as well; the handler temporarily restores `request_id_ctx` from it while logging
- The header could be added twice (by the handler and the middleware) → the middleware only appends `X-Request-ID` when it's absent
- `FastAPI(debug=True)` would bypass the 500 handler → use our own `settings.debug`, never Starlette's
- Starlette re-raises after the 500 response, so uvicorn also prints the traceback → accepted for now; the server log just shows it twice
- `main.py` currently imports deleted modules → fixed in Step 7

## Trade-offs & Rationale
- Exception handlers rather than catching errors in middleware → FastAPI's intended mechanism; catches validation errors; works with streaming
- Pure ASGI middleware rather than `BaseHTTPMiddleware` → `BaseHTTPMiddleware` interferes with streaming, which LLM chat will need
- Generic 409 for DB conflicts → constraint names expose the schema and need a mapping table; controllers do explicit checks for friendly messages
- LLM error classes deferred → they're added with the LLM feature, which also designs the streaming (SSE) error event
- No new runtime dependencies → stdlib `logging` and `contextvars`, plus FastAPI and Starlette; only pytest is added, as a dev dependency
- Plain-text logs → easier to read locally; switch to JSON when deploying
- Log file at a fixed `logs/app.log` → no new setting until there's a real need (e.g. Docker logging to stdout only)
- Crash location left out of DEBUG 500 responses (user's choice) → the logged traceback has it, and is findable by request ID
- `OperationalError` → 503 rather than 500 → "the database is down or misconfigured" is the most common local failure and should be obvious from the code alone
- Deferred: slow-request warnings (declined for now), Sentry-style error tracking (at deploy), a DB readiness endpoint (with Docker), background-task error handling (with document ingestion)

## Project Rules Applied
- No `.claude/CLAUDE.md` or `.claude/rules/` in this repo. Follows the agreed conventions: `app/` package, `modules/<name>/route → controller → repository`, controllers stay free of HTTP concerns.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | Mapped current files; found `main.py` still imports the deleted error modules; confirmed httpx is installed and pytest is not |
| grill-me (via AskUserQuestion) | 8 decisions: pytest + TestClient seam, general + auth errors only, plain-text logs, defer the SSE error path, generic 409, accept safe client IDs, 422 for validation, DEBUG-gated 500 details. Debuggability round: request ID on crash logs, raise location on AppError logs, rotating log file (crash location in DEBUG responses declined). Hardening round: DB-down 503, malformed JSON edge case, conventions notes (slow-request warning declined) |
| ponytail | Kept it to stdlib + FastAPI; LLM classes and the SSE path deferred (YAGNI) |
| security-review (considered inline) | No input echo in validation errors; DB messages and 500 details hidden from clients; client request IDs validated against log injection |

## Ready to Implement
- All requirements mapped to steps
- Every step has a Test tag; every AC and EC is in the coverage map
- Affected files identified, including the currently broken `main.py`
- Blockers resolved and edge cases handled
- Trade-offs documented
- Deviation from the workflow: no spec.md (approved by the user); requirement and AC/EC IDs are defined in this plan

## Implementation Notes (added during /implement)
- Step 7 wiring was done first with stub modules, because every test imports `app.main`
- AC16's test lives with the middleware tests (Step 6), since it needs a real request ID
- Handlers are registered from a list typed `Any` (Starlette's handler type is invariant in the exception parameter)
- `AppError` instances expose `response_headers` (class `ClassVar` headers merged with per-raise headers)
- See task.md "Deviations from Plan" for details
