# Session 12, Hour 4: Final Assessment & Certification-Style Review

## 🎯 Outcomes
- Demonstrate end-to-end competency in Basics objectives.
- Identify next-step study targets.

## 🗣️ Instructor Speaking Script

### Introduction (10-15 min)
"We've made it! Hour 48 of 48. Today is about celebrating what you've built and reviewing the fundamental skills that will prepare you for the PCEP certification and beyond."

"Here is our review agenda. Think about how comfortable you are with each of these:"
- Types and conversions
- Strings and formatting
- Data structures (lists, tuples, sets, dictionaries)
- Conditionals and loops
- Functions, modules, and basic class usage
- Files, pathlib, and directory listing
- Exceptions like `ValueError`, `FileNotFoundError`, and `JSONDecodeError`.

"The certification exams are heavy on conceptual understanding and code reading. You don't just write code; you read it, trace it, and predict its output."

### Live Demo (5-10 min)
*Action: Share your screen showing a short code snippet.*

"Let's do a quick 'predict the output' exercise together."

*Action: Show this snippet:*
```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
```
"Who can tell me what this prints, and why? ... Exactly, it prints 4, because `x` and `y` point to the same list in memory. This is the kind of reading you must be comfortable doing."

## 💻 Final Assessment (60-75 min)

**Activity 1: Capstone Demos (approx. 30-45 min)**
- Students present their 3-minute demos.
- Score each demo using the Capstone Rubric.

**Activity 2: Written/Quiz Review (15-20 min)**
Run through the following code reading prompts with the class. Either display them one by one or provide them as a handout.

**Code Reading Set (10 prompts):**
1. Predict output: string slicing + `len()`
2. Predict output: f-string with numeric conversion
3. Find bug: off-by-one loop with `range()`
4. Find bug: list index error (guard with `len()`)
5. Find bug: dict key access (use `in` or `.get()`)
6. Trace: function return vs `print`
7. Trace: import from `utils.py` (working directory reminder)
8. Trace: JSON load with missing file (handle `FileNotFoundError`)
9. Trace: `JSONDecodeError` recovery to defaults
10. Explain: why `pathlib` avoids hardcoded paths

**Activity 3: Individual Feedback**
- Provide brief feedback to each student on their strengths and what they should practice next.

### ✅ Completion Criteria
- Capstone meets all requirements.
- Learner can accurately explain their code at a high level.

### 🛑 Common Pitfalls (Instructor Eyes Only)
- **Time management:** Demos can easily run over time. Keep a strict 3-minute timer per student.

### 🚀 Optional Extensions
- Provide the students with a link to practice PCEP exams or a printed question set (no new topics outside the basics).

## 📝 Quick Check / Exit Ticket
**Ask the class:** "Before we wrap up the course, what is one concept you feel really strong about, and what is one concept you want to review further?"
