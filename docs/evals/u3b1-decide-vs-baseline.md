# U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline

**Verdict: better, not a regression; recorded as the new decide baseline.** Decision accuracy rose from 0.800 / 0.867
to 0.933 / 0.933, confirmed by a third repeat at 0.933 (+1 to +2 cases of 15), and over-probing (asking a follow-up
the label says isn't needed) fell from 2 / 1 to 0 / 0 / 0. Nothing got worse.

**What changed in stage 2:** the follow-up decision moved from the hand-built `LLMProvider` to LangChain with
structured output: the request carries the `ModelDecision` JSON schema (`action`, `gap`, `note`, all required; `gap`
and `note` nullable), and `parse_decision_reply` still checks the reply text. Same prompt (`follow_up_decision_v1`),
same model. Details: `docs/features/u3b1-interview-calls/` (steps 8-9).

**Setup:** model `gemini-3.5-flash-lite`, run by the user on 2026-11-27 with `--repeat 3` and the note "U3b1 stage 2,
decide on LangChain". **Only `r1` and `r2` reached Langfuse** (as with every `--repeat 3` run today). Baseline:
`docs/evals/baselines.md`, section "U3b1 baselines".

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2) | Baseline (r1 / r2) | Noise margin | Verdict |
|---|---|---|---|---|---|
| decide | `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261127-153726` | accuracy 0.933 / 0.933 | 0.800 / 0.867 | 0.067 (one case) | better (+1 to +2 cases) |

Secondary numbers (same runs):

| Measure | Now (r1 / r2) | Baseline (r1 / r2) | Reading |
|---|---|---|---|
| pass rate (every check) | 0.933 / 0.933 | - | the one failing case per run is the decision itself |
| over-probing | 0 / 0 | 2 / 1 | the whole gain is here: no unneeded follow-ups |
| under-probing | 0 / 0 | 0 / 0 | same |
| errored items | 0 / 0 | 0 / 0 | same |

## Failures

- One case per run still decides wrong (accuracy 14 / 15). It isn't over- or under-probing, so the action was right
  and the **gap** was wrong (follow-up with a different gap than the label).

## Why it may have improved

- With the schema, Gemini's reply is decoded against the allowed values, so the model can't drift into an off-list
  gap or an extra field; the old path relied on the prompt alone. That doesn't obviously explain fewer follow-ups, so
  part of the gain may be noise: two repeats can't separate a one-case change from luck.

## Should this be the new baseline?

**Yes, recorded 2026-11-27.** A confirming repeat, `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261127-155824`
(`--repeat 1`, note "U3b1 stage 2, decide confirm"), scored accuracy 0.933 again, over-probing 0, under-probing 0,
0 errored. Three repeats at 0.933 against a baseline of 0.800 / 0.867 is a steady gain of one to two cases, not luck
on one run. The project rule (a change that moves a score and is kept on purpose becomes the baseline row) applies:
`baselines.md` now has a "decide (current)" row with the three repeats, and the old row is marked superseded. Later
decide changes compare with the new row.
