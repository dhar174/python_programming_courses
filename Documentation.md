# Documentation

Usage: Log milestone status updates and decisions so future handoffs can continue with full context.

## Milestone Status
- **2026-02-26 — Autograder workflow review (Days 1–2)**: Completed a workflow + integration audit and drafted a manual testing plan. See the report below for findings, alignment notes, and a triggerable test suite design.
- **2026-02-26 — Basics Days 1–2 alignment review**: Completed a runbook-to-courseware alignment audit for Hours 1–8. See the report below for matches, gaps, and scope drift.

## Decisions
- _No decisions recorded yet._

## Autograder Workflow Review (2026-02-26)

### 1) Workflow overview
- **Workflow file**: `.github/workflows/autograder.yml`
- **Grade job** (`push` + `workflow_dispatch`):
  - Stages Day 1 homework notebook/configs into `submission/.github/autograder/`.
  - Runs `webtech-network/autograder@v1` (template preset: `io`).
  - Grades Day 1 & Day 2 HTML quizzes by parsing `QUIZ_DATA.expectedAnswers` and comparing to exported `student_answers`.
  - On manual dispatch, commits results to a timestamped `autograder-results-*` branch.
- **grade_pr job** (`pull_request`):
  - Validates JSON structure for Day 1 configs and quiz HTML `QUIZ_DATA`.
  - Does **not** execute tests (security posture for PRs).

### 2) Basics Day 1 & Day 2 integration findings
**Assignments**
- Day 1 grading is wired into the workflow staging step.
- Day 2 homework has full configs (`criteria.json`, `setup.json`, `feedback.json`) but is **not** staged in the workflow, so it is not graded in CI today.

**Quizzes**
- Day 1 & Day 2 HTML quizzes are graded from:
  - `Basics/quizzes/Basics_Day1_Quiz.html`
  - `Basics/quizzes/Basics_Day2_Quiz.html`
- Required answer exports:
  - `Basics_Day1_Quiz_answers.json`
  - `Basics_Day2_Quiz_answers.json`
- Workflow writes criteria-style outputs to:
  - `submission/.github/autograder/Basics_Day1_Quiz_criteria.json`
  - `submission/.github/autograder/Basics_Day2_Quiz_criteria.json`
  - `submission/.github/autograder/quiz_grades.json`

### 3) Alignment evaluation (course intent vs. implementation)
- **Aligned**: deterministic notebook grading, explicit `criteria.json` expectations, HTML quiz grading with numeric question IDs, and manual `workflow_dispatch` results publishing.
- **Misalignment**: Day 2 homework grading is prepared at the content level, but missing in CI staging, so Day 2 assignment results are not produced by the current workflow.
- **Recommendation**: extend the workflow (or a manual testing workflow) to stage Day 2 in the same way as Day 1 so both assignments can be graded in CI.

### 4) Triggerable testing suite plan (manual workflow design)
**Goal**: Provide a manual, comprehensive test suite covering Day 1 + Day 2 assignments and quizzes without invoking any live AI APIs.

**Proposed workflow shape (manual trigger only)**:
- **Workflow name**: `autograder-manual-tests.yml`
- **Trigger**: `workflow_dispatch` with inputs:
  - `assignment_day`: `day1` | `day2` | `both`
  - `include_quizzes`: `true` | `false`
  - `scenario`: `happy_path` | `missing_answers` | `invalid_json`
- **Matrix design**:
  - Run autograder once per assignment day (separate staging per run).
  - Quiz grading step runs when `include_quizzes == true`.
- **Mock API requirement**:
  - No AI API calls exist today. If an AI API is introduced later, gate it behind an environment flag (e.g., `USE_AI_API=false`) and replace with a deterministic mock script for testing runs.

**Manual testing steps (current repo, no new workflow yet)**:
1. **Day 1 assignment**:
   - Use the existing autograder workflow via **Actions → Autograder → Run workflow**.
   - Ensure `Basics/assignments/Basics_Day1_homework.ipynb` and configs are present.
2. **Day 2 assignment (manual run)**:
   - Locally convert/run using `Basics/assignments/Basics_Day2_homework/setup.json` commands.
   - Compare output against `Basics/assignments/Basics_Day2_homework/criteria.json`.
