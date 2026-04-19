# Python Programming Course Package (96 Hours)

[![Slide Build & Deploy](https://github.com/dhar174/python_programming_courses/actions/workflows/marp-action.yml/badge.svg)](https://github.com/dhar174/python_programming_courses/actions/workflows/marp-action.yml)
[![Autograder](https://github.com/dhar174/python_programming_courses/actions/workflows/autograder.yml/badge.svg)](https://github.com/dhar174/python_programming_courses/actions/workflows/autograder.yml)
[![GitHub Pages](https://img.shields.io/badge/Slides-GitHub%20Pages-blue?logo=github)](https://dhar174.github.io/python_programming_courses/)

A complete, instructor-led **96-hour Python training package** built by **GlobalIT** and taught by **Charles Niswander**. The course delivers two sequential 48-hour modules aligned to the [Python Institute](https://pythoninstitute.org/) certification pathway (PCEP → PCAP).

> **Looking to jump in?** Jump to the section for your role:
> [📚 I'm a Learner](#-for-learners) · [🎓 I'm an Instructor](#-for-instructors) · [🛠 I'm a Contributor or AI Agent](#-for-contributors--ai-agents)

---

## Table of Contents

- [Course Overview](#course-overview)
- [For Learners](#-for-learners)
- [For Instructors](#-for-instructors)
- [For Contributors & AI Agents](#-for-contributors--ai-agents)
- [Repository Structure](#repository-structure)
- [CI/CD Pipelines](#cicd-pipelines)
- [Certification Alignment](#certification-alignment)

---

## Course Overview

| | |
|---|---|
| **Total Duration** | 96 hours (two 48-hour modules) |
| **Format** | Live, instructor-led; hands-on labs; capstone projects |
| **Instructor** | Charles Niswander |
| **Organization** | GlobalIT |
| **Certifications** | PCEP™ (Module 1) → PCAP™ (Module 2) |

### Module 1 — Python Programming: Basic (48 Hours)

Introduces Python from the ground up. Students build scripts, work with all core data structures, handle files, and implement basic OOP. Culminates in a capstone project and PCEP certification preparation.

**Topics:** environment setup · data types & operators · lists/tuples/sets/dicts · control flow · functions & modules · file I/O · exception handling · basic OOP · PCEP prep

### Module 2 — Python Programming: Advanced (48 Hours)

Builds on Module 1 to cover professional-grade Python. Students build GUI apps, connect to databases, create REST APIs, analyze data, write unit tests, and package applications. Culminates in a full-stack capstone project and PCAP certification preparation.

**Topics:** advanced OOP & design patterns · factory patterns · GUI (Tkinter/PyQt) · SQL & ORMs · Flask/Django REST APIs · NumPy/Pandas/Matplotlib · unit testing (pytest) · packaging & deployment · PCAP prep

---

## 📚 For Learners

### Prerequisites

| Module | Requirement |
|---|---|
| Module 1 (Basic) | Basic computer skills (Windows/macOS/Linux) |
| Module 2 (Advanced) | Module 1 completion or equivalent Python experience |

### Lab Setup

- **OS:** Windows 10/11 64-bit (macOS and Linux supported)
- **Python:** 3.x latest stable
- **VM:** VirtualBox with Lubuntu VM (provided by GlobalIT)
- **Editor:** VS Code or PyCharm
- **Access:** Internet connection for package installation

### Syllabi (PDF)

- [Python Basics 48h Syllabus — PCEP/PCAP Aligned](Basics/Python%20Basics%20%2848h%29%20Syllabus%20%2812x4h%29%20—%20Pcep_pcap%20Aligned.pdf)
- [Python Advanced 48h Syllabus — Path to PCPP1](Advanced/Python%20Advanced%20%2848h%29%20Syllabus%20%2812x4h%29%20—%20Pcap_path%20To%20Pcpp1.pdf)

### Career Outcomes

After completing both modules, learners are prepared for:

- Junior Python Developer
- Backend / API Developer
- QA Automation Engineer
- Full-Stack Python Developer
- Data Analyst / Data Science Assistant
- Python DevOps / Scripting Engineer

---

## 🎓 For Instructors

### Source of Truth: Instructor Runbooks

All lesson content must align to the runbooks. Do not modify lesson files without cross-referencing the runbook for that day.

- [`Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md`](Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md)
- [`Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`](Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md)

### Quick Start: Building Slides Locally

No `package.json` — use `npx` directly.

```bash
# Build all slides (mirrors CI)
npx @marp-team/marp-cli -c .marprc.yml
# Output: ./_site/slides/ (HTML, PDF, PPTX, PNG)

# Build and watch a single file during development
npx @marp-team/marp-cli --no-config-file -w Basics/lessons/slides/day-01/day-01-session-1.md

# Build a specific file as PDF
npx @marp-team/marp-cli --no-config-file Basics/lessons/slides/day-01/day-01-session-1.md -o out.pdf --pdf
```

Slides are published automatically to **GitHub Pages** on every push to `main` that touches slide source files under `Basics/lessons/slides/day-*/` or `Advanced/lessons/slides/day-*/`, or updates `.marprc.yml` / the workflow file.

### Lecture Scripts

Each hour of instruction has a dedicated Markdown lecture script for verbatim delivery.

- **Location:** `Basics/lessons/lecture/DayX_HourY_Basics.md` or `Advanced/lessons/lecture/DayX_HourY_Advanced.md`
- **Standard:** ~4,000 words minimum per hour
- **Status:** All 96 hours complete (48 Basics + 48 Advanced)

### Assignments & Quizzes

| Asset | Location | Count |
|---|---|---|
| Basics homework notebooks | `Basics/assignments/Basics_DayX_homework.ipynb` | 12 |
| Advanced homework notebooks | `Advanced/assignments/Advanced_DayX_homework.ipynb` | 12 |
| Basics quizzes (HTML) | `Basics/quizzes/Basics_DayX_Quiz.html` | 12 |
| Advanced quizzes (HTML) | `Advanced/quizzes/Advanced_DayX_Quiz.html` | 12 |

---

## 🛠 For Contributors & AI Agents

### Essential Reading

Before making any changes to this repository, read:

- **[`AGENTS.md`](AGENTS.md)** — Comprehensive agent governance, repository structure, naming conventions, autograder contracts, and development workflow. This is required reading for all contributors (human and AI).
- **[`.github/copilot-instructions.md`](.github/copilot-instructions.md)** — Copilot-specific coding instructions and build commands.

### Autograder Contracts

Homework notebooks are graded automatically. Every assignment directory must contain:

```
Basics/assignments/Basics_DayX_homework/
├── criteria.json         # Test specs: command, stdin, expected_stdout, points
├── setup.json            # Dependencies: nbconvert, file assertions
├── feedback.json         # (optional) Custom feedback settings
└── submissions/
    └── *Basics_DayX*.ipynb   # Student submission (discovered by CI glob)
```

**Critical constraints:**
- All test outputs must be **deterministic** — no `datetime.now()`, no random seeds, no unseeded state
- Converted script name should match the module-prefixed autograder contract (for example, `basics_day1.py` or `advanced_day12.py`)
- Numeric precision must match `criteria.json` exactly (e.g., `85.50` not `85.5`)

### AI Agent Stack

Ten specialized agents are defined in [`.github/agents/`](.github/agents/). The agent stack is governed by [`AGENTS.md`](AGENTS.md) and documented in [`.github/agent-stack-provenance.json`](.github/agent-stack-provenance.json).

### Local Autograder Testing

```bash
cd Basics/assignments/Basics_Day1_homework/

# Convert submission to grading script
python -m pip install nbconvert
jupyter nbconvert --to script submissions/<name>_Basics_Day1_homework.ipynb --output basics_day1

# Run and compare against criteria.json expectations
python basics_day1.py
```

---

## Repository Structure

```
python_programming_courses/
│
├── Basics/                          # Module 1 — 48 hours
│   ├── Instructor/                  #   Instructor runbook (authoritative schedule)
│   ├── lessons/
│   │   ├── lecture/                 #   48 per-hour lecture scripts
│   │   └── slides/                  #   Marp slide source (Markdown → HTML/PDF/PPTX)
│   ├── assignments/                 #   12 homework notebooks + autograder configs
│   ├── quizzes/                     #   12 HTML quizzes + 12 _answers.json exports
│   └── themes/                      #   CSS themes (python-dark.css, python-light.css)
│
├── Advanced/                        # Module 2 — 48 hours (parallel structure)
│   ├── Instructor/
│   ├── lessons/lecture/             #   48 per-hour lecture scripts
│   ├── lessons/slides/              #   Generated HTML slide decks
│   ├── assignments/
│   └── quizzes/
│
├── _site/slides/                    # Build output (generated by CI, not committed)
│
├── .github/
│   ├── workflows/
│   │   ├── marp-action.yml          #   Slide build → GitHub Pages deployment
│   │   └── autograder.yml           #   Homework + quiz grading pipeline
│   ├── agents/                      #   10 custom AI agent definitions
│   ├── instructions/                #   Per-module Copilot instructions
│   └── skills/                      #   50+ repo-local agent skill definitions
│
├── AGENTS.md                        # ⭐ Primary contributor + agent documentation
├── REPOSITORY_SUMMARY.md            # Technical architecture deep-dive
├── Architecture.md                  # Design principles and constraints
├── Plans.md                         # Milestone tracking
├── Documentation.md                 # Decision log and milestone status
├── .marprc.yml                      # Marp build configuration (used by CI)
└── spec/
    └── spec-process-project-completion.md  # Completion criteria and acceptance tests
```

> For a full technical architecture walkthrough, see [REPOSITORY_SUMMARY.md](REPOSITORY_SUMMARY.md).

---

## CI/CD Pipelines

### Slide Build & Deploy (`marp-action.yml`)

| | |
|---|---|
| **Trigger** | Push to `main` touching `Basics/lessons/**`, `Advanced/lessons/**`, or `.marprc.yml` |
| **Action** | Builds HTML, PDF, PPTX, and PNG from all Marp slide Markdown sources |
| **Output** | Deployed to GitHub Pages |

### Autograder (`autograder.yml`)

| | |
|---|---|
| **Trigger** | Push to `main`, pull requests, and manual `workflow_dispatch` |
| **Action** | Converts notebooks via `nbconvert`, runs deterministic stdout tests, grades HTML quizzes |
| **Results** | Written to `submission/.github/autograder/assignment_grades.json` and `quiz_grades.json` |
| **Manual dispatch** | Commits results to a timestamped `autograder-results-*` branch |

---

## Certification Alignment

| Module | Certification |
|---|---|
| Module 1 — Basic | [PCEP™ – Certified Entry-Level Python Programmer](https://pythoninstitute.org/pcep) |
| Module 2 — Advanced | [PCAP™ – Certified Associate in Python Programming](https://pythoninstitute.org/pcap) |

---

*Delivered by **Charles Niswander** on behalf of **GlobalIT**. For questions, contact your GlobalIT course coordinator.*
