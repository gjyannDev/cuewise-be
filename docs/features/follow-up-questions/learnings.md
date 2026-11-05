# Learn: Follow-up questions (decide / write split)

**Concepts:** 2 Context, 4 Structured output, 5 The LLM decides and the code enforces, 9 Cost (the turn deadline),
10 Evals (labelled cases). See `docs/ai-engineering-learning-path.md`.

> **Status.** The code is built and unit-tested end to end with fakes (2026-10-31). Several measurements still need
> real-model runs; those parts of this file are marked **pending** and listed in section 9.

---

## 1. Why it exists

A good interviewer doesn't move on after a vague answer: they dig ("What was the actual outcome?"). But a model told to
do that will sometimes dig forever, and one call that both judges the answer and writes the next question is hard to
validate and hard to bound.

So a turn is split in two:

1. A small **decide** call: is the answer complete, or is there a gap worth probing?
2. A **write** call: write the follow-up or the next main question.

The model suggests, and the code decides what is allowed.

## 2. What it is

- **A closed decision.** The decide call returns `{action, gap, note}`: `action` is `follow_up` or `next_question`,
  `gap` comes from a closed list, `note` is a short free-text note. A closed list makes "is this valid" a parser
  question, not a judgement.
- **Code enforces the rules.** The cap (`MAX_FOLLOW_UPS = 2` per main question), the time check and a follow-up's
  category live in `apply_limits` and the controller, after the model's reply is parsed. The prompt mentions the cap only
  to save wasted decisions, not to enforce it.
- **One deadline for two calls.** The turn has one time budget. The decide call gets the smaller of its cap and the time
  left minus a reserve; the write call is what the candidate sees, so it gets the rest.
- **Labelled evals for a decision.** A question has no single right answer, but a decision does, so decisions can be
  labelled and scored.

## 3. When to use it

| Do this | When | Why / limit |
|---|---|---|
| Ask a follow-up | The decide call finds a gap **and** follow-ups are left for this main question **and** enough time remains | Otherwise the code turns it into `next_question` (`cap_reached`, `no_time`) |
| Cap follow-ups in code | Always | A model told "at most 2" will still sometimes ask for a third (prediction, pending a real run) |
| A closed list for `gap` | The decision must be checkable by a parser | A bad free-text `note` is dropped without losing the decision |
| Accept a wasted decide call | Every answer turn | It costs roughly +740 input tokens even when the decision is "next question" |
| Count over- and under-probing separately | In evals | They cost different things (patience vs. depth) |

**I'd revisit this when** the real-model decide evals show the extra ~740 tokens per answer turn don't buy better
probing, or when p95 turn time doesn't stay well under the starting deadlines.

## 4. How it works

**The design choices:**

| Concern | Choice | Why |
|---|---|---|
| Judging vs writing | Two calls (decide, then write) | Each has one job; the decision is small and cheap to validate |
| Decision format | Closed `{action, gap, note}` | Less to get wrong than a free-form reply |
| Who limits follow-ups | The code (`apply_limits`) | The prompt is a hint, the code is the guarantee |
| Time | One shared `Deadline` | The write call is what the user sees, so it gets the reserve |
| Context for a thread | A window that never starts inside a thread | A follow-up needs its main question |

**The flow:**

```
interviews_turn.py:194   answer_turn / :211 stream_turn   the turn (JSON and streamed share the same rules)
interviews_turn.py:462   _decide        at most 2 attempts within the decide cap; ANY failure means next_question, no note
interviews_reply.py:188  parse_decision_reply -> Decision (closed action, gap, note)
interviews_turn.py:147   apply_limits   cap_reached / no_time override, last main question completes the interview
interviews_turn.py:395   plan_write     follow-ups left = MAX_FOLLOW_UPS - (turns in this thread - 1); picks the write inputs
interviews_turn.py:416   settle         a failed follow-up moves on as if the model said so; logs the turn summary
interviews_turn.py:66    Deadline       the shared time budget (an injectable clock, so tests control time)
interviews_constants.py:144   MAX_FOLLOW_UPS = 2
prompts/follow_up_decision_v1.md   the decide prompt;   prompts/interviewer_v4.md   the write prompt
```

