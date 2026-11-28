# U3c (provider chain, question bank removed, old layer deleted) vs. the baseline

**Verdict: no change in quality.** Write, stream and decide score exactly what their baselines scored; feedback
repeats the baseline's single out-of-band case. No errors, no length cut-offs, no rejected quotes in any run.
Latency is the same or a little lower (same-day network noise, not a claim).

**What changed in U3c:** the chat model is now a chain of every provider in `LLM_PROVIDERS` (one provider is
configured, so every call goes to the same model as before); a turn that cannot write ends in a retryable 503
instead of a bank question; the bank, the "LLM off" modes and the old provider layer are gone. Prompts, model and
retrieval are unchanged. Details: `docs/features/u3c-fallback-chain/`.

**Setup:** model `gemini-3.5-flash-lite`, run by the user on 2026-11-28 with `--repeat 2` and the note "U3c chain"
(all 8 repeats reached Langfuse, environment `eval`). Baseline: `docs/evals/baselines.md`, section "U3b1 baselines"
(the write and feedback rows, "stream (current latency)" and "decide (current)"). The chain was exercised on one
provider only: the fallback itself is proven with fake models in `tests/core/ai/test_chat_chain.py`, not in these
runs.

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2) | Baseline | Noise margin | Verdict |
|---|---|---|---|---|---|
| write | `write/interviewer_v4/gemini-3.5-flash-lite/20261128-121629` | pass rate 1.00 / 1.00 | 1.00 / 1.00 | 0 | no change |
| stream | `stream/interviewer_v5/gemini-3.5-flash-lite/20261128-122800` | pass rate 1.00 / 1.00 | 1.00 / 1.00 / 1.00 | 0 | no change |
| decide | `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261128-130120` | accuracy 0.933 / 0.933 | 0.933 / 0.933 / 0.933 | 0.067 (one case) | no change |
| feedback | `feedback/feedback_score_v2/gemini-3.5-flash-lite/20261128-131954` | pass rate 0.90 / 1.00 | 0.90 / 1.00 | 0.10 (one case) | no change |

Secondary numbers (same runs):

| Measure | Now (r1 / r2) | Baseline | Reading |
|---|---|---|---|
| write avg latency | 797 / 840 ms | 961 / 926 ms | a little lower; the baseline's own spread is small, so treat it as network noise |
| stream avg time to first token | 742 / 705 ms | 793 / 776 / 734 ms | inside the baseline's range |
| stream avg latency | 809 / 761 ms | 857 / 849 / 805 ms | inside the baseline's range, a touch lower |
| decide over-probing / under-probing | 0 / 0 and 0 / 0 | 0 / 0 (all repeats) | same |
| feedback in-band rate | 0.889 / 1.00 | 0.889 / 1.00 | same |
| feedback valid replies | 1.00 / 1.00 | 1.00 / 1.00 | same |
| feedback rejected quotes, template texts | 0 / 0 and 0 / 0 | 0 | same |
| errored items, length cut-offs (all four evals) | 0 | 0 | same |

## Failures

- feedback r1: one case scored outside its expected band (`overall_in_band`, `level_gap` and two criterion checks
  failed for that one case; the reply itself was valid). It is the same kind and the same count as the baseline's one
  out-of-band case (`overall_in_band_rate` 0.889 in both, i.e. 8 of 9 cases). I did not match it to the baseline's
  case by name, so "the same case" is not claimed; r2 had no failure. Type: quality (the model's score), not
  infrastructure or contract.
- No other failure in any run: every other case passed every check.

## Baseline

No row in `baselines.md` changes: nothing moved on purpose, and every score is within its noise margin. The U3b1
rows stay the reference for later changes.

## Not covered by these runs

- **Retrieval and generation evals were not run.** U3c changed no retrieval, ingestion, prompt or notes code, only
  the `parse_note` / `load_corpus` signature (the splitter is passed in), which the ingest tests and the shipped
  corpus test cover. Run `--task retrieval` if you want that confirmed on the real corpus.
- **No second real provider.** The cost/score comparison "provider B scores N/M at X times the cost of A" waits for a
  slice that adds a second vendor.
- **Summary and profile evals were not run**: the chain reaches them through the same helper, but their prompts and
  code did not change.
