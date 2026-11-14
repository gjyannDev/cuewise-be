# How to evaluate an AI feature: from the command to the fix

A practical guide for every Cuewise eval: the interviewer's question writing (`write`), the streamed turn (`stream`),
the follow-up decision (`decide`), the end-of-interview feedback (`feedback`), the knowledge-base retrieval
(`retrieval`) and the résumé profile (`profile`, its own runner). Use it again for any AI feature you add later
(section 10). Every task records each run as a Langfuse
*experiment run* you compare in the Langfuse UI (section 6a).

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
| `retrieval` | Whether the right reference note comes back for a job description | `data/retrieval_eval_cases.json` (21) | **Rank** of the labelled note, against a filter-only baseline | recall@5, MRR (vector vs filter), threshold sweep |
| `profile` (own runner, see below) | Résumé → candidate profile, through the real upload pipeline (read, scrub, extract, parse, ground) | `app/modules/profile/data/profile_eval_cases.json` (5 synthetic résumés, built into real PDF and DOCX files) | **Labels** (`expect`): the skills and role titles the résumé states, plus `forbidden` strings a hidden injection tries to add | skills precision, skills recall, title recall, role count, **injection ignored** |

The knowledge-base `generation` and `ranking` tasks are explained in `docs/features/knowledge-base-rag/`.

**Why `profile` has its own command.** Each eval lives in the module it tests. `--task` switches between the
interviews module's own steps; the résumé profile is its own module (`app/modules/profile/`), so its runner is
`app/modules/profile/tooling/profile_evals.py`. It shares the same Langfuse experiment helpers, flags and rules, so
its runs look and compare like every other task. See `docs/features/resume-upload/learnings.md`.

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
| `profile` | 1, plus 1 per retry | about 5-10 |

`--repeat N` multiplies everything by N. On the free tier, keep `N` at 2 or 3, and add `--pause-seconds 2.5` to space
the calls out (every task supports it).

---

## 3. Run

```bash
uv run python -m app.modules.interviews.tooling.interviews_evals --task <write|decide|stream|feedback> --model gemini-3.5-flash-lite [--repeat N]
uv run python -m app.modules.profile.tooling.profile_evals --model gemini-3.5-flash-lite [--repeat N]   # the résumé profile
```

| Flag | What it does | Applies to |
|---|---|---|
| `--task` | Which task. Default `write` | interviews runner |
| `--model` | Overrides the primary provider's model for this run. Keep it the same when you compare runs | all |
| `--repeat N` | Runs every case N times and reports the pass rate's mean, min and max. `feedback` also reports the score **spread** | all |
| `--reasoning-effort` | Reasoning effort for models that support it | interviews runner |
| `--prompt <version>` | Swaps the **interviewer** prompt for the chosen strategy | **`write` only** |
| `--strategy` | `window_ledger` or `full_history` | `write` only |
| `--notes on/off`, `--summary on/off` | Ablations: the running note, and the job description summary | `write`, `stream` |
| `--note "<why>"` | Why you are running this and what you expect. Saved as the Langfuse run's description, so the reason travels with the numbers (cut to 300 characters) | all |
| `--pause-seconds` | Wait between cases, and between repeats (free-tier limits). Default 2.5 for `retrieval` and `generation`, 0 for the others | all |
| `--arms C,D,E` | Which generation arms run (two or more of A-E). Default `A,B,C`. D and E add the résumé-aware arms and two generation-only setups (injection, mismatch) | `generation` only |

**Trying a new prompt for another task.** `--prompt` doesn't reach `decide`, `stream` or `feedback` yet. Point the
task's constant in `app/modules/interviews/constants/interviews_constants.py` at the new file for the run, then point it back:

| Task | Constant |
|---|---|
| `decide` | `DECISION_PROMPT_VERSION` |
| `stream` | `INTERVIEWER_V5_PROMPT_VERSION` |
| `feedback` | `FEEDBACK_SCORE_PROMPT_VERSION`, `FEEDBACK_WRITE_PROMPT_VERSION` |

With Langfuse keys set, each repeat is one **experiment run** (section 6a) and the run's last line reads
`Langfuse runs: <run name> (<link>); ...`; without keys, or when Langfuse fails, it says why nothing was recorded. The
console output is otherwise the same with and without keys. The cases are synced into the datasets
`interviews-eval/write` (shared with `stream`), `interviews-eval/decide`, `interviews-eval/feedback`,
`interviews-eval/retrieval` and `interviews-eval/generation` before each run; the profile cases into
`profile-eval/extract`.

---

## 4. Read the output

**A case.** All tasks print the same first line:

```
PASS|FAIL  <case id>   <failed checks with their detail, or the error>
```

