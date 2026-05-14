<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Tech Context

## Stack
- Language: Python, TypeScript, TSX, JavaScript
- Frameworks: pytest
- CI/CD: .github/workflows/autograder.yml, .github/workflows/marp-action.yml

## Local setup
- Install: python -m pip install nbconvert
- Dev server: not yet detected
- Test command: ├── criteria.json         # Test specs: command, stdin, expected_stdout, points
- Lint command: discover from lint tooling
- Typecheck command: discover from type tooling

## Constraints
- Preserve user-authored docs and existing agent assets outside managed sections.
<!-- repo-agent-bootstrap:managed:end -->
