# Feature: Langfuse Tracing

## Problem
LLM behaviour (what was sent, what came back, cost, latency, retries) is only visible in structured logs and in
token columns stored per interview. There is no way to open one interview turn and see its full chain of LLM calls,
inputs and outputs, so debugging prompts and comparing prompt versions is guesswork.

## Goal
Every LLM call made by the API appears in Langfuse (Hobby plan, Cloud) as a generation, grouped into one trace per
request, labelled with the user and interview session, with full prompt and output content. Tracing never slows or
breaks a request, and is fully off when no keys are configured.

## Project Conventions
- Consulted: `CLAUDE.md` (cuewise-be); no `.claude/rules/` exists.
- Constraints it imposes:
  - Vendor SDK calls stay behind an abstraction in `core/ai/`; no Langfuse calls in routers.
  - Config only from env via `pydantic-settings` (`core/config.py`); secrets are `SecretStr`; `.env.example` updated.
  - Don't log PII, tokens or passwords: Langfuse errors written to our own logs must not contain prompt/answer content.
  - Never block the event loop; the LLM provider keeps its sync `complete()` and async `stream()` contract.
  - Tests mock the LLM and must not make network calls to Langfuse.
  - Privacy guideline ("don't log raw content") is deliberately overridden for Langfuse by the owner's decision: **full content is captured** (see Constraints).

## User Flow
Developer-facing (no end-user change):
1. A candidate starts an interview or answers a question (normal or streamed).
2. The API opens one Langfuse trace for that request, tagged with the user id and interview session id.
3. Each LLM call inside the request is recorded as a generation under that trace (prompt, reply, model, tokens, latency, labels).
4. The developer opens the Langfuse dashboard, finds the session, and inspects each turn.
5. On app shutdown, buffered events are flushed.

## Requirements

### Functional
- Settings: optional `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_BASE_URL`, and `APP_ENV` (default `development`). Tracing is enabled only when both keys are present.
- One trace per request for exactly these operations: start interview, answer (sync), answer (stream). Other routes are not traced.
- Each LLM call (`complete()` and `stream()` on the provider) is one generation: model, input messages, output text, token usage (prompt, completion, cached, reasoning), latency, finish reason.
- A call that retried is still one generation; `attempts` is metadata.
- Generation metadata carries the app labels: `task`, `prompt_version`, `attempts`, `finish_reason`, `budget_left`.
- Trace carries `user_id` and `session_id` (interview session UUID as string) and `environment` from `APP_ENV`.
- Failed calls end the generation at level ERROR with the error class name and status code (no raw exception text).
- Stream cut short (client disconnect or turn deadline): the generation ends with the text received so far, level WARNING, status message `cancelled`.
- Offline eval script traces its calls with `environment=eval`.
- The client is flushed and shut down in the app lifespan shutdown.

### Non-Functional
- Fail-open: any Langfuse error (bad keys, outage, timeout, SDK exception) is swallowed and logged without content; the request and the LLM result are unaffected.
- No added latency on the request path beyond in-memory span creation (SDK exports in the background).
- Hobby-plan budget: one generation per LLM call, nothing per HTTP attempt or per stream chunk.
- Keys never appear in logs or error messages.

## UX Requirements
Not applicable (no UI, backend only). Frontend untouched.

## Constraints
- Provider uses plain httpx, so the OpenAI-SDK drop-in wrapper cannot be used; generations are created manually.
- Langfuse SDK reads `os.environ`, but `.env` is loaded by pydantic-settings only, so the client is built from `Settings` explicitly.
- **Full content privacy:** prompts include job descriptions and candidate answers, and are sent to Langfuse Cloud. Owner accepted this for the learning project. Any real-user rollout needs a revisit (masking or self-hosting).
- Langfuse Hobby: 50k units/month, limited retention (assumption — verify current limits).
- `langfuse>=5.1.0` already in `pyproject.toml`; no new dependencies.

