# Day 7, Hour 2: while Loops + Sentinel Patterns (Course Hour 26)
**Python Programming Basics – Session 7**

**Course:** Python Programming (Basics)
**Runbook alignment:** Session 7, Course Hour 26 – while loops + sentinel patterns
**Duration:** 60 minutes
**Mode:** Instructor-led + live coding + guided lab
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. Keep the hour tightly focused on while loops: what they are, how they repeat until a condition becomes False, how to avoid infinite loops, and how to use break and continue for early exits. The sentinel pattern (using a special value like 'q' to signal stopping) is the core application. Stay within Basics scope — do not introduce do-while patterns (Python does not have them), complex state machines, or event-driven loops. The key outcomes are writing while loops with proper termination conditions, using break/continue appropriately, and building a password prompt with attempt limiting. The lab reinforces all of this in a retry-until-success authentication flow.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Write a while loop that repeats code until a condition becomes False.
2. Explain the difference between a while loop and a for loop (which we will cover in Hour 3).
3. Use the break statement to exit a loop early when a goal is achieved.
4. Use the continue statement to skip the rest of the current iteration and start the next one.
5. Implement a sentinel pattern: keep prompting the user until they enter a special value like 'q' to quit.
6. Build a password prompt that allows up to 3 attempts and locks out after failures."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Hour 1 conditionals; introduce the need for repetition
- **0:05–0:18** Core concept: while loops, loop condition, infinite loops, updating state
- **0:18–0:28** break and continue: early exits and skipping iterations
- **0:28–0:35** Sentinel patterns: special values that signal stopping
- **0:35–0:45** Live demo: password prompt with attempt counter
- **0:45–0:57** Guided lab: Password Prompt with retry limit
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour26_while_demo.py` before class begins.
- Have a second file called `hour26_lab_password.py` ready with empty comments as a starter for learners who fall behind.
- Have the Python REPL ready in a terminal for quick experiments.
- Plan to deliberately create an infinite loop and show how to stop it (Ctrl+C).
- Plan to show the difference between break (exit loop) and continue (skip to next iteration).
- Have a simple flowchart or diagram ready to show how while evaluates the condition at the top of each iteration.

**Say:** "Please have your editor open and an empty file ready. Today we learn how to make programs repeat actions until a goal is reached. You will type alongside me, then build your own authentication flow."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Hour 1

**Say:**
"Welcome back. In Hour 1, we learned how to make programs choose between different paths using if/elif/else statements. Your program could evaluate a condition once and execute one block of code based on that condition.

But what if you need to repeat an action multiple times? What if you want to keep asking the user for input until they give you a valid answer? What if you want to retry a failed operation until it succeeds?

That is where loops come in. A loop repeats a block of code. Today we focus on one type of loop: the while loop."

### 3.2 Motivating the need

**Say:**
"Let me give you a few real-world situations where you need repetition:

- A password prompt: keep asking for the password until the user gets it right, or until they fail 3 times.
- A menu system: show options, execute the user's choice, then show options again until they choose 'quit.'
- A game loop: process player input, update the game state, render the screen, repeat until the player quits or loses.
- A data validation loop: keep prompting for a number until the user enters something that can be converted to an integer.

In each case, you do not know in advance how many times the loop will run. It depends on what the user does. This is different from 'repeat exactly 10 times,' which we will cover in Hour 3. Today, we focus on 'repeat until some condition is met.'"

### 3.3 Set expectations for the hour

**Say:**
"In this hour, we will learn:
- how to write a while loop that repeats code until a condition becomes False
- how to avoid infinite loops by ensuring the condition eventually becomes False
- how to use break to exit a loop early
- how to use continue to skip the rest of an iteration
- how to implement a sentinel pattern, where a special input value signals 'stop'
- and how to build a secure password prompt with a limited number of attempts

The concepts are simple, but while loops are powerful and require careful thinking. If you do not update the loop condition properly, your program will run forever."

---

## 4) Concept: while Loops

### 4.1 Beginner-friendly definition

**Say:**
"A while loop repeats a block of code as long as a condition is True. The structure is:

```python
while condition:
    # code to repeat
```

Here is how Python executes a while loop:

1. Evaluate the condition.
2. If the condition is True, execute the indented block.
3. Go back to step 1 and evaluate the condition again.
4. If the condition is False, skip the loop and continue with the code after it.

The key insight: the condition is checked before each iteration, including the first one. If the condition is False the first time, the loop body never runs."

### 4.2 Simple example

**Say:**
"Let me show you the simplest possible while loop:

```python
count = 1

