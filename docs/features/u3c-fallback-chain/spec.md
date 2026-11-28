# Feature: U3c — Fallback chain, question bank removal, old LLM layer deleted

## Problem
Two things are half-done after U3a/U3b. The provider list (`LLM_PROVIDERS`, primary first) exists, but only the first
provider is ever built, so a provider outage is a total outage. And a hand-written question bank still quietly stands
in whenever the LLM is off or a turn's reply is unusable: that hides LLM failures from the metrics and keeps the old
LLM layer (`LLMProvider`, `openai_compatible.py`, `json_reply.py`, `TracingProvider`, `FakeProvider`) alive next to
LangChain. The maintainer wants one LLM stack (LangChain, inside `core/ai` and feature `ai/` folders), a real fallback
chain, and honest, retryable errors instead of silent bank questions.

## Goal
- Providers listed in `LLM_PROVIDERS` are tried in order; the trace and log say which one answered.
- The question bank and every "LLM off" mode are gone; a failed LLM turn is a clear retryable error and saves nothing.
- The old LLM layer is deleted (the `LLMError` family stays), and `tests/test_layers.py` allows `langchain*` only in
  `app/core/ai/` and feature `ai/` folders.
- Interview quality is unchanged on the single configured provider (write, decide, stream, feedback evals within the
  noise margin), and old sessions still read correctly.

## Project Conventions
- Rules consulted: `CLAUDE.md` (project), `docs/ai-engineering-upgrade-path.md` (U3c), memories `llm-provider-fallback-plan`,
  `langchain-migration-decision`, `u3b-split-decision`.
- Constraints they impose:
  - Route -> controller -> service -> repository; LangChain and vendor SDKs only in `app/core/ai/` and feature `ai/`
    folders. Vendor exceptions are mapped to `LLMError` types before leaving `core/ai/`.
  - Keep the `LLMError` family, `Deadline` and the repositories. Schema changes only through a new Alembic migration
    (never edit an applied one); UUID keys unchanged.
  - Structured errors from `core/errors.py`; generic messages to clients, details to logs with the request id; no vendor
    text, no raw interview text in logs or traces.
  - Config only from env via `pydantic-settings`; `.env.example` stays in sync (a test enforces it); no hardcoded model
    names; no new dependency without the user's OK.
  - AI change: run the covering evals (same model, >= 2 repeats) and compare with `docs/evals/baselines.md`; write
    `docs/evals/u3c-<change>-vs-baseline.md`. The user runs real-model evals and live tests; Claude gives the commands.
  - Tests mock the LLM (fake chat model); real-model calls stay opt-in.
  - Never commit, push or stage; run `graphify update .` after code changes.

## User Flow
Candidate-facing behavior only changes when the LLM cannot answer.

1. Start an interview: the first question is written by the LLM through the provider chain. If every provider fails, the
   request fails with a retryable error and no interview exists; the candidate starts again.
2. Submit an answer: decide and write run through the chain. A provider that fails before producing any output
   (timeout, rate limit, server error) hands the call to the next provider within the same turn deadline.
3. Streamed answer: text streams from one provider. If it fails after the first text, the client gets `reset` (drop
   the partial text) and then a failed event with a retryable code; nothing is saved and the candidate sends the same
   answer again.
4. A turn whose decide or write is unusable (two invalid replies, the turn deadline ran out, input too long) ends in the
   same retryable error, with nothing saved.

## Requirements

### Functional
- **Chain.** Build one chat model per entry of `LLM_PROVIDERS`, in order, from its `LLM_<VENDOR>_*` block, and try them
  in order inside the call helpers (an explicit loop, decided in the plan: the helpers own the per-attempt timeout,
  retries and tracing, which `.with_fallbacks()` would bypass). A single entry behaves exactly as today.
- **What switches.** Only transport errors (timeout, rate limit, server error, as mapped to `LLMError` types) move a call
  to the next provider. Invalid or rule-breaking replies are not transport errors: they stay in the existing attempt
  loop, which runs through the same chain.
- **Streams.** A stream switches provider only if it fails before its first chunk; after that the error is raised and
  the existing reset + failed-event handling applies. The chain must not multiply attempts beyond the worst case pinned
  in `tests/core/ai/test_retry_budget.py` (updated for the chain, number recorded in the plan).
- **Time.** One turn deadline covers the whole chain. Each provider call keeps its own timeout (`LLM_TIMEOUT_SECONDS`),
  and the next provider gets the time that is left. No time left -> the retryable error.
- **Provider in the trace.** The Langfuse trace and the log line name the provider and model that answered, without
  prompt or answer text. Nothing new is stored in the database for this.
