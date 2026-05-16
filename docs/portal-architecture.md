# Portal Architecture Contract

**Epic:** #419  
**Issue:** #420  
**Status:** Approved architecture target for issues #421-#425

## 1. Authority and relationship to other docs

This document is the authoritative contract for:

- portal information architecture and page inventory
- published route and path semantics
- manifest ownership and schema
- root and module entrypoint ownership
- rollout gates between issues #421-#425

`spec/spec-process-cicd-marp-action.md` remains the authoritative reference for workflow job shape, permissions, artifact staging, and deployment flow.

If portal entrypoint or fallback behavior changes, this document, `spec/spec-process-cicd-marp-action.md`, and `.github/workflows/marp-action.yml` must be updated together in the same pull request.

## 2. Goals and non-goals

### Goals

- deliver a static, GitHub Pages-compatible course portal with a stable root page and two module landing pages
- define a manifest rich enough that downstream pages do not hardcode day ordering, breadcrumbs, or artifact badges
- preserve fallback safety while the portal is rolled out incrementally
- keep the implementation zero-CDN, zero-framework, and offline-friendly

### Non-goals for this epic

- introducing a frontend framework, bundler, remote fonts, or analytics
- requiring day-level overview pages as a separate page type in this rollout
- publishing lecture notebooks, assignments, or quizzes into Pages unless a later issue adds explicit workflow support
- changing portal copy beyond small implementation-driven wording fixes

## 3. Current-state constraints

| Area | Current reality | Why it matters |
| --- | --- | --- |
| Basics module root | `Basics/lessons/slides/index.html` is both the current Basics landing page and a fallback input to the Pages root entrypoint logic. | Rebuilding Basics without decoupling root ownership could silently replace `/`. |
| Advanced module root | `Advanced/lessons/slides/` has day folders but no module `index.html`. | #423 must add the first Advanced landing page. |
| Workflow fallback | `marp-action.yml` has three distinct behaviors: Basics module fallback copy, Advanced module fallback copy, and root `_site/index.html` synthesis. | The contract must address all three behaviors, not only Basics. |
| Published artifact scope | The Pages artifact currently guarantees slide trees under `_site/slides/**`. Lecture Markdown, assignments, and quizzes are not copied into the artifact. | Artifact badges and links must distinguish between Pages-hosted assets and repository-hosted assets. |
| Ordering signal | Module day folders already use zero-padded `day-01` through `day-12` names. | The manifest can use numeric day order instead of guessing from titles. |
| Theme sources | `Basics/themes/python-light.css` and `python-dark.css` define the current semantic token names, while `Basics/lessons/slides/day-01/day-01-session-1.html` establishes the requested visual language. | #421 needs a shared portal token layer that preserves dark/light parity and reflects the day-01 aesthetic. |

## 4. Target sitemap and page inventory

The finished portal for this epic uses a small set of stable pages.

| Surface | Source path | Staged artifact path | Published URL | Notes |
| --- | --- | --- | --- | --- |
| Course root dashboard | `slides/index.html` | `_site/index.html` | `${BASE_PATH}` | Introduced as a dedicated root entrypoint in #421, then upgraded in #424. |
| Basics module landing page | `Basics/lessons/slides/index.html` | `_site/slides/basics/index.html` | `${BASE_PATH}slides/basics/` | Rebuilt in #422. |
| Advanced module landing page | `Advanced/lessons/slides/index.html` | `_site/slides/advanced/index.html` | `${BASE_PATH}slides/advanced/` | Created in #423. |
| Basics day overview pages | `Basics/lessons/slides/day-XX/index.html` | `_site/slides/basics/day-XX/index.html` | `${BASE_PATH}slides/basics/day-XX/index.html` | Generated from structured metadata; module day cards route here before decks. |
| Advanced day overview pages | `Advanced/lessons/slides/day-XX/index.html` | `_site/slides/advanced/day-XX/index.html` | `${BASE_PATH}slides/advanced/day-XX/index.html` | Generated from structured metadata; module day cards route here before decks. |
| Shared portal asset kit | `slides/shared/portal/**` | `_site/slides/shared/portal/**` | `${BASE_PATH}slides/shared/portal/**` | Added in #421. |
| Printable full-course index | `slides/printable-index.html` | `_site/slides/printable-index.html` | `${BASE_PATH}slides/printable-index.html` | Implemented in #424 as the compact full-course deck index. |
| Custom 404 page | `slides/404.html` | `_site/404.html` | `${BASE_PATH}404.html` | Implemented in #424 as the course-portal recovery page. |