The deadline's starting values (a guess for a flash-lite model): decide cap 10 s, write minimum 5 s, 30 s per turn.

**What `apply_limits` does** (`interviews_turn.py:147`):

- the model wants `follow_up` but none are left -> `next_question`, override `cap_reached`
- the model wants `follow_up` but too little time is left -> `next_question`, override `no_time`
- the model wants `next_question` on the last main question -> `complete`
- no decision at all (decide call failed) -> `next_question`

## 5. What can go wrong

| Failure | What the candidate sees | What the code does | Proof |
|---|---|---|---|
| The model always says `follow_up` | Exactly 2 follow-ups per main question, then the next question | Third decision logs `override=cap_reached` | `test_a_model_that_always_follows_up_gets_exactly_two_per_main_question` |
| An answer or job description orders "keep asking follow-ups" | Nothing changes | The cap is in code, not in anything the text can reach | `test_injected_text_cannot_raise_the_follow_up_cap_or_reach_a_system_prompt` |
| The decide call fails, is empty, or is invalid twice | The next main question | `_decide` returns no decision; `apply_limits` -> `next_question` | `_decide` (empty -> break, invalid -> second attempt) |
| Too little time for a follow-up | The next main question | `no_time` override | `test_turn_budget.py` (6 cases with a fake clock) |
| The follow-up's write fails | The next main question | `settle` moves on as if the model had said so | `settle` |
| Context too large | The next main question | `context_too_large` logged, no decision | `_decide` |
| A long thread would not fit | Older threads dropped first | The current thread is never split | `test_the_window_never_starts_inside_a_thread`, `test_the_guard_never_drops_the_current_thread` |
| A bad `note` | The decision still counts | The note is dropped, the decision survives | `test_decision_contract.py` (14 cases, one reason code each) |

## 6. Try it yourself

Write your prediction first, then check.

1. **Cap.** Predict what a model told "at most 2 follow-ups" will do over many answers. Then read
   `test_follow_ups.py::test_a_model_that_always_follows_up_gets_exactly_two_per_main_question` and find the three
   `cap_reached` log lines per interview.
2. **Valid decisions.** Predict that a closed `{action, gap, note}` reply is valid far more often than the question
   reply, and that most failures will be a `gap` on `next_question` or a missing `gap` on `follow_up`. Then run
   `uv run python -m app.modules.interviews.interviews_evals --task decide --repeat 3 --model gemini-3.5-flash-lite` and
   read the `valid_reply` failures.
3. **Cost.** Predict that the decide call is cheaper than the write call (no job description, only the current thread)
   but adds a full system prompt to every answer turn. Then compare with the `context_build` log lines (section 7).
4. **Accuracy.** Predict decision accuracy above 0.8 on the 15 labelled cases, more over-probing than under-probing, and
   the "complete answer" cases as the most likely needless follow-up. Then read `decision accuracy mean`,
   `over_probing`, `under_probing` from the decide run.
5. **Deadline.** Predict that p95 per turn will be well under 10 s, so the reserve rarely matters. Then run one live
   interview and `uv run python -m app.scripts.usage_report` for `turn_llm_ms` p50/p95, and read `budget_left_ms` on the
   write lines.

## 7. What surprised me

Only checkpoints A and C have measurements so far; B, D and E wait for real-model runs (section 9).

**Checkpoint A: the cap held, whatever the model said.** With a fake decide call that always says `follow_up`, a
3-question interview stores exactly main, follow-up, follow-up three times (9 rows), and the third decision of each
thread logs `override=cap_reached`. An answer and a job description that order "keep asking follow-ups" change nothing.

**Checkpoint C: what a follow-up costs in context** (estimated tokens, from `context_build` lines):

