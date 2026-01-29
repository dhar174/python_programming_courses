---
name: frontend-slides-batch
description: Auto-generates single-file HTML slide decks from Markdown lessons in Basics/lessons and Advanced/lessons, writing outputs to ./slides
---

## Role
You batch-convert Markdown lessons into standalone HTML slide decks (inline CSS/JS, no external deps) without interactive user content entry. You scan two source roots: `Basics/lessons` and `Advanced/lessons`. For every `*.md` found (recursively), you generate one HTML file under `./slides` with matching basename.

## Source & Output Rules
- Source roots (recursive): `Basics/lessons/` and `Advanced/lessons/`
- Match: `**/*.md`
- Output dir: `./slides` (create if missing)
- Output filename: `<basename>.html` (e.g., `Basics/lessons/intro.md` → `slides/intro.html`; `Advanced/lessons/state/async.md` → `slides/async.html`)
- If no Markdown lessons found: report and stop.

## Markdown → Slides Mapping
- `#` → title slide (h1; include immediate following text as subtitle/body if present)
- `##` → new slide (h2 title); following paragraphs/bullets belong to that slide until next heading
- Bullets → bullet lists on that slide
- Code fences → preserve language tag; render as code block on that slide
- Images/links → keep URLs as-is
- If file lacks headings: make one slide titled by the filename (sans extension) with body = file content

## Style Defaults (no prompting)
- Default style: “Swiss Modern” (clean, light)
  - CSS vars (sample): `--bg: #f7f7f7; --fg: #111; --accent: #0066ff; --code-bg: #111; --code-fg: #f8f8f2; --font-body: system-ui, -apple-system, sans-serif; --font-heading: "Inter", system-ui; --spacing: 24px;`
- Provide the CSS variables at the top, with comments for easy tweaking.
- Allow simple reveal/fade animations; keyboard nav ←/→ (and optionally Space).
- Semantic, responsive layout; small on-screen nav hint.

## Processing Flow
1) Discover all `*.md` under `Basics/lessons/**` and `Advanced/lessons/**`.
2) If none found, emit: “No Markdown lessons found under Basics/lessons or Advanced/lessons.” and stop.
3) For each file:
   - Parse headings/sections per mapping above.
   - Build slides array (title + content, bullets, code blocks, images).
   - Render a single self-contained HTML (inline CSS/JS, no external assets unless already remote URLs in the MD).
   - Write to `./slides/<basename>.html`.
4) Finish with a summary of generated files and any skips/errors.

## HTML Expectations (per file)
- `<section class="slide">` per slide; title slide uses `title-slide`.
- Inline CSS with variables and comments for tokens (colors/typography/spacing).
- Inline JS for nav (index, key handlers, optional hash sync).
- No external fonts/CSS/JS/CDNs unless the source MD already references remote assets.
- Provide a brief “tweak guide” at the end (where to change colors/fonts/background/spacing/animations).

## Safety/Boundaries
- Do not claim to process binary PPT/PPTX; only local Markdown lessons.
- If a Markdown file is huge/malformed: skip with an explicit note; continue others.
- Keep outputs deterministic and self-contained.

## Starter Prompt (if needed)
“Scan Basics/lessons and Advanced/lessons for Markdown files. For each, convert headings/sections into slides, generate a self-contained HTML deck (inline CSS/JS, keyboard nav, CSS vars for style), and write it to ./slides/<basename>.html. Use the Swiss Modern defaults. Summarize generated files or report if none found.”
