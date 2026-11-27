# Feature: U3b1 Interview calls on LangChain

## Problem
The interview's LLM calls (write, streamed write, decide, and feedback scoring and writing) still run on the hand-built `LLMProvider` layer (`app/core/ai/provider.py`, `openai_compatible.py`, `tracing.py`, `fake.py`), while U3a built the LangChain call layer (`app/core/ai/chat.py`) beside it and moved only the job-description summary and profile extraction. Four things follow:
- U3c can't delete the old layer while these calls still use it.
- The streaming path has no LangChain version: U3a's helpers (`complete_chat`, `complete_structured`) are synchronous.
- The eval tooling for these tasks (`interviews_evals.py`, `interviews_feedback_evals.py`, `interviews_rag_evals.py`) still calls `LLMProvider`, so a baseline comparison would measure the old code, not the migration.
- The shared `llm` test fixture (`tests/modules/interviews/conftest.py`, about 35 test files) is built around `FakeProvider`, which routes calls by their system prompt.

U3b1 is the second of the four U3 sub-slices (U3a, U3b1, U3b2, U3c; see `docs/ai-engineering-upgrade-path.md`). The learner is the developer, building Cuewise as an AI-engineering project.

## Goal
- Write, write-stream, decide, and feedback scoring and writing run on the U3a LangChain call layer (plus an async stream path), and no production code outside `core/ai/` calls `LLMProvider`.
- The candidate notices nothing: same SSE events, same fallbacks, same log lines, same worst-case call budget.
- Each task, after its stage, scores within the noise margin of a fresh 3-repeat baseline on the same model (`gemini-3.5-flash-lite`), compared in Langfuse.
- Learning goal: `astream()` and the streaming retry/fallback rules, structured output on harder tasks, and why a lenient second check still earns its place (the U3a profile lesson).

## Project Conventions
- Rule files consulted: `CLAUDE.md` (repo root); there is no `.claude/rules/`. Also `docs/ai-engineering-upgrade-path.md` (U3, U3b1) and `docs/features/u3a-langchain-foundation/learnings.md`, `docs/evals/baselines.md`.
- Constraints those rules impose:
  - LangChain is imported only in `app/core/ai/` and the feature `ai/` folders. Routes, controllers, services and repositories never import LangChain or a vendor SDK (`tests/test_layers.py`).
  - Vendor exceptions are mapped to `LLMError` types before they leave `core/ai/`; models and keys come from config; no hardcoded model names.
  - Prompts stay as versioned `.md` files (registry: `interviews_prompt_registry.py`); this slice changes none.
  - Validate every LLM output with Pydantic and a safe fallback; handle malformed or empty replies with retries.
  - Interview answers and résumés are personal data: no raw content in logs; user text is untrusted and stays apart from instructions.
  - Tests mock the LLM; the user runs real-model evals (same model, at least 2 repeats; this slice asks for 3), Claude compares them in Langfuse and writes one `docs/evals/u3b1-<task>-vs-baseline.md` per stage (CLAUDE.md "Compare AI changes against the baseline"); `learnings.md` links to them.
  - Old and new layers may coexist between stages, never inside one task.
  - No new dependency without a justification (none is expected here).
  - Never commit, push or stage.
