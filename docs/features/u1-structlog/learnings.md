# Learn: structured logging with structlog (U1)

**Concepts:** structured logs, the processor pipeline, redaction as code, context binding across threads and async code, migrating a log format without breaking its readers. **Status:** built and measured on 2026-11-26. One live interview is still **pending** (see section 9).

## 1. Why it exists
Before U1, a log line was a string like `llm_call session=… task=… latency_ms=191 outcome=ok`.
- The report (`interview_report`) turned it back into data with a regex plus `split_fields`. A value with a space in it, or a renamed word, silently broke a number. Nothing raised.
- "No PII in logs" was a rule each developer had to remember at every call site.
- `session` and `user` were passed by hand. That meant ~40 calls passed `session_id` only so the log line could carry it.
- Library logs (uvicorn, SQLAlchemy, httpx) never reached `logs/app.log`.

## 2. What it is
Every log call is now an **event name plus fields**: `log.info("llm_call", task="write", latency_ms=191)`. Before anything is written, the event passes through a chain of small functions, the **processors**. Each one takes the event dict and returns it changed. The last one **renders** it: one JSON object per line in the file, or a readable block on the dev console.

    call ──► merge request fields ──► logger, level, timestamp ──► request_id "-" if none ──► traceback ──► REDACT ──► render
                                                                                                              ├─► file: JSON line
                                                                                                              └─► console: JSON, or the readable view in debug

Because redaction sits before both renderers, no output can skip it.

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| `get_logger("app.x").info("event_name", key=value)` | Every new log line | Fields stay typed (int, bool, null); the report and `jq` read them directly |
| `bind_log_context(session=...)` | Once, where a service first knows the id | Every later line of the request carries it; don't pass it to each call |
| A free-text sentence as the event | One-off notices (startup warnings) | Fine; only `key=value` strings inside a message are banned |
| Add a key to `SENSITIVE_KEYS` | A new field could hold user text or a secret | Key names only. A secret inside a sentence is **not** caught |

**I'd revisit this when** logs are shipped to a hosted service. That needs pattern-based scrubbing and sampling, which key-based redaction doesn't give.

## 4. How it works
| Option | Verdict |
|---|---|
| structlog on top of stdlib `logging` (`ProcessorFormatter` on the root handlers) | **Chosen**: one pipeline for app, library and not-yet-converted calls; keeps the rotating file handler |
| Pure structlog writing the file itself | Rejected: library logs would need a second pipeline, so redaction would be wired twice |
| stdlib only with a JSON formatter | Rejected: U1 exists to learn structlog |

**One answer turn, walked through the code:**
1. `RequestContextMiddleware` creates the request's field dict `{"request_id": …}` and enters `request_log_context` (`app/core/middleware.py:34`, `:52`).
2. FastAPI runs `get_current_user` in a worker thread. It calls `bind_log_context(user=…)` (`app/modules/auth/dependencies/auth_dependencies.py:44`), which updates that same dict (`app/core/logging.py:90`).
3. `AnswerService.prepare_answer` binds `session` (`app/modules/interviews/services/interviews_answer_service.py:180`).
4. The decide call logs `llm_call` through `log_llm_call` (`app/modules/interviews/ai/interviews_turn_log.py:27`). It passes no session.
5. The chain `_SHARED` (`app/core/logging.py:135`) runs on the event:
   - `_merge_request_fields` (`:107`) adds `request_id`, `user` and `session`.
   - `redact_sensitive` (`:130`) masks any sensitive key.
   - The JSON renderer writes the line.
6. The middleware logs `http_request` with the same fields when the response ends.
7. `interview_report` reads the line through `parse_log` (`app/modules/interviews/tooling/interviews_log.py:79`). JSON lines go to `_json_event` (`:100`); old text lines still go to `_split_fields` (`:118`).

**The surprise that shaped step 2:** structlog's own `contextvars` binding was not enough. FastAPI runs sync dependencies and sync endpoints in worker threads, and each thread gets a **copy** of the context. A value bound in the copy never flows back, so `user` bound in `get_current_user` would vanish before the endpoint logged anything.

The fix is one mutable dict per request: every copy holds a reference to the same dict, so an update in any thread is seen everywhere. `test_concurrent_requests_and_streams_keep_their_own_context` fails without it.

