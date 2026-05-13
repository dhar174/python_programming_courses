# Day 3, Hour 1: Comparisons + Boolean Logic
**Python Programming Basics – Session 3**

**Learning Outcomes for This Hour:**
By the end of this hour, you will be able to:
1. Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) to compare values
2. Explain the critical difference between `==` (comparison) and `=` (assignment)
3. Combine conditions using `and`, `or`, and `not`
4. Chain comparison operators in Python
5. Apply comparison logic to build eligibility checks and decision rules

---

## Section 1: Instructor Prep & Setup Checklist

### Pre-Class Checklist
- [ ] Have Python 3 IDE or REPL ready with a clean script file
- [ ] Test all demo code before class; confirm output matches expectations
- [ ] Prepare the age-gating demo (`age_gate.py`) to use live
- [ ] Prepare the eligibility checker rubric (scoring criteria visible to learners)
- [ ] Draw a truth table or decision tree on paper/whiteboard to visualize `and`/`or`/`not`
- [ ] Prepare 3–4 "mystery conditionals" for prediction exercises
- [ ] Have boundary value test cases written out (ages 12, 13, 18, 65 exactly)
- [ ] Prepare a "common mistakes" reference (type mixing, string comparisons, logic errors)

### Timing Breakdown
- **Opening & Recap** (3 min)
- **Comparison Operators** (10 min)
- **Boolean Logic (and/or/not)** (8 min)
- **Truthy/Falsey Preview** (3 min)
- **Live Demo (Age Gating)** (5 min)
- **Lab Checkpoint Work** (20 min with 3 checkpoints)
- **Debrief & Exit Ticket** (3 min)
- **Total: 52 minutes** (8 min buffer for questions)

### Materials & Resources
- IDE or Python REPL
- Truth table or decision tree diagram (for whiteboard)
- Sample code: age gating, eligibility checker
- Eligibility checker lab prompt (provided below)
- Timer (visible to learners)

### Session Timing Overview
**Total Time:** 60 minutes (52 min core + 8 min buffer)  
- Recap & Transition from Day 2: 3 minutes
- Comparison Operators: 10 minutes
- Boolean Logic (and/or/not): 8 minutes
- Truthy/Falsey Preview: 3 minutes
- Live Demo (Age Gating): 5 minutes
- Hands-On Lab (Eligibility Checker): 20 minutes (3 checkpoints)
- Debrief & Exit Ticket: 3 minutes

---

## Section 2: Opening Script & Recap (3 minutes)

### Quick Review

**[Instructor speaks:]**

Welcome to Day 3! Over the first two days, we covered a lot of ground. Let's do a quick recap:

**Day 1 Highlights:**
- **Hour 1-2**: We set up our environment, learned about `print()`, comments, and reading errors
- **Hour 3**: We introduced variables, data types (int, float, str), and type conversion
- **Hour 4**: We explored numbers, arithmetic operators, and operator precedence

**Day 2 Highlights:**
- **Hour 5-6**: We dove into string fundamentals—indexing, slicing, `len()`—and mastered string methods like `.upper()`, `.lower()`, `.find()`, `.replace()`, and `.strip()`
- **Hour 7**: We built interactive programs with `input()` and practiced type conversion in real scenarios
- **Hour 8**: We completed Checkpoint 1, putting all those fundamentals to the test

Quick show of hands: **Who completed the Tip Calculator from yesterday?**

[Wait for responses]

Excellent! You're all now officially writing **programs**, not just scripts. Programs take input, make decisions, and produce output. That's a big deal.

### What We're Building Toward Today

Today, we're going to **strengthen your decision-making logic**. By the end of Day 3, your programs will be able to:

- Compare values and make complex decisions
- Format output beautifully with f-strings
- Process and transform text data
- Debug errors like a professional

**Hour 9 (right now)** is all about **comparisons and boolean logic**—the foundation of every decision a program makes.

Let's dive in!

---

## Section 3: Comparison Operators (10-12 minutes)

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

### Real-World Comparison Scenarios

**[Instructor speaks:]**

Let's look at a few more examples, because comparisons are everywhere in real programs. Think about the kinds of checks you make every day—even outside of code.

**Scenario 1: Temperature check**

Imagine you're building a weather app that tells people what to wear:

```python
temperature = 32

print(temperature <= 32)    # True — freezing or below
print(temperature > 100)    # False — not dangerously hot
print(temperature != 72)    # True — not "room temperature"
```

**Output:**
```
True
False
True
```

Every decision this app makes starts with a comparison like one of these.

**Scenario 2: Password length validation**

When users create an account, you need to check that their password meets minimum requirements:

```python
password = "secret"
min_length = 8

print(len(password) >= min_length)    # False — "secret" is only 6 characters
```

**Output:**
```
False
```

