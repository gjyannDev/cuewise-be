# Implementation: Agentic Workflow v2

## Status
All 12 steps built. Structural checks and the EC audit pass. **Dry runs pending with the user** (Step 8 and Step 12 behavior). Not ready for PR until they're done.
Health Check: n/a for this run (it ran under the old implement skill, before the health check existed)

## Completed Steps
- [x] 1. Back up the originals to `~/.claude/skills-backup/2026-11-15/` (feature 2/2 files, create-plan 3/3, implement 4/4, each SKILL.md present)
- [x] 2. create-plan: gate commands, coverage check and health check
- [x] 3. Create debug/SKILL.md
- [x] 4. Create review-feature/SKILL.md
- [x] 5. implement/SKILL.md: gated loop, debug handoff and health check
- [x] 6. implement references: routing file and task template
- [x] 7. feature: health check, and the grilling fix (feature, create-plan and both routing files)
- [~] 8. Milestone A check and dry run. Structural checks pass. Dry run **pending**. The user chose to continue to Milestone B before running it.
- [x] 9. feature: problem confirmation
- [x] 10. create-plan: approaches, self-contained steps and the checkpoint field
- [x] 11. implement: ponytail every step, caveman lite and checkpoints
- [~] 12. Final audit and learnings. Structural checks and the EC audit pass, and learnings.md is updated. Dry run B **pending**.

## Current Step
### Dry runs (needs the user)
**Milestone A (AC12, AC19, EC1):**
1. Pick a small Cuewise feature and run `/implement` on it for at least one step, and confirm the gate commands run after the step.
2. Force a failing step (for example a deliberately wrong assertion in a scratch test) and confirm that attempt 2 hands off to `/debug`.
3. Run `/review-feature` and confirm a Review section is written and no code changes before you select fixes.
4. Rename `~/.claude/skills/ponytail` temporarily, and confirm a one-line `missing:` warning appears. Then rename `implement/references/task-template.md` temporarily, and confirm implement stops before doing any work. Restore both.

**Milestone B (AC20–AC23):**
5. Run `/feature` on a new idea, and confirm the problem restatement is asked before any grilling.
6. Run `/create-plan`, and confirm plan.md has Approaches Considered, files and a verification command per step, and a checkpoint interval.
7. Run `/implement`, and confirm caveman lite in chat (full prose for failures and explanations), normal mode at the end, and a pause at the checkpoint for a large plan.

## Changes Made
No commits (the user commits). Every skill edit is outside this repo, in `~/.claude/skills/`:
- New: `debug/SKILL.md`, `review-feature/SKILL.md`
- Edited:
  - `feature/SKILL.md` (Dependencies, health check, grilling, problem confirmation)
  - `create-plan/SKILL.md` (Dependencies, health check, gate commands, coverage check, grilling, Approaches Considered, self-contained steps, checkpoint interval)
  - `create-plan/references/plan-template.md` (Gate commands line, Approaches Considered section, checkpoint interval and per-step Files/Verify format, Ready checklist, grilling)
  - `create-plan/references/capability-routing.md` (grilling)
  - `implement/SKILL.md` (Dependencies, health check, gate commands, debug handoff, verification evidence, ponytail every step, step 3a checkpoints, caveman lite Chat Style, normal mode at finalize, Notes)
  - `implement/references/capability-routing.md` (debug and review-feature replace review-implementation; grilling; ponytail every step; caveman lite)
  - `implement/references/task-template.md` (Health Check line, Debug Log, Review, checklist items)
- In this repo: `docs/features/agentic-workflow/{spec,plan,task,learnings}.md`

## Test Results
Final structural checks (Select-String, 2026-11-15): **43 pass, 0 fail**. They cover every grep check from plan Steps 2–11, plus `(?i)cuewise` with 0 matches across all 5 workflow skills (AC11).
- AC1/AC3: `debug` and `review-feature` appeared in the session's available-skills list right after they were created, so no new session was needed.
- AC13: the `create-plan` description in the skills list now names `grilling`.

