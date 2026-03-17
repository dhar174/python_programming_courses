# Day 11, Hour 4: Integrate Analytics into the Capstone
**Python Programming Advanced - Session 11**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe analytics as a product feature: 5 minutes  
- Direct instruction on repeatable report pipelines: 15 minutes  
- Live demo of one-command report generation: 10 minutes  
- Guided integration lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Add a report-generation path to the capstone
2. Produce a CSV export, summary artifact, and at least one chart in a repeatable way
3. Document how to run the report feature
4. Explain why a report feature should rely on the same cleaned pipeline each time
5. Treat analytics as part of the product rather than an isolated notebook exercise

---

## Section 1: Analytics as a Feature (5 minutes)

### Opening Script

**[Instructor speaks:]**

The analytics work becomes much more valuable when it is integrated back into the application. A report feature says, \"this project does not just store and retrieve data; it can also summarize and communicate that data intentionally.\"

---

## Section 2: Direct Instruction on Repeatable Reports (15 minutes)

### Report Pipeline

Teach the pipeline explicitly:

1. export data
2. load and clean data
3. compute summaries
4. generate charts
5. save artifacts to `reports/`

Then say:

**[Instructor speaks:]**

If the pipeline only works when you remember hidden manual steps, it is not really repeatable.

### One Command or One Button

Show a simple target such as:

```bash
python -m reports.generate_report
```

Or a GUI button that triggers the same underlying function. The important part is that the path is documented and repeatable.

---

## Section 3: Live Demo (10 minutes)

### Example `generate_report.py`

```python
from reports.export_data import export_records_csv
from reports.analyze import build_summary
from reports.plotting import create_plots


def main():
    csv_path = export_records_csv()
    summary_path = build_summary(csv_path)
    create_plots(summary_path)
    print("Report artifacts generated in reports/")


if __name__ == "__main__":
    main()
```

Narrate:

**[Instructor speaks:]**

This is not a giant reporting system. It is a clear pipeline entry point that generates consistent artifacts.

---

## Section 4: Guided Integration Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Add a real report feature to your capstone. It can be command-line driven or triggered from the GUI, but it must generate artifacts consistently.

### Required Tasks

1. create or refine an export step
2. generate a summary table
3. save at least one chart
4. place outputs in `reports/`
5. document how to run the feature in the README

### Coaching Prompts

- What exact command or action generates the report?
- Which files should appear in `reports/` afterward?
- What manual step can you remove to make the process more repeatable?
- Would another learner know how to run this feature tomorrow?

### Common Mistakes

- hard-coded file paths that only work on one machine
- report logic scattered across notebooks and scripts with no entry point
- missing documentation
- report generation depends on hand-edited intermediate files

### Recovery Script

**[Instructor speaks:]**

If the full report feels too large, build the simplest honest pipeline: export one CSV, generate one summary CSV, save one chart. That already satisfies the course goal if it is repeatable.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Repeatability is the key word from this hour. A report feature becomes useful when someone can run it on demand and trust what it produces.

### Exit Ticket

1. What makes a report feature repeatable?
2. Which artifacts does your report generate?
3. Where did you document how to run it?

### Preview of the Next Session

**[Instructor speaks:]**

Next session we strengthen quality and delivery with pytest, coverage, packaging, and the final capstone demonstration.

---

## Shared Day 11 Instructor Reference

Reuse the shared day-level instructor support from `Day11_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 11 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
