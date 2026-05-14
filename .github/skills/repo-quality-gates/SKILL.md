---
name: repo-quality-gates
description: 'Run the repositorys test, lint, and typecheck commands, then summarize failures and next actions for coding agents.'
---

# Repo Quality Gates

Use this skill when you need to validate a change or interpret failing automation for this repository.

## Default validation commands
- `python -m pip install nbconvert`
- `├── criteria.json         # Test specs: command, stdin, expected_stdout, points`

## Workflow
1. Run the smallest relevant validation subset first.
2. Group failures by root cause instead of by raw output order.
3. Call out missing tooling or environment issues separately from code regressions.
4. Do not relax or delete tests just to produce a green run.
