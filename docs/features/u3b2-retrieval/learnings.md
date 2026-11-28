# Learn: retrieval on LangChain (U3b2)

Status: built, tested and evaluated (retrieval eval: no change, 2026-11-27).

## 1. Why it exists
Retrieval was the last part of the app on the hand-built layer alone. U3c deletes that layer and U6 needs a LangChain
retriever, so query embedding and vector search had to speak LangChain's interfaces (`Embeddings`, `BaseRetriever`)
**without changing what retrieval returns**: same stored vectors, same model, same notes, same outcome strings.

## 2. What it is
- `GoogleEmbedder` (`app/core/ai/google_embedder.py:32`) is now also a LangChain `Embeddings`. It gained
  `embed_documents` (`:71`) and `embed_query` (`:74`); each is one call to the existing `embed` (`:77`), so the same
  request, retry rules, time budget and error types apply.
- `VectorRetriever` (`app/modules/interviews/ai/interviews_retrieve.py:40`) is a `BaseRetriever` bound to a vector the
  service already computed and to a search function the service passes in. `nearest` (`:55`) runs it and returns plain
  `Nearest` tuples, so no LangChain type leaves the `ai/` folder.
- `RetrievalService._ranked` (`app/modules/interviews/services/interviews_retrieval_service.py:176`) searches through
  `nearest`; the similarity floor, ranks, merge, time cap and degrade reasons stay in the service.

### Why not `GoogleGenerativeAIEmbeddings` (the plan's first choice)
Reading langchain-google-genai 3.2.0 before writing the wrapper showed two problems:
- `embed_documents` calls `self.client.batch_embed_contents(request)` (`embeddings.py:306` in the package) with no
  `timeout` and no `retry`. The `request_options` field is declared but never used. So every call gets the Google
  client's defaults: a 60 s timeout.
- The Google client's default retry for that method resends on `503 ServiceUnavailable` for up to a 60 s deadline. That
  is a second retry layer under our `RetryPolicy`.

The service's 0-to-cap time budget only works through `embed(..., budget_seconds=cap)` (`interviews_retrieval_service.py:194`),
and the retry budget test pins `1 + embedding_max_retries` calls. Neither could hold through that class. The user chose
our own class; then, to avoid a second copy of the HTTP code, `GoogleEmbedder` itself became the `Embeddings`.
Consequence: the vectors come from the exact same request code, so the planned live spike (AC1) was not needed.

### Why the retriever is bound to a vector, not a query text
A standard LangChain retriever takes the query text and embeds it itself. The service embeds the job-description and
profile queries in **one** batched call (AC6, `tests/modules/interviews/services/test_retrieval_profile.py:63`); a
text-taking retriever would make one embed call per query. A text-taking retriever with an `Embeddings` is deferred to
U6, when something needs it.