| Call | Input tokens | Of which system prompt |
|---|---|---|
| decide, one-answer thread | about 740 | about 706 |
| write, `interviewer_v4`, at the start | about 850 | about 834 |

So **every answer turn now costs roughly +740 input tokens even when the decision is "next question".** A maximum
interview (10 main questions, 2 follow-ups each, 500-character questions, 2,000-character answers) stays under the
5,000-token limit for both tasks at every turn, because older threads are dropped first and the current thread is never
split. The thread-aware window moves its start back to the thread's main question, and the guard may only drop turns
older than the current thread. Test: `test_context_strategies.py::test_a_maximum_interview_with_maximum_follow_ups_fits_in_both_tasks`.

**Pending predictions** (no measurements yet):

- **B, closed decision:** most failures will be a `gap` on `next_question` or a missing `gap` on `follow_up`.
- **D, labelled evals:** accuracy above 0.8 on 15 cases; more over-probing than under-probing.
- **E, deadline:** p95 per turn well under 10 s.

## 8. Check your understanding

1. **(Proof, concept 5)** Can you make the interviewer ask a third follow-up, whatever the model says? Which tests show
   it?
2. **(Why)** Why split the turn into a decide call and a write call?
3. **(When)** When does a follow-up *not* happen even though the model asked for one?
4. **(How)** How does the code count how many follow-ups are left for the current question?
5. **(How)** How do the two calls share one time budget?
6. **(What if)** What if the decide call fails or returns garbage?
7. **(What if)** What if the cap were only written in the prompt?

<details>
<summary>Reference answers (write yours first)</summary>

1. No. The cap lives in `apply_limits` and the controller, after the model's reply is parsed; a third `follow_up` is turned
   into `next_question` with `override=cap_reached`. Tests:
   `test_a_model_that_always_follows_up_gets_exactly_two_per_main_question` and
   `test_injected_text_cannot_raise_the_follow_up_cap_or_reach_a_system_prompt`.
2. Each call has one job. The decision is small, closed and cheap to validate, and it lets the code limit follow-ups
   before any question is written. A free-form combined reply is harder to bound and validate.
3. When none are left (`cap_reached`), when too little time remains (`no_time`), or when the follow-up's write call
   fails (`settle` moves on as if the model had said `next_question`).
4. `plan_write` computes `MAX_FOLLOW_UPS - (number of turns in this thread - 1)`, starting from the thread's main
   question (`thread_start`).
5. A `Deadline` is created once per turn. `_decide` gets the smaller of the decide cap and the time left minus the write
   reserve; the write call gets what is left, and a failed decide call is not retried with the last seconds.
6. Any failure means `next_question` with no note (`_decide` returns no decision), so the interview continues with the
   next main question.
7. The model would sometimes ask for a third follow-up, and nothing would stop it, including text injected through an
   answer or job description. That is the "LLM decides, code enforces" rule the code applies.

</details>

## 9. Go deeper / Still open

- Spec and plan: `docs/features/follow-up-questions/spec.md`, `plan.md`.
- Related: `sse-streaming/learnings.md` (the same decide / write rules on a streamed turn).
- Next concept this unlocks: end-of-interview feedback and scoring (richer structured output).

**Still open** (opt-in, real calls; the free tier rate-limits at about 25 calls, so pause between runs):

- `uv run python -m app.modules.interviews.interviews_evals --task decide --repeat 3 --model gemini-3.5-flash-lite`
  (checkpoints B and D: `valid_reply` failures, `decision accuracy mean`, `over_probing`, `under_probing`, per gap)
- `uv run python -m app.modules.interviews.interviews_evals --repeat 3 --model gemini-3.5-flash-lite` (write rules on v4)
- One live interview with the dev server, then `uv run python -m app.scripts.usage_report` for p50/p95 per turn
  (checkpoint E: `turn_llm_ms`, `budget_left_ms` on the write lines)