while count <= 3:
    print(f"Iteration {count}")
    count = count + 1

print("Done")
```

Let us trace this:

- Start: count is 1.
- Check condition: is 1 <= 3? Yes, so enter the loop.
- Print 'Iteration 1.'
- Increment count to 2.
- Check condition: is 2 <= 3? Yes, so loop again.
- Print 'Iteration 2.'
- Increment count to 3.
- Check condition: is 3 <= 3? Yes, so loop again.
- Print 'Iteration 3.'
- Increment count to 4.
- Check condition: is 4 <= 3? No, so exit the loop.
- Print 'Done.'

The loop ran exactly 3 times because we updated count each time, and eventually the condition became False."

### 4.3 The infinite loop danger

**Say:**
"What happens if you forget to update the variable that the condition depends on?

```python
count = 1

while count <= 3:
    print(f"Iteration {count}")
    # forgot to increment count
```

Now count never changes. The condition is always True. The loop runs forever. This is called an infinite loop.

If you accidentally create an infinite loop, your program will freeze. You must stop it manually. In most terminals and editors, press Ctrl+C to send a keyboard interrupt and stop the program.

Rule: every while loop must have a way for the condition to eventually become False. This usually means updating a variable inside the loop."

---

## 5) Concept: break and continue

### 5.1 The break statement

**Say:**
"Sometimes you want to exit a loop before the condition becomes False. You use the break statement:

```python
count = 1

while count <= 10:
    print(f"Iteration {count}")
    if count == 3:
        print("Breaking out of loop")
        break
    count = count + 1

print("Done")
```

When Python hits break, it immediately exits the loop, even though the condition `count <= 10` is still True. The program jumps to the code after the loop.

Output:
```
Iteration 1
Iteration 2
Iteration 3
Breaking out of loop
Done
```

Use break when you achieve your goal early and do not need to keep looping."

### 5.2 The continue statement

**Say:**
"The continue statement skips the rest of the current iteration and jumps back to the top of the loop to check the condition again.

```python
count = 0

while count < 5:
    count = count + 1
    if count == 3:
        print(f"Skipping {count}")
        continue
    print(f"Processing {count}")

print("Done")
```

When count is 3, we hit continue. Python skips the line `print(f'Processing {count}')` and goes straight back to the top. The condition is checked, and the loop continues.

Output:
```
Processing 1
Processing 2
Skipping 3
Processing 4
Processing 5
Done
```

Use continue when you want to skip certain cases but keep looping."

### 5.3 When to use break vs continue

**Say:**
"Use break when:
- You found what you were looking for (e.g., correct password entered).
- You hit an error condition that makes continuing pointless (e.g., file not found).
- The user chose to quit early (e.g., typed 'q').

Use continue when:
- You want to skip processing for this iteration but keep going (e.g., skip blank lines in a file).
- You hit a recoverable error and want to retry (e.g., user entered invalid input, re-prompt without exiting).

Both are control flow tools. Use them sparingly and clearly document why you are exiting or skipping."

---

## 6) Concept: Sentinel Patterns

### 6.1 What is a sentinel value?

**Say:**
"A sentinel is a special value that signals 'stop.' It is a common pattern in CLI programs.

Example: you want to let the user enter as many names as they want, then stop when they type 'done.'

```python
names = []

while True:
    name = input("Enter a name (or 'done' to finish): ")
    if name == 'done':
        break
    names.append(name)

print(f"You entered {len(names)} names.")
```

Notice the pattern:
1. The loop condition is `while True`, which means 'repeat forever.'
2. Inside the loop, we check if the user entered the sentinel value 'done.'
3. If they did, we break out of the loop.
4. Otherwise, we process the input and loop again.

This is called a 'loop-and-a-half' or 'sentinel pattern.' It is safe because the break guarantees we will eventually exit."

### 6.2 Choosing a sentinel value

**Say:**
"Your sentinel should be a value that the user would never enter as real data. For names, 'done' or 'quit' works. For numbers, -1 or 0 might work, but be careful: what if the user legitimately wants to enter 0?

Common sentinels:
- 'q' or 'quit' for text input
- Empty string '' if blank input is not valid data
- -1 for lists of positive numbers
- None in some contexts (not covered in Basics)

Document your sentinel clearly in the prompt so users know how to stop."

---

## 7) Live Coding Demo: Password Prompt (~10 minutes)

### 7.1 Announce the demo

**Say:**
"Now I am going to build a password prompt. The rules are:

- The correct password is 'python123' (hardcoded for demo purposes).
- The user has up to 3 attempts to enter it correctly.
- If they succeed, print 'Access granted' and stop.
- If they fail 3 times, print 'Account locked' and stop.

I will use a while loop with an attempt counter and a break statement. Watch how I think through the logic."

### 7.2 Code the solution

**Type aloud:**

```python
# Password prompt with retry limit