- Code findings that frame this slice (from the pre-spec check, 2026-11-27):
  - `Interviewer` (`interviews_turn.py`) takes one `LLMProvider` and uses it for decide, write and stream. `answer_turn` is synchronous; `stream_turn` is async and runs decide in a worker thread (`anyio.to_thread`), then streams the write.
  - Write, decide and the feedback generator each have their own reply loop built on `ReplyAttempts` (at most two attempts, only for a reply that came back but broke the contract); the call layer retries transport errors. The stream loop also retries after text was shown (`LLMError.after_output`), sending a `Reset` first.
  - Live prompts: blocking write (`interviewer_turn`) sends `interviewer_v4`, `v7_json` (notes) or `v8_json` (profile); streamed write (`interviewer_stream`) sends `v5`, `v7` or `v8`; decide sends `follow_up_decision_v1`; feedback sends `feedback_score_v2` and `feedback_write_v1`. `v7_json` and `v8_json` have no eval baseline.
  - `RetryPolicy.acall` already exists in `core/ai/retry.py` (the old stream uses it); `FakeChatModel` implements only `_generate`, with no streaming.
  - Feedback also writes Langfuse steps and checks through `Tracer.step` / `Tracer.check`; the generations nest inside them today.
  - `tests/core/ai/test_retry_budget.py` scripts an httpx transport against the old layer to pin the worst-case call count.
  - Baselines (`docs/evals/baselines.md`, 2 repeats, commit `e12941b`, dirty tree): write 19 items 1.00/1.00 noise 0; stream 19 items 1.00/1.00 noise 0; decide 15 items accuracy 0.80/0.80 noise 0 (one case is 0.07); feedback 10 items pass rate 1.00/0.90 noise 0.10; generation arms A 0.800/0.775, B 0.867/0.442 (noise 0.43), C 0.700/0.700, D 0.558/0.483, E 0.550 (one repeat).

## User Flow
Nothing changes for the candidate.

1. The candidate starts an interview: the first question is written (blocking write), or a bank question is used if the LLM is off or fails.
2. The candidate answers: decide picks follow-up or next question, then the next question is written, streamed to the client token by token on the streaming endpoint, or returned whole on the blocking one.
3. When the interview ends, feedback is scored and written; if the written text fails, the template text is used.

For the developer, per stage (write, decide, write-stream, feedback):
1. Run the unit tests with the fake chat model.
2. Run the task's eval (3 repeats) on the migrated code; Claude compares it with the fresh baseline in Langfuse and writes the comparison file.
3. Move to the next stage only when the comparison says "no change" (or the one-case rule below applies).

## Requirements

