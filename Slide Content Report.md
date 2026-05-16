# Slide Content Comparison Report

## Executive Summary
This report compares the backup slide directories with the new main lessons/slides directories.

- **Total Files Compared:** 34
- **Total Slides Added:** 10
- **Total Slides Removed:** 0
- **Total Text Lines Changed:** 281

### Coverage & Concept Analysis
Overall, the new directories show a net increase in content, suggesting expanded coverage or added concepts.

## Basics Course Comparison
- Files compared: 22
- Files added: 0
- Files removed: 0
- Slides Added: 5
- Slides Removed: 0
- Lines Changed: 142

### Significant File Differences

#### `index.html`
- Slides: +5 / -0
- Lines : +142 / -0
```diff
--- 
+++ 
@@ -0,0 +1,142 @@
+Module 1 · PCEP aligned
+Python Programming: Basic
+Interactive HTML slide decks for Python programming lessons. This module portal keeps the existing day-by-day content map while making the full 48-hour Basics sequence easier to browse by day and artifact.
+Start with Day 1
+Back to course portal
+Continue to Advanced
+12
+day decks
+12
+lecture sets
+12
+homework notebooks
+12
+HTML quizzes
+Theme
+Appearance
+Auto
+Light
+Dark
+Module notes
+Day-deck links stay static and relative so this page works both from the source tree and from the published Basics portal path. Manifest data enhances badges and repository artifact links when JavaScript is available.
+Basics day grid
+The day descriptions and lecture-file references below remain the core content map for the module. The shared portal layer adds theme persistence, repository artifact links, and manifest-backed badge status without replacing the direct deck links.
+Day 1 — Session 1 (Hours 1–4)
+Open Presentation
+Comprehensive basics covering environment setup, print(), variables, and operators
+59-slide session deck
+Slides ✓
+Lecture ✓
+Assignment ✓
+Quiz ✓
+Per-hour lecture source files: lecture/Day1_Hour1_Basics.md through lecture/Day1_Hour4_Basics.md
+Repository artifact links load here when JavaScript is available.
+Day 2 — Session 2 (Hours 5–8)
+Open Full Session Presentation
+Strings (indexing, slicing, methods), Input/Output, Type conversion, and Checkpoint 1
+74-slide session deck
+Slides ✓
+Lecture ✓
+Assignment ✓
+Quiz ✓
+Per-hour lecture source files: lecture/Day2_Hour1_Basics.md through Day2_Hour4_Basics.md (runbook Session 2 / course Hours 5–8; HTML deck covers full session)
+Repository artifact links load here when JavaScript is available.
+Day 3 — Session 3 (Hours 9–12)
+Open Full Session Presentation
+Comparisons & boolean logic, f-string formatting, split/join text processing, and debugging habits
+48-slide session deck
... (diff truncated)
```

## Advanced Course Comparison
- Files compared: 12
- Files added: 1
  - `+ index.html`
- Files removed: 0
- Slides Added: 5
- Slides Removed: 0
- Lines Changed: 139

### Significant File Differences

#### `index.html`
- Slides: +5 / -0
- Lines : +139 / -0
```diff
+ Module 2 · Applied project track
+ Python Programming: Advanced
+ Interactive HTML slide decks for the project-focused half of the course. This portal organizes the Advanced track across object design, GUI development, sqlite, REST APIs, analytics, testing, and delivery.
+ Start with Day 1
+ Jump to final review
+ Back to course portal
+ 12
+ day decks
+ 12
+ lecture sets
+ 12
+ homework notebooks
+ 12
+ HTML quizzes
+ Theme
+ Appearance
+ Auto
+ Light
+ Dark
+ Module notes
+ Advanced keeps the same static-first portal structure as Basics, but frames the work as an applied build track. Need a fundamentals refresher? Reopen the
+ Basics module portal.
+ Advanced day grid
+ Each day card points directly to the session deck while preserving the runbook-aligned topic map. Manifest enhancement fills in artifact status and repository links without changing the published deck routes.
+ Day 1 — Session 1 (Hours 1–4)
+ Open Presentation
+ Advanced kickoff, class design from requirements, invariants, custom exceptions, and composition vs inheritance
+ Slides
+ Lecture
+ Assignment
+ Quiz
+ Per-hour lecture source files: lecture/Day1_Hour1_Advanced.md through lecture/Day1_Hour4_Advanced.md
+ Repository artifact links load here when JavaScript is available.
+ Day 2 — Session 2 (Hours 5–8)
+ Open Presentation
+ Factory and Strategy patterns, class ergonomics, type hints, and Checkpoint 1 for the domain plus service layer
+ Slides
+ Lecture
+ Assignment
+ Quiz
+ Per-hour lecture source files: lecture/Day2_Hour1_Advanced.md through lecture/Day2_Hour4_Advanced.md
+ Repository artifact links load here when JavaScript is available.
+ Day 3 — Session 3 (Hours 9–12)
+ Open Presentation
+ Project structure, packages, logging, safer file operations with context managers, and decorators for timing, validation, or authorization
+ Slides
+ Lecture
+ Assignment
+ Quiz
+ Per-hour lecture source files: lecture/Day3_Hour1_Advanced.md through lecture/Day3_Hour4_Advanced.md
... (diff truncated)
```