**AC10 EC audit:** each edge case maps to the line that covers it (paths under `~/.claude/skills/`, line numbers as of 2026-11-15).
| EC | Covered at | EC | Covered at |
|----|-----------|----|-----------|
| EC1 | implement/SKILL.md:63 | EC15 | implement/SKILL.md:112 |
| EC2 | debug/SKILL.md:3, :35 | EC16 | implement/SKILL.md:49 |
| EC3 | debug/SKILL.md:38 | EC17 | implement/SKILL.md:22 |
| EC4 | debug/SKILL.md:43 | EC18 | feature/SKILL.md:15 |
| EC5 | implement/SKILL.md:59 | EC19 | implement/SKILL.md:112 |
| EC6 | implement/SKILL.md:58 | EC20 | implement/SKILL.md:115 |
| EC7 | debug/SKILL.md:61 | EC21 | implement/SKILL.md:30 (same in every phase's step 0) |
| EC8 | review-feature/SKILL.md:35 | EC22 | implement/SKILL.md:29 |
| EC9 | review-feature/SKILL.md:26 | EC23 | implement/SKILL.md:27 |
| EC10 | review-feature/SKILL.md:27 | EC24 | feature/SKILL.md:49 |
| EC11 | review-feature/SKILL.md:43 | EC25 | create-plan/SKILL.md:46 |
| EC12 | review-feature/SKILL.md:58 | EC26 | create-plan/SKILL.md:47 |
| EC13 | review-feature/SKILL.md:54 | EC27 | implement/SKILL.md:73 |
| EC14 | create-plan/SKILL.md:60 | EC28 | implement/SKILL.md:43 |

## Tests Pending
- Milestone A dry run: AC12, AC19, EC1 (see Current Step 1–4)
- Milestone B dry run: AC20–AC23 (see Current Step 5–7)

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 3, 4 | new skills listed as available | spec | AC1, AC3 | pass |
| T2 | 2–7 | structural grep checks | spec | AC2, AC4–AC9, AC11, AC13, AC16–AC18 | pass |
| T3 | 8 | gate commands run, review writes task.md | spec | AC12 | pending |
| T4 | 8 | hidden optional skill warns, missing required file stops | spec | AC19, EC21, EC22 | pending |
| T5 | 8 | attempt 2 failure hands off to debug | spec | EC1 | pending |
| T6 | 12 | every EC maps to a covering skill line | spec | AC10 | pass |
| T7 | 9–11 | Milestone B structural greps | spec | AC14, AC15, AC20–AC23 (text) | pass |
| T8 | 12 | restatement, approaches, checkpoints and caveman behave in a real run | spec | AC20–AC23 | pending |

## Open Questions
- none

## Baseline Failures
- n/a (no project code changes)

## Known Issues
- The first EC audit reported EC18 and EC24 as missing. The cause was in the audit script: PowerShell variable names ignore case, so the loop variable `$f` overwrote `$F` (the feature path). With the path written out, both were found. The skill text was fine.
- Line numbers in the EC audit go stale as the skills are edited. They're a record of this audit, not permanent references.

## Deviations from Plan
- None beyond the plan's own AC13 move into Milestone A. Step 8's "start a new session" wasn't needed, because the new skills were listed straight away.
- The Milestone A checkpoint was passed before the Milestone A dry run, at the user's request. Both dry runs are now pending together.

## Debug Log
- none

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 0 | graphify | `graphify query` on workflow/skills: hits only existing docs/features plans and tasks, so no app code is affected (as the plan says) |
| 1–7 | native Read/Edit | skill files are outside the repo root, where lean-ctx refuses paths |
| 8 | lean-ctx (ctx_shell) | graphify update |

## Links
- Spec: docs/features/agentic-workflow/spec.md
- Plan: docs/features/agentic-workflow/plan.md
- Backup: ~/.claude/skills-backup/2026-11-15/ (rollback: copy the folders back)
