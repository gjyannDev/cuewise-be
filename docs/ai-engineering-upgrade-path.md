# AI Engineering Upgrade Path (Cuewise)

The first path (`docs/ai-engineering-learning-path.md`) built the fundamentals by hand: the `LLMProvider` interface, prompts as files, structured output with fallback, SSE streaming, context management, pgvector RAG, Langfuse tracing and evals. This path upgrades that foundation with the tools and frameworks teams use in production, so you learn what each one gives you **and** what it costs, because you already built the version without it.

## The rules for this path

- **Frameworks stay in the AI layers.** LangChain replaces the hand-built `LLMProvider` (U3) and becomes the model abstraction, but it lives only in `app/core/ai/` and the feature `ai/` folders. Routes, controllers, services and repositories stay framework-free: services call the feature's `ai/` functions, as they do today. Speech stays behind `SpeechSynthesizer` / `Transcriber` until U9 moves the real-time path to LiveKit.
- **No upgrade without a number.** Each slice records a baseline before the change and the same measurement after it (eval score, recall@k, latency p50/p95, cost per interview). "It feels better" doesn't count.
- **One owner per concern.** Retries, logging and tracing each have exactly one layer responsible for them. When a slice is done, the new library has replaced the old code. During a migration both may exist, but never inside the same task.
- **Each new dependency is justified in its slice**: what it replaces, what it adds, and its weight. Check that it supports Python 3.14 before adding it.
- **The project rules still apply**: route → controller → service → repository, prompts as data, user text as untrusted data, no PII in logs, mocked LLMs in unit tests and real-model runs opt-in.

## Build order

| # | Slice | Why here |
|---|-------|----------|
| U0 | Baselines | Every later slice compares against these numbers |
| U1 | structlog | Every later slice logs through it |
| U2 | tenacity | Replaces the custom retry code before new vendors arrive |
| U3 | Migrate to LangChain + fallback chain | The base that U4, U6 and U8 build on; also delivers the old Slice 10. Runs as four sub-slices: |
| U3a | ↳ Foundation + first chains | Model factory, error mapping, deadline, callbacks, fake model; JD summary and profile extraction |
| U3b1 | ↳ Interview calls | Write, write-stream (async), decide, feedback; the eval tooling moves with each task |
| U3b2 | ↳ Retrieval | Embeddings, the retriever, the splitter if chunks stay identical |
| U3c | ↳ Fallback chain + remove the old layer | `.with_fallbacks()`, question bank removed, old LLM layer deleted |
| U4 | Prompt templates + Langfuse Prompt Management | Uses LangChain templates; prompts linked to traces |
| U5 | Expand the knowledge corpus | Hybrid RAG can't show a gain on a tiny corpus |
| U6 | Advanced RAG: hybrid, reranking, query rewriting | Needs the U5 corpus and evals |
| U7 | Langfuse evaluators: LLM-as-judge and online evals | The old skipped Slice 7, done with Langfuse |
| U8 | LangGraph turn graph + tool use | Gives LiveKit one clean, streamable turn to call; covers the old Slice 9 |
| U9 | LiveKit real-time interview + ElevenLabs | The biggest change; needs everything above |

**What depends on what:**
- U0 comes before everything: every slice compares against it.
- U1 and U2 are small and standalone; you can swap them.
- U4, U6 and U8 need U3 (LangChain templates, retrievers and models). U9 needs U8.
- Inside U3: U3a → U3b1 → U3b2 → U3c, in that order (U3b2 only needs U3a, but running it after U3b1 keeps each eval comparison to one cause). U4 can start after U3b1 (every prompt is a template); U6 after U3b2 (the retriever exists); U8 waits for U3c (fallbacks in place, old layer gone).
- U6 needs U5 (a corpus big enough to measure on).
- **U5 is content work, not code**: draft notes while you do U1 to U4, so the corpus is ready when U6 starts.
- U7 only needs U0. It comes after U6 in the list, but you can move it earlier if you want a judge to compare U3/U4 changes.

## Slices in detail

### U0: Baselines

**Goal:** Know where you stand before changing anything.

**Get the environment ready first:**
- Postgres with pgvector running (`docker compose up -d`: pgvector 0.8.7 on Postgres 18, host port 5433), `uv run alembic upgrade head`, the corpus ingested (`uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest`), and the `postgres`-marked tests passing with `TEST_POSTGRES_URL` set to a throwaway database.
- A model API key and Langfuse configured, so eval runs are traced and stored as experiments.
- The open first-path work either finished or written down as known gaps: the 8a corpus review, the interview-room backend review, and the unticked slices in the first path's Progress list.

