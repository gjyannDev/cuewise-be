# U3a (LangChain foundation) vs. the baselines

**Verdict: no change after one fix.** The job-description summary and the write eval score the same as before. Profile extraction **regressed on the first run**, the cause was found and fixed, and the re-run matches the baseline. `baselines.md` stays as it is (the summary row was added in Step 2, on the old call layer, and is the reference for this comparison).

**What changed in U3a:** the job-description summary and profile extraction moved from the hand-built `LLMProvider` to LangChain (`ChatGoogleGenerativeAI` behind `app/core/ai/chat.py`). Same prompts, same model, same time caps. Details: `docs/features/u3a-langchain-foundation/`.

**Setup:** model `gemini-3.5-flash-lite`, `--repeat 2` (write once), run by the user on 2026-11-26. Baseline: `docs/evals/baselines.md`.

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2) | Baseline (r1 / r2) | Noise margin | Verdict |
|---|---|---|---|---|---|
| summary | `summary/job_description_summary_v2/gemini-3.5-flash-lite/20261126-194748` | pass rate 0.67 / 0.83 | 0.67 / 0.83 | 0.17 | no change |
| write (once) | `write/interviewer_v4/gemini-3.5-flash-lite/20261126-200659` | pass rate 1.00 | 1.00 / 1.00 | 0 | no change |
| profile, first run | `profile/profile_extract_v1/gemini-3.5-flash-lite/20261126-195626` | title recall 0 / 0; role count match false / false; skills precision about 0.4-0.8 | all 1.00 / 1.00 | 0 | **regression** |
| profile, after the fix | `profile/profile_extract_v1/gemini-3.5-flash-lite/20261126-214403` | all scores 1.00 / 1.00, valid 5/5 | all 1.00 / 1.00 | 0 | no change |

Secondary numbers (same runs):

| Eval | Measure | Now (r1 / r2) | Baseline (r1 / r2) | Reading |
|---|---|---|---|---|
| summary | errored items | 0 / 0 | 0 / 1 (a timeout) | fewer, but a timeout is luck, not a U3a effect |
| summary | avg latency | 2,194 / 3,102 ms | 3,347 / 4,088 ms | faster; network-bound, 2 runs |
| summary | prompt / completion tokens per case | ~502 / ~76 | ~503 / ~77 | the native token counts match the old layer's |
| write | avg latency | 3,350 ms | 2,988 / 4,568 ms | inside the baseline's spread |
| profile | prompt tokens per run | 3,156 | 3,161 | same |
| profile | completion tokens per run | 935 / 1,015 | 744 / 744 | **+25 to +36%**; not a quality problem, see below |

## Failures

- summary r1: 1 case failed (`facts_kept`), as in the baseline's r1 (2 dropped facts there). Model noise inside the 0.17 margin.
- profile, first run: roles missing and skills padded on all 5 résumés (`valid` still 5/5, so only the content scores caught it); r2 also used 2,389 completion tokens.

## The profile regression

- **Cause (confirmed by the re-run):** `RawProfile` has a default on every field, so the JSON schema given to Gemini marked nothing as required. The model was free to leave out `roles` and pad `skills`. The old code asked for the shape in prose and the model followed it.
- **Fix:** a separate schema for the model, `ModelProfile` (and `ModelRole`, `ModelProject`), with every field required. `RawProfile` stays lenient for text replies. A test pins the `required` lists.
- **Result:** every score back to 1.00 on both repeats, `valid` 5/5.
- **Left over:** completion tokens are 25-36% above the baseline (935 / 1,015 against 744), probably because the structured reply always carries every field, empty ones included. Small in absolute terms (about 200-270 tokens per upload); watch it, no action.

## What this shows

- A schema marking every field optional is a quality regression the unit tests cannot see (the fake model returns what is scripted); only an eval against known answers caught it.
- Validity checks passed throughout; the content scores (title recall, role count, skills precision) were the ones that moved.
