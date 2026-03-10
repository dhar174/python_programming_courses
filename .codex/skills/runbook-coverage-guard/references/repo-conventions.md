# Repository Conventions For Runbook Coverage Guard

## Scope

Use this skill for this repository's two-module course package:
- `Basics` (Python Programming Basic)
- `Advanced` (Python Programming Advanced)

Both modules target 12 days and 4 hours per day by default unless the user requests a narrower range.

## Lecture Script Conventions

- Directory:
  - Basics: `Basics/lessons/lecture/`
  - Advanced: `Advanced/lessons/lecture/`
- Filename:
  - Basics: `Day{D}_Hour{H}_Basics.md`
  - Advanced: `Day{D}_Hour{H}_Advanced.md`

## Assignment Conventions

- Notebook:
  - `Module/assignments/Module_Day{D}_homework.ipynb`
- Config directory:
  - `Module/assignments/Module_Day{D}_homework/`
- Expected config files:
  - `criteria.json`
  - `setup.json`
  - `feedback.json`

## Quiz Conventions

- Directory:
  - `Module/quizzes/`
- Quiz file accepted as present if either exists:
  - `Module_Day{D}_Quiz.md`
  - `Module_Day{D}_Quiz.html`
- Optional answer export:
  - `Module_Day{D}_Quiz_answers.json`

## Audit Priorities

1. Missing lecture files (hour-level instructional continuity)
2. Missing assignment notebook/config bundle (grading readiness)
3. Missing quiz files (assessment coverage)
4. Naming mismatches that break automation assumptions

## Scaffolding Policy

- Default to non-destructive creation only.
- Avoid overwriting any existing file unless explicitly requested (`--force`).
- Keep scaffold templates minimal and deterministic.
