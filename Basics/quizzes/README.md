# Basics Quiz HTML + Autograder Grading Reference (Day 1 & Day 2)

Day 1 and Day 2 quizzes are interactive HTML files:

- `Basics/quizzes/Basics_Day1_Quiz.html` (or `Basics/quizzes/Basics_Day1/Basics_Day1_Quiz.html`)
- `Basics/quizzes/Basics_Day2_Quiz.html` (or `Basics/quizzes/Basics_Day2/Basics_Day2_Quiz.html`)

## Student answer export and required filenames

1. Open the quiz HTML file in a browser.
2. Select one answer per question.
3. Answers are saved in browser `localStorage`.
4. Click **Save/Export Answers (JSON)**.

Keep the exported filename unchanged so the workflow can find it:

- `Basics_Day1_Quiz_answers.json`
- `Basics_Day2_Quiz_answers.json`

Expected location for grading pickup:

- `Basics/quizzes/Basics_Day1_Quiz_answers.json` or next to the Day 1 HTML file
- `Basics/quizzes/Basics_Day2_Quiz_answers.json` or next to the Day 2 HTML file

## Expected exported JSON structure

Each quiz export contains metadata plus answer/test data. Example:

```json
{
  "quiz_id": "Basics_Day1_Quiz",
  "title": "Python Basics - Day 1 Quiz",
  "exported_at": "2026-02-21T00:00:00.000Z",
  "student_answers": {
    "1": "D",
    "2": "C"
  },
  "expected_answers": {
    "1": "D",
    "2": "C"
  },
  "criteria_like_tests": [
    {
      "name": "Question 1",
      "points": 1,
      "expected_stdout": ["D"],
      "student_stdout": ["D"],
      "pass": true
    }
  ]
}
```

`student_answers` is the field consumed by `.github/workflows/autograder.yml` for score calculation. Question IDs must be numeric string keys.

## How this maps to `criteria.json` and the workflow

- Assignment grading still uses `Basics/assignments/Basics_DayX_homework/criteria.json` + `setup.json`.
- Quiz grading runs in `.github/workflows/autograder.yml` (`Grade Basics HTML quizzes` step), reads `expectedAnswers` from quiz HTML, and compares to `student_answers` from exported JSON.
- The workflow writes consolidated summary files to:
  - `submission/.github/autograder/assignment_grades.json`
  - `submission/.github/autograder/quiz_grades.json`

## `quiz_grades.json` structure change

The consolidated format now embeds per-question quiz tests directly in each quiz record.

- Previous shape:
  ```json
  {
    "quiz_id": "Basics_Day1_Quiz",
    "criteria_file": "submission/.github/autograder/Basics_Day1_Quiz_criteria.json"
  }
  ```
- Current shape:
  ```json
  {
    "quiz_id": "Basics_Day1_Quiz",
    "score": 28,
    "total": 30,
    "tests": [
      {
        "name": "Basics_Day1_Quiz Question 1",
        "points": 1,
        "expected_stdout": ["D"],
        "student_stdout": ["D"],
        "pass": true
      }
    ]
  }
  ```
