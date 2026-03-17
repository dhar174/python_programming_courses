# Day 11, Hour 3: Regression Demo or Equivalent Analysis
**Python Programming Advanced - Session 11**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame regression as optional and limited: 5 minutes  
- Direct instruction on train/test thinking and one metric: 15 minutes  
- Live demo with a tiny dataset: 10 minutes  
- Guided regression mini-lab or fallback analysis: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain at a high level when regression is appropriate
2. Describe why training and testing data should be separated
3. Run a small regression workflow if the environment and data support it
4. Report one simple evaluation metric or, if regression is not appropriate, complete an equivalent additional analysis
5. Keep the machine-learning portion inside the runbook's deliberately limited scope

---

## Section 1: Scope Guardrail (5 minutes)

### Opening Script

**[Instructor speaks:]**

This hour is intentionally narrow. We are not becoming machine-learning engineers in sixty minutes. We are doing one small modeling demo so learners see the shape of a predictive workflow and understand the words around it.

If the dataset or environment does not fit regression well, that is not failure. The runbook explicitly allows an equivalent extra analysis instead.

---

## Section 2: Direct Instruction on the Workflow (15 minutes)

### When Regression Makes Sense

**[Instructor speaks:]**

Regression is useful when you are trying to predict a numeric value from one or more numeric features. If your data is mostly free text or categories without proper encoding, forcing regression into the lesson can create more confusion than insight.

### Train/Test Split

**[Instructor speaks:]**

The core idea of train/test split is simple: do not evaluate a model only on the same data it learned from. Hold some data back so you get a more honest signal.

### One Metric Is Enough

Use one metric such as mean absolute error or `R^2`. Then explain what it means in ordinary language instead of disappearing into formulas.

---

## Section 3: Live Demo (10 minutes)

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("reports/model_data.csv")

X = df[["priority"]]
y = df["hours_to_complete"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"MAE: {mae:.2f}")
```

Narrate:

**[Instructor speaks:]**

This is not a production model. It is a tiny demonstration of the workflow: prepare features and target, split data, train, predict, and evaluate.

If the environment does not support `scikit-learn`, replace the live demo with an additional analysis and a second chart.

---

## Section 4: Guided Mini-Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Run one small regression workflow if your data supports it. If not, complete one additional analysis that still deepens your report pipeline.

### Required Tasks

Learners should:

1. decide whether their data supports a simple regression
2. run the workflow or choose the fallback path
3. report one metric or observation
4. write one sentence explaining what the result means

### Coaching Prompts

- Is your target numeric?
- Are your features numeric and clean enough for this demo?
- What does the metric tell you in plain language?
- If regression is not appropriate, what extra summary or chart would still add value?

### Common Mistakes

- mixing string categories into the model without encoding
- interpreting the demo as a production-ready model
- skipping cleaning and then blaming the tool
- focusing on code instead of explaining the result

### Recovery Script

**[Instructor speaks:]**

If regression is turning into a fight, stop. The fallback path is valid. Build another analysis and chart from the same dataset. The learning objective is thoughtful analysis, not forcing the wrong technique.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

This hour is valuable even when the answer is, \"regression is not the right fit for this dataset.\" Good analysis includes knowing when not to force a method.

### Exit Ticket

1. Why do we separate training data from testing data?
2. What metric or observation did you report?
3. Was regression appropriate for your data, and why or why not?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour we connect analytics back into the capstone with a repeatable report feature.

---

## Shared Day 11 Instructor Reference

Reuse the shared day-level instructor support from `Day11_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 11 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
