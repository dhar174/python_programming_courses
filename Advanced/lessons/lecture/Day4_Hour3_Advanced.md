# Day 4, Hour 3: Capstone Planning Workshop – Scope, Milestones, and Delivery Path
**Python Programming Advanced – Session 4**

---

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 4, Hour 3 of 48, also Hour 15 in the Advanced runbook sequence
- **Focus**: Helping learners lock a realistic capstone MVP, choose a delivery path, and create a one-page plan plus README skeleton before they build further.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 4, Hour 15.
- **Prerequisites**: Learners should have enough project context to describe their core data, persistence plan, likely interface, analytics idea, and test targets.
- **Advanced trajectory**: This is a planning workshop, not a coding hour. Learners use engineering judgment to protect scope and sequence work across core, persistence, UI, analytics, tests, and packaging.
- **Instructor goal**: By the end of this hour, every learner has a realistic one-page capstone plan, a chosen GUI-first or API-first path, a README skeleton with run-instruction placeholders, and a named biggest risk.

Important instructor positioning:

- Keep students focused on deliverables they can finish. A smaller finished MVP is better than a large idea that never stabilizes.
- Do not introduce runnable code requirements in this hour. Folder structure and README examples are planning artifacts, not a new implementation assignment.
- Push for concrete verbs: add, update, save, load, search, calculate, validate, test, package.
- Treat stretch goals as a pressure-release valve. Students can preserve ambition without making every idea mandatory.
- The workshop must be long enough for writing, not just discussion. Protect the capstone planning time.

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe the capstone and set workshop expectations: 4 minutes
- Milestones and definition of done: 11 minutes
- Delivery-path decision (GUI-first vs API-first): 7 minutes
- Live Demo (sample folder structure + README skeleton + issue checklist): 7 minutes
- Hands-On Workshop (one-page capstone plan): 26 minutes
- Debrief & Exit Ticket: 5 minutes

This one-hour workshop totals exactly 60 minutes: 4 + 11 + 7 + 7 + 26 + 5 = 60. The hands-on workshop is 26 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect that workshop time. If discussion runs long, compress the delivery-path comparison rather than removing time from the one-page plan, because the written plan and README skeleton are the required artifacts.

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Lock a realistic capstone scope for an MVP rather than an aspirational wish list
2. Break the project into milestones: core, persistence, UI, analytics, tests, and packaging
3. Explain what “definition of done” means for each milestone
4. Choose a delivery path such as GUI-first or API-first and justify that choice
5. Summarize a basic data model and persistence plan in writing
6. Identify key risks, error-handling needs, and test targets before full implementation begins
7. Create a README skeleton with placeholders for setup and run instructions
8. Produce a one-page plan that can guide the next build sessions without scope drift

---

## Section 1: Reframe the Capstone and Set Workshop Expectations (4 minutes)

### What This Hour Is Really About

**[Instructor speaks:]**

This hour is a workshop, not a lecture-heavy content dump. Students are not mainly learning a new syntax feature. They are learning how to aim their effort.

Many capstones fail for predictable reasons:

- the idea is too big
- the milestones are fuzzy
- the team or student starts with flashy features instead of a stable core
- the README is postponed until the end
- there is no realistic plan for persistence, testing, or error handling

The strong projects are rarely the ones with the most ambitious idea. They are the ones with the clearest path from “basic core works” to “feature-rich but still stable.”

So today’s goal is to replace vague enthusiasm with a delivery plan.

### Keep the Workshop Encouraging and Concrete

**[Instructor speaks:]**

I want you to feel encouraged, not constrained. Planning is not about shrinking creativity. Planning is about protecting creativity from chaos.

If a student says, “I want to build an app that tracks tasks, syncs with external APIs, has analytics dashboards, multi-user auth, notifications, exports, and a GUI,” do not dismiss the ambition. Instead say, “Great long-term vision. What is the smallest version that still proves the core value?”

That question is the heart of MVP thinking.

