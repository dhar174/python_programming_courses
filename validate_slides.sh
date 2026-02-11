#!/bin/bash

echo "==================================================================="
echo "VALIDATING GENERATED HTML SLIDE DECKS"
echo "==================================================================="
echo ""

# Default to Basics/lessons/slides, but allow override via first argument
slides_dir="${1:-Basics/lessons/slides}"

echo "Validating slides in: $slides_dir"
echo ""

for html_file in "$slides_dir"/*.html; do
    if [ -f "$html_file" ]; then
        filename=$(basename "$html_file")
        echo "Checking: $filename"
        echo "-------------------------------------------------------------------"
        
        # Count slides
        slide_count=$(grep -c 'class="slide' "$html_file")
        echo "  ✓ Slides found: $slide_count"
        
        # Check for CSS variables
        css_vars=$(grep -c "CSS VARIABLES" "$html_file")
        if [ $css_vars -gt 0 ]; then
            echo "  ✓ CSS variables: Present"
        else
            echo "  ✗ CSS variables: Missing"
        fi
        
        # Check for keyboard navigation
        kbd_nav=$(grep -c "ArrowRight" "$html_file")
        if [ $kbd_nav -gt 0 ]; then
            echo "  ✓ Keyboard navigation: Implemented"
        else
            echo "  ✗ Keyboard navigation: Missing"
        fi
        
        # Check for touch support
        touch_nav=$(grep -c "touchstart" "$html_file")
        if [ $touch_nav -gt 0 ]; then
            echo "  ✓ Touch/swipe support: Implemented"
        else
            echo "  ✗ Touch/swipe support: Missing"
        fi
        
        # Check for progress bar
        progress=$(grep -c "progress-bar" "$html_file")
        if [ $progress -gt 0 ]; then
            echo "  ✓ Progress bar: Present"
        else
            echo "  ✗ Progress bar: Missing"
        fi
        
        # Check for slide counter
        counter=$(grep -c "slide-counter" "$html_file")
        if [ $counter -gt 0 ]; then
            echo "  ✓ Slide counter: Present"
        else
            echo "  ✗ Slide counter: Missing"
        fi
        
        # Check for navigation hint
        nav_hint=$(grep -c "nav-hint" "$html_file")
        if [ $nav_hint -gt 0 ]; then
            echo "  ✓ Navigation hint: Present"
        else
            echo "  ✗ Navigation hint: Missing"
        fi
        
        # Check for no external dependencies
        external_deps=$(grep -o -E "(https?://|<link[^>]*href=|<script[^>]*src=)" "$html_file" 2>/dev/null | wc -l)
        if [ "$external_deps" -eq 0 ]; then
            echo "  ✓ No external dependencies"
        else
            echo "  ⚠ External dependencies detected: $external_deps"
        fi
        
        # Check file size
        size=$(du -h "$html_file" | cut -f1)
        echo "  ✓ File size: $size"
        
        # Check for title slide
        title_slide=$(grep -c "title-slide" "$html_file")
        if [ $title_slide -gt 0 ]; then
            echo "  ✓ Title slide: Present"
        else
            echo "  ✗ Title slide: Missing"
        fi
        
        echo ""
    fi
done

echo "==================================================================="
echo "VALIDATION COMPLETE"
echo "==================================================================="
