# Day 4, Hour 2: Input Validation (Basics Approach)
**Python Programming Basics – Day 4 / Session 8 / Course Hour 30**

---

## Subtitle
**Helping beginner programs stay calm when users type something unexpected**

**Instructor framing:** This file is the standalone script for **Day 4, Hour 2**, aligned to **Course Hour 30** in the runbook. It builds directly on the menu-loop work from the previous hour and focuses on a Basics-friendly validation pattern: **check first, convert second**.

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & transition from Hour 29 menu loops: 5 minutes  
- Why input validation matters in beginner programs: 8 minutes  
- Using `.isdigit()` and `if` checks before conversion: 12 minutes  
- Re-prompt loops and validation functions: 10 minutes  
- Light preview of `try/except` for later study: 3 minutes  
- Live Demo – Safe whole-number input: 10 minutes  
- Hands-On Lab – Safe Number Entry: 7 minutes  
- Debrief & Exit Ticket: 5 minutes  

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain why input validation matters in user-facing programs
2. Use `.isdigit()` to check whether a string contains whole-number digits
3. Use `if` checks before calling `int()`
4. Re-prompt the user with a `while` loop when input is invalid
5. Build a simple reusable pattern for safe integer input
6. State one important limitation of `.isdigit()`
7. Preview, at a light level, that `try/except` exists for more advanced input handling later

---

## Section 1: Recap & Transition from Day 4, Hour 1 (5 minutes)

### Quick Review

**[Instructor speaks:]**

In **Day 4, Hour 1 / Course Hour 29**, students built menu loops. That was a big structural step. Their programs could stay open, show choices, route actions, and keep data in memory during one run.

Now we are going to improve the **robustness** of those programs.

If a user types something unexpected, what should happen?

For example:

- If we expect a whole number and the user types `hello`
- If we expect a menu number and the user types `9`
- If we expect a positive count and the user presses Enter without typing

Should the program crash?

Of course not. At least, we do not want it to if we can help it.

Today’s theme is one of the most practical habits beginners can learn:

> **Do not trust input automatically. Check it first.**

### Warm-Up Prompt

**[Instructor asks:]**

What is the problem with this line if the user types `cat`?

```python
age = int(input("Enter your age: "))
```

[Pause.]

**[Instructor speaks:]**

Exactly. `int("cat")` causes a `ValueError`. Students have already seen errors and tracebacks. Today we want to prevent some of those crashes by validating before converting.

### Transition Statement

**[Instructor speaks:]**

Hour 29 gave us the program structure. Hour 30 gives us better protection around user input so the structure does not fall apart when the user makes a common mistake.

---

## Section 2: Why Input Validation Matters (8 minutes)

### Programs Meet Real Users

**[Instructor speaks:]**

One of the fastest ways to make a beginner program feel frustrating is to let it crash on very ordinary user behavior.

Real users do things like:

- type letters when you expected numbers
- add spaces before or after input
- hit Enter too quickly
- misunderstand the prompt
- type negative numbers when you wanted positive numbers
- type decimals when you wanted whole numbers

A beginner sometimes thinks, “But the prompt clearly said enter a number.” That is not enough.

Good programming means anticipating that humans are human.

### Validation Is Part of Good User Experience

**[Instructor speaks:]**

Input validation is not just a technical detail. It is also a **user experience** decision.

Compare these two experiences.

**Poor experience:**
- User types `hello`
- Program crashes with a traceback

**Better experience:**
- User types `hello`
- Program says: “Invalid input. Please enter a whole number.”
- Program asks again

The second experience is calmer, clearer, and more respectful.

### A Beginner-Friendly Rule

**[Instructor speaks:]**

For this hour, I want students to remember a very simple rule:

> **Check first, convert second.**

That means:

1. get input as a string
2. inspect whether it looks valid
3. if valid, convert it
4. if invalid, show a message and ask again

This is the core pattern for today.

### Prediction Prompt

**[Instructor asks:]**

Why might it be safer to keep input as a string for a moment instead of converting immediately?

[Accept answers like “so we can inspect it first,” “so we can avoid crashing,” or “because input() always returns a string.”]

**[Instructor speaks:]**