### Quick Opening Prompt

**[Ask students:]** In one sentence, what should your capstone help a user do?

Give them about 30 seconds to think, then collect a few examples. Push for user-centered phrasing rather than implementation phrasing.

“Manage my reading list” is better than “use classes and JSON.”

---

## Section 2: Milestones and Definition of Done (11 minutes)

### The Recommended Milestone Path

**[Instructor speaks:]**

The runbook gives us a milestone sequence for a reason:

1. **Core**
2. **Persistence**
3. **UI**
4. **Analytics**
5. **Tests**
6. **Package**

This sequence protects students from building a beautiful shell around unstable logic. If the core does not work, a GUI only hides the instability temporarily. If persistence is not solved, the app forgets everything between runs. If tests arrive too late, bugs accumulate in silence.

### Milestone 1: Core

**[Instructor speaks:]**

The core is the smallest set of business rules that makes the project meaningful. For a library tracker, that might be adding books, marking progress, searching, and computing simple summaries. For an inventory app, it might be creating items, updating counts, and listing low-stock items.

A good core milestone has these properties:

- it works without a GUI
- it can be demonstrated from a script or CLI
- it has clear inputs and outputs
- errors are handled sensibly
- it represents the true value of the project

**Definition of done for core:** the service logic works correctly and can be demonstrated in isolation.

### Milestone 2: Persistence

**[Instructor speaks:]**

Persistence means state survives beyond one run. In this stage of the course, that often means JSON save/load or a persistence-ready design that can later connect to a database.

**Definition of done for persistence:** data survives restart, corrupted or missing storage is handled, and save/load behavior is observable and testable.

### Milestone 3: UI

**[Instructor speaks:]**

The user interface could be GUI-first or API-first depending on the capstone. The important thing is that the UI calls into a stable service layer rather than containing the business logic itself.

**Definition of done for UI:** a user can complete the primary workflow through the chosen interface, and interface code delegates real work to core services.

### Milestone 4: Analytics

**[Instructor speaks:]**

Analytics here does not mean massive business intelligence. It means some thoughtful insight based on your project’s data: trends, summaries, counts, averages, top items, or simple charts if appropriate.

**Definition of done for analytics:** at least one meaningful derived insight is computed from persisted project data.

### Milestone 5: Tests

**[Instructor speaks:]**

Students often think testing belongs at the end. In reality, test thinking belongs early, even if full implementation grows over time.

**Definition of done for tests:** the most important business rules and failure paths have repeatable checks.

### Milestone 6: Package

**[Instructor speaks:]**

Packaging is about project professionalism: structure, importability, documentation, and execution flow.

**Definition of done for package:** the project has a coherent layout, a usable README, and a repeatable way to run the application.

**[Prediction prompt:]** Which milestone do students most often want to jump to too early?

[Pause. Usually UI or flashy analytics.]

Exactly. And that is why we name the sequence explicitly.

---

## Section 3: Choosing a Delivery Path – GUI-First or API-First (7 minutes)

### The Decision Matters

**[Instructor speaks:]**

Students need to choose a delivery path now because it affects how they organize folders, services, and milestones. The runbook explicitly asks them to choose GUI-first or API-first. That does not mean the project can never grow in another direction later. It means the team needs a sensible first surface.

### GUI-First Path

**[Instructor speaks:]**

GUI-first makes sense when the value of the project is strongly tied to a human operator interacting directly with forms, buttons, tables, or visual workflows.

Good candidates include:

- personal productivity tools
- tracker dashboards
- data entry apps
- classroom management tools

Advantages:

- tangible and motivating quickly
- easy to demo to non-technical audiences
- strong usability feedback

Risks:

- students can hide logic in callbacks
- interface work can consume all available time
- core testing gets postponed

### API-First Path

**[Instructor speaks:]**

API-first makes sense when the project’s value is more about services, automation, integration, or future multiple clients.

Good candidates include:

- data processing services
- automation backends
- inventory or booking logic with multiple future front ends
- systems likely to integrate with outside tools

Advantages:

- clear service boundaries
- easier to test the logic directly
- supports future web, CLI, or GUI layers

Risks:

- less visually exciting at first
- students may under-document endpoints or usage
- teams may neglect human-facing demo preparation

### Choosing with a Rubric

**[Instructor speaks:]**

Give students a simple rubric:

- Who is the primary user?
- What is the main workflow?
- What is the easiest way to demonstrate value by the checkpoint?
- Which path best protects the core business logic from being tangled with interface code?

Then state the most important constraint: whichever path they choose, the core logic must still live in reusable services.

---

## Section 4: Live Demo – Folder Structure, README Skeleton, and Issue Checklist (7 minutes)

### Demo Goal

**[Instructor speaks:]**

I want students to leave this hour with a concrete artifact shape, not just planning advice. So I will show a sample project structure, a README skeleton, and a lightweight issue checklist.

```text
capstone_project/
├── README.md
├── src/
│   └── task_tracker/
│       ├── __init__.py
│       ├── models.py
│       ├── services.py
│       ├── persistence.py
│       └── ui.py
├── tests/
│   └── test_services.py
└── data/
    └── sample_data.json
```

Explain that the exact names may vary, but the structure should make responsibilities discoverable.

### README Skeleton Demo

```markdown
## Task Tracker Capstone

## Project Goal
One or two sentences describing the user problem.

## MVP Features
- Add task
- Update task status
- List overdue tasks

## Planned Milestones
- Core services
- Persistence
- Interface
- Analytics
- Tests
- Packaging

## Setup
Placeholder for environment setup.

## Run Instructions
Placeholder for application entry points.

## Testing
Placeholder for how to run tests.
```

### Issue Checklist Demo

**[Instructor speaks:]**

Show a lightweight checklist rather than a heavy project-management system:

```markdown
- [ ] Define data model
- [ ] Implement core service methods
- [ ] Add JSON save/load
- [ ] Create primary user workflow
- [ ] Add one analytics feature
- [ ] Write tests for core rules
- [ ] Finalize README and run instructions
```

Point out that a good checklist is specific enough to finish and review. “Build app” is not a helpful task. “Implement `add_task()` validation” is helpful.

### Demo Questions

**[Ask students:]**

- Which folder or file in this layout protects your business logic from UI code?
- Which README section will help your future self the most two weeks from now?
- Which checklist item is most likely to be underestimated?

Invite brief answers to keep the workshop energy active.

---

## Section 5: Hands-On Workshop – One-Page Capstone Plan (26 minutes)

### Workshop Task

**[Instructor speaks:]**

Students now draft a one-page plan in bullets. The goal is clarity, not polish. Encourage short, honest writing over elaborate prose.

Their plan should include:

- project scope and main features
- a short data model summary
- chosen UI surface or delivery path
- persistence plan
- one analytics idea
- a test plan describing what they intend to test
- a README skeleton with run-instruction placeholders
- stretch goals listed separately from MVP

### Suggested Planning Template

```markdown
## Capstone Plan

## Project Goal
What user problem does this solve?

## MVP Scope
- Feature 1
- Feature 2
- Feature 3

## Data Model Summary
- Main entity:
- Important fields:
- Relationships:

## Delivery Path
- GUI-first or API-first
- Why this path makes sense:

## Persistence Plan
- JSON save/load now
- Future database-ready considerations:

## Analytics Idea
- One useful summary, trend, or derived insight:

## Test Plan
- Core logic to test:
- Error cases to test:
- Persistence behavior to test:

## Risks and Mitigations
- Biggest scope risk:
- Biggest technical risk:

## Stretch Goals
- Optional feature 1
- Optional feature 2
```

### Workshop Mini-Budget

The 26-minute workshop can feel large unless students know how to spend it. Use this mini-budget to keep them moving:

- 3 minutes: write the project goal and MVP scope in user-centered language.
- 4 minutes: identify the main data model, fields, and relationships.
- 3 minutes: choose GUI-first or API-first and write one sentence explaining why.
- 4 minutes: write the persistence plan, including what must survive restart.
- 3 minutes: name one analytics idea that uses project data rather than invented sample data.
- 4 minutes: write the test plan, including at least one core rule and one failure case.
- 3 minutes: create the README skeleton with setup and run-instruction placeholders.
- 2 minutes: separate stretch goals from MVP and name the biggest current risk.

If students run behind, protect the data model, persistence plan, test plan, and README skeleton first. Those are the areas most likely to become vague if they are not written down during class.

### Completion Criteria

A student plan is complete when:

- the scope is realistic for the course timeline
- the MVP is distinguishable from stretch goals
- the delivery path is chosen and justified
- persistence is acknowledged rather than postponed into vagueness
- the test plan mentions both core rules and failure cases
- a README skeleton exists with setup/run placeholders

### Circulation Notes

**[Circulate:]**

Ask the same pressure-testing questions repeatedly across the room:

1. What is the smallest version that still proves the idea?
2. If time ran short, what would you cut first?
3. Where will your business logic live?
4. How will you prove data survives restart?
5. What is one failure case you already know you must handle?
6. What will you test before demo day?

When a plan feels too large, do not just say “too big.” Show where to split it:

- move notifications into stretch goals
- move multiple user roles into stretch goals
- reduce external integrations to one
- postpone advanced charts until the basic summary works

When a plan feels too vague, ask for verbs and nouns. “Analytics dashboard” is vague. “Display average completion time per project” is concrete.

### Common Pitfalls to Watch For

- Scope too big for the remaining sessions.
- No plan for persistence.
- No plan for testing.
- UI chosen, but no clear service layer underneath.
- README postponed until “later.”
- Stretch goals mixed into MVP so everything becomes mandatory.
- No mention of error handling or validation.

### Optional Extensions

If a student finishes early, suggest:

- add a simple milestone calendar with dates or class sessions
- add acceptance criteria for the top three features
- add a “not in scope” section to defend the MVP boundary
- sketch a user flow from launch to successful completion of one core task
- write a one-sentence risk mitigation for the biggest current risk

These extensions help strong students deepen their plan without forcing everyone into extra complexity.

---


### Planning Conference Questions for Circulation

**[Instructor speaks:]**

During the workshop, I want to circulate like a project coach rather than like a syntax helper. Students do not mainly need technical rescue in this hour. They need pressure-tested thinking.

Use a predictable set of coaching questions:

1. What is the user’s main job in this app?
2. What is the smallest workflow that proves the app is useful?
3. If you could only finish three features, which three would survive?
4. What piece of state must persist between runs?
5. What is the first thing you will demo if someone asks, “Show me it works”?
6. What failure case are you already planning for?
7. What part of the project can be tested without the interface?

These questions force specificity. They also help students discover that a good plan is full of verbs: create, update, save, load, calculate, validate, search.

### Model Scope-Narrowing Conversations

**[Instructor speaks:]**

Students often need help translating a big vision into a workable MVP. Below are model conversations you can use almost verbatim.

**Scenario: The feature list is too large.**

Student: “My app will track books, recommend what to read next, sync with an online API, generate analytics dashboards, support multiple users, and export PDF reports.”

Instructor: “That is a strong long-term vision. For the MVP, what single user problem do you most want to solve? If the answer is ‘help users track reading progress,’ then recommendations, multi-user support, and export may all become stretch goals. Let’s identify the core actions first: add book, update progress, list current books, save state, reload state.”

This preserves enthusiasm while restoring realism.

**Scenario: The plan is vague.**

Student: “I’m making a management app.”

Instructor: “What exactly is being managed? What objects exist? What does the user do first? What will be visible after a successful action?”

This pushes the student from abstract category labels toward a real system.

**Scenario: The UI is leading the architecture.**