**What you build:**
- Eval runs for the live prompts (`uv run python -m app.modules.interviews.tooling.interviews_evals ...`), each with `--repeat 3` and the same `--model`:
  - `--task write`: interviewer_v4 (the JSON writer)
  - `--task stream`: interviewer_v5, with time to first token
  - `--task decide`: follow_up_decision_v1
  - `--task feedback`: feedback_score_v2 / feedback_write_v1
  - `--task retrieval`, then `--task generation --arms A,B,C,D,E` (arm A runs v5, B and C run v7, D and E run v8)
  - profile extraction: `uv run python -m app.modules.profile.tooling.profile_evals --repeat 3`
- **Routes with no eval of their own** today: the JSON notes and profile writers (v7_json, v8_json) and the job-description summary (v2). Try them through `--prompt` (the ablation flag); whatever can't run goes into the baselines as a known gap, so U3 knows it can't prove those unchanged.
- At least 3 live interviews, then `uv run python -m app.scripts.interview_report --last 3` for p50/p95 turn latency, time to first token and cost, and `uv run python -m app.scripts.usage_report` for tokens per question position.
- **Capture the live-interview numbers before U1.** `interview_report` reads `logs/app.log` in today's text format, so these numbers have to exist before U1 switches the log to JSON.
- **Claude writes the baselines from Langfuse.** Langfuse already stores every eval run with its scores, latency and cost, so you don't copy numbers by hand. Once the runs are done, ask Claude (using the langfuse skill and the keys in `.env`) to fill `docs/evals/baselines.md`. The file holds only what Langfuse can't give you:
  - which run is the official baseline for each eval: eval, Langfuse run name, score, noise margin (the spread across the 3 repeats), notes
  - the live-interview numbers from `interview_report` and `usage_report`, which come from your own log, not Langfuse
  - the cost of one full eval run, so you know what each later re-check costs (U3 alone re-runs the evals after each migration step)
- **Why keep a file at all:** Langfuse plans keep data for a limited time, and this path runs for months. Later slices ask Claude to compare a new run against the row in `baselines.md`, and that row still exists after Langfuse has deleted the original run.

**You learn:**
- that a refactor is only "safe" when the same evals give the same numbers afterwards
- how noisy your evals are between repeats (the margin a later change has to beat)

**Done when:**
- every later slice can point to a baseline row it compares against

### U1: structlog

**Goal:** Real structured logs instead of `event key=value` strings parsed back by `split_fields`.

**What the user sees:** Nothing. You get searchable JSON logs and a cleaner console.

