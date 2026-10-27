# Cuewise BE — Project Instructions

## About the Project
- This repo is the **API / backend for Cuewise**, an **AI interview coach**.
- It is a **learning project**: the goal is to learn the fundamentals of **AI engineering** (LLM integration, prompting, RAG/embeddings, evaluation, etc.) by building something real.
- When implementing AI features, favor clarity and explaining the *why* (trade-offs, concepts) over clever shortcuts; keep AI logic modular and swappable (e.g. provider/model behind an abstraction, prompts kept separate from code).

FastAPI backend (Python, `uv`, SQLAlchemy + Alembic). Code lives in `app/`.

## Git Rules (STRICT)
- **NEVER commit, push, or open PRs** unless the user explicitly asks in that message.
- Don't stage files, amend, rebase, or reset either. Leave all changes in the working tree for the user to review.

## Tooling
- **Always use lean-ctx** for project work:
  - `ctx_compose` to orient first; `ctx_read` (not native Read) for exploration; `ctx_search` instead of Grep; `ctx_glob` instead of Glob; `ctx_tree` instead of ls/find; `ctx_shell` for commands.
  - Edits: `ctx_read(mode="anchored")` → `ctx_patch`. Native `Read` only for the edit gate.
- **Always use graphify**:
  - Before answering codebase questions, if `graphify-out/graph.json` exists run `graphify query "<question>"` (also `graphify path "<A>" "<B>"`, `graphify explain "<concept>"`).
  - Use `graphify-out/wiki/index.md` for broad navigation; read `GRAPH_REPORT.md` only for architecture reviews.
  - **After finishing a task that changes code, run `graphify update .`** to keep the graph current.

## Architecture: Modular, Feature-Driven
Request flow: **router → controller (service) → repository**.

```
app/
  core/        # cross-cutting: config, errors, exception_handlers, logging, middleware, security (passwords), tokens (JWT)
  db/          # engine/session, base models
  modules/
    <feature>/                     # e.g. auth/, users/
      <feature>_route.py           # HTTP only: path, status code, deps, response_model. No business logic.
      <feature>_controller.py      # business logic / orchestration. No HTTP objects, no raw SQL.
      <feature>_repository.py      # all DB access. No business rules.
      <feature>_schema.py          # Pydantic request/response models (never expose ORM models)
      <feature>_utils.py           # feature-local pure helpers
      (<feature>_model.py / <feature>_dependencies.py / <feature>_constants.py as needed)
  main.py      # app factory, middleware, router registration
tests/modules/<feature>/   # mirrors app/modules
```

Rules:
- **File naming:** every file in a feature module is prefixed with the module folder name and an underscore (`auth/auth_controller.py`, `users/users_route.py`), so open tabs and tracebacks are unambiguous. Use `_`, never `.` (`auth.controller.py` is not importable in Python).
- Every feature module **always** has `<feature>_schema.py` and `<feature>_utils.py` (alongside route/controller/repository).
- Layers only call downward: router → controller → repository. Never skip a layer or import upward.
- Shared, feature-agnostic helpers go in `app/core/`, not duplicated across modules.
- Features don't import each other's repositories; go through the other feature's controller.

