# Learn: Context management (what to send, and what it costs)

**Concepts:** 2 Context management, 3 Prompts as data, 9 Cost, 10 Evals, and model choice. See
`docs/ai-engineering-learning-path.md`.

---

## 1. Why it exists

Slice 2 resends the whole interview on every call: the system prompt, the job description, and every earlier question and
answer. Real runs showed input and hidden-reasoning output doubling and tripling by question 3, and a reasoning model
running out of `max_tokens` (`finish=length`).

The baseline (`uv run python -m app.scripts.usage_report` on the dev DB, 2026-10-29, prompt `interviewer_v1`, full
history):

```
interviews=16 llm_interviews=2l
interview 01a1869f-...  questions=3 llm=3 bank=0
  q1 prompt=523 completion=261 latency_ms=2677
  q2 prompt=580 completion=474 latency_ms=4624
  q3 prompt=627 completion=811 latency_ms=5590
  total prompt=1730 completion=1546
interview 01a18690-...  questions=2 llm=1 bank=1
  q1 prompt=288 completion=453 latency_ms=3353
```

Input grew about 50 tokens per question. Output roughly tripled from question 1 to 3 (261 -> 811), and latency doubled
with it. 14 of the 16 stored interviews ran on the bank only (LLM off), so the report averages over the 2 that used the LLM.

## 2. What it is

**Context management** is deciding what goes into the model's input. The context window is limited and every token you
send costs money. More context isn't always better: relevant details get diluted.

Two kinds of cost, and they behave differently:

| Kind | Example | Behavior |
|---|---|---|
| **Growing** | The history of earlier turns | Rises by one turn per question |
| **Fixed per call** | System prompt, job description | Resent unchanged every call |

A context *strategy* can only shrink the growing part. The fixed part needs a shorter prompt or a cache.

Cuewise has a `ContextManager` that builds the input per task using a named strategy:

- **`full_history`**: everything so far (the baseline).
- **`window_ledger`**: the last few turns in full, older ones as a short ledger, answers capped in length, plus running
  notes and a job-description summary, under an input limit.

The prompt itself is also context. `interviewer_v2` is written as **six parts**: `# Role`, `# Task`, `# Input`,
`# Output`, `# Constraints`, `# Capabilities`.

## 3. When to use it

| Use it when | Skip / expect little when |
|---|---|
| History is long enough to hit a limit or a real cost | Interviews are short: the fixed prompt is the bigger cost |
| Answers are long (about 2,000 chars): the break-even against full history is around Q6-7 | Answers are short (about 440-1,080 chars): the gap closes too slowly to break even within the 10-question maximum |
| You need a **cap** so the maximum interview stays under the input limit | You expected a saving: here it is a cap on input, not a saving |
| A job description is long: summarise it once (it saved about 148 tokens per call) | The job description is already short |
| The stable prefix is identical every call: it can be cached by the provider | Evals: each case is a different interview, so `cached=0` there says nothing about caching |

**I'd revisit this when** answers get longer or interviews get longer than 10 questions (the ledger saves more as
history grows), or after the cache and ablation runs in section 9.

## 4. How it works

**The options compared:**

| Setup | What it sends | Result in this app |
|---|---|---|
| `full_history` + `interviewer_v1` | Everything so far | Cheapest on short interviews, input grows each turn |
| `window_ledger` + `interviewer_v2` | Window + ledger + summary + notes | **About twice the old input**: the 5,501-char prompt is resent every call |
| `window_ledger` + `interviewer_v3` | Same, shorter prompt (2,848 chars) | 35% less input than v2; near parity with v1 at Q9; the live default |

**The flow:**

