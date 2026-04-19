---
title: Project Completion Specification
version: 1.0
date_created: 2026-04-19
owner: dhar174
tags: [process, course, completion]
---

# Introduction

This specification defines the current completion status and the remaining required tasks for the 96-hour Python Programming Training Course Package. The course consists of Module 1: Basics (48 hours) and Module 2: Advanced (48 hours). 

## 1. Purpose & Scope

The purpose of this document is to explicitly outline what has been completed in the repository, and what remains pending, specifically across instructor runbooks, lecture scripts, assignment configurations, quiz resources, and automated grading pipelines. The target audience is content developers, instructional designers, and DevOps engineers maintaining the `python_programming_courses` repository.

## 2. Definitions

- **Module 1 (Basics)**: The first 48 hours of instruction, aligned with Python Institute PCEP and PCAP pathways.
- **Module 2 (Advanced)**: The second 48 hours of instruction, focusing on advanced Python methodologies.
- **Notebook**: A `.ipynb` document containing coding homework assignments.
- **Answer Export**: A JSON file (`_answers.json`) parsed from the quiz HTML interface to evaluate students' answers.

## 3. Requirements, Constraints & Guidelines

- **REQ-001**: All 12 days for Module 1 (Basics) must have 4 per-hour lecture Markdown files (`DayX_HourY_Basics.md`).
- **REQ-002**: All 12 days for Module 2 (Advanced) must have 4 per-hour lecture Markdown files (`DayX_HourY_Advanced.md`).
- **REQ-003**: Each day in both modules must include a `.ipynb` homework assignment template, and a set of automated grading configuration files (`criteria.json`, `setup.json`, `feedback.json`).
- **REQ-004**: Each day must feature a multiple choice quiz (`.html`).
- **REQ-005**: All quizzes must have corresponding `_answers.json` files to enable CI/CD autograding workflows.
- **REQ-006**: **Lecture Length & Scope** - Each per-hour lecture script must be a standalone Markdown file designed as a live speaking script, targeting a minimum length of ~4,000 words per hour.
- **REQ-007**: **Assignment Structure** - Student notebook submissions must strictly follow the `[name]-Basics_DayX_homework.ipynb` or comparable Advanced template naming convention.
- **REQ-008**: **Bash Execution Formatting** - Autograder scripts are to evaluate purely converted python files named exclusively as `dayN.py` (where N is the day) to remain standardized across the pipeline.

## 4. Interfaces & Data Contracts

- **Autograder Configuration (`criteria.json`)**: Contains `tests` array defining the command, expected standard output list, and points per test.
- **Quiz Export Format (`_answers.json`)**: A JSON document that contains a `student_answers` property dictionary mapping question string IDs to answer string values.

## 5. Acceptance Criteria

- **AC-001**: Given the Basics module is fully authored, When we check the `Basics/lessons/lecture/` directory, Then 48 distinct per-hour lecture script files should be present.
- **AC-002**: Given the automated grading workflow runs, When the quizzes are validated, Then every quiz must have a corresponding `_answers.json` file in the same directory or within the root `quizzes` folder.

## 6. Test Automation Strategy

- **Test Levels**: Functional verification via GitHub Actions autograding workflow.
- **Frameworks**: Jupyter nbconvert and `webtech-network/autograder@v1`.
- **Testing Mechanics**:
  - `setup.json` uses a simplified bash resolution script structure: `set -- submissions/*DayX*.ipynb; if [ "$1" = 'submissions/*DayX*.ipynb' ]; then echo 'ERROR: No matching Day X notebook found'; exit 1; fi; if [ "$#" -ne 1 ]; then echo 'ERROR: Multiple matching Day X notebooks found'; exit 1; fi; jupyter nbconvert --to script "$1" --output dayX --output-dir .` without relying on fallback loops.
  - `criteria.json` commands array must execute exactly `python dayX.py` and perform precise deterministic expected output matching.
- **Coverage Requirements**: The GitHub action test suite currently parses assignment notebooks and checks all matching Quiz HTML models against `_answers.json`.
- **CI/CD Integration**: Executes deterministic notebook tests per-submission on `push`, `pull_request`, and `workflow_dispatch`.

## 7. Rationale & Context

To ensure the automated grading pipeline and course structure are scalable, standardized workflows have been implemented. The course requires 96 total hours, and every sub-module file ensures atomic pacing mapping perfectly to standard runbooks without relying on manual grading overhead.

## 8. Dependencies & External Integrations

### Infrastructure Dependencies
- **INF-001**: `nbconvert` library to transform student notebooks into executable Python scripts.
- **INF-002**: webtech-network/autograder@v1 GH Action template to manage deterministic stdout match assertions.

## 9. Examples & Edge Cases

Missing `_answers.json` files currently break full workflow execution verification as the CI action looks for them during grading steps.

## 10. Validation Criteria

### Completed Tasks Status
- **Basics Lectures**: 48/48 per-hour lecture files completed (`Basics/lessons/lecture/`).
- **Advanced Lectures**: 48/48 per-hour lecture files completed (`Advanced/lessons/lecture/`).
- **Basics Assignments**: 12/12 day directories created with `.ipynb` assignment templates. 
- **Advanced Assignments**: 12/12 day directories created with `.ipynb` assignment templates.
- **Basics Quizzes**: 12/12 daily `.html` quizzes created.
- **Advanced Quizzes**: 12/12 daily `.html` quizzes created.
- **Basics Quiz Answers**: Only Days 1-5 have matching `_answers.json` exports. Days 6-12 are missing.
- **Advanced Quiz Answers**: All 12 days are missing corresponding `_answers.json` export files.

### Pending Tasks
- **PEN-001**: Generate `Basics_DayX_Quiz_answers.json` for Basics Days 6 through 12.
- **PEN-002**: Generate `Advanced_DayX_Quiz_answers.json` for all Advanced Days 1 through 12.
- **PEN-003**: Provide sample submissions for all Advanced Module assignments to ensure CI validation testing succeeds.

## 11. Related Specifications / Further Reading

- [`AGENTS.md`](file:///mnt/c/Users/darf3/Documents/python_programming_courses/AGENTS.md)
- [`autograder.yml`](file:///mnt/c/Users/darf3/Documents/python_programming_courses/.github/workflows/autograder.yml)
- [`Documentation.md`](file:///mnt/c/Users/darf3/Documents/python_programming_courses/Documentation.md)