## Code Principles
- **DRY**: extract repeated logic into `<feature>_utils.py` / `core/`; reuse existing code before writing new.
- **Separation of concerns**: one responsibility per file/function; HTTP, business logic, and persistence stay apart.
- Match surrounding style, naming, and comment density. No speculative abstractions (YAGNI).
- Type-hint everything; use `async` consistently (don't mix blocking I/O into async routes).
- **IDs: every table's primary key (and every foreign key to it) is a UUID, never an auto-increment integer.** Use time-ordered UUIDv7 (`uuid.uuid7()` from the stdlib, Python 3.14+) generated in the app, never by the DB: every model inherits `UUIDPrimaryKeyMixin` from `app/db/mixins.py` instead of declaring its own `id`. Reasons: IDs in URLs/tokens can't be guessed or enumerated, and they stay unique across tables and environments. Routes, schemas and JWT `sub` carry the UUID as a string; never expose or accept integer IDs.

## Security
- **Auth**: JWT (short-lived access tokens, validate `exp`, `iss`, `aud`, signature algorithm explicitly). Protect routes via `Depends(...)` auth dependencies; default-deny.
- **Passwords**: hash with Argon2/bcrypt only (via `core/security.py`); never log or return hashes/secrets.
- **Secrets/config**: only from env via `pydantic-settings` (`core/config.py`); never hardcode; never commit `.env`. Provide `.env.example`.
- **Input validation**: Pydantic schemas on every input; constrain lengths, formats, enums; `extra="forbid"` where appropriate.
- **SQL**: SQLAlchemy ORM/parameterized queries only; never build SQL via string formatting.
- **Responses**: use `response_model` to whitelist fields; never leak internals, stack traces, or ORM objects.
- **Errors**: raise the project's structured errors (`core/errors.py`); generic messages to clients, details to logs with request ID.
- **CORS**: explicit origin allowlist; no `*` with credentials.
- **Rate limiting** on auth/sensitive endpoints; enforce authorization (ownership checks) in controllers, not just authentication.
- Add security headers, HTTPS-only in prod, and keep dependencies updated/audited.
- Don't log PII, tokens, or passwords.

## FastAPI Best Practices & Standards
- One `APIRouter` per feature with `prefix` and `tags`; register in `main.py`.
- Use dependency injection (`Depends`) for DB sessions, current user, settings; no globals.
- Explicit `status_code` and `response_model` on every route; document errors via `responses=`.
- Keep routes thin; no business logic or DB calls in routers.
- DB: one session per request via dependency; transactions managed in controller/repository boundary; schema changes only through **Alembic migrations** (never edit DB by hand, never rely on `create_all`).
- Version the API (`/api/v1`). Use plural nouns, proper HTTP verbs/status codes; paginate list endpoints.
- Structured logging with request ID tracing (see `core/logging.py`, `core/middleware.py`).
- Provide health/readiness endpoints.
- Python: PEP 8, type hints, `ruff` for lint/format; no bare `except`; no mutable default args.
- Dependencies managed with `uv` (`pyproject.toml` + `uv.lock`).

## Testing
- `pytest` under `tests/`, mirroring `app/modules`. Cover happy path, validation errors, auth/authz failures.
- Run tests after changes (`uv run pytest`) and report real results.

## Common Commands
- Install deps: `uv sync`
- Run dev server: `uv run fastapi dev app/main.py` (or `uv run uvicorn app.main:app --reload`)
- Tests: `uv run pytest`
- Lint/format: `uv run ruff check . && uv run ruff format .`
- Migrations: `uv run alembic revision --autogenerate -m "<msg>"` then `uv run alembic upgrade head` (always review the generated migration)

## AI Engineering Guidelines
- **Provider abstraction**: LLM/embedding calls live behind an interface in the feature (or `core/ai/`); no direct SDK calls from routers or controllers.
- **Prompts are data, not inline strings**: keep them in dedicated, versioned files/modules; no prompt text scattered through business logic.
- **Structured outputs**: validate all LLM output with Pydantic schemas; handle malformed/empty responses with retries and a safe fallback.
- **Cost & reliability**: set timeouts, retries with backoff, max tokens, and log token usage/latency per call. Never block the event loop; use async clients.
- **Prompt-injection safety**: treat user text (answers, resumes, job descriptions) as untrusted; separate instructions from user content, never let it alter system behavior, and never put secrets in prompts.
- **Privacy**: interview answers/resumes are personal data; don't log raw content, and minimize what is sent to providers.
- **Evaluation**: add a small eval set (sample inputs + expected qualities) for each AI feature so prompt/model changes can be compared, not guessed.
- **Tests**: mock the LLM in unit tests (deterministic); keep real-model calls in separate, opt-in tests.
- **RAG** (when added): keep ingestion, chunking, embedding, retrieval, and generation as separate, individually testable steps.
- **Teach as you build**: when adding an AI concept, briefly explain what it is and why it was chosen over alternatives.

## Workflow / Definition of Done
1. Orient with graphify + `ctx_compose` before changing anything.
2. Implement within the router → controller → repository layers (schema/utils included).
3. Add/update tests and run them; run lint.
4. Run `graphify update .`.
5. Summarize what changed and what's left. **Do not commit or push.**

## Don'ts
- Don't hardcode secrets, API keys, or model names/URLs; use config.
- Don't add dependencies without saying why (prefer stdlib / already-installed first).
- Don't edit applied Alembic migrations; add a new one.
- Don't swallow exceptions or return raw exception text to clients.
- Don't over-engineer: ship the minimum that works, then iterate.
