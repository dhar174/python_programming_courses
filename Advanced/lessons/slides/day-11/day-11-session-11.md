# Advanced Day 11 — Session 11 (Hours 41–44)
Python Programming (Advanced) • Analytics, Visualization, and Reporting

---

# Session 11 Overview

## Topics Covered Today
- Hour 41: pandas essentials — loading, cleaning, summarizing
- Hour 42: visualization with matplotlib
- Hour 43: regression demo or equivalent analysis
- Hour 44: integrate analytics into the capstone

## Day Goal
- Turn capstone data into a repeatable reporting pipeline

---

# Alignment Sources

- Runbook: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → Session 11 overview; Hours 41–44
- Lecture: `Advanced/lessons/lecture/Day11_Hour1_Advanced.md` through `Day11_Hour4_Advanced.md`
- Homework: `Advanced/assignments/Advanced_Day11_homework.ipynb`
- Quiz: `Advanced/quizzes/Advanced_Day11_Quiz.html`

## Session Theme
- Use the **same dataset** all day
- Clean before trusting
- Visualize with intention
- Package analytics as a feature, not a notebook fragment

---

# Session Success Criteria

- Exported data loads into pandas cleanly
- At least one summary artifact is saved
- At least one readable chart lands in `reports/`
- Analysis stays within course scope
- Report generation becomes repeatable

---

# Scope Guardrails for Today

- Start from the capstone dataset when possible
- Do not force machine learning if the data does not fit
- A clear summary + one strong chart beats a flashy but shallow notebook
- Repeatability matters more than manual heroics

---

# Hour 41: pandas Essentials

## Learning Outcomes
- Load capstone data into a DataFrame
- Inspect shape, columns, and types
- Clean common data issues
- Compute useful summaries and grouped counts

---

## The Analytics Mindset

- We are not leaving the capstone behind
- We are adding a reporting lens to the same project
- Strong analysis starts with:
  - inspection
  - cleaning
  - simple, honest summaries

## Day 11 reminder
- Use the same dataset from Hour 41 through Hour 44

---

## First Inspection Steps

```python
import pandas as pd

df = pd.read_csv("reports/records_export.csv")
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
```

## Habit
- Inspect before you interpret

---

## Common Cleaning Moves

```python
df["category"] = df["category"].str.strip().str.lower()
df["priority"] = pd.to_numeric(df["priority"], errors="coerce")
df["status"] = df["status"].fillna("unknown")
```

## Typical issues
- whitespace
- missing values
- numeric strings
- inconsistent casing

---

## Summary Patterns Worth Starting With

- total row count
- counts by category
- counts by status
- mean or sum of a numeric field

```python
summary = df.groupby("status").size().reset_index(name="count")
print(summary)
```

---

## Demo Flow: Load, Clean, Summarize

1. Load exported data
2. Inspect `head()`, `shape`, and `dtypes`
3. Make one explainable cleaning choice
4. Group and summarize
5. Save a reusable summary artifact

---

## Lab: Build the First Analytics Pass

**Time: 25–35 minutes**

### Tasks
- Locate or export one CSV
- Load it into pandas
- Inspect the structure
- Make at least one cleaning decision
- Compute at least three metrics
- Save a summary CSV into `reports/`

### Completion Criteria
- Learner can explain one cleaning choice
- Summary artifact is saved and reusable

---

## Common Pitfalls (Hour 41)

⚠️ Analyzing before inspecting  
⚠️ Cleaning data in ways you cannot explain  
⚠️ Ignoring missing values  
⚠️ Forgetting to save the summary artifact

---

## Homework + Quiz Emphasis (Hour 41)

- Homework goal: a small cleaned DataFrame with labeled summary outputs
- Best practice: normalize and clean before trusting counts
- Pitfall to avoid: summarizing dirty data hides real problems
- Quiz-ready anchor: `Hour 41 | dataframe rows: 5`

---

## Quick Check

**Question**: What can `df.dtypes` reveal before you compute a single summary?

---

# Hour 42: Visualization with Matplotlib

## Learning Outcomes
- Create at least one readable chart
- Label title and axes clearly
- Save plots into `reports/`
- Avoid common figure-management mistakes

---

## Why Chart Design Matters

- A chart is a compressed explanation
- If the labels are weak, the chart stops helping
- Good plots should stand on their own without narration

## Minimum readability checklist
- title
- x-axis label
- y-axis label
- readable categories
- saved artifact path

---

## Start from Aggregated Data

- Counts by category are often a strong first chart
- Counts by status are usually easy to explain
- Time-based summaries can support line charts later

## Practical rule
- Plot the **summary**, not the raw noise

---

## Bar Chart Pattern

