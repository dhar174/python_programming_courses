# Basics Quiz HTML + Autograder Grading Reference (Day 1 & Day 2)

Day 1 and Day 2 quizzes are interactive HTML files:

- `Basics/quizzes/Basics_Day1_Quiz.html` (or `Basics/quizzes/Basics_Day1/Basics_Day1_Quiz.html`)
- `Basics/quizzes/Basics_Day2_Quiz.html` (or `Basics/quizzes/Basics_Day2/Basics_Day2_Quiz.html`)

## Visual Design

Both quiz files use a **dark IDE theme** styled for a Python coding academy:

| Token | Value | Purpose |
|---|---|---|
| `--bg` | `#1E1E2E` | Page background (dark IDE) |
| `--surface` | `#252537` | Card background |
| `--py-blue` | `#4B8BBE` | Python-brand blue accent |
| `--py-yellow` | `#FFD43B` | Python-brand yellow accent |
| `--txt` | `#CDD6F4` | Primary text (WCAG AA) |
| `--txt-muted` | `#A6ADC8` | Secondary / muted text |
| `--txt-code` | `#CBA6F7` | Inline code highlight |

Spacing is **primarily based on an 8-point grid** via the `--sp*` spacing tokens (`--sp1: 8px` … `--sp6: 48px`). Some small non-8px values (such as tight padding and `3px`/`4px` border-radii) are used at the component level for visual polish. All interactive elements use `transition: all 0.2s ease-in-out` for micro-interactions. Code blocks render in `JetBrains Mono` (with monospace fallbacks) and have a Python-yellow left-border accent. A live progress bar in the header tracks answered questions.

To edit the core theme (colors and spacing tokens), modify the `:root` CSS variables at the top of each quiz HTML file. Component-specific spacing and border-radius tweaks may also appear in individual CSS rules below `:root`. Do **not** change the JavaScript `QUIZ_DATA` block or export logic.

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
