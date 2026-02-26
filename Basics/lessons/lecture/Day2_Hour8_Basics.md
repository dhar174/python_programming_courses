# Hour 8: Checkpoint 1 — Fundamentals Mini-Assessment
Python Programming (Basic) • Day 2, Session 2

---

## Learning Outcomes
- Demonstrate basic script writing, variables, numbers, strings, and input
- Apply concepts from Hours 1–7 in a practical exercise
- Self-assess understanding of Python fundamentals

---

## Checkpoint Overview

### Assessment Format
- **Open-book**: Notes and slides allowed
- **Individual**: Complete your own work
- **Timeboxed**: 45–60 minutes for the lab
- **Focus**: Correctness first, then formatting

---

## Instructor Talk Points

### Before Starting
- Explain the rules: open-book, individual, timeboxed
- Remind: focus on **correctness first**, then formatting
- Encourage: test with sample inputs before submitting

### During Assessment
- Circulate and observe (don't solve for them)
- Note common struggles for debrief
- Allow questions about requirements, not solutions

---

## Demo: Sample Rubric Walkthrough

### How Submissions Will Be Evaluated
1. **Runs without errors** (40%)
   - Program executes end-to-end
   - No crashes on valid input

2. **Correct calculations** (30%)
   - Math is accurate
   - Type conversions done properly

3. **Readable output** (20%)
   - Formatted nicely
   - Clear labels for values

4. **Code quality** (10%)
   - Meaningful variable names
   - Appropriate comments

---

## Checkpoint Lab: Simple Receipt Generator

**Time: 45-60 minutes**

### Requirements
- Input: item name, quantity, price per item
- Compute subtotal and total
- Print a receipt with aligned lines and 2-decimal money formatting

---

## Receipt Generator: Expected Output

### Example Interaction
```
=== Receipt Generator ===
Enter item name: Widget
Enter quantity: 3
Enter price per item: 9.99

========== RECEIPT ==========
Item:     Widget
Quantity: 3
Price:    $9.99 each
-----------------------------
Subtotal: $29.97
=============================
```

---

## Receipt Generator: Sample Solution

```python
# Receipt Generator
print("=== Receipt Generator ===")

# Get input
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

# Calculate
subtotal = quantity * price

# Print receipt
print()
print("=" * 28)
print("         RECEIPT")
print("=" * 28)
print(f"Item:     {item_name}")
print(f"Quantity: {quantity}")
print(f"Price:    ${price:.2f} each")
print("-" * 28)
print(f"Subtotal: ${subtotal:.2f}")
print("=" * 28)
```

---

## Optional Quiz (10 minutes)

### Quick Knowledge Check
8–10 questions covering:
- Variable types (str, int, float, bool)
- Arithmetic operators
- String indexing and slicing
- String methods
- Type conversion

---

## Sample Quiz Questions

### Question 1
What is the output of `print(type(42))`?
- A) `int`
- B) `<class 'int'>`
- C) `42`
- D) `number`

**Answer**: B

---

## Sample Quiz Questions

### Question 2
What does `"Python"[2:5]` return?
- A) `"Pyt"`
- B) `"yth"`
- C) `"tho"`
- D) `"thon"`

**Answer**: C (`"tho"` — indices 2, 3, 4)

---

## Sample Quiz Questions

### Question 3
Why does `input()` always return a string?
- A) Because keyboards only type text
- B) To avoid errors with special characters
- C) Because Python doesn't know what type you want
- D) It's a bug in Python

**Answer**: C

---

## Completion Criteria (Hour 8)

✓ Program runs end-to-end without crashes  
✓ Correct math and type conversions  
✓ Output is readable and formatted

---

## Common Pitfalls (Hour 8)

⚠️ **Forgetting float conversion for price**
```python
price = input("Price: ")  # String!
total = price * 3  # '9.999.999.99' not 29.97
```

⚠️ **String concatenation vs numeric addition**
```python
# ❌ Wrong
result = "3" + "5"  # '35'
# ✓ Correct
result = int("3") + int("5")  # 8
```

---

## Optional Extensions

- Add: discount percent
- Add: tax percent

```python
# Extension example
tax_rate = 0.08  # 8% tax
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Total:    ${total:.2f}")
```

---

## Quick Check (Debrief)

**Question**: Ask 2–3 learners to explain how they debugged one error.

### Discussion Points
- What error did you encounter?
- How did you identify the problem?
- What was your fix?

---

# Session 2 Wrap-Up

## What We Covered Today

### Hour 5: String Fundamentals
- Indexing and negative indexing
- Slicing with `s[start:end]`
- The `len()` function
- Membership with `in`

### Hour 6: String Methods
- `.lower()`, `.upper()`, `.strip()`
- `.replace()` and `.find()`
- String immutability

### Hour 7: Input/Output
- `input()` returns strings
- Type conversion with `int()` and `float()`
- Unit converter exercise

### Hour 8: Checkpoint 1
- Receipt Generator assessment
- Fundamentals review

---

## Scope Guardrail Reminder

### Stay in Basics Scope
✓ Core string operations and methods  
✓ Simple type conversion  
✓ Basic input/output patterns  
✓ Clear variable names and formatting

### Not Yet (Advanced Topics)
✗ Regular expressions  
✗ String formatting with format()  
✗ Advanced string parsing  
✗ Exception handling (try/except)

---

## No-Go Topics for Basics Course

### Keep for Advanced
- Web frameworks (Flask/Django)
- Databases/SQL/ORM
- GUI frameworks (Tkinter/PyQt)
- Testing frameworks (pytest)
- Packaging/distribution

---

## Homework / Practice

### Recommended Exercises
1. Create a username generator with additional rules
2. Build a simple data cleaner for messy text
3. Create a multi-unit converter (length, weight, temperature)
4. Practice string slicing with different scenarios

---

## Next Session Preview

### Session 3 (Hours 9–12)
- Hour 9: Booleans and comparisons
- Hour 10: if/elif/else branching
- Hour 11: Combining conditions
- Hour 12: Checkpoint 2 – Branching mini-assessment

---

## Questions?

**Remember**:
- Strings are immutable — always assign back
- `input()` returns strings — convert when needed
- Use `in` for simple membership checks
- Test with sample data before submitting

---

# Thank You!

See you in Session 3!