correct_password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    attempts = attempts + 1
    password = input(f"Enter password (attempt {attempts} of {max_attempts}): ")

    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password.")

# Check if we exited because of success or failure
if attempts == max_attempts and password != correct_password:
    print("Account locked. Too many failed attempts.")
```

**Say:**
"Let me explain the key parts:

1. **Loop condition:** `while attempts < max_attempts` means 'keep looping as long as we have not used all attempts.'

2. **Increment first:** We increment attempts at the start of each iteration so the counter is accurate.

3. **Check for success:** If the password is correct, we print 'Access granted' and break immediately. This exits the loop even though we might have attempts left.

4. **Final check:** After the loop, we check if we used all attempts and still failed. If so, we lock the account.

Notice that if the user succeeds on attempt 1, the loop exits immediately and we never reach attempts 2 or 3. That is the power of break."

### 7.3 Test the code

**Say:**
"Let me test this with a few scenarios."

**Test 1: Success on first try**
- Input: python123
- Output: "Access granted!"

**Test 2: Success on third try**
- Input: wrong1
- Output: "Incorrect password."
- Input: wrong2
- Output: "Incorrect password."
- Input: python123
- Output: "Access granted!"

**Test 3: Failure after 3 tries**
- Input: wrong1
- Output: "Incorrect password."
- Input: wrong2
- Output: "Incorrect password."
- Input: wrong3
- Output: "Incorrect password."
- Output: "Account locked. Too many failed attempts."

**Say:**
"All three scenarios work correctly. The loop terminates either when the user succeeds (via break) or when attempts reaches 3 (condition becomes False)."

### 7.4 Common mistake: off-by-one in attempts

**Say:**
"A common bug is incrementing attempts in the wrong place. If you increment after checking the password, the count will be wrong:

```python
# WRONG
while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        break
    attempts = attempts + 1  # incremented only on failure
```

Now if the user succeeds on attempt 1, attempts never increments, and the final check does not work correctly. Always increment at the top of the loop so the counter is accurate every iteration."

---

## 8) Guided Lab: Password Prompt (~25 minutes)

### 8.1 Announce the lab

**Say:**
"Now it is your turn. You will build a password prompt with retry logic. Here is the specification:

**Lab: Password Prompt**

**Goal:** Create a program that prompts for a password up to 3 times. If the user enters the correct password, grant access and stop. If they fail 3 times, lock them out.

**Rules:**

- Correct password: 'secure123' (hardcoded for this lab)
- Maximum 3 attempts
- After each incorrect attempt, show how many attempts remain
- On success, print 'Access granted!' and stop immediately
- On failure, print 'Account locked. Contact support.'

**Optional extensions (if you finish early):**

1. Add a message showing remaining attempts after each failure.
2. Add validation: if the user enters an empty string, do not count it as an attempt and re-prompt.

**Completion criteria:**

- Program stops correctly on success (uses break)
- Program stops correctly after 3 failures
- Attempt counter is accurate
- Clear output for each attempt

You have 25 minutes. I will circulate and help."

### 8.2 Circulate and provide feedback

Walk around the room. Look for:

- **Infinite loops:** Students forget to increment the attempt counter, or forget to use break.
- **Off-by-one errors:** Incrementing attempts in the wrong place, or using the wrong comparison (<= vs <).
- **No final check:** Not checking after the loop whether the user succeeded or failed.
- **Hardcoding instead of looping:** Using three separate if statements instead of a loop.

**Common mistake to watch for:**

```python
while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
    attempts = attempts + 1
