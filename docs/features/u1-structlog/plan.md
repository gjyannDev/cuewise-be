# Implementation Plan: U1 structlog (structured JSON logs)

## Overview
Replace the hand-built text logging (`event key=value` strings, `split_fields`, `RequestIdFilter`, `ConsoleFormatter`) with structlog, so every line in `logs/app.log` is one JSON object with `request_id`. Sensitive values are masked by a processor, the dev console stays readable, and `interview_report` gives the same numbers. Spec: `docs/features/u1-structlog/spec.md`.

## Architecture & Design
structlog runs **on top of the standard library's `logging`**. One shared processor chain does the work: merge contextvars, add logger, level and timestamp, default `request_id` to `-`, redact, move the traceback into `exception`, render. structlog's `ProcessorFormatter` is attached to the root logger's handlers: a rotating file handler that always renders JSON, and a console handler that renders the readable view when debug is on and JSON when it is off. Because the handlers sit on the root logger, library logs (uvicorn, sqlalchemy, httpx) and not-yet-converted `logging.getLogger(...)` calls go through the same chain. That is how existing calls keep working during the move. Request, session and user ids live in `structlog.contextvars`. The middleware clears and binds `request_id` per request, `get_current_user` binds `user`, and the interview services bind `session`.

**Concepts this teaches (U1 goals):**
- **Processor pipeline:** each processor is a small function `(logger, method, event_dict) -> event_dict`. Order matters: redaction must run before any renderer, so no output path can skip it.
- **contextvars:** each asyncio task gets a copy of the context. A streamed SSE response runs inside the request's task tree, so it sees the request's ids. A new request starts clean because the middleware clears the context first.
- **Structured logs for aggregates:** the report reads fields directly instead of re-parsing strings.

## Approaches Considered

| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. structlog on stdlib logging (`structlog.stdlib` + `ProcessorFormatter` on root handlers) | One pipeline for app, library and legacy calls. Keeps `RotatingFileHandler` and pytest's `caplog`. Slightly more config. | **Yes**: the spec requires library logs in the file (AC6) and a stdlib bridge during the move. This is structlog's documented way to do both. |
| B. Pure structlog (`WriteLoggerFactory` to a file) plus a separate stdlib bridge | Faster and simpler for structlog-only calls. Library logs need a second pipeline, rotation is hand-built, and redaction must be wired twice. | No: two pipelines means two places redaction can be missed. |
| C. stdlib only, with a JSON formatter (no structlog) | No new dependency. | No: U1 exists to learn structlog (spec, Project Conventions). |

## Spec Requirements -> Implementation
- JSON file, rotation, all loggers, stdlib bridge, console by debug flag, redaction, exceptions, non-encodable values, unwritable folder -> Step 3
- `request_id` context, access line `http_request`, X-Request-ID, `user` binding -> Step 4
- `session` binding, interview events converted, SSE and concurrent isolation -> Steps 5, 6
- Remaining call sites converted -> Step 7
- Legacy symbols removed (AC7), `split_fields` moved into the report reader -> Step 8
- Report gives the same numbers (AC8) -> Steps 1, 5, 9
- Report reads both formats -> done before this plan (`parse_log`, `tests/modules/interviews/tooling/test_interviews_log.py`)

## Implementation Steps
Checkpoint interval: every 3 steps (large plan).

Each step's Verify = the step's tests + the gate commands (Testing Strategy).

1. **Freeze the text-format report as a golden file** (before any logging change).
   - Use the existing emit helpers in `test_interview_report.py`, which call the real log functions and format the lines with today's `LOG_FORMAT`.
   - Write one representative interview to a text log: start with retrieval, answer turns, a follow-up, a partial (failed) request, a feedback request, and a stream summary.
   - Save the rendered text report next to it. A test asserts that `parse_log` + `analyze_interview` + `render_text` on the log equals the saved report.
   - Copy the scratchpad `report_before_u1.txt` (the real `--last 3` output) into the feature folder so it survives.
   - Files: `tests/modules/interviews/tooling/data/legacy_interview.log`, `tests/modules/interviews/tooling/data/legacy_interview_report.txt`, `tests/modules/interviews/tooling/test_interview_report_formats.py`, `docs/features/u1-structlog/report_before_u1.txt`
   - Verify: `uv run pytest tests/modules/interviews/tooling -q` + gates
   - Test: first. Seam: the report (`parse_log` -> `analyze_interview` -> `render_text`), user-confirmed. Slices: the golden report matches.
