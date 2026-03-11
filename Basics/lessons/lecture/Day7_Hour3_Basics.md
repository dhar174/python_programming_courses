# Day 7, Hour 3: for Loops + range() (Course Hour 27)
**Python Programming Basics – Session 7**

**Course:** Python Programming (Basics)
**Runbook alignment:** Session 7, Course Hour 27 – for loops + range()
**Duration:** 60 minutes
**Mode:** Instructor-led + live coding + guided lab
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. Keep the hour tightly focused on for loops: iterating over sequences, using range() for counted loops, understanding inclusive/exclusive endpoints, and choosing between for and while. Stay within Basics scope — do not introduce enumerate(), zip(), list comprehensions, or generator expressions. The key outcomes are writing for loops to iterate over lists, using range() with one/two/three arguments, and building a multiplication table. The lab reinforces all of this in a practical table-generation program.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Write a for loop that iterates over a list or other sequence.
2. Use range(n), range(start, stop), and range(start, stop, step) to generate number sequences.
3. Explain why range() uses exclusive endpoints and how to adjust for inclusive ranges.
4. Choose between for loops and while loops based on whether you know the iteration count in advance.
5. Build a multiplication table using nested for loops with range()."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Hour 2 while loops; introduce for loops for known iteration counts
- **0:05–0:18** Core concept: for loops, iterating over sequences
- **0:18–0:30** range() function: one, two, and three argument forms
- **0:30–0:38** Nested for loops: tables and grids
- **0:38–0:48** Live demo: multiplication table
- **0:48–0:57** Guided lab: Multiplication Table
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour27_for_demo.py` before class begins.
- Have a second file called `hour27_lab_table.py` ready with empty comments as a starter.
- Have the Python REPL ready for quick range() experiments.
- Plan to demonstrate range() with different argument counts.
- Plan to show a common off-by-one error with range() and how to fix it.
- Prepare to show nested loops with clear indentation.

**Say:** "Please have your editor open and an empty file ready. Today we learn for loops, which are perfect when you know exactly how many times to repeat something. You will build a multiplication table using nested loops."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Hour 2

**Say:**
"Welcome back. In Hour 2, we learned while loops: repeat until a condition becomes False. While loops are flexible and powerful, but they require careful management of the loop condition.

Today we learn for loops. A for loop is designed for a different scenario: when you want to process each item in a collection, or when you want to repeat an action a specific number of times.

The key difference: with a for loop, Python handles the iteration for you. You do not manually update a counter or check a condition. Python does that automatically."

### 3.2 Motivating the need

**Say:**
"Let me give you a few real-world situations where for loops are the right tool:

- Print every name in a list of students.
- Calculate the sum of all numbers in a list.
- Repeat an action exactly 10 times (like printing a row of stars).
- Build a multiplication table from 1 to 10.
- Process every file in a directory (covered in Session 11).

In each case, you know what you are iterating over: a list, a range of numbers, a collection of files. You do not need to manually check when to stop. Python handles that for you."

### 3.3 Set expectations for the hour

**Say:**
"In this hour, we will learn:
- how to write a for loop that iterates over a list
- how to use range() to generate sequences of numbers
- why range() endpoints are exclusive and how to handle that
- when to choose for loops versus while loops
- and how to use nested for loops to build tables

By the end, you will understand when to use for instead of while, and you will have built a multiplication table."

---

## 4) Concept: for Loops

### 4.1 Beginner-friendly definition

**Say:**
"A for loop repeats a block of code once for each item in a sequence. The structure is:

```python
for item in sequence:
    # code to repeat
```

Here is how Python executes a for loop:

1. Python gets the first item from the sequence.
2. It assigns that item to the variable after the word 'for' (in this case, 'item').
3. It executes the indented block.
4. It goes back to step 1 and gets the next item.
5. When there are no more items, the loop stops.

The key insight: you do not update a counter. Python moves through the sequence automatically."

### 4.2 Simple example with a list

**Say:**
"Let me show you the simplest for loop:

```python
names = ['Alice', 'Bob', 'Charlie']

for name in names:
    print(f'Hello, {name}!')
```

Output:
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

Python takes each name from the list, one at a time, and executes the print statement. When there are no more names, the loop stops.

Compare this to a while loop:

```python
names = ['Alice', 'Bob', 'Charlie']
index = 0

while index < len(names):
    name = names[index]
    print(f'Hello, {name}!')
    index = index + 1
