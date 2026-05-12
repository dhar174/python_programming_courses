# Day 11, Hour 3: Regression demo: practical, limited scope

**Python Programming Advanced - Session 11**
**Runbook alignment:** Session 11, Hour 43
**Capstone theme:** Full-stack Tracker with models, services, repositories, SQLite, Flask API, optional GUI/API integration, reports, pytest, and packaging.

## 60-minute Timing Overview

| Minutes | Activity | Instructor intent |
| --- | --- | --- |
| 0-5 | Welcome, recap, and outcome framing | Connect this hour to the previous capstone layer and name the deliverable. |
| 5-17 | Concept briefing and vocabulary | Teach the ideas learners need before touching code. |
| 17-35 | Live demo with happy and sad paths | Model careful implementation, prediction, and debugging. |
| 35-50 | Guided lab / build time | Learners implement the hour milestone in their own capstone. |
| 50-56 | Debrief and troubleshooting clinic | Surface common mistakes and reinforce contracts. |
| 56-60 | Quick check / exit ticket | Verify readiness for the next hour. |

## Learning Outcomes

By the end of this hour, learners will be able to:

- Run a simple regression workflow when the dataset supports it.
- Explain train/test split and one evaluation metric at a high level.
- Recognize when regression is not appropriate and choose a better analysis.

## Instructor Prep Notes

- Confirm learners are in the correct project folder and virtual environment.
- Keep the authoritative runbook open to Session 11, Hour 43; this script expands that hour into a near-verbatim delivery guide.
- Use Python 3.11+ conventions: clear type hints, f-strings, `pathlib` for paths, context managers for resources, and small functions with one responsibility.
- Use the tracker capstone vocabulary consistently: model objects express domain data, services enforce workflow rules, repositories handle SQLite persistence, Flask routes expose JSON contracts, and reports/tests/packaging prove the app can be delivered.
- Keep a regression suitability checklist visible: numeric input, numeric target, enough rows, no hidden categorical strings, and a plain-language explanation of what the model can and cannot claim.

## Opening Script (0-5 minutes)

**[Instructor speaks:]**
"Welcome back. In the previous parts of the advanced course, we built a layered tracker: domain model, service layer, repository, and persistence. Today we keep turning that code into a deliverable system. This hour is not about memorizing syntax. It is about making a design choice, proving it with code, and leaving the project easier to test and maintain."

*(Action: Ask learners to open the project and run the last known-good command. For API hours, that may be `flask run` or `python -m api.app`; for analytics it may be a report script; for testing it may be `pytest -q`.)*

**[Instructor speaks:]**
"Before we add anything, we want a baseline. If your project does not run at the start of the hour, adding a feature will make debugging harder. Run the smallest command that proves your project is alive. If it fails, write down the first error line and do not start editing yet."

### Bridge from prior work

- The tracker already has a model/service/repository shape from earlier sessions.
- SQLite remains the source of truth for persisted records.
- This hour adds or strengthens the outer layer: API behavior, client integration, analytics, tests, packaging, or final delivery.
- The class norm is still: make one small change, run it, observe the result, then continue.

## Concept Briefing (5-17 minutes)

**[Instructor speaks:]**
"Here are the ideas I want you to listen for during the demo. First, where does this responsibility belong? Second, what is the happy path? Third, what is the sad path? Fourth, how will another person know how to use or verify it? Advanced Python is less about clever lines of code and more about reliable boundaries."

### Talk points

- Regression is for predicting a numeric value from numeric features.
- This hour is about workflow literacy, not becoming a data scientist in 60 minutes.
- Train/test split checks whether the model generalizes beyond examples it saw.
- If the capstone data is not suitable, do an additional analysis and chart instead of forcing a bad model.

### Why this matters in real projects

**[Instructor speaks:]**
"Real teams spend a surprising amount of time at boundaries: the boundary between a GUI and a service, an API and a client, a CSV and a DataFrame, or a test and the system under test. Bugs often appear where assumptions cross those boundaries. If we make contracts explicit, the next developer can reason about the program without reading every line."

Use these prompts to keep the class active:

- "What do you expect this function to return on success?"
- "What should happen if the input is missing, malformed, or points to a record that does not exist?"
- "Which layer should know about this detail?"
- "How could we test this without clicking through the whole application?"

## Live Demo (17-35 minutes)