### Functional
- **FR1: stream spike.** Before write-stream is built, a short spike with tests on `astream` of the Gemini chat model records: whether the call's `timeout` bounds the whole stream or each read; usage and finish reason on the last chunk; how a failure before the first chunk and after it surfaces; what a real timeout looks like (`DeadlineExceeded`, never observed against the live endpoint yet). If the spike shows a rule we need can't be kept (usage and finish reason at the end, flagging a failure after the first chunk, the no-whole-stream-cap rule), work on write-stream stops and the decision is revisited before building on it; write and decide stages are not blocked by it.
- **FR2: stream-capable fake chat model.** The fake chat model supports streaming with scripted chunks, an error before the first chunk and an error after some chunks, in addition to what it does today (set replies, structured replies, mapped errors).
- **FR3: the shared `llm` test fixture runs on the fake chat model**, routing each call to the right script by task, so the interview tests keep their current style (`llm.script(...)`, `script_decide`, `script_score`, `script_write`). Behavior tests keep their assertions; tests that script the old layer's internals are rewritten, and the plan lists each rewrite.
- **FR4: fresh baselines.** Before write moves, the user re-runs `--task write`, `stream`, `decide` and `feedback` on the current clean tree (still on the old layer for these tasks) with 3 repeats; Claude records the rows in `docs/evals/baselines.md` as the U3b1 baseline. A new eval covers the JSON writers `interviewer_v7_json` and `v8_json` (the blocking first question with notes or a profile), with its own baseline run on the old layer.
- **FR5: write on LangChain.** The blocking write (first question and the non-streaming answer route) sends the same built messages through `complete_chat`. The reply loop (`ReplyAttempts`, `parse_interviewer_reply`, the earlier-question repeat check, `note_dropped`) and its fallback (a bank question) are unchanged.
- **FR6: decide on LangChain with structured output.** The model gets a schema in which every field is required (nullable where "none" is a valid answer), through `complete_structured`. The existing `parse_decision_reply` still runs on the reply text as a second check, so the note and gap rules keep their one home. A reply that fails the schema or the parser counts as an invalid reply and uses the existing loop (decide cap `DECIDE_MAX_SECONDS`, write reserve `WRITE_RESERVE_SECONDS`, at most two attempts); any failure ends in "next question, no note", as today.
- **FR7: write-stream on LangChain.** The streamed write uses `astream()` through an async helper in `core/ai/` that follows the same rules as the sync helpers: the turn's time budget, transport retries only before the first chunk (through `RetryPolicy.acall`), vendor errors mapped to `LLMError`, one Langfuse generation per call, and failures after output flagged with `after_output`. A stream has no whole-stream cap below the turn deadline: the per-attempt `LLM_TIMEOUT_SECONDS` applies to getting the first chunk. The write loop's rules stay: a failed or rejected draft is taken back with `Reset` and retried within the deadline; a bad CATEGORY line before any text is an invalid reply.
- **FR8: feedback on LangChain.** Scoring uses `complete_structured` with a required-fields schema and the existing `parse_score_reply` as second check (quote checks, caps, truncation via the token cap), temperature from `score_temperature` as today. Feedback writing uses `complete_chat` and `parse_write_reply`. Attempt limits, `retry_skipped:no_time`, the template fallback for writing, the "feedback fails rather than show partial scores" rule for scoring and the Tracer steps and checks are unchanged.
- **FR9: wiring.** `Interviewer`, the answer service, the interviews service and the feedback service take the chat model (`ChatModel`) instead of `LLMProvider`; `get_llm_provider`, the `llm` parameters and the `llm_provider` startup wiring are removed from services, dependencies and the app. The old classes (`LLMProvider`, `OpenAICompatibleProvider`, `TracingProvider`, `FakeProvider`, `json_reply.py`) stay in the repo, unused by production code, until U3c deletes them. With the LLM off (no chat model) every task falls back as it does today.
- **FR10: tracing and logging parity.** Generations carry the same labels as today (`task`, `prompt_version`, `attempt`, `budget_left_ms`), token usage and latency; the log lines (`ok`, `invalid_reply:*`, `empty_reply`, `context_too_large`, `cancelled`, `retry_wait`, `retry_giveup`) and the feedback summary line keep their text and fields; no answer or résumé text reaches logs.
- **FR11: eval tooling moves with each task.** `--task write`, `stream`, `decide`, `feedback`, `generation` and the new v7_json/v8_json eval call the same `ai/` functions the app uses, on the chat model, so an eval measures the LangChain path.
- **FR12: worst-case call budget.** `tests/core/ai/test_retry_budget.py` is ported to the fake chat model (decide case; the embedder case stays) and pins the same worst-case number as today.
- **FR13: staged cut-over.** Order: write, decide, write-stream, feedback. Each stage leaves the full suite green and the app working with the tasks of the other stages on whichever layer they have; no task is ever on both layers.

### Non-Functional
- **Latency and cost:** each task at least as fast and as cheap as its fresh baseline within the noise margin; token usage is logged per call as today. Stream time to first token is compared with the baseline (about 2.6 s).
- **Match rule:** a score matches its baseline if it is within the baseline's noise margin, or within one eval case (decide: 0.07 of 15); a one-case drop triggers one extra run before it is called a regression; anything larger is a regression to fix before the next stage. Generation arms A, C and D are judged; B (noise 0.43) and E (one repeat) are reported, never called regressions.
- **Privacy and security:** unchanged. User text goes in only as message content built by the context manager; no raw answers or résumés in logs; keys only from config.
- **Dependencies:** none expected; any addition is justified in the plan.

## UX Requirements
- No visible change. Status codes, error messages, SSE event names and order (`PhaseChanged`, `ActionKnown`, `question.delta`, `reset`, `Settled`), and the bank and template fallbacks stay exactly as today.