```

This works, but it is longer and more error-prone. You have to manage the index manually. The for loop is cleaner and safer."

### 4.3 Choosing meaningful variable names

**Say:**
"The variable after 'for' is a temporary name that exists only inside the loop. Choose a name that describes what each item is.

Good:
```python
for student in students:
    print(student)

for number in numbers:
    print(number * 2)
```

Bad:
```python
for x in students:
    print(x)  # what is x?

for thing in numbers:
    print(thing * 2)  # too generic
```

Use singular form for the loop variable and plural form for the list: student/students, number/numbers, file/files."

---

## 5) Concept: range()

### 5.1 What is range()?

**Say:**
"The range() function generates a sequence of numbers. It is commonly used with for loops when you want to repeat an action a specific number of times.

**range(n)** generates numbers from 0 up to (but not including) n.

Example:
```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

Notice two things:

1. It starts at 0, not 1.
2. It stops before 5, not at 5.

This is called an exclusive endpoint. The range includes 0, 1, 2, 3, 4 — five numbers total, but 5 itself is not included."

### 5.2 Why exclusive endpoints?

**Say:**
"Exclusive endpoints feel strange at first, but they have advantages:

1. The length is obvious: range(5) gives you 5 numbers (0 to 4).
2. Ranges do not overlap: range(0, 5) and range(5, 10) fit together perfectly without gaps or overlaps.
3. List indexing works naturally: a list with 5 items has valid indices 0, 1, 2, 3, 4, which is exactly what range(5) gives you.

If you need to count from 1 to 5 inclusive, use range(1, 6):

```python
for i in range(1, 6):
    print(i)
```

Output:
```
1
2
3
4
5
```

The first argument is the start (inclusive), the second is the stop (exclusive)."

### 5.3 Three forms of range()

**Say:**
"range() has three forms:

**1. range(stop):** Start at 0, count up to (but not including) stop.

```python
for i in range(3):
    print(i)
# Output: 0, 1, 2
```

**2. range(start, stop):** Start at start, count up to (but not including) stop.

```python
for i in range(2, 5):
    print(i)
# Output: 2, 3, 4
```

**3. range(start, stop, step):** Start at start, count by step, stop before stop.

```python
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

You can also count backwards:

```python
for i in range(5, 0, -1):
    print(i)
# Output: 5, 4, 3, 2, 1
```

The step determines the direction and size of each increment."

---

## 6) Concept: Nested for Loops

### 6.1 What is a nested loop?

**Say:**
"A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

Example:
```python
for row in range(3):
    for col in range(4):
        print(f'({row}, {col})', end=' ')
    print()  # new line after each row
```

Output:
```
(0, 0) (0, 1) (0, 2) (0, 3)
(1, 0) (1, 1) (1, 2) (1, 3)
(2, 0) (2, 1) (2, 2) (2, 3)
```

The outer loop runs 3 times (row = 0, 1, 2). For each row, the inner loop runs 4 times (col = 0, 1, 2, 3). Total: 3 × 4 = 12 iterations."

### 6.2 When to use nested loops

**Say:**
"Use nested loops when you have two-dimensional data:

- A grid or table (rows and columns)
- A multiplication table (one factor on each axis)
- A seating chart (rows and seats)
- Nested lists (list of lists)

The outer loop typically handles rows or the first dimension. The inner loop handles columns or the second dimension.

Keep nesting to two levels when possible. Three or more levels become hard to read and debug."

---

## 7) Live Coding Demo: Multiplication Table (~10 minutes)

### 7.1 Announce the demo

**Say:**
"Now I am going to build a multiplication table. The goal is to print a table showing n × m for values 1 through 10.

I will use nested for loops with range(). Watch how the outer loop controls the rows and the inner loop controls the columns."

### 7.2 Code the solution

**Type aloud:**

```python
# Multiplication table: 1 through 10

print("Multiplication Table (1-10)")
print()

for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        print(f"{product:4}", end="")
    print()  # new line after each row
```

**Say:**
"Let me explain the key parts:

1. **range(1, 11):** This gives us 1 through 10 (remember, 11 is exclusive).

2. **Outer loop (i):** Controls which row we are on. i goes from 1 to 10.

3. **Inner loop (j):** Controls which column we are on. j goes from 1 to 10.

4. **product = i * j:** Compute the multiplication result.

5. **f'{product:4}':** Format with width 4 so columns align. The :4 means 'use at least 4 characters, right-aligned.'

6. **end='':** Print without a newline so all products in a row stay on the same line.

7. **print() after inner loop:** After finishing a row, print a newline to move to the next row."

### 7.3 Test the code

**Say:**
"Let me run this."

**Output (first few lines):**
```
Multiplication Table (1-10)

   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
