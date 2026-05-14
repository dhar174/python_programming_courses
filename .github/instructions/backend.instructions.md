---
applyTo: "src/**,tests/**"
---

<!-- repo-agent-bootstrap:file-kind=path-instructions -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Backend instructions

- Preserve existing interfaces and module boundaries unless the task explicitly changes them.
- Add or update automated coverage for behavior changes.
- Run `├── criteria.json         # Test specs: command, stdin, expected_stdout, points`, `ruff check .`, and `mypy .` when the touched paths justify them.
- Reuse established helper modules before introducing new abstractions.
<!-- repo-agent-bootstrap:managed:end -->