Exactly. The string is the raw material. We do not convert it until it passes our simple check.

---

## Section 3: `.isdigit()` and Checking Before Conversion (12 minutes)

### What `.isdigit()` Does

**[Instructor speaks:]**

Python strings have a method called `.isdigit()`.

It returns:

- `True` if every character in the string is a digit
- `False` otherwise

Examples:

```python
print("123".isdigit())     # True
print("007".isdigit())     # True
print("12a".isdigit())     # False
print("".isdigit())        # False
print("12.5".isdigit())    # False
print("-3".isdigit())      # False
print(" 42 ".isdigit())    # False
```

### Important Teaching Note

**[Instructor speaks:]**

That last example matters. If a user types spaces around a number, `.isdigit()` will return `False` unless we strip the spaces first.

So the usual beginner pattern is:

```python
user_input = input("Enter a whole number: ").strip()
```

Then test:

```python
if user_input.isdigit():
    number = int(user_input)
```

### The Basic Safe Pattern

```python
user_input = input("Enter a whole number: ").strip()

if user_input.isdigit():
    number = int(user_input)
    print(f"You entered {number}")
else:
    print("Invalid input. Please enter digits only.")
```

### Why This Works

**[Instructor speaks:]**

Notice the order:

- first we gather input
- then we inspect it with `.isdigit()`
- only then do we call `int()`

That prevents the obvious crash on inputs like `hello`.

### Common Mistake #1: Converting Too Early

```python
number = int(input("Enter a whole number: ").strip())
if str(number).isdigit():
    print("Valid")
```

**[Instructor speaks:]**

This defeats the purpose. By the time you check `.isdigit()`, the conversion has already happened. If the input is bad, the program already crashed.

Validation has to happen **before** conversion.

### Common Mistake #2: Forgetting `.strip()`

**[Instructor speaks:]**

If the user enters ` 42 `, then without `.strip()` the string contains spaces.

```python
value = input("Enter a number: ")
print(value.isdigit())
```

This may return `False` even though the visible content looks numeric.

So encourage students to normalize the string first:

```python
value = input("Enter a number: ").strip()
```

### Common Mistake #3: Over-Trusting `.isdigit()`

**[Instructor speaks:]**

`.isdigit()` is useful, but it is limited.

It works well for:

- positive whole numbers like `7`, `42`, `1000`

It does **not** directly handle:

- negative integers like `-5`
- decimals like `3.14`
- numbers with commas like `1,000`

This is not a flaw in Python. It is simply the scope of the method.

For **this Basics hour**, that limitation is acceptable. We are intentionally teaching a simple, reliable beginner pattern.

### Prediction Prompt

**[Instructor asks:]**

What will this print?

```python
value = "-12"
print(value.isdigit())
```

[Pause.]

**[Instructor speaks:]**

It prints `False`, because the minus sign is not a digit.

That is today’s key limitation to remember.

---

## Section 4: Re-Prompting with a `while` Loop (10 minutes)

### Why One Check Is Not Enough

**[Instructor speaks:]**

If the user enters bad input, we usually do not want to give up immediately. We want to **ask again**.

That means validation and loops work beautifully together.

Here is the pattern:

```python
while True:
    user_input = input("Enter a whole number: ").strip()

    if user_input.isdigit():
        number = int(user_input)
        break
    else:
        print("Invalid input. Please enter digits only.")
```

### Explaining the Flow

**[Instructor speaks:]**

This loop says:

- keep asking forever
- if the input is valid, convert it and `break`
- otherwise, show an error and keep looping

That is a clean beginner-friendly structure.

### Turning the Pattern into a Small Function

**[Instructor speaks:]**

Because students will probably need this more than once, it is useful to show a small function pattern.

```python
def get_whole_number(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit():
            return int(user_input)

        print("Invalid input. Please enter a whole number.")
```

Then we can call it like this:

```python
age = get_whole_number("Enter your age: ")
quantity = get_whole_number("Enter quantity: ")
```

### Teaching Note on Functions Here

**[Instructor speaks:]**

This is a light use of functions in service of the lesson. The goal is not a full functions lesson. The goal is to show that repeated validation logic can be wrapped in one readable place.