**What you build:**
- **structlog configured in `app/core/logging.py`**: JSON lines to `logs/app.log`, the pretty console renderer in dev. The standard library's `logging` is routed through structlog, so existing `logger.info(...)` calls keep working during the move.
- **Context binding**: `request_id` (replaces `request_id_ctx` and `RequestIdFilter`), and `session` / `user` bound once per request or turn, not passed to every call. Built as one dict per request that the middleware creates, because FastAPI runs sync dependencies and endpoints in worker threads, each with a copy of the context; outside a request it falls back to `structlog.contextvars`.
- **A redaction processor**: masks keys such as `answer`, `resume`, `job_description`, `token`, `password`, `authorization` before any renderer runs. The "no PII in logs" rule becomes code. It matches key names only: a secret inside free text (a library's own message, an exception message) is not scanned.
- **Gradual conversion**: one module at a time to `log.info("llm_call", tokens=..., latency_ms=...)`; delete `split_fields` once nothing uses it.
- **Keep the interview report working**: `interviews_log.py` (behind `app.scripts.interview_report`) parses today's text log with `split_fields`. Teach it to read the JSON lines, and the old text lines in `logs/app.log.1` too, before the format changes.

**You learn:**
- processors as a pipeline (enrich → redact → render)
- why structured logs matter for aggregates (cost per interview, error rates) and not just for reading
- contextvars across `async` code and SSE generators

**Not included:** shipping logs to a hosted service.

**Done when:**
- a test logs an event with a PII key and the output doesn't contain the value
- every line in `logs/app.log` is valid JSON with `request_id`
- the console stays readable in dev
- `interview_report` gives the same numbers for an interview logged before the change and one logged after it

### U2: tenacity

**Goal:** Replace hand-written retry code with a standard library while keeping your rules: backoff with jitter, `Retry-After`, the turn's `Deadline`, and no retry after the first streamed chunk.

**What you build:**
- **Network retries**: `app/core/ai/retry.py` had three hand-written callers: `openai_compatible.py` (`complete` and `stream`, with `retry_delay`, no SDK), `google_embedder.py` (`embed`, its own loop) and `deepgram.py` (`run_with_retries`). All move to one `RetryPolicy` class on tenacity, which each adapter builds in its constructor: `retry_if_exception` for the retryable errors only (`LLMTimeoutError`, `LLMRateLimitError`, `LLMServerError`), `wait_random_exponential` (full jitter) raised to `LLMError.retry_after`, and a sync `call` plus an async `acall`. The policy holds configuration only; every call builds its own tenacity object (adapters serve concurrent requests).
- **A deadline stop**: `stop_after_attempt(n)` combined with a short stop on the adapter's own clock, so a retry never starts when the turn's budget can't fit the coming wait.
- **`before_sleep` logging** through structlog: `retry_wait` before each wait and `retry_giveup` with a reason (`max_attempts`, `deadline`, `not_retryable`), never the payload.
- **Reply retries, kept separate**: the 4 reply loops (decide, write, write stream, feedback turn) re-ask the model after malformed output. Decided: not tenacity (content retries have no backoff, no HTTP errors and are bounded by the turn's time), but one shared attempt iterator, `app/modules/interviews/ai/interviews_reply_attempts.py`, for the loop header; each loop keeps its own body.
- **Know what happens next**: in U3, LLM transport retries move to LangChain's `.with_retry()` (built on tenacity) and the SDKs' own `max_retries`. Tenacity stays for Deepgram (the REST speech flow) and possibly the reply loops. The U2 policy is what U3 copies, so it isn't wasted work.

**You learn:**
- transport retries vs. content retries (a 503 vs. invalid JSON)
- retry budgets: how 3 attempts at each of 3 layers become 27 calls
- why streams can only be retried before the first chunk

**Done when:**
- the existing `test_retry.py`, `test_openai_compatible*.py` and `test_deepgram.py` tests pass against the tenacity version (behavior unchanged)
- a test with a deadline that's almost over shows no new attempt starting
- the custom retry code is deleted

### U3: Migrate to LangChain + provider fallback chain

**Goal:** Replace the hand-built LLM layer (`LLMProvider`, `openai_compatible.py`, `json_reply.py`, `TracingProvider`, `FakeProvider`) with LangChain, one AI task at a time, without changing behavior. LangChain's `BaseChatModel` becomes the provider abstraction, and `.with_fallbacks()` delivers the fallback chain planned as Slice 10.

**What the user sees:** Nothing at first (the evals prove that). After the fallback chain: fewer errors when a provider has an outage.

**Where LangChain may live:** `app/core/ai/` (model factory, error mapping, deadline wrapper, callbacks) and the feature `ai/` folders (`interviews/ai/`, `profile/ai/`: chains, structured output). Routes, controllers, services and repositories never import LangChain; services keep calling the feature's `ai/` functions.

**Scope today:** 33 app files use `LLMProvider` / `LLMResult` / `ChatMessage`, 22 use the `LLMError` types, 20 test files depend on them, and `app/core/ai/` is about 2,000 lines.

**What maps to what:**

| Today | LangChain |
|---|---|
| `LLMProvider`, `openai_compatible.py`, `factory.build_provider` | `init_chat_model` / `ChatGoogleGenerativeAI`; the factory returns a `BaseChatModel` built from config |
| `ChatMessage`, `LLMResult` (usage, finish reason) | `SystemMessage` / `HumanMessage`, `AIMessage.usage_metadata` and `response_metadata` |
| `.md` prompts + `load_prompt` | `ChatPromptTemplate` built from the same `.md` files (U4 moves them to Langfuse) |
| `json_reply.py` + Pydantic checks | `.with_structured_output(Model)` (the attempt loop and safe fallback stay) |
| `TracingProvider` | Langfuse `CallbackHandler`; `Tracer` stays for scores, datasets, experiments and steps |
| `retry.py` / tenacity (U2) | `.with_retry()` for model calls, or keep tenacity; one owner, written down |
| Provider fallback (Slice 10) | `.with_fallbacks([...])` |
| `FakeProvider` | `GenericFakeChatModel` / `FakeListChatModel` |
| `Embedder` / `GoogleEmbedder` | LangChain `Embeddings` (`GoogleGenerativeAIEmbeddings`) |

**How LangChain covers the harder parts** (and the small piece of each that stays yours):
- **Errors: handled inside the chain.** `.with_retry(retry_if_exception_type=..., wait_exponential_jitter=True, stop_after_attempt=n)` (built on tenacity, so U2 carries over) and `.with_fallbacks(exceptions_to_handle=...)` deal with transient vendor errors, and the model's own `timeout` / `max_retries` cover the request itself. **Stays yours:** a thin `to_llm_error()` at the edge of `core/ai/` for errors that escape every retry and fallback, because SSE `error` events, HTTP 503s, retrieval degrade reasons and logs need one vendor-neutral category. Expect the five `LLMError` classes to shrink to the ones callers actually branch on.
- **The turn `Deadline`: model timeouts now, graph state in U8.** U3 uses the per-model `timeout` plus `asyncio.timeout(deadline.remaining())` around each call, since LangChain has no "rest of this turn's budget". In U8 the deadline moves into the LangGraph state and conditional edges decide what to skip when time runs short (for example skip decide and write the next main question), so the time rules become visible in the graph instead of hidden in helpers.
- **`reasoning_effort`: declarative config instead of code.** LangChain doesn't unify it (`ChatOpenAI(reasoning_effort=...)`, the thinking settings on `ChatGoogleGenerativeAI`, ...). Build the model with `init_chat_model(..., configurable_fields=(...))` and set it per call with `.with_config(configurable={...})`; a small vendor → parameter table in config replaces the mapping code. (Alternative: Gemini through `ChatOpenAI` on Google's OpenAI-compatible endpoint, where `reasoning_effort` works as today, at the cost of skipping the native Gemini integration.)
- **Streaming rules: mostly built in.** On a stream, `.with_fallbacks()` only moves to the next model if the error comes before the first chunk; after that it raises. `.with_retry()` doesn't retry streams, and the SDK's `max_retries` retries the request before any token arrives. So "no retry or fallback after the first chunk" comes from LangChain, and the done-when tests prove it instead of trusting it. **Stays yours:** the "reset" on a rejected draft, because that's an interview rule (your check of the text), not plumbing.
- **Knowledge base: LangChain retrievers over your own tables.** LangChain is strong at *composing* retrieval (fusion, multi-query, reranking; see U6), weak at *owning* your schema. So the tables stay Alembic-made with UUIDv7 keys, and SQL stays in `KnowledgeRepository`. On top of it, `interviews/ai/` defines LangChain `BaseRetriever`s that return `Document`s; the service hands them the repository's search functions, so `ai/` never imports the repository. Not used: LangChain vector stores (`PGVector` / `PGVectorStore`); they bring their own engine and connections next to your session and transactions, and your role/level filters and U6's hybrid SQL already fit the repository.
- **Ingestion: LangChain splitters where they fit.** `Document` and `MarkdownHeaderTextSplitter` can replace the section splitter in `interviews_knowledge_utils.py`. **Stays yours:** the note header (roles, levels, source), hash-based change detection and the corpus checks.
- **Speech: LiveKit, not LangChain.** LangChain has no STT/TTS pipeline. In U9, LiveKit Agents' STT/TTS plugins (Deepgram, ElevenLabs) and its fallback adapters take over the real-time path, and LiveKit's LangChain plugin can run the U8 graph as the agent's LLM. Until then, the current speech code stays; after U9 it's only needed for the pause-and-continue fallback flow.

**Split into four sub-slices.** U3 is too big for one spec, so it runs as U3a, U3b1, U3b2 and U3c, each with its own `/feature` → `/create-plan` → `/implement` → `/review-feature` cycle and its own `docs/features/<sub-slice>/` folder. Old and new layers live side by side until U3c, but never inside the same task (rule: one owner per concern). Each migration step is checked against the U0 evals before the next one starts.

**U3a: Foundation + first chains** (steps 1-3; needs U0, U2)
1. **Foundation**: dependencies (check Python 3.14 support), the chat model factory from config, `to_llm_error()`, the deadline wrapper, the Langfuse callback, the fake chat model and a contract test that every model the factory builds passes. Settle who owns LLM retries (`.with_retry()` or tenacity) and how `reasoning_effort` reaches Gemini, and confirm import paths and the streaming retry/fallback behavior in a spike (see "Check first").
2. **Job-description summary**: the simplest task (plain text), the first real chain `prompt | model`.
3. **Profile extraction**: the first `.with_structured_output`.

Done when: the JD summary and profile extraction run on LangChain and match U0 (the JD summary needs its own eval first, see `docs/evals/baselines.md`); a fake model's vendor rate-limit error arrives as your vendor-neutral rate-limit error; an almost-spent deadline cuts the call off; the U2 retry rules hold for the migrated tasks.

**U3b1: Interview calls** (steps 4-6; needs U3a)

Before step 4 (found in the U3b pre-check, 2026-11-27):
- A short `astream` spike: the whole-stream timeout through gRPC (the old layer bounded each read, gRPC takes one deadline for the call), usage and finish reason on the last chunk, how `after_output` gets set, and a real `DeadlineExceeded` (never observed yet).
- A stream-capable fake chat model (scripted chunks, an error before and after the first chunk). `FakeChatModel` only has `_generate`. The shared `llm` fixture in `tests/modules/interviews/conftest.py` (about 35 test files) moves onto it.
- An eval for the first-question JSON writers (`interviewer_v7_json`, `v8_json`), which have no baseline.
- A plan for `Interviewer`, which takes one `LLMProvider` for decide and write: the two layers may not mix inside one task, so the plan says how write, decide and write-stream move without a half-migrated turn.

4. **Write and write-stream**: `complete_chat` for write. `astream()` through an async helper built on `RetryPolicy.acall` (it already exists), which sets `after_output`; SSE events unchanged. The reset on a rejected draft stays yours.
5. **Decide**: `complete_structured` with a model-facing schema whose fields are all required (U3a: a schema with defaults sends no `required` list and the profile scores collapsed while the validity score stayed green), inside the existing attempt loop. `tests/core/ai/test_retry_budget.py` scripts an httpx transport against the old layer, so it is ported to the fake chat model with the same worst-case number.
6. **Feedback**: scoring with structured output (required fields) and writing. The reply parsers (`parse_score_reply`, `parse_write_reply`) stay as a second check, since they hold interview rules (quotes, lengths, template fallback).

With every step, the eval tooling (`interviews_evals.py`, `interviews_feedback_evals.py`) moves to the chat model with its task; until then it still measures the old layer. Run 3 repeats against `baselines.md` (it has 2, taken on a dirty tree, and decide and feedback are coarse: one decide case is 0.07).

Done when: write, write-stream, decide and feedback match U0 within the noise margin; SSE events are unchanged; a stream failing after its first chunk is never retried; the worst-case call budget (`tests/core/ai/test_retry_budget.py`) still holds on the LangChain path.

Result (implemented 2026-11-27, `docs/features/u3b1-interview-calls/`): all four calls run on the chat model, and `get_llm_provider` and the app's `LLMProvider` are gone from the app's wiring (the old classes stay for U3c to delete). Evals against the U3b1 baselines: write and generation no change; decide better (0.933 x 3 vs 0.800 / 0.867, the new decide baseline row); write-stream no change in quality and ~300-600 ms faster to the first token (native Gemini streaming); feedback no change, with Gemini taking the nested score schema. Comparison files: `docs/evals/u3b1-*-vs-baseline.md`. Reviewed (`/review-feature`) and committed.

**U3b2: Retrieval** (step 7; needs U3a, best after U3b1)

7. **Embeddings and retrieval**: spike first. Compare `GoogleGenerativeAIEmbeddings` vectors (`gemini-embedding-001`, 768 dimensions, `RETRIEVAL_QUERY` / `RETRIEVAL_DOCUMENT`, both set per call) with the stored ones. If they match, use it, with its errors mapped (it wraps them as `GoogleGenerativeAIError`, the Google error is `__cause__`) and retries owned by `RetryPolicy`. If not, a thin `Embeddings` adapter over `GoogleEmbedder`, with no re-embedding. Then the vector `BaseRetriever` over `KnowledgeRepository`; the time cap, degrade reasons, similarity floor and ranking merge stay in `RetrievalService`. `MarkdownHeaderTextSplitter` only if it reproduces today's chunks and hashes; it lives in `langchain-text-splitters`, which isn't installed, so it needs a dependency justification, and any chunk difference means re-embedding everything.

Done when: retrieval evals match U0 (recall@5, MRR); stored vectors and the model name are unchanged; the embedder call-count test in `test_retry_budget.py` is ported and still holds.

Result (implemented 2026-11-27, `docs/features/u3b2-retrieval/`): `GoogleGenerativeAIEmbeddings` was not used: it sends no per-call timeout (its `request_options` is never passed) and its Google client retries 503s on its own for up to 60 s, so the time cap and retry budget couldn't hold. Instead `GoogleEmbedder` became a LangChain `Embeddings` itself (same request code, so no spike and no port of the call-count test were needed; it still holds). The vector search runs through a `BaseRetriever` bound to the already-computed vector (`interviews_retrieve.py`), keeping one batched embed call. `MarkdownHeaderTextSplitter` reproduced all 75 chunks and hashes and was adopted (`langchain-text-splitters`, approved), for section text only: it drops empty sections and merges repeated headings, so the ingestion checks keep their own heading scan. Retrieval eval: no change (26 of 26 cases with the same notes, order and scores; recall@5 1.00, MRR 0.909), `docs/evals/u3b2-embeddings-vs-baseline.md`. Reviewed (`/review-feature low`, 2026-11-27): two should-fix findings on the splitter fixed (indented lines and heading-format mismatches are now refused); two nits left open (see the feature's `task.md`).

