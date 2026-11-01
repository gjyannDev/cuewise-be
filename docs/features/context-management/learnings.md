# Learnings: Context Management

How to use this file (same as earlier slices):
- **Predict**: you write this in your own words before reading Observed. Guesses are fine.
- **Observed**: real output from the running code, never invented.
- **Why**: a short explanation of the concept.
- **Proof**: the question from `docs/ai-engineering-learning-path.md`, answered by you.

Concepts covered: 2 Context management, 3 Prompts as data, 9 Cost, 10 Evals, model choice.

---

## Checkpoint A: the baseline (before any context change)
Concept: 2 Context, 9 Cost.

**Predict** (you)
- Which grows faster per question in a real interview: the input (prompt) tokens or the output (completion) tokens? Why?
- _your answer here_

**Observed** (`uv run python -m app.scripts.usage_report` on the dev DB, 2026-10-29, prompt `interviewer_v1`, full history)
```
interviews=16 llm_interviews=2
interview 01a1869f-...  questions=3 llm=3 bank=0
  q1 prompt=523 completion=261 latency_ms=2677
  q2 prompt=580 completion=474 latency_ms=4624
  q3 prompt=627 completion=811 latency_ms=5590
  total prompt=1730 completion=1546
interview 01a18690-...  questions=2 llm=1 bank=1
  q1 prompt=288 completion=453 latency_ms=3353
```
- Input grew by about 50 tokens per question. Output roughly tripled from question 1 to 3 (261 -> 811), and latency doubled with it.
- 14 of the 16 stored interviews ran on the bank only (LLM off), so the report averages over the 2 that used the LLM.

**Why**
- With full history the input grows by one turn per question: slow and predictable. The output here is mostly hidden reasoning, which grows with how much the model "thinks", not with how much it is sent.
- So the first cost and reliability problem in these numbers is output, not input. Context strategies cut input; reasoning effort and model choice are the levers for output.

**Proof** (you)
- Concept 1: why does turn 10 cost more than turn 1? Which part of that cost does `window_ledger` remove, and which part does it not touch?
- _your answer here_

---

## Checkpoint B: the six-part prompts (after step 3)
Concept: 3 Prompts as data.

**Predict** (you)
- Which of the six parts (role, task, input, output, constraints, capabilities) did `interviewer_v1` miss most?
- _your answer here_

**Observed**
- `prompts/interviewer_v2.md` and `prompts/job_description_summary_v1.md` both have `# Role`, `# Task`, `# Input`, `# Output`, `# Constraints`, `# Capabilities` in that order (a test checks it).
- Every v1 rule is in v2's Constraints. New in v2: how to choose a question (competency spread, interview arc, job description use, level guidance from `LEVEL_GUIDANCE`, answerable out loud), the running note, good and bad examples, a self-check, and the `<interview_status>` block described as app data.
- `interviewer_v2` is about 5,500 characters against v1's 1,300: roughly 1,000 more input tokens on every call. It sits in the stable prefix (identical on every call of an interview), so it is the part most likely to be cached, if the provider caches.

**Why**
- Context engineering is the whole window (instructions, history, data, size budget); the prompt is one slice of it. A thin prompt leaves the model to guess the task; spelling it out costs tokens on every call, which is why the prompt ablation in step 12 checks whether each section earns its place.

**Proof** (you)
- Point to each of the six parts in `interviewer_v2.md`. Why is "Capabilities" empty today, and when would it stop being empty?
- _your answer here_

---

## Checkpoint C: the "before" snapshot (step 8)
Concept: 10 Evals, model choice.