...
```

**Say:**
"The table shows all products from 1×1 to 10×10. Each row represents one value of i, and each column represents one value of j."

### 7.4 Common mistake: wrong range

**Say:**
"A common bug is using range(10) instead of range(1, 11). Let me show what happens:

```python
for i in range(10):  # This gives 0-9, not 1-10
    for j in range(10):
        print(i * j, end=' ')
    print()
```

Output starts with:
```
0 0 0 0 ...  # first row is all zeros
0 1 2 3 ...  # second row starts at 0
```

This is wrong because we wanted 1-10, not 0-9. The fix is to use range(1, 11)."

---

## 8) Guided Lab: Multiplication Table (~25 minutes)

### 8.1 Announce the lab

**Say:**
"Now it is your turn. You will build a multiplication table. Here is the specification:

**Lab: Multiplication Table**

**Goal:** Ask the user for a number n, then print a multiplication table from 1 to n.

**Rules:**

- Prompt user for n (a positive integer)
- Print a table showing i × j for all i and j from 1 to n
- Format output so columns align
- Label the first row and first column (optional extension)

**Optional extensions (if you finish early):**

1. Add row and column headers (the numbers 1 through n).
2. Add validation: if n is not a positive integer, re-prompt.

**Completion criteria:**

- Table prints correctly for any n (test with n=5, n=10, n=12)
- Columns align properly
- Range uses correct start and stop values

You have 25 minutes. I will circulate and help."

### 8.2 Circulate and provide feedback

Walk around the room. Look for:

- **Wrong range:** Using range(n) instead of range(1, n+1).
- **No newline after row:** Forgetting print() after the inner loop.
- **Misaligned columns:** Not using formatting like {:4}.
- **Nested loop confusion:** Mixing up which loop is outer and which is inner.

**Common mistake to watch for:**

```python
for i in range(n):
    for j in range(n):
        print(i * j)  # prints each product on its own line
```

This prints every product on a separate line instead of in a table. The fix is to use `end=' '` and add `print()` after the inner loop.

**Coaching language:**

- "How many times does the inner loop run for each iteration of the outer loop?"
- "If n is 5, what values should i and j take? Does range(5) give you that?"
- "How do you print multiple values on the same line?"

### 8.3 Debugging support

If a student is stuck:

1. Ask them to print i and j at the start of each inner loop iteration to see what values they are getting.
2. Ask them to run their program with n=3 first (small table is easier to debug).
3. If alignment is wrong, show them the {:4} format specifier.

---

## 9) Debrief and Knowledge Check (~12 minutes)

### 9.1 Share-out

**Say:**
"Let us hear from a few people. Who wants to show their solution and explain how nested loops work?"

**Call on 2–3 learners. Ask:**

- "How did you ensure your range started at 1 and ended at n?"
- "What does the outer loop control? What does the inner loop control?"
- "Did you try any of the optional extensions?"

### 9.2 Common mistakes review

**Say:**
"Here are the most common mistakes I saw today:

1. **Wrong range:** Using range(n) gives you 0 to n-1, not 1 to n. Use range(1, n+1) if you want 1 to n inclusive.

2. **No newline after row:** Forgetting print() after the inner loop means everything prints on one long line.

3. **Confusing i and j:** The outer loop variable (usually i) controls rows. The inner loop variable (usually j) controls columns.

4. **Not formatting output:** Without formatting like {:4}, columns do not align and the table looks messy.

The fix for all of these: plan your loops carefully, test with small values, and use print statements to debug."

### 9.3 Conceptual recap

**Say:**
"Let me summarize today's key ideas:

1. **for loops iterate over sequences.** Python handles the iteration automatically. You do not update a counter.

2. **range() generates number sequences.** Use range(n) for 0 to n-1, range(start, stop) for start to stop-1, and range(start, stop, step) for custom increments.

3. **Endpoints are exclusive.** range(1, 11) gives you 1 through 10. The stop value is not included.

4. **Nested loops create tables.** The outer loop runs once per row. For each row, the inner loop runs once per column.

5. **for vs while:** Use for when you know what you are iterating over. Use while when you repeat until a condition changes.

These patterns apply to many problems: processing lists, generating sequences, building tables, and more."

---

## 10) Exit Ticket (~3 minutes)

**Say:**
"Before we finish, write down your answer to this question:

**Question:** What does range(1, 4) produce? What about range(4, 1)? What about range(4, 1, -1)?

**Pause for 1 minute, then reveal the answer:**

**Say:**
"range(1, 4) produces 1, 2, 3. Start at 1, stop before 4.

range(4, 1) produces nothing. The start is greater than the stop, and the default step is +1, so Python cannot count from 4 to 1 going upwards.

range(4, 1, -1) produces 4, 3, 2. Start at 4, step backwards by 1, stop before 1.

Lesson: range() with only two arguments assumes step = +1. If you want to count backwards, you must provide a negative step as the third argument."

---

## 11) Transition to Next Hour

**Say:**
"Excellent work today. You now know how to use for loops to iterate over collections and use range() to generate sequences.

In Hour 4, we will learn common loop patterns: counters, accumulators, and finding min/max values. These are the building blocks for almost every program you will write.

Take a 5-minute break. When you return, have your editor ready."

---

## 12) Appendix: Quick Reference for Instructors

### for loop patterns

**Iterate over a list:**
```python
for item in my_list:
    print(item)