3. **Quizzes (Day 1 & Day 2)**:
   - Export answers from the HTML quiz UI into the required JSON file names.
   - Re-run workflow dispatch and verify `quiz_grades.json` plus `*_Quiz_criteria.json`.
4. **Negative scenarios**:
   - Remove or corrupt an answer export to validate missing/invalid JSON handling.

### 5) Key file locations
- **Workflow**: `.github/workflows/autograder.yml`
- **Day 1 assignment**:
  - `Basics/assignments/Basics_Day1_homework.ipynb`
  - `Basics/assignments/Basics_Day1_homework/{setup.json,criteria.json,feedback.json}`
- **Day 2 assignment**:
  - `Basics/assignments/Basics_Day2_homework.ipynb`
  - `Basics/assignments/Basics_Day2_homework/{setup.json,criteria.json,feedback.json}`
- **Quizzes**:
  - `Basics/quizzes/Basics_Day1_Quiz.html`
  - `Basics/quizzes/Basics_Day2_Quiz.html`
  - `Basics/quizzes/Basics_Day1_Quiz_answers.json`
  - `Basics/quizzes/Basics_Day2_Quiz_answers.json`

## Basics Days 1–2 Alignment Review (2026-02-26)

### 1) Scope reviewed
- **Runbook**: Basics Instructor 4hr Runbook, Hours 1–8 (Sessions 1–2).
- **Day 1 materials**: `Basics/lessons/lecture/Day1_Hour1_Basics.md` through `Day1_Hour4_Basics.md`, Day 1 homework, Day 1 quiz.
- **Day 2 materials**: `Basics/lessons/day-02-session-2.md`, Day 2 homework, Day 2 quiz.

### 2) Alignment matches (runbook → materials)
- **Hour 1** (orientation + environment readiness): fully covered in Day 1 Hour 1 lecture, reinforced in Day 1 homework and quiz.
- **Hour 2** (print(), comments, reading errors): fully covered in Day 1 Hour 2 lecture, reinforced in Day 1 homework and quiz.
- **Hour 3** (variables + basic types): fully covered in Day 1 Hour 3 lecture, reinforced in Day 1 homework and quiz.
- **Hour 4** (numbers + operators): fully covered in Day 1 Hour 4 lecture, reinforced in Day 1 quiz.
- **Hours 5–8** (strings, methods, input/type conversion, checkpoint): covered in `day-02-session-2.md`, Day 2 homework, and Day 2 quiz.

### 3) Gaps or mismatches
- **Hour 4 lab alignment**: Runbook specifies a Tip Calculator lab; Day 1 homework instead focuses on a restaurant bill and a unit converter. The Tip Calculator appears only in the lecture script.
- **Input-driven lab vs autograder-safe homework**: Runbook Hours 5–8 labs rely on user input; Day 2 homework uses fixed values to stay deterministic for autograding, reducing alignment with the input-driven practice.
- **Checkpoint alignment**: Runbook Hour 8 receipt generator is input-driven; Day 2 homework receipt uses fixed values.

### 4) Scope drift (topics appearing earlier than runbook)
- **Day 1 homework**: unit converter exercises (aligned to Hour 7 content) and `==` vs `=` reflection (runbook Hour 9 topic); type hints are also introduced.
- **Day 2 homework/quiz**: runbook Hour 11 string topics are split across Day 2 materials: homework introduces `split()`, `title()`, and `join()`, while the Day 2 quiz covers `split()`, `join()`, and `max(..., key=len)` (no `.title()` question).

### 5) Structural mismatches
- **Day 2 lecture structure**: No per-hour lecture scripts in `Basics/lessons/lecture/` for Hours 5–8; content is consolidated in `day-02-session-2.md` without hour-specific lecture files.

### 6) Follow-up recommendations
- Add Hour 5–8 lecture scripts or explicitly label `day-02-session-2.md` as the canonical lecture source for Day 2.
- Decide whether to move `split()/join()/title()` content to Day 3 or mark it as a preview in Day 2 materials.
- Consider a Tip Calculator homework/lab entry to mirror the Hour 4 runbook lab.
