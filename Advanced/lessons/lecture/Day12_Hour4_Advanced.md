# Day 12, Hour 4: Final Capstone Demo, Certification-Style Review, and Retrospective
**Python Programming Advanced - Session 12**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame the final session and demo expectations: 10 minutes  
- Facilitate demos and review prompts: 30 minutes  
- Certification-style code-reading review: 10 minutes  
- Retrospective and next-step planning: 10 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Demonstrate the minimum capstone deliverables clearly and concisely
2. Explain architecture choices and tradeoffs
3. Practice code-reading and certification-style reasoning
4. Reflect on the strongest skill gained during the course
5. Identify one concrete next step for continued practice

---

## Instructor Prep Notes

- Keep demos timeboxed and supportive
- Use the capstone rubric language from the runbook
- Have a few short code-reading prompts ready in case demo timing finishes early
- Encourage learners to run from a clean environment or at least show that their project is packaged thoughtfully

---

## Section 1: Final Framing (10 minutes)

### Opening Script

**[Instructor speaks:]**

This final hour is about demonstration, explanation, and reflection. The point is not perfection. The point is to show a coherent system, explain the design choices behind it, and leave with a clear picture of what you can already do and what you want to practice next.

Remind learners that the capstone minimum includes:

- model and service layer
- SQLite persistence
- one interface surface, GUI or API
- analytics or reporting
- tests
- packaging readiness

---

## Section 2: Capstone Demos (30 minutes)

### Demo Expectations

**[Instructor speaks:]**

Aim for a three-to-five-minute demo. Show the system, not every line of code. Good demo flow:

1. one-sentence problem statement
2. create or retrieve data
3. show persistence
4. show interface surface
5. show one analytics or report artifact
6. mention testing or packaging evidence

### Questions to Ask During Demos

- Why did you choose this architecture?
- What part was hardest to stabilize?
- What is one tradeoff you made intentionally?
- Where would you improve the project next?

### Coaching Note

If a learner gets lost in code details, gently bring them back to the user journey and architecture story.

---

## Section 3: Certification-Style Review (10 minutes)

### Framing

**[Instructor speaks:]**

The course outcomes also include preparation for certification-style thinking. That means reading code, predicting behavior, and explaining why something happens.

### Example Review Prompt

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

Ask learners what prints and why. Then expand with one exception or import question if time allows.

---

## Section 4: Retrospective and Next Steps (10 minutes)

### Reflection Script

**[Instructor speaks:]**

Think about the course in three layers:

- what you can do now that you could not do before
- what still feels shaky but understandable
- what you want to practice next while the material is still fresh

Ask learners to write down:

1. one skill they will apply immediately
2. one skill they will keep practicing
3. one artifact from the capstone they are proud of

### Closing Message

**[Instructor speaks:]**

A strong final project is not only one that works. It is one you can explain. Explanation is evidence of understanding. You should leave this course knowing that you can design a layered Python application, persist data, expose or consume an API, analyze results, test core logic, and package a runnable deliverable.

### Final Exit Ticket

1. What is one skill from this course you will apply immediately?
2. What is one skill you still want to practice?
3. What part of your capstone best represents your growth?

---

## Shared Day 12 Instructor Reference

Reuse the shared day-level instructor support from `Day12_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`
- `## Final Delivery Appendix`
- `## Certification Review Appendix`

This keeps the Day 12 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
