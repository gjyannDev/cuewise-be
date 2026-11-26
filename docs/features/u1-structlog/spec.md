# Feature: U1 structlog (structured JSON logs)

Slice U1 of `docs/ai-engineering-upgrade-path.md`. Nothing changes for the app's users; this is a backend and developer-experience change.

## Problem
Logs are text lines like `llm_call session=… task=… latency_ms=…`. Fields are packed into the message and parsed back with `split_fields` (and a regex in `interviews_log.py`), so a change to the wording can silently break the interview report. The dev console formatter is custom code. The rule "no PII in logs" depends on every developer remembering it at every call site. Request, session and user ids are passed by hand instead of attached once.

## Goal
Every log line in `logs/app.log` is one JSON object with a `request_id`. Sensitive values are masked by code, not by habit. The dev console stays readable. `interview_report` gives the same numbers for an interview logged before the change and one logged after it.

## Project Conventions
- Rules consulted: root `CLAUDE.md` of cuewise-be (the repo has no `.claude/rules/`).
- Constraints those rules impose:
  - Cross-cutting code (logging config, redaction, context) lives in `app/core/`; log reading for reports stays in the interviews `tooling/` folder.
  - Layers only call downward; no layer imports another feature's repository. Logging must not break that (enforced by `tests/test_layers.py`).
  - "Don't log PII, tokens, or passwords" and "don't log raw interview content": redaction turns this into code.
  - A new dependency must be justified: structlog is added because this slice exists to learn it (stdlib `logging` alone would meet the output goal).
  - Tests under `tests/` mirror `app/`; mock external systems; run `uv run pytest` and lint; do not commit.

## User Flow
There is no end-user flow. The developer flow:
1. Run the API in dev: the console shows the readable view; `logs/app.log` gets JSON lines.
2. Make a request: every line it produces carries the same `request_id`, and lines about an interview also carry `session` (and `user` when authenticated), without the calling code passing them.
3. Log an event with a sensitive key: the file and console show the key with the value masked.
4. Run `interview_report`: it reads old text lines and new JSON lines and reports the same numbers.

## Requirements

### Functional
- **JSON file:** `logs/app.log` is written as one JSON object per line, with keys `timestamp`, `level`, `logger`, `request_id`, `event`; every other key is a field. Rotation stays as today (5 MB, 3 backups).
- **All loggers:** library logs (uvicorn, sqlalchemy, httpx and others) go through the same pipeline into the file, as well as the app's own loggers.
- **Stdlib bridge:** existing `logging.getLogger(...).info(...)` calls keep working until converted.
- **Console:** with the debug setting on, the console shows a coloured, readable view (one field per line); with debug off, the console shows the same JSON lines as the file.
- **Context binding:**
  - `request_id` is attached to every line, replacing `request_id_ctx` and `RequestIdFilter`; outside a request it is `-`.
  - `session` and `user` (the names the report already reads) are bound once per request and appear on every line of that request after they are known.
  - Context never leaks between concurrent requests, nor between a streamed (SSE) response and the next request.
- **Redaction:** before any renderer runs, the value of a sensitive key is replaced with `[redacted]`. Matching is by key name, case-insensitive, at any nesting depth. The key list covers at least `answer`, `resume`, `job_description`, `token`, `password`, `authorization` and is changed in one place.
- **Exceptions:** the traceback appears in one `exception` field of the JSON line, so the file stays one object per line.
- **Conversion:** every existing `logger.x("event k=%s", …)` call in `app/` becomes an event with key/value fields (same event names, same field names). `split_fields`, the text `LOG_FORMAT`, `RequestIdFilter`, `request_id_ctx` and the custom `ConsoleFormatter` are removed once nothing uses them.
- **Access line:** the request log becomes `event="http_request"` with `method`, `path`, `status`, `duration_ms` fields (the contract `parse_log` already reads).
- **Report reader:** `interviews_log.parse_log` keeps reading both formats (done before this spec): the new JSON lines and the old text lines in rotated or older log files.
- **Log failures never fail a request:** values that JSON cannot encode (UUIDs, exceptions, unknown objects) are written as text; a log call never raises into request handling.

### Non-Functional
- **Security/privacy:** masking applies to the file and the console alike. Redaction is key-based only (see Edge Cases EC3).
- **Performance:** logging adds no network or blocking I/O to the event loop beyond today's file handler.
- **Compatibility:** old text log files stay readable by the report and are not rewritten.

## UX Requirements
Developer console only:
- Dev (debug on): time, level, short request id (8 chars), logger, event, then one aligned `key  value` row per field; colour only when stderr is a terminal; exceptions printed below the event.
- Non-dev (debug off): plain JSON, no colour.

