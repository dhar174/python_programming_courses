<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Progress

## Milestones
- [x] Repository profile captured
- [x] Hybrid agent stack scaffolded
- [ ] Maintenance drift reviewed against future repo changes

## What works
- Repo-wide instructions, memory-bank scaffolding, and specialist agents exist.
- Managed sections allow maintenance runs to update generated content safely.

## What is incomplete
- Third-party imports remain optional until a pinned, licensed source is selected.
- The generated stack may still need repo-specific hand tuning after major architecture shifts.

## Validation status
- Install: `python -m pip install nbconvert`
- Test: `├── criteria.json         # Test specs: command, stdin, expected_stdout, points`

## Last meaningful update
[2026-05-13] Generated or refreshed the repo bootstrap stack.
<!-- repo-agent-bootstrap:managed:end -->
