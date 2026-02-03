#!/usr/bin/env python3
"""
Markdown to HTML Slide Deck Generator
Converts Markdown lessons to standalone HTML presentations
"""

import re
from pathlib import Path
from html import escape

# HTML Template with Swiss Modern styling
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* ====================================
           CSS VARIABLES - TWEAK GUIDE
           ==================================== */
        :root {{
            /* Colors - Swiss Modern Palette */
            --bg: #f7f7f7;              /* Main background (light gray) */
            --fg: #111111;              /* Main text color (near black) */
            --accent: #0066ff;          /* Accent color (blue) */
            --accent-light: #e6f0ff;    /* Light accent background */
            --code-bg: #1e1e1e;         /* Code block background (dark) */
            --code-fg: #f8f8f2;         /* Code text color (light) */
            --border: #cccccc;          /* Border color */
            --shadow: rgba(0, 0, 0, 0.1); /* Shadow color */
            
            /* Typography */
            --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
            --font-heading: "Inter", system-ui, -apple-system, sans-serif;
            --font-code: "SF Mono", "Monaco", "Consolas", monospace;
            
            /* Spacing */
            --spacing: 24px;            /* Base spacing unit */
            --slide-padding: 60px;      /* Padding inside slides */
            
            /* Animation timing */
            --transition-speed: 0.3s;   /* Slide transition duration */
        }}
        
        /* ====================================
           BASE STYLES
           ==================================== */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: var(--font-body);
            background: var(--bg);
            color: var(--fg);
            line-height: 1.6;
            overflow: hidden;
        }}
        
        /* ====================================
           SLIDE CONTAINER
           ==================================== */
        #slides-container {{
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }}
        
        /* ====================================
           INDIVIDUAL SLIDES
           ==================================== */
        .slide {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            padding: var(--slide-padding);
            display: flex;
            flex-direction: column;
            justify-content: center;
            opacity: 0;
            transform: translateX(100%);
            transition: opacity var(--transition-speed) ease,
                        transform var(--transition-speed) ease;
        }}
        
        .slide.active {{
            opacity: 1;
            transform: translateX(0);
            z-index: 10;
        }}
        
        .slide.previous {{
            opacity: 0;
            transform: translateX(-100%);
        }}
        
        /* Title slide special styling */
        .slide.title-slide {{
            background: linear-gradient(135deg, var(--accent) 0%, #0052cc 100%);
            color: white;
            text-align: center;
            justify-content: center;
        }}
        
        .slide.title-slide h1 {{
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: calc(var(--spacing) * 2);
            line-height: 1.2;
        }}
        
        .slide.title-slide .subtitle {{
            font-size: 1.5rem;
            opacity: 0.9;
            font-weight: 300;
        }}
        
        /* ====================================
           TYPOGRAPHY
           ==================================== */
        h1, h2, h3, h4, h5, h6 {{
            font-family: var(--font-heading);
            font-weight: 600;
            line-height: 1.2;
            margin-bottom: var(--spacing);
        }}
        
        .slide:not(.title-slide) h1 {{
            font-size: 2.5rem;
            color: var(--accent);
            border-bottom: 3px solid var(--accent);
            padding-bottom: calc(var(--spacing) / 2);
        }}
        
        .slide h2 {{
            font-size: 2rem;
            margin-top: calc(var(--spacing) * 1.5);
        }}
        
        .slide h3 {{
            font-size: 1.5rem;
            margin-top: var(--spacing);
        }}
        
        p {{
            margin-bottom: var(--spacing);
            font-size: 1.2rem;
            max-width: 900px;
        }}
        
        /* ====================================
           LISTS
           ==================================== */
        ul, ol {{
            margin-left: calc(var(--spacing) * 1.5);
            margin-bottom: var(--spacing);
            max-width: 900px;
        }}
        
        li {{
            margin-bottom: calc(var(--spacing) / 2);
            font-size: 1.2rem;
            line-height: 1.6;
        }}
        
        ul li {{
            list-style-type: none;
            position: relative;
            padding-left: calc(var(--spacing) * 1.5);
        }}
        
        ul li::before {{
            content: "→";
            position: absolute;
            left: 0;
            color: var(--accent);
            font-weight: bold;
        }}
        
        /* Nested lists */
        ul ul, ol ol {{
            margin-top: calc(var(--spacing) / 2);
            margin-bottom: calc(var(--spacing) / 2);
        }}
        
        /* ====================================
           CODE BLOCKS
           ==================================== */
        pre {{
            background: var(--code-bg);
            color: var(--code-fg);
            padding: var(--spacing);
            border-radius: 8px;
            overflow-x: auto;
            margin-bottom: var(--spacing);
            box-shadow: 0 4px 6px var(--shadow);
            max-width: 1000px;
        }}
        
        code {{
            font-family: var(--font-code);
            font-size: 1rem;
            line-height: 1.5;
        }}
        
        /* Inline code */
        p code, li code {{
            background: var(--accent-light);
            color: var(--accent);
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.9em;
        }}
        
        /* ====================================
           BLOCKQUOTES
           ==================================== */
        blockquote {{
            border-left: 4px solid var(--accent);
            padding-left: var(--spacing);
            margin: var(--spacing) 0;
            font-style: italic;
            color: #555;
            background: var(--accent-light);
            padding: var(--spacing);
            border-radius: 4px;
        }}
        
        /* ====================================
           IMAGES
           ==================================== */
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 6px var(--shadow);
            margin: var(--spacing) 0;
        }}
        
        /* ====================================
           LINKS
           ==================================== */
        a {{
            color: var(--accent);
            text-decoration: none;
            border-bottom: 2px solid transparent;
            transition: border-color 0.2s;
        }}
        
        a:hover {{
            border-bottom-color: var(--accent);
        }}
        
        /* ====================================
           NAVIGATION CONTROLS
           ==================================== */
        #nav-hint {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 12px 20px;
            border-radius: 20px;
            font-size: 0.9rem;
            z-index: 100;
            opacity: 0.8;
            transition: opacity 0.3s;
        }}
        
        #nav-hint:hover {{
            opacity: 1;
        }}
        
        #progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: var(--accent);
            z-index: 100;
            transition: width 0.3s ease;
        }}
        
        #slide-counter {{
            position: fixed;
            bottom: 30px;
            left: 30px;
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            z-index: 100;
        }}
        
        /* ====================================
           RESPONSIVE DESIGN
           ==================================== */
        @media (max-width: 768px) {{
            .slide {{
                padding: 30px;
            }}
            
            .slide.title-slide h1 {{
                font-size: 2.5rem;
            }}
            
            .slide h1 {{
                font-size: 2rem;
            }}
            
            .slide h2 {{
                font-size: 1.5rem;
            }}
            
            p, li {{
                font-size: 1rem;
            }}
        }}
        
        /* ====================================
           SPECIAL ELEMENTS
           ==================================== */
        hr {{
            border: none;
            border-top: 2px solid var(--border);
            margin: calc(var(--spacing) * 2) 0;
        }}
        
        strong, b {{
            font-weight: 600;
            color: var(--accent);
        }}
        
        em, i {{
            font-style: italic;
        }}
        
        /* Checkmarks and X marks for task lists */
        .check {{
            color: #22c55e;
            font-weight: bold;
        }}
        
        .cross {{
            color: #ef4444;
            font-weight: bold;
        }}
        
        /* Warning/Alert styling */
        .warning {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: var(--spacing);
            margin: var(--spacing) 0;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <div id="slides-container">
        {slides}
    </div>
    
    <div id="progress-bar"></div>
    <div id="slide-counter"><span id="current">1</span> / <span id="total">1</span></div>
    <div id="nav-hint">← → or Space to navigate</div>
    
    <script>
        // ====================================
        // SLIDE NAVIGATION
        // ====================================
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        const progressBar = document.getElementById('progress-bar');
        const currentCounter = document.getElementById('current');
        const totalCounter = document.getElementById('total');
        
        // Initialize
        totalCounter.textContent = totalSlides;
        
        function updateSlideDisplay() {{
            // Hide all slides
            slides.forEach((slide, index) => {{
                slide.classList.remove('active', 'previous');
                if (index < currentSlide) {{
                    slide.classList.add('previous');
                }}
            }});
            
            // Show current slide
            if (slides[currentSlide]) {{
                slides[currentSlide].classList.add('active');
            }}
            
            // Update progress bar
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            progressBar.style.width = progress + '%';
            
            // Update counter
            currentCounter.textContent = currentSlide + 1;
            
            // Update URL hash (for bookmarking)
            window.location.hash = currentSlide + 1;
        }}
        
        function nextSlide() {{
            if (currentSlide < totalSlides - 1) {{
                currentSlide++;
                updateSlideDisplay();
            }}
        }}
        
        function prevSlide() {{
            if (currentSlide > 0) {{
                currentSlide--;
                updateSlideDisplay();
            }}
        }}
        
        function goToSlide(index) {{
            if (index >= 0 && index < totalSlides) {{
                currentSlide = index;
                updateSlideDisplay();
            }}
        }}
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            switch(e.key) {{
                case 'ArrowRight':
                case ' ':
                case 'PageDown':
                    e.preventDefault();
                    nextSlide();
                    break;
                case 'ArrowLeft':
                case 'PageUp':
                    e.preventDefault();
                    prevSlide();
                    break;
                case 'Home':
                    e.preventDefault();
                    goToSlide(0);
                    break;
                case 'End':
                    e.preventDefault();
                    goToSlide(totalSlides - 1);
                    break;
            }}
        }});
        
        // Touch/swipe support for mobile
        let touchStartX = 0;
        let touchEndX = 0;
        
        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.changedTouches[0].screenX;
        }});
        
        document.addEventListener('touchend', (e) => {{
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }});
        
        function handleSwipe() {{
            const swipeThreshold = 50;
            if (touchEndX < touchStartX - swipeThreshold) {{
                nextSlide();
            }}
            if (touchEndX > touchStartX + swipeThreshold) {{
                prevSlide();
            }}
        }}
        
        // Load slide from URL hash
        window.addEventListener('load', () => {{
            const hash = window.location.hash.slice(1);
            if (hash) {{
                const slideNum = parseInt(hash) - 1;
                if (!isNaN(slideNum)) {{
                    goToSlide(slideNum);
                    return;
                }}
            }}
            updateSlideDisplay();
        }});
        
        // Initialize first slide
        updateSlideDisplay();
    </script>