**[Instructor speaks:]**
"I am going to demo this in small slices. Please do not copy yet. First, predict what should happen. Then I will run it. Then we will decide whether the result matches the contract. After that, I will pause so you can implement the same pattern in your project."

### Demo steps

1. Use a tiny synthetic dataset or cleaned numeric tracker data.
2. Split train/test, fit LinearRegression if scikit-learn is available.
3. Compute MAE or R^2 and explain it in plain language.
4. Show a sad path: categorical strings cannot be fed directly without encoding.

### Demo code or command sketch

```python
from pathlib import Path
import pandas as pd

data_path = Path("data/records.csv")
required_columns = {"amount"}

if data_path.exists():
    df = pd.read_csv(data_path)
else:
    print(f"Using synthetic demo data because {data_path} was not found.")
    df = pd.DataFrame({"amount": [20, 35, 40, 55, 70, 80, 95, 110]})

missing_columns = required_columns - set(df.columns)
if missing_columns:
    raise ValueError(f"Regression demo needs columns: {sorted(missing_columns)}")

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
model_data = df.dropna(subset=["amount"]).reset_index(drop=True)
if len(model_data) < 4:
    raise ValueError("Regression demo needs at least four numeric rows.")
model_data["record_number"] = model_data.index + 1

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error
    from sklearn.model_selection import train_test_split
except ImportError:
    correlation = model_data["record_number"].corr(model_data["amount"])
    print(f"scikit-learn unavailable; correlation fallback: {correlation:.2f}")
else:
    X = model_data[["record_number"]]
    y = model_data["amount"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")

```

### Demo narration guide

**[Instructor speaks:]**
"Notice that I am not starting with the biggest possible version. I am building a thin vertical slice. A thin slice is one small feature that crosses the layers we need: input, service behavior, persistence or data handling if relevant, and a visible result. Once that slice is correct, the next route, chart, test, or packaging step is easier."

*(Action: Run the code or command once for a happy path. Ask: "What proves this worked?")*

**[Instructor speaks:]**
"Now we need a sad path. A feature is not done just because the perfect input worked. I am going to send bad input, omit a required value, use a missing id, stop the server, or run from a clean environment depending on the hour. The goal is not to embarrass the code; the goal is to define how the program behaves when reality is messy."

*(Action: Trigger the sad path deliberately. For API work, show JSON errors. For pandas and reports, show a missing file or bad column and discuss the message. For tests, show a failing assertion and read it carefully.)*

### Instructor checkpoints during the demo

- Ask learners to identify the layer being edited.
- Ask whether the code is using project-safe paths rather than machine-specific paths.
- Ask what a reviewer would need in order to reproduce the result.
- Ask what test or manual check would catch a regression later.

## Guided Practice (35-40 minutes)

**[Instructor speaks:]**
"Now you will implement the same idea, but keep the scope narrow. Do not redesign your whole capstone. Pick the smallest slice that satisfies the hour outcome. If you finish early, use the optional extensions; do not start an unrelated rewrite."

Suggested instructor circulation questions:

1. "Show me the file you are editing and tell me why this responsibility belongs there."
2. "What is your first happy-path command?"
3. "What is your first sad-path command?"
4. "If I review this tomorrow, where is the contract documented?"
5. "What would you test automatically if you had ten more minutes?"

## Hands-on Lab (40-50 minutes)

### Lab prompt

Regression mini-lab: if supported, run a simple numeric regression and report one metric plus one observation. If not appropriate, produce an equivalent extra analysis and chart using the same cleaned dataset.

### Required learner workflow

1. Start from a known-good run.
2. Make one small implementation change.
3. Run the narrowest check possible.
4. Add the happy-path proof.
5. Add one sad-path proof.
6. Commit or save the working state before attempting an extension.

### Completion criteria

- Regression run or equivalent analysis is completed.
- Learner can explain the metric in plain language.
- Data cleaning steps are documented.
- No one claims a model is useful solely because code ran.

## Debrief and Troubleshooting (50-56 minutes)

**[Instructor speaks:]**
"Let us collect what we learned. I want one example of a happy path, one example of a sad path, and one example of a design boundary that became clearer. If your code is not fully working yet, you can still contribute by naming the exact symptom and the next diagnostic step."

### Common pitfalls to watch for

- Garbage in, garbage out from uncleaned data.
- Feeding categorical strings into a numeric model without encoding.
- Training and evaluating on the same rows.
- Overstating conclusions from tiny sample data.

### Debugging script for stuck learners

Use this sequence aloud when helping a learner:

1. "Read the first meaningful error message, not the last line only."
2. "What command produced it? Can we reproduce it?"
3. "What changed since the last working run?"
4. "Can we test the service or helper function without the outer UI/API/report layer?"
5. "What is the smallest rollback or fix that restores a working state?"

## Optional Extensions

If learners meet the completion criteria early, offer one of these stretch goals:

- Try a second numeric feature and compare MAE.
- Plot predicted vs actual values.
- Write a short limitations paragraph for the report.

Remind learners that optional work must not break the required slice. A polished required feature is better than three unfinished experiments.

## Quick Checks and Exit Ticket (56-60 minutes)

Ask learners to answer individually, then discuss two or three responses:

- Why do we separate training data from testing data?
- What is the happy path you proved this hour?
- What sad path did you test or plan to test next?
- Which file or module is now most important for the next hour?

**[Instructor speaks:]**
"Your exit ticket is a sentence, not an essay: name what works, name what still needs attention, and name your next command. That habit will keep your capstone moving as the system gets larger."

## Instructor Wrap-up Notes

- Reinforce the capstone through-line: each hour should leave behind a runnable artifact, not just notes.
- Encourage frequent commits with messages such as `feat: add records endpoint`, `test: cover validation errors`, or `docs: add report quickstart`.
- If multiple learners are blocked by the same issue, pause the room and debug one shared example rather than repeating the same fix individually.
- Keep advanced scope boundaries: do not detour into production OAuth, complex ORMs, elaborate front-end frameworks, or advanced machine learning unless the runbook marks the topic as optional.


## Expanded Facilitation Notes for a Full 60-Minute Delivery

Use this section when the class needs more structure, when learners are unevenly paced, or when you want a more detailed speaking guide than the core hour script above. It is intentionally written as an instructor companion rather than a student handout.

### Board plan and vocabulary anchor

At the start of the hour, reserve one side of the board for the capstone architecture and leave it visible. Draw the same four boxes every time: interface, service, repository, and data or artifact. For API hours, the interface is Flask routes and JSON. For client or GUI integration hours, the interface may be a Tkinter callback or a Python client object. For analytics hours, the artifact is a CSV, summary file, chart, or report. For testing and packaging hours, the artifact is evidence that the project can be verified and run by another person.

**[Instructor speaks:]**
"The box we edit today is important, but the boundaries between boxes are even more important. If we keep the boundary clean, we can swap a GUI for an API, replace manual checks with pytest, or generate a report without rewriting the domain model."

Use these vocabulary checks during the first ten minutes:

- A model represents the domain data and rules that belong with the data.
- A service coordinates use cases and raises meaningful domain exceptions.
- A repository hides SQLite details and returns domain objects or simple records.
- An API route translates HTTP into service calls and translates results back to JSON.
- A client translates Python function calls into HTTP requests and translates responses into useful Python values.
- A report pipeline turns persisted data into repeatable artifacts that can be reviewed.
- A test is executable evidence about expected behavior.
- A package or deliverable is successful only when another person can install and run it from instructions.

### Instructor pacing detail

If learners are new to this topic, spend extra time on prediction before execution. Before every run, ask, "What status code, file, chart, exception, or test result do we expect?" Prediction forces learners to state the contract. If the result differs, the class has a concrete debugging target.

If learners are moving quickly, shorten the lecture and lengthen the lab, but keep the same quality gates: happy path, sad path, readable code, and a repeatable command. Do not let the hour become a feature race. A learner who can explain one clean vertical slice is better prepared than a learner with five partial features.

Suggested minute-by-minute adjustment:

- If setup consumes more than 8 minutes, skip optional styling and focus on one minimal deliverable.
- If the demo fails, narrate the recovery process. This is valuable modeling, not a failure of instruction.
- If half the room is blocked by the same problem, pause the room and solve one shared example.
- If only one or two learners are blocked, keep the rest moving with the lab checklist while you circulate.

### Deeper demo prompts

Use this prompt cycle while live coding:

1. "What input enters this layer?"
2. "What output leaves this layer on success?"
3. "What named error or status represents failure?"
4. "Where is the rule written exactly once?"
5. "How will we prove this behavior after class?"

For API work, insist that learners show at least one JSON error body. A route that works for perfect input but returns an HTML traceback for predictable bad input is not yet a reliable API. For analytics work, insist that learners show the generated file path and explain whether it can be regenerated. For tests, insist that learners read the failing assertion aloud before editing. For packaging, insist that learners follow their own README rather than relying on memory.

