# Python Course HTML Slide Decks

This directory contains standalone HTML slide presentations generated from the course Markdown lessons.

## Generated Files

- **01-intro-to-python.html** - Introduction to Python slides (3 slides)
- **day-01/day-01-session-1.html** - Basics Day 1 Session 1 comprehensive lesson (59 slides)
- **day-02-session-2.html** - Basics Day 2 Session 2: Strings, I/O, and Checkpoint 1 (74 slides)
- **day-03/day-03-session-3.html** - Basics Day 3 Session 3: Comparisons, F-Strings, Text Processing & Debugging (48 slides)
- **day-04/day-04-session-4.html** - Basics Day 4 Session 4: Lists & Iteration — Lists Fundamentals, for Loops, Nested Lists, Checkpoint 2 (53 slides)
- **day-05/day-05-session-5.html** - Basics Day 5 Session 5: Tuples, Sets, and Dictionaries (43 slides)
- **day-06/day-06-session-6.html** - Basics Day 6 Session 6: Data Structure Selection & Mini-Projects — Choosing structures, drill circuit, mini-project tracker, Checkpoint 3 (62 slides)

## Features

All slide decks include:

- ✅ **Standalone HTML** - No external dependencies, all CSS/JS inline
- ✅ **Swiss Modern Design** - Clean, professional styling
- ✅ **Keyboard Navigation** - Arrow keys (← →), Space, Page Up/Down
- ✅ **Touch Support** - Swipe gestures on mobile devices
- ✅ **Progress Indicators** - Progress bar and slide counter
- ✅ **Responsive Layout** - Works on desktop, tablet, and mobile
- ✅ **Code Syntax Highlighting** - Preserved code blocks with dark theme
- ✅ **CSS Variables** - Easy customization of colors, fonts, spacing

## How to Use

### Opening Slides

Simply open any `.html` file in a web browser:
- Double-click the file, or
- Right-click → Open with → Your browser, or
- Drag and drop into an open browser window

### Navigation

**Keyboard:**
- `→` or `Space` - Next slide
- `←` or `Shift+Space` - Previous slide
- `Home` - First slide
- `End` - Last slide
- `Page Down` - Next slide
- `Page Up` - Previous slide

**Mobile/Touch:**
- Swipe left - Next slide
- Swipe right - Previous slide

**URL Bookmarking:**
- The current slide number is saved in the URL (e.g., `#5`)
- Share or bookmark specific slides

## Customization

Each HTML file contains CSS variables at the top that control the appearance. Open any file in a text editor and look for the `:root` section:

```css
:root {
    /* Colors - Swiss Modern Palette */
    --bg: #f7f7f7;              /* Main background */
    --fg: #111111;              /* Main text color */
    --accent: #0066ff;          /* Accent color */
    --code-bg: #1e1e1e;         /* Code background */
    --code-fg: #f8f8f2;         /* Code text color */
    
    /* Typography */
    --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
    --font-heading: "Inter", system-ui, -apple-system, sans-serif;
    --font-code: "SF Mono", "Monaco", "Consolas", monospace;
    
    /* Spacing */
    --spacing: 24px;            /* Base spacing unit */
    --slide-padding: 60px;      /* Padding inside slides */
    
    /* Animation timing */
    --transition-speed: 0.3s;   /* Slide transition speed */
}
```

### Quick Customization Examples

**Dark Mode:**
```css
--bg: #1e1e1e;
--fg: #f0f0f0;
--accent: #4a9eff;
```

**Larger Text:**
```css
--spacing: 32px;
```

**Different Fonts:**
```css
--font-body: "Georgia", serif;
--font-heading: "Arial", sans-serif;
```

**Faster Transitions:**
```css
--transition-speed: 0.15s;
```

## Presentation Tips

1. **Full Screen Mode** - Press F11 (or Fn+F11 on Mac) for distraction-free presenting
2. **Zoom** - Use Ctrl/Cmd + Plus/Minus to adjust text size if needed
3. **Bookmarks** - Share specific slides by copying the URL with #slide-number
4. **Print** - Use browser Print → Save as PDF to create PDF versions
5. **Offline** - All files work completely offline, no internet required

## Regenerating Slides

To regenerate the source-backed standalone HTML slide decks in this directory, run from the repository root:

```bash
python3 Basics/generate_slides.py Basics/lessons/slides
```

This scans `Basics/lessons/slides/**/*.md`, regenerates the source-adjacent HTML files in this directory, and writes the public day-based Basics mirrors under `slides/basics/day-XX/` when applicable.

## Technical Details

