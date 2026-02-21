# Basics Quiz HTML Format (Day 1 & Day 2)

Day 1 and Day 2 quizzes now use interactive HTML files:

- `Basics_Day1_Quiz.html`
- `Basics_Day2_Quiz.html`

## Student usage

1. Open the quiz HTML file in a browser.
2. Select one answer per question.
3. Answers are saved immediately in browser `localStorage` and restored on reload.
4. Click **Save/Export Answers (JSON)** to download your response file.
   The download is pre-named to match autograder expectations (e.g., `Basics_Day1_Quiz_answers.json`).

For autograder pickup, keep the exported filename as:

- `Basics_Day1_Quiz_answers.json` for Day 1
- `Basics_Day2_Quiz_answers.json` for Day 2

## Autograder compatibility note (`criteria.json`)

The exported JSON includes:

- `student_answers` (question -> selected option)
- `criteria_like_tests` (per-question entries with `name`, `points`, `expected_stdout`, `student_stdout`, and `pass`)

This mirrors the per-test structure used by autograder `criteria.json` workflows, so maintainers can map each exported question entry to a `tests[]` item for grading pipelines.