</body>
</html>"""


class MarkdownSlideParser:
    """Parse Markdown and convert to HTML slides"""
    
    def __init__(self, markdown_text, filename):
        self.markdown_text = markdown_text
        self.filename = filename
        self.slides = []
        
    def parse(self):
        """Main parsing method"""
        lines = self.markdown_text.split('\n')
        
        # Skip YAML frontmatter if present (between --- markers at start)
        start_index = 0
        if lines and lines[0].strip() == '---':
            # Find the closing ---
            for j in range(1, len(lines)):
                if lines[j].strip() == '---':
                    start_index = j + 1
                    break
        
        current_slide = {'type': 'content', 'title': '', 'content': []}
        in_code_block = False
        code_block_content = []
        code_language = ''
        first_h1 = True
        
        i = start_index
        while i < len(lines):
            line = lines[i]
            
            # Handle code blocks
            if line.strip().startswith('```'):
                if not in_code_block:
                    # Start of code block
                    in_code_block = True
                    code_language = line.strip()[3:].strip()
                    code_block_content = []
                else:
                    # End of code block
                    in_code_block = False
                    code_html = self._render_code_block(code_block_content, code_language)
                    current_slide['content'].append(code_html)
                    code_block_content = []
                    code_language = ''
                i += 1
                continue
            
            if in_code_block:
                code_block_content.append(line)
                i += 1
                continue
            
            # Skip horizontal rules (but not frontmatter, handled above)
            if line.strip() in ['---', '***', '___']:
                i += 1
                continue
            
            # H1 - Title slide or section
            if line.startswith('# '):
                if current_slide['title'] or current_slide['content']:
                    self.slides.append(current_slide)
                
                title = line[2:].strip()
                current_slide = {
                    'type': 'title' if first_h1 else 'content',
                    'title': title,
                    'content': []
                }
                first_h1 = False
                
                # Look ahead for subtitle on next line
                if i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].startswith('#'):
                    i += 1
                    subtitle = lines[i].strip()
                    if subtitle and not subtitle.startswith('```'):
                        current_slide['subtitle'] = subtitle
            
            # H2 - New slide
            elif line.startswith('## '):
                if current_slide['title'] or current_slide['content']:
                    self.slides.append(current_slide)
                
                title = line[3:].strip()
                current_slide = {'type': 'content', 'title': title, 'content': []}
            
            # H3 - Subheading within slide
            elif line.startswith('### '):
                heading = f"<h3>{escape(line[4:].strip())}</h3>"
                current_slide['content'].append(heading)
            
            # H4 and below
            elif line.startswith('#### '):
                heading = f"<h4>{escape(line[5:].strip())}</h4>"
                current_slide['content'].append(heading)
            
            # Lists
            elif line.strip().startswith('- ') or line.strip().startswith('* '):
                list_items = [line]
                i += 1
                while i < len(lines) and (lines[i].strip().startswith('- ') or 
                                         lines[i].strip().startswith('* ') or
                                         lines[i].strip().startswith('  ')):
                    list_items.append(lines[i])
                    i += 1
                current_slide['content'].append(self._render_list(list_items))
                continue
            
            # Numbered lists
            elif re.match(r'^\d+\.\s', line.strip()):
                list_items = [line]
                i += 1
                while i < len(lines) and re.match(r'^\d+\.\s', lines[i].strip()):
                    list_items.append(lines[i])
                    i += 1
                current_slide['content'].append(self._render_numbered_list(list_items))
                continue
            
            # Blockquotes
            elif line.strip().startswith('>'):
                quote_text = line.strip()[1:].strip()
                current_slide['content'].append(f"<blockquote>{escape(quote_text)}</blockquote>")
            
            # Regular paragraphs
            elif line.strip():
                # Process inline formatting
                formatted_line = self._process_inline_formatting(line.strip())
                current_slide['content'].append(f"<p>{formatted_line}</p>")
            
            i += 1
        
        # Add last slide
        if current_slide['title'] or current_slide['content']:
            self.slides.append(current_slide)
        
        # If no slides were created, make one from the filename
        if not self.slides:
            self.slides.append({
                'type': 'title',
                'title': self.filename.replace('-', ' ').replace('_', ' ').title(),
                'content': ['<p>No content available</p>']
            })
        
        return self.slides
    
    def _render_code_block(self, lines, language):
        """Render a code block"""
        code_content = escape('\n'.join(lines))
        lang_label = f' data-lang="{language}"' if language else ''
        return f'<pre{lang_label}><code>{code_content}</code></pre>'
    
    def _render_list(self, items):
        """Render an unordered list"""
        html = '<ul>\n'
        for item in items:
            stripped_item = item.strip()
            # Basic indentation check for nested items
            if item.startswith('  ') and (stripped_item.startswith('- ') or stripped_item.startswith('* ')):
                content = stripped_item[2:].strip()
                html += f'  <li style="margin-left: 30px;">{self._process_inline_formatting(content)}</li>\n'
            elif stripped_item.startswith('- ') or stripped_item.startswith('* '):
                content = stripped_item[2:].strip()
                html += f'  <li>{self._process_inline_formatting(content)}</li>\n'
        html += '</ul>'
        return html
    
    def _render_numbered_list(self, items):
        """Render an ordered list"""
        html = '<ol>\n'
        for item in items:
            content = re.sub(r'^\d+\.\s', '', item.strip())
            html += f'  <li>{self._process_inline_formatting(content)}</li>\n'
        html += '</ol>'
        return html
    
    def _process_inline_formatting(self, text):
        """Process inline Markdown formatting"""
        # Escape HTML first
        text = escape(text)
        
        # Bold with **
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        
        # Italic with *
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        
        # Inline code with `
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        
        # Links [text](url)
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
        
        # Checkmarks ✓
        text = text.replace('✓', '<span class="check">✓</span>')
        text = text.replace('✗', '<span class="cross">✗</span>')
        
        # Warning markers
        text = text.replace('⚠️', '<strong>⚠️</strong>')
        
        return text
    
    def render_html(self):
        """Render complete HTML document"""
        slides_html = []
        
        for i, slide in enumerate(self.slides):
            if slide['type'] == 'title':
                # Title slide
                title = escape(slide['title'])
                subtitle = ''
                if 'subtitle' in slide:
                    subtitle = f'<div class="subtitle">{escape(slide["subtitle"])}</div>'
                
                slide_html = f'''
        <section class="slide title-slide">
            <h1>{title}</h1>
            {subtitle}
        </section>'''
            else:
                # Content slide
                title = escape(slide['title']) if slide['title'] else ''
                title_html = f'<h1>{title}</h1>' if title else ''
                content_html = '\n'.join(slide['content'])
                
                slide_html = f'''
        <section class="slide">
            {title_html}
            {content_html}
        </section>'''
            
            slides_html.append(slide_html)
        
        # Get title for the document
        doc_title = self.slides[0]['title'] if self.slides else self.filename
        
        # Render complete HTML
        html = HTML_TEMPLATE.format(
            title=escape(doc_title),
            slides='\n'.join(slides_html)
        )
        
        return html


def process_markdown_file(input_path, output_dir):
    """Process a single Markdown file and generate HTML slides"""
    try:
        # Read the Markdown file
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Get base filename without extension
        basename = Path(input_path).stem
        
        # Parse and convert to HTML
        parser = MarkdownSlideParser(markdown_content, basename)
        parser.parse()
        html_content = parser.render_html()
        
        # Write HTML file
        output_path = output_dir / f"{basename}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return True, output_path, len(parser.slides)
    
    except Exception as e:
        return False, str(e), 0


def main():
    """Main execution function"""
    # Dynamically determine repository root
    script_dir = Path(__file__).parent.resolve()
    repo_root = script_dir
    output_dir = repo_root / 'slides'
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Find all Markdown files
    source_dirs = [
        repo_root / 'Basics' / 'lessons',
        repo_root / 'Advanced' / 'lessons'
    ]
    
    markdown_files = []
    for source_dir in source_dirs:
        if source_dir.exists():
            markdown_files.extend(source_dir.glob('**/*.md'))
    
    if not markdown_files:
        print("No Markdown lessons found under Basics/lessons or Advanced/lessons.")
        return
    
    print(f"Found {len(markdown_files)} Markdown file(s):\n")
    
    # Process each file
    results = []
    for md_file in markdown_files:
        print(f"Processing: {md_file.relative_to(repo_root)}")
        success, output_or_error, slide_count = process_markdown_file(md_file, output_dir)
        
        if success:
            results.append({
                'input': md_file.relative_to(repo_root),
                'output': output_or_error.relative_to(repo_root),
                'slides': slide_count,
                'success': True
            })
            print(f"  ✓ Generated: {output_or_error.relative_to(repo_root)} ({slide_count} slides)")
        else:
            results.append({
                'input': md_file.relative_to(repo_root),
                'error': output_or_error,
                'success': False
            })
            print(f"  ✗ Error: {output_or_error}")
        print()
    
    # Summary
    print("=" * 70)
    print("GENERATION SUMMARY")
    print("=" * 70)
    
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    if successful:
        print(f"\n✓ Successfully generated {len(successful)} HTML slide deck(s):\n")
        for result in successful:
            print(f"  • {result['output']} ({result['slides']} slides)")
    
    if failed:
        print(f"\n✗ Failed to process {len(failed)} file(s):\n")
        for result in failed:
            print(f"  • {result['input']}: {result['error']}")
    
    print(f"\n📁 Output directory: {output_dir.relative_to(repo_root)}")
    print("\n" + "=" * 70)
    print("CUSTOMIZATION GUIDE")
    print("=" * 70)
    print("""
To customize the appearance of your slides, edit the CSS variables at the
top of any generated HTML file:

Colors:
  --bg: Background color
  --fg: Text color
  --accent: Accent color (headings, bullets, links)
  --code-bg: Code block background
  --code-fg: Code text color

Typography:
  --font-body: Body text font family
  --font-heading: Heading font family
  --font-code: Code font family

Spacing:
  --spacing: Base spacing unit (affects margins/padding)
  --slide-padding: Padding inside each slide

Animation:
  --transition-speed: Slide transition duration

Navigation:
  Arrow keys (← →) or Space/Shift+Space to navigate
  Home/End to jump to first/last slide
  Touch/swipe gestures on mobile devices
""")


if __name__ == '__main__':
    main()
