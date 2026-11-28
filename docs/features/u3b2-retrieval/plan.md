# Implementation Plan: U3b2 — Retrieval on LangChain

## Overview
Move query embedding and vector search onto LangChain classes (`Embeddings`, `BaseRetriever`) behind the interfaces the
service already uses, so results, outcomes and the retry budget stay identical (spec: `spec.md`).

## Architecture & Design
**Revised 2026-11-27 (deviation, user-approved):** `GoogleEmbedder` itself becomes a LangChain `Embeddings` (it gains
`embed_documents` / `embed_query`, each one `RetryPolicy`-run call over the same httpx request). It keeps the `Embedder`
interface, so the service, ingestion, factory and evals are unchanged and the vectors are identical by construction.
Reason: `GoogleGenerativeAIEmbeddings.embed_documents` sends no timeout (`request_options` is never used; the Google
client's fixed 60 s default applies) and keeps the Google client's own 503 retry (60 s deadline), so the time cap and
the retry budget (AC5, EC2, EC12) can't hold through it. The original wrapper design is kept below, struck by this note.

~~A new `core/ai` class, `LangChainEmbedder`, satisfies the existing `Embedder` interface by wrapping a LangChain
`Embeddings` (the Google class, or a thin adapter over `GoogleEmbedder` if the spike says no). It owns retries
(`RetryPolicy`), error mapping (`to_llm_error`), the time budget and the vector-size check, and returns the same
`EmbeddingResult`. A new factory function builds it for retrieval and the evals only; ingestion keeps `GoogleEmbedder`.~~
In the interviews `ai/` folder a small `BaseRetriever` is bound to the vector the service already computed (one batched
call for both queries) and to the search function the service passes in (backed by `nearest_chunks`). The service keeps
the time cap, degrade reasons, similarity floor, merge and filter fallback.

## Approaches Considered
Spec settled the scope (embeddings spike, retriever over the repository, splitter only if identical). Design choices the
spec left open were settled with the user:

| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. `Embedder`-shaped wrapper class in `core/ai`, retrieval only | Service/evals barely change; ingestion untouched; old and new never mix in one task | **Yes** — keeps the layer rule (service never sees LangChain) and the smallest diff |
| B. Service calls `Embeddings` directly | Service imports/handles a LangChain type; bigger diff | No — breaks the layer rule |
| C. Retriever bound to the computed vector | Smallest; keeps one batched embed call | **Yes** — spec AC6, ponytail |
| D. Retriever + lookup `Embeddings` (standard shape) | One extra class today; useful for U6 | No — add it in U6 if needed |
| E. Splitter via `uv run --with` first | No `pyproject.toml` change unless adopted | **Yes** — dependency only on adoption, with the user's OK |
| F. `GoogleGenerativeAIEmbeddings` (A's first option) | No per-call timeout; its client retries 503 on its own for 60 s | No (2026-11-27) — breaks the cap and budget |
| G. `GoogleEmbedder` subclasses `Embeddings` | ~10 lines; shared with ingestion; no new factory, eval wiring or test port; no spike needed | **Yes** (2026-11-27, replaces A) |

## Spec Requirements -> Implementation
- Spike, match rule (AC1, EC1) -> Step 2; decision recorded in `learnings.md` (Step 9)
- Embeddings via LangChain, errors/retries/size/budget (AC2, AC5, EC2-EC5, EC12) -> Steps 1, 3, 7
- Retriever, layer rule (AC3) -> Steps 4, 5
- Service behavior unchanged, one batched call (AC4, AC6, EC6-EC10) -> Step 5
- Evals through the new path (AC7) -> Steps 6, 9
- Splitter comparison / conditional adoption (AC8, EC11) -> Steps 8, 10
- Suite, ruff, no raw text in logs (AC9) -> every step's gate commands

## Implementation Steps
Checkpoint interval: stop after Step 2 (you run the live spike) and after Step 8 (you decide on the splitter).

**Deviation 2026-11-27 (approach G):** Step 1 becomes "`GoogleEmbedder` gains `embed_documents` / `embed_query`"
(files: `app/core/ai/google_embedder.py`, `tests/core/ai/test_google_embedder.py`; Test: first, seam
`embed_documents()` / `embed_query()`). Steps 2, 3, 6 and 7 are dropped: the vectors come from the same request code (AC1
answered by construction, no live call), the factory and evals already build `GoogleEmbedder`, and the budget test
already drives it. The only checkpoint left is after Step 8.

1. **Embedding wrapper.** Files: `app/core/ai/embeddings.py` (new), `tests/core/ai/test_embeddings.py` (new), a scripted
   fake `Embeddings` in `tests/core/ai/` helpers (or the existing `tests/` fakes). Wraps an injected `Embeddings`:
   one batched call per `embed()` with the task type and `output_dimensionality` (768, from config: the model's default is
   3072) per call (never set `task_type` on the instance: the class lets it override the per-call one), `RetryPolicy.call`
   for retries and the budget (each attempt bounded by `min(timeout, remaining)`; how the class takes a per-attempt
   timeout is a spike finding, since its `request_options` is an instance field), `to_llm_error` (taking the Google
   error from `__cause__`; a vendor error that is no Google API error must still map to `LLMTimeoutError` /
   `LLMServerError`, not the generic `LLMError`, or the degrade reason changes), vector-length check, `model`/`dimensions`/`close`, `EmbeddingResult` with attempts
   and latency. Verify: `uv run pytest tests/core/ai/test_embeddings.py` + gate commands. Test: first (seam: `embed()`)
2. **Live spike.** Files: `tests/live/test_embeddings_live.py` (new, opt-in via `LLM_LIVE_TEST=1`). Embeds sample note
   texts (as documents) and the retrieval eval's queries (as queries) with `GoogleGenerativeAIEmbeddings` and with
   the old `GoogleEmbedder`, prints each cosine, asserts >= 0.9999, checks the batched call, the vector length (768 via
   per-call `output_dimensionality`), the transport (the class defaults to gRPC; `EMBEDDING_BASE_URL` is a REST URL, so
   `transport="rest"` or a host form must be shown to work), that neither the class nor the Google client retries on its
   own (counted at a scripted failing endpoint), how a per-attempt timeout is passed, and that a forced 429, 5xx and
   timeout each arrive as the right `LLMError` (so the degrade reason matches today's).
   You run it; the outcome picks the path. Verify: `$env:LLM_LIVE_TEST = "1"; uv run pytest tests/live/test_embeddings_live.py -s`
   (run by the user). Test: after (external behavior)
3. **Path and factory.** Files: `app/core/ai/factory.py` (new `build_retrieval_embedder(settings)`), `app/main.py` (the
   lifespan sets `app.state.embedder` from it; `get_embedder` in `interviews_shared_dependencies.py` is unchanged and
   ingestion keeps `build_embedder`), `tests/core/ai/test_factory.py`; if the spike said no, also an adapter class in
   `app/core/ai/embeddings.py` over `GoogleEmbedder` (no re-embedding, no second retry layer). Config only: model,
   dimensions, timeout, retries and key from settings. Verify: `uv run pytest tests/core/ai/test_factory.py tests/core/ai/test_embeddings.py` + gate commands.
   Test: skip (wiring; factory assertion added to the existing file)
4. **Retriever.** Files: `app/modules/interviews/ai/interviews_retrieve.py` (new), `tests/modules/interviews/ai/test_retrieve.py`
   (new). A `BaseRetriever` bound to the search function and a vector; `invoke` returns documents carrying chunk id,
   competency, text and score; a plain function the service calls returns the ranked chunks (no LangChain type leaves
   the `ai/` folder). The similarity floor is not applied here. Verify: `uv run pytest tests/modules/interviews/ai/test_retrieve.py` + gate commands.
   Test: first (seam: `invoke()`)
5. **Wire the service.** Files: `app/modules/interviews/services/interviews_retrieval_service.py`,
   `tests/modules/interviews/services/test_retrieval_service.py`. `_ranked` calls the `ai/` function with
   `repo.nearest_chunks` as the search (the embedder reaches the service through the existing `get_embedder`, now
   holding the new class); one new test: a profile query makes one embed call (AC6). Existing expectations stay unchanged.
   Verify: `uv run pytest tests/modules/interviews/services/test_retrieval_service.py tests/test_layers.py` + gate commands.
   Test: first (seam: `retrieve()`)
6. **Eval tooling.** Files: `app/modules/interviews/tooling/interviews_rag_evals.py`, `tests/modules/interviews/tooling/test_retrieval_eval.py`,
   `tests/modules/interviews/tooling/test_generation_eval.py`. The retrieval and generation arms build the embedder with
   the new factory function; the run metadata still names the embedding model and dimensions. Verify: those two test
   files + gate commands. Test: skip (wiring; existing tests must still pass)
7. **Port the budget test.** Files: `tests/core/ai/test_retry_budget.py`. The embedder case drives the new wrapper over
   a scripted failing `Embeddings` and asserts at most `embedding_max_retries + 1` calls (2 today). If the spike chose
   the adapter, the case keeps the real `GoogleEmbedder` over the mock transport. Verify: `uv run pytest tests/core/ai/test_retry_budget.py` + gate commands.
   Test: first (seam: `embed()`)
8. **Splitter comparison.** Files: `tests/modules/interviews/utils/test_splitter_compare.py` (new; `pytest.importorskip` so
   the suite skips it). Chunks every note in `app/modules/interviews/data/knowledge` with `parse_note` and with
   `MarkdownHeaderTextSplitter`, reports per chunk text/heading equality and which chunk hashes would change.
   Verify (you run it): `uv run --with langchain-text-splitters pytest tests/modules/interviews/utils/test_splitter_compare.py -s`.
   Test: after (decides adoption; no `pyproject.toml` change here)
9. **Evals and docs.** Files: `docs/features/u3b2-retrieval/{task.md,learnings.md}`, `docs/evals/u3b2-embeddings-vs-baseline.md`,
   `docs/ai-engineering-upgrade-path.md`, `docs/evals/baselines.md` (only if a change is kept on purpose). You run the
   retrieval eval (command given at that point); I compare it in Langfuse against `retrieval/threshold-0.55/notes-754d0f/20261125-200010`
   (recall@5 1.00, MRR 0.909). Generation arms run only if retrieval returned different notes. Then `graphify update .`.
   Verify: `uv run pytest` + `uv run --with ruff ruff check .`. Test: skip (docs; full suite is the check)
10. **Only if Step 8 reports every chunk and hash identical, and you OK the dependency:** add `langchain-text-splitters`
    to `pyproject.toml`, adopt the splitter in the chunking path, re-run the knowledge tests and the retrieval eval.
    Otherwise skip, keep the current chunker and record the difference (EC11). Files: `pyproject.toml`,
    `app/modules/interviews/utils/interviews_knowledge_utils.py` (or an `ai/` function: LangChain only in `ai/`),
    `tests/modules/interviews/utils/test_knowledge_utils.py`. Verify: those tests + gate commands. Test: first (seam: `parse_note()`)

## Affected Files & Patterns
- `app/core/ai/embeddings.py`, `factory.py`, `app/main.py` — new wrapper, factory, lifespan wiring; follow `chat.py` / `chat_errors.py`
  (`RetryPolicy`, `to_llm_error`, labels) and `google_embedder.py` (result shape, size error).
- `app/modules/interviews/ai/interviews_retrieve.py` — follow the other `interviews/ai/` modules (plain functions).
- `interviews_retrieval_service.py`, `interviews_rag_evals.py` — `_ranked` through the `ai/` function; evals build the new embedder.
- Left alone: `GoogleEmbedder`, `Embedder`, ingestion, `KnowledgeRepository`, models, migrations, stored vectors.
- Risks: the Google class has no retry setting of its own, but the Google client under it may retry (double retries);
  an instance `task_type` overrides the per-call one; without `output_dimensionality` vectors are 3072 long
  (`size_mismatch` degrade); gRPC default vs the REST `EMBEDDING_BASE_URL`; the class batches in groups of 100 (fine for
  two queries); a non-Google transport error would map to the generic `LLMError` (`embedder_error`) instead of
  `timeout`/`rate_limited`, which would change the outcome strings.

## Testing Strategy
- Framework & command: `uv run pytest` (targets named per step).
- Gate commands: `uv run pytest`, `uv run --with ruff ruff check .` (layer rules run inside the suite via `tests/test_layers.py`).
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 2 | after | live; you run it |
| AC2 | 1, 3, 5 | first / skip | stored vectors untouched: no ingest runs |
| AC3 | 4, 5 | first | layer test |
| AC4 | 5 | first | existing tests unchanged |
| AC5 | 1, 7 | first | |
| AC6 | 5 | first | |
| AC7 | 9 | skip | you run the eval; Langfuse comparison |
| AC8 | 8 | after | |
| AC9 | 1-10 | gate | full suite + ruff; check logs hold ids, counts, codes only |
| EC1 | 2, 3 | after / skip | adapter path |
| EC2, EC3, EC4, EC5 | 1, 5 | first | map to existing degrade reasons |
| EC6, EC7, EC8, EC9 | 5 | first | existing service tests |
| EC10 | 5 | first | same as AC6 |
| EC11 | 8, 10 | after / first | |
| EC12 | 7 | first | |

- Must verify, not assume: cosine >= 0.9999 on both paths; the Google class's own retry behavior and error shape
  (`GoogleGenerativeAIError` with the Google error as `__cause__`, so EC3 maps to the same degrade reasons);
  per-call task type (never set on the instance); batch limits on the class's `embed_documents`.
- Open questions: none (every EC has an expected outcome).
- Known baseline failures: flaky `tests/modules/profile/utils/test_profile_read_resume.py` (passes alone); pyright errors in
  `interviews_feedback.py`, `interviews_report.py`, `profile_schema.py` are unrelated.

## Blockers & Resolutions
- Embeddings path -> decided by Step 2; Steps 1, 4, 5, 7 don't depend on it, Step 3 does.
- Splitter dependency -> only on adoption, with the user's OK (Step 10).
- Real Gemini calls -> the user runs Steps 2, 8 (compare) and 9 (eval); nothing live runs in the suite.

## Trade-offs & Rationale
- Retrieval-only wrapper (not ingestion) -> keeps stored vectors and ingestion unchanged; the old layer goes in U3c.
- Retriever bound to the vector -> keeps one embed call; a text-taking retriever with an `Embeddings` is deferred to U6.
- Similarity floor stays in the service -> spec and `CLAUDE.md`; the retriever is search only.

## Project Rules Applied
- `CLAUDE.md` -> LangChain only in `core/ai` and feature `ai/`; SQL in the repository; errors mapped to `LLMError`;
  evals compared with the baseline and written to `docs/evals/`; tests mock the embedder; no commits.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify / lean-ctx | retrieval service, repository, embedder, factory, eval tooling and test locations |
| grilling | retriever input shape, wrapper design, spike home, test seams (all user-confirmed) |
| ponytail | `uv run --with` for the splitter, vector-bound retriever, retrieval-only wrapper |

## Ready to Implement
- All spec requirements mapped to steps; every step has a Test tag; every AC and EC mapped (no uncovered IDs)
- Gate commands listed; every step names files and a verification command
- Approaches Considered filled; checkpoints set (after Steps 2 and 8)
- Seams user-confirmed: `embed()`, retriever `invoke()`, `RetrievalService.retrieve()`; `parse_note()` (Step 10) is
  conditional and gets confirmed if adopted
- No deviations from spec
