---
name: 'Coverage audit: Basics slides vs official module outline'
about: Verify the full Basics slide set (all days) covers every module/topic in the
  official outlines, and flag gaps or duplicates.
title: "[Basics] Audit — Slides match official module outline (coverage + gaps)"
labels: basics, curriculum, qa
assignees: ''

---

# =========================
# TEMPLATE 3 — Coverage audit: Basics slides vs official module outline
# =========================

Title: [Basics] Audit — Slides match official module outline (coverage + gaps)
Labels: qa, curriculum, basics
Assignees: {{ASSIGNEE}}
Milestone: {{MILESTONE}}

## Goal
Verify the full Basics slide set (all days) covers every module/topic in the official outlines, and flag gaps or duplicates.

## Inputs / References
- Python Programming - Basic.docx — “Course Outline (Modules)”
- Python GIT Training Course Package.docx — “Python Programming for Developers Basic” Course Outline (Modules)
- Python_Basics_Instructor_Runbook_4hr_Days.pdf — session/hour breakdown (source of truth for pacing)

## Tasks
- [ ] Create a mapping table: Module → Topics → Slide deck day/session → Slide numbers (or section titles).
- [ ] Check off each module/topic from the official outline as “covered” with evidence (deck + slide refs).
- [ ] Identify:
  - [ ] Missing topics (not present anywhere)
  - [ ] Under-covered topics (mentioned but no demo/lab)
  - [ ] Over-covered topics (taking disproportionate time)
- [ ] Propose fixes:
  - [ ] Add/adjust slides in specific Day {{DAY}} issues (link those issues)
  - [ ] If runbook intentionally omits a topic, document rationale + where it appears elsewhere (lab, handout, etc.)

## Acceptance Criteria
- [ ] Every module/topic line item is mapped to a deck + slide reference.
- [ ] Gaps are listed with a clear remediation plan (which day, what to add).
- [ ] Updates are filed as follow-up issues (or PRs) and linked.

## Deliverables
- Mapping doc link/path: {{LINK_OR_PATH}}
- Gap list (bullets) included in issue comments or attached doc.
