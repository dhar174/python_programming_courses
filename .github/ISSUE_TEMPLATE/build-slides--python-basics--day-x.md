---
name: 'Build slides: Python Basics, Day X'
about: 'Create the slide deck (or annotated teaching notes) for **Basics Day {{DAY}}**
  that follows the runbook’s hour-block rhythm:'
title: "[Basics] Slides — Day {{DAY}} (Session {{SESSION}}, Hours {{HOURS}})"
labels: basics, slides
assignees: ''

---

# =========================
# TEMPLATE 1 — Build slides: Python Basics, Day X
# =========================

Title: [Basics] Slides — Day {{DAY}} (Session {{SESSION}}, Hours {{HOURS}})
Labels: slides, basics
Assignees: {{ASSIGNEE}}
Milestone: {{MILESTONE}}

## Goal
Create the slide deck (or annotated teaching notes) for **Basics Day {{DAY}}** that follows the runbook’s hour-block rhythm:
**Outcomes → Instructor talk points → Live demo → Hands-on lab → Completion criteria (+ quick check / exit ticket)**.

## Inputs / References
- Python_Basics_Instructor_Runbook_4hr_Days.pdf — **Session {{SESSION}} (Hours {{HOURS}})** + any referenced checkpoints for this session
- Python Programming - Basic.docx — “Course Outline (Modules)” (for topic coverage)
- Python GIT Training Course Package.docx — “Python Programming for Developers Basic” Course Outline (Modules)

## Tasks
- [ ] Pull the exact hour blocks for Session {{SESSION}} from the runbook (titles + outcomes + talk points + demo steps + lab prompts + completion criteria + pitfalls + quick check).
- [ ] Draft deck outline with sections per hour (1 hour = 1 major section).
- [ ] Build slides per hour:
  - [ ] Outcomes slide (bullet list)
  - [ ] Key concepts slide(s) (talk points)
  - [ ] Demo slide(s): “watch for…” + expected output
  - [ ] Lab slide: instructions + timebox + completion criteria
  - [ ] Quick check / exit ticket slide
- [ ] Add speaker notes:
  - [ ] Common pitfalls + pacing adjustments
  - [ ] “Optional extensions (stay in Basics scope)” (if listed for that hour)
- [ ] Add “Scope guardrail” note in speaker notes (see “No-go topics for the Basics course” list).
- [ ] Export + commit:
  - [ ] Save as {{FORMAT}} (PPTX/Google Slides link/PDF)
  - [ ] Store in repo path: {{REPO_PATH}} (e.g., /slides/basics/day-{{DAY}})

## Acceptance Criteria
- [ ] Every hour block in Session {{SESSION}} is represented in the deck.
- [ ] Each lab in the runbook is reflected with timebox + completion criteria.
- [ ] Deck contains at least one slide explicitly reminding “stay in Basics scope” (speaker notes OK).
- [ ] File/link is in the correct repo location and named consistently.

## Deliverables
- Link/file: {{LINK_OR_PATH}}