### Capstone quality gate

Before the exit ticket, have learners mark their hour result against this quick rubric:

| Category | Ready evidence | Needs attention |
| --- | --- | --- |
| Correctness | The feature works with a realistic happy path. | It only works with hard-coded or instructor-only data. |
| Error handling | A sad path produces a clear exception, JSON error, message, or test failure. | The app crashes or hides the cause. |
| Structure | The responsibility is in the correct layer. | Route, GUI, service, SQL, and reporting logic are tangled together. |
| Repeatability | There is a command, test, or documented step to reproduce the result. | The result depends on manual memory or IDE state. |
| Maintainability | Names are clear and the next feature has an obvious place to go. | The code works once but will be hard to extend. |

**[Instructor speaks:]**
"This rubric is not only for grading. It is a professional checklist. When you leave a feature behind, the next developer should be able to run it, understand it, and change it without fear."

### Common instructor interventions

When a learner puts too much logic in a Flask route or GUI callback, say: "Let us underline the business rule. Now move that sentence into the service or validation helper. The route or callback should coordinate, not own the rule."

When a learner hard-codes paths, say: "This path works on your machine because your machine is currently the hidden dependency. Replace it with a project-relative pathlib Path and create the directory in code."

When a learner catches Exception broadly, say: "Catching everything is like turning off the smoke alarm. Catch the error you expect, convert it into a helpful message, and let surprising errors remain visible during development."

When a learner wants to add a large optional feature before the required slice works, say: "Park that idea in a comment or issue. First make the required slice boring and reliable. Advanced projects succeed through boring reliability."

### Exit-ticket collection options

Choose one depending on time:

- Verbal round-robin: each learner states the working command and the next command.
- Written note: learners submit three bullets: works, broken, next.
- Pair check: partners run each other’s command from the README or lab note.
- Demo lottery: randomly choose two learners to show one happy path and one sad path.

Close the hour by connecting forward: the next hour assumes today has a runnable artifact. If a learner is behind, help them identify the smallest safe stopping point rather than encouraging a risky last-minute rewrite.

## Instructor Cross-Check Concepts

If regression is not appropriate for a learner dataset, keep the analytics path valuable by producing an additional matplotlib chart and a written observation. The goal is evidence-based reporting, not forcing every tracker dataset into a model.

## Additional Instructor-Ready Expansion

Use this expansion to deepen the hour without changing the runbook mapping. The focus remains **Regression or equivalent analysis**. The concrete artifact for this hour is a limited-scope numeric relationship analysis with caveats and plain-language interpretation. Keep returning to that artifact whenever discussion becomes abstract: learners should be able to point at a command, a file, a response, a chart, a test, or a README step and say, "This is the evidence that the hour worked."

### Deeper instructor narration

**[Instructor speaks:]**
"The most important habit in this hour is separating the visible surface from the rule underneath it. Today we are working at the analytical reasoning layer that complements summaries and charts without overclaiming. That layer matters because it is where another human or another part of the system forms expectations. If we leave the expectation implicit, the next person has to guess. If we make it explicit, the project becomes easier to test, easier to debug, and easier to explain during the final capstone review."

**[Instructor speaks:]**
"Before I run anything, I want us to predict the evidence. Our baseline is to execute a script that computes a slope/correlation or equivalent comparison and prints an interpretation paragraph. A successful run should prove this happy path: the analysis uses numeric, cleaned data and explains what the result suggests in the capstone context. A responsible implementation should also prove this sad path: too few rows, constant values, missing columns, or nonnumeric input produce a graceful skip with explanation. Notice that we are not adding sad paths to be negative. We are adding them because production code spends much of its life receiving imperfect input, missing configuration, stale data, or unexpected user behavior."

Pause after that statement and ask learners to write a one-sentence contract in their own words. For example: "When this input arrives, this layer returns this result or this named error." Circulate quickly and listen for vague language such as "it works" or "it fails." Coach those learners to replace vague language with observable evidence: a status code, exception type, saved filename, printed message, chart title, pytest result, or README command.

### Detailed demo walkthrough

Run the demo as a sequence of small predictions rather than one long typing performance. The suggested demo arc is to plot x/y values, compute a simple fit or comparison, read coefficients cautiously, and state limitations aloud. At each pause, ask the room to identify three things: the input entering this layer, the output leaving this layer, and the single responsibility that should not leak into neighboring layers. If learners cannot name those three things, slow down and draw the boundary again.