See how we used `len()` from Day 2 inside a comparison? The tools you already know keep combining in new ways.

**Scenario 3: Checking string equality (case-sensitive)**

Remember `.lower()` from our string methods lesson? Here's why it matters for comparisons:

```python
user_answer = "Paris"
correct_answer = "paris"

print(user_answer == correct_answer)              # False — capital P vs lowercase p
print(user_answer.lower() == correct_answer)      # True — both are "paris"
```

**Output:**
```
False
True
```

**[Key takeaway]:** Comparisons are the building blocks. On their own, they answer simple yes/no questions. In the next section, we'll learn how to **combine** those questions into complex logic.

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

## Section 4: Boolean Logic – and, or, not (8-10 minutes)

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

### Quick Check #3

**[Instructor asks:]**

Let's try a slightly harder one. What does this print?

```python
username = "admin"
password = "1234"
is_locked = False

if username == "admin" and password == "secret" or not is_locked:
    print("Access granted")
else:
    print("Access denied")
```

[Pause for student predictions]

**Answer:**
```
Access granted
```

**Wait—the password is wrong! How did that happen?**

Remember the order of operations: `and` is evaluated before `or`. So Python reads this as:

```
(username == "admin" and password == "secret") or (not is_locked)
```

The first part is `True and False` → `False`. But the second part is `not False` → `True`. So the whole expression becomes `False or True` → `True`.

**This is a real bug you could write.** The fix is to require all three conditions with explicit parentheses:

```python
if (username == "admin") and (password == "secret") and (not is_locked):
    print("Access granted")
```

Now the logic is crystal clear: the username must be `"admin"`, AND the password must be `"secret"`, AND the account must not be locked. All three must be `True` for access to be granted. **Parentheses aren't just for clarity—they prevent subtle security bugs.**

---

## Section 5: Truthy and Falsey Values – A Preview (3-5 minutes)

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

### One More Practical Example

**[Instructor speaks:]**

Here's another pattern you'll run into almost immediately. Say you ask a user for their age and want to make sure they actually typed something before you try to convert it:

```python
age_input = input("Enter your age: ")

if age_input:
    age = int(age_input)
    print(f"You are {age} years old")
else:
    print("You didn't enter anything!")
```

If the user just presses Enter without typing, `age_input` is `""` (an empty string)—which is falsey. The `if age_input:` check prevents us from calling `int("")`, which would crash with a `ValueError`.

And here's a numeric version of the same idea:

```python
items_in_cart = 0

if items_in_cart:
    print("Proceed to checkout")
else:
    print("Your cart is empty")
```

**Output:**
```
Your cart is empty
```

Because `0` is falsey, this prints the "empty" message. It's the same as writing `if items_in_cart != 0:` or `if items_in_cart > 0:`, just shorter.

**[Reminder]:** You don't need to write code this way yet. The explicit versions (`!= ""`, `> 0`) are perfectly fine and often easier to read. But now you'll understand what's happening when you see the short form online or in someone else's code.

---

## Section 6: Live Demo – Age Gating (5-10 minutes)

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

## Section 7: Hands-On Lab – Eligibility Checker (20 minutes, 3 checkpoints)

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

### Lab Checkpoints

#### **Checkpoint 1: Input & Type Conversion (5 minutes)**
- Get age and residency input from the user
- Convert age to integer
- Convert residency answer to boolean with `.lower()`
- Test with at least two different inputs
- **Success criteria**: Both inputs are received and converted correctly with no type errors

#### **Checkpoint 2: Build Core If/Elif Logic (10 minutes)**
- Implement the eligibility rules using if/elif/else
- Test boundary values: ages 12, 13, 18, 65 (exactly)
- Verify only ONE program prints per user
- Check at least 4 different age values
- **Success criteria**: All four age ranges print correct program names; boundary values work correctly

#### **Checkpoint 3: Debug & Optimize (5 minutes)**
- Run through at least one non-resident adult case
- Verify the residency check works for the Adult Program only
- Test with invalid input (optional: add error handling)
- Add comments explaining the boundary checks
- **Success criteria**: All test cases pass; code is readable with clear comments

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

Alright, you have 20 minutes with three checkpoints. Focus on:
- Getting input and converting types first (Checkpoint 1)
- Building correct logic for each age bracket (Checkpoint 2)
- Testing boundary values thoroughly (Checkpoint 3)

Let's build!

---

## Section 8: Debrief & Exit Ticket (3 minutes)

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

## Section 9: Troubleshooting Pitfalls & Common Mistakes

### Pitfall 1: Confusing `=` (Assignment) with `==` (Comparison)
**The mistake:**
```python
if age = 18:  # SYNTAX ERROR
    print("Adult")
```
**Why it happens:** Muscle memory from math class; in programming, `=` is assignment, not comparison.

