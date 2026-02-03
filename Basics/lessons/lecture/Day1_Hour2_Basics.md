# Day 1, Hour 2: First Scripts – print(), Comments, and Reading Errors
**Python Programming Basics – Session 1**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Hour 1: 3 minutes
- Core Concepts (print, comments, syntax): 10-15 minutes
- Style Standards Introduction: 5 minutes
- Live Demo (Common Mistakes): 5-10 minutes
- Hands-On Lab (Greeter): 25-35 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Use `print()` to produce output with string literals
2. Write comments using `#` and explain when and why to use them
3. Recognize and read common Python error messages
4. Apply basic Python style standards (indentation, naming, f-strings)
5. Deliberately create a syntax error, read the message, and fix it
6. Explain why whitespace and indentation matter in Python

---

## Section 1: Recap & Transition from Hour 1 (3 minutes)

### Quick Review

**[Instructor speaks:]**

Welcome back! In Hour 1, we got our environment set up, navigated the lab platform, and ran our very first Python script. You should now have:

- A working lab environment with your `python_basics` folder
- The ability to open and run `.py` files
- An understanding of the difference between the REPL and script files

Quick show of hands: **Who successfully ran their `hello_course.py` script and saw output?**

[Wait for responses]

Great! And if you didn't quite get there—that's okay. Stay after this hour and we'll troubleshoot together.

### What We're Building Toward

In Hour 1, we ran code that was basically handed to us. Starting now, **you're going to write your own**. And here's something important to know upfront:

**You will make mistakes. Everyone does. I do. Every professional programmer does—daily.**

The difference between a beginner and an experienced programmer isn't that experienced programmers don't make errors. It's that **they know how to read error messages and fix them quickly.**

So this hour is about three core skills:

1. **Writing simple output** with `print()`
2. **Documenting your code** with comments
3. **Reading and fixing errors** like a pro

By the end of this hour, errors won't scare you anymore. They'll be your helpful assistants.

Let's get started.

---

## Section 2: Core Concepts – print(), Strings, and Comments (10-15 minutes)

### The print() Function

**[Instructor speaks:]**

Let's talk about `print()`. You've already used it in Hour 1, but let's understand it properly.

**What is `print()`?**

`print()` is a **built-in function** in Python. Its job is simple: take whatever you give it and display it to the screen (technically, to "standard output," which is usually your terminal or console).

Here's the anatomy of a print statement:

```python
print("Hello, world!")
```

Let's break this down:

- **`print`**: The function name
- **`(`**: Opening parenthesis—this starts the argument list
- **`"Hello, world!"`**: The argument—what we want to display
- **`)`**: Closing parenthesis—this ends the argument list

**[Key point]:** The parentheses are **required**. You can't just write `print "Hello"` (that was valid in Python 2, but we're using Python 3). If you forget them, Python will give you an error.

### String Literals

**[Instructor speaks:]**

Notice those quotation marks around `"Hello, world!"`? That's how we tell Python: "This is text, not code."

In Python, text is called a **string**. A string is a sequence of characters—letters, numbers, spaces, punctuation—anything you can type.

**You can use either single quotes or double quotes:**

```python
print("This works!")
print('This also works!')
```

Both are perfectly valid. Python doesn't care which you use, as long as you're consistent. 

**When do you choose one over the other?**

- If your text contains an apostrophe, use double quotes:
  ```python
  print("It's a beautiful day!")
  ```

- If your text contains double quotes, use single quotes:
  ```python
  print('She said, "Hello!"')
  ```

- Otherwise, **be consistent**. In this course, we'll generally use double quotes unless we have a reason not to.

### Printing Multiple Things

**[Instructor speaks:]**

You can pass multiple items to `print()` separated by commas:

```python
print("Hello", "world", "from", "Python")
```

**What do you think this will output?**

[Pause for student predictions]

It prints:
```
Hello world from Python
```

Notice that Python automatically adds **spaces between the items**. That's convenient!

