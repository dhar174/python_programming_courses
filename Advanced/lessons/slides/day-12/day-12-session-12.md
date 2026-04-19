# Advanced Day 12 — Session 12 (Hours 45–48)
Python Programming (Advanced) • Testing, Packaging, and Final Delivery

---

# Session 12 Overview

## Topics Covered Today
- Hour 45: testing with pytest for the service layer
- Hour 46: coverage, edge cases, and a lightweight integration test
- Hour 47: packaging and delivery
- Hour 48: final capstone demo, certification-style review, and retrospective

## Day Goal
- Finish the capstone with quality, delivery confidence, and explanation clarity

---

# Alignment Sources

- Runbook: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → Session 12 overview; Hours 45–48
- Lecture: `Advanced/lessons/lecture/Day12_Hour1_Advanced.md` through `Day12_Hour4_Advanced.md`
- Homework: `Advanced/assignments/Advanced_Day12_homework.ipynb`
- Quiz: `Advanced/quizzes/Advanced_Day12_Quiz.html`

## Session Theme
- Quality supports confidence
- Packaging supports handoff
- The final demo should show a system, not random features

---

# Session Success Criteria

- Core service behavior is covered by pytest tests
- Coverage is used as a guide, not a vanity metric
- README + requirements support a fresh-run test
- Final demos show architecture, persistence, analytics, and growth

---

# Scope Guardrails for Today

- Prioritize service-layer and repository-confidence tests over UI testing
- Do not chase 100% coverage blindly
- Package the runnable source release before optional executables
- Final demos should be concise, stable, and explainable

---

# Hour 45: Testing with pytest

## Learning Outcomes
- Write focused service-layer unit tests
- Use fixtures and plain `assert`
- Cover success and failure paths
- Explain why UI testing is not the priority here

---

## Why Testing Fits Here

- The capstone now has enough structure to test meaningfully
- Service logic and exception patterns are stable enough to protect
- Testing now reinforces quality instead of chasing a moving target

## Framing
- Tests are fast feedback
- Tests are not punishment

---

## pytest Basics

- Plain test functions stay readable
- Arrange → Act → Assert is enough structure
- Fixtures reduce repeated setup
- Negative tests matter as much as happy paths

---

## Fixture + Test Pattern

```python
@pytest.fixture
def service():
    repo = InMemoryTrackerRepository()
    return TrackerService(repo=repo)

def test_add_and_get_record(service):
    created = service.add_record("Write report", "ops", "open")
    fetched = service.get_record(created.id)
    assert fetched.title == "Write report"
```

---

## Negative Test Pattern

```python
def test_add_record_rejects_empty_title(service):
    with pytest.raises(ValidationError):
        service.add_record("", "ops", "open")
```

## Teaching point
- Good tests protect behaviors learners actually care about

---

## Lab: Write the First Real Test Suite

**Time: 25–35 minutes**

### Tasks
- Create a test file such as `tests/test_service.py`
- Add at least five tests
- Include at least two negative tests
- Run pytest and confirm the suite passes

### Completion Criteria
- Test names communicate the behavior clearly
- The suite focuses on logic, not UI callbacks

---

## Common Pitfalls (Hour 45)

⚠️ Testing UI callbacks directly  
⚠️ One test checking too many behaviors  
⚠️ Shared mutable state without reset  
⚠️ Happy-path-only thinking

---

## Homework + Quiz Emphasis (Hour 45)

- Homework goal: a small pytest suite for core service-layer rules
- Best practice: focused unit tests around behavior and validation
- Pitfall to avoid: testing private implementation details
- Quiz-ready anchor: `Hour 45 | test runner: pytest`

---

## Quick Check

**Question**: What should a strong unit test avoid if you want refactors to stay safe?

---

# Hour 46: Coverage + Edge Cases + Integration

## Learning Outcomes
- Run a basic coverage report
- Find high-value gaps
- Add edge-case tests
- Prove one meaningful boundary with an integration-style test

---

## Coverage with Perspective

- Coverage shows which lines executed
- Coverage does **not** prove the tests are meaningful
- Use it as a flashlight, not a scorecard

## Smart question
- Which uncovered branch is most likely to matter in a real bug?

---

## Coverage Commands

```bash
coverage run -m pytest
coverage report -m
```

## Great edge-case candidates
- missing record
- invalid input
- empty search result
- auth helper failure
- duplicate ID assumptions

---

## Lightweight Integration Test

```python
def test_service_and_sqlite_repo_work_together(tmp_path):
    db_path = tmp_path / "tracker.db"
    repo = SQLiteTrackerRepository(str(db_path))
    repo.init_db()
    service = TrackerService(repo=repo)

    created = service.add_record("Ship deck", "training", "open")
    fetched = service.get_record(created.id)

    assert fetched.title == "Ship deck"
```

---

## Lab: Harden the Suite

**Time: 25–35 minutes**

### Tasks
- Run coverage
- Identify at least two valuable missing branches
- Add two tests for those branches
- Add one integration-style test

### Completion Criteria
- Coverage changes testing priorities intelligently
- Integration proves a real boundary, not a giant workflow

---

## Common Pitfalls (Hour 46)