## 5. What can go wrong
| Failure | What the user sees | What the code does | Proof (test name) |
|---|---|---|---|
| A field named `answer` / `password` / `authorization` is logged | Nothing | Value becomes `[redacted]` in file and console, any depth, any case | `test_a_sensitive_key_is_masked_in_the_file_and_on_the_console`, `test_a_nested_or_mixed_case_sensitive_key_is_masked` |
| A UUID, datetime or exception is logged as a value | Nothing | Written as text; the line stays valid JSON | `test_a_value_json_cannot_encode_is_written_as_text` |
| `logs/` can't be written | Nothing; the API runs | Console only, one `log_file_unavailable` warning | `test_an_unwritable_log_folder_falls_back_to_the_console_with_one_warning` |
| Two requests run at once, one streaming | Nothing | Each line keeps its own request's ids | `test_concurrent_requests_and_streams_keep_their_own_context` |
| The log format changes again | Wrong report numbers | The golden file test breaks first | `test_the_same_interview_logged_as_json_gives_the_same_report` |
| httpx logs a URL with a key in its query | Nothing | Library INFO lines are not written (root level WARNING) | `test_library_info_lines_stay_out_of_the_file` |
| A secret inside free text (an exception message) | Nothing visible, but it is in the log | **Not masked**: key names only | known limit, no test |

## 6. Try it yourself
1. **Predict:** what does the console show for one GET /health in debug mode? Then run `DEBUG=true uv run uvicorn app.main:app --port 8765` and call `/health`. You get one `http_request` block with `method`, `path`, `status` and `duration_ms` rows.
2. **Predict:** will the value appear in `logs/app.log` if you log `get_logger("app.test").info("try", Resume="hello")` from a Python shell after `setup_logging()`? Check the line.
3. **Predict:** what breaks if you remove `_merge_request_fields` from `_SHARED`? Run `uv run pytest tests/test_request_context.py -q` and read which tests fail and why.
4. Query the log as data: `uv run python -c "import json; [print(l['latency_ms']) for l in map(json.loads, open('logs/app.log', encoding='utf-8')) if l['event']=='llm_call']"`.

## 7. What surprised me
- **Same numbers, both formats** (2026-11-26):
  - `interview_report --last 3` on the same three interviews gives byte-identical output before and after the change. Before: saved as `docs/features/u1-structlog/report_before_u1.txt`. After: run with `--log logs/app.pre-u1.log`.
  - The golden interview emitted as JSON gives exactly the report saved from its old text form.
- **Real log after the change** (2026-11-26, local dev server): 336 lines in `logs/app.log`, 0 that fail to parse or miss a record key.
- **The test suite was writing the real log.**
  - Several full runs during the work rotated `logs/app.log` past 5 MB, and rotation deleted the two oldest backups for good.
  - Tests now log to a temp file. The interviews the before-report needs survived, copied to `logs/app.pre-u1.log`.
  - This was a hidden pre-existing hazard, not caused by structlog.
- **Thread copies of the context** (see section 4): the plan's "bind with `structlog.contextvars`" would have silently lost `user` on every sync endpoint.
- **Suite:** 2489 passed, 7 skipped (`uv run pytest -q`, 2026-11-26).
- **Live interview through the new pipeline:** **pending**. The user runs it, then `interview_report` on it.

## 8. Check your understanding
1. Why does redaction have to run before the renderer, not inside it?
2. When would `bind_log_context` fall back to `structlog.contextvars`, and is that safe?
3. How does a line written by the SSE generator, after the endpoint returned, still carry `session`?
4. What if someone logs `log.info("note", text=answer_text)`?

<details>
<summary>Reference answers (write yours first)</summary>

1. There are two renderers (file JSON and console), and more may come. A processor before the fork means every output gets the masked event; a renderer-level check would have to be repeated, and one could be forgotten.
2. Outside a request: evals, scripts, startup. There is no per-request dict there. It is safe because those run one case at a time, each case rebinds `session`, and the test fixtures clear the bindings afterwards.
3. The generator runs inside the request's task tree, so it sees the same context value, a reference to the request's dict, which `prepare_answer` already filled in.
4. It is written as is: `text` is not a sensitive key. Either add the key to `SENSITIVE_KEYS` or, better, don't log content at all. Log a length or a count instead, as the interview events do.

</details>

## 9. Go deeper / Still open
- Spec: `docs/features/u1-structlog/spec.md`; plan: `docs/features/u1-structlog/plan.md`; progress: `docs/features/u1-structlog/task.md`.
- Next slice that uses this: U2 (tenacity) logs each retry through these events (attempt, wait, error class), with the request's ids attached for free.
- Still open:
  - One live interview through the new pipeline, then `interview_report` on it (**pending**, user).
  - The AI functions (`decide`, `write`, `stream_write`, `settle`, `FeedbackGenerator.score/write`) and a few service methods still take a `session_id` / `user` they no longer use for logging (follow-up cleanup).
  - Free-text secrets are not scrubbed (key-based only).
