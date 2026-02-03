# Day 3, Hour 1: Comparisons + Boolean Logic
**Python Programming Basics – Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Day 1: 3 minutes
- Comparison Operators: 10-12 minutes
- Boolean Logic (and/or/not): 8-10 minutes
- Truthy/Falsey Preview: 3-5 minutes
- Live Demo (Age Gating): 5-10 minutes
- Hands-On Lab (Eligibility Checker): 25-35 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) to compare values
2. Explain the critical difference between `==` (comparison) and `=` (assignment)
3. Combine conditions using `and`, `or`, and `not`
4. Chain comparison operators in Python
5. Apply comparison logic to build eligibility checks and decision rules
6. Identify and avoid common boundary condition mistakes (off-by-one errors)

---

## Section 1: Recap & Transition from Day 1 (3 minutes)

### Quick Review

**[Instructor speaks:]**

Welcome to Day 2! Yesterday, we covered a lot of ground. Let's do a quick recap:

**Day 1 Highlights:**
- **Hour 1-2**: We set up our environment, learned about `print()`, comments, and reading errors
- **Hour 3**: We introduced variables, data types (int, float, str), and type conversion
- **Hour 4**: We built our first interactive programs with `input()` and basic if statements

Quick show of hands: **Who completed the Tip Calculator from yesterday?**

[Wait for responses]

Excellent! You're all now officially writing **programs**, not just scripts. Programs take input, make decisions, and produce output. That's a big deal.

### What We're Building Toward Today

Today, we're going to **strengthen your decision-making logic**. By the end of Day 2, your programs will be able to:

- Compare values and make complex decisions
- Format output beautifully with f-strings
- Process and transform text data
- Debug errors like a professional

**Hour 9 (right now)** is all about **comparisons and boolean logic**—the foundation of every decision a program makes.

Let's dive in!

---

## Section 2: Comparison Operators (10-12 minutes)

### The Foundation: What Is a Comparison?

**[Instructor speaks:]**

When your program needs to make a decision, it needs to **compare values**. Is this number bigger than that number? Is this string equal to that string? Is the user old enough to access this feature?

Every comparison in Python produces a **boolean result**: either `True` or `False`. Those are the only two possible outcomes.

Let's look at the six comparison operators:

### The Six Comparison Operators

**[Instructor speaks:]**

```python
# Equality
x == y    # True if x equals y
x != y    # True if x is not equal to y

# Ordering
x < y     # True if x is less than y
x > y     # True if x is greater than y
x <= y    # True if x is less than or equal to y
x >= y    # True if x is greater than or equal to y
```

Let me show you these in action:

```python
age = 18

print(age == 18)    # True (equality check)
print(age == 21)    # False
print(age != 21)    # True (not equal)
print(age < 21)     # True (less than)
print(age > 21)     # False (greater than)
print(age >= 18)    # True (greater than or equal)
```

**[Key insight]:** Notice that each of these expressions **evaluates to either True or False**. They don't print "yes" or "no"—they return a boolean value.

### The Critical Distinction: == vs =

**[Instructor speaks:]**

This is **the most common mistake** beginners make, and many experienced programmers still slip up on it:

**`=` is assignment. `==` is comparison.**

Let me say that again:

- **`=`** means "store this value in this variable"
- **`==`** means "are these two values equal?"

Here's the mistake in action:

```python
age = 18

# WRONG - This is assignment, not comparison
if age = 18:
    print("You are 18")
```

**What happens?** You get a `SyntaxError`. Python sees you trying to assign a value inside an `if` statement and knows that's not what you meant.

**Correct version:**

```python
age = 18

# RIGHT - This is comparison
if age == 18:
    print("You are 18")
```

**[Memory device]:** Think of `==` as asking a question: "Are these equal?" Two equal signs = one question.

### Quick Check #1

**[Instructor asks:]**

What will this code print?

```python
score = 85

print(score >= 80)
print(score == 100)
```

[Pause for student predictions]

**Answer:**
```
True
False
```

Good! The first comparison checks if 85 is greater than or equal to 80—it is, so `True`. The second checks if 85 equals 100—it doesn't, so `False`.