**U3c: Fallback chain + remove the old layer** (steps 8-9; needs U3b1 and U3b2)

8. **Fallback chain**: reuse the existing `LLM_PROVIDERS` list in `core/config.py` (already ordered, primary first) and its `LLM_<VENDOR>_*` blocks. Build the models in that order with `.with_fallbacks()`; switches happen only before the first streamed chunk, and the trace records which provider answered. **Then remove the question bank**, but only after the spec decides two things. First, what the candidate sees when every provider fails (most likely a clear, retryable error). Second, what replaces today's "`LLM_PROVIDERS` empty = LLM off, bank only" mode for local development and tests (most likely the fake chat model).
9. **Delete the old layer**: `LLMProvider`, `openai_compatible.py`, `json_reply.py`, `TracingProvider`, `FakeProvider`, once nothing imports them. Update `tests/test_layers.py` so only `core/ai` and feature `ai/` folders may import `langchain*`.

Done when: the first provider timing out makes the second answer and the log says which; a stream failing after its first chunk doesn't switch providers; the layer test fails on a LangChain import outside the AI folders; you can say "provider B scores N/M at X times the cost of A".

**You learn:**
- what LangChain's abstraction gives you and what it hides, compared with the layer you built
- Runnables and LCEL: composing `prompt | model | parser`, `.with_retry()`, `.with_fallbacks()`, callbacks
- the strangler pattern: migrating a live system one piece at a time behind evals
- the same prompt behaving differently across vendors