The following are explicitly **not** required as separate page types in this epic:

- dedicated search-results pages
- lecture/assignment/quiz render pages inside the Pages artifact

Search is an enhancement inside the root or module pages. Day navigation starts on module landing cards, continues through generated day overview pages, and opens the underlying deck through explicit slide CTAs.

## 5. URL and path contract

### 5.1 Base path

Portal pages must treat the site root as a runtime variable named `BASE_PATH`.

- On GitHub Pages project-site deploys, `BASE_PATH` is the repository path prefix ending in `/python_programming_courses/`.
- On local preview served from the repository root with a static HTTP server, `BASE_PATH` is `/`.
- On staged artifact preview served from `_site`, `BASE_PATH` is `/`.
- Raw `file://` preview is unsupported for manifest-driven portal pages.

### 5.2 Path rules

1. Manifest paths are stored without a leading slash and are relative to `BASE_PATH`.
2. Same-tree links inside module slide folders may remain relative when they stay within the copied module tree, for example `day-01/day-01-session-1.html`.
3. Cross-module links, shared-asset links, root-dashboard links, and download links must resolve through `BASE_PATH` rather than `../` arithmetic.
4. Portal pages may use a tiny inline bootstrap script to resolve `BASE_PATH` before attaching shared CSS or JS URLs.
5. Local preview for manifest-driven pages must use a static server such as `python -m http.server`; direct file opening is not part of the contract.

### 5.3 Delivery modes for links

Each artifact link must declare one of these delivery modes:

- `pages` - asset is published in the Pages artifact and opens under `BASE_PATH`
- `repo` - asset is discovered in the repository and should open via a GitHub repository URL
- `none` - asset is absent and should render as unavailable

This distinction prevents the portal from pretending that every artifact is already part of the Pages artifact.

## 6. Shared asset and deployment contract

### 6.1 Canonical shared asset location

The canonical shared portal asset source is:

- `slides/shared/portal/portal.css`
- `slides/shared/portal/portal.js`
- `slides/shared/portal/course-manifest.json`

This location is shared by the root dashboard and both module landing pages. Shared assets are reusable by design and must not be copied manually into Basics or Advanced pages.

### 6.2 Workflow implications

Issue #421 must update workflow behavior to make the shared asset contract real:

1. add trigger coverage for `slides/index.html`, `slides/shared/portal/**`, and any approved supporting pages under `slides/`
2. copy `slides/shared/portal/**` into `_site/slides/shared/portal/**`
3. copy `slides/index.html` into `_site/index.html` once the dedicated root entrypoint exists
4. copy `slides/printable-index.html` into `_site/slides/printable-index.html` if the printable index is implemented
5. copy `slides/404.html` to `_site/404.html` if the custom 404 page is implemented
6. preserve the existing module fallback copies unless a later workflow change intentionally replaces them

Until #421 lands, no page may depend on the shared asset kit.

## 7. Manifest contract

### 7.1 Canonical file

The canonical navigation and artifact manifest is `slides/shared/portal/course-manifest.json`.

### 7.2 Ordering authority

Ordering is defined as follows:

1. module order is `basics`, then `advanced`
2. day order comes from the numeric `day-01` through `day-12` directory names, not from alphabetical title sorting
3. artifact display order is `slides`, `lecture`, `assignment`, `quiz`, `syllabus`, then `downloads`