### Comparing Different Data Types

**[Instructor speaks:]**

You can compare numbers to numbers:

```python
print(10 < 20)        # True
print(5.5 > 5.0)      # True
```

You can compare strings to strings:

```python
print("apple" == "apple")    # True
print("Apple" == "apple")    # False (case matters!)
```

**But here's a common pitfall:** comparing a number to a string usually doesn't work the way you expect:

```python
age = 18
user_input = "18"

print(age == user_input)    # False!
```

**Why?** Because `18` (integer) is not the same as `"18"` (string). Remember from Day 1: you need to convert types when comparing:

```python
age = 18
user_input = "18"

print(age == int(user_input))    # True!
```

**[Important note]:** Python 3 won't let you compare incompatible types with ordering operators:

```python
print(10 < "20")    # TypeError: '<' not supported between int and str
```

This is a **good thing**—it prevents silent bugs. If you see this error, check your data types.

### Chaining Comparisons (Python's Special Feature)

**[Instructor speaks:]**

Here's something cool that Python does that many other languages don't: **you can chain comparisons**.

Instead of writing:

```python
age = 25

if age >= 18 and age <= 65:
    print("Working age")
```

You can write:

```python
age = 25

if 18 <= age <= 65:
    print("Working age")
```

This reads almost like math notation: "18 is less than or equal to age, and age is less than or equal to 65."

**Is this required?** No. The first version works fine. But chaining can make your code more readable when checking ranges.

---

## Section 3: Boolean Logic – and, or, not (8-10 minutes)

### Combining Conditions with Boolean Operators

**[Instructor speaks:]**

Real programs rarely make decisions based on just one condition. You need to combine multiple checks:

- "Is the user old enough **AND** do they have a valid membership?"
- "Is it the weekend **OR** is it a holiday?"
- "The file **NOT** already exists?"

Python gives us three boolean operators to combine conditions:

### The `and` Operator

**[Instructor speaks:]**

`and` requires **both** conditions to be True:

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can rent a car")
else:
    print("Cannot rent a car")
```

**Truth table for `and`:**

```
True  and True   → True
True  and False  → False
False and True   → False
False and False  → False
```

**Translation:** "Both must be True for the whole thing to be True."

**Real-world example:**

```python
age = 16
has_permission = True

if age >= 13 and has_permission:
    print("You can create a social media account")
```

Even though they have permission, if they're under 13, the whole condition is False.

### The `or` Operator

**[Instructor speaks:]**

`or` requires **at least one** condition to be True:

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
```

**Truth table for `or`:**

```
True  or True   → True
True  or False  → True
False or True   → True
False or False  → False
```

**Translation:** "At least one must be True for the whole thing to be True."

**Real-world example:**

```python
payment_method = "credit_card"

if payment_method == "credit_card" or payment_method == "debit_card":
    print("Card payment accepted")
```

If either payment method matches, we accept it.

### The `not` Operator

**[Instructor speaks:]**

`not` flips the boolean value:

```python
is_raining = False

if not is_raining:
    print("Let's go for a walk!")
```

**Truth table for `not`:**

```
not True   → False
not False  → True
```

**Translation:** "Reverse the boolean value."

**Real-world example:**

```python
file_exists = False

if not file_exists:
    print("Creating new file...")
```

**[Common pattern]:** Using `not` with comparisons:

```python
age = 16

if not age >= 18:
    print("You are a minor")
```

Though usually it's clearer to write:

```python
if age < 18:
    print("You are a minor")
```

### Combining Multiple Operators

**[Instructor speaks:]**

You can combine `and`, `or`, and `not`:

```python
age = 25
is_student = True
has_coupon = False

if (age < 18 or is_student) and not has_coupon:
    print("Discount applies, but you need a coupon")
```

**Order of operations:**
1. Comparisons (`<`, `==`, etc.) happen first
2. `not` happens next
3. `and` happens next
4. `or` happens last

**[Best practice]:** Use parentheses to make your intent clear:

```python
if (age < 18 or is_student) and (not has_coupon):
    print("Clear and explicit!")
```