## Blockers
- None. (Sampling is deferred; revisit if the Hobby quota is hit.)

## Edge Cases
- **EC1:** `LANGFUSE_*` keys blank or missing -> tracing is a no-op, app starts, no network calls, no warnings per request.
- **EC2:** Only one of public/secret key set -> tracing off, one startup warning (no key values), app starts.
- **EC3:** Langfuse unreachable or returns auth error -> requests and LLM results unchanged; failures logged without content; request latency not noticeably affected.
- **EC4:** Tracing SDK raises inside the provider -> exception swallowed, LLM result returned normally.
- **EC5:** LLM call fails after retries -> generation ends ERROR with error class and status code; the original `LLMError` still propagates unchanged.
- **EC6:** Client disconnects mid-stream -> generation closed with partial text, WARNING, `cancelled`; no hanging open observation.
- **EC7:** Turn deadline ends the stream mid-way -> same as EC6, and the existing `LLMTimeoutError` behaviour is unchanged.
- **EC8:** Provider returns no usage -> usage fields omitted, never guessed (matches `LLMResult` None semantics).
- **EC9:** LLM call outside a traced request (e.g. unit test, script) -> no crash; recorded as its own trace or skipped, never an error.
- **EC10:** App shutdown with unsent events -> flush attempted once; a flush failure or timeout does not block shutdown indefinitely (assumption — verify SDK shutdown timeout).
- **EC11:** Two concurrent requests -> each has its own trace with its own user_id/session_id; no attribute bleed between them.
- **EC12:** Test suite run -> no outbound Langfuse traffic; tracing disabled or faked.

## Acceptance Criteria
- [ ] **AC1:** With keys set, starting an interview with a long job description produces one Langfuse trace containing the summary generation, with user_id, session_id and environment set. (EC1, EC11)
- [ ] **AC2:** Answering via `POST /messages` produces one trace whose generations cover every LLM call of that turn (e.g. decide, interviewer) with full input and output text.
- [ ] **AC3:** Answering via `POST /messages/stream` produces one trace with the streamed generation, ending with final text, usage and latency.
- [ ] **AC4:** Each generation records model, prompt/completion/cached/reasoning tokens (omitted when not reported), latency, finish_reason, attempts, task, prompt_version and budget_left. (EC8)
- [ ] **AC5:** A retried call is one generation with `attempts` > 1.
- [ ] **AC6:** A failed call ends ERROR with error class and status code, and the same `LLMError` is raised to the caller. (EC5)
- [ ] **AC7:** A cancelled or deadline-cut stream ends WARNING `cancelled` with partial text. (EC6, EC7)
- [ ] **AC8:** With keys blank, the app starts and serves requests with no Langfuse network calls; with one key only, a single startup warning. (EC1, EC2)
- [ ] **AC9:** When the Langfuse client raises or the host is unreachable, endpoints return the same responses as without tracing. (EC3, EC4)
- [ ] **AC10:** Lifespan shutdown flushes the client; shutdown completes even if flush fails. (EC10)
- [ ] **AC11:** Auth, users, health, get, transcript and report routes create no traces.
- [ ] **AC12:** Eval script runs appear with `environment=eval`.
- [ ] **AC13:** `uv run pytest` and `ruff` pass with no network access to Langfuse; new tests cover disabled mode, fail-open, error, and cancelled paths. (EC12)
- [ ] **AC14:** `.env.example` lists `LANGFUSE_*` and `APP_ENV`; no key values appear in logs.

## Out of Scope
- Frontend / client-side tracing (backend only, per owner).
- Masking or redaction of content (owner chose full content; revisit before real users).
- Sampling and `LANGFUSE_SAMPLE_RATE` (not needed at current volume).
- Langfuse prompt management, datasets, scores/evals (existing prompts stay in code).
- Replacing the existing `log_llm_call` logging or the stored token columns.
- Tracing non-LLM routes, DB queries or HTTP spans.
- Per-HTTP-attempt observations and per-chunk events (Hobby-plan units).
