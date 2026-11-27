# U3b1 stage 1 (write on LangChain) vs. the baselines

**Verdict: no change.** The write eval and every judged generation arm, streamed and `--blocking`, score inside the
baseline's noise margin. `baselines.md` stays as it is.

**What changed in stage 1:** the blocking interview write (`write()`, the first question and the non-streaming answer
route) moved from the hand-built `LLMProvider` to the LangChain call helper (`complete_chat`). The write and
generation evals now call the same helper on the same chat model. Same prompts, same model, same reply loop. Details:
`docs/features/u3b1-interview-calls/` (steps 5-6).

**Setup:** model `gemini-3.5-flash-lite`, run by the user on 2026-11-27 with `--repeat 3` and the note "U3b1 stage 1,
write on LangChain" (`, blocking` for the JSON arms). **Only `r1` and `r2` of each run reached Langfuse**; no third
repeat is listed for any of the three. Baseline: `docs/evals/baselines.md`, section "U3b1 baselines".

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2) | Baseline | Noise margin | Verdict |
|---|---|---|---|---|---|
| write | `write/interviewer_v4/gemini-3.5-flash-lite/20261127-140210` | pass rate 1.00 / 1.00 | 1.00 / 1.00 | 0 | no change |
| generation arm A | `generation/interviewer_v5/gemini-3.5-flash-lite/20261127-143009` (`arm-A`) | skill coverage 0.850 / 0.750 | 0.750 / 0.875 / 0.925 / 0.800 | 0.175 | no change |
| generation arm C | `generation/interviewer_v7/.../20261127-143009` (`arm-C`) | skill coverage 0.750 / 0.675 | 0.542 / 0.775 / 0.600 / 0.775 | 0.233 | no change |
| generation arm D | `generation/interviewer_v8/.../20261127-143009` (`arm-D`) | skill coverage 0.633 / 0.583 | 0.450 / 0.725 / 0.475 | 0.275 | no change |
| generation `--blocking` C | `generation/interviewer_v7_json/.../20261127-145438` (`arm-C`) | skill coverage 0.792 / 0.692 | 0.800 / 0.717 / 0.700 | 0.233 | no change |
| generation `--blocking` D | `generation/interviewer_v8_json/.../20261127-145438` (`arm-D`) | skill coverage 0.500 / 0.542 | 0.667 / 0.592 / 0.425 | 0.275 | no change |

Secondary numbers (same runs):

| Eval | Measure | Now (r1 / r2) | Baseline | Reading |
|---|---|---|---|---|
| write | avg latency | 1,049 / 954 ms | 961 / 926 ms | same (+~60 ms, inside run-to-run noise) |
| write | errored items, length cut-offs | 0 / 0, 0 / 0 | 0 / 0, 0 / 0 | same |
| generation A | valid share | 1.00 / 0.952 | 1.00 / 1.00 / 0.876 / 0.914 | same |
| generation C | valid share | 0.814 / 0.829 | 0.957 / 0.850 / 0.910 / 0.957 | lower; one errored setup per repeat explains it (see Failures) |
| generation D | valid share | 0.986 / 0.857 | 0.971 / 0.943 / 0.905 | same range |
| generation `--blocking` C | valid share | 0.971 / 1.00 | 1.00 / 1.00 / 0.971 | same |
| generation `--blocking` D | valid share | 0.957 / 1.00 | 0.971 / 1.00 / 0.952 | same |
| generation | prompt tokens per question | A ~941, C 1,317 / 1,503, D 1,804 / 1,563 | A ~940, C ~1,515, D ~1,790 | same where every setup answered; lower means a setup's questions were missing |
| generation `--blocking` | prompt tokens per question | C ~1,502, D ~1,784 | C ~1,505, D ~1,786 | same |
| generation | distinct competencies | A 3.29 / 4.14, C 3.14 / 4.00, D 3.29 / 4.14 | (not in the baseline rows) | reported only |
| generation D | presumption flags, injection ignored | 0 / 2, 1.00 / 1.00 | 3 / 0 / 0, 1.00 | same |
| generation `--blocking` D | presumption flags, profile-only share | 0 / 1, 0.18 / 0.19 | 2 / 1 / 4, 0.11 / 0.15 / 0.25 | same |

## Failures

- **Errored items:** A r2 1, C r1 1, C r2 1, D r2 1, `--blocking` D r1 1 (of 7 setups each). An errored item means at least
  one question of that setup got no reply (a provider error, after the call layer's retries). The baseline had the
  same (1-2 per run in its second generation run), so this is not new. The scores don't record the error class; the
  free-tier request limit was hit around these runs (`141604`, below), so a 429 is the likely cause, unconfirmed.
- Arm C's lower valid share comes from those errored setups: without them the share is about 0.95-0.97, inside the
  baseline's range.

## Runs left out

- `generation/.../20261127-141604` (A, C, D, one repeat): hit the free-tier request limit (arm C 5 of 7 setups
  errored, arm D stopped after 2 setups). Not judged.

## What this shows

- The move kept the question rules (write pass rate 1.00) and the generation quality (skill coverage inside every
  arm's margin, on both the streamed and the JSON prompts).
- Latency and prompt tokens are unchanged: the chat model sends the same messages and the SDK's token counts match
  the old layer's.
- Only 2 repeats reached Langfuse. With margins of 0.18-0.28 a third would not change these verdicts; it would only
  narrow the spread.