2. **Add the structlog dependency.**
   - `uv add structlog`. Why: the slice's learning goal, and stdlib JSON would need hand-built context and redaction (see Approaches).
   - Files: `pyproject.toml`, `uv.lock`
   - Verify: `uv run python -c "import structlog"` + full `uv run pytest` (nothing should change yet) + gates
   - Test: skip (dependency only)
3. **Logging core on structlog.** Rewrite `setup_logging(debug, log_file=LOG_FILE)` in `app/core/logging.py`:
   - **Shared chain:** merge contextvars; add logger name, level, ISO UTC `timestamp`; set `request_id` to `-` when absent; **redact**; format the exception into `exception`; JSON render with a `default=str` fallback, so a UUID, datetime or exception is written as text.
   - **Redaction processor:**
     - Case-insensitive key match, at any nesting depth (dicts and lists), value replaced with `[redacted]`.
     - The key set is one module constant: `answer`, `resume`, `job_description`, `token`, `access_token`, `refresh_token`, `password`, `authorization`, `api_key`, `secret`, `cookie`.
     - A comment states the EC3 limit (key names only, free text is not scanned).
   - **Handlers on the root logger:**
     - Rotating file handler: 5 MB, 3 backups, always JSON.
     - Console: readable view when debug is on, JSON when it is off. The readable view is a structlog renderer ported from today's `ConsoleFormatter` look: time, level, 8-character request id, logger, event, aligned `key  value` rows, colour only when stderr is a TTY, traceback below.
     - The app level stays DEBUG/INFO by the debug flag. The root level is WARNING: library warnings and errors reach the file, while library INFO lines (httpx logs full request URLs) do not. `uvicorn.access` stays at WARNING. (Deviation, see task.md.)
   - **Unwritable `logs/`:** catch the error, use console only, emit one warning (EC6).
   - **Transitional:** a processor that copies `request_id_ctx` into the event when contextvars has no `request_id`, so the old middleware keeps working until Step 4. `split_fields`, `request_id_ctx` and `RequestIdFilter` stay until Step 8.
   - **Test fixture:**
     - Add `log_lines` to `tests/conftest.py`. It runs `setup_logging` into a temp file, yields a callable returning the file's lines parsed as dicts, and restores the logging config afterwards.
     - Also add a console-capture variant for AC5.
     - The old `app_logs` fixture keeps working (caplog on the `app` logger).
     - The suite logs to a temp file (`TEST_LOG_FILE`), never the real `logs/app.log`. Full runs rotated it and deleted old backups (deviation, see task.md).
     - The legacy `ConsoleFormatter` goes in this step; its tests move to the readable console (deviation, see task.md).
   - Files: `app/core/logging.py`, `app/main.py` (only if the `setup_logging` signature changes), `tests/conftest.py`, `tests/core/test_logging.py`
   - Verify: `uv run pytest tests/core/test_logging.py -q` + gates
   - Test: first. Seam: `setup_logging` + the rendered output through `log_lines`, user-confirmed. Slices in order:
     1. A stdlib `%s` call becomes one valid JSON line with the five record keys; outside a request, `request_id` is `-` (AC2, EC1).
     2. A sensitive top-level key is masked in the file and on the console (AC1).
     3. A nested and mixed-case key is masked (EC2).
     4. A UUID, datetime or exception value doesn't raise and the line is valid JSON (AC9, EC5).
     5. A logged exception is one line with `exception` (AC11, EC7).
     6. A library logger (`uvicorn.error`, `sqlalchemy.engine`) lands in the file as JSON (AC6).
     7. Debug on gives the readable console; debug off gives JSON (AC5).
     8. An unwritable folder gives console only plus one warning (AC10, EC6).