### Quick Check #2

**[Instructor asks:]**

What will this code print?

```python
temperature = 75
is_sunny = True

if temperature >= 70 and is_sunny:
    print("Perfect beach day!")
else:
    print("Maybe another day")
```

[Pause for student predictions]

**Answer:**
```
Perfect beach day!
```

Both conditions are True (75 >= 70, and is_sunny is True), so the `and` condition is True.

---

## Section 4: Truthy and Falsey Values – A Preview (3-5 minutes)

### Beyond True and False

**[Instructor speaks:]**

Here's something that might surprise you: **in Python, every value has a "truthiness"**—it's either considered truthy or falsey in a boolean context.

**I'm not going to go deep on this now**, but I want to introduce it because you'll see it in code online.

### Falsey Values

These values are considered **False** in a boolean context:

```python
# The obvious one
False

# Empty collections
""          # empty string
[]          # empty list
{}          # empty dict
set()       # empty set

# Zero
0
0.0

# None (Python's "null" value)
None
```

### Truthy Values

**Everything else** is considered truthy:

```python
True
"any text"
[1, 2, 3]
42
-1
{"key": "value"}
```

### Why This Matters (Quick Example)

**[Instructor speaks:]**

You'll see code like this:

```python
name = input("Enter your name: ")

if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name")
```

This works because an empty string `""` is falsey, and any non-empty string is truthy.

**This is equivalent to:**

```python
if name != "":
    print(f"Hello, {name}!")
```

**[Important note]:** We're not using truthy/falsey extensively in this course yet. I just want you to recognize it when you see it. For now, **stick to explicit comparisons** like `name != ""` or `count > 0`—it's clearer.

---

## Section 5: Live Demo – Age Gating (5-10 minutes)

### Demo Script: Age-Based Access Control

**[Instructor speaks:]**

Now I'm going to build a small program that combines everything we've learned. Watch how I:
- Get user input
- Convert types
- Use comparison operators
- Combine conditions with `and`

I'll narrate my thinking as I go.

**[Open editor and create `age_gate.py`]**

**[Instructor types and speaks:]**

```python
# age_gate.py
# Purpose: Check if a user meets age and membership requirements

print("=== Membership Eligibility Checker ===\n")

# Get user input
age_input = input("Enter your age: ")
has_membership_input = input("Do you have a membership? (yes/no): ")

# Convert age to integer
age = int(age_input)

# Convert membership answer to boolean
has_membership = has_membership_input.lower() == "yes"

# Check eligibility
print("\n--- Checking eligibility ---")

# Rule 1: Must be 18 or older
if age >= 18 and has_membership:
    print("✓ Access granted! Welcome to the premium section.")
elif age >= 18 and not has_membership:
    print("✗ You are old enough, but you need a membership.")
    print("  Visit our signup page to join!")
elif age >= 13:
    print("✗ You must be 18 or older for this content.")
    print("  But you can access our teen section!")
else:
    print("✗ This content requires adult supervision.")
```

**[Run the program with several test cases]**

**Test 1: Age 25, membership yes**
```
Enter your age: 25
Do you have a membership? (yes/no): yes

--- Checking eligibility ---
✓ Access granted! Welcome to the premium section.
```

**Test 2: Age 20, membership no**
```
Enter your age: 20
Do you have a membership? (yes/no): no

--- Checking eligibility ---
✗ You are old enough, but you need a membership.
  Visit our signup page to join!
```

**Test 3: Age 15, membership yes**
```
Enter your age: 15
Do you have a membership? (yes/no): yes

--- Checking eligibility ---
✗ You must be 18 or older for this content.
  But you can access our teen section!
```

**[Instructor explains the logic:]**

Let's walk through what's happening:

1. **Line 7-8**: We get raw input as strings
2. **Line 11**: Convert age to an integer so we can compare it numerically
3. **Line 14**: This is a nice pattern—we convert "yes"/"no" to a boolean. `has_membership_input.lower() == "yes"` returns `True` or `False`
4. **Lines 20-28**: We have three conditions checking different scenarios

**Notice the order:** We check the most specific conditions first, then fall back to more general cases.