Student: “I want to start with the dashboard because that’s the exciting part.”

Instructor: “What service method will the dashboard call? If that method does not exist yet, the dashboard is only mock-up energy. Let’s define the service boundary first.”

That phrasing helps students see the value of sequence.

### Example MVP vs Stretch Goal Rewrites

**[Instructor speaks:]**

Sometimes students learn best by seeing weak and strong versions side by side.

**Weak MVP statement:**

> Build a full student success platform with accounts, notifications, dashboards, analytics, exports, and calendar sync.

**Stronger MVP statement:**

> Build a course-progress tracker that lets a student add courses, update completion status, save progress, reload progress, and view a simple completion summary.

Notice what changed. The stronger version names concrete user actions and avoids bundling advanced integrations into the first promise.

Here is another example.

**Weak MVP statement:**

> Build an inventory system with AI recommendations, barcode scanning, web dashboard, mobile support, and purchase-order automation.

**Stronger MVP statement:**

> Build an inventory manager that lets a user add items, update quantities, flag low-stock items, save state to JSON, reload state, and display a low-stock report.

The point is not to reduce ambition forever. The point is to give the ambition a sequence.

### Definition-of-Done Coaching Prompts

**[Instructor speaks:]**

Students often write milestones that sound reasonable until you ask how anyone would know they are finished. That is why definition of done matters.

For each milestone, ask:

- What can the user do when this milestone is complete?
- What file or module will contain the change?
- What evidence will prove the milestone works?
- What failure case must already be handled before you call it done?

Examples of strong “done” language:

- “A user can add a task and list all tasks through the service layer.”
- “State is written to JSON, the app can restart, and tasks reappear after loading.”
- “The primary workflow works through the GUI without placing business logic directly in callbacks.”
- “A summary report displays average completion rate using persisted data.”
- “Tests cover validation rules for invalid dates and missing titles.”

### README Coaching Script

**[Instructor speaks:]**

If students resist README work because “we haven’t built everything yet,” use this script:

“Perfect. That is exactly why the README should start now. The README is not only final polish; it is a place to clarify what the project is supposed to become. If you cannot explain setup, run flow, and MVP features in writing yet, your plan is not clear enough.”

Then ask them to fill at least these sections today:

- project goal
- MVP features
- planned milestones
- placeholder setup instructions
- placeholder run instructions

This turns documentation into a planning tool rather than a chore.

### Signs of a Healthy Plan

**[Instructor speaks:]**

As you review student plans, look for these signals:

- the user problem is understandable in one or two sentences
- the MVP contains a small number of core features
- persistence is planned before advanced analytics
- one delivery path is chosen, not left undecided
- service-layer thinking is visible
- tests are named early
- stretch goals are separate and optional

A healthy plan is not necessarily the most detailed one. It is the one most likely to survive contact with reality.

### Reflection Prompt if Time Remains

**[Instructor speaks:]**

If the room reaches a natural pause, ask students to complete this sentence in writing:

> The biggest reason my capstone will succeed is __________, and the biggest reason it could drift off track is __________.

This reflection helps students recognize that project risk is manageable when it is named early.


### Final Planning Reminder Before Debrief

**[Instructor speaks:]**

If I need to summarize this entire workshop in one sentence, it is this: a capstone plan should make the next week of work easier, not more confusing.

A good plan reduces decision fatigue. It tells the student where the core logic lives, what gets built first, what counts as done, and what can wait. It also protects morale. Students who know what “enough” looks like are far more likely to finish with confidence.

So before we move into the debrief, ask students to scan their plan once more and check for these signals:

- Can I explain the user value quickly?
- Is my MVP small enough to finish?
- Did I choose one delivery path clearly?
- Did I name persistence and testing explicitly?
- Did I separate stretch goals from required work?

If the answer is yes to those questions, the plan is probably in good shape.

### Short Reflection Prompt if Time Remains

**[Instructor speaks:]**

Invite students to finish this sentence in writing:

> The most important thing I cut from my project today was ________, and cutting it makes my MVP stronger because ________.

That reflection helps students see scope reduction as strategy, not failure.


### Example Milestone Map Students Can Adapt

**[Instructor speaks:]**

Some students struggle because they understand milestones conceptually but do not know what a realistic sequence looks like over actual work sessions. Give them an example they can adapt rather than copy blindly.

Here is a reasonable milestone map for a medium-sized capstone:

- **Build Session 1:** define data models and core service methods
- **Build Session 2:** add validation and finish primary business rules
- **Build Session 3:** implement JSON save/load and prove restart behavior
- **Build Session 4:** add the chosen interface path for the main workflow
- **Build Session 5:** add one analytics feature using persisted data
- **Build Session 6:** write focused tests for the highest-value rules and failure cases
- **Build Session 7:** refine package structure, README, and demo flow

Explain that the exact count may change, but the pattern is the key: stable core first, persistence second, interface third, polish later.

### Team or Solo Workflow Guidance

**[Instructor speaks:]**

Whether students are working solo or in a small team, planning still needs ownership. Encourage them to decide who owns which milestone or module, even if that owner later collaborates with others.

Helpful ownership questions include:

- Who is responsible for the core service layer?
- Who will verify persistence actually works across runs?
- Who keeps the README current?
- Who will write or at least review the tests?

Even solo students benefit from this framing because it makes responsibilities visible instead of fuzzy. In a team, it prevents everyone from choosing the fun surface work while no one owns validation, persistence, or tests.

### Instructor Closing Coaching Note for the Workshop Portion

**[Instructor speaks:]**

Remind students that planning is allowed to change, but it should not drift casually. Changes should happen because they learned something, reduced risk, or clarified user value—not because every new idea became an obligation.

That distinction helps students treat a plan as a living tool rather than a forgotten document.


### Final Instructor Checklist for Plan Review

**[Instructor speaks:]**

When I review a student’s capstone plan quickly, I ask whether I can clearly locate six things on the page:

- the user problem
- the MVP features
- the chosen delivery path
- the persistence plan
- the analytics idea
- the test plan

If any of those are missing, the plan is probably still too fuzzy. If they are all present and realistic, the student is much more likely to turn planning into progress.


### One-Sentence Takeaway to Repeat Aloud

**[Instructor speaks:]**

If students remember one sentence from this workshop, let it be this: **a realistic capstone plan is not the enemy of ambition; it is the structure that gives ambition a real chance to ship.**

## Section 6: Debrief & Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

Planning can feel less exciting than coding, but mature developers know that a realistic plan saves enormous time and frustration. Today’s strongest output is not a repository full of code. It is a map that tells students what code to write next, in what order, and why.

Reinforce the central ideas:

- MVP first
- milestones in sequence
- services before surface polish
- persistence cannot stay abstract forever
- tests are part of the plan, not a rescue mission at the end
- documentation begins now, not on submission day

**[Ask students:]** What feature is definitely in your MVP, and what feature did you move to stretch goals today?

That question is powerful because it reveals whether students actually protected scope.

Then ask the runbook's quick-check question verbatim:

**[Quick check:]** What feature is your MVP, and what is your biggest risk?

### Exit Ticket

**[Instructor asks:]**

1. What feature is your MVP, in one sentence?
2. What is your chosen delivery path: GUI-first or API-first, and why?
3. What is your biggest project risk right now?
4. What is one thing you already know you need to test?

**[Expected direction of answers:]**

- The MVP statement should describe real user value, not just technical mechanisms.
- The delivery path should connect to user workflow and project architecture.
- The biggest risk should be honest and specific, such as scope, persistence, or integration complexity.
- The test target should name a core rule or failure path.

### Instructor Closing Line

**[Instructor speaks:]**

Next hour, we convert planning into a concrete technical checkpoint: a persistence-ready core with JSON save/load, logging, and error handling. The best capstone plans will make that build feel like the obvious next step.
