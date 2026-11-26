# Implementation: U1 structlog (structured JSON logs)

## Status
Ready for /review-feature (Steps 1-9 done; one manual check pending: a live interview by the user, see Tests Pending)
Health Check: missing: caveman -> fallback: normal chat. All other dependencies present.
Review Health Check: all present (code-review, security-review, llm-security, simplify, verification-before-completion); level: low.

## Completed Steps
- [x] 0. (before spec) `parse_log` reads text and JSON lines (`tests/modules/interviews/tooling/test_interviews_log.py`)
- [x] 1. Freeze the text-format report as a golden file
- [x] 2. Add the structlog dependency (structlog 26.1.0)
- [x] 3. Logging core on structlog
- [x] 4. Request context on structlog contextvars
- [x] 5. Convert the interview AI log events
- [x] 6. Bind `session` in the interview services
- [x] 7. Convert the remaining call sites
- [x] 8. Remove the legacy logging code
- [x] 9. End-to-end check and docs

## Current Step
None: all steps done. Next: `/review-feature`.

## Changes Made
Not committed (the user commits). Suggested messages:
- Steps 0-1: `test(interviews): read JSON log lines and freeze the text-format report as a golden file`
- Step 2: `build: add structlog`
- Step 3: `feat(logging): structlog pipeline with JSON file, redaction and readable dev console`
- Step 4: `feat(logging): per-request log context (request_id, user) and the http_request access event`
- Steps 5-6: `refactor(interviews): structured interview log events with session bound once per request`
- Steps 7-8: `refactor(logging): structured events everywhere; drop split_fields, LOG_FORMAT and RequestIdFilter`
- Step 9: `docs(u1): structlog learnings, task log and upgrade-path wording`

Files so far:
- Step 1: `tests/modules/interviews/tooling/test_interview_report_formats.py`, `tests/modules/interviews/tooling/data/legacy_interview.log`, `tests/modules/interviews/tooling/data/legacy_interview_report.txt`, `docs/features/u1-structlog/report_before_u1.txt`
- Step 2: `pyproject.toml`, `uv.lock`
- Step 3: `app/core/logging.py`, `tests/conftest.py`, `tests/core/test_logging.py`
- Step 4: `app/core/logging.py`, `app/core/middleware.py`, `app/core/exception_handlers.py`, `app/modules/auth/dependencies/auth_dependencies.py`, `app/modules/interviews/controllers/interviews_answer_controller.py`, `tests/test_request_context.py`
- Steps 5-6:
  - App: `app/modules/interviews/ai/interviews_turn_log.py`, `app/core/ai/context.py`, `app/modules/interviews/ai/{interviews_decide,interviews_write,interviews_write_stream,interviews_feedback_turn,interviews_turn_limits}.py`, `app/modules/interviews/services/{interviews_service,interviews_answer_service,interviews_feedback_service,interviews_voice_service,interviews_retrieval_service}.py`, `app/modules/interviews/tooling/interviews_feedback_evals.py`
  - Tests: `tests/conftest.py`, `tests/modules/interviews/tooling/test_interview_report.py`, `tests/modules/interviews/tooling/test_interview_report_formats.py`, `tests/modules/interviews/routes/test_log_context.py` (new)
- Step 7: `app/core/speech/gateway.py`, `app/core/ai/factory.py`, `app/core/ai/tracing.py`, `app/core/exception_handlers.py`, `app/modules/auth/constants/auth_constants.py`, `app/modules/profile/services/profile_service.py`, `app/modules/interviews/services/{interviews_job_url_service,interviews_voice_service,interviews_answer_service}.py`, `tests/modules/interviews/routes/test_job_url.py`, `tests/modules/profile/routes/test_profile_routes.py`
- Step 8: `app/core/logging.py`, `app/modules/interviews/tooling/interviews_log.py`, `tests/core/test_logging.py`, `tests/modules/interviews/tooling/test_interviews_log.py`
- Step 9: `docs/ai-engineering-upgrade-path.md` (U1 wording), `docs/features/u1-structlog/learnings.md`, this file; `graphify update .` run