If students are not yet comfortable with defining functions, it is perfectly fine to teach the loop inline first and show the function as a preview or helper.

### A Good Prompt Makes Validation Easier

**[Instructor speaks:]**

Prompts matter. Compare:

```python
input("Enter input: ")
```

versus:

```python
input("Enter a whole number between 1 and 10: ")
```

The second prompt tells the user what kind of answer is expected. That reduces confusion before validation even begins.

### Beyond Type Validation: Simple Rule Validation

**[Instructor speaks:]**

We can also validate simple rules after conversion.

Example:

```python
def get_menu_choice() -> int:
    while True:
        user_input = input("Choose 1, 2, or 3: ").strip()

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 3:
                return choice

        print("Invalid choice. Enter 1, 2, or 3.")
```

Now we are checking two things:

1. is it numeric?
2. is it in the allowed range?

That is exactly the kind of simple robustness beginners can handle.

---

## Section 5: Light Preview of `try/except` (3 minutes)

**[Instructor speaks:]**

I want to give a **very light preview** of something students will study more deeply later: `try/except`.

Sometimes Python programmers validate by attempting a conversion and catching the error if it fails.

For example, later in the course we may write patterns like this:

```python
try:
    number = int(user_input)
except ValueError:
    print("Please enter a valid integer.")
```

But for **today**, we are **not** teaching exception handling deeply. We are using the Basics-friendly rule:

> **Use `.isdigit()` and `if` checks before conversion.**

That keeps the mental model simple.

### Important Boundary for This Hour

**[Instructor speaks:]**

If students ask, “Should I use `try/except` here?” the answer is:

- It exists
- It is useful
- We will cover it more fully later
- For this hour, stay with the simpler guard-based approach

That keeps the lesson aligned with the runbook and prevents accidental topic drift.

---

## Section 6: Live Demo – Safe Whole-Number Input Function (10 minutes)

### Demo Goal

**[Instructor speaks:]**

Now I will live-code a small program that safely asks for two whole numbers and then uses them in a calculator.

The demo will model three good habits:

1. validate before converting
2. re-prompt on bad input
3. use the validated values in a real task

### Live Coding Script

```python
# safe_number_demo.py
# Day 4, Hour 2 demo: validation with while + isdigit()

def get_whole_number(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit():
            return int(user_input)

        print("Invalid input. Please enter a whole number using digits only.")


print("=== Safe Number Calculator ===")

first_number = get_whole_number("Enter the first whole number: ")
second_number = get_whole_number("Enter the second whole number: ")

print("\nResults:")
print(f"Addition: {first_number} + {second_number} = {first_number + second_number}")
print(f"Multiplication: {first_number} * {second_number} = {first_number * second_number}")
print(f"Larger value: {max(first_number, second_number)}")
```

### Live Narration Points

**[Instructor speaks:]**

As I type, I want to say things like:

- “I am keeping input as a string first.”
- “I call `.strip()` so accidental spaces do not break validation.”
- “Only after `.isdigit()` returns `True` do I use `int()`.”
- “If the input is bad, I do not crash. I explain and ask again.”

### Suggested Demo Inputs

Test these live:

1. `12` and `7` — valid path  
2. `cat` then `12` — invalid then recovery  
3. `3.5` then `8` — decimal rejected  
4. `-4` then `4` — negative rejected in this version  

### Teaching the Limitation Explicitly

**[Instructor speaks:]**

If a student says, “But `-4` is a real integer,” agree with them. Then explain:

“Yes, mathematically it is. But our current validation rule uses `.isdigit()`, which is a limited but useful beginner tool. Today we are intentionally keeping the pattern simple.”

That keeps the lesson accurate and honest.

---

## Section 7: Hands-On Lab – Safe Number Entry (7 minutes setup + remainder of work time)

### Lab Prompt

**Lab: Safe Number Entry**

Create a program that safely asks the user for a whole number. If the user types invalid input, the program must show an error message and ask again until a valid whole number is entered.

Then use the validated number in a small calculator-style result.

### Required Features

Your program must:

- ask for at least one whole number
- reject non-numeric input without crashing
- re-prompt until the user enters valid digits
- convert the input to an integer only after validation
- use the validated number in a small calculation

### Suggested Versions