```
core/ai/context.py:73          ContextManager.build(task, inputs, strategy)   picks the strategy, applies the input limit
core/ai/context.py:33          Strategy: the contract each strategy implements
interviews_context.py:83       FullHistory      (baseline)
interviews_context.py:113      WindowLedger     (live default)
interviews_constants.py:310    WINDOW_LEDGER = "window_ledger"
interviews_constants.py:326    WINDOW_TURNS = 3,  WINDOW_ANSWER_CAP = 600,  WINDOW_INPUT_LIMIT = 5000
interviews_constants.py:340    LEVEL_GUIDANCE (level text used by the v2/v3 prompts)
prompts/                       interviewer_v1..v3.md, job_description_summary_v1.md
scripts                        python -m app.scripts.usage_report       (tokens per question and interview)
evals                          python -m app.modules.interviews.interviews_evals --strategy ... --prompt ... --repeat N
```

**The six prompt parts** (a test checks the order in `interviewer_v2.md` and `job_description_summary_v1.md`): every v1
rule is in v2's Constraints. New in v2: how to choose a question (competency spread, interview arc, job description use,
level guidance from `LEVEL_GUIDANCE`, answerable out loud), the running note, good and bad examples, a self-check, and the
`<interview_status>` block described as app data. `interviewer_v2` is about 5,500 characters against v1's 1,300: roughly
1,000 more input tokens on every call, in the stable prefix.

## 5. What can go wrong

| Failure | What happens | What the code / you do |
|---|---|---|
| Free model rate limit (HTTP 429) | The first attempt on `gemma-4-26b-a4b-it:free` got 429 on 26 of 27 calls; later runs hit 429 after about 25 calls | Pause between runs; the runner counts these as failures, so separate infrastructure errors from quality failures |
| Reasoning model runs out of `max_tokens` | `finish=length`, no text, bank question | Larger `max_tokens`, or a non-reasoning model |
| Reply wrapped in an extra object | `{"json": {"question": ...}}` rejected by the strict contract | In the app: one retry, then a bank question |
| Key written twice in one object | `json.loads` keeps the last value, so `extra="forbid"` doesn't see it | Format slip that passed; known gap |
| Latency compared across runs | Rate-limited calls are averaged in at 0 ms | Don't compare latency from these runs |
| Strategy sends fewer turns but a bigger prompt | Costs *more* per interview | Measure the fixed prefix before calling a strategy a saving |
| Input limit | A maximum interview (10 main, 2 follow-ups each, 500-char questions, 2,000-char answers) stays under the 5,000-token limit at every turn | Older threads are dropped first and the current thread is never split |
| Injection after a prompt rewrite | Both injection cases passed 3/3 under v3 as well | Keep the injection evals in every prompt comparison |

## 6. Try it yourself

Write your prediction first, then check.

1. **Input vs output growth.** Predict which grows faster per question in a real interview: the input or the output
   tokens, and why. Then run `uv run python -m app.scripts.usage_report`.
2. **Six parts.** Predict which of the six parts `interviewer_v1` missed most. Then open `interviewer_v2.md` and point to
   each part.
3. **Which sends fewer tokens?** For a 5-question interview, predict whether `window_ledger` or `full_history` sends
   fewer tokens in total. Then check the table in section 7, checkpoint E.
4. **Compare strategies.** Run the same cases under each strategy (pause a minute between runs):
   `uv run python -m app.modules.interviews.interviews_evals --strategy full_history --repeat 3 --model gemini-3.5-flash-lite`
   and again with the default (`window_ledger`).
5. **Compare prompts.** Run `--prompt interviewer_v2` against the default (v3) with the same model and `--repeat 3`.

## 7. What surprised me

**Checkpoint A: output, not input, grew fastest.** With full history the input grows by one turn per question: slow and
predictable. The output here is mostly hidden reasoning, which grows with how much the model "thinks", not with how much
it is sent. So the first cost and reliability problem in these numbers was output. Context strategies cut input;
reasoning effort and model choice are the levers for output.

**Checkpoint B: v2 is much bigger than v1.** `interviewer_v2` is about 5,500 characters against 1,300, roughly 1,000
more input tokens per call, in the stable prefix (the part most likely to be cached, if the provider caches).