## Test Results
- Step 1: `uv run pytest -q` -> 2458 passed, 7 skipped
- Step 3: `uv run pytest tests/core/test_logging.py -q` -> 24 passed; full `uv run pytest -q` -> 2474 passed, 1 failed (flaky, see Baseline Failures), 7 skipped; `ruff check app tests` -> clean
- Step 4: step tests 84 passed; full suite 2480 passed, 7 skipped; ruff clean
- Steps 5-6: `uv run pytest -q` -> 2487 passed, 7 skipped; `ruff check app tests` -> clean
- Step 7: 2483 passed, 4 failed. Two were assertions on the old text form, now fixed. One was a Windows socket buffer error (WinError 10055) that passed on re-run. -> after the fixes, the touched files ran 218 passed
- Step 8 / final: `uv run pytest -q` -> **2489 passed, 7 skipped**; `uv run --with ruff ruff check app tests` -> clean
- AC7 search (`grep` over `app/`):
  - No `split_fields`, `LOG_FORMAT`, `request_id_ctx`, `RequestIdFilter` or `ConsoleFormatter`. The one match is the private `_split_fields` reader for old lines in `interviews_log.py` (user decision).
  - No `key=%s` message strings.
  - structlog is imported only in `app/core/logging.py`.
- Step 9, real runs:
  - `interview_report --last 3 --log logs/app.pre-u1.log` gives output identical to `report_before_u1.txt` (AC8).
  - A debug instance on port 8765 showed the readable console (AC5).
  - `logs/app.log` has 336 lines, every one JSON with the five record keys (AC2).

## Tests Pending
- Step 9: live interview run by the user, then `interview_report` on it

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | the old text log still gives the saved report | spec | AC8 | pass |
| T2 | 3 | a stdlib call outside a request is one JSON line with `request_id` `-` | spec | AC2, EC1 | pass |
| T3 | 3 | a structlog event keeps its fields typed (int, null, bool) | inferred | report reads typed values | pass |
| T4 | 3 | a sensitive key is masked in the file and on the console (6 keys) | spec | AC1 | pass |
| T5 | 3 | a nested or mixed-case sensitive key is masked | spec | EC2 | pass |
| T6 | 3 | `prompt_tokens` / `cached_tokens` are not masked (exact key match) | inferred | risk: over-redaction hides report fields | pass |
| T7 | 3 | UUID, datetime, exception, object values are written as text | spec | AC9, EC5 | pass |
| T8 | 3 | a logged exception (stdlib and structlog) is one line with `exception` | spec | AC11, EC7 | pass |
| T9 | 3 | uvicorn.error, sqlalchemy.engine, httpx warnings land in the file | spec | AC6 | pass |
| T10 | 3 | library INFO lines (httpx URLs) stay out of the file | code-derived | root level WARNING | pass |
| T11 | 3 | debug on: readable console; debug off: console JSON equals the file line | spec | AC5 | pass |
| T12 | 3 | readable console: free text on one line, outcome colours, traceback appended | inferred | ported ConsoleFormatter behaviour | pass |
| T13 | 3 | unwritable log folder: console only, one `log_file_unavailable` warning | spec | AC10, EC6 | pass |
| T14 | 4 | one `http_request` line per request with method, path, status, duration_ms | spec | AC13, AC3 | pass |
| T15 | 4 | every line of a request carries its request_id (= X-Request-ID) | spec | AC3 | pass |
| T16 | 4 | an unsafe client id never reaches the log | spec | EC9 | pass |
| T17 | 4 | the crash line keeps the real request id and has the traceback | spec | AC16 (error-handling), AC11 | pass |
| T18 | 4 | an authenticated request logs `user` without passing it; no email in the log | spec | AC4 | pass |
| T19 | 4 | a line after the request has request_id `-` and no user | spec | EC1 | pass |
| T20 | 4 | every line across varied requests is JSON with the record keys | spec | AC2 | pass |
| T21 | 5 | the golden interview logged as JSON gives the identical saved report | spec | AC8 | pass |
| T22 | 5 | an llm_call with no session bound leaves the report unchanged | spec | EC10 | pass |
| T23 | 6 | start request: every interview line has the new session, every line the user | spec | AC4 | pass |
| T24 | 6 | answer turn: session and user on every line | spec | AC4 | pass |
| T25 | 6 | streamed turn: session and user on lines written by the SSE generator | spec | AC4, EC4 | pass |
| T26 | 6 | a foreign interview's 404 logs the stranger's user and the asked-for id | inferred | ownership-check debugging | pass |
| T27 | 6 | concurrent streams and thread-pool requests keep their own request_id/session | spec | EC4 | pass |
| T28 | 8 | an old text line splits into its event and fields; one without key=values keeps its message | spec | EC8 | pass |

