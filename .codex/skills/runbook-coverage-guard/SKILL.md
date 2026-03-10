---
name: runbook-coverage-guard
description: Audit curriculum coverage against instructor runbook structure and repository naming rules for Basics and Advanced modules. Use when Codex needs to detect missing or misnamed Day/Hour lecture files, missing daily assignment artifacts, missing quiz artifacts, autograder-readiness gaps, or when scaffolding standardized placeholders for missing course files.
---

# Runbook Coverage Guard

## Overview

Audit per-day and per-hour course artifact coverage and optionally scaffold missing files using this repository's conventions. Produce a deterministic gap report before creating placeholders.

## Bundled Resources

- `scripts/audit_runbook_coverage.py`: Audit coverage and optionally scaffold missing files.
- `references/repo-conventions.md`: Naming rules and expected folder structure used by the audit.

## Workflow

1. Confirm scope with user: module (`Basics`, `Advanced`, or `both`) and day range.
2. Run audit in report-only mode and inspect missing or malformed artifacts.
3. Share prioritized findings with concrete file paths.
4. If user asks for scaffolding, rerun with `--scaffold` and selected categories.
5. Re-run audit to confirm gaps were reduced.

## Command Patterns

```bash
# Report only (both modules, 12 days x 4 hours default)
py -3 .codex/skills/runbook-coverage-guard/scripts/audit_runbook_coverage.py

# Report Basics days 1-5 only
py -3 .codex/skills/runbook-coverage-guard/scripts/audit_runbook_coverage.py --module basics --days 5

# Scaffold missing lecture files only
py -3 .codex/skills/runbook-coverage-guard/scripts/audit_runbook_coverage.py --module advanced --scaffold lecture

# Scaffold all artifact categories and print JSON report
py -3 .codex/skills/runbook-coverage-guard/scripts/audit_runbook_coverage.py --module both --scaffold lecture,assignment,quiz --json
```

## Scaffolding Rules

- Generate lecture files in `Module/lessons/lecture/DayX_HourY_Module.md` with minimal instructional placeholders.
- Generate assignment notebook stubs in `Module/assignments/Module_DayX_homework.ipynb`.
- Generate assignment config stubs in `criteria.json`, `setup.json`, and `feedback.json` under `Module/assignments/Module_DayX_homework/`.
- Generate quiz stubs in `Module/quizzes/Module_DayX_Quiz.html`.
- Never overwrite existing files unless `--force` is explicitly set.

## Reporting Expectations

- Include totals for expected, present, and missing files for each artifact type.
- Include concrete missing file paths in the report output.
- Keep output deterministic and free of current date/time values.

Load `references/repo-conventions.md` when rules need confirmation or when this repository's structure changes.
