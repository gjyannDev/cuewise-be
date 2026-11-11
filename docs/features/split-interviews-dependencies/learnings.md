# Learn: Splitting the interviews dependency wiring

> Status: done. A pure move, no behavior change; the full suite matches the baseline.

## 1. Why it exists
`dependencies/interviews_dependencies.py` held every piece of request wiring for the interviews feature in 241
lines: startup lookups, small providers, two rate limiters and the service/controller builders for four use cases.
Finding one thing meant scanning past the rest, and every new feature made it longer.

## 2. What it is
- **Dependency (FastAPI):** a function a route, or another dependency, asks for with `Depends(...)`. FastAPI calls it
  for each request and passes in the result.
- **Composition root:** the one place that builds objects from their parts. Services receive what they need; they
  never build it. That is what this folder is.
- **The split:** one shared file and one file per use case.

| File | Holds |
|---|---|
| `interviews_shared_dependencies.py` | `app.state` lookups (LLM, transcriber, embedder, tracer) and small providers (bank, clock, now, context manager) |
| `interviews_start_dependencies.py` | retrieval service, interviews service, controller |
| `interviews_answer_dependencies.py` | answer service, controller |
| `interviews_transcription_dependencies.py` | limiter, guard, service, controller |
| `interviews_feedback_dependencies.py` | limiter, guard, service, controller |

## 3. When to use it
Split a wiring file by use case when it mixes unrelated builders. Keep shared pieces in one file that imports none of
the use-case files, so imports only point one way and no cycle can form. Don't split per function: a service, its
controller and its alias read best together.

## 4. How it works
A start request, walked through:
1. The route asks for `InterviewsControllerDep` (`app/modules/interviews/dependencies/interviews_start_dependencies.py:70`).
2. That calls `get_interviews_controller` (`:64`), which asks for `get_interviews_service` (`:41`).
3. The service builder asks for the database session, bank, LLM, clock, context manager and tracer from
   `interviews_shared_dependencies.py`, plus `get_retrieval_service` (`:31`), which asks for `get_embedder`
   (`interviews_shared_dependencies.py:33`).
4. Within one request, FastAPI runs each dependency once and reuses the result, so the service and the retrieval
   repository share one database session.

Decisions:
- **No re-export facade.** The project bans re-exports from layer `__init__.py` files, and a facade would hide where
  each function lives. Every importer was repointed instead.
- **Limiters live with their guard.** `TRANSCRIPTION_LIMITER` and `limit_transcriptions` are read together; a separate
  "limits" file would split them for no gain.

## 5. What can go wrong
| Failure | What happens | Test |
|---|---|---|
| A test keeps importing from the old module | It fails at import time, so it can't silently skip its override | every route test |
| A use-case file imports another use-case file | A cycle could form; none do (each imports only the shared file) | `tests/test_layers.py::test_the_real_tree_follows_the_layer_rules` |
| A limiter is created twice | Counts would split; each stays one module-level instance | `tests/modules/interviews/routes/test_feedback_endpoint.py` (rate-limit cases) |

## 6. Try it yourself
1. Predict: if `test_tracing_routes.py` imported `get_tracer` from `interviews_start_dependencies` (which imports it from
   the shared file), would `app.dependency_overrides[get_tracer]` still work? (Yes: it is the same function object;
   overrides match by identity, not by module path.)
2. Run `uv run pytest tests/test_layers.py -q` and open the new files: each fits on one screen.

## 7. What surprised me
- Ruff's import sorter (I001) failed on five importers after the move: replacing one import with two changes their
  sort order. Run ruff on every touched importer, not only the new files.

## 8. Check your understanding
1. Why can't the shared file import a use-case file?
2. Why does deleting the old file make the change safer than keeping a facade?

<details>
<summary>Answers</summary>

1. Use-case files import the shared file. If the shared file imported one back, Python would hit a circular import,
   and the one-way rule that makes the folder easy to read would be gone.
2. A forgotten import fails loudly at once. With a facade, it would keep working, and the old name would spread again.

</details>

## 9. Still open
- Nothing for this change.
