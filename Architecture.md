# Architecture

_Guiding principles and constraints that must stay consistent across all work in this repository._

---

## Principles

### 1. Runbooks Are the Source of Truth
All lesson content — lecture scripts, slides, assignments, and quizzes — must align to the instructor runbooks:
- `Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md`
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`

Before authoring or modifying any course content, cross-reference the relevant runbook entry. Do not introduce topics, examples, or objectives that are not present in the runbook for that session.

### 2. Per-Hour File Granularity
Every instructional hour receives exactly one dedicated file. Never combine multiple hours into one file. This enforces:
- Clear curriculum traceability (ISO day/hour → file)
- Granular agent automation (one file = one tractable task)
- Safe concurrent editing (no merge conflicts across hours)

Naming convention: `DayX_HourY_{Module}.md` (e.g., `Day3_Hour2_Basics.md`).

### 3. Deterministic Autograder Contracts
All graded outputs must be fully deterministic:
- No `datetime.now()`, no `random` without explicit seeds, no environment-dependent output
- Numeric precision must match `criteria.json` exactly (e.g., `85.50` not `85.5`)
- Converted notebook script must use the module-prefixed autograder name (for example, `basics_day12.py` or `advanced_day12.py`)
- Grading commands run the script and compare stdout character-for-character

### 4. AI Agent Governance
Human contributors and AI agents operate under the same rules defined in `AGENTS.md`. Each agent has an explicit scope — agents must not author content outside their designated module or directory. All agents must cite the runbook and `AGENTS.md` as authority before making content decisions.

### 5. Separation of Content and Build Artifacts
Source content (Markdown, notebooks, HTML quizzes) is committed to version control. Build artifacts (generated HTML/PDF/PPTX slides, `_site/`) are produced by CI and are either deployed or discarded — not committed directly to `main`.

### 6. Documentation as First-Class Citizen
Long-running work requires explicit memory files (`Prompt.md`, `Plans.md`, `Architecture.md`, `Implement.md`, `Documentation.md`) to maintain coherence across agent and human handoffs. These files are updated as milestones are completed or decisions are made.

---

## Constraints

| Constraint | Rule |
|---|---|
| **Technology** | Marp CLI via `npx` (no `package.json`). Python 3.x. Jupyter/nbconvert. GitHub Actions only. |
| **Slide themes** | Only `python-dark.css` and `python-light.css` from the respective `themes/` directory unless a task explicitly requires theme work |
| **File naming** | Strict naming conventions for all course artifacts (see `AGENTS.md` §Naming Convention) |
| **Autograder** | `webtech-network/autograder@v1` only. Inputs and outputs must match the documented JSON schema. |
| **No live APIs in tests** | CI grading must never call external APIs or LLMs. All test assertions are deterministic stdout comparisons. |
| **Scope isolation** | Basics content belongs in `Basics/`; Advanced content belongs in `Advanced/`. Cross-module dependencies are not permitted. |
| **Per-hour file rule** | One file per instructional hour. No combined session files. |