**Not included:** LangChain agents (U8 uses LangGraph), LangChain vector stores, circuit breakers, routing by difficulty.

**Check first:** LangChain moves fast (in 1.x several retrievers and chains moved to `langchain-classic`). Confirm import paths and the streaming fallback/retry behavior above in the U3a step 1 spike, with tests.

**Done when (all of U3, after U3c):**
- every migrated task matches its U0 eval numbers within the noise margin
- a test where a fake model raises a vendor rate-limit error shows it arriving as your vendor-neutral rate-limit error
- a test with an almost-spent deadline shows the call cut off at the deadline
- a test where the first provider times out shows the second answering, and the log says which
- a stream that fails after its first chunk doesn't switch providers
- the layer test fails if a service, controller, route or repository imports LangChain
- you can say "provider B scores N/M at X times the cost of A"

### U4: Prompt templates + Langfuse Prompt Management

**Goal:** Prompts with checked variables, explicit message roles and versions you can see in every trace.

**What you build:**
- **Template contracts**: U3 already builds `ChatPromptTemplate`s from the `.md` files; now each one declares its input variables and a test fails on a missing or extra one. System message from the template, user content only ever as a **variable**.
- **Few-shot examples** as data (`FewShotChatMessagePromptTemplate`) where an eval shows they help.
- **Langfuse Prompt Management**: prompts stored with versions and labels (`production`, `staging`), fetched with a cache and a local-file fallback when Langfuse is down. Each generation is linked to the prompt version that produced it.
- **Migration**: the current `.md` files become the seed versions; `interviews_prompt_registry.py` points to Langfuse names and labels, and its `live` / `archived` statuses map to Langfuse labels.
- **One source of truth**: decide in the spec whether the repo files or Langfuse own the text. Recommended: the repo files are the source (reviewed in git); a sync script pushes them to Langfuse, the app reads Langfuse with the files as fallback, and a test fails if the two differ.
- **Guard the `production` label**: changing it changes what every interview sends, with no deploy. Until U7's regression gate exists, promote a version only after running its evals by hand; after U7, the gate decides.

