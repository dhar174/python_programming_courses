# Day 4, Hour 2: Boolean Expressions, Comparison Operators, and Logical Operators

**Course Hour**: 14  
**Session**: Day 4 (Session 4), Hour 2  
**Duration**: 60 minutes  

---

## 1. Learning Outcomes

After this instructional hour, learners will be able to:

- **Use comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) to compare values and understand the distinction between assignment (`=`) and equality (`==`).
- **Understand boolean values and truthiness** in Python, recognizing that comparisons evaluate to `True` or `False` and that these are first-class Python objects.
- **Combine conditions with logical operators** (`and`, `or`, `not`) to create complex boolean expressions and understand operator precedence and short-circuit evaluation.
- **Apply boundaries and edge cases correctly** in real-world conditionals, avoiding off-by-one errors and invalid type comparisons.
- **Trace and predict boolean expressions** in code, reading compound conditions aloud to build mental models of control flow.

---

## 2. Instructor Prep Section

### Pre-Class Checklist
- [ ] Have Python 3 ready in your IDE/terminal for live demo
- [ ] Test all demo code snippets before class (run them yourself)
- [ ] Prepare a simple text document with the "common pitfalls" examples to paste quickly
- [ ] Have the eligibility checker lab rubric visible (shared or printed)
- [ ] Test the breakout or hands-on lab delivery method (screen share, local IDE, online repl, etc.)
- [ ] Prepare a "prediction slide" or notebook with 3–4 mystery boolean expressions for learners to predict

### Timing Breakdown
- **Opening Script** (5 min)
- **Conceptual Briefing: Comparisons** (8 min)
- **Conceptual Briefing: Boolean Logic** (8 min)
- **Live Demo: Comparisons + and/or** (10 min)
- **Guided Practice Walkthrough** (7 min)
- **Lab Checkpoint 1: Eligibility Checker** (20 min)
- **Wrap-Up + Quick-Check Questions** (4 min)

### Materials & Resources
- IDE or Python REPL (online or local)
- Sample code: age-gating example, membership check, nested conditions
- Eligibility checker lab prompt (provided below)
- Optional: truth table or Venn diagram (visual aids help retention)

---

## 3. Opening Script

**[Read or paraphrase the following to open, ~5 minutes]**

"Good morning. In the last few sessions, we've learned how to store data in variables, work with strings and numbers, and even get input from users. But here's the question: *what do we do when we need the program to make a decision?*

Think about this: if you were writing a program for a movie theater, you'd need to ask, 'Is the customer 18 or older?' or 'Do they have a membership?' In the real world, we make decisions all the time based on conditions. Today, we're going to learn how Python makes decisions using **boolean values** and **comparisons**.

By the end of this hour, you'll be able to write code that answers questions like:
- 'Is this age valid?'
- 'Do all these conditions need to be true?'
- 'Is at least one of these true?'

Let's start simple and build up. Ready?"

---

## 4. Conceptual Briefing

### Part A: Understanding Comparison Operators (8 minutes)

**The Core Idea**

A **comparison operator** takes two values and asks a question: 'How do these relate?' The answer is always either `True` or `False`. Think of it like a yes/no question.

```python
# Asking questions with comparisons:
5 > 3         # Is 5 greater than 3? Answer: True
5 == 3        # Is 5 equal to 3? Answer: False
5 != 3        # Is 5 not equal to 3? Answer: True
```

**The Six Main Comparison Operators**

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Is equal to? | `5 == 5` | `True` |
| `!=` | Is NOT equal to? | `5 != 3` | `True` |
| `<` | Is less than? | `3 < 5` | `True` |
| `>` | Is greater than? | `5 > 3` | `True` |
| `<=` | Is less than or equal? | `5 <= 5` | `True` |
| `>=` | Is greater than or equal? | `5 >= 3` | `True` |

**The Critical Distinction: `=` vs. `==`**

This is THE most common mistake learners make:
- `=` is **assignment**: it *puts* a value into a variable. Example: `age = 18`
- `==` is **comparison**: it *asks* if two values are equal. Example: `age == 18`

```python
age = 18        # Put 18 into the age variable
age == 18       # Ask: is age equal to 18? (Yes, True)
age == 21       # Ask: is age equal to 21? (No, False)
```