Portal pages must never infer order from rendered text.

### 7.3 Required schema

```json
{
  "version": 1,
  "repository": {
    "owner": "dhar174",
    "name": "python_programming_courses",
    "defaultBranch": "main"
  },
  "supportingPages": {
    "root": "index.html",
    "printableIndex": "slides/printable-index.html",
    "notFound": "404.html"
  },
  "modules": [
    {
      "id": "basics",
      "title": "Python Programming: Basic",
      "order": 1,
      "sourceRoot": "Basics/lessons/slides",
      "publishedRoot": "slides/basics/",
      "theme": "portal",
      "days": [
        {
          "id": "day-01",
          "dayNumber": 1,
          "title": "Day 1 - Session 1 (Hours 1-4)",
          "order": 1,
          "primaryHref": "slides/basics/day-01/day-01-session-1.html",
          "sourcePrimaryHref": "Basics/lessons/slides/day-01/day-01-session-1.html",
          "overviewHref": "slides/basics/day-01/index.html",
          "sourceOverviewHref": "Basics/lessons/slides/day-01/index.html",
          "breadcrumbs": [
            { "label": "Course", "href": "index.html" },
            { "label": "Basics", "href": "slides/basics/" },
            { "label": "Day 1", "href": "slides/basics/day-01/index.html" }
          ],
          "prev": null,
          "next": {
            "label": "Day 2",
            "href": "slides/basics/day-02/index.html"
          },
          "artifacts": {
            "slides": {
              "present": true,
              "delivery": "pages",
              "href": "slides/basics/day-01/day-01-session-1.html",
              "downloads": {
                "html": "slides/basics/day-01/day-01-session-1.html",
                "pdf": null,
                "pptx": null,
                "png": null
              }
            },
            "lecture": {
              "present": true,
              "delivery": "repo",
              "repoPath": "Basics/lessons/lecture/Day1_Hour1_Basics.md",
              "href": null
            },
            "assignment": {
              "present": true,
              "delivery": "repo",
              "repoPath": "Basics/assignments/Basics_Day1_homework.ipynb",
              "href": null
            },
            "quiz": {
              "present": true,
              "delivery": "repo",
              "repoPath": "Basics/quizzes/Basics_Day1_Quiz.html",
              "href": null
            }
          }
        }
      ]
    }
  ]
}
```

### 7.4 Schema rules

- `supportingPages` values are published paths relative to `BASE_PATH`, not source-repository paths.
- `primaryHref` and `sourcePrimaryHref` identify the actual deck HTML file and must remain stable for deck CTAs and download discovery.
- `overviewHref` and `sourceOverviewHref` identify the generated day overview page when it exists.
- `href` is required only for `pages` delivery.
- `repoPath` is required only for `repo` delivery.
- `present` drives badge visibility and no-JS fallback text.
- `downloads` may include only paths that actually exist; no guessed file names.
- `breadcrumbs`, `prev`, and `next` are authored or generated into the manifest, not hardcoded in page templates.
- `breadcrumbs`, `prev`, and `next` should prefer day overview pages while deck CTAs continue to use the slide artifact href.
- Titles are manifest data, not runtime filename parsing.

## 8. Theme contract

### 8.1 Source of visual direction

Portal visuals must clearly descend from `Basics/lessons/slides/day-01/day-01-session-1.html`, especially its:

- Swiss Modern light palette
- system-ui and Segoe UI body typography with an Inter-like heading feel
- generous spacing rhythm centered on `24px`
- bold blue accent treatment
- restrained `0.3s` motion tone

### 8.2 Semantic token contract

`Basics/themes/python-light.css` and `python-dark.css` remain the semantic token reference for:

- `--bg`
- `--fg`
- `--muted`
- `--accent`
- `--accent-contrast`
- `--code-bg`
- `--code-fg`
- `--code-border`
- `--table-border`
- `--blockquote-bg`
- `--blockquote-border`