```python
import matplotlib.pyplot as plt

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

---

## Chart Choice Is Communication

- Bar chart → category comparisons
- Line chart → trend over time
- Choose the chart that matches the question

## Teaching point
- Plotting is not just syntax; it is storytelling

---

## Lab: Save a Report-Ready Plot

**Time: 25–35 minutes**

### Tasks
- Reuse a cleaned dataset or summary
- Create at least one chart
- Label title + axes
- Save the artifact into `reports/`
- Open the file and confirm readability

### Completion Criteria
- Another learner can understand the plot quickly
- The saved file works as a reusable artifact

---

## Common Pitfalls (Hour 42)

⚠️ Unlabeled axes  
⚠️ Overlapping category labels  
⚠️ Plotting raw data when a summary would be clearer  
⚠️ Forgetting `tight_layout()` or `plt.close()`

---

## Homework + Quiz Emphasis (Hour 42)

- Homework goal: a saved matplotlib chart that supports the tracker report
- Best practice: clear labels, titles, and saved artifact path
- Pitfall to avoid: an unlabeled chart communicates very little
- Quiz-ready anchor: `Hour 42 | chart type: bar`

---

## Quick Check

**Question**: Why is saving the plot to `reports/` better than leaving it only inside a notebook session?

---

# Hour 43: Regression Demo or Equivalent Analysis

## Learning Outcomes
- Explain when regression makes sense
- Describe why train/test split matters
- Run one small predictive workflow if appropriate
- Use a fallback analysis if the data does not support regression

---

## Scope Guardrail

- We are **not** becoming ML engineers in one hour
- This is a limited workflow demo
- The runbook explicitly allows a fallback analysis

## Smart decision
- If the dataset does not fit, do more honest analysis instead

---

## When Regression Makes Sense

- Target must be numeric
- Features should be numeric and clean enough
- The question should genuinely involve prediction

## Keep evaluation simple
- One metric is enough for today
- Explain the result in plain language

---

## Tiny Workflow Example

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

X = df[["priority"]]
y = df["hours_to_complete"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
```

---

## What This Demo Is Really Teaching

- Prepare features + target
- Hold back test data
- Fit a model
- Predict on unseen data
- Report one metric honestly

## If regression is a bad fit
- Add another summary
- Add another chart
- Explain why the fallback is better

---

## Lab: Predictive Slice or Honest Fallback

**Time: 25–35 minutes**

### Tasks
- Decide whether the data supports regression
- Run the workflow or choose fallback analysis
- Report one metric or observation
- Write one sentence explaining the result

### Completion Criteria
- Learner can justify the method choice
- The outcome is explained in plain language

---

## Common Pitfalls (Hour 43)

⚠️ Forcing regression onto non-numeric data  
⚠️ Treating the demo as production-ready analytics  
⚠️ Skipping cleaning and blaming the tool  
⚠️ Reporting a metric without explaining it

---

## Homework + Quiz Emphasis (Hour 43)

- Homework goal: a simple regression example with one labeled prediction
- Best practice: keep the forecast practical and limited
- Pitfall to avoid: overstating a quick demo as production-ready analytics
- Quiz-ready anchor: `Hour 43 | model: linear regression`

---

## Quick Check

**Question**: Why is “regression is not the right fit here” sometimes the most advanced answer?

---

# Hour 44: Integrate Analytics into the Capstone

## Learning Outcomes
- Add a report-generation path to the capstone
- Produce export, summary, and chart artifacts repeatably
- Document how the report runs
- Treat analytics as part of the product

---

## Analytics as a Feature

- The capstone should not only store data
- It should also summarize and communicate data intentionally
- A report feature turns analysis into something reusable

## Product mindset
- one command
- or one button
- same cleaned pipeline every time

---

## Repeatable Report Pipeline

1. export data
2. load + clean data
3. compute summaries
4. generate charts
5. save artifacts to `reports/`

## Anti-pattern
- hidden manual steps between those stages

---

## Example Entry Point

```python
from reports.export_data import export_records_csv
from reports.analyze import build_summary
from reports.plotting import create_plots

def main():
    csv_path = export_records_csv()
    summary_path = build_summary(csv_path)
    create_plots(summary_path)
    print("Report artifacts generated in reports/")
```

---

## Lab: Add the Report Feature

**Time: 25–35 minutes**

### Tasks
- Create or refine an export step
- Generate a summary table
- Save at least one chart
- Put outputs in `reports/`
- Document how to run the feature

### Completion Criteria
- Another learner could trigger the report tomorrow
- Artifacts appear in predictable places

---

## Common Pitfalls (Hour 44)

⚠️ Hard-coded paths that work on only one machine  
⚠️ Report logic scattered across scripts and notebooks  
⚠️ Missing README guidance  
⚠️ Hand-edited intermediate files

---

## Homework + Quiz Emphasis (Hour 44)

- Homework goal: a report feature that connects data outputs to the tracker project
- Best practice: combine summaries, charts, and predictions into one readable feature
- Pitfall to avoid: disconnected notebook snippets weaken the capstone
- Quiz-ready anchor: `Hour 44 | report file: reports/weekly_summary.txt`

---

## Quick Check

**Question**: What makes a report feature repeatable instead of “works when I remember the steps”?

---

# Day 11 Wrap-Up

## End-of-Day Evidence
- Data is loaded and cleaned intentionally
- Summaries answer real questions
- Charts are readable and saved
- The capstone now has a report-generation path

---

## Homework Focus

- Keep outputs deterministic in `Advanced_Day11_homework.ipynb`
- Rehearse the anchor lines:
  - `dataframe rows: 5`
  - `chart type: bar`
  - `model: linear regression`
  - `report file: reports/weekly_summary.txt`

---

## Exit Ticket

1. Which cleaning decision changed your analysis most?
2. What question does your chart answer?
3. Is regression the right fit for your data — why or why not?

---

# Looking Ahead

## Next Session
- Lock in quality with pytest
- Use coverage strategically
- Package the project for handoff
- Finish with a final capstone demo and reflection