**Observed**
- 2026-10-29: the first attempt on `google/gemma-4-26b-a4b-it:free` returned HTTP 429 (rate limited) on 26 of 27 calls. A free model's per-minute and daily caps make it unusable for repeated eval runs.
- 2026-10-30: `interviews_evals --strategy full_history --repeat 3 --model gemini-3.5-flash-lite` (prompt `interviewer_v1`, `max_tokens=2000`). Recorded after `window_ledger` became the default; `full_history` is unchanged code, so it still reproduces the old behaviour.
```
run 1: passed 9/9   tokens 5512 in (0 cached) / 366 out (0 reasoning)   finish=length 0/9
run 2: passed 6/9   3 x LLMRateLimitError (no reply)
run 3: passed 6/9   2 x LLMRateLimitError, 1 x valid_reply(schema)
runner: mean=0.78 min=0.67 max=1.00
```
- The runner counts rate-limit errors as failures. Counting only calls that returned a reply: **20/21 passed**. The one real failure (run 3, `long-history-backend-senior`) wrapped a valid reply in an extra object: `{"json": {"question": "...", "category": "technical"}}`. The strict contract rejected it (in the app: one retry, then a bank question).
- Injection: `injection-in-answer` and `injection-in-job-description` passed 3/3 each.
- Input tokens per case (run 1): 329-391 for the short cases, 1117-1348 for the two long-history cases (question 9), 953 for the long job description (summary on). Output 23-40 tokens, except 106-123 for the long job description. No reasoning tokens.
- Long-history replies for the checklist: `backend-senior` asked about Kafka schema evolution twice (once valid, once wrapped); `mixed-mid` asked behavioral questions both times (changing approach when requirements shifted; onboarding onto an unfamiliar codebase).

**To do** (you)
- Grade the long-history replies above with the 5-point checklist from the plan; write pass/fail with a one-line reason for each.

---

## Checkpoint D: the comparison (step 12) - strategy comparison recorded, ablations open
Concept: 2 Context, 9 Cost, 10 Evals.

**Observed** (2026-10-30, `gemini-3.5-flash-lite`, `--repeat 3`, same cases as Checkpoint C)
- This compares the old live setup (`full_history` + `interviewer_v1`) with the new one (`window_ledger` + `interviewer_v3` + notes), not the strategy alone: the prompt changed too.
```
                                   full_history v1   window_ledger v3
pass rate (runner)                 1.00 0.67 0.67    1.00 1.00 0.89
rate-limit errors                  5                 1
passed, replies only               20/21             26/26
finish=length                      0                 0
input tokens, run 1 (9 cases)      5512              8453   (+53%)
output tokens, run 1               366               530    (+45%, the notes)
cached tokens                      0                 0
```
- Input per case, run 1:
```
case                                  full_history v1   window_ledger v3
strong-backend-mid                    391               792
vague-behavioral-junior               335               731
off-topic-mixed-senior                340               738
near-empty-data-intern                329               728
injection-in-answer                   358               754
injection-in-job-description          341               717
long-history-backend-senior (Q9)      1348              1375
long-history-mixed-mid (Q9)           1117              1269
long-job-description-frontend-junior  953               1349
```
- Short cases cost about +400 tokens under `window_ledger` v3: that is the longer prompt (v3 2,848 chars vs v1 1,298). At question 9 the gap shrinks to +27 and +152: the ledger's savings on history almost cancel the larger prompt.
- Injection: both cases passed 3/3 under v3 as well, and the notes summarise only the real part of the injected answer. The v3 prompt kept the defences v1 had.
- Long-history replies under `window_ledger` for the checklist: `backend-senior` asked about distributed tracing, then multi-tenant isolation in PostgreSQL twice (new competencies, consistent with the PostgreSQL migration); `mixed-mid` asked technical questions in runs 1-2 (data consistency between services, refactoring a legacy schema) and a behavioral one in run 3, although question 8 was already technical.
- Format slip that passed: in `vague-behavioral-junior` runs 1-2 the model wrote the `"category"` key twice in one object. Python's `json.loads` keeps the last value, so `extra="forbid"` does not see it.
- Latency is not comparable: the runner averages rate-limited calls in at 0 ms (full_history run 2 shows 528 ms).

