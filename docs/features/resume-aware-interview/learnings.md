# Learn: Résumé-aware interview (Slice 8d)

> Code complete and unit-tested. The real-model eval (Step 10) is yours to run; every number from it is marked
> **pending** below until you paste it in.

## 1. Why it exists
Since 8c a candidate can store a small, validated profile (skills, roles, projects), but no interview read it: two
candidates with the same role, level and job description got the same kind of questions. A real interviewer has read the
résumé and asks "in that payments project you listed, how did you make retries safe?". 8d lets a candidate opt in,
interview by interview, so main questions are angled at their own background while the job description keeps the topic.

It is also the first time candidate-written text steers the model on every turn. The free-text parts of the profile are
not grounding-checked, so they can carry instructions, and they are personal data sent to the provider. Most of this
slice is about doing that safely and measurably.

## 2. What it is
- An opt-in `use_profile` flag on each interview (request, session column, response).
- `interviewer_v8` / `interviewer_v8_json`: v7 plus a `<candidate_profile>` data block and its rules, used only for
  main-question writes of an interview that opted in and still has a profile.
- A second retrieval query at start (the profile's short items) merged by quota into the job description's notes.
- A three-arm eval (C = v7, D = v8 prompt only, E = v8 prompt and query) with a gain metric, guards and a noise margin.

## 3. When to use it
- Personalise a prompt with user data: fence it as data, neutralise tags, keep it out of the calls that don't need it,
  and redact the calls that carry it.
- Add a second signal to retrieval without letting it take over: a quota, not a blend.
- Claim a gain only against a baseline arm measured the same way, with the run-to-run spread as the margin.

## 4. How it works

### Decisions (and the alternative each one beat)
| Decision | Why | Rejected |
|---|---|---|
| Opt-in per interview, only the flag stored | DELETE really deletes; the user chooses each time whether résumé text goes to the provider | Snapshot on the session (keeps personal data after DELETE) |
| Read live each turn | A replace takes effect on the next question (one extra SELECT per turn) | Read once at start |
| New `interviewer_v8`, v7 untouched | Shipped prompts are never edited in place; old questions stay explained by their stored version, no-profile prompts stay byte-identical | Editing v7 |
| Profile only in main-question writes | Follow-ups and decide react to what was said; fewer calls carry résumé text | Profile everywhere |
| Quota merge (≤ 2 of 6 notes) | JD dominance by construction; each note traceable to its side; `RETRIEVAL_PROFILE_SLOTS = 0` turns it off | Weighted vector blend; concatenated text |
| Short items only in the query | They match note headings; less personal than summaries | Whole profile text |
| No organization or period in the prompt | Data minimisation; the question needs what they did, not where or when | All fields |
| Drop order history → profile → notes | Personalisation is the unproven part; the notes' depth guidance is measured (8a) | Notes before profile |
| Profile-carrying calls labelled `redact` | Same as 8c's extraction; Langfuse keeps tokens, latency, version | Full traces |

### One opted-in start, walked through the code
1. `POST /api/v1/interviews` with `"use_profile": true`. `InterviewCreateIn.use_profile` is `Field(default=False,
   strict=True)` (`app/modules/interviews/schemas/interviews_schema.py:122`): lax Pydantic would turn `"true"` and `1`
   into `True`, and for a consent-like switch the client should have to send a real boolean.
2. `InterviewsService.start` reads the profile **before** any trace, model or embedding call
   (`app/modules/interviews/services/interviews_service.py:125`) through `ProfileService.find_for_interview`
   (`app/modules/profile/services/profile_service.py:93`), never the profile repository (layer rule). None → 409
   `PROFILE_REQUIRED` (line 127): nothing created, nothing sent.
3. Retrieval gets `profile_query_text(profile)` (`interviews_service.py:155`; `interviews_profile_utils.py:48`).
   `RetrievalService._retrieve` embeds `[job description, profile items]` in **one** call
   (`interviews_retrieval_service.py:190`; Google's `batchEmbedContents` is one request), ranks each side, then
   `merge_note_rankings` (`interviews_knowledge_utils.py:102`) keeps JD notes first and adds at most 2 profile notes.
4. The first question: `WithInterviewData.build` (`app/modules/interviews/ai/interviews_context.py:294`) picks v8
   because a profile is present and this is a main question; `WindowLedger` renders `candidate_profile_block`
   (`interviews_profile_utils.py:12`) after the job description and any notes, every value tag-neutralised.
5. `write_trace_labels` (`interviews_context.py:514`) sees `counts["profile"] == 1` and adds `redact: True`, so Langfuse
   gets no prompt or reply text for this call.
6. Each answer turn: `prepare_answer` reads the profile again before the read transaction is released
   (`interviews_answer_service.py:202`). Deleted → no block, today's prompt; replaced → the new one.

### Why the gain metric excludes job-description items
A question that just follows the job description ("how would you use PostgreSQL here?") would look personalised if
"PostgreSQL" is also in the profile. `profile_only_items` (`tooling/interviews_profile_eval_metrics.py:46`) drops
every item the job description names, and the metric runs on C too, so the gain is D − C and E − C.

### Why the guard needs a noise margin
Two runs of the same arm differ. `guard_verdict` (`interviews_profile_eval_metrics.py:84`) fails D or E only when its
`skill_coverage` is below C's mean by more than C's own spread across repeats (max − min of the per-repeat means), and
refuses below 3 repeats, where there is no spread worth the name.

## 5. What can go wrong
| Risk | What it would look like | Test that proves it doesn't |
|---|---|---|
| `"true"` silently enables résumé sharing | 201 instead of 422 | `test_invalid_setup_is_422_and_creates_nothing[use-profile-string]` |
| No-profile prompts drift | Different prompts for every existing interview | `test_without_a_profile_every_prompt_is_byte_identical_to_before_v8` (28 golden hashes) |
| Profile text closes its block | `</candidate_profile>` in a summary escapes the fence | `test_a_fake_closing_tag_in_free_text_cannot_leave_the_block` |
| Another user's profile used | User B's prompt carries A's items | `test_each_interview_gets_only_its_owners_profile`, `test_another_users_profile_does_not_count` |
| Refused start still costs a call | LLM or embedder called before the 409 | `test_flag_on_without_a_stored_profile_is_409_and_nothing_is_created_or_sent` |
| DELETE ignored mid-interview | Next question still personalised | `test_profile_deleted_mid_interview_makes_later_questions_profile_free` |
| Résumé text in Langfuse | Prompt visible in the trace | `test_a_main_write_with_the_profile_is_redacted_but_keeps_its_metadata` |
| Profile in follow-ups/decide | Résumé text sent where it isn't needed | `test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile` |
| Profile pushes a question to the bank | `context_too_large` because of the block | `test_neither_block_can_make_the_input_too_large` |
| Profile takes over retrieval | More than 2 profile notes, or profile-led notes when the JD side is short | `test_a_short_job_description_side_never_lets_the_profile_take_over` |
| Start latency doubles | Two embedding requests | `test_with_a_profile_one_batched_call_embeds_both_and_the_quota_merges` |
| Gain inflated by shared items | "java" counted inside "javascript", JD skills counted | `test_profile_mentions_are_whole_profile_only_items` |

## 6. Try it yourself
1. Predict: a start with `"use_profile": true` for a user with no résumé. Answer: 409 `PROFILE_REQUIRED`, and
   `llm.fake.calls == []`.
2. Set `RETRIEVAL_PROFILE_SLOTS = 0` and predict what `test_zero_profile_slots_gives_the_job_description_ranking`
   shows: the same notes as without a profile (the query change switched off, the prompt change kept).
3. Run `uv run python -m app.modules.interviews.tooling.interviews_evals --task generation --arms C,D,E --repeat 1`
   and predict the guard lines. Answer: `refused`, because one repeat has no spread.

## 7. What surprised me
- The no-profile path could be proven byte-identical without a model: hashes of today's built messages, recorded before
  v8 existed, turned "AC13: no-profile prompts unchanged" into a unit test.
- Counting "notes added by the profile" after the merge is ambiguous (a note can sit in both rankings), so the merge
  returns the count itself.
- The eval's no-job-description case already existed (`near-empty-data-intern`, `complete-behavioral-junior`), so 8d
  added only the injection and mismatch setups.

### Eval log
| Date | Task / arms | What changed | Versions | Summary numbers | Failures (type) | Decision |
|---|---|---|---|---|---|---|
| **pending** | `generation --arms C,D,E --repeat 3` | 8d baseline | v7 / v8, slots 2 | **pending** | **pending** | **pending** |
| **pending** | `retrieval` | profile cases added | threshold 0.55 | JD recall@5 / MRR must equal the last run: **pending**; profile cases: **pending** | **pending** | **pending** |
| **pending** | `write` injection JD cases | closes job-url AC12 | v4 | **pending** | **pending** | **pending** |

## 8. Check your understanding
1. Why store only a boolean on the session instead of a copy of the profile?
2. Why is the profile dropped before the notes when the input is too large?
3. Why does the gain metric run on arm C, which never sees the profile?
4. What does `RETRIEVAL_PROFILE_SLOTS = 0` turn off, and what does it leave on?

<details><summary>Answers</summary>

1. A copy would outlive a profile DELETE. The live read costs one SELECT per turn.
2. The notes' depth guidance was measured in 8a; the personalisation is the unproven addition. Neither may ever cause a
   bank fallback, so both can go.
3. C can still mention profile items by chance (or through the job description); measuring C makes D − C the real gain.
4. The profile half of the retrieval query (E becomes D). The v8 prompt with the profile block stays.
</details>

## 9. Still open
- Step 10 real-model runs and their numbers (eval log above): **pending**, yours.
- Known limit (accepted): profile-derived question text is stored like any question and replayed in later traced
  calls; asked questions outlive a profile DELETE until the interview is deleted.
- Google AI Studio data terms for résumé text in prompts and embeddings, before real users.
- No-profile prompts still say "developer"; a later prompt bump fixes them.