If you use `=` when you meant `==`, Python will try to assign instead of compare, and you'll get a syntax error or unexpected behavior.

**Comparisons with Different Types**

Comparisons work within the same type:
```python
5 > 3           # Both numbers: True
"apple" == "apple"  # Both strings: True
```

But comparing across types is often meaningless or wrong:
```python
5 > "3"         # Error: can't compare int to str
```

Always convert to the same type first:
```python
5 > int("3")    # Convert string to int: True
```

### Part B: Boolean Logic—Combining Conditions (8 minutes)

**The Motivation**

One condition is fine, but real decisions often require multiple criteria:
- 'Is the customer 18 AND do they have a membership?'
- 'Is the item small OR lightweight?'
- 'Is the request NOT from a blocked IP?'

That's where **logical operators** come in: `and`, `or`, and `not`.

**The `and` Operator**

`and` means *both* conditions must be `True`.

```python
age >= 18 and has_license       # Both must be True
age >= 18 and age <= 65         # 18 <= age <= 65
```

Truth table for `and`:
| A | B | A and B |
|---|---|---------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Only the top row is True**: both must be true.

**The `or` Operator**

`or` means *at least one* condition must be `True`.

```python
is_weekend or is_holiday        # At least one must be True
age < 13 or age > 65            # Outside the middle range
```

Truth table for `or`:
| A | B | A or B |
|---|---|--------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

**Only the bottom row is False**: both must be false for the result to be false.

**The `not` Operator**

`not` flips a boolean value. `True` becomes `False` and vice versa.

```python
is_adult = True
not is_adult                    # False
```

**Combining All Three**

You can build complex expressions:
```python
# Eligibility rule: 
# Adult (18+) AND (has_membership OR pays_fee)
age >= 18 and (has_membership or pays_fee)
```

**Short-Circuit Evaluation (Optional Insight)**

Python is smart: it stops evaluating as soon as it knows the answer.
```python
# If age < 18, Python doesn't even check the second part
age >= 18 and has_license       # If first is False, result is False—stop!
```

This is a performance detail, but it's also useful to know: if the first check fails, the second might not run.

---

## 5. Live Demo: Comparisons and Logical Operators (10 minutes)

**Set Up the Scenario**: "Let's build an age-gating system for an online service. We need to check:
1. Is the user at least 18?
2. Does the user have either a membership or have paid a fee?

Let's code this live."

### Demo Code Part 1: Basic Comparisons

```python
# Simple age check
age = 16
print(f"Age: {age}")
print(f"Age >= 18? {age >= 18}")        # False

age = 18
print(f"Age: {age}")
print(f"Age >= 18? {age >= 18}")        # True

age = 25
print(f"Age: {age}")
print(f"Age >= 18? {age >= 18}")        # True
```

**Narration**: "Notice that the comparison returns `True` or `False`. We can print it directly. As we change age, the result changes."

### Demo Code Part 2: Combining with `and`

```python
# Adult AND has license
age = 25
has_license = True

print(f"Age {age}, License: {has_license}")
print(f"Eligibile? {age >= 18 and has_license}")  # True

has_license = False
print(f"Age {age}, License: {has_license}")
print(f"Eligible? {age >= 18 and has_license}")   # False
```

**Narration**: "When I turn off the license, the result flips to `False` even though age is still 25. Both conditions must be `True`."

### Demo Code Part 3: Combining with `or`

```python
# Has membership OR paid fee
has_membership = False
paid_fee = True

print(f"Membership: {has_membership}, Paid: {paid_fee}")
print(f"Can proceed? {has_membership or paid_fee}")  # True

has_membership = False
paid_fee = False
print(f"Membership: {has_membership}, Paid: {paid_fee}")
print(f"Can proceed? {has_membership or paid_fee}")  # False
```

**Narration**: "With `or`, as long as ONE is `True`, the result is `True`. Only when both are `False` does the result become `False`."

### Demo Code Part 4: Complete Eligibility Check

```python
# Full eligibility: adult AND (has membership OR paid)
age = 20
has_membership = False
paid_fee = True

eligible = age >= 18 and (has_membership or paid_fee)
print(f"Eligible: {eligible}")  # True

# What if they're not an adult?
age = 16
eligible = age >= 18 and (has_membership or paid_fee)
print(f"Eligible: {eligible}")  # False (age fails the check)
```

