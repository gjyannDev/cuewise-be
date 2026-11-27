# U3b1 stage 4 (feedback on LangChain, structured score) vs. the baseline

**Verdict: no change.** Pass rate 0.90 / 1.00 / 0.90 against a baseline of 0.90 / 1.00 (noise margin: one case,
0.10). Every reply was valid, no quote was rejected, no text fell back to the template, and the overall landed in its
band in 26 of the 27 labelled cases over the three repeats. Gemini took the nested score schema (with its criterion
-> score map), and the content scores held, not only validity. `baselines.md` stays as it is.

**What changed in stage 4:** end-of-interview feedback moved from the hand-built `LLMProvider` to LangChain. The score
call sends the `ModelScore` JSON schema (questions, a criterion -> score map, evidence; every field required) through
`complete_structured`, and `parse_score_reply` still checks the text (quotes found in the answers, the thread's
criteria, caps). The write call is `complete_chat` + `parse_write_reply`. Same prompts (`feedback_score_v2`,
`feedback_write_v1`), same model, same temperature and token caps. Details: `docs/features/u3b1-interview-calls/`
(steps 16-17).

**Setup:** model `gemini-3.5-flash-lite`, run by the user on 2026-11-27 with `--repeat 3` and the note "U3b1 stage 4,
feedback on LangChain". All three repeats reached Langfuse. Baseline: `docs/evals/baselines.md`, section "U3b1
baselines" (2 repeats).

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2 / r3) | Baseline (r1 / r2) | Noise margin | Verdict |
|---|---|---|---|---|---|
| feedback | `feedback/feedback_score_v2/gemini-3.5-flash-lite/20261127-171608` | pass rate 0.90 / 1.00 / 0.90 | 0.90 / 1.00 | 0.10 (one case) | no change |

Content and secondary numbers (same runs):

| Measure | Now (r1 / r2 / r3) | Baseline (r1 / r2) | Reading |
|---|---|---|---|
| overall in band | 1.00 / 1.00 / 0.889 | 0.889 / 1.00 | same: one case out of band in one repeat, as in the baseline |
| valid replies (score) | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 | the nested schema never broke a reply |
| quotes rejected | 0 / 0 / 0 | 0 | every quote was found in the candidate's answers |
| template texts (write failed) | 0 / 0 / 0 | - | every write reply was valid |
| errored cases | 0 / 0 / 0 | - | no provider failures |

## Failures

- **r1:** one case, one criterion out of its band (`trade_offs` of question 2), overall still in band.
- **r3:** one case, two criteria out of band (`depth` and `trade_offs` of question 2), so its overall left the band
  and its level-gap check failed too.
- Both are the technical criteria of the same question number, and of the same kind as the baseline's single failure
  (one case, overall out of band, r1). Model scoring noise inside the one-case margin, not a schema effect: the schema
  constrains the shape, not the score values.

## Langfuse nesting (spec assumption to verify)

Generations still nest under their feedback steps with the chat model's tracer: in the run's window, all 27
`feedback_score` generations have the `score` step as their parent and all 30 `feedback_write` generations the
`write` step (Langfuse v2 observations API, `parentObservationId`). None is at the root.

## What this shows

- Gemini's JSON-schema mode takes a nested schema with a map (`additionalProperties`), and with every field required
  the content scores (in band, quotes) hold, not only validity: the U3a profile lesson didn't repeat.
- The parser stays the business-rule check: with the schema, the model can still quote a sentence the candidate never
  said or score the wrong criteria, and only `parse_score_reply` catches that (none happened here).
