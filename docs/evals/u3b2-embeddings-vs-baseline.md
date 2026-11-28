# U3b2 (retrieval on LangChain) vs. the baseline

**Verdict: no change.** The retrieval eval returned the same notes, in the same order, with the same similarity
scores for all 26 cases as the baseline run: vector recall@5 1.00 and MRR 0.909, as before. The generation eval was
not run: it only runs when retrieval picks different notes, and it didn't.

**What changed in U3b2:** query embedding goes through `GoogleEmbedder`, which is now also a LangChain `Embeddings` (same
request code as before); the vector search runs through a LangChain `BaseRetriever` (`interviews_retrieve.py`); note
sections are split by `MarkdownHeaderTextSplitter` (it reproduced all 75 chunks and hashes, so nothing was re-embedded).
Same embedding model, dimensions and stored vectors. Details: `docs/features/u3b2-retrieval/`.

**Setup:** no chat model (retrieval embeds the queries only), run by the user on 2026-11-27 with
`uv run python -m app.modules.interviews.tooling.interviews_evals --task retrieval --note "u3b2: retriever + splitter"`.
Baseline: `docs/evals/baselines.md`, the `retrieval` row.

## Scores

| Eval | Langfuse run | Score | Baseline | Noise margin | Verdict |
|---|---|---|---|---|---|
| retrieval | `retrieval/threshold-0.55/notes-754d0f/20261127-203131/r1` | vector recall@5 1.00, MRR 0.909 | `retrieval/threshold-0.55/notes-754d0f/20261125-200010` (recall@5 1.00, MRR 0.909) | 0 (deterministic: same vectors, same SQL ranking) | no change |

Secondary numbers (same run, from the run's printout):

| Measure | Now | Reading |
|---|---|---|
| filter mode recall@5 / MRR | 0.506 / 0.288 (20 orderings) | the fallback, unchanged code |
| profile cases (vector) recall@5 / MRR | 1.000 / 1.000 | the second query in the same batched call |
| threshold sweep | recall@5 1.000 up to 0.60, 0.857 at 0.65 | same shape as the baseline's |

## Case-by-case check (Langfuse)

Each case's output (`top_notes`: the top 5 note keys and their scores) was read from both runs through the Langfuse
API (`/api/public/experiment-items`, then each item's observations) and compared:

- 26 of 26 cases in both runs, no missing outputs;
- 26 of 26 with the same notes in the same order;
- 26 of 26 with the same scores (largest difference 0.0).

The comparison read note keys and scores only, never the cases' job-description text.

## Should this be the new baseline?

No: nothing moved, so the `retrieval` row in `baselines.md` stays as it is.