**Narration**: "Notice the parentheses around `has_membership or paid_fee`. They group that part so it's evaluated first. Without them, Python would read it differently."

### Quick Prediction Moment

Ask the learners:
"What will this print?"
```python
age = 30
has_membership = True
result = age >= 18 and not has_membership
print(result)
```

Give them 10 seconds to think, then reveal: `False` (because `not has_membership` is `False`).

---

## 6. Practice Walkthrough: Guided Practice (7 minutes)

**The Scenario**: "You're building a discount checker for an online store. The rule is:
- Customers 65+ get a senior discount.
- Customers under 13 get a kid discount.
- Everyone else pays full price.

Let's code this together, step by step."

### Step 1: Set Up Variables

```python
age = 70
is_senior = age >= 65
print(f"Is senior? {is_senior}")  # True
```

**Instructor Talk**: "We create a variable `is_senior` by comparing age to 65. Notice: we use `>=`, not `>`, to include 65 itself."

### Step 2: Add the Kid Check

```python
age = 70
is_senior = age >= 65
is_kid = age < 13
print(f"Is senior? {is_senior}")  # True
print(f"Is kid? {is_kid}")        # False
```

**Instructor Talk**: "We add another variable for the kid check. Now we have two boolean values."

### Step 3: Determine the Discount

```python
age = 70
is_senior = age >= 65
is_kid = age < 13

if is_senior:
    discount_percent = 15
elif is_kid:
    discount_percent = 10
else:
    discount_percent = 0

print(f"Age {age} gets {discount_percent}% discount")  # 15
```

**Instructor Talk**: "Now we USE these booleans to make decisions. We're peeking at `if/elif/else`, which we'll dive into next hour. But notice: the conditions are the comparisons we just learned."

### Step 4: Test with Different Ages

```python
def check_discount(age):
    is_senior = age >= 65
    is_kid = age < 13
    
    if is_senior:
        discount_percent = 15
    elif is_kid:
        discount_percent = 10
    else:
        discount_percent = 0
    
    return discount_percent

print(f"Age 70: {check_discount(70)}%")  # 15
print(f"Age 10: {check_discount(10)}%")  # 10
print(f"Age 40: {check_discount(40)}%")  # 0
```

**Instructor Talk**: "We wrap it in a function so we can test multiple ages. Notice how the boolean comparisons (`age >= 65`, `age < 13`) drive the logic."

---

## 7. Lab with Checkpoints: Eligibility Checker

**Lab Duration**: 20 minutes  
**Objective**: Apply comparisons and logical operators to solve a real-world problem.

### Lab Prompt

You're building an eligibility checker for a summer camp. Write a program that asks for:
1. The participant's age
2. Whether they have completed a swimming test (yes/no or True/False)
3. Whether they have a parent/guardian contact on file (yes/no or True/False)

Based on these inputs, determine if the participant is **eligible** using these rules:

- **Eligible if**: age is between 8 and 16 (inclusive) AND swimming test is passed AND parental contact is on file.
- **Not eligible if** any condition fails.

Print a clear message: either "Eligible for camp" or "Not eligible: [reason]"

### Checkpoint 1: Correct Comparisons (5 minutes)

**Your code should have**:
- Three input prompts (age, swimming_test, parent_contact)
- Correct type conversion (age must be an integer)
- At least two comparisons (e.g., `age >= 8`, `age <= 16`)
- One use of `and` to combine conditions

**Test case 1**: age=12, swimming_test=True, parent_contact=True → "Eligible"  
**Test case 2**: age=12, swimming_test=False, parent_contact=True → "Not eligible"  
**Test case 3**: age=7, swimming_test=True, parent_contact=True → "Not eligible"

### Checkpoint 2: Compound Expression (10 minutes)

**Build the eligibility expression**:
```python
eligible = (age >= 8 and age <= 16) and swimming_test and parent_contact
```

Or use Python's chaining syntax:
```python
eligible = 8 <= age <= 16 and swimming_test and parent_contact
```

Print the result clearly:
```python
if eligible:
    print("Eligible for camp!")
else:
    print("Not eligible. Please check your information.")
```

### Checkpoint 3: Test Edge Cases (5 minutes)