- **Format:** HTML5 with inline CSS3 and ES6 JavaScript
- **Browser Support:** Modern browsers (Chrome, Firefox, Safari, Edge)
- **No Dependencies:** Zero external libraries or frameworks
- **File Size:** Self-contained, typically 15-40KB per deck
- **Accessibility:** Semantic HTML with keyboard navigation

## Source Files

These slides were generated from:
- `Basics/lessons/01-intro-to-python.md`
- `Basics/lessons/slides/day-01/day-01-session-1.md`
- `Basics/lessons/day-02-session-2.md` (combined session file — still present for CI/Marp builds)
- `Basics/lessons/slides/day-03/day-03-session-3.md`
- `Advanced/lessons/01-intro-to-python.md`

### Per-Hour Lecture Files (Day 2, Session 2)

The Day 2, Session 2 content has been split into individual per-hour lecture files for easier
instructional use and agent automation. These files live in `Basics/lessons/lecture/`:
- `Basics/lessons/lecture/Day2_Hour1_Basics.md` (String Fundamentals; runbook Session 2 / course Hour 5)
- `Basics/lessons/lecture/Day2_Hour2_Basics.md` (String Methods; runbook Session 2 / course Hour 6)
- `Basics/lessons/lecture/Day2_Hour3_Basics.md` (Input/Output + Type Conversion; runbook Session 2 / course Hour 7)
- `Basics/lessons/lecture/Day2_Hour4_Basics.md` (Checkpoint 1 + Session Wrap-Up; runbook Session 2 / course Hour 8)

The compiled `day-02-session-2.html` slide deck was generated from the combined markdown and
covers the full session. Future sessions should follow the per-hour file standard.

### Per-Hour Lecture Files (Day 3, Session 3)

The Day 3, Session 3 content also has per-hour lecture files in `Basics/lessons/lecture/`:
- `Basics/lessons/lecture/Day3_Hour1_Basics.md` (Comparisons + Boolean Logic)
- `Basics/lessons/lecture/Day3_Hour2_Basics.md` (String Formatting with F-Strings)
- `Basics/lessons/lecture/Day3_Hour3_Basics.md` (Working with Text: split/join)
- `Basics/lessons/lecture/Day3_Hour4_Basics.md` (Debugging Habits)

The compiled `day-03/day-03-session-3.html` slide deck covers the full session.

### Per-Hour Lecture Files (Day 4, Session 4)

The Day 4, Session 4 content also has per-hour lecture files in `Basics/lessons/lecture/`:
- `Basics/lessons/lecture/Day4_Hour1_Basics.md` (Lists Fundamentals — Course Hour 13)
- `Basics/lessons/lecture/Day4_Hour2_Basics.md` (Iterating Lists with for Loops — Course Hour 14)
- `Basics/lessons/lecture/Day4_Hour3_Basics.md` (Nested Lists for Table-Like Data — Course Hour 15)
- `Basics/lessons/lecture/Day4_Hour4_Basics.md` (Checkpoint 2: Lists + String Handling — Course Hour 16)

The compiled `day-04/day-04-session-4.html` slide deck covers the full session.

### Per-Hour Lecture Files (Day 5, Session 5)

The Day 5, Session 5 content also has per-hour lecture files in `Basics/lessons/lecture/`:
- `Basics/lessons/lecture/Day5_Hour1_Basics.md` (Tuples + Unpacking — Course Hour 17)
- `Basics/lessons/lecture/Day5_Hour2_Basics.md` (Sets – Uniqueness + Membership — Course Hour 18)
- `Basics/lessons/lecture/Day5_Hour3_Basics.md` (Dictionaries Fundamentals — Course Hour 19)
- `Basics/lessons/lecture/Day5_Hour4_Basics.md` (Dictionary Iteration + Counting Pattern — Course Hour 20)

The compiled `day-05/day-05-session-5.html` slide deck covers the full session.

### Per-Hour Lecture Files (Day 6, Session 6)

The Day 6, Session 6 content also has per-hour lecture files in `Basics/lessons/lecture/`:
- `Basics/lessons/lecture/Day6_Hour1_Basics.md` (Choosing the Right Structure — Course Hour 21)
- `Basics/lessons/lecture/Day6_Hour2_Basics.md` (Data-Structure Drill Circuit — Course Hour 22)
- `Basics/lessons/lecture/Day6_Hour3_Basics.md` (Mini-Project: In-Memory Tracker — Course Hour 23)
- `Basics/lessons/lecture/Day6_Hour4_Basics.md` (Checkpoint 3: Data Structures Assessment — Course Hour 24)

The compiled `day-06/day-06-session-6.html` slide deck covers the full session.

---

**Generated:** March 13, 2026
**Generator:** `python3 Basics/generate_slides.py Basics/lessons/slides`
**Style:** Swiss Modern with CSS Variables