You can also print numbers without quotes:

```python
print("I am", 25, "years old")
```

Output:
```
I am 25 years old
```

When you don't use quotes around a number, Python treats it as an actual numeric value, not text. We'll dive deeper into the difference next hour.

### Empty Lines and print()

**[Instructor speaks:]**

What if you just want to print a blank line to space things out?

```python
print()
```

Just `print()` with nothing inside the parentheses prints an empty line. This is useful for making your output more readable:

```python
print("Welcome to my program!")
print()
print("Let's get started.")
```

Output:
```
Welcome to my program!

Let's get started.
```

See that blank line in the middle? That makes the output easier to read.

---

### Comments: Talking to Humans (Not Python)

**[Instructor speaks:]**

Now let's talk about comments. A comment is a line (or part of a line) that **Python completely ignores**. Comments are for **humans**—they explain what your code does, why you wrote it a certain way, or what you're planning to do next.

**How to write a comment:**

```python
# This is a comment
print("This is code")  # This is also a comment (after the code)
```

Anything after a `#` symbol on that line is a comment. Python skips right over it.

**Why do we write comments?**

Let me give you a few scenarios:

1. **Explaining intent:**
   ```python
   # Ask the user for their name (we'll learn input() later)
   # For now, we'll just print a greeting
   print("Hello, student!")
   ```

2. **Documenting assumptions:**
   ```python
   # This assumes the file is in the same directory
   # and uses UTF-8 encoding
   ```

3. **Leaving notes for yourself:**
   ```python
   # TODO: Add error handling here
   print("Processing data...")
   ```

4. **Explaining "why," not "what":**
   
   **Bad comment (states the obvious):**
   ```python
   # Print hello world
   print("Hello, world!")
   ```
   
   **Good comment (explains context):**
   ```python
   # Display welcome message to confirm the program started
   print("Hello, world!")
   ```

**[Important principle]:** Good code should be readable without comments. **Comments explain "why" you did something**, especially when it's not obvious. They don't just repeat what the code already says.

### When Should Beginners Use Comments?

**[Instructor speaks:]**

As you're learning, I recommend commenting more than you might need to. It helps you:

- Organize your thoughts before you code
- Remember what you were trying to do when you come back later
- Communicate with instructors and peers when asking for help

In this course, we'll ask you to include:

1. **A header comment** at the top of each file:
   ```python
   # Greeter program
   # Prints a personalized greeting message
   # Author: [Your Name]
   ```

2. **Section comments** if your script has distinct parts:
   ```python
   # Display welcome message
   print("Welcome!")
   
   # Show instructions
   print("Follow the prompts below.")
   ```

3. **Explanatory comments** when you try something new or tricky

**Don't comment the obvious, but do comment the "why."**

---

### Multi-Line Comments (Bonus Tip)

**[Instructor speaks:]**

Python doesn't have a special syntax for multi-line comments, but there are two common approaches:

**Option 1: Multiple # symbols**
```python
# This is a longer explanation
# that spans multiple lines
# to describe something complex
print("Hello!")
```

**Option 2: Triple-quoted strings (unofficial)**
```python
"""
This is technically a string, not a comment.
But if it's not assigned to anything, Python ignores it.
Some people use this for multi-line documentation.
"""
print("Hello!")
```

The triple-quote approach is more commonly used for **docstrings** (documentation strings) at the start of functions, which we'll cover later. For now, stick with `#` for comments.

---

## Section 3: Python Syntax Rules & Style Standards (5 minutes)

### Understanding Syntax vs. Style

**[Instructor speaks:]**

Before we start making mistakes (intentionally!), let's talk about two different kinds of rules in Python:

**1. Syntax Rules (You MUST follow these)**

These are the rules that make Python able to understand your code. Break these, and Python will give you an error. Examples:

- String literals must have matching quotes: `"hello"` not `"hello'`
- Functions need parentheses: `print()` not `print`
- Indentation must be consistent (more on this in a moment)