**How to catch it:** IDE highlighting; Python raises `SyntaxError: invalid syntax`. Read the error message carefully—it tells you the exact line.

**The fix:**
```python
if age == 18:  # Correct comparison
    print("Adult")
```

### Pitfall 2: Type Mixing (Comparing String to Integer)
**The mistake:**
```python
age = input("Enter your age: ")  # Returns a STRING
if age > 18:  # ALWAYS False (string comparison, not numeric)
    print("Adult")
```
**Why it happens:** `input()` returns a string; students forget the `int()` conversion.

**How to catch it:** Test with edge values like age 20; if the program says "Not Adult," you have a type issue.

**The fix:**
```python
age = int(input("Enter your age: "))  # Convert to integer
if age > 18:
    print("Adult")
```

### Pitfall 3: Off-by-One Errors in Boundary Conditions
**The mistake:**
```python
if age > 18:  # Missing equality; age 18 falls through
    print("Adult")
else:
    print("Not Adult")
# For age 18, this prints "Not Adult" – wrong!
```
**Why it happens:** Confusion about whether boundaries are inclusive or exclusive; `<` vs. `<=`.

**How to catch it:** Write a test case for the boundary value itself (age 18, 13, 65, 5). Trace through your code line by line.

**The fix:**
```python
if age >= 18:  # Include equality
    print("Adult")
```

### Pitfall 4: Incorrect Operator Precedence in Complex Conditions
**The mistake:**
```python
if age >= 18 and is_resident or income > 50000:
    # This reads as: (age >= 18 AND is_resident) OR (income > 50000)
    # Not the intended: (age >= 18 AND is_resident AND income > 50000)
```
**Why it happens:** Operator precedence: `and` binds tighter than `or`.

**How to catch it:** Add parentheses to clarify intent during testing; trace through with sample inputs.

**The fix:**
```python
if (age >= 18 and is_resident) or income > 50000:
    # Explicitly group; still might not be your intent; re-read
if age >= 18 and (is_resident or income > 50000):
    # Or this grouping—which logic did you want?
```

### Pitfall 5: Not Handling Truthy/Falsey in Boolean Expressions
**The mistake:**
```python
is_resident = "yes"  # String, not boolean
if is_resident:  # Truthy—any non-empty string is True
    print("Resident")
# This always prints, even if is_resident = "no" (which is truthy!)
```
**Why it happens:** Not distinguishing between string values and boolean `True`/`False`.

**How to catch it:** Test with `is_resident = "no"` or `is_resident = False`; see which branches execute.

**The fix:**
```python
is_resident = True  # Use boolean, or
is_resident = input("Are you a resident? (yes/no): ").lower() == "yes"  # Convert string to boolean
```

---

## Section 10: Wrap-Up & Recap

### What We Covered Today

**Hour 9: Comparisons & Boolean Logic**
- **Comparisons:** `==`, `!=`, `<`, `>`, `<=`, `>=` let your programs make decisions based on values
- **Boolean Logic:** `and`, `or`, `not` let you combine multiple conditions
- **Chaining:** Python allows `5 < age < 18`, which is elegant and readable
- **Truthy/Falsey:** Every value in Python has a truth value; understand the hidden rules to avoid subtle bugs

### Why This Matters

You just wrote your first **decision-making program**. Comparisons and boolean logic are the **foundation of all conditionals**. By Hour 11 (tomorrow), you'll use these same operators inside `if`-statements to control program flow. By Day 4, you'll use them in loops. Every professional program on Earth uses this logic—in web apps, mobile apps, embedded systems, AI, everything.

### Looking Ahead

- **Hour 10 (today, afternoon):** We'll introduce `if`-statements—the final piece of Day 3's puzzle. Your programs will start asking questions and making decisions.
- **Day 4 (tomorrow):** Checkpoint 1 Assessment. We'll revisit everything from Days 1-3 to ensure you have the fundamentals locked down.
- **Advanced Path:** Once conditionals are solid, you'll tackle loops, functions, data structures—all built on this foundation.

### Encourage Reflection

**Quick thought exercise:**
- Think of a decision *you* make every day (e.g., "If it's raining and I'm going out, I take an umbrella").
- Can you write it as a Python condition? Try it—talk to a peer or jot it down.

---

## Section 11: Facilitation Notes

### Classroom Management & Timing

- **Start Lab by minute 35** to ensure 20 minutes of focused checkpoint work
- Use a visible timer projected on screen during lab; announce "5 minutes remaining"
- Watch for students stuck on boundary values; pair them with students who've passed Checkpoint 2
- Common interruption: students testing with invalid input (non-numeric age). Have them add a comment in their code: `# Note: This version assumes valid integer input`

### Intervention Strategies

**If most students are behind at Checkpoint 1 (minute 7):**
- Model the first 3 lines of code on the board while students code along
- Re-emphasize: "Try typing the code line by line, don't copy-paste yet"

