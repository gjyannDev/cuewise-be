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

## Checkpoint C: the "before" snapshot (step 8) - NOT RECORDED YET
Concept: 10 Evals, model choice.

**Observed so far**
- 2026-10-29: `interviews_evals --strategy full_history --repeat 3` with the configured model `google/gemma-4-26b-a4b-it:free` returned HTTP 429 (rate limited) on 26 of 27 calls. A free model's per-minute and daily caps make it unusable for repeated eval runs, so there is no snapshot yet.

**To do** (you, before relying on `window_ledger` as the live default)
1. `uv run python -m app.modules.interviews.interviews_evals --strategy full_history --repeat 3 --model <a model that is not rate limited>`
2. Review the long-history outputs (the `review:` lines) with the 5-point checklist from the plan; write pass/fail with a one-line reason for each.
3. Record here: tokens per case and per run, `finish=length` count, pass rate mean/min/max, checklist results.

---

## Checkpoint D: the comparison (step 12) - NOT RECORDED YET
Run the same N as Checkpoint C and compare against it: `full_history` vs `window_ledger`, `--summary on/off`, `--notes on/off`, `--reasoning-effort low/medium/high`, a reasoning vs a non-reasoning model, and the prompt ablation (`--prompt <variant>`). Read `finish=length` first. Note whether the provider reports cached tokens (`cached=` in the runner output) before claiming any caching saving, and whether wrong notes carried into later questions (error accumulation).