Students can choose one of these mini calculators:

1. **Double and square**
   - print the number doubled and squared
2. **Age helper**
   - ask for age in years and print months lived (rough estimate)
3. **Simple add-two-numbers tool**
   - safely ask for two numbers and add them

### Starter Template

```python
def get_whole_number(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit():
            return int(user_input)

        print("Invalid input. Please enter a whole number.")


number = get_whole_number("Enter a whole number: ")

print(f"You entered: {number}")
print(f"Double: {number * 2}")
print(f"Square: {number ** 2}")
```

### Completion Criteria

A student solution is complete when:

- ✅ the program never crashes on non-numeric input  
- ✅ invalid input triggers an error message and re-prompt  
- ✅ valid numbers are accepted and converted correctly  
- ✅ the validated number is used in a small calculator result  

### Common Pitfalls to Watch For

1. **Using `.isdigit()` after `int()`**  
   Validation must happen first.

2. **Forgetting `.strip()`**  
   Inputs with spaces may fail unexpectedly.

3. **Thinking `.isdigit()` handles negatives or decimals**  
   It does not in this version.

4. **Breaking out of the loop too early**  
   Some students accidentally `break` before the valid conversion.

5. **Returning a string instead of an integer**  
   Make sure the function returns `int(user_input)`.

### Optional Extension

If students finish early, invite them to handle negative whole numbers with a small extension:

```python
if user_input.startswith("-"):
    check_text = user_input[1:]
else:
    check_text = user_input
```

Then validate `check_text.isdigit()`.

Frame this as optional only. The core lesson remains the positive-whole-number pattern.

### Coaching Prompts While Circulating

**[Instructor speaks:]**

Use prompts like:

- “Where does validation happen?”
- “When exactly do you convert to `int`?”
- “What happens if I type `hello`?”
- “What happens if I type `3.14`?”
- “Does your program recover, or does it stop?”

---

## Section 8: Debrief & Exit Ticket (5 minutes)

### Debrief Questions

**[Instructor asks:]**

- What is the benefit of checking with `.isdigit()` before using `int()`?
- Why is re-prompting better than crashing?
- What kinds of input does `.isdigit()` handle well?
- What kinds of input does it not handle well?

### Instructor Synthesis

**[Instructor speaks:]**

Today’s goal was not to solve every validation problem in Python. It was to build a clean, basic habit students can actually use right away.

That habit is:

- gather input
- normalize it
- validate it
- convert it
- keep going if it is invalid

That is an excellent beginner workflow.

### Exit Ticket

**[Instructor asks:]**

Answer this in one sentence:

**What is one limitation of `.isdigit()`?**

**Expected answer:** It does not directly handle negative numbers or decimals.

---

## Recap: What We Accomplished in Day 4, Hour 2 / Course Hour 30

In this hour, learners:

- used `.isdigit()` to check whole-number strings
- applied `if` checks before conversion
- built re-prompt loops with `while`
- created a reusable safe-input pattern
- previewed, lightly, that `try/except` exists for later
- discussed the limits of simple validation

**[Instructor speaks:]**

This hour matters because many beginner bugs come from assuming input will be perfect. Students now have a pattern for writing programs that are more patient and more durable.

In **Day 4, Hour 3 / Course Hour 31**, they will use loops, data structures, menus, and friendly messages together in a larger mini-project: a **CLI Contact Manager**.

---

## Appendix A: Full Demo Solution

```python
# safe_number_demo.py
# Day 4, Hour 2 demo solution

def get_whole_number(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit():
            return int(user_input)

        print("Invalid input. Please enter a whole number using digits only.")


print("=== Safe Number Calculator ===")

first_number = get_whole_number("Enter the first whole number: ")
second_number = get_whole_number("Enter the second whole number: ")

print("\nResults:")
print(f"Addition: {first_number} + {second_number} = {first_number + second_number}")
print(f"Subtraction: {first_number} - {second_number} = {first_number - second_number}")
print(f"Multiplication: {first_number} * {second_number} = {first_number * second_number}")
```

---

## Appendix B: Instructor Notes on Scope and Accuracy

### What We Are Teaching Today

- positive whole-number validation
- `.isdigit()` as a simple guard
- `while` loops for re-prompting
- conversion only after validation