4. **Request context on structlog contextvars.**
   - **`RequestContextMiddleware`:** clear the contextvars, bind `request_id` (same safe-id rule as today), and reset at the end. Log the access line as event `http_request` with fields `method`, `path`, `status`, `duration_ms` (the contract `parse_log` already reads).
   - **`unhandled_exception_handler`:** rebinds the request id from scope state with structlog's bound-context helper, replacing the `request_id_ctx` set/reset.
   - **`current_request_id()`** in `app/core/logging.py` (returns `None` outside a request). `interviews_answer_controller` uses it for the SSE error event.
   - **`bind_log_context(**fields)`** in `app/core/logging.py`. It is the only bind helper, so features don't import structlog directly. `get_current_user` calls it with `user=<id>`.
   - **Deviation (applied):** request fields live in one dict per request, set by the middleware (`request_log_context`) and kept in scope state for the 500 handler. Sync dependencies and endpoints run in worker threads with a copied context, and every copy shares that dict. Outside a request, `bind_log_context` falls back to `structlog.contextvars`.
   - Update `tests/test_request_context.py` and `tests/test_error_handling.py` (the log assertions) to use `log_lines`.
   - Files: `app/core/middleware.py`, `app/core/exception_handlers.py`, `app/core/logging.py`, `app/modules/auth/dependencies/auth_dependencies.py`, `app/modules/interviews/controllers/interviews_answer_controller.py`, `tests/test_request_context.py`, `tests/test_error_handling.py`
   - Verify: `uv run pytest tests/test_request_context.py tests/test_error_handling.py tests/modules/auth -q` + gates
   - Test: first. Seam: HTTP API via the `client` fixture, user-confirmed. Slices in order:
     1. All lines of one request share the id from X-Request-ID (AC3).
     2. An unsafe client id is replaced (EC9).
     3. The crash log carries the real id.
     4. An authenticated request's lines carry `user` (AC4, user half).
     5. After a varied set of API calls, every file line is JSON with the five keys (AC2).
5. **Convert the interview AI log events** (the events the report reads).
   - **`interviews_turn_log.py`:** `log_llm_call`, `log_result`, `log_llm_error`, `log_turn_summary`, `log_embedding_call`, `log_retrieval` and `log_stream_summary` emit structlog events with the same event and field names.
     - The `session` parameter is dropped; it comes from context.
     - `None` stays `None` (rendered as JSON null; `parse_log` turns it into `-`).
     - `retrieval.scores` keeps today's comma-joined 3-decimal string, so the report's numbers can't move.
   - **`app/core/ai/context.py`:** `context_build` becomes key/value fields (the trailing `ledger=… notes=…` become their own fields).
   - Convert the warnings in `interviews_decide.py`, `interviews_write.py` and `interviews_feedback_turn.py` the same way.
   - **Callers:** the eval and report tooling that run AI code outside a request bind `session` with `bind_log_context`.
   - **`test_interview_report.py`:**
     - The emit helpers keep calling the real log functions; each emit binds `session`/`request_id` the way the app does.
     - `lines_of` now returns the JSON lines from `log_lines`.
   - **New test in `test_interview_report_formats.py`:** emit the same interview as Step 1 through the converted functions; the JSON log's report must equal `legacy_interview_report.txt` (AC8).
   - Files: `app/modules/interviews/ai/interviews_turn_log.py`, `app/core/ai/context.py`, `app/modules/interviews/ai/interviews_decide.py`, `app/modules/interviews/ai/interviews_write.py`, `app/modules/interviews/ai/interviews_feedback_turn.py`, their callers in `app/modules/interviews/ai/` and `app/modules/interviews/tooling/`, `tests/modules/interviews/tooling/test_interview_report.py`, `tests/modules/interviews/tooling/test_interview_report_formats.py`, `tests/core/ai/test_context.py`
   - Verify: `uv run pytest tests/modules/interviews tests/core/ai -q` + gates
   - Test: first. Seam: the report, user-confirmed. Slices in order:
     1. The golden interview emitted as JSON gives the identical report (AC8).
     2. An `llm_call` with no `session` bound still reports, with `-` (EC10).
6. **Bind `session` in the interview services.**
   - Each service binds `session` once when it knows it, through `bind_log_context`:
     - Interviews start: after the session is created.
     - Answer and stream: `AnswerService`.
     - Feedback: `FeedbackService`.
     - Voice: `interviews_voice_service`.
     - Retrieval at start.
   - Update the interview route tests that inspect log records to use `log_lines`, and check `session` and `user` there.
   - Add one test with two concurrent requests, one an SSE answer stream (the existing streaming test setup), asserting each line has its own request's `request_id`/`session`.
   - Files: `app/modules/interviews/services/interviews_service.py`, `app/modules/interviews/services/interviews_answer_service.py`, `app/modules/interviews/services/interviews_feedback_service.py`, `app/modules/interviews/services/interviews_voice_service.py`, `app/modules/interviews/services/interviews_retrieval_service.py`, the log-inspecting tests under `tests/modules/interviews/routes/`, `tests/modules/interviews/services/` and `tests/modules/interviews/controllers/`
   - Verify: `uv run pytest tests/modules/interviews -q` + gates
   - Test: first. Seam: HTTP API via `client`, user-confirmed. Slices in order:
     1. A start request's lines carry `session` without passing it (AC4).
     2. An answer turn's lines carry `session` and `user` (AC4).
     3. Concurrent requests plus an SSE stream keep separate ids (EC4).