**You learn:**
- templates as contracts (inputs validated before the call)
- prompt deployment without a code deploy, and why that needs evals as a gate
- template injection: never build the template itself from user text; avoid Jinja on anything user-controlled

**Done when:**
- a test fails when a template variable is missing
- a trace in Langfuse shows the prompt name and version
- the app still starts and answers with Langfuse unreachable (local fallback)
- the interviewer evals match U0 after the migration

### U5: Expand the knowledge corpus

**Goal:** Enough reference notes that retrieval has real choices to make, across the roles and levels interviews actually use.

**What the user sees:** Better-grounded questions for more roles and topics.

**What you build:**
- **A coverage map**: roles × levels × topics, with which cells have notes today (21 notes now). The gaps decide what to write.
- **New notes** that follow `note-guide.md` and `note-template.md` and pass the ingest checks (header, sections, hidden-character check, `source_share_problem`).
- **A drafting decision**: hand-written, or LLM-drafted and reviewed by you. If drafted, add a review checklist (facts checked, level-appropriate, no copied text) so a wrong fact doesn't become "ground truth" for the interviewer.
- **More retrieval eval cases**: a few new cases in `retrieval_eval_cases.json` for every new topic, including hard ones (similar topics, wrong role, wrong level).
- **Corpus stats** in the ingest output: notes and chunks per role and level, average chunk length.

**You learn:**
- that data quality limits RAG more than retrieval tricks do
- coverage analysis and building an eval set alongside the data
- the trade-offs of synthetic data