**[Key teaching moment]:**

Notice how I tested **boundary values**:
- Age exactly 18 (the threshold)
- Age 13 (the lower threshold)
- Ages above and below each threshold

This is how you verify your logic is correct. We'll talk more about this in the debugging hour.

---

## Section 6: Hands-On Lab – Eligibility Checker (25-35 minutes)

### Lab Overview

**[Instructor speaks:]**

Now it's your turn! You're going to build a similar eligibility checker, but with your own rules.

**Lab Goal:** Create a program that determines eligibility for different age brackets with multiple conditions.

### Lab Instructions: Eligibility Checker

**Scenario:** You're building a program for a community center that offers different programs based on age and residency status.

**Requirements:**

Create a Python script called `eligibility_checker.py` that:

1. **Prompts the user for:**
   - Their age (as an integer)
   - Whether they are a local resident (yes/no)

2. **Determines eligibility using these rules:**
   - **Children's Program**: Age 5-12, any residency status
   - **Teen Program**: Age 13-17, any residency status
   - **Adult Program**: Age 18-64, must be a local resident
   - **Senior Program**: Age 65+, any residency status

3. **Provides clear feedback:**
   - If eligible: Print which program(s) they qualify for
   - If not eligible: Explain why and what would make them eligible

4. **Handles boundary values correctly:**
   - Age 12 should be children's, not teen
   - Age 13 should be teen, not children's
   - Age 18 should be adult, not teen
   - Age 65 should be senior, not adult

### Starter Template

```python
# eligibility_checker.py
# Purpose: Determine community center program eligibility

print("=== Community Center Eligibility Checker ===\n")

# Get user input
age_input = input("Enter your age: ")
resident_input = input("Are you a local resident? (yes/no): ")

# Convert inputs
age = int(age_input)
is_resident = resident_input.lower() == "yes"

# Your eligibility logic goes here
print("\n--- Checking eligibility ---")

# TODO: Add your if/elif/else conditions here
```

### Example Output

**Test Case 1:**
```
=== Community Center Eligibility Checker ===

Enter your age: 8
Are you a local resident? (yes/no): no

--- Checking eligibility ---
✓ You qualify for the Children's Program!
```

**Test Case 2:**
```
=== Community Center Eligibility Checker ===

Enter your age: 30
Are you a local resident? (yes/no): no

--- Checking eligibility ---
✗ Sorry, the Adult Program requires local residency.
  You can apply for residency at City Hall!
```

**Test Case 3:**
```
=== Community Center Eligibility Checker ===

Enter your age: 70
Are you a local resident? (yes/no): yes

--- Checking eligibility ---
✓ You qualify for the Senior Program!
```

### Completion Criteria

Your solution must:
- ✅ Correctly identify all four program categories
- ✅ Use comparison operators (`<`, `<=`, `>=`) appropriately
- ✅ Handle boundary values (ages 12, 13, 18, 65) correctly
- ✅ Check residency status for the Adult Program
- ✅ Provide helpful feedback messages
- ✅ Run without errors

### Common Pitfalls to Watch For

**[Instructor speaks:]**

As you work, watch out for these common mistakes:

1. **Off-by-one errors:**
   ```python
   # WRONG - Age 18 gets counted as teen
   if age < 18:
       print("Teen program")
   
   # RIGHT - Age 18 is adult
   if age <= 17:
       print("Teen program")
   ```

2. **Comparing strings to numbers:**
   ```python
   age = "30"    # Oops, forgot to convert
   if age >= 18:  # TypeError!
   ```

3. **Case sensitivity in yes/no:**
   ```python
   # WRONG - "Yes" or "YES" won't work
   if resident_input == "yes":
   
   # RIGHT - Convert to lowercase first
   if resident_input.lower() == "yes":
   ```

4. **Forgetting the `and` operator:**
   ```python
   # WRONG - Two separate conditions
   if age >= 18:
       if is_resident:
           print("Adult program")
   
   # BETTER - Combined condition
   if age >= 18 and age <= 64 and is_resident:
       print("Adult program")
   ```

### Optional Extensions

If you finish early, try these:

