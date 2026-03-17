# Day 10, Hour 3: Integration Choice - GUI to API or Parallel UI and API
**Python Programming Advanced - Session 10**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame the architecture decision: 5 minutes  
- Direct instruction on the two valid integration patterns: 15 minutes  
- Live demonstration of one end-to-end flow: 10 minutes  
- Guided integration sprint: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Describe two valid integration patterns for the capstone
2. Choose an approach that matches their current project maturity and risk tolerance
3. Demonstrate how GUI and API work over the same underlying logic or data store
4. Identify tradeoffs between direct local service calls and GUI-to-API calls
5. Keep the system coherent rather than accidentally building two separate applications

---

## Instructor Prep Notes

- Present both options neutrally; do not imply that GUI-to-API is always superior
- Use the runbook's exact framing: Option A, GUI to API; Option B, parallel surfaces sharing the same service layer and DB
- Help learners choose the safer path if they are behind schedule

---

## Section 1: The Architecture Choice (5 minutes)

### Opening Script

**[Instructor speaks:]**

This hour is about choosing an integration path, not proving that one architecture is morally better than another. You have two valid options in this course:

- Option A: the GUI talks to the API
- Option B: the GUI stays local and the API exists as a parallel interface over the same service layer and database

Either can succeed. The right choice depends on where your project is stable and where the risk lives.

---

## Section 2: Direct Instruction on the Two Options (15 minutes)

### Option A: GUI to API

**[Instructor speaks:]**

In Option A, the GUI becomes an HTTP client. Instead of calling the service layer directly, it calls your client functions, which call the API. The flow looks like this:

```text
GUI -> client functions -> API routes -> service -> repository -> database
```

Benefits:

- one outward-facing interface for writes and reads
- GUI exercises the same API contract another external client would use
- good practice for decoupled systems

Tradeoffs:

- more moving pieces
- more failure points
- GUI must handle network-style concerns such as timeouts or connectivity

### Option B: Parallel GUI and API

**[Instructor speaks:]**

In Option B, the GUI keeps using the service layer locally, and the API uses the same service and repository structure as a separate surface. The flow looks like this:

```text
GUI -> service -> repository -> database
API -> service -> repository -> database
```

Benefits:

- less integration friction
- faster to stabilize for course delivery
- still demonstrates clean architecture and reuse

Tradeoffs:

- GUI does not exercise the HTTP contract
- you must stay disciplined so the two surfaces do not drift in fields or behavior

### How to Choose

**[Instructor speaks:]**

If your API is stable and your client functions are working, Option A is reasonable. If your project is still shaky, Option B is often the smarter choice because it protects the milestone and still demonstrates architectural reuse.

This is an excellent place to model professional judgment. Choosing the safer path is not less advanced. It is often more mature.

---

## Section 3: Live End-to-End Demonstration (10 minutes)

### Suggested Demo: Option B First

Because it is easier to show reliably, demonstrate Option B first:

**[Instructor speaks:]**

I am going to show the GUI adding a record locally through the service layer, then I will call the API and show that the same data is visible there because both surfaces share the same database and core logic.

Then say:

**[Instructor speaks:]**

This proves the system is cohesive even though the interfaces are different.

If time allows, also show Option A conceptually by swapping one GUI action to use the client module instead.

---

## Section 4: Guided Integration Sprint (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Choose one integration path and make it work end to end. The success condition is not theoretical elegance. It is a coherent system that you can explain and demo.

### Required Work

Learners should:

1. Choose Option A or Option B intentionally
2. Document the choice in a short note or README line
3. Demonstrate both surfaces touching the same underlying data
4. Fix at least one mismatch in field names, refresh behavior, or flow if discovered

### Coaching Prompts

- What is the biggest risk in your chosen architecture?
- How will you prove both surfaces operate on the same data?
- If the GUI is calling the API, what happens when the API is down?
- If the GUI is local, how are you ensuring the API and GUI use the same service rules?

### Common Mistakes

- GUI uses one field name while API uses another
- GUI displays stale data because it does not refresh after a write
- learners accidentally create two separate database files
- integration choice is not explicit, so the project becomes inconsistent

### Recovery Script

**[Instructor speaks:]**

If you are behind, choose Option B and make it solid. A stable parallel architecture is better than a half-finished GUI-to-API flow.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Integration decisions are where project reality meets design ideals. Today was an opportunity to make a deliberate tradeoff instead of drifting into one by accident. That is exactly the kind of judgment good engineers develop.

### Exit Ticket

1. Which option did you choose and why?
2. What is the biggest tradeoff of that choice?
3. How did you prove the system is still one coherent application?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour is Checkpoint 5. You will demonstrate the API milestone with persistence, consistent errors, security gating, and a convincing end-to-end flow.

---

## Shared Day 10 Instructor Reference

Reuse the shared day-level instructor support from `Day10_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 10 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