```

**Count n times:**
```python
for i in range(n):
    print(i)
```

**Count from start to stop:**
```python
for i in range(start, stop):
    print(i)
```

**Count with step:**
```python
for i in range(0, 10, 2):
    print(i)
```

**Nested loops (table):**
```python
for row in range(rows):
    for col in range(cols):
        print(f'({row},{col})', end=' ')
    print()
```

### Testing checklist

- Does the loop iterate the expected number of times?
- Are the range endpoints correct (inclusive/exclusive)?
- Does the nested loop structure produce the right shape?
- Does each row end with a newline?
- Is output formatted and aligned?

### Troubleshooting common student issues

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "My table prints all on one line" | Missing print() after inner loop | Add print() after the inner for loop |
| "My table starts at 0 instead of 1" | Using range(n) instead of range(1, n+1) | Use range(1, n+1) for 1 to n inclusive |
| "My columns don't line up" | No formatting | Use {:4} or similar format specifier |
| "range(5, 1) produces nothing" | Step defaults to +1, can't count down | Use range(5, 1, -1) to count backwards |
| "I don't understand nested loops" | Inner loop runs fully for each outer iteration | Draw a diagram showing outer loop rows, inner loop columns |

---

## 13) Real-World Context: Why Loops Matter

**Teaching point:**
"for loops are everywhere in professional code. Here are real examples:

1. **Data Processing:** A data analyst loops through thousands of records to compute statistics.

2. **Web Scraping:** A script loops through a list of URLs, fetching and parsing each page.

3. **Game Development:** A game loop runs 60 times per second, updating positions and rendering graphics.

4. **Report Generation:** An accounting system loops through transactions to build a summary report.

In every case, the programmer knows what they are iterating over: a list of records, a list of URLs, a fixed frame rate, a list of transactions. That is when for loops shine."

---

## 14) Comparison: for vs while

**Teaching point:**
"When should you use for instead of while?

**Use for when:**
- You are iterating over a known collection (list, string, file lines).
- You want to repeat an action a specific number of times.
- You do not need to check a condition that could change unpredictably.

**Use while when:**
- You do not know in advance how many iterations you need.
- You are waiting for a condition to become True or False.
- The user controls when to stop (sentinel pattern).

Example: Reading user input until they type 'quit' → while loop.
Example: Processing every item in a list of 100 names → for loop.

Many problems can be solved with either loop, but one is usually more natural."

---

## 15) Deep Dive: Why range() is Exclusive

**Teaching point:**
"The exclusive endpoint design is not arbitrary. It comes from computer science conventions:

1. **Zero-based indexing:** Arrays and lists start at index 0. A list with 5 items has indices 0, 1, 2, 3, 4. range(5) produces exactly those indices.

2. **Non-overlapping ranges:** range(0, 5) and range(5, 10) fit together perfectly. If 5 were included in both, you would double-count.

3. **Length equals stop minus start:** range(start, stop) produces (stop - start) numbers. range(2, 7) produces 5 numbers: 2, 3, 4, 5, 6. The math is simple.

4. **Empty ranges are natural:** range(5, 5) produces nothing, which makes sense: there are zero numbers from 5 (inclusive) to 5 (exclusive).

These conventions are used in Python, C, Java, JavaScript, and many other languages. Once you get used to exclusive endpoints, they feel natural."

---

## 16) Style Guide: Writing Readable for Loops

**Teaching point:**
"Good for loop style makes your code easier to understand:

**1. Use meaningful loop variable names:**

Bad:
```python
for x in students:
    print(x)