## 3. When to use it
- Any new code that needs a LangChain `Embeddings` (a retriever, an evaluator): pass the app's `GoogleEmbedder`.
- Service code keeps calling `embed(...)`: it carries the time budget and returns attempts and latency for the logs.
  `embed_documents` / `embed_query` have no budget argument (LangChain's interface has none), so they use the
  per-attempt timeout as the budget.

## 4. How it works: one interview start, through the code
1. `RetrievalService._retrieve` reads eligible chunks, releases the transaction, then `_embed` calls
   `self.embedder.embed(queries, kind=query, budget_seconds=cap)` once for both queries (`:194`).
2. For each vector, `_ranked` (`:176`) calls `nearest(lambda v: repo.nearest_chunks(...), vector)` (`:179`).
3. `nearest` builds a `VectorRetriever` and calls `invoke("")`; `_get_relevant_documents` (`interviews_retrieve.py:44`)
   calls the search with the bound vector and turns each `(chunk, score)` into a `Document` (text as `page_content`;
   chunk id, competency and score as metadata).
4. `nearest` converts the documents back to `Nearest` tuples; `_ranked` drops those below the floor and numbers the rest.

## 5. What can go wrong
| Failure | What happens | Test |
|---------|--------------|------|
| 503 twice through `embed_query` | `LLMServerError` after 2 calls (same budget as `embed`) | `tests/core/ai/test_google_embedder.py::test_the_langchain_methods_keep_the_retry_rules_and_the_typed_errors` |
| Wrong task type through the LangChain methods | documents use `RETRIEVAL_DOCUMENT`, queries `RETRIEVAL_QUERY` | `test_google_embedder.py::test_it_is_a_langchain_embeddings_whose_methods_send_one_batched_call` |
| The retriever applies the floor by mistake | a 0.01 score must still come back from `nearest` | `tests/modules/interviews/ai/test_retrieve.py::test_nearest_returns_plain_chunks_and_applies_no_similarity_floor` |
| Degrade reasons change | the existing retrieval service tests pass unchanged (AC4) | `tests/modules/interviews/services/test_retrieval_service.py`, `test_retrieval_profile.py` |
| LangChain leaks into the service | layer test fails | `tests/test_layers.py` |

## 6. Try it yourself
- Predict: if `nearest` were called with a search that returns 8 chunks, how many come back? (All 8: `top_k` is the
  repository's limit, passed in the lambda, not the retriever's.) Check by adding a case to `test_retrieve.py`.
- Predict: `GoogleEmbedder(...).embed_query("x")` with a 3-number vector configured as 4 dimensions. (An
  `EmbeddingSizeError`, from `_parse`, not retried.)

## 7. What surprised me
- A LangChain integration field (`request_options`) that exists but is never sent. Read the code path, not the field
  list, before relying on a setting.
- The Google client under LangChain retries on its own; "LangChain has no retry setting" does not mean "no retries".

### Eval log
| Date | Change | Eval | Runs | Result | Decision |
|------|--------|------|------|--------|----------|
| 2026-11-27 | retriever + `GoogleEmbedder` as `Embeddings` + splitter | retrieval (threshold 0.55), `retrieval/threshold-0.55/notes-754d0f/20261127-203131/r1` | 1 (deterministic) | vector recall@5 1.00, MRR 0.909; filter 0.506 / 0.288; 26 of 26 cases same notes, order and scores as the baseline; no failures | no change; generation eval not needed; baseline row unchanged ([comparison](../../evals/u3b2-embeddings-vs-baseline.md)) |

### Splitter comparison (Step 8) and adoption (Step 10)
- Run by the user, 2026-11-27:
  `uv run --with langchain-text-splitters pytest tests/modules/interviews/utils/test_splitter_compare.py -s` ->
  `splitter vs parse_note: 75 of 75 chunks identical (text and hash)`. So adopting it re-embeds nothing.
- Adopted (`langchain-text-splitters` 1.2.0, user OK): `split_sections` in `app/modules/interviews/ai/interviews_split.py`
  gives each `##` heading's text, and `_sections` in `interviews_knowledge_utils.py` uses it.
- Surprise: the splitter is lenient where ingestion must be strict. It silently drops a `##` heading with no text and
  merges two sections with the same heading. So `_sections` still scans the headings itself (to raise "empty section"
  and "duplicate heading") and takes only the text from the splitter (`tests/modules/interviews/ai/test_split.py`).
- The comparison test was removed after adoption: with `parse_note` on the splitter it would compare it with itself.
- Found in review: the splitter also strips every line and drops tabs, so an indented nested list or code block in a
  future note would be flattened silently (new text, new hash). The corpus has none, which is why it matched 75/75.
  `_sections` now refuses such lines, and a `##` heading the splitter doesn't see (`##B` without a space, or inside a
  code fence) gets a clear error instead of "empty section" (`tests/modules/interviews/utils/test_knowledge_utils.py`).
  Lesson: "identical on today's data" is not "identical"; check what the library does to inputs the data doesn't have yet.

## 8. Check your understanding
1. Why does `GoogleEmbedder` keep its own `embed(...)` when it now has `embed_documents`?
2. Why is the retriever bound to a vector instead of embedding its query itself?
3. What would have broken with `GoogleGenerativeAIEmbeddings`?

<details>
<summary>Answers</summary>

1. `embed` takes the caller's time budget and returns attempts, latency and model for the logs; LangChain's interface
   has no place for either.
2. To keep one batched embed call for the job-description and profile queries (AC6, no extra round trip).
3. The time cap (no per-call timeout, fixed 60 s) and the retry budget (its Google client retries 503s itself).
</details>

## 9. Still open
- U3c: move `GoogleEmbedder` out of the old layer's naming, move ingestion onto the `Embeddings` methods if useful.