**Done when:**
- the coverage map has no empty cell for the target roles and levels
- retrieval evals run on the larger set, and recall@k is recorded as the U6 baseline

### U6: Advanced RAG

**Goal:** Go beyond naive vector top-k, one technique at a time, each kept only if the retrieval evals say it helps.

**What you build (in this order, measuring after each):**
1. **Hybrid search**: Postgres full-text search (`tsvector` column + GIN index, through an Alembic migration) next to pgvector, as a second `BaseRetriever` over `KnowledgeRepository`, fused with the vector retriever by `EnsembleRetriever` (weighted **Reciprocal Rank Fusion, RRF**). Keyword search catches exact terms (tool names, acronyms) that embeddings blur. Use Postgres for the keyword side, not the in-memory `BM25Retriever`, which would rebuild a second index outside the DB.
2. **Reranking**: take the top ~20 from hybrid and rerank with `ContextualCompressionRetriever` plus a reranker. Choose the reranker in the spec, because each option has a cost:
   - a local cross-encoder: a heavy dependency (`sentence-transformers` / PyTorch) and CPU latency
   - a hosted reranker: a new vendor that receives the job description and profile
   - an LLM reranker: one more model call

   Measure the quality gain against the added latency. Retrieval runs **once, at interview start** (`interviews_service.py`), so the budget is `RETRIEVAL_TIME_CAP_SECONDS`, not a turn's deadline.
3. **Query rewriting**: `MultiQueryRetriever` (or HyDE) turns the job description and profile into focused queries, with the rewrite prompt as data and the job description as untrusted input.
4. **Optional, if the evals show a need**: contextual chunk headers or a better chunking strategy.

Each step stays a separate, testable retriever or function: query building → retrieve (vector, keyword) → fuse → rerank → filter. Composing them from LangChain parts means a stage can be switched off by config without touching the others.

**You learn:**
- lexical vs. semantic retrieval and why fusing them works
- RRF vs. weighted score fusion
- the latency cost of each stage, and that every extra stage needs a time cap and a fallback
- retrieval metrics: recall@k, MRR, nDCG

**Not included:** a separate vector database, GraphRAG, agentic retrieval (U8 adds a `search_notes` tool).

**Done when:**
- a table shows recall@k / MRR for vector-only vs. hybrid vs. hybrid + rerank vs. + rewriting, on the U5 eval set
- every stage that didn't improve the numbers is removed or switched off by config, and the reason is written down
- retrieval still finishes within `RETRIEVAL_TIME_CAP_SECONDS`, or falls back to the previous stage

### U7: Langfuse evaluators

**Goal:** Automated quality scores you can trust, offline on datasets and online on live traces.

**What you build:**
- **LLM-as-judge evaluators** for the interviewer and feedback (relevance, level fit, follow-up quality, rubric adherence), with the judge prompt as data and structured scores validated with Pydantic.
- **Calibration**: grade a sample by hand (Langfuse annotation queues), compare with the judge, and only rely on the judge once agreement is measured and acceptable.
- **Offline**: judge evaluators added to the existing `run_experiment` datasets, so a prompt or model change shows a score diff.
- **Online**: evaluators scoring a sample of live traces. Decide what is sent to the judge model (sampling, redaction), since interview answers are personal data.
- **A regression gate**: a script that fails when a run scores below the baseline by more than the noise margin.

**You learn:**
- judge bias (position, length, self-preference) and how calibration exposes it
- offline vs. online evaluation
- evaluation as a deploy gate

**Done when:**
- you can state the judge's agreement with your grades as a number
- a deliberately worse prompt fails the regression gate
- live traces in Langfuse carry judge scores, without raw answers going anywhere they shouldn't

### U8: LangGraph turn graph + tool use

**Goal:** The interview turn as an explicit state graph, then a bounded tool loop inside it, with the code still deciding what's allowed.

**What you build:**
- **Turn graph**: nodes for decide → write → settle (retrieval stays at interview start, and its notes are part of the state), with conditional edges (follow-up vs. next main question, the follow-up cap, last question). State is a typed object rebuilt from Postgres on each request. **Postgres stays the source of truth**; no LangGraph checkpointer for the session unless the spec gives a reason.
- **Streaming**: the graph streams tokens and progress events, and the existing SSE route and the U9 agent both consume it.
- **The deadline in the graph**: the turn's `Deadline` lives in the graph state, and conditional edges route around slow steps when time runs short (for example skip decide and write the next main question), replacing the U3 `asyncio.timeout` helpers.
- **Same rules**: one atomic save, and a client that disconnects saves nothing.
- **Tool use (old Slice 9)**: read-only tools such as `search_notes(role, level, topic)` (the first time retrieval can happen per turn, reusing the U6 retrievers) and `get_rubric(criterion)` with Pydantic argument schemas, an allowlist, a cap on calls per turn, a timeout per tool, everything scoped to the session and user, and tool results treated as untrusted.
- **A comparison**: the tool-using graph vs. the fixed pipeline, on cost, latency and quality.