1. **Multiple Programs:** Allow users to qualify for multiple programs (e.g., a 65-year-old resident qualifies for both Adult and Senior)

2. **Add a Membership Level:** Include a third input for membership level (basic/premium) and adjust eligibility

3. **Input Validation:** Check that age is positive and residency input is valid

**[Instructor speaks:]**

Alright, you have 25-35 minutes. Remember:
- Test your code with different ages, especially the boundary values
- Read error messages carefully
- Ask for help if you're stuck

Let's build!

---

## Section 7: Debrief & Exit Ticket (5 minutes)

### Solution Walkthrough

**[Instructor shares solution:]**

```python
# eligibility_checker.py
# Purpose: Determine community center program eligibility

print("=== Community Center Eligibility Checker ===\n")

# Get user input
age_input = input("Enter your age: ")
resident_input = input("Are you a local resident? (yes/no): ")

# Convert inputs
age = int(age_input)
is_resident = resident_input.lower() == "yes"

# Determine eligibility
print("\n--- Checking eligibility ---")

if 5 <= age <= 12:
    print("✓ You qualify for the Children's Program!")
elif 13 <= age <= 17:
    print("✓ You qualify for the Teen Program!")
elif 18 <= age <= 64 and is_resident:
    print("✓ You qualify for the Adult Program!")
elif 18 <= age <= 64 and not is_resident:
    print("✗ Sorry, the Adult Program requires local residency.")
    print("  You can apply for residency at City Hall!")
elif age >= 65:
    print("✓ You qualify for the Senior Program!")
else:
    print("✗ Sorry, you must be at least 5 years old for our programs.")
```

**[Key points to highlight:]**

1. **Chained comparisons** make range checks clean: `5 <= age <= 12`
2. **Order matters**: Check more specific conditions before general ones
3. **The `and` operator** combines age and residency checks
4. **Helpful messages** tell users what to do next

### Common Issues Students Encountered

**[Instructor speaks:]**

Let me address a few things I saw as I walked around:

[Adjust based on actual student work, but common issues include:]

1. **Boundary confusion:** Remember `<=` includes the number, `<` does not
2. **Residency check:** The adult program is the ONLY one that requires residency
3. **Elif order:** If you put `age >= 18` before checking `age >= 65`, seniors would match the adult condition first

### Exit Ticket

**[Instructor asks:]**

Before we wrap up Hour 9, answer this in your notes or in the chat:

**Question:** What's the difference between `==` and `=`? And why does this matter?

**Expected answer:** `=` is assignment (storing a value), `==` is comparison (checking equality). This matters because using `=` in an `if` statement causes a syntax error and doesn't test the condition you intended.

---

## Recap: What We Accomplished

In this hour, you:
✅ Learned all six comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)  
✅ Understood the critical difference between `==` (comparison) and `=` (assignment)  
✅ Combined conditions using `and`, `or`, and `not`  
✅ Saw Python's comparison chaining feature  
✅ Built a multi-condition eligibility checker  
✅ Practiced handling boundary values correctly  

**This is a major milestone.** You can now write programs that make **complex decisions** based on multiple conditions. This is the foundation of almost every program you'll ever write.

In Hour 10, we'll make your output look professional with f-string formatting.

**Great work! Take a quick 5-minute break.**

---

## Quick Reference Card (for students)

**Comparison Operators:**
```python
==    # Equal to
!=    # Not equal to
<     # Less than
>     # Greater than
<=    # Less than or equal to
>=    # Greater than or equal to
```

**Boolean Operators:**
```python
and   # Both conditions must be True
or    # At least one condition must be True
not   # Reverses the boolean value
```

**Common Patterns:**
```python
# Range check
if 18 <= age <= 65:

# Multiple conditions
if age >= 18 and has_license:

# Either/or
if day == "Saturday" or day == "Sunday":

# Negation
if not is_raining:
```

**Remember:**
- `=` assigns, `==` compares
- Test boundary values (edges of ranges)
- Use parentheses for clarity in complex conditions
- Convert input types before comparing (`int()`, `.lower()`)

---

**End of Hour 9 Script**
