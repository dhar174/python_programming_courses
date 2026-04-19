# Plans

_Track milestones and validations in order, updating status as work progresses._

---

## Current Initiative: Course Package Completion & CI Hardening

**Goal:** Deliver a fully content-complete, autogradable, CI-validated 96-hour Python training package.

---

## Milestones & Validations

### Phase 1 — Content Authoring ✅ Complete

- [x] **Milestone 1.1 — Basics Lecture Scripts (Hours 1–48)**
  - All 48 `DayX_HourY_Basics.md` files present in `Basics/lessons/lecture/`
  - **Validation:** `ls Basics/lessons/lecture/ | wc -l` returns 48+ files; each ≥ ~4,000 words

- [x] **Milestone 1.2 — Advanced Lecture Scripts (Hours 1–48)**
  - All 48 `DayX_HourY_Advanced.md` files present in `Advanced/lessons/lecture/`
  - **Validation:** `ls Advanced/lessons/lecture/ | wc -l` returns 48+ files

- [x] **Milestone 1.3 — Basics Homework Assignments (Days 1–12)**
  - 12 `.ipynb` templates + `criteria.json`, `setup.json`, `feedback.json` per day
  - **Validation:** Each `Basics/assignments/Basics_DayX_homework/` contains all three config files

- [x] **Milestone 1.4 — Advanced Homework Assignments (Days 1–12)**
  - 12 `.ipynb` templates + `criteria.json`, `setup.json`, `feedback.json` per day
  - **Validation:** Each `Advanced/assignments/Advanced_DayX_homework/` contains all three config files

- [x] **Milestone 1.5 — Basics Multiple Choice Quizzes (Days 1–12)**
  - 12 `Basics_DayX_Quiz.html` files in `Basics/quizzes/`
  - **Validation:** All 12 HTML files present

- [x] **Milestone 1.6 — Advanced Multiple Choice Quizzes (Days 1–12)**
  - 12 `Advanced_DayX_Quiz.html` files in `Advanced/quizzes/`
  - **Validation:** All 12 HTML files present

---

### Phase 2 — CI Infrastructure ✅ Substantially Complete

- [x] **Milestone 2.1 — Slide Build Pipeline**
  - `marp-action.yml` builds HTML/PDF/PPTX slides and deploys to GitHub Pages
  - **Validation:** GitHub Actions badge green on `main`

- [x] **Milestone 2.2 — Autograder Pipeline (Basics)**
  - `autograder.yml` grades Basics assignments and quizzes
  - **Validation:** Autograder badge green; `assignment_grades.json` and `quiz_grades.json` produced

- [x] **Milestone 2.3 — Autograder Pipeline (Advanced)**
  - `autograder.yml` expanded to cover all 12 Advanced days
  - **Validation:** PR #114 merged; Advanced setup.json files standardized

---

### Phase 3 — Quiz Answer Key Extraction ✅ Complete (as of 2026-04-19)

- [x] **Milestone 3.1 — Basics Quiz Answer Keys (Days 1–12)**
  - 12 `Basics_DayX_Quiz_answers.json` files generated from HTML quiz sources
  - **Validation:** All 12 `_answers.json` files present in `Basics/quizzes/`

- [x] **Milestone 3.2 — Advanced Quiz Answer Keys (Days 1–12)**
  - 12 `Advanced_DayX_Quiz_answers.json` files generated from HTML quiz sources
  - **Validation:** All 12 `_answers.json` files present in `Advanced/quizzes/`

---

### Phase 4 — Sample Submissions & Full CI Validation ✅ Complete (as of 2026-04-19)

- [x] **Milestone 4.1 — Advanced Sample Submissions**
  - Sample `.ipynb` submissions added for all 12 Advanced assignment directories
  - **Validation:** Each `Advanced/assignments/Advanced_DayX_homework/submissions/` contains at least one `*Advanced_DayX*.ipynb`

- [x] **Milestone 4.2 — Autograder Config Standardization**
  - All `setup.json` files use the standardized bash resolution script pattern
  - **Validation:** `criteria.json` commands execute `python dayN.py` consistently across all 24 assignments

---

### Phase 5 — Documentation & Agent Governance ✅ Complete (as of 2026-04-19)

- [x] **Milestone 5.1 — AGENTS.md**
  - Comprehensive contributor and AI agent governance documentation authored
  - **Validation:** `AGENTS.md` at repo root; covers naming, structure, autograder contracts, workflow

- [x] **Milestone 5.2 — README.md**
  - Multi-audience README with CI badges, quick-start, and accurate repository contents
  - **Validation:** README has Learner / Instructor / Contributor sections; no stale placeholder text

- [x] **Milestone 5.3 — Architecture & Memory Files**
  - `Architecture.md`, `Plans.md`, `Documentation.md` contain real project content
  - **Validation:** No template placeholder text remains in any root-level memory file

---

## Next Steps (Post-Completion)

- [ ] **Future 6.1 — Live Student Validation**
  - Run the autograder against real student submissions from first cohort
  - Iterate on `criteria.json` based on observed edge cases

- [ ] **Future 6.2 — Slide Coverage Audit**
  - Run coverage audit (GitHub Issue template available) for both Basics and Advanced slides vs. runbook
  - Fill any gaps in slide coverage

- [ ] **Future 6.3 — Manual Autograder Test Workflow**
  - Implement proposed `autograder-manual-tests.yml` (see `Documentation.md` §Autograder Workflow Review)
  - Covers Day 1 + Day 2 happy path, missing-answers, and invalid-JSON scenarios
