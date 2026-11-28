# Feature: U3b2 — Retrieval on LangChain

## Problem
Retrieval (embedding the interview's query, finding similar reference notes, splitting notes into chunks) is the last
part of the app still running on the hand-built layer: our own `Embedder` interface and `GoogleEmbedder`. That blocks
U3c (which deletes the old layer) and U6 (which needs a LangChain retriever). The maintainer wants retrieval on
LangChain building blocks **without changing what it returns**.

## Goal
Embeddings and retrieval run on LangChain classes (`Embeddings`, `BaseRetriever`), with stored vectors and the model
name unchanged (no re-embedding), the retrieval eval unchanged (recall@5 1.00, MRR 0.909), and the time cap, degrade
reasons, similarity floor and ranking merge behaving as today.

## Project Conventions
- Rules consulted: `CLAUDE.md` (project), `docs/ai-engineering-upgrade-path.md` (U3b2), memory `u3b-split-decision`.
- Constraints they impose:
  - LangChain may be imported only in `app/core/ai/` and feature `ai/` folders; routes, controllers, services and
    repositories never import it. The service calls the feature's `ai/` functions.
  - SQL stays in `KnowledgeRepository`; no LangChain vector stores (`PGVector`). A retriever in the feature's `ai/`
    folder gets the repository's search function from the service instead of importing the repository.
  - Vendor exceptions are mapped to the `LLMError` types before they leave `core/ai/`; retries are owned by `RetryPolicy`.
  - Old layer (`Embedder`, `GoogleEmbedder`) stays until U3c; old and new never mix inside one task.
  - AI change: run the covering eval(s) against `docs/evals/baselines.md`; comparison written to
    `docs/evals/u3b2-<change>-vs-baseline.md`. The user runs real-model evals and live tests; Claude gives commands.
  - Tests mock the embedder (deterministic); real-model calls are opt-in.
  - No new dependency without a justification and the user's OK.

## User Flow
No candidate-facing change. Starting an interview still retrieves reference notes for the job description (and the
profile's query when the interview opted in) and passes them to the question writer.

1. Start request -> `RetrievalService.retrieve(...)`.
2. The service reads eligible chunks, embeds the query (and profile query) in **one** batched call, searches by vector,
   applies the similarity floor, merges the rankings and returns notes (or a degraded/skipped result with a reason).
3. Steps 2's embed call and search now go through LangChain classes; the observable result is the same.

## Requirements

### Functional
- **Embeddings spike first.** Compare `GoogleGenerativeAIEmbeddings` (`gemini-embedding-001`, 768 dimensions,
  `RETRIEVAL_QUERY` / `RETRIEVAL_DOCUMENT` task type set per call) with the vectors the current path produces and the
  stored ones, on a sample. Match -> use the LangChain class, with its errors mapped to `LLMError` types
  (it wraps them as `GoogleGenerativeAIError`; the Google error is `__cause__`) and retries owned by `RetryPolicy`.
  No match -> a thin `Embeddings` adapter over `GoogleEmbedder`. The result and the chosen path are recorded.
- **Vector retriever.** A `BaseRetriever` in the interviews `ai/` folder that searches by an already-computed vector,
  using a search function the service passes in (backed by `KnowledgeRepository.nearest_chunks`). It returns documents
  carrying chunk id, competency, text and similarity score.
- **Service keeps the policy.** `RetrievalService` still owns: the time cap, the degrade reasons, the similarity
  floor, the batched embed call for the job-description and profile queries, the ranking merge, the filter fallback and
  the logging/tracing.
- **Failures keep their outcomes.** A failing embed call yields the same `retrieval_degraded:<reason>` /
  `retrieval_skipped:<reason>` strings and the same worst-case embed call count as today.
- **Splitter: compare, adopt only if identical.** Add `langchain-text-splitters` only for the comparison; adopt
  `MarkdownHeaderTextSplitter` only if it reproduces today's chunks and their hashes for the whole corpus. Otherwise
  keep the current chunker and record the difference.
- **Evals follow the code.** The retrieval eval tooling (`interviews_rag_evals.py`) runs through the new path.
- **Test port.** The embedder case in `tests/core/ai/test_retry_budget.py` (real `GoogleEmbedder` over a mock transport)
  is ported if the embedder changes, with the same worst-case number.

### Non-Functional
- Latency: no extra embed round trip per start (the two queries stay in one call).
- Privacy: logs and traces keep ids, counts, scores and codes only; no query or note text.
- Config only: no hardcoded model name, URL or key.

## UX Requirements
- No UI change. Candidates see the same "notes used or not" behavior; a failed retrieval still degrades silently to
  the filter mode with the outcome code in logs/traces.

## Constraints
- Stored vectors and the embedding model name must not change; no re-embedding.
- `Embedder` / `GoogleEmbedder` stay for ingestion and until U3c; ingestion is untouched in this slice.
- Python 3.14, `uv`; the spike needs live Gemini calls, run by the user.

## Blockers
- Which embeddings path (LangChain class vs adapter) is decided by the spike; the plan's first step is the script and
  the user runs it. The spec holds for both outcomes.
- Splitter adoption depends on the chunk/hash comparison and the user's OK for the new dependency (comparison only).

## Edge Cases
- **EC1:** `GoogleGenerativeAIEmbeddings` vectors differ from the stored ones beyond the match rule -> use the thin
  `Embeddings` adapter over `GoogleEmbedder`; stored vectors untouched.
- **EC2:** Embed call times out or exceeds the time cap -> `retrieval_degraded:<reason>` as today; filter mode notes.
- **EC3:** Rate-limit / server / bad-response error from the vendor -> mapped to the matching `LLMError`, same degrade
  reason as today (assumption — verify against the mapping in the spike).
- **EC4:** Embedder not configured -> `not_configured` degrade, as today.
- **EC5:** Returned vector length differs from `KNOWLEDGE_VECTOR_SIZE` (or embedder dimensions differ) -> `size_mismatch`
  degrade, as today.
- **EC6:** No eligible chunks for role/level -> `retrieval_skipped:no_match`, as today.
- **EC7:** Database error while reading or searching -> `retrieval_skipped:db_error`, transaction released, as today.
- **EC8:** Job description has no usable query text but a profile query exists -> the profile ranking leads, as today.
- **EC9:** First ranking has nothing above the similarity floor -> filter mode with `below_threshold` degrade; the
  profile ranking never takes over, as today.
- **EC10:** Profile query present -> one batched embed call for both queries, not two.
- **EC11:** Splitter output differs from today's chunks or hashes in any chunk -> do not adopt it; keep the current
  chunker; no re-embedding; record the difference.
- **EC12:** Retry budget: scripted vendor failures -> embed attempts never exceed today's worst case (`1 + max retries`).

## Acceptance Criteria
- [ ] **AC1:** A spike script embeds a sample of stored note texts and sample queries with `GoogleGenerativeAIEmbeddings`
  and reports, per vector, cosine similarity to the current path's/stored vector; the match rule is >= 0.9999 and the
  retrieval ranking on the sample is unchanged. The outcome (LangChain class vs adapter) is written in the feature docs.
- [ ] **AC2:** Query embedding in retrieval goes through a LangChain `Embeddings` implementation (the class or the
  adapter); the stored vectors and the embedding model name are unchanged (no re-embedding runs).
- [ ] **AC3:** The vector search is a `BaseRetriever` in the interviews `ai/` folder fed by a search function passed from
  the service; no LangChain import exists in the service, repository, controller or route (`tests/test_layers.py` holds).
- [ ] **AC4:** The time cap, degrade reasons, similarity floor, ranking merge and filter fallback behave as today: the
  existing `RetrievalService` unit tests pass without changes to their expected outcomes.
- [ ] **AC5:** Embedding failures (timeout, rate limit, server error, bad response) produce the same outcome strings as
  before, and `tests/core/ai/test_retry_budget.py`'s embedder case (ported if needed) gives the same worst-case call count.
- [ ] **AC6:** With a profile query, one embed call serves both queries (asserted in a test).
- [ ] **AC7:** The retrieval eval, run by the user, scores recall@5 1.00 and MRR 0.909 (the `retrieval/threshold-0.55`
  baseline); the comparison is written to `docs/evals/u3b2-<change>-vs-baseline.md`. The generation eval runs afterwards
  only if retrieval returned different notes.
- [ ] **AC8:** The splitter comparison reports, for every chunk of the corpus, identical/different text and hash. It is
  adopted only if all match; otherwise the current chunker stays and the result is recorded.
- [ ] **AC9:** Full test suite and ruff pass; no raw note or query text appears in logs or traces.

## Out of Scope
- Deleting `Embedder`, `GoogleEmbedder` and the rest of the old layer (U3c).
- Moving ingestion/embedding of documents onto LangChain (left with the old layer until U3c).
- The fallback chain and the question-bank removal (U3c).
- LangChain vector stores (`PGVector`) and any change to the schema, vectors or embedding model.
- Re-embedding or re-chunking the corpus.
- New retrieval features (hybrid search, reranking, the U6 work).