**2. Style Rules (You SHOULD follow these)**

These are conventions that make your code readable and professional. Break these, and Python will still run your code—but other programmers (including future you) will have a harder time reading it. Examples:

- Use 4 spaces for indentation (not 2, not tabs)
- Use descriptive variable names: `user_name` not `x`
- Add comments to explain non-obvious decisions

### The Style Standard for This Course

**[Instructor speaks:]**

Let's establish our style standard now. These rules will apply to everything you write in this course:

#### 1. Indentation: 4 Spaces (No Tabs)

Python uses indentation to group code (unlike languages that use braces like `{}`). This means **whitespace matters** in Python.

**Our rule:** Use **4 spaces** for each level of indentation. Do not use Tab characters.

**Why?** Tab characters can display differently in different editors. Four spaces is the Python community standard (PEP 8).

**[Practical tip]:** Most modern code editors can be configured to insert 4 spaces when you press the Tab key. Check your editor's settings.

Right now, you won't need indentation yet (that comes with functions and loops), but start the habit early.

#### 2. Naming: snake_case and Descriptive

When you name things in Python (variables, functions, files), use **lowercase letters with underscores** between words:

**Good:**
```python
user_name
calculate_average
my_first_program.py
```

**Avoid:**
```python
UserName      # This is camelCase (used in some other languages)
username      # Not wrong, but harder to read if it's multi-word
my-program.py # Hyphens cause problems (Python sees them as subtraction)
```

**Be descriptive.** Names should tell you what something is or does:

- `count` is better than `c`
- `total_price` is better than `tp`
- `greeting_message` is better than `msg`

Exception: In very small examples, short names like `i`, `x`, or `n` are acceptable when the context is obvious.

#### 3. Output: Prefer f-strings for Readability

When you need to mix text and values, use **f-strings** (formatted string literals):

```python
name = "Alice"
age = 30

# f-string (preferred)
print(f"My name is {name} and I am {age} years old.")

# Alternative (also works, but less readable)
print("My name is", name, "and I am", age, "years old.")
```

**Why f-strings?** They're more readable and flexible. We'll use them throughout the course.

**Note:** f-strings require Python 3.6+, which you have in the lab.

#### 4. Comments: Explain "Why," Not "What"

We already covered this, but to reiterate:

**Good comment:**
```python
# Use lowercase to match database format
name = name.lower()
```

**Unnecessary comment:**
```python
# Convert name to lowercase
name = name.lower()
```

The code already says "convert to lowercase." The good comment explains **why** we're doing it.

**[Action item]:** Bookmark or write down these style rules. We'll reinforce them every time you write code.

---

### Why Indentation and Whitespace Matter in Python

**[Instructor speaks:]**

Let me emphasize something unique about Python: **indentation is part of the syntax**.

In many programming languages, indentation is just for human readability. In Python, **it actually changes how the code runs**.

Here's a preview (you'll see this in action when we learn functions and loops):

**Example (you don't need to understand this fully yet):**

```python
# Correctly indented
if True:
    print("This will run")
    print("This will also run")
```

```python
# Incorrectly indented (ERROR!)
if True:
    print("This will run")
  print("This will NOT run - indentation error!")
```

The second example will crash because the indentation is inconsistent.

**Why does Python do this?** It forces you to write clean, readable code. You can't be sloppy with structure in Python—the language won't let you.

**For now:** You don't need to indent anything yet (we're writing simple scripts). But when we get to functions and control flow, indentation will be critical.

**[Quick check]:** Can anyone tell me: if Python uses 4 spaces for indentation, what happens if you use 2 spaces on one line and 4 on another?

[Wait for answers]

Right—Python will give you an `IndentationError`. Consistency is key.

---

## Section 4: Live Demo – Common Mistakes and How to Read Errors (5-10 minutes)

### The Safe Space for Errors

**[Instructor speaks:]**

