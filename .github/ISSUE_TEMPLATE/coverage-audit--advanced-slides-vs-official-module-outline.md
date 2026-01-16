---
name: 'Coverage audit: Advanced slides vs official module outline'
about: Verify the full Advanced slide set (all days) covers every module/topic in
  the official outlines, and flag gaps or duplicates.
title: "[Advanced] Audit — Slides match official module outline (coverage + gaps)"
labels: advanced, curriculum, qa
assignees: ''

---

# =========================
# TEMPLATE 4 — Coverage audit: Advanced slides vs official module outline
# =========================

Title: [Advanced] Audit — Slides match official module outline (coverage + gaps)
Labels: qa, curriculum, advanced
Assignees: {{ASSIGNEE}}
Milestone: {{MILESTONE}}

## Goal
Verify the full Advanced slide set (all days) covers every module/topic in the official outlines, and flag gaps or duplicates.

## Inputs / References
- Python Programming Advanced Global IT training package.docx — “Course Outline (Modules)”
- Python GIT Training Course Package.docx — “Python Programming Advanced” Course Outline (Modules)
- Python_Advanced_Instructor_Runbook_4hr_Days.pdf — session/hour breakdown (source of truth for pacing)

## Tasks
- [ ] Create a mapping table: Module → Topics → Slide deck day/session → Slide numbers (or section titles).
- [ ] Check off each module/topic from the official outline as “covered” with evidence (deck + slide refs).
- [ ] Identify:
  - [ ] Missing topics
  - [ ] Under-covered topics (no demo/lab)
  - [ ] Over-covered topics
- [ ] Propose fixes and link follow-up slide-day issues.

## Acceptance Criteria
- [ ] Every module/topic line item is mapped to a deck + slide reference.
- [ ] Gaps are listed with a clear remediation plan (which day, what to add).
- [ ] Follow-up issues (or PRs) are created and linked.

## Deliverables
- Mapping doc link/path: {{LINK_OR_PATH}}
- Gap list included in issue comments or attached doc.
