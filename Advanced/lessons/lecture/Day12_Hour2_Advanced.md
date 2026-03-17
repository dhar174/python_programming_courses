# Day 12, Hour 2: Coverage, Edge Cases, and a Lightweight Integration Test
**Python Programming Advanced - Session 12**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe coverage as a signal, not a game: 5 minutes  
- Direct instruction on meaningful coverage and integration tests: 15 minutes  
- Live demo of coverage and one repo-plus-service test: 10 minutes  
- Guided hardening lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Run a basic coverage report for the test suite
2. Identify important gaps without obsessing over 100 percent
3. Add tests for high-value edge cases
4. Write one lightweight integration-style test involving more than one layer
5. Explain why high coverage can still miss bugs

---

## Section 1: Coverage with Perspective (5 minutes)

### Opening Script

**[Instructor speaks:]**

Coverage is useful, but it is not a trophy. It tells us which lines executed during tests. It does not guarantee those tests were meaningful. Today we use coverage as a guide, not as a vanity metric.

---

## Section 2: Direct Instruction on Coverage and Integration (15 minutes)

### Coverage Basics

Show a typical command:

```bash
coverage run -m pytest
coverage report -m
```

Explain that uncovered lines can help us spot neglected branches.

### Edge Cases

**[Instructor speaks:]**

The best edge cases are usually the ones your project has already hinted at:

- missing record
- invalid input
- empty search result
- duplicate ID assumptions
- auth helper failures if separated cleanly

### One Lightweight Integration Test

**[Instructor speaks:]**

An integration-style test means more than one layer works together. In this course, a great example is service plus SQLite repository using a temporary database. That is enough to test wiring without turning the suite into a full end-to-end system.

---

## Section 3: Live Demo (10 minutes)

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

Then run coverage and explain what changed.

---

## Section 4: Guided Hardening Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Use coverage to choose smarter tests, then add one integration-style test that proves a real layer boundary works.

### Required Tasks

1. run coverage or an equivalent report
2. identify at least two valuable missing branches
3. add two tests for those branches
4. add one integration-style test

### Coaching Prompts

- Which uncovered line matters most to a real bug?
- Are you testing meaningful behavior or just inflating the number?
- What boundary does your integration test prove?
- Did a past bug suggest a test you still have not written?

### Common Mistakes

- chasing 100 percent coverage blindly
- writing shallow tests that only execute code without asserting useful behavior
- turning an integration test into a giant end-to-end test with too many moving parts

### Recovery Script

**[Instructor speaks:]**

If coverage feels abstract, pick one real branch you care about and test it. Then add one honest integration test. That is already valuable progress.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Coverage is best used as a flashlight, not a scorecard. Shine it on the parts of the project most likely to break or most expensive to debug.

### Exit Ticket

1. Why can high coverage still miss bugs?
2. Which edge case did you add a test for?
3. What boundary did your integration test prove?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour we package the project so someone else can install and run it without guessing.

---

## Shared Day 12 Instructor Reference

Reuse the shared day-level instructor support from `Day12_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`
- `## Final Delivery Appendix`
- `## Certification Review Appendix`

This keeps the Day 12 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