**Checkpoint C: the "before" snapshot** (`--strategy full_history --repeat 3`, `gemini-3.5-flash-lite`, `interviewer_v1`,
`max_tokens=2000`, 2026-10-30; `full_history` is unchanged code, so it still reproduces the old behaviour):

```
run 1: passed 9/9   tokens 5512 in (0 cached) / 366 out (0 reasoning)   finish=length 0/9
run 2: passed 6/9   3 x LLMRateLimitError (no reply)
run 3: passed 6/9   2 x LLMRateLimitError, 1 x valid_reply(schema)
runner: mean=0.78 min=0.67 max=1.00
```

Counting only calls that returned a reply: **20/21 passed**. The one real failure wrapped a valid reply in an extra
object. Injection: `injection-in-answer` and `injection-in-job-description` passed 3/3 each. Input per case (run 1):
329-391 for short cases, 1117-1348 for the two long-history cases (question 9), 953 for the long job description.
Output 23-40 tokens, except 106-123 for the long job description. No reasoning tokens.

**Checkpoint D: the strategy comparison** (2026-10-30, `gemini-3.5-flash-lite`, `--repeat 3`). It compares the old live
setup (`full_history` + `interviewer_v1`) with the new one (`window_ledger` + `interviewer_v3` + notes), not the strategy
alone: the prompt changed too.

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

Input per case, run 1:

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

- Short cases cost about +400 tokens under `window_ledger` v3: that is the longer prompt (v3 2,848 chars vs v1 1,298). At
  question 9 the gap shrinks to +27 and +152: the ledger's savings on history almost cancel the larger prompt.
- Injection: both cases passed 3/3 under v3 as well, and the notes summarise only the real part of the injected answer.
- Long-history replies: `backend-senior` asked about distributed tracing, then multi-tenant isolation in PostgreSQL
  twice (new competencies, consistent with the PostgreSQL migration); `mixed-mid` asked technical questions in runs 1-2
  (data consistency between services, refactoring a legacy schema) and a behavioral one in run 3, although question 8
  was already technical.
- Format slip that passed: in `vague-behavioral-junior` runs 1-2 the model wrote the `"category"` key twice in one object.
- Separate infrastructure errors from quality failures before reading a pass rate. The runner's 0.78 vs 0.96 is mostly
  rate limits.

**Checkpoint E: where the cost went** (live interview `01a18a8f-...`, `gemini-3.5-flash-lite`: 5 questions, a 1030-char
job description summarised to 439, answers of 441 / 458 / 836 / 633 / 1081 chars). Every call re-built offline from the
stored data under each setup; estimated input tokens, chars / 4. The `window_ledger v2` row matches the live
`context_build` log exactly.

```
setup                              Q1     Q2     Q3     Q4     Q5   total
full_history v1 + original JD     606    777    936   1190   1400    4909
full_history v1 + summary         458    630    788   1043   1252    4171
window_ledger v2 + summary       1534   1725   1884   2138   2227    9508
window_ledger v3 + summary        875   1066   1225   1479   1568    6213
```

- Every part of the context manager worked: the summary saved about 148 tokens per call (740 over 5 calls, against 546
  for the one summary call); the ledger kicked in at Q5 (Q4 -> Q5 grew +89 tokens against +210 for full history); the
  836-char answer was capped to 600 once it left the latest turn.
- Yet **`window_ledger v2` sent about twice as much as the old setup.** `interviewer_v2` (5,501 chars, about 1,400 tokens)
  is resent on every call. That fixed cost was bigger than everything the history strategy saved.
- With answers like these, full history grows about 200 tokens per question and `window_ledger` about 90 after Q4: the
  gap closes too slowly to break even within the 10-question maximum. With 2,000-char answers it would break even around
  Q6-7.
- `interviewer_v3` (2,848 chars) keeps v2's rules but drops the bad examples, the self-check and repeated wording: 35% less
  input than v2 (6,213 vs 9,508). Still above v1, because the level guidance, the interview arc and the note
  instructions cost tokens.