- **Startup.** An empty `LLM_PROVIDERS` refuses to start (as a half-configured vendor already does). The `llm_configured`
  "off" mode, the "LLM disabled" branches in the factory, and the "retrieval off when LLM off" switch are removed.
- **Retryable error.** One structured error from `core/errors.py` (503, stable code, generic message, request id) is used
  for: start failed, a blocking turn failed, and the failed SSE event of a streamed turn.
- **Bank removed.** Delete the bank file and its loader/schema (`BankQuestion`, `QuestionBank`), `select_questions`,
  `pick_fallback_question`, `bank_question`, the `get_bank` dependency and every fallback branch that asks the bank.
  Setup validation at start depends only on the request enums, no longer on the bank.
- **Old data.** A new Alembic migration renames stored `source = bank` rows to `stored`, drops `bank_id`, and updates the
  column default. `QuestionSource` loses `bank` and gains `stored`. History, report and usage code read `stored` rows
  as before (not LLM-written, no usage, no prompt version).
- **Stored-question path stays.** An old session whose questions were stored up front can still be finished without the
  LLM; only the bank file and bank fallbacks go.
- **Old layer deleted.** Remove `LLMProvider`, `openai_compatible.py`, `TracingProvider` and `build_provider`, once
  nothing imports them. `FakeProvider` moves out of `app/` into the test helper `tests/provider_fakes.py` (22 test files
  use it; porting them to `FakeChatModel` is a later cleanup), and `json_reply.py` stays in `app/core/ai/` (the profile
  feature uses it too, so it is shared, not old-layer code). Both amended 2026-11-28 with the user's approval. Keep the `LLMError` family (move or keep in place;
  the plan decides, imports must stay valid). Decide in the plan whether the `Embedder` protocol stays.
- **Layer test.** `tests/test_layers.py` fails if any module outside `app/core/ai/` and feature `ai/` folders imports
  `langchain*` or a vendor SDK. The note parser in `interviews/utils/` no longer imports `ai/interviews_split.py`
  (review nit R3).
- **Eval tooling.** The eval scripts and fixtures that used the old layer or the bank run on the chat model.

### Non-Functional
- Latency: unchanged on the happy path; a failing primary costs at most its own timeout before the next provider.
- Privacy: logs and traces carry ids, counts, codes and provider/model names only.
- Security: the client never sees vendor error text, stack traces or provider names.
- Maintainability: no code path remains that can silently replace an LLM question with a canned one.

## UX Requirements
- Error message for candidates is short, generic and tells them to try again (no vendor, no internals).
- The client can tell the retryable error from other failures by its stable code (HTTP 503 or the failed SSE event).
- Partial streamed text is always discarded with `reset` before the failed event.

## Constraints
- Python 3.14, `uv`, LangChain 1.x; only `google` is a known vendor today (`LLM_VENDORS`).
- No second real vendor is added in U3c (no new dependency): the chain is proven with fake models. Adding a vendor and
  the "provider B scores N/M at X times the cost of A" comparison come in a later slice.
- The `openai` package is used only by the old layer; it is removed in this slice once nothing imports it (approved).
- Applied Alembic migrations are not edited. The `source` column stays.

## Blockers
- None blocking the spec. To verify in the plan's first step (assumption): `.with_fallbacks()` on the real LangChain
  Google chat model switches only before the first chunk on `astream`, and keeps our `LLMError` mapping and
  `after_output` marking intact.
- Name and code of the retryable error is a plan detail (consistent with `core/errors.py`).

## Edge Cases
- **EC1:** First provider times out before any output, second answers -> the second's answer is used; the log and trace
  name the second provider.
- **EC2:** First provider returns a rate-limit or server error -> same as EC1.
- **EC3:** First provider returns an invalid reply (bad JSON, rule-breaking text) -> no provider switch; the existing
  attempt loop retries; after its limit the turn fails with the retryable error, nothing saved.
- **EC3b:** The decide call fails (any reason) -> the turn ends in the retryable error, nothing saved (today a failed
  decide only skips the follow-up; the maintainer chose to fail the turn).
- **EC4:** Every provider fails with transport errors -> retryable error; nothing saved; blocking turn, streamed turn and
  start all use it.
- **EC5:** A stream fails after its first chunk -> no switch; `reset` event then failed event; nothing saved.
- **EC6:** A stream fails before its first chunk on the primary -> the next provider streams the whole question.
- **EC7:** Turn deadline runs out while the first provider is still hanging -> its call times out at the earlier of its
  own timeout and the deadline; with no time left, the retryable error and no further provider is started.
