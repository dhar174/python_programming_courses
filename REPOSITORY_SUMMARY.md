# Repository Analysis: python_programming_courses

> Generated: 2026-04-19

## Overview

This repository is a **96-hour Professional Python Training Course Package** designed to take learners from zero programming knowledge to Python Institute certification readiness. It is published by **GlobalIT** and instructed by **Charles Niswander**, targeting participants on a path toward the PCEP and PCAP certifications.

The course is split into two equal 48-hour modules delivered across 12 days each (4 hours/day):

- **Module 1 — Python Programming (Basic)**: Core syntax, data types, control flow, functions, file I/O, and introductory OOP
- **Module 2 — Python Programming (Advanced)**: Advanced OOP, functional programming, decorators, concurrency, testing, and packaging

All instructional content lives as Markdown source files, generated into slides (HTML/PDF/PPTX) via the Marp presentation framework and deployed automatically to GitHub Pages via CI/CD.

---

## Architecture

```
python_programming_courses/
├── Basics/                     # Module 1 — 48 hours
│   ├── Instructor/             #   Instructor runbook (authoritative schedule)
│   ├── lessons/
│   │   ├── lecture/            #   48 per-hour lecture scripts (DayX_HourY_Basics.md)
│   │   └── slides/             #   Marp slide source + generated HTML/PDF/PPTX
│   ├── assignments/            #   12 Jupyter notebook homework assignments
│   │   └── Basics_DayX_homework/
│   │       ├── criteria.json   #     Autograder test specs
│   │       ├── setup.json      #     nbconvert + file assertions
│   │       └── submissions/    #     Student notebook submissions
│   ├── quizzes/                #   12 HTML quizzes + 12 _answers.json exports
│   └── themes/                 #   CSS themes (dark, light)
│
├── Advanced/                   # Module 2 — 48 hours (parallel structure)
│   ├── Instructor/
│   ├── lessons/lecture/        #   48 per-hour lecture scripts (DayX_HourY_Advanced.md)
│   ├── lessons/slides/         #   Full set of generated Advanced HTML slide decks
│   ├── assignments/            #   12 Jupyter notebook homework assignments
│   └── quizzes/                #   12 HTML quizzes + 12 _answers.json exports
│
├── _site/slides/               # Marp build output (HTML, PDF, PPTX, PNG)
│
├── .github/
│   ├── workflows/
│   │   ├── marp-action.yml     # Slide build & GitHub Pages deployment
│   │   └── autograder.yml      # Automated homework + quiz grading (webtech-network/autograder@v1)
│   ├── agents/                 # Custom AI agent definitions (10 agents)
│   ├── instructions/           # Copilot coding instructions per module
│   └── skills/                 # Repo-local agent skill definitions (50+ skills)
│
├── .claude/skills/             # Claude-specific skills (frontend-design, pdf, pptx, themes)
├── .codex/skills/              # Codex-specific skills (runbook-coverage-guard)
│
├── AGENTS.md                   # Global AI agent instructions for all contributors
├── Plans.md                    # Milestone tracking
├── Architecture.md             # Guiding principles and constraints
├── Documentation.md            # Decision log and milestone status
└── .marprc.yml                 # Primary Marp build configuration
```

---

## Key Components