## Constraints
- New dependency: `structlog` (justified under Project Conventions).
- Field and event names stay as they are today (`llm_call`, `context_build`, `turn_summary`, `retrieval`, `embedding_call`, `stream_turn_summary`, `session`, `user`, …) so the report and the Langfuse comparison work are unaffected.
- Not a baseline-eval slice: no prompt, model or retrieval change, so the eval comparison step is skipped; the report comparison is the safety check.
- U2 (tenacity) logs its retries through this logging, so U1 must land first or U2 must use the stdlib bridge.

## Blockers
- None. The "before" reference is `interview_report --last 3` output saved before the change (see AC8); it must be compared against the same interviews after the switch.

## Edge Cases
- **EC1:** A log call happens outside any request (startup, scripts, background code) -> the line is valid JSON and `request_id` is `-`.
- **EC2:** An event is logged with a sensitive key nested inside a dict or list field (for example `data={"Answer": "…"}`) -> the nested value is masked; the key name case is ignored.
- **EC3:** A secret appears inside free text rather than under a sensitive key (for example a library's own log message) -> not masked; this is a known limit of key-based redaction, to be recorded in the docs.
- **EC4:** Two requests run at the same time, one streaming an SSE response -> each line carries its own request's `request_id`/`session`; nothing from one shows up on the other.
- **EC5:** A field value cannot be encoded as JSON (UUID, datetime, exception object) -> it is written as text and the line stays valid JSON.
- **EC6:** `logs/` cannot be created or written at startup -> the app keeps running with console logging only and prints one warning.
- **EC7:** An exception is logged -> one JSON line with the traceback in `exception`; the exception message is kept as it is today (a library error message could contain input text, accepted risk).
- **EC8:** The report reads a log whose rotated file is the old text format and whose current file is JSON -> both are read and one report is produced (covered by the existing parse_log tests).
- **EC9:** A client sends an unsafe `X-Request-ID` -> a fresh id is used, as today.
- **EC10:** A converted call is missing a field the report needs (for example `session` on an `llm_call`) -> the report still runs and shows `-` for it, as it does for today's lines.

## Acceptance Criteria
- [ ] **AC1:** A test logs an event with a sensitive key (`answer`, `resume`, `job_description`, `token`, `password`, `authorization`) at the top level and nested; neither the file output nor the console output contains the value, and both show `[redacted]`.
- [ ] **AC2:** After exercising the API in a test, every line of the log file parses as JSON and has `timestamp`, `level`, `logger`, `request_id`, `event`.
- [ ] **AC3:** All lines produced by one request share its `request_id`, and the same id is in the `X-Request-ID` response header; a log call outside a request has `request_id` `-` (EC1).
- [ ] **AC4:** A request about an interview logs `session` (and `user` when authenticated) on its lines without any log call passing them; two concurrent requests, one an SSE stream, keep separate values (EC4).
- [ ] **AC5:** With debug on, the console output is the readable view (header line plus one row per field); with debug off, it is JSON identical in shape to the file lines.
- [ ] **AC6:** Library loggers (for example `uvicorn.error`, `sqlalchemy.engine`) produce JSON lines in the file.
- [ ] **AC7:** Searching `app/` finds no use of `split_fields`, `LOG_FORMAT`, `RequestIdFilter`, `request_id_ctx` or the old `ConsoleFormatter`, and no `logger.x("… k=%s …")` key=value strings remain; the test suite passes.
- [ ] **AC8:** `interview_report --last 3` run on the logged interviews before the change (saved output) and the same command on a log of the same interviews after the change report the same numbers; a test that feeds the report the same events as text lines and as JSON lines gets identical results.
- [ ] **AC9:** A value JSON cannot encode (UUID, datetime, exception) is logged without raising and the line stays valid JSON (EC5).
- [ ] **AC10:** With an unwritable log folder the app starts, logs to the console and emits one warning (EC6).
- [ ] **AC11:** A logged exception produces a single JSON line with the traceback in `exception` (EC7).
- [ ] **AC12:** `uv run pytest`, the layer test and `ruff check` pass.

## Out of Scope
- Shipping logs to a hosted service or a log viewer (named "Not included" in the upgrade path).
- Pattern-based scrubbing of secrets inside free text (key-based only; EC3).
- Rewriting existing log files or migrating old text lines to JSON.
- Changing which events are logged, their names or their meaning; changing the report's contents.
- Tracing, metrics or Langfuse changes.
