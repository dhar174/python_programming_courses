import difflib
from html.parser import HTMLParser
from pathlib import Path


class SlideSectionParser(HTMLParser):
    """Parse HTML and collect section text while preserving block-level line breaks."""

    # Tags that should force a line boundary in the extracted text output.
    BLOCK_TAGS = {
        "address",
        "article",
        "aside",
        "blockquote",
        "div",
        "dl",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "tr",
        "ul",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._all_sections = []
        self._current_section = None
        self._section_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "section":
            if self._section_depth == 0:
                classes = [c for c in attrs_dict.get("class", "").split() if c]
                self._current_section = {"classes": classes, "text_parts": []}
            self._section_depth += 1

        if self._section_depth > 0 and (tag in self.BLOCK_TAGS or tag == "br"):
            self._current_section["text_parts"].append("\n")

    def handle_endtag(self, tag):
        if self._section_depth == 0:
            return

        if tag in self.BLOCK_TAGS:
            self._current_section["text_parts"].append("\n")

        if tag == "section":
            self._section_depth -= 1
            if self._section_depth == 0:
                self._all_sections.append(self._current_section)
                self._current_section = None

    def handle_data(self, data):
        if self._section_depth > 0:
            self._current_section["text_parts"].append(data)

    def extracted_sections(self):
        """Return parsed sections, preferring sections with the `slide` class."""
        sections_with_slide_class = [
            section for section in self._all_sections if "slide" in section["classes"]
        ]
        return sections_with_slide_class if sections_with_slide_class else self._all_sections


def normalize_section_text(text_parts):
    """Normalize extracted text parts into newline-separated, non-empty lines."""
    normalized_lines = []
    for raw_line in "".join(text_parts).splitlines():
        collapsed = " ".join(raw_line.split())
        if collapsed:
            normalized_lines.append(collapsed)
    return "\n".join(normalized_lines)


def extract_slides(html_path):
    """Extract slide text and classes from an HTML file path."""
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    parser = SlideSectionParser()
    parser.feed(html)
    parser.close()

    slides = []
    for section in parser.extracted_sections():
        text = normalize_section_text(section["text_parts"])
        slides.append({"text": text, "classes": section["classes"]})
    return slides


def get_slide_text_lines(slides):
    """Return non-empty text lines across all slides."""
    return [line for line in "\n".join(s["text"] for s in slides).splitlines() if line.strip()]


def compare_directories(backup_dir, new_dir):
    """Compare backup and new slide directories and return aggregate diff metrics."""
    backup_path = Path(backup_dir)
    new_path = Path(new_dir)

    backup_files = {p.relative_to(backup_path): p for p in backup_path.rglob("*.html")}
    new_files = {p.relative_to(new_path): p for p in new_path.rglob("*.html")}

    all_files = set(backup_files.keys()).union(new_files.keys())

    report_data = {
        "files_compared": 0,
        "files_added": [],
        "files_removed": [],
        "total_slides_added": 0,
        "total_slides_removed": 0,
        "total_lines_changed": 0,
        "file_details": {},
    }

    for f in sorted(all_files):
        if f not in backup_files:
            report_data["files_added"].append(str(f))
            new_slides = extract_slides(new_files[f])
            slides_added = len(new_slides)
            added_lines = get_slide_text_lines(new_slides)
            lines_added = len(added_lines)
            report_data["total_slides_added"] += slides_added
            report_data["total_lines_changed"] += lines_added
            report_data["file_details"][str(f)] = {
                "slides_added": slides_added,
                "slides_removed": 0,
                "lines_added": lines_added,
                "lines_removed": 0,
                "text_diff": [f"+ {line}" for line in added_lines[:50]],
            }
            continue

        if f not in new_files:
            report_data["files_removed"].append(str(f))
            old_slides = extract_slides(backup_files[f])
            slides_removed = len(old_slides)
            removed_lines = get_slide_text_lines(old_slides)
            lines_removed = len(removed_lines)
            report_data["total_slides_removed"] += slides_removed
            report_data["total_lines_changed"] += lines_removed
            report_data["file_details"][str(f)] = {
                "slides_added": 0,
                "slides_removed": slides_removed,
                "lines_added": 0,
                "lines_removed": lines_removed,
                "text_diff": [f"- {line}" for line in removed_lines[:50]],
            }
            continue

        report_data["files_compared"] += 1

        old_slides = extract_slides(backup_files[f])
        new_slides = extract_slides(new_files[f])

        old_texts = [s["text"] for s in old_slides]
        new_texts = [s["text"] for s in new_slides]

        diff = list(difflib.ndiff(old_texts, new_texts))

        slides_added = sum(1 for line in diff if line.startswith("+ "))
        slides_removed = sum(1 for line in diff if line.startswith("- "))

        report_data["total_slides_added"] += slides_added
        report_data["total_slides_removed"] += slides_removed

        old_full_text = get_slide_text_lines(old_slides)
        new_full_text = get_slide_text_lines(new_slides)
        text_diff = list(difflib.unified_diff(old_full_text, new_full_text, lineterm=""))

        lines_added = sum(
            1
            for line in text_diff
            if line.startswith("+") and not line.startswith("+++")
        )
        lines_removed = sum(
            1
            for line in text_diff
            if line.startswith("-") and not line.startswith("---")
        )

        report_data["total_lines_changed"] += lines_added + lines_removed

        if slides_added > 0 or slides_removed > 0 or lines_added > 0 or lines_removed > 0:
            report_data["file_details"][str(f)] = {
                "slides_added": slides_added,
                "slides_removed": slides_removed,
                "lines_added": lines_added,
                "lines_removed": lines_removed,
                "text_diff": text_diff[:50],
            }

    return report_data


def generate_report(basics_data, advanced_data):
    """Write markdown summary report from Basics and Advanced comparison data."""
    report = ["# Slide Content Comparison Report\n"]

    report.append("## Executive Summary")
    report.append(
        "This report compares the backup slide directories with the new main lessons/slides directories.\n"
    )

    total_files = basics_data["files_compared"] + advanced_data["files_compared"]
    total_added = basics_data["total_slides_added"] + advanced_data["total_slides_added"]
    total_removed = (
        basics_data["total_slides_removed"] + advanced_data["total_slides_removed"]
    )
    total_lines = basics_data["total_lines_changed"] + advanced_data["total_lines_changed"]

    report.append(f"- **Total Files Compared:** {total_files}")
    report.append(f"- **Total Slides Added:** {total_added}")
    report.append(f"- **Total Slides Removed:** {total_removed}")
    report.append(f"- **Total Text Lines Changed:** {total_lines}")

    report.append("\n### Coverage & Concept Analysis")
    if total_added > total_removed:
        report.append(
            "Overall, the new directories show a net increase in content, suggesting expanded coverage or added concepts."
        )
    elif total_removed > total_added:
        report.append(
            "Overall, the new directories show a net decrease in content, suggesting possible missing concepts, consolidation, or streamlined material."
        )
    else:
        report.append(
            "Overall, the slide count remains stable, though specific concepts may have been rewritten."
        )

    def add_section_data(title, data):
        report.append(f"\n## {title}")
        report.append(f"- Files compared: {data['files_compared']}")
        report.append(f"- Files added: {len(data['files_added'])}")
        for fa in data["files_added"]:
            report.append(f"  - `+ {fa}`")
        report.append(f"- Files removed: {len(data['files_removed'])}")
        for fr in data["files_removed"]:
            report.append(f"  - `- {fr}`")
        report.append(f"- Slides Added: {data['total_slides_added']}")
        report.append(f"- Slides Removed: {data['total_slides_removed']}")
        report.append(f"- Lines Changed: {data['total_lines_changed']}")

        if data["file_details"]:
            report.append("\n### Significant File Differences")
            for filename, details in data["file_details"].items():
                report.append(f"\n#### `{filename}`")
                report.append(
                    f"- Slides: +{details['slides_added']} / -{details['slides_removed']}"
                )
                report.append(
                    f"- Lines : +{details['lines_added']} / -{details['lines_removed']}"
                )
                if details["text_diff"]:
                    report.append("```diff")
                    for line in details["text_diff"]:
                        report.append(line)
                    if len(details["text_diff"]) == 50:
                        report.append("... (diff truncated)")
                    report.append("```")

    add_section_data("Basics Course Comparison", basics_data)
    add_section_data("Advanced Course Comparison", advanced_data)

    with open("Slide Content Report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))


if __name__ == "__main__":
    print("Comparing Basics slides...")
    basics_data = compare_directories(
        "backup_main Basics-lessons_slides", "Basics/lessons/slides"
    )

    print("Comparing Advanced slides...")
    advanced_data = compare_directories(
        "backup_main advanced slides", "Advanced/lessons/slides"
    )

    print("Generating report...")
    generate_report(basics_data, advanced_data)
    print("Report generated at 'Slide Content Report.md'")
