# Python Course HTML Slide Decks

This directory contains standalone HTML slide presentations generated from the course Markdown lessons.

## Generated Files

- **01-intro-to-python.html** - Introduction to Python slides (3 slides)
- **day-01-session-1.html** - Basics Day 1 Session 1 comprehensive lesson (59 slides)
- **day-02-session-2.html** - Basics Day 2 Session 2: Strings, I/O, and Checkpoint 1 (74 slides)

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

To regenerate these slides from the source Markdown files, run:

```bash
python3 generate_slides.py
```

This will scan `Basics/lessons/` and `Advanced/lessons/` for any `.md` files and generate updated HTML slides.

## Technical Details

- **Format:** HTML5 with inline CSS3 and ES6 JavaScript
- **Browser Support:** Modern browsers (Chrome, Firefox, Safari, Edge)
- **No Dependencies:** Zero external libraries or frameworks
- **File Size:** Self-contained, typically 15-40KB per deck
- **Accessibility:** Semantic HTML with keyboard navigation

## Source Files

These slides were generated from:
- `Basics/lessons/01-intro-to-python.md`
- `Basics/lessons/day-01-session-1.md`
- `Basics/lessons/day-02-session-2.md` (combined session file — still present for CI/Marp builds)
- `Advanced/lessons/01-intro-to-python.md`

### Per-Hour Lecture Files (Day 2, Session 2)

The Day 2, Session 2 content has been split into individual per-hour lecture files for easier
instructional use and agent automation. These files live in `Basics/lessons/lecture/`:
- `Basics/lessons/lecture/Day2_Hour5_Basics.md` (String Fundamentals)
- `Basics/lessons/lecture/Day2_Hour6_Basics.md` (String Methods)
- `Basics/lessons/lecture/Day2_Hour7_Basics.md` (Input/Output + Type Conversion)
- `Basics/lessons/lecture/Day2_Hour8_Basics.md` (Checkpoint 1 + Session Wrap-Up)

The compiled `day-02-session-2.html` slide deck was generated from the combined markdown and
covers the full session. Future sessions should follow the per-hour file standard.

---

**Generated:** February 3, 2025  
**Generator:** generate_slides.py  
**Style:** Swiss Modern with CSS Variables
