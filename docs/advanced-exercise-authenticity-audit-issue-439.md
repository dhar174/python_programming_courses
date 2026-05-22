# Advanced Exercise Authenticity Audit (Issue #439)

Date: 2026-05-21  
Scope: `Advanced/assignments/Advanced_Day*_homework.ipynb` + matching `criteria.json` files  
Runbook reference: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`

## Assignment → runbook mapping + exercise authenticity classification

| Assignment | Runbook session/hours | Per-hour classification |
|---|---|---|
| Day 1 | Session 1 (Hours 1–4) | H1 partial, H2 partial, H3 partial, H4 partial |
| Day 2 | Session 2 (Hours 5–8) | H5 partial, H6 partial, H7 partial, H8 partial |
| Day 3 | Session 3 (Hours 9–12) | H9 partial, H10 partial, H11 partial, H12 partial |
| Day 4 | Session 4 (Hours 13–16) | H13 partial, H14 partial, H15 aspirational, H16 partial |
| Day 5 | Session 5 (Hours 17–20) | H17 partial, H18 partial, H19 partial, H20 partial |
| Day 6 | Session 6 (Hours 21–24) | H21 partial, H22 partial, H23 partial, H24 partial |
| Day 7 | Session 7 (Hours 25–28) | H25 partial, H26 partial, H27 partial, H28 partial |
| Day 8 | Session 8 (Hours 29–32) | H29 partial, H30 partial, H31 partial, H32 partial |
| Day 9 | Session 9 (Hours 33–36) | H33 partial, H34 partial, H35 partial, H36 partial |
| Day 10 | Session 10 (Hours 37–40) | H37 real, H38 partial, H39 aspirational, H40 partial |
| Day 11 | Session 11 (Hours 41–44) | H41 partial, H42 partial, H43 partial, H44 partial |
| Day 12 | Session 12 (Hours 45–48) | H45 real, H46 real, H47 real, H48 aspirational |

Totals across 48 hour-exercises: **Real 4**, **Partial 41**, **Aspirational 3**

## Per-day authenticity metadata for learner-facing docs

Use this day-level label in learner-facing notebook headers. The hour-level audit above remains the source of truth for exact exercise nuance.

| Day | Authenticity | Hour-level note |
|---|---|---|
| Day 1 | partial | H1–H4 partial |
| Day 2 | partial | H5–H8 partial |
| Day 3 | partial | H9–H12 partial |
| Day 4 | aspirational | H13–H14 partial, H15 aspirational, H16 partial |
| Day 5 | partial | H17–H20 partial |
| Day 6 | partial | H21–H24 partial |
| Day 7 | partial | H25–H28 partial |
| Day 8 | partial | H29–H32 partial |
| Day 9 | partial | H33–H36 partial |
| Day 10 | aspirational | H37 real, H38 partial, H39 aspirational, H40 partial |
| Day 11 | partial | H41–H44 partial |
| Day 12 | aspirational | H45 real, H46 real, H47 real, H48 aspirational |

## Missing starter code / steps / success criteria

1. **Starter-code quality is inconsistent**
   - Day 2, Day 8, and Day 12 include heavily pre-solved code in primary homework notebooks, reducing authentic learner construction.
   - Other days rely on TODO prompts but do not specify minimum implementation shape.

2. **Steps are under-specified**
   - Most Part blocks provide Goal/Best practice/Pitfall, but no numbered implementation procedure or artifact checklist.

3. **Success criteria are externalized to output contracts**
   - Acceptance is mostly in `criteria.json` (`expected_stdout` string matching), not as in-notebook “Definition of Done.”
   - This enables output-contract completion without proving robust design/behavior.

## Weakest learner-facing exercises (with references)

1. **Day 4, Hour 15 (Capstone planning workshop)**  
   Files:
   - `Advanced/assignments/Advanced_Day4_homework.ipynb` (Part 3)
   - `Advanced/assignments/Advanced_Day4_homework/criteria.json` (Hour 15 expected output lines)  
   Problem: passes via narrative prints; no required plan artifact/rubric.

2. **Day 10, Hour 39 (Integration choice)**  
   Files:
   - `Advanced/assignments/Advanced_Day10_homework.ipynb` (Part 3)
   - `Advanced/assignments/Advanced_Day10_homework/criteria.json` (Hour 39 expected output lines)  
   Problem: validates stated decisions, not executable integration behavior.

3. **Day 12, Hour 48 (Final retrospective)**  
   Files:
   - `Advanced/assignments/Advanced_Day12_homework.ipynb` (Part 4)
   - `Advanced/assignments/Advanced_Day12_homework/criteria.json` (Hour 48 expected output lines)  
   Problem: static summary text can satisfy completion without demonstrable capstone evidence.

## Prioritized redesign list

### P0 (critical)
1. Replace print-only acceptance for weak checkpoint/planning/final hours (15, 39, 48) with artifact + behavior checks.
2. Add explicit in-notebook “Definition of Done” for every Part (files/functions/commands/expected outcomes).
3. Add structural anti-gaming checks (AST/file assertions) across all days, not only days with guardrails.

### P1 (high)
4. Standardize exercise template: Goal, Starter, Steps, Success Criteria, Common Failure Modes.
5. Keep homework notebooks learner-incomplete; move complete references to `submissions/sample_*` only.
6. Enforce behavior checks over literal string labels where possible.

### P2 (medium)
7. Add per-day authenticity score metadata (real/partial/aspirational).
8. Add quick learner self-validation commands before submission.
9. Add expected effort/time guidance for each Part to reduce interpretation drift.
