# U0 baselines

The numbers every upgrade slice (U1–U9) compares against. Filled from Langfuse on 2026-11-26 (experiments with the note "U0 baseline", run on 2026-11-25), plus the live-interview reports from `logs/app.log`.

**Setup for every run:** model `gemini-3.5-flash-lite`, commit `e12941b` (working tree not clean), max tokens 2000, reasoning effort default, notes and job-description summary on.

**Noise margin** = the spread between the repeats of the same run (r1 vs r2). A later change must move a score by more than this before it means anything. Every eval has **2 usable repeats**, not 3, so treat these margins as rough.

**Left out:** runs with errors. That means generation arm E r2 (7 of 7 items errored) and the profile runs `20261125-203951`, `20261125-205236` (all scores 0 or missing) and `20261126-073323` (only 3 of 5 valid).

## How to use this file

After an AI change, run only the evals that cover it (same model, at least 2 repeats), then ask Claude to compare the new run with the rows below.

| You changed | Run |
|---|---|
| Interviewer prompt or question-writing code | `--task write`, `--task stream`, `--task generation` |
| Follow-up decision | `--task decide` |
| Feedback | `--task feedback` |
| Retrieval, ingestion or notes | `--task retrieval`, plus `--task generation` if notes feed the prompt |
| Profile extraction | `profile_evals` |
| Job-description summary | `--task summary` |
| Shared `core/ai/` code or model config | all of the above |

A difference within the noise margin is no change. A drop beyond it is a regression. If you keep a change that moves a score on purpose, replace that row with the new run.

## Eval baselines

| Eval | Prompt | Langfuse run (prefix) | Items | Score (r1 / r2) | Noise margin | Notes |
|---|---|---|---|---|---|---|
| write | interviewer_v4 | `write/interviewer_v4/gemini-3.5-flash-lite/20261125-185221` | 19 | pass rate 1.00 / 1.00 | 0 | latency 2,988 / 4,568 ms (±1,580 ms, so latency is noisy) |
| stream | interviewer_v5 | `stream/interviewer_v5/gemini-3.5-flash-lite/20261125-190432` | 19 | pass rate 1.00 / 1.00 | 0 | time to first token 2,591 / 2,698 ms (±107); latency 3,517 / 3,147 ms |
| decide | follow_up_decision_v1 | `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261125-193926` | 15 | accuracy 0.80 / 0.80 | 0 | over-probing 2 / 2, under-probing 0 / 0 |
| feedback | feedback_score_v2 + feedback_write_v1 | `feedback/feedback_score_v2/gemini-3.5-flash-lite/20261125-195121` | 10 | pass rate 1.00 / 0.90 | 0.10 | in-band 1.00 / 1.00, valid replies 1.00 / 1.00 |
| retrieval | (no model) | `retrieval/threshold-0.55/notes-754d0f/20261125-200010` | 26 | vector recall@5 1.00, MRR 0.909 | n/a (deterministic, 1 run) | with filters: recall@5 0.506, MRR 0.288; profile vector: recall@5 1.00, MRR 1.00 |
| generation arm A | interviewer_v5 | `generation/interviewer_v5/.../20261125-200609` | 7 | skill coverage 0.800 / 0.775 | 0.025 | valid 1.00 / 1.00; ~943 prompt tokens |
| generation arm B | interviewer_v7 | `generation/interviewer_v7/.../20261125-200609` (arm-B) | 7 | skill coverage 0.867 / 0.442 | **0.43** | valid 0.94 / 0.85; ~1,529 prompt tokens. Very noisy |
| generation arm C | interviewer_v7 | `generation/interviewer_v7/.../20261125-200609` (arm-C) | 7 | skill coverage 0.700 / 0.700 | 0 | valid 0.85 / 0.83; retrieval start ~370 ms |
| generation arm D | interviewer_v8 | `generation/interviewer_v8/.../20261125-200609` (arm-D) | 7 | skill coverage 0.558 / 0.483 | 0.075 | valid 0.96 / 0.97; ~1,793 prompt tokens |
| generation arm E | interviewer_v8 | `generation/interviewer_v8/.../20261125-200609/r1/arm-E` | 7 | skill coverage 0.550 (r1 only) | unknown | valid 0.96; r2 excluded (7 errors) |
| profile | profile_extract_v1 | `profile/profile_extract_v1/gemini-3.5-flash-lite/20261126-073615` | 5 | all scores 1.00 / 1.00, valid 5/5 | 0 | 3,161 prompt + 744 completion tokens per run |
| summary | job_description_summary_v2 | `summary/job_description_summary_v2/gemini-3.5-flash-lite/20261126-185243` | 6 | pass rate 0.67 / 0.83 (r2: 5 of 5 answered cases passed, 1 errored) | 0.17 | Added 2026-11-26 for U3a, on the old call layer. valid 6/6 / 5/5; injection ignored 6/6 / 5/5; facts kept 4/6 / 5/5 (r1 dropped the job title of `data-analyst-junior` and "iOS" in `injection-ignore-instructions`). r2's injection case timed out at the 10 s summary cap (`LLMTimeoutError`). ~503 / 513 prompt + 77 / 80 completion tokens per case; latency 3,347 / 4,088 ms |