⚠️ Chasing 100% blindly  
⚠️ Executing code without useful assertions  
⚠️ Turning one integration test into an end-to-end maze  
⚠️ Adding coverage numbers without discussing risk

---

## Homework + Quiz Emphasis (Hour 46)

- Homework goal: a tighter test suite with edge-case and integration confidence
- Best practice: add edge cases and one lightweight integration test after unit tests pass
- Pitfall to avoid: chasing a number instead of meaningful scenarios
- Quiz-ready anchor: `Hour 46 | coverage target: service layer`

---

## Quick Check

**Question**: How can high coverage still miss real bugs?

---

# Hour 47: Packaging and Delivery

## Learning Outcomes
- Explain the difference between “runs here” and “ships”
- Refine `README.md`, `requirements.txt`, and `requirements-dev.txt`
- Perform a fresh-run smoke test
- Identify hidden dependency or path assumptions

---

## What Shipping Really Means

- Repeatable install
- Repeatable run
- Honest documentation
- Clear entry point

## Course minimum
- A runnable source release
- Optional packaging extras only if time permits

---

## Deliverable Recipe

- `README.md` with exact setup + run steps
- `requirements.txt` for runtime dependencies
- `requirements-dev.txt` for dev tooling
- `.gitignore` for environment and build outputs
- one verified entry point

---

## Fresh-Run Sequence

**Windows (cmd / PowerShell)**
```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pytest
python api/app.py
```

**macOS / Linux (bash / zsh)**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
python api/app.py
```

## Teaching point
- If the steps are not written clearly, the deliverable is weaker than it looks

---

## Lab: Make the Project Shareable

**Time: 25–35 minutes**

### Tasks
- Update `README.md`
- Verify runtime and dev dependencies
- Check `.gitignore`
- Perform a fresh-run smoke test
- Fix one missing setup step if discovered

### Completion Criteria
- Another learner could follow the setup without guessing
- Entry points and environment variables are documented

---

## Common Pitfalls (Hour 47)

⚠️ Missing dependency in `requirements.txt`  
⚠️ Undocumented environment variables  
⚠️ Entry-point confusion between GUI, API, and scripts  
⚠️ Relative paths that only work from one folder

---

## Homework + Quiz Emphasis (Hour 47)

- Homework goal: a documented runnable delivery package for the capstone
- Best practice: package the runnable app before optional build tooling
- Pitfall to avoid: spending all packaging time on an executable
- Quiz-ready anchor: `Hour 47 | requirements file: ready`

---

## Quick Check

**Question**: What does a fresh-run test reveal that “it works on my machine” usually hides?

---

# Hour 48: Final Demo + Review + Retrospective

## Learning Outcomes
- Demonstrate the minimum capstone deliverables clearly
- Explain architecture choices and tradeoffs
- Practice certification-style code reading
- Name one next step for continued growth

---

## Capstone Minimum Deliverables

- model + service layer
- SQLite persistence
- one interface surface: GUI or API
- analytics/reporting
- tests
- packaging readiness

## Final-hour mindset
- coherence over perfection

---

## Strong Demo Flow

1. one-sentence problem statement
2. create or retrieve data
3. show persistence
4. show interface surface
5. show one analytics/report artifact
6. mention testing or packaging evidence

## Timebox
- aim for 3–5 minutes

---

## Questions Worth Answering During Demos

- Why did you choose this architecture?
- What part was hardest to stabilize?
- What tradeoff did you make intentionally?
- What would you improve next?

## Coaching note
- Bring the story back to user flow + architecture if details take over

---

## Certification-Style Review Prompt

```python
class Tracker:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

t = Tracker()
t.add("alpha")
print(len(t.items))
```

## Ask
- What prints?
- Why?

---

## Retrospective Prompts

- What can you do now that you could not do before?
- What still feels shaky but understandable?
- What will you practice next while the material is fresh?

## Ask learners to capture
1. one skill to apply immediately
2. one skill to keep practicing
3. one artifact they are proud of

---

## Homework + Quiz Emphasis (Hour 48)

- Homework goal: a final capstone walkthrough and certification-style review summary
- Best practice: connect the whole course back to one coherent architecture
- Pitfall to avoid: a demo without reflection
- Quiz-ready anchor: `Hour 48 | final demo domain: tracker`

---

## Quick Check

**Question**: What makes a final demo convincing even if the project is not perfect?

---

# Day 12 Wrap-Up

## End-of-Day Evidence
- Tests protect core behavior
- Coverage informs smarter improvements
- Packaging supports a clean handoff
- The final demo proves understanding, not just feature count

---

## Homework Focus

- Keep outputs deterministic in `Advanced_Day12_homework.ipynb`
- Rehearse the anchor lines:
  - `test runner: pytest`
  - `coverage target: service layer`
  - `requirements file: ready`
  - `final demo domain: tracker`

---

## Final Exit Ticket

1. Which test gives you the most confidence?
2. What did the fresh-run test teach you?
3. What part of your capstone best shows your growth?

---

# Course Close

## You Can Now
- design layered Python applications
- persist and query data
- expose and consume APIs
- build analytics/reporting paths
- test core logic
- package a runnable deliverable

## Next step
- keep the capstone alive through one deliberate improvement
