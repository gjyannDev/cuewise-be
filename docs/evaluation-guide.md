# How to evaluate an AI feature: from the command to the fix

A practical guide for every Cuewise eval: the interviewer's question writing (`write`), the streamed turn (`stream`),
the follow-up decision (`decide`) and the end-of-interview feedback (`feedback`). Use it again for any AI feature you
add later (section 10).

An eval run is only useful if each failure leads to a decision. The loop is the same for every task:

```
 predict ─► run ─► read ─► triage ─► diagnose ─► fix (smallest, right place) ─► re-run ─► record
    ▲                                                                                       │
    └───────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Know what each task measures

Every task runs real model calls on fixed, synthetic cases and checks the replies **with code**. The checks differ
because the answers differ: a question has no single right text, a decision has one right answer, and a score has a
right *range*.

| Task | What it tests | Cases | How a case is judged | Key numbers |
|---|---|---|---|---|
| `write` | The interviewer's next question (`interviewer_v4`, JSON) | `data/eval_cases.json` (19) | **Rules** with no expected answer: `valid_reply`, `no_judgement`, `question_only`, `injection_ignored`, `note` | pass rate, `finish=length`, tokens |
| `stream` | The same cases through the streamed call (`interviewer_v5`) | same 19 | The same rules as `write`, so v4 and v5 compare on one table | pass rate, **time to first token** |
| `decide` | Follow up or move on, and which gap | the 15 labelled cases in `eval_cases.json` | **Labels** (`expect`): `decision`, `gap`, `valid_reply`, `injection_ignored` | accuracy, **over-probing**, **under-probing**, per-gap |
| `feedback` | Rubric scores, verified quotes, written feedback | `data/feedback_eval_cases.json` (10) | **Bands** (`expect_overall`, `expect_criteria`), plus `quotes_verified`, `write_valid`, `insufficient`, and `level_gap` for a case paired with an earlier one at a lower level (`lower_than`) | overall in band, valid replies, quotes rejected, template texts, **spread** |

Rules can't judge quality. `write` and `stream` print a `review:` line for long-history cases: read those replies
yourself, because no check can tell whether a question is *good*.

---

## 2. Before you run

| Check | Why |
|---|---|
| `.env` has a working LLM key, plus Langfuse keys if you want traces | Without Langfuse you only have the console. That shows *what* failed, not always *why* |
| You picked one task and one question to answer | e.g. "does v5 stream as well as v4 writes?" or "does the senior score drop?" |
| You estimated the calls | Free tiers allow about 25 calls a minute. A burst over that gives `LLMRateLimitError`, which says nothing about quality |
| You wrote a prediction | One line, e.g. "decide accuracy stays at or above 13/15". A run you didn't predict teaches you less |

**Calls per run (one repeat)**

| Task | Calls per case | One run |
|---|---|---|
| `write`, `stream` | 1, plus 1 to summarize a job description longer than `SUMMARY_THRESHOLD` (with `--summary on`) | about 19-25 |
| `decide` | 1 | about 15 |
| `feedback` | 2 (score + write), plus 1 per retry. The near-empty case is decided by code, with no call | about 18-22 |

`--repeat N` multiplies everything by N. On the free tier, keep `N` at 2 or 3 until the runner can pause between calls
(section 9).

---

## 3. Run

```bash
uv run python -m app.modules.interviews.tooling.interviews_evals --task <write|decide|stream|feedback> --model gemini-3.5-flash-lite [--repeat N]
```

| Flag | What it does | Applies to |
|---|---|---|
| `--task` | Which task. Default `write` | all |
| `--model` | Overrides the primary provider's model for this run. Keep it the same when you compare runs | all |
| `--repeat N` | Runs every case N times and reports the pass rate's mean, min and max. `feedback` also reports the score **spread** | all |
| `--reasoning-effort` | Reasoning effort for models that support it | all |
| `--prompt <version>` | Swaps the **interviewer** prompt for the chosen strategy | **`write` only** |
| `--strategy` | `window_ledger` or `full_history` | `write` only |
| `--notes on/off`, `--summary on/off` | Ablations: the running note, and the job description summary | `write`, `stream` |

**Trying a new prompt for another task.** `--prompt` doesn't reach `decide`, `stream` or `feedback` yet. Point the
task's constant in `app/modules/interviews/constants/interviews_constants.py` at the new file for the run, then point it back:

| Task | Constant |
|---|---|
| `decide` | `DECISION_PROMPT_VERSION` |
| `stream` | `INTERVIEWER_V5_PROMPT_VERSION` |
| `feedback` | `FEEDBACK_SCORE_PROMPT_VERSION`, `FEEDBACK_WRITE_PROMPT_VERSION` |

With Langfuse keys set, the run ends with `Langfuse session: <task>/<prompt>/<strategy>/<model>/<effort>/<time>`. Each
case is one trace in that session (environment `eval`), and every trace has the tags `task:`, `prompt:`, `strategy:`,
`model:` and `effort:`. The cases are mirrored into the datasets `interviews-eval/write` (shared with `stream`),
`interviews-eval/decide` and `interviews-eval/feedback`.

---

## 4. Read the output

**A case.** All tasks print the same first line:

```
PASS|FAIL  <case id>   <failed checks with their detail, or the error>
```

| Task | Line 2 and beyond | Hints in the console? |
|---|---|---|
| `write`, `stream` | `tokens=in/out cached reasoning latency_ms finish` (`stream` adds `first_token_ms`), then `reply='...'` and, for long cases, `review:` | No: hints are in the Langfuse trace output |
| `decide` | The same, with the reply | No: Langfuse trace output (over- or under-probing, injection) |
| `feedback` | `overall insufficient text quotes_rejected tokens latency_ms`, then a `hint:` line per failure | Yes |

**The summary.**

| Number | Tasks | Healthy | If not |
|---|---|---|---|
| `passed x/y`, `pass rate mean/min/max` | all | Stable across repeats | A wide min-max means the result is noise: add repeats before you act |
| `failed checks: {...}` | all | `none` | Shows which rule breaks most. Start there |
| `finish=length` | all | 0 | `max_tokens` is too low (or the reasoning effort too high). Fix this **before** judging quality |
| `decision accuracy`, `over_probing`, `under_probing`, `per gap` | `decide` | High accuracy, both errors low | Over-probing wastes the candidate's time. Under-probing leaves a vague answer unexplored. Fix them separately |
| `avg first token` | `stream` | Lower than `write`'s full latency | The streamed format adds delay before the question |
| `valid replies`, `quotes rejected`, `template texts` | `feedback` | total, 0, 0 | The contract breaks, or a provider error forced the template |
| `overall in band`, `criterion spread` | `feedback` | all in band, spread at most 1 | The judgement is off, or it isn't repeatable |
| tokens, cached, latency | all | Steady between runs | A change that doubles them needs a reason |

---

## 5. Triage: what kind of failure is it?

Sort **every** failure into one of these four types before touching anything. The type decides where the fix goes.

| Type | How it shows | Examples | Fix goes in |
|---|---|---|---|
| **Infrastructure** | `ERROR: LLMRateLimitError`, `LLMTimeoutError`, `no_time`; `context_too_large`; a feedback template caused by one of these | A case late in a burst gets rate-limited | The runner or the limits, never the prompt |
| **Contract** | `valid_reply` fails, `invalid_reply:<code>`, `finish=length`, `note` missing, quotes rejected | A malformed JSON reply; a quote over 200 characters | Prompt wording, `max_tokens`, or the code's rule if the rule is wrong |
| **Quality** | The reply is valid but a behaviour check or label fails | `no_judgement`, `question_only`, `injection_ignored`, a wrong `decision`, a score out of band | Prompt, rubric, or gap definitions |
| **Label** | The model is right and the case expected the wrong thing | Two gaps both fit the answer; you read the answer and agree with the score | The case file |

**Two rules:**

1. **A single failure isn't a finding yet.** If it passed last run and failed this one, re-run it (`--repeat`). Act on
   what repeats. Exception: a failure on *both* attempts within one run is already a pattern.
2. **Keep infrastructure out of quality numbers.** A rate-limited case doesn't mean the prompt got worse. Re-run it
   before you count it.

---

## 6. Diagnose in Langfuse

Filter on environment `eval`, open the session from the run's last line, and open the trace `<task>: <case id>`. The
trace **output** holds the verdict, the reply, what was expected and the **hints**. Read those first.

**`write`, `stream`, `decide`:**

```
write: vague-answer-backend                trace: input = kind, last question and answer (and the job description)
│                                          output = verdict, reply, decided vs expected (decide), hints, notes
├── llm-call                               the job description summary (only for a long job description, --summary on)
└── llm-call                               the exact prompt and reply, tokens, finish reason
scores: one boolean per check, case_passed (+ over_probing / under_probing for decide)
```

**`feedback`** has more structure, because one case runs two calls with checks in between:

```
feedback: same-answer-senior               output = verdict, overall vs expected band, scores, hints
├── score                                  chain: outcome, attempts, quotes_rejected, scores (or hint)
│   ├── feedback_score (attempt 1)         the exact prompt and reply
│   ├── check-score-reply                  guardrail: passed, verdict (reason code), hint
│   └── feedback_score (attempt 2)         only after a rejection
└── write                                  chain: outcome, text_source
    ├── feedback_write (attempt 1)
    └── check-write-reply