- **EC8:** Input too long for the write call even after trimming -> retryable error, nothing saved (today: the bank asks).
- **EC9:** `LLM_PROVIDERS` empty or blank -> the app refuses to start with a message naming `LLM_PROVIDERS`.
- **EC10:** `LLM_PROVIDERS` lists a vendor with missing settings, an unknown name or a duplicate -> startup refused, as today.
- **EC11:** Only one provider configured and it fails -> same as EC4 (no chain to fall back to).
- **EC12:** Start fails because every provider failed -> 503, and no interview session or question row is created.
- **EC13:** Old session with rows `source = bank` -> after the migration the rows read as `stored`; history, report and the
  stored-question path behave as before; no `bank_id` exists.
- **EC14:** The migration runs on a database with no old rows -> succeeds (no-op data change, schema change applied).
- **EC15:** Job-description summary or retrieval fails at start -> still non-fatal as today (interview starts without
  them); only the first-question write failing blocks the start.
- **EC16:** Retry budget: every provider scripted to fail -> total call attempts never exceed the documented worst case
  for the chain (`tests/core/ai/test_retry_budget.py`).

## Acceptance Criteria
- [x] **AC1:** A test with two fake chat models where the first raises a timeout before any output shows the second
  answering, and the log/trace record the second provider's name and model (EC1, EC2).
- [x] **AC2:** A test with a stream that fails after its first chunk shows no provider switch, a `reset` then a failed
  event, and nothing saved; a stream failing before its first chunk switches (EC5, EC6).
- [x] **AC3:** An invalid reply does not switch providers; the attempt loop handles it and the turn ends in the
  retryable error after its limit (EC3).
- [x] **AC4:** With every provider failing, start, a blocking answer and a streamed answer each return the retryable
  error (stable code, generic message, request id, no vendor text), and no row is created or changed (EC4, EC11, EC12).
- [x] **AC5:** The turn deadline bounds the whole chain: with a scripted slow first provider, the second gets only the
  remaining time, and with none left no further provider is started (EC7).
- [x] **AC6:** `tests/core/ai/test_retry_budget.py` pins the chain's worst-case attempts and passes (EC16).
- [x] **AC7:** An empty or blank `LLM_PROVIDERS` makes `Settings` raise at startup; no `llm_configured` off-mode,
  "LLM disabled" branch or retrieval-off switch remains (`grep` for them is empty) (EC9, EC10).
- [x] **AC8:** No bank code remains: the bank file, `BankQuestion`/`QuestionBank`, `select_questions`,
  `pick_fallback_question`, `bank_question`, `get_bank` and every bank fallback branch are gone; setup validation at start
  works without them.
- [x] **AC9:** A migration renames `bank` rows to `stored`, drops `bank_id`, and sets the new default; it applies and
  downgrades cleanly on a test database, and history/report/usage tests pass with `stored` rows (EC13, EC14).
- [x] **AC10:** `LLMProvider`, `openai_compatible.py`, `TracingProvider` and `build_provider` are gone from `app/`;
  `FakeProvider` exists only as the test helper `tests/provider_fakes.py`; `json_reply.py` stays in `app/core/ai/`;
  the `LLMError` family remains; nothing imports a deleted name (amended 2026-11-28).
- [x] **AC11:** `tests/test_layers.py` fails when a service, controller, route, repository or utils module imports
  `langchain*` or a vendor SDK (demonstrated by a test or a temporary violation), and passes on the repo; the note parser
  no longer imports `ai/interviews_split.py`.
- [x] **AC12:** The write, decide, stream and feedback evals, run by the user (>= 2 repeats, same model), are within the
  noise margin of `docs/evals/baselines.md`; the comparison is written to `docs/evals/u3c-<change>-vs-baseline.md`.
- [x] **AC13:** `uv run pytest` and `ruff check app tests` pass (known baseline failures excepted and recorded); no raw
  interview text, vendor error text or prompt content appears in logs or traces; `.env.example` and the config test list
  every LLM setting; `graphify update .` has run.

## Out of Scope
- Adding a real second vendor (OpenAI-compatible, Cloudflare, ...) and the cost/score comparison of provider B vs A;
  this needs a new dependency and its own slice.
- A second Google model as provider B, circuit breakers, routing by difficulty, health checks.
- Pausing or resuming an interview when the LLM is down (the candidate simply retries).
- Dropping the `source` column, removing the stored-question path for old sessions, or touching old session content.
- Changing prompts, models, retrieval, ingestion, speech (Deepgram) or the retry/backoff policy of a single provider.
- Updating the progress tracker artifact (asked separately).