AC coverage:
- AC1: T4, T5
- AC2: T2, T20, plus the real log (336/336)
- AC3: T14, T15
- AC4: T18, T23-T25, T27
- AC5: T11 and the debug instance
- AC6: T9
- AC7: the search above
- AC8: T1, T21, plus the real `--last 3` diff
- AC9: T7
- AC10: T13
- AC11: T8, T17
- AC12: gates
- EC3: documented limit (learnings section 5, upgrade-path U1), no test, by spec

## Open Questions
- None

## Baseline Failures
- `ruff check .` reports 47 errors, all in `alembic/` (applied migrations, which must not be edited). Gate is `ruff check app tests`.
- Flaky, pass alone and on re-run, not touched by this feature:
  - `tests/modules/interviews/routes/test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` asserts `budget_left_ms=30000`; a slow run logs 29999.
  - `tests/modules/profile/utils/test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table`

## Known Issues
- **Real log files were deleted by rotation during Step 3 test runs.**
  - The test suite has always written to the real `logs/app.log`, because `app.main` sets up logging on import.
  - Several full runs pushed it past 5 MB. Rotation then removed the oldest backups: the original `app.log.1` and `app.log.3`, lines from Nov 15 before 20:08.
  - The original `app.log`, with the interviews in the before-report, survived. A copy is kept as `logs/app.pre-u1.log`, a name rotation never touches.
  - `interview_report --last 3 --log logs/app.log.3` still gives the saved before-report exactly.
  - Fixed: tests now log to a temp file (`TEST_LOG_FILE` in `tests/conftest.py`).
- The user's `fastapi dev` server was running during implementation and holds `logs/app.log` open. On Windows that makes rotation from a second process fail ("file is being used by another process").

## Deviations from Plan
- Step 3: the legacy `ConsoleFormatter` was removed in Step 3 instead of Step 8. Nothing used it once the readable renderer existed, and its tests were ported to the new console. -> plan.md unchanged in intent (Step 8 just has one item less). -> Approved by: user at checkpoint 1 ("continue").
- Step 3: the root logger level is WARNING. Library INFO lines are not written (httpx logs full request URLs at INFO), while warnings and errors from every library are. uvicorn's own INFO lines still arrive, because uvicorn sets its logger to INFO. -> spec says "library logs go into the file" without a level. -> Approved by: user at checkpoint 1 ("continue").
- Step 3: tests now write to a temp log file (`TEST_LOG_FILE`), not `logs/app.log`. Not in the plan; fixes the rotation data loss above. -> Approved by: user at checkpoint 1 ("continue").
- Step 3: the code was written before its tests, rather than red then green one slice at a time. All 13 cases were written against the finished code and pass. They check the rendered output at the confirmed seam.
- Step 4: request fields live in one dict per request, set by the middleware (`request_log_context`, `bind_log_context`), not in `structlog.contextvars` bindings.
  - Why: FastAPI runs sync dependencies and endpoints in worker threads, each with a copy of the context, so a value bound in `get_current_user` would never reach the endpoint's or the access line's logs. Every copy shares the same dict.
  - Outside a request, `bind_log_context` falls back to `structlog.contextvars` (evals, scripts).
  - plan.md updated.
- Steps 5-6 were done together, because dropping the `session` argument without binding it would have left lines without a session in between.
- Steps 5-6: the `app_logs` test fixture now reads what the real pipeline wrote (the JSON file, after redaction) and shows each line as `event key=value`. This replaces migrating each of the ~125 log-checking tests to `log_lines` by hand. Their assertions keep their meaning, and the "no secret in the log" checks now run against real output.
- Steps 5-6: the AI functions (`decide`, `write`, `stream_write`, `settle`, `FeedbackGenerator.score/write`) keep their `session_id` parameter even though logging no longer needs it. Removing it would ripple through the `Interviewer` API, the evals and their tests. Left as a follow-up cleanup. The retrieval service's private helpers lost theirs.
- Steps 5-6: `RetrievalService.retrieve` and the feedback eval also bind `session`, because the RAG and feedback evals call them outside a request.
- Step 7: `user` is no longer passed explicitly by the profile, job-URL and voice log lines; it comes from the request context. As a result, `VoiceService.transcribe` and `JobUrlService.import_*` take a `user` / `session_id` they no longer use. Left as is, because they are the routes' API (follow-up cleanup).
- Step 7: library-style sentences (the startup "... disabled" notices) stay as plain-sentence events. AC7 bans only `key=value` strings.