Use this checkpoint rhythm:

1. **Baseline:** Execute a script that computes a slope/correlation or equivalent comparison and prints an interpretation paragraph before editing. If it fails, narrate the failure honestly and recover before adding new code.
2. **First slice:** Implement only enough to prove the analysis uses numeric, cleaned data and explains what the result suggests in the capstone context. Do not add optional polish yet.
3. **Read the code aloud:** Point to the function or method boundary and say what it accepts and returns.
4. **Sad path:** Trigger too few rows, constant values, missing columns, or nonnumeric input produce a graceful skip with explanation deliberately. Ask, "Is this failure understandable to the person who receives it?"
5. **Architecture check:** Ask whether the code belongs in the route, client, service, repository, analytics helper, test fixture, or delivery documentation.
6. **Repeatability check:** Identify the exact command or manual step that proves the result again later.
7. **Commit-quality check:** Ask whether the current state could be saved with a clear commit message.

A useful live-coding move is to introduce one small defect on purpose, such as a wrong field name, missing header, missing timeout, incorrect path, or overly broad exception handler. Then read the observed behavior with the class. This models a mature debugging posture: we do not panic; we compare expected behavior with observed behavior, isolate the layer, and make the smallest correction that restores the contract.

### Guided lab checkpoints

During the lab, avoid answering first with a complete solution. Ask learners to show evidence in this order:

- "Show me the command you ran before editing."
- "Show me the smallest code change that targets this hour's artifact."
- "Show me the happy-path evidence: the analysis uses numeric, cleaned data and explains what the result suggests in the capstone context."
- "Show me the sad-path evidence: too few rows, constant values, missing columns, or nonnumeric input produce a graceful skip with explanation."
- "Show me where this behavior would be changed if the requirement changed next week."

If a learner is ahead, direct them to this extension only after the required artifact is stable: add residual plot or simple before/after comparison when regression is not appropriate for the dataset. Make it clear that extension work must be reversible. A good extension leaves the required path cleaner or better documented. A risky extension creates a second debugging problem right before the hour closes.

For pairs, assign roles for five-minute intervals. The driver types and runs commands. The navigator reads the contract and watches for boundary violations. Halfway through, switch roles. This keeps faster learners from taking over and gives quieter learners a defined speaking responsibility. Ask the navigator to use the review question: What can this result support, and what would be irresponsible to claim?

### Troubleshooting decision tree

Use this decision tree when the room gets stuck:

- If the first command cannot start, stop feature work and fix environment, import, or configuration issues first.
- If the happy path fails, inspect the boundary closest to the symptom. For API work, inspect request body, headers, route pattern, and service call. For analytics work, inspect path, columns, dtypes, and row counts. For testing work, inspect fixture setup and the exact assertion. For packaging work, inspect README steps and dependency installation.
- If the sad path returns a confusing result, improve the translation layer. Convert expected domain errors into the agreed JSON response, user message, report warning, or pytest assertion. Do not hide unexpected errors while still developing.
- If two layers disagree, choose the service or documented contract as the source of truth and update the outer layer to match it.
- If a learner proposes a rewrite, ask for the smallest reversible change that proves the next fact. Rewrites are sometimes necessary, but they should be chosen deliberately, not as an emotional response to a messy error.

Name the common risk explicitly: teaching learners to treat a regression line as proof of causation or as a production ML model. Write it on the board as an anti-pattern, then ask learners to point to the line or step in their project that prevents it.

### Formative questions and differentiation notes

Use these questions for quick checks throughout the hour:

- What is the contract this layer promises?
- Which command proves the contract without relying on your memory?
- What invalid input or missing dependency did you test?
- Which part of the code should not know about this detail?
- What would a teammate need in order to reproduce your result tomorrow?
- If this breaks during the final demo, what is the first diagnostic step?

For learners who need more support, narrow the task to one happy path and one sad path. Provide a partially completed function signature or checklist, but still require them to run the command and explain the result. For learners who are ready for more challenge, ask them to document the contract in README language, add a focused test, or compare two design options and justify the simpler one. Keep both groups anchored to the same hour outcome so the class does not split into unrelated projects.

Close by saying: "The goal is not to make this layer impressive. The goal is to make it dependable. Dependable code has a clear contract, a repeatable proof, a known failure behavior, and an obvious next place to change it."
