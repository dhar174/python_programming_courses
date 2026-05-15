<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Active Context

## Current objective
Investigate the GitHub Pages 404 and keep repo guidance aligned with the current slide deploy shape.

## Why it matters now
The bootstrap stack only stays useful if commands, architecture notes, and specialist routing still match the repository, especially when Pages URLs or slide artifact paths shift.

## Current status
- Done:
  - Base repo inventory exists.
  - Pages deploy root vs `/slides/` mismatch has been investigated.
- In progress:
  - Keep managed guidance aligned with the codebase.
- Blocked:
  - none

## Relevant files
- `README.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `CLAUDE.md`
- `.github/workflows/marp-action.yml`
- `slides/basics/day-*/index.html`
- `slides/advanced/day-*/index.html`

## Next recommended steps
1. Keep CLI flows, prompts, and output contracts aligned with current deploy behavior.
2. Verify Pages root and `/slides/` URLs after any workflow or artifact-path change.
3. Update web UI or static assets while preserving usability and responsiveness.
<!-- repo-agent-bootstrap:managed:end -->