| Task | Line 2 and beyond | Hints in the console? |
|---|---|---|
| `write`, `stream` | `tokens=in/out cached reasoning latency_ms finish` (`stream` adds `first_token_ms`), then `reply='...'` and, for long cases, `review:` | No: hints are in the case's output in Langfuse |
| `decide` | The same, with the reply | No: the case's output in Langfuse (over- or under-probing, injection) |
| `feedback` | `overall insufficient text quotes_rejected tokens latency_ms`, then a `hint:` line per failure | Yes |
| `profile` | `precision recall roles titles injection_ignored hidden_chars ungrounded` | No: the profile it produced is the case's output in Langfuse |

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
| `valid`, `skills_precision`, `skills_recall` | `profile` | 5, high, high | Precision low: the model adds skills the label lacks (check `ungrounded` too). Recall low: it misses stated skills, or the reader lost them (a column or hidden-text rule) |
| `title_recall`, `role_count_match` | `profile` | 1.0 | A title rewritten ("Sr. Engineer" for "Senior Backend Engineer") or a role merged or dropped |
| `injection_ignored` | `profile` | 1.0 | The hidden instruction reached the profile: check the reader dropped it (`hidden_chars` > 0), then the prompt |
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

Open the run from the last line's link (or **Experiments**, environment `sdk-experiment`, the task's dataset), then a
case's result. Its **output** holds the verdict, the reply, what was expected and the **hints**. Read those first. The
calls and steps under it are laid out as below (the result's own name comes from the SDK; the shape underneath is
ours).

**`write`, `stream`, `decide`:**

```
write:vague-answer-backend                 input = the case (setup, job description, history)
│                                          output = verdict, reply, decided vs expected (decide), hints, notes
├── llm-call                               the job description summary (only for a long job description, --summary on)
└── llm-call                               the exact prompt and reply, tokens, finish reason
scores: one boolean per check, case_passed (+ over_probing / under_probing for decide)
```

**`feedback`** has more structure, because one case runs two calls with checks in between:

```
feedback:same-answer-senior                output = verdict, overall vs expected band, scores, hints
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

## 6a. Compare experiment runs

Every task records each run as a Langfuse **experiment run**: one result per case, linked to the dataset's items, so
two runs line up case by case. You no longer save the console output and diff files to compare them.

**What every run carries**

- **A name that says what it tested**, then when: `<task>/<main prompt version or setting>/<model>/<local time>/r<n>`
  (generation adds `/arm-A|B|C|D|E`; retrieval uses `threshold-<t>/notes-<fingerprint>` instead of a prompt).
- **Metadata**: `task`, `commit` (`-dirty` with uncommitted changes, `unknown` without git), `model`, `prompt.*`,
  `repeat`, `flag.*`, `note`; retrieval and generation add `embedding_model`, `embedding_dimensions`, `threshold`,
  `notes_fingerprint` (changes when any ingested note changes); generation adds `arm`.
- **Description**: your `--note`.
- **`errored`** on every case: a rate limit or provider error counts as a failed case and is flagged, never dropped.

**Scores per task**

| Task | Dataset | Runs per command | Scores per case | Scores per run |
|---|---|---|---|---|
| `write` | `interviews-eval/write` | one per repeat | the checks, `case_passed`, `errored` | `pass_rate`, `errored_count`, `finish_length_count`, `avg_latency_ms` |
| `stream` | `interviews-eval/write` (shared) | one per repeat, `task=stream` | the same | the same + `avg_first_token_ms` |
| `decide` | `interviews-eval/decide` | one per repeat | the checks, `case_passed`, `over_probing`, `under_probing`, `errored` | `pass_rate`, `decision_accuracy`, `over_probing_count`, `under_probing_count`, `errored_count` |
| `feedback` | `interviews-eval/feedback` | one per repeat; cases in file order | `valid_reply`, the checks, `case_passed`, `errored`; `criterion_spread_max` on the last run when repeating | `pass_rate`, `valid_reply_rate`, `overall_in_band_rate`, `quotes_rejected_count`, `template_text_count`, `errored_count` |
| `retrieval` | `interviews-eval/retrieval` | one; `--repeat` is ignored | `vector_recall_at_5`, `vector_reciprocal_rank`, `filter_recall_at_5`, `filter_reciprocal_rank`, `errored` | `vector_recall_at_5`, `vector_mrr`, `filter_recall_at_5`, `filter_mrr`, `errored_count` |
| `generation` | `interviews-eval/generation` (one item per setup) | one per repeat **and arm** | `valid_share`, `distinct_competencies`, `skill_coverage` (when the setup lists skills), `prompt_tokens`, `start_ms`, `errored`; with a D or E arm also `profile_only_mention_share`, `presumption_flags`, `profile_notes`, and `injection_ignored` on the injection setup | the `_mean` of each, `errored_count`; with D or E, `profile_only_mention_share_mean`, `presumption_flags_total`, `profile_notes_mean`, `injection_ignored_mean` |
| `ranking` | (posts onto generation's results) | none | `human_rank` (1 = best); when rated, `human_fit`, `human_relevance`, `human_variety`, `human_specificity`, `human_score` | none |

The run scores are computed from the same summaries the console prints, so the two never disagree.

**Generation and the blind ranking.** `--task generation` writes three local files next to the sheet: the sheet, its
key, and `<sheet>.traces.json` (each setup and arm's Langfuse result). **Rank the sheet before opening the runs**: their
names and metadata say which arm is which. Under each set you may also fill `Rating: fit relevance variety specificity`
(four whole numbers 1 to 5; relevance `-` when the setup has no job description) and `Note: <one line>`. Then
`--task ranking` prints the tally and posts your rank (and ratings) onto each arm's result, with stable ids, so running
it again updates the scores instead of adding new ones. Ratings compare across runs (a 4 means the same in every run);
ranks only within one sheet.

**The résumé-aware arms (8d).** `--task generation --arms C,D,E --repeat 3` compares C (`interviewer_v7`, job-description
notes, no profile), D (`interviewer_v8` with the setup's synthetic profile from `data/generation_eval_profiles.json`,
the same notes: the prompt change alone) and E (v8 and the quota-merged notes: prompt and query). After the usual table
it prints a second one, computed for **every** arm, C included, against each setup's profile:
- `profile_only_mentions`: the share of main questions that name a profile item the job description does **not** also
  name (whole terms, case-insensitive). Shared items are left out, or following the job description would look
  personalised. The gain is D - C and E - C; no pass mark until there is a baseline.
- `presumption_flags`: questions matching a phrase such as "since you led" or "your résumé". Crude: read every hit by
  hand; repeated hits mean v8's "never as a verified fact" rule needs a new prompt version.
- `profile_notes`, `notes_overlap_vs_C` (Jaccard of chunk ids; below 1 means the profile query changed the notes) and
  `injection_ignored` (the injection setup's forbidden strings never appeared).
- `guard D` / `guard E`: pass when `skill_coverage` is not below C's mean by more than C's own spread across repeats
  (max - min of its per-repeat means: the run-to-run noise), and the injection was ignored every time. With fewer than
  3 repeats the guard says `refused`: one repeat has no spread to measure. If E fails a guard D passes, set
  `RETRIEVAL_PROFILE_SLOTS = 0` (the query change off, code kept) and record why.

The synthetic profiles are fake people; their eval traces keep full prompts (only the app's own profile calls are
redacted). `--task retrieval` also scores five `profile` cases (a profile's short items as the query) apart from the
job-description cases: the job-description `recall@5` / `MRR` must match the last run, and `profile cases` gives the
profile half its own baseline.

**Reading the runs list.** The name says what a run tested, so the baseline and the new run are told apart by name:
`decide/follow_up_decision_v1/...` against `decide/follow_up_decision_v2/...`. Score columns are listed in alphabetical
order. A boolean score shows as `false: n / true: m` (how many cases had each value); a run score shows as a number.

**How to compare**

1. Before you change anything, run the task once (with `--note "baseline"`). That run is your baseline.
2. Make one change and run again with a `--note` saying what changed and what you expect.
3. In Langfuse, open **Experiments** (the runs' environment is `sdk-experiment`, not `eval`), pick the dataset, select
   the baseline run and the new run, and compare.
4. Read the **metadata difference** first: it says what changed (prompt version, commit, notes fingerprint,
   threshold). If two things changed, the comparison can't tell you which one helped.
5. Read the run scores, then the per-case scores: which cases flipped, in which direction. Open a flipped case's trace
   to read the prompt and the reply.
6. Judge noise as in section 8: with N cases, one case changing moves a rate by 1 / N.
7. Write the eval log row with both run names and your decision.

A baseline is not stored anywhere in Langfuse: you choose it in the compare view and name it in the eval log row.
Without keys, or when Langfuse fails, the tasks run exactly as before and the last line says nothing was recorded.

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
| Raw results: every call, reply and score | Langfuse: one experiment run per repeat, one result per case | Automatic |
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
- **Real numbers only.** Copy them from the summary line, or read them back from the Langfuse run. Write "—" for
  anything you didn't measure.
- **Keep the run names** (baseline and new) in the Run column, so you can find the results behind the row (section
  6a).

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
Case:            <id>          Task: <task>          Run: <Langfuse run name>
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
- `--pause <seconds>`: wait between calls, so free-tier runs don't hit rate limits. `retrieval` and `generation` have
  `--pause-seconds`; the other tasks don't yet.
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
5. **Wire it into a runner** as an experiment run (`run_cases` in `tooling/interviews_eval_runs.py`): scores per
   check, run scores from the console's summary, and the cases mirrored into a dataset. A step of the interviews module
   becomes a new `--task` (dataset `interviews-eval/<task>`). A new module gets its own runner in its own
   `tooling/` folder that reuses the same helpers and flags (dataset `<module>-eval/<task>`), as
   `app/modules/profile/tooling/profile_evals.py` does: the eval stays with the code it tests.
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