Issue #421 must create a portal-specific token layer under `slides/shared/portal/portal.css` that:

- reuses the same semantic token names for parity
- adds portal-only tokens only when both light and dark variants are defined
- does not import the Marp theme files directly into portal pages
- preserves dark/light parity while translating the day-01 visual language into portal-safe styles

Portal text content should remain substantively the same unless a later issue explicitly expands copy scope.

## 9. Fallback and entrypoint contract

The workflow currently has three independent entrypoint decisions. The portal architecture adopts these rules:

| Behavior | Current source | Target contract |
| --- | --- | --- |
| Basics module fallback copy | `Basics/lessons/slides/. -> _site/slides/basics/` | Remains valid. The rebuilt Basics portal continues to own the Basics module landing page. |
| Advanced module fallback copy | `Advanced/lessons/slides/. -> _site/slides/advanced/` | Remains valid once `Advanced/lessons/slides/index.html` exists. |
| Root `_site/index.html` synthesis | Currently prefers `Basics/lessons/slides/index.html` | Must be reassigned to the dedicated root source `slides/index.html` in #421 before #422 merges. |

### Explicit decision

`Basics/lessons/slides/index.html` must **stop** serving as the fallback input for the live site root before or during issue #421.

As a result:

- issue #421 is responsible for introducing a dedicated root source page or stub at `slides/index.html`
- issue #422 must not merge while the workflow still copies `Basics/lessons/slides/index.html` to `_site/index.html`
- issue #424 may replace the root stub with the full course dashboard without changing module ownership

If the root dashboard is temporarily incomplete, the dedicated root source may be a minimal student-safe landing page or redirect, but it must not be the Basics module page.

## 10. Rollout contract for issues #421-#425

| Issue | Required contract from this document |
| --- | --- |
| #421 | establish `BASE_PATH`, publish shared assets, implement the manifest file, and decouple root ownership from the Basics portal |
| #422 | consume the shared kit and manifest, preserve the Basics module fallback contract, and avoid any root-entrypoint regression |
| #423 | reuse the same shared kit and manifest contract without introducing Advanced-only path rules |
| #424 | replace the dedicated root stub with the final course dashboard and add only the supporting pages approved here |
| #425 | verify that workflow, preview, accessibility, navigation, and docs still match this contract |

## 11. Validation and preview contract

Before portal-affecting pull requests merge, the implementation must prove:

- `_site/index.html`, `_site/slides/basics/index.html`, `_site/slides/advanced/index.html`, all generated day overview pages, and `_site/slides/shared/portal/course-manifest.json` all exist when their owning issue has landed
- module fallback copies still produce valid module roots
- the published root entrypoint no longer matches `Basics/lessons/slides/index.html`
- no-JS rendering leaves root and module pages readable
- local preview works through a static HTTP server, not only inside GitHub Pages
- artifact badges do not link to nonexistent Pages outputs

## 12. Decision log

- **D-001:** The root course dashboard owns `/`; module portals own `/slides/basics/` and `/slides/advanced/`.
- **D-002:** The shared portal asset kit lives under `slides/shared/portal/**`.
- **D-003:** The canonical manifest file is `slides/shared/portal/course-manifest.json`.
- **D-004:** Root ownership must be decoupled from `Basics/lessons/slides/index.html` in #421 before the Basics portal rebuild in #422.
- **D-005:** Day ordering is numeric and runbook-aligned through the zero-padded `day-NN` directory names.
- **D-006:** Lecture, assignment, and quiz artifacts may be discovered as `repo` delivery targets until workflow support publishes them to Pages.
- **D-007:** Search is an inline enhancement, not a separate approved page type for this epic.
- **D-008:** Per-day overview pages are now an approved portal page type. Module day cards route to these overview pages; root featured links and the printable index remain direct deck shortcuts.
