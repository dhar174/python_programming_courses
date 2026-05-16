<!-- repo-agent-bootstrap:file-kind=memory-bank -->
<!-- repo-agent-bootstrap:provenance=repo-agent-bootstrap@2026-05-13 -->
<!-- repo-agent-bootstrap:managed:start -->
# Active Context

## Current objective
All 96 hours of course content are written. The final task was fixing the GitHub Pages root 404. That fix has been applied and pushed.

## Why it matters now
The repository is now in a maintenance state. All lecture scripts, slides, and CI/CD are complete. Future work is incremental updates or Advanced slide regeneration.

## Current status
- Done:
  - All 48 Basics lecture scripts (Days 1–12, 4 hours each, ~3000+ words each)
  - All 48 Advanced lecture scripts (Days 1–12, 4 hours each)
  - Per-deck Basics slide regeneration for materially changed days
  - `marp-action.yml` `sudo chown` permission fix (PR #418)
  - Pages root 404 root-cause identified and fixed:
    - `marp-action.yml` now writes root `_site/index.html` as meta-refresh → `./slides/basics/`
    - `marp-action.yml` now copies source index to `_site/slides/basics/index.html` (not root)
    - `Basics/lessons/slides/index.html` updated with Days 5–12 cards and correct Day 2 link
- In progress:
  - none
- Blocked:
  - none

## Relevant files
- `README.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `CLAUDE.md`
- `.github/workflows/marp-action.yml`
- `Basics/lessons/slides/index.html`
- `Basics/lessons/slides/day-*/day-*-session-*.html`
- `Advanced/lessons/slides/day-*/day-*-session-*.html`

## Slide locations (three kinds)
1. `Basics/lessons/slides/day-NN/` — committed agent-built HTML slides (source of truth for Basics)
2. `Advanced/lessons/slides/day-NN/` — committed agent-built HTML slides (source of truth for Advanced)
3. `_site/slides/basics/` + `_site/slides/advanced/` — CI Marp build output, gitignored, deployed to Pages

## Next recommended steps
1. Wait for CI to complete and verify `https://dhar174.github.io/python_programming_courses/` redirects to `/slides/basics/`.
2. Regenerate Advanced slides if Advanced lecture content was changed since generation.
3. Update `README.md` badges/links if the Pages URL is confirmed working.
<!-- repo-agent-bootstrap:managed:end -->

