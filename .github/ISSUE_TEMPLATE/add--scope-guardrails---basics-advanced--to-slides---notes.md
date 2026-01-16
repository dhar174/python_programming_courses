---
name: Add “scope guardrails” (Basics/Advanced) to slides + notes
about: Prevent scope creep by embedding “what NOT to teach here” reminders into speaker
  notes (and optionally 1 visible slide per day).
title: "[{{COURSE}}] Add scope guardrails to decks (out-of-scope reminders)"
labels: curriculum, qa, slides
assignees: ''

---

# =========================
# TEMPLATE 5 — Add “scope guardrails” (Basics/Advanced) to slides + notes
# =========================

Title: [{{COURSE}}] Add scope guardrails to decks (out-of-scope reminders)
Labels: curriculum, qa, slides
Assignees: {{ASSIGNEE}}
Milestone: {{MILESTONE}}

## Goal
Prevent scope creep by embedding “what NOT to teach here” reminders into speaker notes (and optionally 1 visible slide per day).

## Inputs / References
- If COURSE=Basics:
  - Python_Basics_Instructor_Runbook_4hr_Days.pdf — “No-go topics for the Basics course (keep for Advanced)”
- If COURSE=Advanced:
  - Python_Advanced_Instructor_Runbook_4hr_Days.pdf — “Optional extensions (stay in Advanced scope)” notes per hour
- Official module outline doc(s) for the course (Basic/Advanced) to confirm intended scope

## Tasks
- [ ] Basics: add a reusable speaker-note block to every Basics deck:
  - [ ] “No-go topics” reminder (web frameworks/APIs, DB/SQL/ORM, GUI, pytest/coverage, packaging/deploy, numpy/pandas/matplotlib/ML)
  - [ ] What to say instead if asked (point learners to Advanced course / later module)
- [ ] Advanced: add a reusable speaker-note block to every Advanced deck:
  - [ ] “Stay in Advanced scope” reminder aligned to optional extensions notes
  - [ ] Avoid over-frameworking / rabbit holes (document the “parking lot” approach)
- [ ] Add 1 lightweight visible slide per day (optional) titled “Scope today” (2 bullets: “we cover” / “we’re parking”).
- [ ] Ensure guardrails don’t conflict with official module outlines.

## Acceptance Criteria
- [ ] Every deck includes a scope-guardrail note (speaker notes OK).
- [ ] Basics decks include explicit Basics “no-go topics” reference.
- [ ] Advanced decks include “stay in Advanced scope” note consistent with runbook optional extensions.
- [ ] Any recurring learner questions have a consistent deflection script (parking lot).

## Deliverables
- PR/commit with updated decks: {{LINK_OR_PATH}}