```

This keeps prompting even after success, because there is no break. The user sees "Access granted" but the loop continues. The fix is to add `break` after the success message.

**Coaching language:**

- "What happens if the user enters the correct password on attempt 1? Does your loop stop immediately?"
- "If I run your program and deliberately fail 3 times, what message do I see?"
- "How do you know whether the loop exited because of success or because of running out of attempts?"

### 8.3 Debugging support

If a student is stuck:

1. Ask them to add `print(f"Attempt: {attempts}")` at the top of the loop to trace the counter.
2. Ask them to run the program and deliberately fail 3 times. What happens?
3. If they have an infinite loop, help them identify which variable needs to change in each iteration.

---

## 9) Debrief and Knowledge Check (~12 minutes)

### 9.1 Share-out

**Say:**
"Let us hear from a few people. Who wants to show their solution and explain how they used break?"

**Call on 2–3 learners. Ask:**

- "Where did you increment the attempt counter? Why there?"
- "What happens if the user succeeds on the first try?"
- "How did you check whether the user succeeded or ran out of attempts?"

### 9.2 Common mistakes review

**Say:**
"Here are the most common mistakes I saw today:

1. **Infinite loop:** Forgetting to update the variable that the loop condition depends on. If `attempts` never changes, `attempts < 3` is always True.

2. **No break on success:** The program prints 'Access granted' but keeps looping. You must use break to exit immediately.

3. **Wrong condition:** Using `while attempts <= 3` instead of `while attempts < 3` gives the user 4 attempts instead of 3.

4. **Incrementing in the wrong place:** If you increment only on failure, your counter is wrong when the user succeeds early.

5. **Not checking final state:** After the loop, you must check whether the user succeeded or failed. Do not assume failure just because the loop ended.

The fix for all of these: plan your loop carefully, update the counter consistently, and test both success and failure paths."

### 9.3 Conceptual recap

**Say:**
"Let me summarize today's key ideas:

1. **while loops repeat as long as a condition is True.** Python checks the condition at the top of each iteration. If it is False, the loop body does not run.

2. **Update the loop variable.** Every while loop must change something that affects the condition, or you get an infinite loop.

3. **break exits immediately.** Use break when you achieve your goal early and do not need to keep looping.

4. **continue skips the rest of this iteration.** Use continue when you want to move to the next iteration without executing the rest of the loop body.

5. **Sentinel pattern:** Use `while True` with a break when the user enters a special value. This is safe as long as your break is inside the loop.

While loops are flexible and powerful, but they require careful logic. In Hour 3, we will learn for loops, which are better suited for 'repeat exactly N times' scenarios."

---

## 10) Exit Ticket (~3 minutes)

**Say:**
"Before we finish, write down your answer to this question. You do not need to submit it, but think it through:

**Question:** What is the minimum number of times a while loop's body can execute? What is the maximum?

Hint: think about what happens if the condition is False on the first check."

**Pause for 1 minute, then reveal the answer:**

**Say:**
"Minimum: **zero times**. If the condition is False the first time Python checks it, the loop body never runs.

Example:
```python
count = 10
while count < 5:
    print('This never prints')
```

Maximum: **infinite**. If the condition never becomes False, the loop runs forever. That is why you must always update the loop variable.

This is different from a do-while loop in some other languages, which guarantees at least one execution. Python does not have do-while. If you need to run at least once, you can use `while True` with a break inside, or simply put the first execution before the loop."

---

## 11) Transition to Next Hour

**Say:**
"Excellent work today. You now know how to repeat actions until a condition is met, how to exit loops early, and how to implement sentinel patterns.

In Hour 3, we will learn about for loops, which are designed for iterating over sequences like lists and ranges. We will use range() to repeat code a specific number of times and iterate over collections item by item.

Take a 5-minute break. When you return, have your editor ready."

---

## 12) Appendix: Quick Reference for Instructors

### While loop patterns

**Count-controlled:**
```python
count = 0
while count < n:
    # do something
    count += 1
```

**Sentinel-controlled:**
```python
while True:
    value = input("Enter value (or 'q' to quit): ")
    if value == 'q':
        break
    # process value
```

**Condition-controlled:**
```python
success = False
while not success:
    result = try_something()
    if result is good:
        success = True
