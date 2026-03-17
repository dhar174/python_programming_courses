# Day 12, Hour 3: Packaging and Delivery
**Python Programming Advanced - Session 12**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe packaging as repeatable install and run: 5 minutes  
- Direct instruction on requirements, quickstart, and fresh-run checks: 15 minutes  
- Live demo of a clean install path: 10 minutes  
- Guided packaging lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain the difference between \"it runs on my machine\" and a shippable deliverable
2. Create or refine `README.md`, `requirements.txt`, and `requirements-dev.txt`
3. Run the project from a fresh environment following documented steps
4. Identify missing dependencies or fragile file-path assumptions
5. Describe optional next steps such as wheel builds or executables without making them required

---

## Section 1: What Shipping Really Means (5 minutes)

### Opening Script

**[Instructor speaks:]**

Shipping is mostly not magic. It is repeatable install plus repeatable run. If another person cannot follow your README and get the project running, the project is not truly ready to hand off.

---

## Section 2: Direct Instruction on the Deliverable Recipe (15 minutes)

### Required Deliverable Pieces

Teach the runbook recipe:

- `README.md` with exact steps
- runtime dependencies in `requirements.txt`
- optional dev tooling in `requirements-dev.txt`
- `.gitignore` for environment and build outputs
- a verified entry point

### Fresh-Run Test

**[Instructor speaks:]**

The most honest packaging check is a fresh-run test in a new environment or folder. If you have to remember a hidden setup step, your documentation is incomplete.

### Optional Extras

Mention but do not require:

- `python -m build`
- wheel output
- PyInstaller executable

Keep reminding learners that the course minimum is a clear runnable source release.

---

## Section 3: Live Demo (10 minutes)

Show a quickstart sequence:

```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
python -m pytest
python api/app.py
```

Then point at the README and say:

**[Instructor speaks:]**

If these steps are not written down clearly, the deliverable is weaker than you think.

---

## Section 4: Guided Packaging Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Make your project runnable by someone else. That means documentation, dependencies, and an honest smoke test.

### Required Tasks

1. update `README.md`
2. verify runtime dependencies
3. add or update dev dependencies
4. confirm `.gitignore` covers common env and build outputs
5. perform a fresh-run smoke test

### Coaching Prompts

- Could a teammate run this without asking you three questions?
- Which environment variables need to be documented?
- Which file paths might break outside your IDE?
- Are your dependencies complete or just locally installed?

### Common Mistakes

- missing dependency in `requirements.txt`
- undocumented environment variables
- entry point confusion between GUI, API, and scripts
- assuming a relative path that only works from one directory

### Recovery Script

**[Instructor speaks:]**

If packaging feels big, focus on the runnable source release. Make the README honest and the dependencies complete. That alone is a major professional improvement.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Packaging is where a project becomes shareable. It is one of the clearest tests of whether your work is understandable beyond your own machine.

### Exit Ticket

1. What is the difference between \"it runs on my machine\" and \"it ships\"?
2. What file did you improve most today?
3. What did the fresh-run test reveal?

### Preview of the Final Hour

**[Instructor speaks:]**

Next hour is the final capstone demo, certification-style review, and retrospective. Today gives you the delivery confidence to finish well.

---

## Shared Day 12 Instructor Reference

Reuse the shared day-level instructor support from `Day12_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 12 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