```

| Failure | Look at | Ask |
|---|---|---|
| `valid_reply` / `invalid_reply:<code>` | The generation's reply (and `check-*-reply` for feedback) | Which part broke the format, and is the prompt clear about it? |
| `no_judgement`, `question_only` | The check's detail (the matched words) and the reply | Does the prompt forbid this, with an example? |
| `injection_ignored` | The reply against the case's `marker` | Which part of the input carried the instruction, and is it fenced as data? |
| `decision` wrong | `decided` vs `expected` and the hint (over or under) | Which prompt rule covers this kind of answer? |
| `gap` wrong | The answer, then both gap definitions | Do both gaps fit? If yes, it's a label or definition problem |
| A band or criterion fails (feedback) | The `score` step's per-criterion scores | Which criteria are off? Compare them with the rubric anchors and the level line |
| `finish=length` | The generation's token counts | Is the reply too long, or is reasoning eating the budget? |
| A cost or latency jump | `prompt_tokens`, `cached_tokens` | Did the prompt grow, or did a change break the cached prefix? |

To compare runs, filter traces by a tag (e.g. `prompt:interviewer_v5`) and group by score name (`case_passed`,
`over_probing`, `overall_in_band`, ...). Score names never change between runs, so they always line up.

**Write down the cause in one sentence before fixing it**, e.g. "the model follows up on complete answers that mention
a tool, because the prompt's 'missing detail' gap is too broad". If you can't write the sentence, you haven't diagnosed
it yet.

---

## 7. Fix: the smallest change in the right place

Try these in order. The cheapest and most reliable comes first:

1. **The case**: the label is wrong. Change it and write *why* in the case's `notes`.
2. **Code**: a rule can decide it (lengths, ranges, counts, a pre-check, a computed total). Code is deterministic and
   free.
3. **Prompt**: the model needs a clearer rule or an example.
4. **Reference data**: the standard itself is unclear (the feedback rubric, the decide gap definitions).
5. **Model or settings**: temperature, `max_tokens`, reasoning effort, a different model. Only if nothing above works.

**Rules for every change**

- **Prompts and rubrics are versioned, never edited in place.** Copy `interviewer_v4.md` to `interviewer_v6.md` (or
  `follow_up_decision_v2.md`, `feedback_score_v2.md`), change the copy, and point the constant at it. Stored data and
  traces record which version produced them, and you need the old version to compare against.
- **One change per experiment.** Change two things at once, and you won't know which one helped or which one broke
  something else.
- **Never loosen a check, delete a case or widen a label just to get a pass.** Only change a label if you would defend
  the new one without seeing this run's number.
- **A new failure mode gets a new case.** If the run found a behaviour the cases didn't cover, add a case that shows it,
  so it stays fixed.
- **Run the unit tests after the change** (`uv run pytest tests/modules/interviews`). They check prompt structure,
  parsing and the eval checks themselves, not quality.

---

## 8. Re-run to prove it, then document it

**Step 1: the cases that failed, with repeats.** This answers "did the fix work?".

**Step 2: the whole task.** This answers "did anything else get worse?". Prompts are shared: a rule that fixes
over-probing can cause under-probing, and a stricter rubric can lower everyone's scores.

**Keep the change when:**

- [ ] The targeted cases pass in every repeat, not just once.
- [ ] The other cases didn't get worse beyond the run-to-run noise (compare the min-max pass rate or the spread).
- [ ] Valid replies didn't drop, and `finish=length` didn't rise.
- [ ] Tokens, cached tokens and latency didn't grow without a reason.
- [ ] The opposite error didn't grow. `decide`: over-probing went down and under-probing didn't go up. `feedback`: the
      senior score dropped and the junior one didn't.

If it fails, point the constant back at the old version and return to section 6 with what you learned.

### Document it

Four kinds of information, each in its own place:

| What | Where | Written by |
|---|---|---|
| Raw results: every call, reply and score | Langfuse: one session per run, one trace per case | Automatic |
| The run: what changed, the totals, the decision | The **eval log** in the feature's `learnings.md`, section 7: one row per run | You, after each run |
| Why a label, prompt or rubric changed | Next to the change: the case's `notes`, the comment on the version constant, the commit message, and `task.md` under Deviations from Plan | You, when you change it |
| What you learned | `learnings.md`, section 7: predictions against results, surprises | You, when something surprises you |

Langfuse holds the raw results but not the reasoning: it can show you a score of 3.6 later, not that the 3.6 proved the
label wrong.

**An eval log row:**

| # | Run (UTC) | What changed | Prompt | Pass | Errors | Quotes rejected | Templates | Tokens in / out | Failures → type | Decision |
|---|---|---|---|---|---|---|---|---|---|---|
| 7 | 11-06 05:31 | Score prompt v2: one-sentence quotes | v2 | 7/10 | 1 | 1 | 1 | 19,396 / 4,409 | injection `quote_not_found` ×1, recovered → contract, noise; follow-up 429 → infra | Mixed fixed; repeat v2 |

The numeric columns are the task's own summary numbers. `decide` would log accuracy, over-probing and under-probing
instead; `stream` would log the time to first token.

**Rules:**

- **One change per row.** If you can't say in one sentence what changed, you changed too much.
- **"None" is a valid change.** A re-run with nothing changed is how you learn which failures repeat.
- **Always write the decision:** keep, revert, pending, or not counted (infrastructure). It's the most valuable column.
- **Real numbers only.** Copy them from the summary line, or read them back from the Langfuse session. Write "—" for
  anything you didn't measure.
- **Keep the session time** in the Run column, so you can find the traces behind the row.

**After each run (about two minutes):**

1. Copy the summary line into the row.
2. Triage each failure with the checklist, then fill in the Failures column.
3. Write the decision.
4. If you changed a label, prompt or rubric, put the reason in its notes, comment and commit too.
5. If something surprised you, add one bullet under the log.

---

## Checklist for one failure

Copy this for each failing case and fill it in, top to bottom. Don't skip ahead to the fix.

```
Case:            <id>          Task: <task>          Run: <Langfuse session>
1. Type:         infrastructure / contract / quality / label        (section 5)
2. Repeats?      seen in earlier runs? failed on every attempt?     (once only → re-run first)
3. The rule:     where the code raises it (search the reason code) and its exact limit
4. Evidence:     the trace step → the check → the generation; the exact value that broke the rule
5. Cause:        one sentence
6. Fix:          the first level that applies: case → code → prompt (new version) → reference data → model
7. Proof:        failing case with --repeat, then the whole task; keep / revert
8. Recorded:     a row in the feature's eval log (learnings.md, section 7)
```

---

## 9. Worked example: feedback, run 2 (2026-11-05)

Measured with `--task feedback --model gemini-3.5-flash-lite`: 7/10 passed, 8/10 valid replies, 20,510 tokens in and
4,648 out, about 4.5 s per case.

| Failure | Type | Seen before? | Cause to confirm in Langfuse | Planned fix |
|---|---|---|---|---|
| `follow-up-completes-the-story`: `LLMRateLimitError` | Infrastructure | Yes, same position (last in a burst) | Not needed | Runner: a pause between calls |
| `mixed-strong-and-weak`: `invalid_reply:quote_length` on both attempts | Contract | No, it passed in run 1 | `check-score-reply` and the generation: which quote, and how long | Prompt v2: "one sentence or part of one, 10-200 characters, never a single word". Code: tell the retry *why* the first reply failed (the reason code only) |
| `same-answer-senior`: 4.4, expected 2-3.5 | Quality, or Label | Yes, 4.1 in run 1 | Compare the per-criterion scores with the junior trace | If 4.4 is unfair: a prompt v2 rule, "an experienced candidate who only meets the early-career expectation scores at most 3 on that criterion". If it's fair: change the band |
| `voice-transcript` write call: `length`, then the retry passed | Contract, recovered | Similar (`count` in run 1) | Not needed yet | Watch: act if it starts producing templates |

Then: re-run `mixed`, `junior` and `senior` with `--repeat 2`, then the whole task, and check against section 8.

**Gaps in the runner today** (planned, not built):

- `--cases <ids>`: run only some cases. Today every case runs.
- `--pause <seconds>`: wait between calls, so free-tier runs don't hit rate limits.
- `--score-only` (feedback): skip the write call while tuning scores (halves the calls).
- `--prompt` for `decide`, `stream` and `feedback`. Until then, switch the constant by hand (section 3).
- Hints in the console for `write`, `stream` and `decide`. Today they're in the Langfuse trace output only.

---

## 10. Adding an eval for a new AI feature

Build the eval together with the feature, so prompt and model changes can be compared instead of guessed.

1. **Decide what "good" means, in checkable terms.** Is there one right answer (a label, like `decide`), a right range
   (a band, like `feedback`), or only rules (like `write`)? Use the strictest one that is honest.
2. **Write 6-12 synthetic cases.** Include strong, weak, near-empty, injection in every untrusted input, the longest
   realistic input, and one pair that differs in a single variable (level, category). Never use real user data.
3. **Write the checks as code**, with stable names and a `detail` that says what was wrong. Unit-test them with a fake
   provider, so `uv run pytest` never makes a real call.
4. **Add a hint per check** that says where to look first.
5. **Wire it into the runner** under its own `--task`: traces in environment `eval`, boolean scores per check, and the
   cases mirrored into a dataset `interviews-eval/<task>`.
6. **Run it once and record the baseline** as row 1 of the feature's eval log, before you change any prompt.

---

## Cheat sheet

```
predict ─► run ─► sort each failure: infra / contract / quality / label
                 ├─ seen once?  ─► re-run first
                 └─ repeats     ─► Langfuse: trace output (hints) ─► generation ─► one-sentence cause
                                   ─► fix: case → code → prompt (new version) → reference data → model, one at a time
                                   ─► re-run the failing cases (repeats) ─► re-run the whole task ─► keep or revert
                                   ─► learnings.md
```
