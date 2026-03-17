# Day 11, Hour 2: Visualization with Matplotlib
**Python Programming Advanced - Session 11**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reconnect to the cleaned dataset: 5 minutes  
- Direct instruction on readable charts: 15 minutes  
- Live build of one or two report-ready plots: 10 minutes  
- Guided plotting lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Create at least one readable chart from capstone data
2. Label axes and titles so the plot can stand on its own
3. Save plots into `reports/` as reusable artifacts
4. Avoid common plotting issues such as overlapping labels or stale figures
5. Explain why chart readability matters as much as the code that generated it

---

## Section 1: Why Charts Need Intentional Design (5 minutes)

### Opening Script

**[Instructor speaks:]**

Charts are not just decoration. A chart is a compressed explanation. If the labels are missing, the axes are confusing, or the categories are unreadable, the chart stops helping.

Today we are making visuals that someone else could actually use in a report or demo.

---

## Section 2: Direct Instruction on Plot Basics (15 minutes)

### Start from Aggregated Data

**[Instructor speaks:]**

Most useful charts begin with a summary, not raw noisy rows. For example, counts by category or counts by status are excellent starting points.

### Minimum Readability Checklist

Teach this checklist:

- descriptive title
- labeled x-axis and y-axis
- rotated category labels if needed
- sensible figure size
- saved file path that others can find

### Example Pattern

```python
import matplotlib.pyplot as plt
import pandas as pd

summary = pd.read_csv("reports/summary.csv")

plt.figure(figsize=(8, 4))
plt.bar(summary["category"], summary["count"])
plt.title("Records by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("reports/category_counts.png")
plt.close()
```

Explain why `plt.close()` matters when generating multiple plots in one run.

---

## Section 3: Live Demo (10 minutes)

### Build a Bar Chart and a Trend Chart

Show a bar chart first, then if the dataset supports it, a line chart by date.

Narrate:

**[Instructor speaks:]**

I am choosing a bar chart because counts by category are categorical data. If I have a date field or a timestamp summary, a line chart may tell the story better. Chart choice is part of communication, not just code.

---

## Section 4: Guided Plotting Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Generate one or two plots from your capstone dataset and save them into `reports/`.

### Required Tasks

1. load or reuse a cleaned dataset or summary
2. create at least one chart
3. label the title and axes
4. save the output into `reports/`
5. confirm the image file opens and is readable

### Coaching Prompts

- What question does this chart answer?
- Is the chart type appropriate for the data?
- Can a reader understand it without you narrating over it?
- Did you save the file and close the figure?

### Common Mistakes

- unlabeled axes
- overlapping category names
- plotting raw data when a summary would be clearer
- forgetting `tight_layout()` or `close()`

### Recovery Script

**[Instructor speaks:]**

If you are not sure what to chart, start with counts by category or counts by status. Those are easy to explain and often the clearest first visuals.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Readable visualization is a communication skill. A chart only helps if the next person can interpret it quickly and accurately.

### Exit Ticket

1. Why should plots be saved to files in an automated workflow?
2. What chart did you create?
3. What readability change improved your chart the most?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour we do a limited regression demo or equivalent analysis so learners see one small modeling workflow without leaving the practical scope of the course.

---

## Shared Day 11 Instructor Reference

Reuse the shared day-level instructor support from `Day11_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 11 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