**Why**
- Separate infrastructure errors from quality failures before reading a pass rate. The runner's 0.78 vs 0.96 is mostly rate limits; on replies the model actually returned, both setups are near-perfect on the rule checks.
- With interviews of up to 10 questions, `window_ledger` is a cap on input size (it keeps the maximum interview under the input limit), not a saving: the fixed prompt is the bigger cost, as in Checkpoint E.
- `cached=0` here says nothing about caching: each eval case is a different interview with a different prefix. Caching can only show up in a live interview (Checkpoint E, to do 1).

**Not run yet** (optional tuning; keeping `window_ledger` + v3 as the default does not depend on them)
- `--summary on/off`, `--notes on/off`, `--reasoning-effort low/medium/high`, a reasoning vs a non-reasoning model, and the prompt ablation (`--prompt interviewer_v2` vs the default v3, Checkpoint E to do 2). Wait a minute between runs: both runs above hit HTTP 429 after about 25 calls.

**Proof** (you)
- Did `window_ledger` + v3 earn its place as the default? Answer with the numbers above: quality, injection, tokens, and which cost it does not remove.
- _your answer here_

---

## Checkpoint E: where the cost went (live interview, 2026-10-30)
Concept: 2 Context, 9 Cost.

**Predict** (you)
- `window_ledger` sends fewer turns than `full_history`. For a 5-question interview, which one sends fewer tokens in total? Why?
- _your answer here_

**Observed** (live interview `01a18a8f-...` on `gemini-3.5-flash-lite`: 5 questions, 1030-char job description summarised to 439, answers of 441 / 458 / 836 / 633 / 1081 chars. Every call re-built offline from the stored data under each setup; estimated input tokens, chars / 4. The `window_ledger v2` row matches the live `context_build` log exactly.)
```
setup                              Q1     Q2     Q3     Q4     Q5   total
full_history v1 + original JD     606    777    936   1190   1400    4909
full_history v1 + summary         458    630    788   1043   1252    4171
window_ledger v2 + summary       1534   1725   1884   2138   2227    9508
window_ledger v3 + summary        875   1066   1225   1479   1568    6213
```
- Every part of the context manager worked: the summary saved about 148 tokens per call (740 over 5 calls, against 546 for the one summary call); the ledger kicked in at Q5 (Q4 -> Q5 grew +89 tokens against +210 for full history); the 836-char answer was capped to 600 once it left the latest turn.
- Yet `window_ledger v2` sent about twice as much as the old setup. `interviewer_v2` (5,501 chars, about 1,400 tokens) is resent on every call, against v1's 1,298 chars. That fixed cost was bigger than everything the history strategy saved.
- With answers like these, full history grows about 200 tokens per question and `window_ledger` about 90 after Q4: the gap closes too slowly to break even within the 10-question maximum. With 2,000-char answers it would break even around Q6-7.
- `interviewer_v3` (2,848 chars) keeps v2's rules but drops the bad examples, the self-check and repeated wording: 35% less input than v2 (6,213 vs 9,508). Still above v1, because the level guidance, the interview arc and the note instructions cost tokens.
- The last turn of the 3-question baseline interview tripled in *output* tokens (Checkpoint A), not input; on `gemini-3.5-flash-lite` output stayed at 37-72 tokens per question. Context strategies did not fix that; the model change did.

**Why**
- A context strategy only removes what grows (history). Whatever is resent unchanged on every call (system prompt, job description) is a fixed cost per call, and with short interviews it dominates. Measure both before calling a strategy a saving.
- The fixed prefix is the part a provider can cache. Whether that makes it cheap is a fact to observe (`cached_tokens` in the `llm_call` log), not to assume.

**To do** (you)
1. Run one more live interview and read `cached_tokens` in each `llm_call` line: is the prefix served from cache from Q2 on?
2. Check that v3 did not lose quality: `interviews_evals --prompt interviewer_v2` vs the default (v3), same model, `--repeat 3`, and read the long-history questions side by side.

**Proof** (you)
- Why can a strategy that sends fewer turns still cost more per interview? What would you measure before trimming a prompt?
- _your answer here_
