# Python Programming Course Package (96 Hours)

[![Slide Build & Deploy](https://github.com/dhar174/python_programming_courses/actions/workflows/marp-action.yml/badge.svg)](https://github.com/dhar174/python_programming_courses/actions/workflows/marp-action.yml)
[![Autograder](https://github.com/dhar174/python_programming_courses/actions/workflows/autograder.yml/badge.svg)](https://github.com/dhar174/python_programming_courses/actions/workflows/autograder.yml)
[![GitHub Pages](https://img.shields.io/badge/Slides-GitHub%20Pages-blue?logo=github)](https://dhar174.github.io/python_programming_courses/)

An instructor-led **96-hour Python training package** built by **GlobalIT** and taught by **Charles Niswander**. The course delivers two sequential 48-hour modules aligned to the [Python Institute](https://pythoninstitute.org/) certification pathway (PCEP → PCAP), with active remediation tracked in GitHub Issues.

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
- [Course Content Index](#course-content-index)
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
# Build Basics the same way the workflow does
npx @marp-team/marp-cli -c .marprc.yml --input-dir Basics/lessons/slides --output _site/slides/basics

# Build Advanced the same way the workflow does
npx @marp-team/marp-cli --config-file .marprc.advanced.yml --input-dir Advanced/lessons/slides --output _site/slides/advanced

# Build and watch a single file during development
npx @marp-team/marp-cli --no-config-file -w Basics/lessons/slides/day-01/day-01-session-1.md

# Build a specific file as PDF
npx @marp-team/marp-cli --no-config-file Basics/lessons/slides/day-01/day-01-session-1.md -o out.pdf --pdf
```

Slides are published automatically to **GitHub Pages** on manual dispatch and on pushes to `main` that touch the workflow's configured portal and slide paths, including `Basics/lessons/slides/**`, `Advanced/lessons/slides/**`, `Basics/lessons/lecture/**`, `Advanced/lessons/lecture/**`, assignment and quiz trees for both modules, `slides/**`, `scripts/generate_portal_manifest.py`, `.marprc.yml`, `.github/workflows/marp-action.yml`, or `_site/slides/**`.

### Lecture Scripts

Each hour of instruction has a dedicated Markdown lecture script for verbatim delivery.

- **Location:** `Basics/lessons/lecture/DayX_HourY_Basics.md` or `Advanced/lessons/lecture/DayX_HourY_Advanced.md`
- **Standard:** Per-hour instructor-delivery scripts aligned to the runbooks; lecture-depth remediation remains tracked under [#269](https://github.com/dhar174/python_programming_courses/issues/269).
- **Status:** 96 day/hour lecture files are present across the two modules, plus legacy introductory lesson material in a few locations.

### Assignments & Quizzes

| Asset | Location | Count |
|---|---|---|
| Basics homework notebooks | `Basics/assignments/Basics_DayX_homework.ipynb` | 12 |
| Advanced homework notebooks | `Advanced/assignments/Advanced_DayX_homework.ipynb` | 12 |
| Basics quizzes (HTML) | `Basics/quizzes/Basics_DayX_Quiz.html` | 12 |
| Advanced quizzes (HTML) | `Advanced/quizzes/Advanced_DayX_Quiz.html` | 12 |
| Quiz answer exports | `Basics/quizzes/*_answers.json`, `Advanced/quizzes/*_answers.json` | 24 |

Advanced sample submissions are present for all 12 days. Basics sample submissions are still missing for Days 2, 3, 4, 5, 6, and 8; see [#270](https://github.com/dhar174/python_programming_courses/issues/270). Slide and lesson-source remediation remains open under [#271](https://github.com/dhar174/python_programming_courses/issues/271).

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
│   │   └── slides/                  #   Slide sources, checked-in standalone decks, and module portal assets
│   ├── assignments/                 #   12 homework notebooks + autograder configs
│   ├── quizzes/                     #   12 HTML quizzes + 12 _answers.json exports
│   └── themes/                      #   CSS themes (python-dark.css, python-light.css)
│
├── Advanced/                        # Module 2 — 48 hours (parallel structure)
│   ├── Instructor/
│   ├── lessons/lecture/             #   48 per-hour lecture scripts
│   ├── lessons/slides/              #   Slide sources plus checked-in standalone HTML decks
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
├── .marprc.yml                      # Basics Marp build configuration used by CI
├── .marprc.advanced.yml             # Advanced Marp build configuration used by CI
├── .marprc.basics.yml               # Additional Basics config file currently not referenced by the workflow
└── spec/
    ├── spec-process-cicd-marp-action.md    # Slide publishing workflow specification
    └── spec-process-project-completion.md  # Completion criteria and acceptance tests
```

> For a full technical architecture walkthrough, see [REPOSITORY_SUMMARY.md](REPOSITORY_SUMMARY.md).

---

## CI/CD Pipelines

### Slide Build & Deploy (`marp-action.yml`)

| | |
|---|---|
| **Trigger** | `workflow_dispatch` and pushes to `main` touching slide, portal, lecture, assignment, quiz, or workflow paths needed to rebuild the shared manifest and published artifact |
| **Jobs** | `build` then `deploy`, with Pages concurrency so newer publish runs cancel older in-progress runs |
| **Action** | Builds Basics and Advanced slide trees separately, stages a Pages artifact under `_site`, then deploys that artifact to GitHub Pages |
| **Output** | `_site/index.html`, `_site/404.html`, `_site/slides/basics/**`, `_site/slides/advanced/**`, `_site/slides/printable-index.html`, and `_site/slides/shared/portal/**` published through the `github-pages` environment |

#### `marp-action.yml` Behavior

1. **Build Basics output** from `Basics/lessons/slides` into `_site/slides/basics` using `.marprc.yml`.
2. **Build Advanced output** from `Advanced/lessons/slides` into `_site/slides/advanced` using `.marprc.advanced.yml`.
3. **Remove top-level README artifacts** from generated output so the published module roots expose decks and indexes instead of root README files.
4. **Verify published HTML exists** for both modules. If a generated module tree is missing usable HTML, the workflow falls back to copying the checked-in standalone slide site from `Basics/lessons/slides` or `Advanced/lessons/slides`.
5. **Publish the shared portal foundation**. The workflow copies `slides/shared/portal/**` into the Pages artifact and generates the published manifest at `_site/slides/shared/portal/course-manifest.json`.
6. **Publish supporting portal pages**. If present, `slides/printable-index.html` is copied to `_site/slides/printable-index.html` and `slides/404.html` is copied to `_site/404.html`.
7. **Guarantee a GitHub Pages entrypoint**. If `slides/index.html` exists, the workflow copies it to `_site/index.html` as the dedicated root course entrypoint. If no root page exists, the fallback redirect logic still resolves the published site to the first safe slide path it can discover.
8. **Upload and deploy** the `_site` directory as the Pages artifact, then publish it through a separate deploy job targeting the `github-pages` environment.

#### Maintaining `marp-action.yml`

- **Treat the workflow as a two-module publisher, not a single Marp command.** The local commands that actually mirror CI are:

  ```bash
  npx @marp-team/marp-cli -c .marprc.yml --input-dir Basics/lessons/slides --output _site/slides/basics
  npx @marp-team/marp-cli --config-file .marprc.advanced.yml --input-dir Advanced/lessons/slides --output _site/slides/advanced
  ```

- **Preserve trigger intent carefully.** The workflow now watches the portal source tree plus lecture, assignment, and quiz paths so manifest-backed artifact badges stay current. Changes to `.marprc.advanced.yml` still do **not** currently appear in the workflow path filters even though that file is used during the Advanced build step.
- **Keep config ownership explicit.** The workflow actively uses `.marprc.yml` for Basics and `.marprc.advanced.yml` for Advanced. A third file, `.marprc.basics.yml`, exists in the repository but is not referenced by the current workflow.
- **Do not remove the fallback copy logic casually.** The checked-in `Basics/lessons/slides/index.html` still anchors the Basics module fallback, and `Advanced/lessons/slides/` still anchors the Advanced fallback, when generated output is incomplete.
- **Protect the Pages root behavior.** `_site/index.html` is intentionally managed by `slides/index.html` first and by the redirect fallback second so the published site always resolves to course content.
- **Keep supporting pages in the artifact contract.** `slides/printable-index.html` and `slides/404.html` are now first-class publish surfaces; if they exist in source, the workflow and validator are expected to stage them into `_site`.
- **Regenerate the portal manifest whenever artifact coverage changes.** Use `python scripts/generate_portal_manifest.py` locally; CI regenerates the published manifest against `_site`.
- **Review the pinned action SHAs and temporary runtime flags together.** The workflow opts JavaScript actions into Node 24 through `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true`, and all referenced third-party actions are SHA-pinned. Update those deliberately rather than ad hoc.
- **Treat `_site/slides/**` as a defensive trigger path.** `_site/` is build output and should not normally be committed, so edits there should usually prompt a workflow/config review rather than routine content work.
- **Use the workflow specification for deeper changes.** See [`spec/spec-process-cicd-marp-action.md`](spec/spec-process-cicd-marp-action.md) before changing job flow, permissions, or entrypoint logic.

### Autograder (`autograder.yml`)

| | |
|---|---|
| **Trigger** | Push to `main`, pull requests, and manual `workflow_dispatch` |
| **Action** | Converts notebooks via `nbconvert`, runs deterministic stdout tests, grades HTML quizzes |
| **Results** | Written to `submission/.github/autograder/assignment_grades.json` and `quiz_grades.json` |
| **Manual dispatch** | Commits results to a timestamped `autograder-results-*` branch |

---

## Course Content Index

This index is intentionally **comprehensive but grouped**. It covers both module trees using stable file patterns, explicit counts, and named reference files so maintainers can audit the repository without turning the README into a raw recursive file dump.

### Basics Module Index

#### Basics Top-Level Reference Files

| File | Purpose |
|---|---|
| [`Basics/generate_slides.py`](Basics/generate_slides.py) | Batch-generates standalone Basics HTML slide decks and mirrors |
| [`Basics/Python Basics (48h) Syllabus (12x4h) — Pcep_pcap Aligned.pdf`](Basics/Python%20Basics%20%2848h%29%20Syllabus%20%2812x4h%29%20%E2%80%94%20Pcep_pcap%20Aligned.pdf) | PDF syllabus for the Basics module |
| [`Basics/python_basics_48_h_syllabus_12_x_4_h_pcep_pcap_aligned.md`](Basics/python_basics_48_h_syllabus_12_x_4_h_pcep_pcap_aligned.md) | Markdown syllabus source for the Basics module |
| [`Basics/Python Programming - Basic.md`](Basics/Python%20Programming%20-%20Basic.md) | Additional package-level Basics documentation |

#### Basics Directory and File Patterns

| Area | Current Inventory | Path / Pattern | Notes |
|---|---:|---|---|
| Instructor runbook | 1 file | [`Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md`](Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md) | Primary curriculum source of truth for the module |
| Lecture scripts | 48 files | `Basics/lessons/lecture/DayX_HourY_Basics.md` | Per-hour instructor scripts for Days 1-12 and Hours 1-4 |
| Slide day folders | 12 folders | [`Basics/lessons/slides/`](Basics/lessons/slides/) + `day-01/` ... `day-12/` | Checked-in standalone slide tree grouped by day |
| Slide Markdown sources | 13 files | `Basics/lessons/slides/**/*.md` | Includes day-based deck sources plus module-level slide docs such as the local README |
| Standalone slide HTML | 22 files | `Basics/lessons/slides/**/*.html` | Includes `index.html`, day decks, and additional standalone HTML artifacts |
| Course root landing page | 1 file | [`slides/index.html`](slides/index.html) | Dedicated root portal source copied to `_site/index.html` by the workflow |
| Supporting portal pages | 2 files | [`slides/printable-index.html`](slides/printable-index.html), [`slides/404.html`](slides/404.html) | Printable course index and custom 404 page staged by the workflow |
| Shared portal asset kit | 3 files + generator | [`slides/shared/portal/`](slides/shared/portal/) and [`scripts/generate_portal_manifest.py`](scripts/generate_portal_manifest.py) | Shared CSS/JS/manifest foundation for the root dashboard and later module portals |
| Module slide landing page | 1 file | [`Basics/lessons/slides/index.html`](Basics/lessons/slides/index.html) | Current Basics module landing page used directly and by the module fallback copy |
| Module slide landing page | 1 file | [`Advanced/lessons/slides/index.html`](Advanced/lessons/slides/index.html) | Current Advanced module landing page used directly and by the module fallback copy |
| Assignment templates | 12 files | `Basics/assignments/Basics_DayX_homework.ipynb` | Blank day-level learner notebooks |
| Assignment config directories | 12 folders | `Basics/assignments/Basics_DayX_homework/` | Each contains grading config plus a `submissions/` folder |
| Quiz HTML files | 12 files | `Basics/quizzes/Basics_DayX_Quiz.html` | Day-based learner quiz UIs |
| Quiz answer exports | 12 files | `Basics/quizzes/**/*_answers.json` | Answer-export payloads consumed by the autograder |
| Theme files | 2 files | [`Basics/themes/python-dark.css`](Basics/themes/python-dark.css), [`Basics/themes/python-light.css`](Basics/themes/python-light.css) | Shared design tokens for Marp and related slide UX |

### Advanced Module Index

#### Advanced Top-Level Reference Files

| File | Purpose |
|---|---|
| [`Advanced/generate_slides.py`](Advanced/generate_slides.py) | Batch-generates standalone Advanced HTML slide decks and mirrors |
| [`Advanced/Python Advanced (48h) Syllabus (12x4h) — Pcap_path To Pcpp1.pdf`](Advanced/Python%20Advanced%20%2848h%29%20Syllabus%20%2812x4h%29%20%E2%80%94%20Pcap_path%20To%20Pcpp1.pdf) | PDF syllabus for the Advanced module |
| [`Advanced/python_advanced_48_h_syllabus_12_x_4_h_pcap_path_to_pcpp_1.md`](Advanced/python_advanced_48_h_syllabus_12_x_4_h_pcap_path_to_pcpp_1.md) | Markdown syllabus source for the Advanced module |
| [`Advanced/Python Programming Advanced Global IT training package.md`](Advanced/Python%20Programming%20Advanced%20Global%20IT%20training%20package.md) | Additional package-level Advanced documentation |
| [`Advanced/Python_Advanced_Instructor_Runbook_4hr_Days.pdf`](Advanced/Python_Advanced_Instructor_Runbook_4hr_Days.pdf) | PDF export of the Advanced instructor runbook |

#### Advanced Directory and File Patterns

| Area | Current Inventory | Path / Pattern | Notes |
|---|---:|---|---|
| Instructor runbook | 1 Markdown + 1 PDF | [`Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`](Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md) | Primary curriculum source of truth, with an additional PDF export at module root |
| Lecture scripts | 48 day/hour files + 1 legacy intro file | `Advanced/lessons/lecture/DayX_HourY_Advanced.md` plus `Advanced/lessons/lecture/01-intro-to-python.md` | The day/hour lecture inventory is complete, but one extra legacy intro file remains in the lecture tree |
| Slide day folders | 12 folders | [`Advanced/lessons/slides/`](Advanced/lessons/slides/) + `day-01/` ... `day-12/` | Checked-in standalone slide tree grouped by day |
| Slide Markdown sources | 12 files | `Advanced/lessons/slides/**/*.md` | Day-based standalone deck sources |
| Standalone slide HTML | 12 files | `Advanced/lessons/slides/**/*.html` | One checked-in standalone HTML deck per day |
| Module slide landing page | none at module root | `Advanced/lessons/slides/` | Unlike Basics, Advanced currently has no root `index.html` portal page in this folder |
| Assignment templates | 12 files | `Advanced/assignments/Advanced_DayX_homework.ipynb` | Blank day-level learner notebooks |
| Assignment config directories | 12 folders | `Advanced/assignments/Advanced_DayX_homework/` | Each contains grading config plus a `submissions/` folder |
| Quiz HTML files | 12 files | `Advanced/quizzes/Advanced_DayX_Quiz.html` | Day-based learner quiz UIs |
| Quiz answer exports | 12 files | `Advanced/quizzes/**/*_answers.json` | Answer-export payloads consumed by the autograder |
| Theme files | 2 files | [`Advanced/themes/python-dark.css`](Advanced/themes/python-dark.css), [`Advanced/themes/python-light.css`](Advanced/themes/python-light.css) | Shared design tokens for Marp and related slide UX |

## Certification Alignment

| Module | Certification |
|---|---|
| Module 1 — Basic | [PCEP™ – Certified Entry-Level Python Programmer](https://pythoninstitute.org/pcep) |
| Module 2 — Advanced | [PCAP™ – Certified Associate in Python Programming](https://pythoninstitute.org/pcap) |

---

*Delivered by **Charles Niswander** on behalf of **GlobalIT**. For questions, contact your GlobalIT course coordinator.*