7. **Convert the remaining call sites** to structlog events with key/value fields. Messages stay generic, and exception text is logged only where it is today.
   - `app/core/speech/gateway.py`: `log_fields` tuples become kwargs, and `session`/`user` come from context.
   - `app/modules/interviews/services/interviews_voice_service.py` (its `log_fields`).
   - `app/core/ai/factory.py`, `app/core/ai/tracing.py`, `app/core/exception_handlers.py` (`app_error`, `validation_error`, `integrity_error`, `database_unavailable`, `unhandled_exception`).
   - `app/modules/auth/constants/auth_constants.py`, `app/modules/profile/services/profile_service.py`, `app/modules/interviews/services/interviews_job_url_service.py`, and `stream_turn_failed` in `interviews_answer_service.py`.
   - Update their tests to `log_lines`.
   - Files: the app files above; `tests/core/speech/test_gateway.py`, `tests/core/ai/test_factory.py`, `tests/core/ai/test_tracing.py`, `tests/modules/auth/**`, `tests/modules/profile/routes/test_profile_routes.py`, `tests/modules/interviews/routes/test_job_url.py`, `tests/modules/interviews/routes/test_speech.py`, `tests/modules/interviews/routes/test_transcribe.py`
   - Verify: full `uv run pytest -q` + gates
   - Test: after (existing behaviour tests re-pointed at the new output; no new logic)
8. **Remove the legacy logging code.**
   - Note (Steps 5-6 deviation): the `app_logs` fixture stays, as a view over the real pipeline's JSON file. Only its old caplog version is gone.
   - Move the key=value splitter into `interviews_log.py` as a private legacy-line reader (user decision). `parse_log` behaviour stays the same; its tests still pass.
   - Delete from `app/core/logging.py`: `split_fields`, `_FIELD`, `LOG_FORMAT`, `request_id_ctx`, `RequestIdFilter`, `ConsoleFormatter`, the transitional processor.
   - Delete the `app_logs` fixture and the old `split_fields`/`ConsoleFormatter` tests.
   - **AC7 check:**
     - A search of `app/` finds none of those names, except the private reader in `interviews_log.py`.
     - It finds no `%s`-style `key=` message strings.
   - Files: `app/core/logging.py`, `app/modules/interviews/tooling/interviews_log.py`, `tests/conftest.py`, `tests/core/test_logging.py`
   - Verify: `uv run pytest -q` + the AC7 search with `ctx_search` + gates
   - Test: skip (removal only; covered by the full suite and the search)
9. **End-to-end check and docs.**
   - Run `uv run python -m app.scripts.interview_report --last 3` on the real `logs/` (the same old interviews, still text lines) and diff it with `docs/features/u1-structlog/report_before_u1.txt`. It must be identical (AC8).
   - Start the API in dev (debug on), make a few requests, and check that the console is readable and `logs/app.log` gains JSON lines (AC5, AC2 on real output).
   - The user runs one live interview; `interview_report` on it then runs without error.
   - **Docs:**
     - `docs/ai-engineering-upgrade-path.md` U1: say `session`/`user` instead of `session_id`/`user_id`, and add the EC3 limit.
     - Record the outcome in `docs/features/u1-structlog/task.md`.
   - Run `graphify update .`.
   - Files: `docs/ai-engineering-upgrade-path.md`, `docs/features/u1-structlog/task.md`
   - Verify: the report diff is empty + `uv run pytest -q` + gates
   - Test: after (real app and real log)

## Affected Files & Patterns
- `app/core/logging.py`: rewritten; it becomes the only module that imports structlog. It exposes `setup_logging`, `bind_log_context`, `current_request_id` and `get_logger`.
- `app/core/middleware.py`, `app/core/exception_handlers.py`: context binding and the access event.
- `app/modules/auth/dependencies/auth_dependencies.py`: binds `user`.
- `app/modules/interviews/ai/interviews_turn_log.py`: the main event emitters; `session` param dropped.
- Interview services: bind `session`. Controllers stay thin (only `current_request_id` for the SSE error event).
- `app/modules/interviews/tooling/interviews_log.py`: already reads both formats; gains the private legacy splitter in Step 8.
- About 29 test files that read `app_logs` move to `log_lines` in the step that converts their call site.
- **Reusable patterns:** keep event and field names identical to today's (`llm_call`, `context_build`, `turn_summary`, `retrieval`, `embedding_call`, `stream_turn_summary`, `speech`, `transcription`, `session`, `user`). Follow the existing safe-request-id rule in the middleware.
- **Risks:**
  - `dictConfig` / root handlers in tests: the `log_lines` fixture must restore the prior config, or tests leak handlers into each other.
  - Root-level handlers might double-log the `app` logger, which today has `propagate=False`. Step 3 sets one consistent arrangement.
  - Library loggers at DEBUG could flood the file. The root level stays INFO; `sqlalchemy.engine` keeps its own default.
  - A changed value format in report-read fields would silently move numbers. The Step 1 golden file catches it.