- The last turn of the 3-question baseline interview tripled in *output* tokens (checkpoint A), not input; on
  `gemini-3.5-flash-lite` output stayed at 37-72 tokens per question. Context strategies did not fix that; the model
  change did.

## 8. Check your understanding

1. **(Proof, concept 1)** Why does turn 10 cost more than turn 1? Which part of that cost does `window_ledger` remove,
   and which part does it not touch?
2. **(Proof, prompts)** Point to each of the six parts in `interviewer_v2.md`. Why is "Capabilities" empty today, and
   when would it stop being empty?
3. **(Proof, evals)** Did `window_ledger` + v3 earn its place as the default? Answer with the numbers: quality,
   injection, tokens, and which cost it does not remove.
4. **(Proof, cost)** Why can a strategy that sends fewer turns still cost more per interview? What would you measure
   before trimming a prompt?
5. **(Why)** Why is a pass rate of 0.78 vs 0.96 not a quality difference here?
6. **(When)** When would `window_ledger` actually save tokens over `full_history`?
7. **(How)** How do you tell whether the provider caches the stable prefix?
8. **(What if)** What if the system prompt doubled in size again?

<details>
<summary>Reference answers (write yours first)</summary>

1. The whole history is resent each call, so input grows by one turn per question. `window_ledger` limits that growth
   (full history grows about 200 tokens per question, the ledger about 90 after Q4). It does not touch the fixed
   per-call cost (system prompt, job description) or the model's hidden reasoning output.
2. Role, Task, Input, Output, Constraints, Capabilities, in that order (a test checks it). Capabilities is empty because
   the interviewer calls no tools today; it would fill in when the model is given functions to call (the later
   tool-use stage).
3. Yes, as a cap with equal quality: 26/26 on returned replies vs 20/21, injection 3/3 on both, about +53% input on short
   cases but near parity at Q9 (+27 / +152). It does not remove the fixed prompt cost, and at 10 questions it is a cap
   on input, not a saving.
4. Because whatever is resent unchanged every call (system prompt, job description) is a fixed cost that dominates short
   interviews: v2's 1,400-token prompt outweighed all the history it saved (9,508 vs 4,909). Before trimming, measure
   both the growing and the fixed part.
5. Most of the gap is rate-limit errors (HTTP 429), which the runner counts as failures. On replies the model actually
   returned, both setups are near-perfect on the rule checks.
6. When answers are long. With 2,000-char answers it would break even around Q6-7; with the observed short answers the
   gap closes too slowly within 10 questions.
7. Read `cached_tokens` in the `llm_call` log of a live interview and see whether it is non-zero from Q2 on. Eval runs
   can't show it (each case is a different interview).
8. The fixed cost per call would grow by the same amount on every call, so a history strategy would save an even
   smaller share of the total; a shorter prompt or a cached prefix becomes the lever.

</details>

## 9. Go deeper / Still open

- Spec and plan: `docs/features/context-management/spec.md`, `plan.md`.
- Related: `llm-interviewer/learnings.md` (the first measurements of reasoning tokens), and the follow-up questions
  slice, which needs even more context.
- Next concept this unlocks: prompt caching (`cached_tokens`) and model choice for cost.

**Still open** (optional; keeping `window_ledger` + v3 as the default does not depend on them):

1. Run one more live interview and read `cached_tokens` in each `llm_call` line: is the prefix served from cache from
   Q2 on?
2. Check that v3 did not lose quality: `interviews_evals --prompt interviewer_v2` vs the default (v3), same model,
   `--repeat 3`, and read the long-history questions side by side.
3. `--summary on/off`, `--notes on/off`, `--reasoning-effort low/medium/high`, and a reasoning vs a non-reasoning model.
   Wait a minute between runs: both runs above hit HTTP 429 after about 25 calls.
4. Grade the long-history replies from checkpoint C with the 5-point checklist from the plan (pass/fail with a one-line
   reason each).