**If students are confused about boundary checks (Checkpoint 2):**
- Draw a number line on the whiteboard showing 5, 12, 13, 17, 18, 64, 65
- Mark the ranges with colors: green (5-12), blue (13-17), yellow (18-64), purple (65+)
- Ask: "If I'm exactly 13, which range do I fall into?" (NOT blue—ask them to pick between green and blue to re-engage)

**If a student forgets the residency check:**
- Don't fix it; ask: "Which program is the ONLY one that checks residency?" (Wait for answer: Adult)
- Then: "Where in your code do you check for Adult?" (Guide them to add `and is_resident`)

### Pacing Checkpoints

- **Checkpoint 1 (5 min):** Expect most students done by minute 7. Those slower might finish by minute 9.
- **Checkpoint 2 (10 min):** Should see boundary value testing by minute 17. If debugging `age <= 17` vs. `age < 18`, point them to the number line.
- **Checkpoint 3 (5 min):** Leave time for adding comments. If a student wants to add input validation, that's an extension, not core.

### Troubleshooting Tips

- **"I got a TypeError on line X"**: Almost always a missing `int()` conversion. Ask: "What type is the input?" (String) → "What type do you need?" (Integer) → "What function converts it?"
- **"My code runs but the wrong program prints"**: Likely an off-by-one error. Ask them to trace through with age 18: does `age < 18` print? (Should not.)
- **"It works for age 20 but not age 18"**: Classic boundary value bug. Ask: "At what exact age does the condition change?" → Trace through the edge case together.

---

## Section 12: Assessment Rubric

### Lab Submission Grading (Total: 10 points)

#### **Correctness: Input & Type Conversion (2 points)**
- ✅ **Full (2 pts)**: Both inputs collected; age converted to `int()` with no errors; residency converted to boolean with `.lower()`
- ⚠️ **Partial (1 pt)**: Age converted but residency not; OR inputs collected but only one converted
- ❌ **Missing (0 pts)**: Inputs not collected or no conversions attempted

#### **Correctness: If/Elif/Else Logic (4 points)**
- ✅ **Full (4 pts)**: All four age ranges (5-12, 13-17, 18-64 with residency, 65+) produce correct output; boundary values (ages 12, 13, 18, 65) handled correctly
- ⚠️ **Partial (2 pts)**: 3 out of 4 ranges work OR all ranges work but at least one boundary value fails
- ❌ **Missing (0 pts)**: Fewer than 3 ranges implemented OR logic fundamentally broken (e.g., all outputs identical)

#### **Correctness: Residency Check (2 points)**
- ✅ **Full (2 pts)**: Adult Program (18-64) ONLY checks `is_resident` AND non-residents over 18 see helpful message
- ⚠️ **Partial (1 pt)**: Residency check present but only partially applied (e.g., checks all ages or misses the message)
- ❌ **Missing (0 pts)**: No residency check OR residency check applied incorrectly

#### **Code Quality: Comments & Clarity (2 points)**
- ✅ **Full (2 pts)**: Code includes comments on at least one boundary check; variable names are clear (`age`, `is_resident`, not `a`, `x`)
- ⚠️ **Partial (1 pt)**: Either minimal comments OR variable names could be clearer
- ❌ **Missing (0 pts)**: No comments; unclear variable names throughout

---

### Checkpoint Success Criteria (Self-Assessment for Students)

| Checkpoint | Success Looks Like | How to Check |
|------------|-------------------|--------------|
| **1: Input & Conversion** | You entered an age, got a yes/no answer, and both printed back correctly as the right type | Type `print(type(age))` — should be `<class 'int'>` |
| **2: Core Logic** | Your program prints ONE program name for ages 10, 15, 25, and 70. Age 18 prints "Adult," age 13 prints "Teen." | Manually test with ages 12, 13, 18, 65; verify output |
| **3: Residency Check & Comments** | A 30-year-old non-resident sees the residency message. Your code has at least one comment explaining a boundary check. | Type `python eligibility_checker.py` with age 30, residency "no" |

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

### What Comes Next

**[Instructor speaks:]**

Take a moment to appreciate what you can do now. After just two days of fundamentals, you're already writing programs that:

- **Accept input** from a user (with `input()` and type conversion)
- **Store and manipulate data** (variables, strings, numbers)
- **Make decisions** (comparisons + `and`/`or`/`not`)

That's the core loop of most software: *get data → process data → decide what to do → show the result*. The rest of this course builds on exactly this foundation.

In the next hour, we'll focus on **f-string formatting**—making your output look clean and professional instead of just functional. After that, we'll tackle string processing patterns and then wrap Day 3 with a debugging session where you'll learn to read tracebacks and fix errors systematically.

Everything connects: the comparisons you learned today will show up in every lab from here on out.

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