**You learn:**
- state machines vs. agents, and when to use which
- conditional edges, reducers, streaming modes
- indirect prompt injection through tool results

**Not included:** write tools, multi-agent setups, long-running autonomy.

**Done when:**
- the U0 interviewer evals match on the graph version (no behavior change before tools)
- a fake model that asks for tools forever still ends the turn at the limit
- a tool result containing an instruction doesn't change behavior
- you can say with numbers whether tools beat the fixed pipeline

### U9: LiveKit real-time interview + ElevenLabs

**Goal:** A real conversation instead of record → upload → wait → listen. The candidate speaks, the interviewer answers within about a second, and either side can interrupt.

**What the user sees:** A live voice interview that feels like a call.

**Decide in the spec first:**
- **LiveKit Cloud or self-hosted** LiveKit server (Cloud is simpler to start; self-hosting is more DevOps to learn), with its URL and keys from config.
- **Where the agent lives**: an entry point in this repo (it reuses the services and models), or its own service.
- **The client side**: the Next.js app needs the LiveKit client SDK, a room UI and microphone handling. That's its own frontend plan.
- **Privacy**: live audio now streams to the STT vendor and text to the TTS vendor for the whole call. Check what each vendor keeps.

**What you build:**
- **A spike first**: a minimal LiveKit agent with streaming Deepgram STT, your LLM and ElevenLabs TTS, measuring end-to-end latency before touching the real pipeline.
- **An agent worker** (a separate process, e.g. `agent/` or its own service) that joins the interview's room and runs the U8 turn graph as its LLM (through LiveKit's LangChain plugin, or a thin custom LLM node if the plugin doesn't fit the graph's events). It keeps to the layer rules: the agent is a new entry point like a route, and it talks to services.
- **Speech through LiveKit plugins**: Deepgram STT and ElevenLabs TTS as LiveKit plugins, with LiveKit's fallback adapters for vendor outages. These replace the REST speech adapters on the real-time path.
- **Token issuing in FastAPI**: an authenticated route that checks session ownership and returns a short-lived LiveKit access token for that room only.
- **Turn-taking**: voice activity detection plus LiveKit's end-of-turn model, tuned for interviews (candidates pause to think, so don't cut them off).
- **Interruptions (barge-in)**: the candidate speaks over the interviewer → TTS stops, and the partial interviewer text is recorded as such.
- **ElevenLabs** as the TTS plugin (key, voice and model from config), compared with Deepgram Aura on latency, cost per character and voice quality.
- **Persistence**: transcripts and turns saved through the same services as today, so feedback and reports keep working.
- **Observability**: per-turn latency broken down (STT final → first LLM token → first audio byte), plus cost per minute.
- **Fallback**: the current pause-and-continue voice flow stays available when LiveKit or a vendor is down.

**You learn:**
- real-time voice architecture: WebRTC, rooms, agent workers
- streaming end to end and latency budgets
- turn detection and interruption handling
- cost per conversation minute across STT, LLM and TTS

**Not included:** phone calls (SIP), video, multiple candidates in a room.

**Done when:**
- a live interview runs start to finish in real time and is saved like a normal one
- p50 time from the end of the candidate's speech to the first interviewer audio is measured and written down
- interrupting the interviewer stops its speech
- a user can't join another user's room (token tests)
- the old voice flow still works as the fallback

## How to make it stick

Same habit as the first path: each slice gets `docs/features/<slice>/` with `spec.md`, `plan.md`, `task.md` and `learnings.md`, and its learnings record the before/after numbers, not just what was built.

## Progress

- [ ] U0: Baselines
- [ ] U1: structlog
- [ ] U2: tenacity
- [ ] U3: Migrate to LangChain + provider fallback chain
  - [x] U3a: Foundation + first chains (JD summary, profile extraction)
  - [x] U3b1: Interview calls (write/stream, decide, feedback) - implemented 2026-11-27, reviewed
  - [x] U3b2: Retrieval (embeddings, retriever, splitter) - implemented 2026-11-27, reviewed (low)
  - [ ] U3c: Fallback chain + remove the old layer
- [ ] U4: Prompt templates + Langfuse Prompt Management
- [ ] U5: Expand the knowledge corpus
- [ ] U6: Advanced RAG (hybrid → rerank → query rewriting)
- [ ] U7: Langfuse evaluators (LLM-as-judge, online evals, regression gate)
- [ ] U8: LangGraph turn graph + tool use
- [ ] U9: LiveKit real-time interview + ElevenLabs