```

Better:
```python
for student in students:
    print(student)
```

**2. Avoid modifying the loop variable inside the loop:**

Bad:
```python
for i in range(10):
    i = i * 2  # this has no effect on the loop!
    print(i)
```

The loop variable is reassigned on every iteration. Modifying it inside the loop does not change the iteration.

**3. Keep nested loops simple:**

If your nested loops are more than 2 levels deep, consider breaking them into functions (covered in Session 9).

**4. Use comments to explain complex loops:**

```python
# Build a grid of (row, col) tuples
for row in range(rows):
    for col in range(cols):
        grid.append((row, col))
```

These style practices make your code easier to read and maintain."

---

## 17) Summary: Key Takeaways

**Say:**
"Before we move to Hour 4, let me emphasize the four most important points:

1. **for loops are for known iteration.** Use them when you know what you are iterating over: a list, a string, or a range of numbers.

2. **range() endpoints are exclusive.** range(1, 11) gives you 1 through 10. The stop value is not included.

3. **Nested loops create two-dimensional structures.** Outer loop = rows, inner loop = columns. Total iterations = outer × inner.

4. **Choose for over while when possible.** for loops are safer and clearer when you know the iteration count."

---

**End of Hour 3 Script**

## 18) Advanced Pattern: Using enumerate() (Preview)

**Teaching point:**
"We have not covered enumerate() in detail, but here is a preview for curious learners.

Sometimes you need both the index and the value from a list. You could use range(len(list)) and index into the list:

```python
names = ['Alice', 'Bob', 'Charlie']
for i in range(len(names)):
    print(f"{i}: {names[i]}")
```

But there is a cleaner way using enumerate():

```python
names = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(names):
    print(f"{i}: {name}")
```

This gives you both the index (i) and the value (name) in each iteration.

Output:
```
0: Alice
1: Bob
2: Charlie
```

enumerate() is covered in more detail in advanced topics, but you can use it now if you understand the pattern."

---

## 19) Practical Exercise: Debugging Nested Loops

**Teaching point:**
"Nested loops are a common source of bugs. Here is a debugging strategy:

**1. Print loop variables at the start of each iteration:**

```python
for i in range(3):
    print(f"Outer loop: i={i}")
    for j in range(4):
        print(f"  Inner loop: j={j}")
        # rest of code
```

This shows you exactly which iteration you are on.

**2. Test with small values first:**

If your table should be 10×10, test with 3×3 first. Smaller output is easier to verify.

**3. Check your indentation:**

The code inside the inner loop must be indented twice. The code that runs after the inner loop (like `print()` for a newline) must be indented only once.

**4. Draw a diagram:**

Sketch the expected output on paper. Count how many rows and columns you expect. Then compare to what your code produces."

---

## 20) Real-World Example: Password Strength Checker

**Teaching point:**
"Let me show you a practical use of for loops: checking password strength.

```python
password = input("Enter a password: ")

has_digit = False
has_upper = False
has_lower = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True

if has_digit and has_upper and has_lower and len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")
```

This loops through every character in the password string and checks for digits, uppercase, and lowercase letters. After the loop, we check if all criteria are met.

This is a common pattern: loop through data, collect information, then make a decision based on what you found."

---

## 21) Conceptual Check: Loop Termination

**Teaching point:**
"Every loop must eventually stop. Here is how for loops guarantee termination:

**for loops always terminate** (assuming the sequence is finite). Python iterates through the sequence once and stops when it reaches the end. You cannot accidentally create an infinite for loop (unless you modify the sequence during iteration, which is advanced and discouraged).

**while loops do not guarantee termination.** You must ensure the condition eventually becomes False.

This is one reason for loops are safer: Python handles termination for you."

---

## 22) Quick Reference: Common range() Patterns

**Say:**
"Here are the most common range() patterns you will use:

**Count from 0 to n-1:**
```python
for i in range(n):
    print(i)
```

**Count from 1 to n:**
```python
for i in range(1, n+1):
    print(i)
```

**Count by twos:**
```python
for i in range(0, n, 2):
    print(i)
```

**Count backwards from n to 1:**
```python
for i in range(n, 0, -1):
    print(i)
```

**Iterate over list indices:**
```python
for i in range(len(my_list)):
    print(my_list[i])
```

Memorize these patterns. They cover 90% of range() usage."

---

**End of Hour 3 Script**