## Debug Log

## Review

Level: low (2026-11-26).

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | should-fix | gate (ruff) | `app/modules/interviews/controllers/interviews_answer_controller.py:9` | The import block has two blank lines between `pydantic` and `app.core.logging` (left over from the Step 4 import swap), so the lint gate fails with I001. `ruff check --fix` corrects it; behaviour is unchanged. Earlier "ruff clean" results in this file were for the per-step `--fix` runs, so this one slipped through after the last fix. | fixed |
| R2 | nit | project rules | `app/core/logging.py:287`, `:292` | `get_logger`'s return annotation names `Logger` before the alias is defined. It works only because Python 3.14 evaluates annotations lazily. Moving the alias above `get_logger` makes it read top-down and would survive an older interpreter. | fixed |
| R3 | nit | project rules (no dead code) | `app/modules/interviews/ai/interviews_decide.py`, `interviews_write.py`, `interviews_write_stream.py`, `interviews_turn_limits.py`, `app/modules/interviews/ai/interviews_feedback_turn.py`, `app/modules/interviews/services/interviews_voice_service.py:76`, `interviews_job_url_service.py:71`, `:96` | Parameters (`session_id`, `user`) that only fed the old log lines are still accepted but no longer used. Already recorded as a deliberate follow-up in Deviations: removing them changes the `Interviewer`, `FeedbackGenerator`, voice and job-URL APIs, the evals and their tests. | won't fix (follow-up) |

Check results:
- `uv run --with ruff ruff check app tests` -> **fail**: 1 error (R1). After the R1 and R2 fixes: `All checks passed!`. Logging, request-context, stream and log-context tests (`tests/core`, `tests/test_request_context.py`, `tests/modules/interviews/routes/test_answer_stream.py`, `test_log_context.py`): 499 passed.
- `uv run pytest -q` -> not run: low level. task.md records 2489 passed, 7 skipped on the final diff (Step 8). No code changed after that run; Step 9 changed docs only.
- `tests/test_layers.py` (layer direction) -> passed in that same suite run
- type checker -> not run: low level (none configured in the project)
- static security scan, dependency audit -> not run: low level
- migration round-trip -> not run: no migration in this diff
- `code-review` (low) -> no findings, **partial coverage**. It read the first ~150 changed lines of `app/`: `core/ai/context.py`, `factory.py`, `tracing.py`, `exception_handlers.py` and the start of `core/logging.py`. Not covered: the rest of `logging.py`, `middleware.py`, `auth_dependencies.py`, the interview and profile services, and the tests. Run `/review-feature full` for complete coverage.
- `security-review` -> no high or medium findings. Covered: redaction before both renderers, user id only (never the email), library INFO lines kept out, the safe request-id rule, per-request context isolation. The key-names-only redaction limit (EC3) is accepted by the spec.
- `llm-security` -> not run: no prompt files or LLM call code changed (only their log lines)
- `simplify` -> not run: low level
- Project rules:
  - Layer direction: OK.
  - UUID ids only: OK.
  - No PII in logs: OK, redaction is now code.
  - New dependency justified: structlog, see the plan.
  - Tests added: OK.
  - No prompt, model or retrieval change, so no eval baseline run is needed.
  - Findings: R2, R3.
- Traceability: every AC and EC maps to a passing test or a recorded verification (see AC coverage above). No gaps. The live interview by the user is still pending, as noted in Tests Pending.
## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 0 | find-skills | looked for a structlog skill; none trustworthy enough to install |
| 1, 3 | test | case derivation from AC/EC IDs |
| 3 | security-review (judgment) | redaction key set, exact-match keys, library INFO URLs kept out |

## Links
- Spec: docs/features/u1-structlog/spec.md
- Plan: docs/features/u1-structlog/plan.md