### What We Are Not Teaching Deeply Today

- decimal parsing
- full negative-number support as required content
- exception handling as the main validation strategy
- advanced parsing rules

### Why This Matters

Keeping the scope tight helps beginners succeed. It is better for a learner to confidently master one reliable validation pattern than to vaguely hear about six patterns and retain none of them.

---

## Appendix C: Common Student Misconceptions

### Misconception: “If I type a number with spaces, `.isdigit()` should still work.”
**Clarification:** Not unless the string is stripped first.  
**Response:** “Let’s inspect the raw string and then apply `.strip()`.”

### Misconception: “If `.isdigit()` returns `False`, the input is not a number in any sense.”
**Clarification:** It only means the string is not made entirely of digit characters.  
**Response:** “`-5` and `3.14` are numeric ideas, but they do not pass this specific check.”

### Misconception: “Validation is optional if the prompt is clear.”
**Clarification:** Clear prompts help, but users still make mistakes.  
**Response:** “Validation protects both the program and the user experience.”

### Misconception: “The error message is enough; I don’t need to re-prompt.”
**Clarification:** In an interactive program, recovery is usually better than failure.  
**Response:** “Try to help the user succeed on the next input attempt.”

---

## Appendix D: Sample Board Work / Visual Explanation

### Validation Flow

```text
input() -> string
      ↓
normalize with .strip()
      ↓
check with .isdigit()
      ↓
valid? yes -> int()
valid? no  -> error message + ask again
```

### Re-Prompt Pattern

```text
while True:
    ask
    if valid:
        return / break
    else:
        explain and repeat
```

### Key Phrase to Repeat

```text
Check first.
Convert second.
```

---

## Appendix E: Extension Example for Negative Whole Numbers

**Optional instructor-only stretch example:**

```python
def get_integer_allow_negative(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()

        if user_input.startswith("-"):
            check_text = user_input[1:]
        else:
            check_text = user_input

        if check_text.isdigit() and check_text != "":
            return int(user_input)

        print("Invalid input. Please enter a whole number.")
```

Use this only if students are ready and time allows. Keep the main lesson centered on the required Basics approach.

---

## Appendix F: Additional Instructor Coaching Moves

### When students keep crashing their program

**[Instructor speaks:]**

Do not immediately fix it for them. Ask them to point to the exact line where conversion happens. Then ask:

- “What type is the data before this line?”
- “What could happen if the user typed text instead of digits?”
- “Where should the check happen?”

This helps them reconstruct the rule themselves.

### When students want to jump to advanced solutions

Some learners may say, “I saw `try/except` online.” Respond warmly but steer them back:

- “Yes, that pattern is real.”
- “We will study it more deeply later.”
- “For this hour, I want you to master the simpler guard-based approach first.”

That keeps the lesson coherent and aligned with the current course stage.

### When students are frustrated by `.isdigit()` limitations

Use that frustration productively. Say:

“Good. You are noticing that real input is messy. That means you are thinking like a programmer. Today we use a simple tool with known limits. Later we will learn stronger tools.”

That turns a limitation into a growth point rather than a disappointment.

---

## Appendix G: Quick Reference Card for Students

### Safe Whole Number Pattern

```python
while True:
    user_input = input("Enter a whole number: ").strip()

    if user_input.isdigit():
        number = int(user_input)
        break

    print("Invalid input. Please try again.")
```

### Remember

- `input()` returns a string
- validate before converting
- `.strip()` helps remove spaces
- `.isdigit()` works for positive whole numbers
- `.isdigit()` does not directly handle negatives or decimals
- re-prompting is better than crashing

---

## Appendix H: Guided Practice Script for the Instructor

Use this appendix when you want more spoken guidance before sending students into independent work.

### Guided Example 1: Validate Before Converting

**[Instructor speaks:]**

Let’s say I want to ask for a class size. I know `input()` gives me a string. So I should not rush into `int()` unless I have first checked whether the string looks safe for this lesson’s rules.

I might say to students:

> “Watch the order carefully. First I collect the text. Then I ask whether the text is made of digits. Only then do I convert it.”

Code:

```python
class_size_text = input("Enter class size: ").strip()

if class_size_text.isdigit():
    class_size = int(class_size_text)
    print(f"Class size recorded: {class_size}")
else:
    print("Please enter digits only.")
```

### Guided Example 2: Range Validation After Type Validation

**[Instructor speaks:]**

Sometimes a value is numeric but still not acceptable for the specific situation.

For example, if I ask the user to choose a menu option from 1 to 4, the value `9` is a number, but it is still not a valid choice.

That means validation often has **layers**:

1. Is it the right kind of input?
2. Is it within the allowed rule?

Code:

```python
choice_text = input("Enter a menu number from 1 to 4: ").strip()

if choice_text.isdigit():
    choice = int(choice_text)

    if 1 <= choice <= 4:
        print(f"Valid choice: {choice}")
    else:
        print("That number is outside the allowed range.")
else:
    print("Please enter digits only.")
```

### Guided Example 3: Why Re-Prompting Feels Better

**[Instructor speaks:]**

I like to ask students to imagine two versions of the same calculator:

- version A crashes the first time the user types bad input
- version B says “Please enter a whole number” and asks again

Then I ask:

**[Instructor asks:]**

Which version would you rather use? Which version would you rather show to someone else?

This question helps students understand that validation is not just about avoiding embarrassment. It is part of writing software that respects the user.

### Suggested Call-and-Response Moments

Use these quick prompts during teaching:

- “What type does `input()` return?” → **Expected:** string
- “Do we convert first or check first?” → **Expected:** check first
- “What does `.isdigit()` handle well?” → **Expected:** positive whole numbers
- “What is one thing `.isdigit()` does not handle?” → **Expected:** negatives or decimals
- “If input is invalid, what should our program do?” → **Expected:** explain and ask again

---

## Appendix I: Troubleshooting Scenarios for Live Support

### Scenario 1: Student keeps getting `False` for a value that looks numeric

Possible cause:
- extra spaces before or after the value

Helpful coaching:

**[Instructor speaks:]**

“Let’s print the raw input with markers around it so we can see hidden spaces.”

Example:

```python
user_input = input("Enter a number: ")
print(f"RAW -> [{user_input}]")
print(user_input.isdigit())
```

Then show how `.strip()` changes the result.

### Scenario 2: Student validates correctly but still returns a string

Possible cause:
- they forgot to convert after validation

Helpful coaching:

**[Instructor speaks:]**

“Your check is good, but what type are you returning? Can you print `type(number)` after that line?”

This moves the student from vague frustration to a concrete observation.

### Scenario 3: Student accepts input once but does not re-prompt

Possible cause:
- validation is written with `if/else` but without a loop

Helpful coaching:

**[Instructor speaks:]**

“Right now your program can reject input, but can it recover? What structure do we use when we want to keep asking until a condition is satisfied?”

Expected student insight: use a `while` loop.

### Scenario 4: Student wants to support every possible number format

Possible cause:
- they are expanding beyond the lesson scope

Helpful coaching:

**[Instructor speaks:]**

“That is a thoughtful goal, but for this hour we are mastering one clean pattern first. Let’s make positive whole numbers solid before we broaden the problem.”

This preserves ambition without letting scope overwhelm the learner.

---

## Appendix J: Extra Practice Prompts for Fast Finishers

If time remains, offer one of these short prompts without changing the core lesson focus.

### Practice Prompt 1: Safe Dice Counter

Ask the user how many dice to roll. The input must be a whole number. After validation, print a message like:

```text
You chose to roll 6 dice.
```

Optional extension: reject `0` as well.

### Practice Prompt 2: Safe Ticket Calculator

Ask for a number of tickets. Re-prompt until the user enters a whole number. Then print the total cost if each ticket is $12.

### Practice Prompt 3: Safe Team Size Checker

Ask how many people are on a team. Re-prompt until valid. Then print:

- whether the team is smaller than 5
- exactly 5
- larger than 5

This gives extra practice combining validation with conditionals.

### Practice Prompt 4: Menu Number Validator

Ask for a menu number from 1 to 3 and re-prompt until the user enters a valid option. This directly connects Hour 30 back to Hour 29.

---

**End of Day 4, Hour 2 Script / Course Hour 30**
