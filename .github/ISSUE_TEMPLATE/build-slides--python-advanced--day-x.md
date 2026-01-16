---
name: 'Build slides: Python Advanced, Day X'
about: Create the slide deck (or annotated teaching notes) for **Advanced Day {{DAY}}**
  aligned to the runbook’s hour-block rhythm and any checkpoint(s) in that session.
title: "[Advanced] Slides — Day {{DAY}} (Session {{SESSION}}, Hours {{HOURS}})"
labels: advanced, slides
assignees: ''

---

# =========================
# TEMPLATE 2 — Build slides: Python Advanced, Day X
# =========================

Title: [Advanced] Slides — Day {{DAY}} (Session {{SESSION}}, Hours {{HOURS}})
Labels: slides, advanced
Assignees: {{ASSIGNEE}}
Milestone: {{MILESTONE}}

## Goal
Create the slide deck (or annotated teaching notes) for **Advanced Day {{DAY}}** aligned to the runbook’s hour-block rhythm and any checkpoint(s) in that session.

## Inputs / References
- Python_Advanced_Instructor_Runbook_4hr_Days.pdf — **Session {{SESSION}} (Hours {{HOURS}})** + any checkpoint(s) for this session
- Python Programming Advanced Global IT training package.docx — “Course Outline (Modules)”
- Python GIT Training Course Package.docx — “Python Programming Advanced” Course Outline (Modules)

## Tasks
- [ ] Pull the exact hour blocks for Session {{SESSION}} (outcomes, talk points, demos, labs, completion criteria, pitfalls, optional extensions, quick checks).
- [ ] Draft deck outline with sections per hour (1 hour = 1 major section).
- [ ] Build slides per hour:
  - [ ] Outcomes
  - [ ] Key concepts (talk points)
  - [ ] Live demo guide (what to show + expected results)
  - [ ] Lab instructions + timebox + completion criteria
  - [ ] Quick check / exit ticket
- [ ] If the session includes a Checkpoint:
  - [ ] Add “Checkpoint briefing” slides (requirements, timebox, submission, grading cues)
  - [ ] Add “common pitfalls” slide specific to the checkpoint
- [ ] Add speaker notes:
  - [ ] “Optional extensions (stay in Advanced scope)” (if listed)
  - [ ] Troubleshooting notes relevant to the tools used (Flask ports/DB paths/etc.)
- [ ] Export + commit:
  - [ ] Save as {{FORMAT}} (PPTX/Google Slides link/PDF)
  - [ ] Store in repo path: {{REPO_PATH}} (e.g., /slides/advanced/day-{{DAY}})

## Acceptance Criteria
- [ ] Every hour block in Session {{SESSION}} is represented in the deck.
- [ ] Each lab is represented with timebox + completion criteria.
- [ ] If checkpoint exists: deck includes checkpoint briefing + submission expectations.
- [ ] File/link is in the correct repo location and named consistently.

## Deliverables
- Link/file: {{LINK_OR_PATH}}
