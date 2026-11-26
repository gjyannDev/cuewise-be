# U2 (tenacity) vs. the U0 baseline

**Verdict: no change.** All four evals that cover the changed code score inside the baseline's noise margin. `baselines.md` stays as it is.

**What changed in U2:** only retry code. Transport retries moved onto one tenacity `RetryPolicy` (full-jitter waits, `retry_wait` / `retry_giveup` events), and the four reply loops share one attempt header (`ReplyAttempts`). No prompt, model or parsing change. Details: `docs/features/u2-tenacity/`.

**Why these evals:** U2 touched `core/ai/` and the interviews `ai/` folder; the reply loops it changed are decide, write, write stream and the feedback turn. A healthy provider never retries, so these evals guard the reply loops; they don't exercise the new transport retries (the fault check does, see the end).

**Setup:** model `gemini-3.5-flash-lite`, `--repeat 2`, run by the user on 2026-11-26, Langfuse note "u3 tenacity vs baseline" (a typo for U2; the runs are U2's). Baseline: `docs/evals/baselines.md` (U0, 2026-11-25).

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2) | Baseline (r1 / r2) | Noise margin | Verdict |
|---|---|---|---|---|---|
| write | `write/interviewer_v4/gemini-3.5-flash-lite/20261126-144409` | pass rate 1.00 / 1.00 | 1.00 / 1.00 | 0 | no change |
| stream | `stream/interviewer_v5/gemini-3.5-flash-lite/20261126-145732` | pass rate 1.00 / 1.00 | 1.00 / 1.00 | 0 | no change |
| decide | `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261126-150904` | accuracy 0.80 / 0.80 | 0.80 / 0.80 | 0 | no change |
| feedback | `feedback/feedback_score_v2/gemini-3.5-flash-lite/20261126-152209` | pass rate 0.90 / 1.00 | 1.00 / 0.90 | 0.10 | no change |

Secondary numbers (same runs):

| Eval | Measure | Now (r1 / r2) | Baseline (r1 / r2) | Reading |
|---|---|---|---|---|
| write | errored items | 0 / 0 | 0 / 0 | same |
| write | avg latency | 3,799 / 2,003 ms | 2,988 / 4,568 ms | inside the baseline's own spread (±1,580 ms); latency is noisy |
| stream | avg time to first token | 1,680 / 2,391 ms | 2,591 / 2,698 ms | faster, but network-bound and only 2 runs; not a U2 effect (no retries happened) |
| stream | avg latency | 1,839 / 2,740 ms | 3,517 / 3,147 ms | same reading |
| decide | over- / under-probing | 2 / 2, 0 / 0 | 2 / 2, 0 / 0 | identical |
| feedback | in-band rate, valid replies | 1.00 / 1.00, 1.00 / 1.00 | 1.00 / 1.00, 1.00 / 1.00 | identical |
| all four | errored items | 0 in every run | 0 in every run | no provider failures |

## Failures

- feedback r1: 1 of 10 cases failed (pass rate 0.90). The baseline's r2 failed one case the same way (0.90), and the margin is 0.10, so it's model noise, not U2.
- No other failed items, no errored items.

## An extra set of runs (not used for the verdict)

Claude also started the same four evals by mistake (they ran in the background after the job was believed cancelled), at 2026-11-26 14:34–14:40, note "U2 tenacity: transport retries on RetryPolicy, …": `write/…/20261126-143451`, `stream/…/20261126-143652`, `decide/…/20261126-143922`, `feedback/…/20261126-144048`.

They had 1 to 3 errored items per run, and Langfuse shows each as `ERROR: LLMRateLimitError`: the provider's rate limit (free tier), which the eval itself marks "not a quality problem". Without the errored items their scores match the baseline. They are left out: the user's runs, minutes later on the same code, had no rate-limit errors, so the errors reflect the quota at that moment, not the code.

What they do show: under a real 429, the new transport policy gave up and the reply loop fell back, as designed. The fault check is still the proper end-to-end check of that path.

## Still to do

- Nothing. The fault check passed on 2026-11-26 (`docs/features/u2-tenacity/task.md`, step 15): real timeouts produced `retry_wait` / `retry_giveup` events and a bank fallback, and `interview_report` still reported normally.