## Constraints
- Python 3.14, `uv`. The blocking tasks stay synchronous; only the streamed write is async.
- The user runs all real-model evals; Claude doesn't launch them. Same model as the baselines: `gemini-3.5-flash-lite`; `LLM_TIMEOUT_SECONDS=15` stays in `.env`.
- Prompt text and versions don't change.
- Embeddings, retrieval and the splitter are U3b2; the fallback chain and deleting the old classes are U3c.
- Nothing is committed by Claude.

## Blockers
- **Stream spike results** (assumptions to verify): `astream` reports usage and finish reason on the last chunk; a failure after the first chunk can be told apart from one before it; the per-call timeout doesn't cut a long stream (FR1, FR7). If any fails, write-stream stops and is re-decided.
- **Real gRPC timeout** (assumption to verify): a timeout arrives as `DeadlineExceeded` and maps to `LLMTimeoutError`; it has only been covered by fake-error tests so far.
- **Gemini accepts the decide and score schemas** (assumption to verify): the score schema is nested (questions, criteria, evidence); the native JSON-schema mode must take it, and the eval must show content scores holding (the validity score alone missed the U3a profile regression).
- **Generations nest inside feedback steps** (assumption to verify): with the chat-model callback, generations still appear under `feedback_score` / `feedback_write` steps in Langfuse.
- **Baseline runs by the user** before write moves (FR4), and one run per stage afterwards.

## Edge Cases
- **EC1:** LLM off (`LLM_PROVIDERS` empty, no chat model) -> every task falls back as today: bank question for write, "next question" for decide, feedback unavailable as today; no call, no trace.
- **EC2:** a write, decide or feedback reply is empty, breaks the schema or the parser, or was cut off by the token cap -> an invalid reply: the existing loop makes at most two attempts, then the task's existing fallback (write: bank question; decide: next question with no note; feedback score: feedback fails; feedback write: template text).
- **EC3:** a transport error escapes the call layer's retries -> no further attempt; the same fallback as EC2; the log names the `LLMError` class, never the message.
- **EC4:** a stream fails before any text -> retried by the call layer within the budget; if it still fails, the same fallback as EC3, and no `Reset` is sent (nothing was shown).
- **EC5:** a stream fails after some text was shown -> a `Reset` event, then the whole draft is retried within the turn deadline; if the retry fails or time runs out, the bank question is used.
- **EC6:** the stream's CATEGORY line is missing or broken -> an invalid reply before any text was shown: retried by the write loop, no `Reset`.
- **EC7:** a question is still streaming after `LLM_TIMEOUT_SECONDS` but within the turn deadline -> it keeps streaming (no whole-stream cap); only the turn deadline stops it, as a timeout after output (EC5 rules).
- **EC8:** the client leaves mid-stream -> the call is cancelled, no more tokens are generated, the log says `cancelled`, and the turn is not settled, as today.
- **EC9:** the client leaves during decide -> decide finishes in its worker thread and its result is dropped, as today.
- **EC10:** the turn has no time left for a call (deadline spent, or less than the write reserve for decide) -> no call is sent; `retry_skipped:no_time` for a due feedback retry; the same fallbacks.
- **EC11:** a vendor rate-limit error with Retry-After -> `LLMRateLimitError` carrying it; no retry waits less than it, and none starts past the budget (as in U3a).
- **EC12:** the model reports no token usage -> the call succeeds; usage is logged as unknown, as today (a stream whose last chunk has none included).
- **EC13:** the context is too large even trimmed -> `context_too_large` logged and the fallback used, with no call, as today.
- **EC14:** a schema-valid decide reply that the parser rejects (for example a bad note) -> an invalid reply (EC2); a note that is only dropped by the parser is dropped and logged as `note_dropped`, as today.
- **EC15:** Langfuse is unreachable or off -> calls run and return as today; tracing failures never fail a turn.
- **EC16:** a stage's eval shows a one-case drop -> one extra run before it counts as a regression (match rule); a larger drop blocks the next stage.
- **EC17:** a test depends on an old-layer internal (httpx transport script, `FakeProvider` call record) -> it is rewritten for the fake chat model; its behavior assertion is kept.