```

### Testing checklist

- Does the loop ever start? (Check initial condition)
- Does the loop eventually stop? (Check that the condition can become False)
- Does break work correctly? (Test early exit cases)
- Does continue work correctly? (Test skip cases)
- What happens on the first iteration?
- What happens on the last iteration?

### Troubleshooting common student issues

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "My program never stops" | Infinite loop; condition never becomes False | Check that loop variable is updated each iteration |
| "My loop runs 4 times instead of 3" | Wrong comparison operator | Use `<` not `<=` if you want exactly 3 iterations |
| "Program prints 'Access granted' but keeps looping" | No break after success | Add `break` after success message |
| "Attempt counter shows wrong number" | Incrementing in wrong place | Increment at top of loop, not only on failure |
| "How do I stop an infinite loop?" | Ctrl+C not working | In some IDEs, use Stop button; in terminal, Ctrl+C |

---

## 13) Deep Dive: Loop Invariants (Optional, for advanced learners)

**Teaching point:**
"A loop invariant is a statement that is true before the loop starts, remains true after each iteration, and is still true when the loop ends.

Example: In our password prompt, the invariant might be 'attempts is always the count of how many times we have checked the password.'

Thinking about invariants helps you design correct loops:

1. What must be true before the loop starts? (Initialization)
2. What must remain true after each iteration? (Maintenance)
3. What is true when the loop ends? (Termination)

In our password example:

1. Before loop: attempts = 0 (no checks yet)
2. After each iteration: attempts = number of checks performed
3. After loop: attempts <= max_attempts, and either password matched or attempts == max_attempts

This is an advanced concept, but it is how computer scientists prove that loops are correct. For now, just remember: think about what your loop variables mean at each stage."

---

## 14) Real-World Context: Why Loops Go Wrong

**Teaching point:**
"Infinite loops are one of the most common bugs in software. Here are real examples:

1. **Mars Rover:** A NASA rover's software had a loop that did not properly handle a sensor timeout. The loop kept retrying indefinitely, draining the battery. Engineers had to send a patch.

2. **ATM Machines:** An ATM software bug caused the screen to loop between 'Processing' and 'Please wait' forever. Users could not cancel the transaction. The fix required a reboot.

3. **Video Games:** Many games have had bugs where the loading screen loops forever. This happens when the loop waits for a resource that never loads, and there is no timeout.

4. **Web Servers:** A server application had a loop that retried failed database connections without a delay. It made thousands of connection attempts per second, overwhelming the database and crashing both systems.

The lesson: always design your loops with a clear exit condition, and test that the condition can actually become False."

---

## 15) Style Guide: Writing Readable Loops

**Teaching point:**
"Good loop style makes your code easier to understand and debug:

**1. Use meaningful loop variable names:**

Bad:
```python
i = 0
while i < 3:
    # what does i represent?
    i += 1
```

Better:
```python
attempts = 0
while attempts < max_attempts:
    # clear that this counts attempts
    attempts += 1
```

**2. Document why the loop exists:**

```python
# Keep prompting until user enters a valid positive number
while True:
    value = input("Enter a positive number: ")
    if value.isdigit() and int(value) > 0:
        break
```

**3. Avoid nested while loops if possible:**

Nested while loops are hard to reason about and easy to break. If you need nested loops, consider refactoring into functions (covered in Session 9).

**4. Initialize loop variables clearly:**

```python
# Good: all initialization together, before the loop
attempts = 0
success = False
max_attempts = 3

while attempts < max_attempts and not success:
    # loop body
```

These are not strict rules, but they make your code easier to read and maintain."

---

## 16) Comparison: while vs for (Preview)

**Teaching point:**
"We have not covered for loops yet, but here is a quick preview of the difference:

**while loop:** Use when you do not know in advance how many times you need to loop. The loop continues until a condition becomes False.

Example: Keep asking for input until the user enters 'quit.'

**for loop (covered next hour):** Use when you know in advance how many times to loop, or when you want to iterate over a collection.

Example: Print every name in a list, or repeat an action exactly 10 times.

Both are powerful, and you will use both throughout this course. The key is choosing the right tool for the job."

---

## 17) Summary: Key Takeaways

**Say:**
"Before we move to Hour 3, let me emphasize the four most important points:

1. **while loops repeat as long as a condition is True.** You must ensure the condition eventually becomes False, or you get an infinite loop.

2. **Update the loop variable consistently.** Increment counters at the top of the loop so they are accurate every iteration.

3. **Use break to exit early.** When you achieve your goal (like correct password), use break to stop immediately.

4. **Sentinel patterns are safe.** Using `while True` with a break inside is a common and correct pattern, as long as the break is guaranteed to execute eventually.

These principles apply to every loop you will ever write, not just password prompts."

---

**End of Hour 2 Script**