## U3b1 baselines (old call layer, before the interview calls move to LangChain)

Filled from Langfuse on 2026-11-27 (experiments with the note "U3b1 baseline, old layer", run on 2026-11-27). These are the rows the U3b1 comparisons use. Same model `gemini-3.5-flash-lite`, HEAD `3b44fef` (the tree only had docs changes). They sit next to the U0 rows because the model's speed changed between the two days, so **latencies are only comparable inside this table**.

**Only 2 repeats** were run for write, stream, decide and feedback (the spec asked for 3). Their noise margin is one case, so 2 repeats are enough to judge them. Generation has 4 repeats per arm (the first run `20261127-105016` hit the daily request limit part-way, so the arms were run again as `20261127-114544`).

| Eval | Prompt | Langfuse run (prefix) | Items | Score (r1 / r2) | Noise margin | Notes |
|---|---|---|---|---|---|---|
| write | interviewer_v4 | `write/interviewer_v4/gemini-3.5-flash-lite/20261127-094729` | 19 | pass rate 1.00 / 1.00 | 0 | latency 961 / 926 ms; 0 length cut-offs |
| stream | interviewer_v5 | `stream/interviewer_v5/gemini-3.5-flash-lite/20261127-095810` | 19 | pass rate 1.00 / 1.00 | 0 | time to first token 1,089 / 1,386 ms (±297); latency 1,154 / 1,548 ms |
| stream (current latency) | interviewer_v5 on `stream_chat` | `stream/interviewer_v5/gemini-3.5-flash-lite/20261127-163159` | 19 | pass rate 1.00 / 1.00 / 1.00 | 0 | U3b1 stage 3 (native Gemini streaming): time to first token 793 / 776 / 734 ms, latency 857 / 849 / 805 ms. Later stream changes compare latency with this row (`docs/evals/u3b1-stream-vs-baseline.md`) |
| decide | follow_up_decision_v1 | `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261127-100951` | 15 | accuracy 0.800 / 0.867 | 0.067 (one case) | **superseded by the next row** (old call layer); over-probing 2 / 1, under-probing 0 / 0, valid replies 1.00 / 1.00 |
| decide (current) | follow_up_decision_v1 + `ModelDecision` schema | `decide/follow_up_decision_v1/gemini-3.5-flash-lite/20261127-153726` (`r1`, `r2`) and `.../20261127-155824` (`r1`, the confirming repeat) | 15 | accuracy 0.933 / 0.933 / 0.933 | 0.067 (one case) | U3b1 stage 2 (decide on LangChain with structured output), kept on purpose; over-probing 0 / 0 / 0, under-probing 0 / 0 / 0, 0 errored. Compare later decide changes with this row (`docs/evals/u3b1-decide-vs-baseline.md`) |
| feedback | feedback_score_v2 + feedback_write_v1 | `feedback/feedback_score_v2/gemini-3.5-flash-lite/20261127-102134` | 10 | pass rate 0.90 / 1.00 | 0.10 (one case) | in-band 0.889 / 1.00, valid replies 1.00 / 1.00, quotes verified 1.00, 0 rejected quotes |
| generation arm A | interviewer_v5 | `generation/interviewer_v5/.../20261127-105016` and `.../20261127-114544` | 7 | skill coverage 0.750 / 0.875 / 0.925 / 0.800 | 0.175 | valid 1.00 / 1.00 / 0.876 / 0.914 (the last two had 2 errored items each); ~930–947 prompt tokens |
| generation arm C | interviewer_v7 | same runs, `arm-C` | 7 | skill coverage 0.542 / 0.775 / 0.600 / 0.775 | 0.233 | valid 0.957 / 0.850 / 0.910 / 0.957; retrieval start ~300–360 ms; ~1,515 prompt tokens |
| generation arm D | interviewer_v8 | same runs, `arm-D` | 7 | skill coverage 0.450 / 0.725 / 0.475 | 0.275 | valid 0.971 / 0.943 / 0.905; ~1,790 prompt tokens; profile-only mention share 0.13–0.23; presumption flags 3 in the first repeat, 0 in the others. The 4th repeat (`105016` r2, 6 of 7 items errored) is left out |
| generation arm B | interviewer_v7 | `.../20261127-105016/r2/arm-B` | 7 | skill coverage 0.750 (1 repeat) | unknown | reported only, not judged |
| generation arm E | interviewer_v8 | `.../20261127-105016/r1/arm-E` | 7 | skill coverage 0.442 (1 repeat) | unknown | reported only, not judged; valid 0.957 |
| generation `--blocking` arm C | interviewer_v7_json | `generation/interviewer_v7_json/gemini-3.5-flash-lite/20261127-130930` (`r1`, `r2`) and `.../20261127-132414` (`r1`, the third repeat), `arm-C` | 7 | skill coverage 0.800 / 0.717 / 0.700 | 0.233 (arm C's streamed margin; these 3 repeats spread 0.100) | valid 1.00 / 1.00 / 0.971; distinct competencies 3.86 / 3.43 / 3.14; ~1,505 prompt tokens; retrieval start ~300–380 ms; 0 errored items |
| generation `--blocking` arm D | interviewer_v8_json | same runs, `interviewer_v8_json/.../arm-D` | 7 | skill coverage 0.667 / 0.592 / 0.425 | 0.275 (arm D's streamed margin; these 3 repeats spread 0.242) | valid 0.971 / 1.00 / 0.952 (1 errored item in each of `130930` r1 and `132414` r1); distinct competencies 3.71 / 4.29 / 3.57; ~1,786 prompt tokens; profile-only mention share 0.11 / 0.15 / 0.25; presumption flags 2 / 1 / 4; injection ignored 1.00 |

**The `--blocking` rows** (added 2026-11-27 from Langfuse; U3b1 step 4, note "U3b1 baseline, old layer, blocking") run the same arms on the JSON writer the blocking answer route sends. The first run (`130930`) was asked for 3 repeats but only 2 reached Langfuse, so the third was run on its own (`132414`, `--repeat 1`). The comparison at Stop 2 uses the streamed arms' margins (C 0.233, D 0.275), which are at least as wide as these three repeats' spread. Read the run-level `*_mean` scores.

**Reading the generation rows:** skill coverage moves by 0.18–0.28 between repeats of the *same* code, so a generation change smaller than that is no change. The U0 values (A 0.800 / 0.775, C 0.700, D 0.558 / 0.483) fall inside these ranges, so the old layer behaves the same as it did then. A, C and D are the arms the U3b1 spec judges. The `errored` items in the second generation run (1–2 per run) were not looked into, so their cause is unknown.

## Prompts with no eval baseline (gaps)

U3 can't prove these unchanged until they have one:
- none left: interviewer_v7_json and interviewer_v8_json got their baseline on 2026-11-27 (the `--blocking` rows above)

## Live interviews (from `logs/app.log`, before U1)

From `interview_report --last 3` (2 completed interviews and 1 abandoned):

| Measure | Value |
|---|---|
| Turn LLM time | p50 4,666 ms, p95 12,527 ms (6 turns) |
| Write call | p50 1,502 ms, p95 7,351 ms |
| Decide call | p50 2,005 ms, p95 6,275 ms |
| Request | p50 1,358 ms, p95 9,277 ms |
| Busiest turn | 42% of the 30 s turn deadline |
| Tokens | 5,689 per interview, 2,438 per main question (input 16,544, output 522) |
| Tokens by purpose | write 25%, decide 35%, other 40% |
| Fixed system prompt | 64% of the input |
| Reliability | 6 of 6 answer turns without a failed call or fallback |
| Follow-ups | 0 asked over 7 main questions |

From `usage_report` (all 28 logged interviews): turn LLM time p50 2,169 ms, p95 9,095 ms (60 turns); ~4,485 prompt and 126 completion tokens per interview.

## Cost

- **One full eval run** (every task above, 2 repeats): **about $0.26**, from 479 model calls and 656k tokens (Langfuse, environment `sdk-experiment`, 2026-11-25). With 3 repeats expect about $0.38.
- U3 re-runs the evals after each of its ~8 migration steps, so U3 costs roughly **$2–3** in evals.
- Live interviews: Langfuse logged no cost for them in the eval window. Use the token numbers above.

## Before relying on this

- Run the evals with a clean working tree next time, so `commit` points to real code.
- Arm B's 0.43 spread on skill coverage means one 7-item run can't tell v7 versions apart. Use more items or more repeats before judging generation changes.