Test boundary values:
- Age 8 (boundary): should be eligible (with other conditions true)
- Age 16 (boundary): should be eligible (with other conditions true)
- Age 7 (just below): should not be eligible
- Age 17 (just above): should not be eligible

---

## 8. Troubleshooting Pitfalls

### Pitfall 1: Confusing `=` and `==`

**The Mistake**:
```python
if age = 18:    # SYNTAX ERROR: can't assign in condition
    print("Adult")
```

**Why It Breaks**: Python sees `=` and tries to *assign* 18 to `age`, not *compare*. This causes a syntax error.

**The Fix**:
```python
if age == 18:   # Correct: compare age to 18
    print("Adult")
```

**How to Remember**: "Single `=` puts a value in. Double `==` asks a question."

---

### Pitfall 2: Off-by-One Errors with Boundaries

**The Mistake**:
```python
age = 18
if age > 18:        # Wrong: excludes exactly 18
    print("Adult")
```

**Why It Breaks**: The rule is "18 or older," but `>` means "strictly greater than," so 18 fails.

**The Fix**:
```python
age = 18
if age >= 18:       # Correct: includes 18
    print("Adult")
```

**How to Test**: Always test the boundary value itself. Is 18 supposed to be included? If yes, use `>=`, not `>`.

---

### Pitfall 3: Comparing Strings to Numbers

**The Mistake**:
```python
age = "18"
if age > 18:        # TypeError: can't compare str to int
    print("Adult")
```

**Why It Breaks**: Python doesn't know how to compare a string `"18"` to a number `18`. They're different types.

**The Fix**:
```python
age = int(input("Your age: "))  # Convert to int first
if age > 18:                     # Now both are integers
    print("Adult")
```

**How to Remember**: Always convert `input()` to the type you're comparing. Use `int()`, `float()`, or `.lower()` for strings.

---

### Pitfall 4: Misunderstanding `and` vs. `or`

**The Mistake**:
```python
# Trying to express: age is between 8 and 16
if age > 8 or age < 16:     # WRONG: almost all ages satisfy this!
    print("In range")
```

**Why It Breaks**: `or` means "at least one must be true." Age 20 is NOT > 8? Well, 20 < 16? No. But 20 > 8 is TRUE, so the whole thing is TRUE.

**The Fix**:
```python
# CORRECT: both conditions must be true
if age >= 8 and age <= 16:
    print("In range")
```

**How to Remember**: Use `and` when you need *both* conditions. Use `or` when *either* works.

---

### Pitfall 5: Forgetting Parentheses in Complex Expressions

**The Mistake**:
```python
# Intending: age is 18+ AND (has membership OR paid fee)
# But without parentheses:
if age >= 18 and has_membership or paid_fee:
    # This reads as: (age >= 18 and has_membership) OR paid_fee
    # If paid_fee is True, the whole thing is True, even if age < 18!
    print("Proceed")
```

**Why It Breaks**: Without parentheses, Python follows operator precedence: `and` is evaluated before `or`. So the logic is wrong.

**The Fix**:
```python
if age >= 18 and (has_membership or paid_fee):
    print("Proceed")
```

**How to Remember**: When in doubt, use parentheses. They cost nothing and make your intent clear.

---

## 9. Quick-Check Questions

**These questions are designed to check understanding quickly. Ask them in rapid succession (2–3 min total). Encourage verbal responses.**

1. **"What's the difference between `=` and `==`? Give me one sentence."**  
   *(Expected: `=` is assignment; `==` is comparison.)*

2. **"I write `5 > 3`. What does Python return?"**  
   *(Expected: `True`.)*

3. **"True or False: `and` means at least one condition must be true."**  
   *(Expected: False. `and` means BOTH must be true; `or` means at least one.)*

4. **"If I write `age = 18 and has_license`, what happens?"**  
   *(Expected: Python compares age to 18, then checks has_license, and returns a boolean.)*

5. **"What does `not True` return?"**  
   *(Expected: `False`.)*

---

## 10. Wrap-Up (4 minutes)

### Key Takeaways

Today, we learned the foundations of decision-making in Python:

1. **Comparisons** (`==`, `!=`, `<`, `>`, `<=`, `>=`) let us ask yes/no questions about values. The result is always `True` or `False`.
2. **Remember**: `=` is assignment (puts a value in), `==` is comparison (asks if they're equal).
3. **Logical operators** (`and`, `or`, `not`) let us combine conditions:
   - `and`: ALL conditions must be true.
   - `or`: AT LEAST ONE condition must be true.
   - `not`: Flips true to false, false to true.
4. **Boundaries matter**: Use `>=` and `<=` to include the edge value.
5. **Types must match**: Convert inputs to the right type before comparing.

### Looking Ahead

Next hour, we'll take these boolean expressions and use them in **if/elif/else statements**. That's when your programs will truly start making decisions and running different code paths. Today is the vocabulary; next hour is the grammar.

### Final Thought

Boolean logic might feel abstract right now, but it's everywhere:
- "Is the user logged in?"
- "Is the account balance sufficient?"
- "Is the email valid?"
- "Is today a holiday?"

Every "yes or no" question in software comes down to comparisons and boolean logic. You've just learned the fundamental tool.

---

## 11. Facilitation Notes

### Pacing & Flexibility

- **If learners are quick**: Dive deeper into truth tables, short-circuit evaluation, or ask them to predict complex expressions.
- **If learners are struggling**: Spend more time on the `and`/`or` distinction. Use a Venn diagram or physical props (e.g., "stand if you're an adult AND have a license").
- **If time is tight**: Skip the guided practice walkthrough and move directly to the lab.

### Engagement Tips

1. **Prediction moment**: Before running code, ask, "What will this print?" Learners engage better when they predict first.
2. **Real-world framing**: Always connect to reality. "Imagine you're the programmer for an airline checking if a passenger can board..."
3. **Common mistake emphasis**: Spend extra time on `=` vs. `==`. Ask learners to write both on a piece of paper and explain the difference.
4. **Breakout practice**: If possible, pair learners and have them verbally talk through a boolean expression before coding it.

### Troubleshooting On the Fly

- **"My condition isn't working."** → First, ask them to print the boolean result in isolation. Is it what they expected? If not, debug the comparison.
- **"I got an error."** → Read the error message together. Is it a type error? A syntax error? Guide, don't fix.
- **"Can I use `and` and `or` together?"** → Yes, with parentheses to clarify your intent.

### Assessment During Lab

Circulate and ask:
- "Walk me through your eligibility condition."
- "Why did you choose `and` here instead of `or`?"
- "What happens if age is exactly 8?"

These questions reveal misunderstandings before the checkpoint.

---

## 12. Assessment Rubric

### Eligibility Checker Lab Rubric (20 points total)

| Criterion | Points | Evidence |
|-----------|--------|----------|
| **Correct Input Handling** | 4 | Program prompts for age, swimming_test, parent_contact. Age is converted to integer. |
| **Correct Age Comparisons** | 4 | Uses `age >= 8` and `age <= 16` (or chained `8 <= age <= 16`). Boundaries are correct. |
| **Correct Use of `and`** | 4 | Combines all three conditions with `and`. Expression is logically sound. |
| **Clear Output** | 4 | Prints "Eligible for camp" or "Not eligible" message. Message is clear and readable. |
| **Testing & Edge Cases** | 2 | Program is tested on at least two different inputs. Boundary values (age 8, age 16) work correctly. |
| **Code Quality** | 2 | Readable variable names, reasonable comments, code is not overly complex. |

### Grading Scale
- **18–20 points**: Excellent. All logic correct, clear output, tested thoroughly.
- **15–17 points**: Good. Logic mostly correct, minor issues with boundaries or output clarity.
- **12–14 points**: Satisfactory. Core logic works but has edge-case issues or unclear output.
- **Below 12**: Needs rework. Logic errors or missing components.

### Feedback Template

**For Excellent Work**:
"Your eligibility logic is rock-solid! You correctly used `and` to combine all three conditions, and your boundary checking is spot-on. Well done!"

**For Good Work**:
"Your logic is sound. I noticed a small issue with [boundary/output]. Let's talk about when to use `>=` vs. `>`. You're on the right track!"

**For Needs Rework**:
"Your code is close. The issue is [specific problem]. Let's trace through what happens when age is exactly 8. Walk me through it step by step."

---

**End of Hour 2 Lecture Script**

---

*Word count: 3,200+ words*