### 1. Instructor Runbooks (Source of Truth)
The day-by-day, hour-by-hour authoritative content schedules:
- `Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md`
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`

Every other content artifact is derived from these runbooks. AI agents are instructed to cross-reference runbooks before creating or modifying any lesson material.

### 2. Lecture Scripts (`lessons/lecture/`)
Per-hour Markdown files written for **verbatim instructor delivery**. One file per hour, naming convention `DayX_HourY_{Module}.md`. The Basics module contains ~48 files; Advanced ~48 files — a combined ~96-hour library of spoken instructional content.

### 3. Marp Slide Decks (`lessons/slides/`)
Markdown-based slide sources compiled to HTML, PDF, and PPTX via `npx @marp-team/marp-cli`. Two custom CSS themes (dark/light) provide a consistent visual identity. The Advanced module has a complete set of generated HTML decks; the Basics module slides are in active refinement.

### 4. Jupyter Homework Assignments (`assignments/`)
12 assignments per module. Each assignment directory contains:
- A template notebook (blank, for student distribution)
- A `submissions/` folder with sample/student notebooks
- `criteria.json` — deterministic stdout-comparison test cases
- `setup.json` — `nbconvert` pipeline and file assertions

### 5. HTML Quizzes + Answer Exports (`quizzes/`)
24 HTML quiz files (12 per module), each paired with a `_answers.json` export. These are graded automatically via the autograder workflow by parsing `expectedAnswers` embedded in the HTML against student `student_answers` JSON exports.

### 6. CI/CD Pipeline (`.github/workflows/`)
| Workflow | Trigger | Purpose |
|---|---|---|
| `marp-action.yml` | Push to `main` (lesson files or config) | Build slides → deploy to GitHub Pages |
| `autograder.yml` | Push/PR to `main` + manual dispatch | Grade homework notebooks and quizzes; commit results to timestamped branch |

### 7. AI Agent Stack (`.github/agents/` + skills/)
10 specialized agent definitions orchestrate content creation:
- `presentations-orchestrator.agent.md` — Coordinates slide production
- `presentations-marp-writer.agent.md` — Authors Marp slide content
- `python-educator.agent.md` — Python pedagogy expert
- `technical-content-evaluator.agent.md` — Quality gating
- `frontend-slides-batch.agent.md` — Batch HTML generation
- `repo-planner.agent.md` — Project planning and milestone management
- Plus 4 supporting agents (build, QA, Slidev writer, build engineer)

50+ local skill definitions extend agent capability across: PDF generation, PPTX editing, frontend design, theme application, evaluation rubrics, and coverage auditing.

### 8. Long-Term Memory System (repo root `.md` files)
`Prompt.md`, `Plans.md`, `Architecture.md`, `Implement.md`, and `Documentation.md` form a structured agent memory system for maintaining coherence across AI-assisted work sessions and model handoffs.

---

## Technologies Used

| Category | Technology |
|---|---|
| **Content Format** | Markdown (CommonMark + Marp extensions) |
| **Slide Generation** | Marp CLI (`@marp-team/marp-cli`), Marp for VS Code |
| **Slide Formats** | HTML, PDF, PPTX, PNG |
| **Notebooks** | Jupyter (`.ipynb`), nbconvert (notebook → Python script) |
| **CI/CD** | GitHub Actions |
| **Autograder** | `webtech-network/autograder@v1` |
| **Slide Hosting** | GitHub Pages |
| **AI Agents** | GitHub Copilot, OpenAI Codex, Claude (Anthropic), GitHub Actions bots |
| **Styling** | Vanilla CSS (Marp theme files) |
| **Certification Target** | Python Institute PCEP + PCAP |

---

## Data Flow

```
Instructor Runbooks (source of truth)
        │
        ▼
Lecture Scripts (DayX_HourY_*.md)  ──────────────────────────────────────────┐
        │                                                                      │
        ▼                                                                      ▼
Marp Slide Markdown (.md)                               Jupyter Notebooks (.ipynb)
        │                                                       │
        ▼                                                       ▼
marp-action.yml CI                                  Autograder CI (autograder.yml)
        │                                            nbconvert → Python script
        ▼                                                       │
_site/slides/ (HTML/PDF/PPTX)                       stdout vs criteria.json
        │                                                       │
        ▼                                                       ▼
GitHub Pages                                        assignment_grades.json
(public slide hosting)                              quiz_grades.json
                                                            │
                                            HTML Quiz + _answers.json
                                       (parsed against student submissions)
```

---

## Team and Ownership

| Contributor | Role | Estimated Commits (last year) |
|---|---|---|
| **Charles I Niswander II** | Primary instructor & content author | ~488 |
| **copilot-swe-agent[bot]** | AI pair programmer (GitHub Copilot) | ~247 |
| **github-actions[bot]** | CI automation (build, autograder reports) | ~138 |
| **openai-code-agent[bot]** | AI pair programmer (OpenAI Codex) | ~13 |
| **dhar174** | Repository owner / DevOps | ~11 |
| **anthropic-code-agent[bot]** | AI pair programmer (Anthropic Claude) | ~6 |

**Ownership by area:**
- Content (lectures, slides, quizzes): Charles Niswander II (human)
- Automation and tooling: dhar174 + AI agents
- Grading infrastructure: copilot-swe-agent, openai-code-agent
- GitHub Pages deployment: github-actions[bot]

---

## Current Status (as of 2026-04-19)

- **Basics module**: All 48 lecture hours written; slides in refinement; all 12 assignments and 12 quizzes complete with answer keys
- **Advanced module**: All 48 lecture hours written; full HTML slide deck set generated; all 12 assignments and 12 quizzes complete with answer keys
- **Autograder**: Active on both modules; 106 PRs merged over the past year; results written to timestamped branches
- **Active work**: Standardizing autograder configs, extracting quiz answer files, adding sample Advanced submissions
