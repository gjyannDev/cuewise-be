# Learn: Layered architecture (route -> controller -> service -> repository)

Not an AI concept, but the frame every AI feature in this repo now sits in: where the LLM orchestration lives, and
what may and may not touch it.

## 1. Why it exists
Each feature module was a flat folder with the layer only in the filename, and the layer called "controller" was
really a service: `interviews_controller.py` (728 lines) mixed business rules, LLM orchestration and database calls
with response shaping, SSE framing and the 200/201 choice. Nothing stopped a route from reaching a repository.

## 2. What it is
Four layers, each in its own folder inside the feature, each calling only the one below:

| Layer | Job | Never |
|---|---|---|
| `routes/` | HTTP declaration: path, status code, dependencies, `response_model`, framework plumbing (threadpool, upload read, `EventSourceResponse`) | business logic, services, repositories |
| `controllers/` | request -> service call, domain result -> `*Out` schema, SSE frames, 200 vs 201 | repository, `app.core.ai`, DB session |
| `services/` | business rules, ownership checks, state changes, LLM orchestration, repository calls; raises `core/errors.py` errors | controllers, routes, `*Out` schemas |
| `repositories/` | database access | anything above |

Non-layer code has its own folders: `ai/` (interviewer, feedback generator, context strategies, reply parsers),
`tooling/` (evals and reports, offline only), `utils/`, `constants/`, `models/`, `schemas/`, `dependencies/`.

## 3. When to use it
Every new endpoint. A rule of thumb for "where does this line go?":
- It decides something about the domain (who owns this, what happens next, which LLM call) -> service.
- It changes the shape of data for the client (an `*Out`, an SSE frame, a status code) -> controller.
- It is SQL -> repository.
- It is FastAPI wiring -> route or `dependencies/`.

## 4. How it works
One streamed answer, walked through the code:

1. `app/modules/interviews/routes/interviews_route.py:134` `answer_question_stream` runs
   `ctrl.prepare_answer` in the threadpool, so the 404/409 checks fail as plain JSON before the stream opens.
2. `controllers/interviews_answer_controller.py:50` `stream_answer` wraps the service's stream in `aclosing` and turns
   each domain event into an SSE frame with `_frame` (`:69`).
3. `services/interviews_answer_service.py:335` `stream_answer` yields domain events: the ai module's `PhaseChanged`,
   `Delta`, `Reset`, plus `ReactionChosen`, `TurnSaved` and `TurnFailed`. It keeps the trace, the error handling and
   `log_stream_summary`, so the logs did not change.
4. `finish_answer` (`:260`) saves the whole turn, then `self.repo.refresh(ctx.session, current)` (`:332`) reloads the
   rows the commit expired, still in the worker thread.
5. `repositories/interviews_repository.py:88` `refresh` is the only new repository method.

Decisions and why:
- **Services return domain values, not `*Out`.** The controller then has a real job, and a service can be called from
  a script (`app/scripts/create_admin.py` calls `AuthService` directly) without HTTP shapes.
- **Services return loaded rows.** A controller that reads an expired ORM attribute would run a SELECT, and in the
  stream that would happen on the event loop. Refreshing in the service keeps the same two SELECTs in the worker thread.
- **Upload checks stay in the transcription service**, inside the same try/finally as its log line, so a rejected
  upload is still logged.
- **Shared code goes to `utils/interviews_session_utils.py`** (`owned_session` at `:52`, the bank and LLM question
  builders), so no service imports another.
- **Resources stay at the module root.** `MODULE_DIR` (`constants/interviews_constants.py:331`) is the one place that
  knows where `data/`, `prompts/` and `templates/` are.
- **The rules are a test.** `tests/test_layers.py:14` `check_layers` parses each file with `ast` (never imports it)
  and reports every forbidden import.

## 5. What can go wrong
| Failure | Caught by |
|---|---|
| A route imports a service or repository | `test_route_importing_a_service_or_repository_is_reported`, and `test_the_real_tree_follows_the_layer_rules` on the real code |
| A controller reaches the DB, a repository or the LLM | `test_controller_importing_a_repository_the_llm_or_the_db_session_is_reported` |
| A service builds a response schema | `test_service_importing_a_response_schema_is_reported` |
| A file is left at the module root | `test_a_layer_file_left_at_a_module_root_is_reported` |
| A client leaving mid-stream no longer closes the service stream (no summary log) | `tests/modules/interviews/controllers/test_stream_answer.py` (`test_closing_the_stream_mid_turn_saves_nothing`, `test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing`) |
| A moved file can't find a prompt or the bank | the question bank, prompt, rubric, eval and report tests (they load the real files) |
| The API changed | OpenAPI JSON before/after compared byte for byte (see section 7) |

Not caught by tests: a controller reading an unloaded ORM attribute (blocking I/O on the event loop). That is a
review item: services return refreshed rows or plain values.

## 6. Try it yourself
1. Add `from ..repositories.interviews_repository import InterviewsRepository` to
   `controllers/interviews_controller.py`. Predict: `uv run pytest tests/test_layers.py` fails and names the file and
   the import. Revert.
2. Return an `InterviewOut` from `InterviewsService.get`. Predict: the layer test fails with "service imports response
   schema". Revert.
3. Delete the `self.repo.refresh(...)` line in `finish_answer` and run the stream tests. Predict: they still pass
   (that is why it is a review item, not a test). Revert.

## 7. What surprised me
- The 728-line controller split cleanly by **who knows what**: the service knows the turn, the controller knows the
  wire format. Even the stream split along that line, with domain events in between.
- Measured on 2026-11-09 (local, `uv run pytest`, `uv run --with ruff ruff check .`):

| Check | Before | After |
|---|---|---|
| Tests collected | 1207 | 1216 (+9 layer tests) |
| Result | 1205 passed, 1 skipped, 1 failed | 1214 passed, 1 skipped, 1 failed (same unrelated failure) |
| Ruff errors | 77 | 64 (import sorting in moved files) |
| OpenAPI + `Base.metadata` JSON | snapshot | byte-identical |
| `uv run alembic check` | - | "No new upgrade operations detected." |

- Ruff is not a project dependency: `uv run ruff` fails, `uv run --with ruff ruff check .` works.

## 8. Check your understanding
1. Why does `TranscriptionService.transcribe` return a `str` and not a `TranscriptionOut`?
2. Why does `AnswerService` keep `log_stream_summary` instead of the controller?
3. Why is `refresh` called inside `finish_answer` and not in the controller?
4. Why does `check_layers` parse source instead of importing it?

<details>
<summary>Answers</summary>

1. Response schemas are the controller's job; the service returns the domain value (the text), so it can be reused
   without HTTP shapes, and the layer test forbids a service importing an `*Out`.
2. The summary depends on how the turn ended (done, lost race, error, client left), which only the service sees; the
   controller only renames events. Keeping it there kept the logs identical.
3. `finish_answer` runs in a worker thread (`anyio.to_thread.run_sync`); the controller's mapping runs on the event
   loop. Reloading in the service keeps database I/O off the loop.
4. Importing would execute the code (and a bad import could fail or have side effects); parsing just reads it, and
   works on synthetic sources in the tests.
</details>

## 9. Go deeper / Still open
- `interviews_utils.py` (562 lines) and `interviews_constants.py` (536 lines) were moved as-is; splitting them is a
  separate follow-up.
- `auth` and `users` controllers are near pass-through: the cost of "never skip a layer".
- The baseline failure in `tests/core/test_config.py` (`llm_max_tokens` 800 vs 4000) is unrelated and still open.
