# Documentation

Usage: Log milestone status updates and decisions so future handoffs can continue with full context.

## Milestone Status
- **2026-02-26 — Autograder workflow review (Days 1–2)**: Completed a workflow + integration audit and drafted a manual testing plan. See the report below for findings, alignment notes, and a triggerable test suite design.

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
- Workflow writes consolidated grading summaries to:
  - `submission/.github/autograder/assignment_grades.json`
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
   - Re-run workflow dispatch and verify `assignment_grades.json` and `quiz_grades.json`.
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