## Testing Strategy
- **Framework and command:** pytest, `uv run pytest -q` (per-step paths are listed in each step).
- **Gate commands, after every step:**
  - `uv run pytest -q` (includes `tests/test_layers.py`)
  - `uv run --with ruff ruff check .`
- **Coverage map:**

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 3 | first | file and console both masked |
| AC2 | 3, 4, 9 | first / after | unit, then across API calls, then the real log |
| AC3 | 4 | first | X-Request-ID equals the lines' id |
| AC4 | 4, 6 | first | user in 4, session in 6 |
| AC5 | 3, 9 | first / after | console by debug flag |
| AC6 | 3 | first | uvicorn.error, sqlalchemy.engine |
| AC7 | 8 | skip | search + full suite |
| AC8 | 1, 5, 9 | first / after | golden text report = JSON report; real `--last 3` diff |
| AC9 | 3 | first | |
| AC10 | 3 | first | |
| AC11 | 3 | first | |
| AC12 | all | gate | |
| EC1 | 3 | first | |
| EC2 | 3 | first | |
| EC3 | 3, 9 | doc | known limit; a comment plus an upgrade-path note, no test (out of scope) |
| EC4 | 6 | first | concurrent + SSE |
| EC5 | 3 | first | |
| EC6 | 3 | first | |
| EC7 | 3 | first | |
| EC8 | done | first | existing `test_interviews_log.py` |
| EC9 | 4 | first | |
| EC10 | 5 | first | |

- **Must verify, not assume:**
  - That Starlette's `StreamingResponse` iteration inherits the request's contextvars (EC4 test).
  - That uvicorn's own loggers reach the root handlers when run by `fastapi dev` / `uvicorn` (Step 9, real run).
- **Open questions:** none.
- **Known baseline failures:** none seen. The tooling and logging tests pass, 334 tests.

## Blockers & Resolutions
- AC7 vs reading old text lines -> the splitter moves into the report reader as a private helper (user decision).
- AC4 "without passing" -> the `session` param is removed from the log helpers; services bind it (user decision).
- The real before/after report needs the same interviews -> old interviews stay text lines, which `parse_log` reads; diff against the saved before-report in Step 9.
- The transition breaks old tests -> `app_logs` stays until Step 8; each step migrates its own tests (user decision).

## Trade-offs & Rationale
- stdlib-backed structlog over pure structlog: one redaction path for every logger (security over speed).
- One `bind_log_context` helper in core: features never import structlog, so swapping the logging library later touches one file (the CLAUDE.md "keep things swappable" spirit).
- A golden file before any change: the only reliable proof that "same numbers" holds for formatting-sensitive fields.
- Key-based redaction only: predictable and cheap; pattern scrubbing is out of scope (spec).

## Project Rules Applied
- CLAUDE.md layers: binding happens in services and the auth dependency, controllers stay thin, and `tests/test_layers.py` is a gate.
- CLAUDE.md security and privacy: redaction makes "no PII, tokens, passwords in logs" code; exception and DB text goes only where it is logged today.
- CLAUDE.md dependencies: structlog's addition is justified (Step 2).
- CLAUDE.md AI guidelines: this is not a prompt/model/retrieval change, so there is no eval baseline run; the report golden file is the safety check.
- CLAUDE.md workflow: tests + ruff per step; `graphify update .`; no commits.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | logging call sites (~55 in 11 app files), ~29 log-inspecting test files, `app_logs` fixture, auth dependency, middleware/handler context use |
| graphify | logging.py <-> middleware, exception handlers, report tooling, conftest relationships |
| grilling (via AskUserQuestion) | seams (rendered output, HTTP client, full report), session binding, split_fields location, per-step test migration |
| ponytail (judgment) | rejected a second pipeline (B) and hand-built rotation; one bind helper only |
| security-review (judgment) | redaction key set, before-render ordering, unchanged safe request-id rule |

## Ready to Implement
- All spec requirements map to steps; every AC and EC is mapped (EC3 is a documented limit, EC8 is already done).
- Every step has a Test tag, files and a verify command; gate commands are listed.
- Approaches compared; checkpoint every 3 steps.
- Blockers resolved by user decisions; no other deviations from the spec.