## Acceptance Criteria
- [ ] **AC1:** The stream spike's findings are recorded in `learnings.md` with tests, covering FR1's questions; if one of its conditions fails, write-stream is not built and the decision is recorded.
- [ ] **AC2:** The fake chat model streams scripted chunks and raises an error before and after the first chunk; the contract test covers streaming for every model the factory can build (fake included).
- [ ] **AC3:** The `llm` fixture runs on the fake chat model; the interview, answer, stream, feedback and profile tests pass with their behavior assertions unchanged, and the plan lists every rewritten test (EC17).
- [ ] **AC4:** Fresh 3-repeat baseline rows for write, stream, decide and feedback, and the v7_json/v8_json eval with its old-layer baseline, are in `docs/evals/baselines.md` before write moves.
- [ ] **AC5:** Write runs through `complete_chat`; unit tests with the fake chat model cover EC1-EC3, EC10, EC13 and the repeat-question check for the first question and the blocking answer route.
- [ ] **AC6:** Decide runs through `complete_structured` with a required-fields schema plus `parse_decision_reply`; tests cover EC2, EC3, EC10 and EC14, and show it never retries past `DECIDE_MAX_SECONDS`.
- [ ] **AC7:** Write-stream runs through the async helper on `astream()`; tests with the streaming fake cover EC4-EC8, EC10 and EC12, and the SSE events, their order and the existing stream tests (`test_answer_stream.py`, `test_stream_turn.py`, `test_stream_answer.py`) pass with their assertions unchanged.
- [ ] **AC8:** Feedback scoring runs through `complete_structured` plus `parse_score_reply`, and feedback writing through `complete_chat`; tests cover EC2, EC3, EC10, the `retry_skipped:no_time` outcome and the template fallback.
- [ ] **AC9:** `test_retry_budget.py` runs against the fake chat model and pins the same worst-case call count for the decide case as before the migration.
- [ ] **AC10:** Tests show generations carry `task`, `prompt_version`, `attempt` and `budget_left_ms`, usage and latency, that feedback generations nest in their steps, and that log lines and the feedback summary keep their text; no answer or résumé text appears in a log (EC15).
- [ ] **AC11:** No module outside `core/ai/` references `LLMProvider`, `get_llm_provider` or `llm_provider` wiring; `tests/test_layers.py` still passes and still fails on a LangChain import outside `core/ai/` and the feature `ai/` folders.
- [ ] **AC12:** All eval tooling for write, stream, decide, feedback and generation runs on the chat model through the same `ai/` functions as the app.
- [ ] **AC13:** Per stage, the user-run evals (3 repeats, `gemini-3.5-flash-lite`) match the baseline under the match rule; each comparison is written to `docs/evals/u3b1-<task>-vs-baseline.md` (write, decide, stream, feedback, plus generation and v7/v8_json with write) with the Langfuse run names, each repeat's score, the baseline, the noise margin and the verdict, and `learnings.md` links to them.
- [ ] **AC14:** `uv run pytest -q` and `uv run --with ruff ruff check app tests` pass after every stage; `graphify update .` has been run.
- [ ] **AC15:** `learnings.md` records the spike results, what structured output did on decide and score (against the plain-text baseline), what the second check caught or didn't, how the stream behaves compared with the old layer, and the before/after numbers.

## Out of Scope
- **Embeddings, the retriever and the splitter:** U3b2.
- **Provider fallback chain, removing the question bank, and deleting `LLMProvider` and the old classes:** U3c.
- **Prompt text or version changes, prompt templates, Langfuse Prompt Management:** U4 (changing prompts here would give a score move two causes).
- **Making the blocking tasks async:** only the streamed write needs async.
- **Speech (Deepgram) and the LLM_PROVIDERS list or `reasoning_effort` settings:** unchanged.
- **Retiring the lenient parsers:** kept as a second check; revisit after the eval shows what they catch.