Alright, this is my favorite part of Hour 2. We're going to **deliberately break things** and learn to read the error messages.

I want you to shift your mindset right now: **errors are not failures. Errors are feedback.**

When Python gives you an error, it's trying to help you. It tells you:
1. **What** went wrong
2. **Where** it went wrong (file and line number)
3. Often, **why** it went wrong

Let's make some mistakes together.

---

### Mistake #1: Missing Closing Quote

**[Instructor live-codes this:]**

```python
print("Hello, world!)
```

**[Run it]**

Error message:
```
  File "demo.py", line 1
    print("Hello, world!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

**[Instructor speaks:]**

Okay, let's read this error message together:

- **`File "demo.py", line 1`**: It's telling us the file and line number where the error occurred.
- **The caret (`^`)**: Python is pointing to where it got confused.
- **`SyntaxError: unterminated string literal`**: This is the error type and description.

**"Unterminated string literal"** means: "You started a string with a quote, but you never closed it."

**How to fix it:** Add the closing double quote:

```python
print("Hello, world!")
```

**[Run it]** – Now it works!

**[Key lesson]:** When you see `SyntaxError: unterminated string literal`, **look for mismatched quotes**.

---

### Mistake #2: Mismatched Quotes

**[Instructor live-codes this:]**

```python
print("Hello, world!')
```

**[Run it]**

Error message:
```
  File "demo.py", line 1
    print("Hello, world!')
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

**[Instructor speaks:]**

Same error message! Python started reading a string with a double quote (`"`), so it's looking for another double quote to close it. When it hits the single quote (`'`), it doesn't recognize it as the closing quote.

**How to fix it:** Make sure your opening and closing quotes match:

```python
print("Hello, world!")
```

Or:

```python
print('Hello, world!')
```

Both are fine—just be consistent.

---

### Mistake #3: Missing Parentheses

**[Instructor live-codes this:]**

```python
print "Hello, world!"
```

**[Run it]**

Error message:
```
  File "demo.py", line 1
    print "Hello, world!"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

**[Instructor speaks:]**

This is a **fantastic** error message! Python is literally telling us what to do: **"Did you mean print(...)?**"

In Python 2 (which is now obsolete), you could write `print "Hello"` without parentheses. But in Python 3, `print` is a function, and functions **require** parentheses.

**How to fix it:**

```python
print("Hello, world!")
```

**[Key lesson]:** If you see `Missing parentheses in call to 'print'`, add parentheses around your argument.

---

### Mistake #4: Typo in the Function Name

**[Instructor live-codes this:]**

```python
pritn("Hello, world!")
```

**[Run it]**

Error message:
```
  File "demo.py", line 1
    pritn("Hello, world!")
    ^^^^^
NameError: name 'pritn' is not defined. Did you mean: 'print'?
```

**[Instructor speaks:]**

Another helpful error! Python is saying: **"I don't know what 'pritn' is. Did you mean 'print'?"**

`NameError: name 'X' is not defined` means Python encountered a word it doesn't recognize. Usually this is:

- A typo (like here)
- A variable you forgot to create
- A function you forgot to import

**How to fix it:** Correct the typo:

```python
print("Hello, world!")
```

**[Pro tip]:** Modern editors often highlight syntax errors as you type. If you see a red underline, hover over it—it might tell you what's wrong before you even run the code.

---

### Mistake #5: Smart Quotes (Copy/Paste Error)

**[Instructor live-codes this—may need to copy/paste from a Word doc or web page:]**

```python
print("Hello, world!")
```

Wait, that **looks** fine, right?

**[Run it]**

Error message:
```
  File "demo.py", line 1
    print("Hello, world!")
          ^
SyntaxError: invalid character '"' (U+201C)
```

**[Instructor speaks:]**

Aha! See that error? **`invalid character`**. The issue is that those quotes aren't the "straight quotes" Python expects—they're "curly quotes" or "smart quotes" that word processors and some websites use.

**How to identify this:** Look closely at the quotes. If they're curved (`"` and `"` instead of straight `"`), that's the problem.

**How to fix it:** Retype the quotes inside your code editor (don't copy/paste from Word, Google Docs, or web pages):

```python
print("Hello, world!")
```

**[Key lesson]:** Always write code in a **plain text editor or IDE**, never in a word processor. If you copy code from the web, be careful of smart quotes.

---

### Systematic Error Reading

**[Instructor speaks:]**

Let me give you a **process** for reading error messages. Use this every time you hit an error:

**Step 1: Find the line number**
- Look for `File "filename", line X`
- Go to that line in your code

**Step 2: Read the error type**
- `SyntaxError`: Something about how you wrote the code is wrong
- `NameError`: Python doesn't recognize a name you used
- `TypeError`: You're using the wrong type of data
- `IndentationError`: Your spacing is inconsistent

**Step 3: Read the description**
- Python often tells you exactly what's wrong: "unterminated string literal," "missing parentheses," etc.

**Step 4: Look at the caret (^)**
- The `^` points to where Python got confused. The actual mistake might be **just before** this spot.

**Step 5: Fix one thing at a time**
- Don't try to fix multiple errors at once
- Fix the first error, save, and run again
- Repeat

**[Key mindset]:** Errors are not punishments. They're **helpful feedback**. Python is on your side.

---

### Demo Recap

**[Instructor speaks:]**

In the last 10 minutes, we deliberately made five common mistakes:

1. **Missing closing quote** → `SyntaxError: unterminated string literal`
2. **Mismatched quotes** → Same error
3. **Missing parentheses** → `SyntaxError: Missing parentheses in call to 'print'`
4. **Typo in function name** → `NameError: name 'pritn' is not defined`
5. **Smart quotes** → `SyntaxError: invalid character`

You'll make all of these errors (and more) as you learn. That's normal. The difference now is **you know how to read the feedback and fix it**.

---

## Section 5: Hands-On Lab – Greeter Program (25-35 minutes)

### Lab Overview

**[Instructor speaks:]**

Now it's your turn. You're going to write a program called **Greeter** that:

1. Prints a 3-line greeting message
2. Includes a comment at the top describing what the program does
3. **Intentionally creates a syntax error**, reads the message, and fixes it

This last part is key: **you're going to make a mistake on purpose and practice debugging it**. This is a safe space to fail and learn.

---

### Lab Instructions

**[Display these on screen or provide them in writing:]**

#### Part 1: Create the File

1. In your lab environment, navigate to your `python_basics` folder.
2. Create a new file called `greeter.py`.
3. Open it in your text editor.

#### Part 2: Write the Greeting (10 minutes)

Write a Python script that:

1. **Starts with a header comment** (3-4 lines) that includes:
   - The program name
   - A brief description of what it does
   - Your name

2. **Prints a 3-line greeting.** The greeting should be friendly and personalized. For example:
   ```
   Welcome to Python Basics!
   I'm excited to learn with you.
   Let's write some code together!
   ```

   You can write anything you want, but it must be **three separate print statements** (not one multi-line string).

3. **Add a blank line** between the header comment and the code for readability.

**Expected output when you run it:**

```
Welcome to Python Basics!
I'm excited to learn with you.
Let's write some code together!
```

**[Instructor note]:** Walk around and check on progress. Common issues:

- Forgetting quotes around strings
- Forgetting parentheses on `print()`
- Using smart quotes (if copying from somewhere)

---

#### Part 3: Intentional Error Practice (10 minutes)

Now here's the debugging practice:

1. **Deliberately introduce a syntax error.** Pick one:
   - Remove a closing quote
   - Remove a closing parenthesis
   - Misspell `print`
   - Mix single and double quotes

2. **Save the file and try to run it.**

3. **Read the error message carefully.** Write down (on paper or in a comment):
   - What type of error it is (e.g., SyntaxError)
   - What line number it points to
   - What the description says

4. **Fix the error** based on what the message tells you.

5. **Run it again** to confirm it works.

**[Instructor speaks:]**

The goal here is to **get comfortable with failure**. In real programming, you'll run your code dozens of times while fixing little issues. This is normal workflow.

---

#### Part 4: Style Check (5 minutes)

Before you consider yourself done, check these style requirements:

- ✅ Your file is named `greeter.py` (lowercase, underscore, `.py` extension)
- ✅ You have a header comment at the top
- ✅ Your code uses **double quotes** for strings (consistent style)
- ✅ You have **no trailing whitespace** (extra spaces at the end of lines)
- ✅ Your code is readable and properly spaced

**[Instructor note]:** Emphasize that "done" doesn't just mean "it runs." It means "it runs AND it's clean."

---

### Completion Criteria

You're done with the lab when:

1. ✅ Your program prints **exactly 3 lines** of output
2. ✅ You have a **header comment** that describes the program
3. ✅ You successfully **created and fixed** a syntax error
4. ✅ You can **explain** what the error was and how you fixed it

**[Instructor speaks:]**

When you're done, **don't close your file yet**. We're going to do a quick debrief and talk about what you learned.

---

### Optional Extensions (For Fast Finishers)

**[Instructor speaks:]**

If you finish early and want an extra challenge, try these extensions. These are **completely optional**—if you're still working on the main lab, stay focused on that.

#### Extension 1: ASCII Box Around Your Greeting

Use print statements to create a simple text-based box around your greeting:

**Example output:**
```
*********************************
* Welcome to Python Basics!     *
* I'm excited to learn with you.*
* Let's write some code!        *
*********************************
```

**Hint:** You'll need to manually count spaces to align the text. Don't worry about making it perfect—just experiment!

#### Extension 2: Add More Information

Add two more lines to your greeting that print:
- The current Python version (you can hard-code "Python 3.11" or whatever version you have)
- The course name

Example:
```
Welcome to Python Basics!
I'm excited to learn with you.
Let's write some code together!
You are using Python 3.11.
This is the Basics course from LogicalChoice.
```

#### Extension 3: Use f-strings (Preview)

If you're feeling adventurous, try using an **f-string** to include a variable in your output.

Example:

```python
# Greeter with f-string
# Demonstrates formatted output

course_name = "Python Basics"

print(f"Welcome to {course_name}!")
print("I'm excited to learn with you.")
print("Let's write some code together!")
```

**Note:** We'll cover variables formally in Hour 3. For now, just try copying this pattern and see what happens!

---

### Common Pitfalls & Troubleshooting

**[Instructor speaks:]**

As you work, here are the most common issues I'll be helping you with:

#### Issue 1: "My file won't run"

**Symptoms:**
- Terminal says "No such file or directory"
- OR you're running it but seeing old output

**Likely causes:**
- You're not in the `python_basics` folder. Check with `pwd` and navigate with `cd`.
- You didn't save the file. Save (Ctrl+S or Cmd+S) and try again.
- You named the file something other than `greeter.py`. Check with `ls`.

**How to check:**
```bash
pwd               # Where am I?
ls                # What files are here?
python greeter.py # Run the file
```

---

#### Issue 2: "I get an error but I don't see any mistakes"

**Symptoms:**
- Code looks right but Python disagrees

**Likely causes:**
- **Smart quotes** (curly instead of straight)
- **Trailing/leading spaces** where they shouldn't be
- **Invisible characters** from copy/paste

**How to fix:**
- Retype the quotes manually inside your editor
- Delete and retype the entire line
- Don't copy/paste from Word, Google Docs, or web browsers

---

#### Issue 3: "Python is printing weird characters"

**Symptoms:**
- Output has strange symbols or boxes

**Likely causes:**
- File encoding issue (rare in the lab, but possible)

**How to fix:**
- Make sure your editor is set to save files as **UTF-8 encoding**
- Avoid using emoji or special symbols in your code (for now)

---

#### Issue 4: "I intentionally broke it but now I can't fix it"

**Symptoms:**
- You introduced an error for Part 3, but now you're stuck

**How to fix:**
- Read the error message line by line (use the 5-step process from the demo)
- If you're really stuck, look at your working code from Part 2 and compare
- Ask for help! That's what I'm here for

**[Reassurance]:** Everyone gets stuck sometimes. Learning to ask for help clearly is a skill too.

---

### Instructor Circulation Notes

**[For instructors—don't read this aloud, but keep it in mind:]**

While students are working, circulate and watch for:

1. **Incorrect file location**: Students saving files outside `python_basics/`.
2. **Not saving before running**: A super common mistake.
3. **Confusion between the editor and terminal**: Some students try to run code in the editor's text area.
4. **Copy/paste from outside sources**: Leading to smart quotes or formatting issues.
5. **Perfectionism paralysis**: Students stuck on "what should my greeting say?" Encourage them to just write anything and move on.

**Common questions you'll get:**

- **"Can I print more than 3 lines?"** → Yes, but meet the minimum first.
- **"Does my greeting have to be about Python?"** → Nope, any greeting is fine.
- **"Can I use single quotes?"** → Yes, but be consistent. We prefer double quotes in this course.
- **"What if I can't think of an error to create?"** → Suggest removing a quote or parenthesis—simple and fast.

**Praise specifically:**

- "Great job reading that error message!"
- "I love how descriptive your comment is!"
- "Nice, clean formatting!"

---

## Section 6: Debrief & Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

Alright, let's come back together. Hopefully your greeter is working and you've successfully broken and fixed something!

**Let's do a quick share-out.** I want to hear:

1. **What error did you create?**
2. **What did the error message say?**
3. **How did you fix it?**

[Call on 3-4 volunteers to share. Affirm their answers and clarify if needed.]

**[After a few shares, say:]**

Thank you for sharing! Notice a pattern here? **Different errors, but all fixable.** And Python told you what was wrong in every case.

This is the core skill you're building: **run code → read feedback → fix → repeat**. That cycle is programming.

---

### Key Takeaways from Hour 2

**[Instructor speaks:]**

Let me recap what we covered this hour:

1. **`print()` is your main tool for output.** It takes strings (text in quotes) and displays them.

2. **Comments use `#` and are for humans, not Python.** Use them to explain your intent, especially the "why" behind your code.

3. **Python has strict syntax rules:**
   - Strings need matching quotes
   - Functions need parentheses
   - Indentation must be consistent (we'll see this more in future hours)

4. **Error messages are your friends.** They tell you:
   - What went wrong
   - Where it happened
   - Often, how to fix it

5. **Style matters.** Use 4 spaces, descriptive names, consistent quotes, and clear comments.

**[Key mindset shift]:** You are now comfortable making mistakes, reading errors, and fixing them. That's huge!

---

### Exit Ticket: Quick Check

**[Instructor speaks:]**

Before we wrap up, one quick check. I want you to think about this question (you can answer mentally, or write it down if you prefer):

**"Why is whitespace and indentation important in Python?"**

[Pause for 10 seconds]

Here's the answer: **In Python, indentation is part of the syntax.** It tells Python how to group statements together. Unlike other languages where indentation is just for humans, in Python, **it changes how the code runs**.

Right now, you're writing simple scripts without indentation, but when we get to functions, loops, and conditionals, indentation will be critical. Inconsistent indentation will cause errors.

**[Key principle]:** Python forces you to write clean, readable code. That's by design, and it's one of the reasons Python code is so easy to read compared to other languages.

---

### Looking Ahead to Hour 3

**[Instructor speaks:]**

Next hour, we're going to level up. We'll learn about **variables**—how to store data and reuse it—and we'll explore the main **data types** in Python: strings, numbers, and booleans.

By the end of Hour 3, you'll be able to write programs that:
- Store and manipulate information
- Perform calculations
- Make decisions based on data types

But for now, take a break! Stretch, get some water, and come back ready to build on what you learned today.

**Great work, everyone!**

---

## Appendix: Quick Reference for Instructors

### Hour 2 Learning Objectives (Checklist)

By the end of Hour 2, students should be able to:

- ✅ Write a `print()` statement with a string literal
- ✅ Use both single and double quotes correctly
- ✅ Write a single-line comment using `#`
- ✅ Explain when and why to write comments
- ✅ Identify common syntax errors from error messages
- ✅ Follow the 5-step process for reading error messages
- ✅ Apply basic style standards (4-space indentation, snake_case, consistent quotes)
- ✅ Deliberately create and fix a syntax error

---

### Common Student Misconceptions to Address

1. **"Errors mean I'm bad at this."**
   - **Correction:** Errors are feedback, not failure. Professionals get errors constantly.

2. **"I need to memorize all the syntax."**
   - **Correction:** You'll internalize syntax through practice. For now, focus on understanding the patterns.

3. **"Comments slow me down."**
   - **Correction:** Comments save time later when you (or others) read your code.

4. **"Python is picky about spaces."**
   - **Reality check:** Yes, Python is strict about indentation. But this is a feature, not a bug—it keeps code clean.

5. **"If my code runs, it's correct."**
   - **Correction:** Code can run and still be poorly written. Aim for code that's correct, readable, and maintainable.

---

### Troubleshooting: Most Common Lab Issues

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|-----------------|---------|
| `No such file or directory` | Not in the right folder, or file not saved | Check with `pwd`, navigate with `cd python_basics`, save file |
| `SyntaxError: unterminated string literal` | Missing or mismatched quote | Add closing quote or match opening quote |
| `SyntaxError: invalid character` | Smart quotes from copy/paste | Retype quotes in editor |
| `NameError: name 'X' is not defined` | Typo, or forgot quotes around a string | Check spelling, or add quotes if it's text |
| `SyntaxError: Missing parentheses in call to 'print'` | Forgot parentheses on print() | Add parentheses: `print("text")` |
| Output doesn't match what student expected | Logic issue, or didn't save before running | Review code logic, ensure file is saved |

---

### Timing Adjustments

If you're running behind:

- **Shorten the live demo** to 3 mistakes instead of 5 (keep #1, #3, and #4)
- **Skip the optional extensions** (or mention them as homework)
- **Reduce debrief time** to 3 minutes with just 1-2 share-outs

If you're ahead of schedule:

- **Expand the live demo** with an additional error (e.g., missing colon later when relevant)
- **Do a live code review** of a student's greeter with their permission
- **Introduce the concept of escape characters** briefly (`\n`, `\t`, `\\`, `\"`)

---

### Additional Resources for Students

**For further reading (optional):**

- Python's official style guide (PEP 8): [https://pep8.org](https://pep8.org)
- Built-in functions documentation: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
- Real Python's guide to print(): [https://realpython.com/python-print/](https://realpython.com/python-print/)

**Practice exercises (for after class):**

1. Write a program that prints a simple ASCII art picture (a smiley face, a house, etc.)
2. Create a program with 10 different print statements, then add comments to group them logically
3. Deliberately create 5 different types of errors, screenshot the error messages, and fix them

---

## End of Hour 2 Lecture Script

**Total Word Count:** ~5,000 words

**Instructor Note:** This script is designed to be read verbatim or adapted to your teaching style. The timing suggestions are approximate—adjust based on your class's pace and engagement level. Prioritize student understanding over covering every word.

**Remember:** The goal of Hour 2 is not perfection. The goal is for students to feel **comfortable with the basics** and **confident that errors are fixable**. If they leave this hour thinking, "I can write a simple program and debug it," you've succeeded.

---

**[END OF LECTURE SCRIPT]**
