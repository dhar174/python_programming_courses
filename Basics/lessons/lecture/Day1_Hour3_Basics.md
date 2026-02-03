# Day 1, Hour 3: Variables + Basic Types
## Python Basics Course - Lecture Script

**Session:** Day 1 (Session 1), Hour 3 of 4  
**Duration:** 60 minutes  
**Prerequisites:** Hour 1 (Environment setup) and Hour 2 (print(), comments, reading errors)

---

## Overview & Learning Outcomes

**What students will be able to do by the end of this hour:**
- Create variables and assign values
- Use `type()` to inspect what kind of value a variable holds
- Explain the difference between strings, numbers, and booleans
- Apply Python's naming rules when creating identifiers
- Reassign variables and understand the "read from right to left" mental model

---

## Hour Structure

- **Recap & Bridge** (3-5 minutes)
- **Instructor Talk: Variables & Types** (10-15 minutes)
- **Live Demo: Profile Card** (5-10 minutes)
- **Hands-on Lab: Profile Card** (25-35 minutes)
- **Wrap-up & Quick Check** (5 minutes)

---

## Section 1: Recap & Bridge from Hour 2
### Timing: 3-5 minutes

**[Speaking cues: Energetic, welcoming tone. Acknowledge the transition.]**

Alright everyone, welcome back! We're now in Hour 3 of Day 1, and we're about to take a major step forward in our Python journey.

Let's do a quick recap of where we've been. In Hour 1, we got our environment set up—we made sure Python was installed, we created our workspace folder, and we ran our very first script. In Hour 2, we learned how to use `print()` to send output to the screen, we added comments to document our code, and most importantly, we practiced reading error messages. By now, you should feel comfortable running a Python script and troubleshooting basic syntax errors.

**[Pause for acknowledgment]**

Today, in Hour 3, we're going to introduce one of the most fundamental concepts in all of programming: **variables**. If you've never programmed before, think of this hour as unlocking the ability to *remember* information in your programs. Up until now, every time we printed something, we typed it directly into the `print()` function. That works, but it's limiting. What if we want to use the same piece of information multiple times? What if we want to change it in one place and have that change reflected everywhere? That's where variables come in.

By the end of this hour, you'll be able to store information—like names, numbers, and true/false values—and reuse them throughout your programs. This is a game-changer.

**[Transition cue]**

Let's dive in.

---

## Section 2: Instructor Talk – Variables & Basic Types
### Timing: 10-15 minutes

### Part A: What is a Variable? (3-4 minutes)

**[Speaking cues: Use a metaphor to ground the concept.]**

So, what *is* a variable? 

Think of a variable as a **labeled box**. You can put something inside the box, and you can write a label on the outside so you remember what's in there. Later, when you need that thing, you just look at the label and open the box.

In Python, a variable is a name that points to a value. We create a variable by using the **assignment operator**, which is the equals sign: `=`.

Here's the simplest example:

```python
name = "Alex"
```

Let me break this down word by word:
- `name` is the **variable name** (or what we call an "identifier")
- `=` is the **assignment operator** (it means "assign the value on the right to the name on the left")
- `"Alex"` is the **value** we're storing—in this case, a string

After this line runs, whenever we use the word `name` in our code, Python will substitute in the value `"Alex"`.

Let's see it in action:

```python
name = "Alex"
print(name)
```

**Expected output:**
```
Alex
```

Notice we didn't write `print("name")`—that would print the word "name" literally. We wrote `print(name)` without quotes, so Python looks up the value associated with `name` and prints *that*.

**[Check for understanding]**

Does that make sense so far? Variables are names that hold values. We assign values to variables using `=`.

---

### Part B: The Mental Model—Read from Right to Left (2 minutes)

**[Speaking cues: Emphasize this as a key insight.]**

Here's a mental model that will serve you well throughout your Python journey: when you see an assignment statement, **read it from right to left**.

```python
age = 25
```

Don't read this as "age equals 25." Instead, read it as: **"Take the value 25 and assign it to the variable named age."**

Why does this matter? Because assignment is not the same as equality in mathematics. In math, when we write `x = 5`, we're saying x *is* 5. In Python, we're saying: "From now on, whenever I say `x`, I mean the value 5."

And here's the powerful part: we can *change* what a variable holds. This is called **reassignment**.

```python
age = 25
print(age)  # Prints 25

age = 26
print(age)  # Prints 26
```

The variable `age` first held `25`, then we reassigned it to hold `26`. The old value is gone—it's been replaced.

**[Pause]**

So remember: right to left. Take the value on the right, store it in the variable on the left.

---

### Part C: Naming Rules and Conventions (3-4 minutes)

**[Speaking cues: Transition to practical rules.]**

Now, you can't just name a variable anything you want. Python has rules. Let's talk about what makes a valid **identifier**—that's the formal term for a variable name.

**Rules (these are enforced by Python):**

1. **Must start with a letter or underscore** (`a-z`, `A-Z`, `_`)
   - ✅ `name`, `_temp`, `user1`
   - ❌ `1user` (can't start with a number)
   - ❌ `@name` (can't start with special characters)

2. **Can contain letters, numbers, and underscores**
   - ✅ `first_name`, `age2`, `total_score`
   - ❌ `first-name` (hyphens are not allowed)
   - ❌ `total score` (spaces are not allowed)

3. **Case-sensitive**
   - `Name`, `name`, and `NAME` are three different variables

4. **Cannot be a reserved keyword**
   - Python has special words like `if`, `for`, `while`, `def`, `class`, `return`, etc.
   - You can't name a variable `if` or `for`—Python uses those for other things

**Conventions (these are best practices):**

In Python, we follow a style guide called **PEP 8**. For variable names, the convention is:

- Use **snake_case**: all lowercase, with underscores separating words
  - ✅ `first_name`, `total_score`, `is_active`
  - Not recommended: `firstName` (that's camelCase, used in JavaScript), `FirstName` (that's PascalCase, used for classes)

- Use **descriptive names**
  - ✅ `student_count`, `max_temperature`
  - ❌ `x`, `temp`, `var1` (unless in a very small, obvious context)

Good variable names make your code readable. When you come back to your code in a week, you want to understand what `student_count` means. If you just called it `n`, you might forget.

**[Check for understanding]**

So: letters, numbers, underscores. Start with a letter or underscore. Use snake_case. Be descriptive. Any questions on naming?

---

### Part D: Basic Types—Strings, Numbers, Booleans (4-5 minutes)

**[Speaking cues: Introduce the concept of "types" as categories of data.]**

Okay, so we can store values in variables. But not all values are the same. Python categorizes values into different **types**. Think of a type as the "kind" of data you're working with.

In this hour, we're going to focus on three fundamental types:

#### 1. Strings (`str`)

A **string** is a sequence of characters—text. You create a string by wrapping text in quotes: single quotes `'...'` or double quotes `"..."`.

```python
name = "Jordan"
city = 'Seattle'
message = "Hello, world!"
```

Strings are for text: names, addresses, messages, anything you'd write or read as words.

#### 2. Numbers—Integers and Floats (`int` and `float`)

Numbers in Python come in two main flavors:

- **Integers** (`int`): whole numbers, no decimal point
  ```python
  age = 30
  year = 2024
  score = -5
  ```

- **Floats** (`float`): numbers with a decimal point
  ```python
  temperature = 72.5
  price = 19.99
  pi_approx = 3.14159
  ```

Notice: no quotes around numbers. If you write `"30"`, that's a string, not a number.

#### 3. Booleans (`bool`)

A **boolean** is a value that's either `True` or `False`. (Notice the capital T and F—Python is case-sensitive!)

```python
is_raining = True
has_permission = False
likes_python = True
```

Booleans are used to represent yes/no, on/off, true/false conditions. We'll use them a lot when we get to conditional logic (if statements) in future sessions.

---

**[Speaking cues: Introduce the `type()` function.]**

So how do you know what type a value is? Python gives us a built-in function called `type()`. It tells you the type of whatever you pass to it.

```python
name = "Jordan"
age = 30
temperature = 72.5
is_student = True

print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(temperature))  # <class 'float'>
print(type(is_student))   # <class 'bool'>
```

When you run this, you'll see output like `<class 'str'>`. Don't worry about the word "class" for now—just focus on the second part: `'str'`, `'int'`, `'float'`, `'bool'`. Those are the type names.

**[Key point]**

Here's something really important: in Python, the type is determined by the *value*, not by the variable name. A variable can hold any type, and you can even reassign it to a different type (though we generally try to avoid that because it can be confusing).

```python
x = 10        # x is an int
print(type(x))  # <class 'int'>

x = "hello"   # now x is a str
print(type(x))  # <class 'str'>
```

This is called **dynamic typing**. The variable doesn't have a fixed type—the value does.

---

### Part E: Quick Concept Check—String vs Number (1 minute)

**[Speaking cues: Pose a prediction question.]**

Before we move to the demo, let me ask you a quick question to check understanding:

**What's the difference between `'5'` and `5`?**

Think about it for a moment.

**[Pause for thought]**

The answer: `'5'` (in quotes) is a **string**. It's the character "5"—text. You can't do math with it directly. `5` (no quotes) is an **integer**. It's the number five—you *can* do math with it.

This is a common source of confusion for beginners. If you see quotes, it's a string. No quotes (and it looks like a number), it's a number.

```python
x = '5'
y = 5

print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
```

**[Transition cue]**

Alright, let's see all of this in action with a live demo.

---

## Section 3: Live Demo – Building a Profile Card
### Timing: 5-10 minutes

**[Speaking cues: Switch to your IDE or terminal. Narrate as you type.]**

I'm going to create a new file called `profile_demo.py` in my `python_basics` folder. Watch what I do, and I'll explain each step.

**[Begin typing and narrating]**

```python
# profile_demo.py
# A simple profile card using variables

name = "Taylor"
city = "Austin"
age = 28
favorite_number = 7
likes_python = True
```

Okay, I've created five variables. Let me walk through them:

- `name` holds the string `"Taylor"`
- `city` holds the string `"Austin"`
- `age` holds the integer `28`
- `favorite_number` holds the integer `7`
- `likes_python` holds the boolean `True`

Now, let's print out a formatted profile card using these variables:

```python
print("=== Profile Card ===")
print("Name:", name)
print("City:", city)
print("Age:", age)
print("Favorite Number:", favorite_number)
print("Likes Python:", likes_python)
print("====================")
```

**[Run the script]**

Let me run this and see what we get:

```
=== Profile Card ===
Name: Taylor
City: Austin
Age: 28
Favorite Number: 7
Likes Python: True
====================
```

Beautiful! Notice how we're reusing the variable names multiple times. If I wanted to change the name, I'd only need to change it in one place—the assignment line—and everywhere I print `name`, it would reflect the new value.

**[Speaking cues: Demonstrate reassignment.]**

Let me show you reassignment in action. I'll add a few lines to change some values:

```python
print("\nUpdating profile...")
age = 29
city = "Denver"

print("\n=== Updated Profile Card ===")
print("Name:", name)
print("City:", city)
print("Age:", age)
print("Favorite Number:", favorite_number)
print("Likes Python:", likes_python)
print("============================")
```

**[Run again]**

Now when I run it:

```
=== Profile Card ===
Name: Taylor
City: Austin
Age: 28
Favorite Number: 7
Likes Python: True
====================

Updating profile...

=== Updated Profile Card ===
Name: Taylor
City: Denver
Age: 29
Favorite Number: 7
Likes Python: True
============================
```

See? The age changed from 28 to 29, and the city changed from Austin to Denver. The variables were reassigned, and when we printed them again, we got the new values.

**[Speaking cues: Demonstrate `type()` function.]**

Now let's use `type()` to inspect each of our variables:

```python
print("\n=== Type Information ===")
print("Type of name:", type(name))
print("Type of city:", type(city))
print("Type of age:", type(age))
print("Type of favorite_number:", type(favorite_number))
print("Type of likes_python:", type(likes_python))
```

**[Run again]**

```
=== Type Information ===
Type of name: <class 'str'>
Type of city: <class 'str'>
Type of age: <class 'int'>
Type of favorite_number: <class 'int'>
Type of likes_python: <class 'bool'>
```

Perfect! We can see that `name` and `city` are strings, `age` and `favorite_number` are integers, and `likes_python` is a boolean.

**[Speaking cues: Highlight the key takeaway.]**

So the key takeaway from this demo: variables let us store information and reuse it. We can change the values (reassignment), and we can inspect what type of data we're working with using `type()`.

**[Transition cue]**

Now it's your turn! You're going to build your own profile card in the lab.

---

## Section 4: Hands-on Lab – Profile Card
### Timing: 25-35 minutes

**[Speaking cues: Provide clear instructions for the lab.]**

Alright, everyone, it's time for hands-on practice. Open up your IDE or terminal, navigate to your `python_basics` folder, and create a new file called `profile_card.py`.

### Lab Instructions

**Your task:**

1. **Create variables** for the following information about yourself (or a fictional person):
   - `name` (a string)
   - `city` (a string)
   - `favorite_number` (an integer)
   - `likes_python` (a boolean—`True` or `False`)

2. **Print a formatted profile card** that displays all four values. Make it look nice—use labels like "Name:", "City:", etc.

3. **Use `type()`** to print the type of each variable. Add a section at the end of your output that shows the type information.

### Completion Criteria

Your program should:
- ✅ Print all four values correctly
- ✅ Use clear, descriptive variable names (following snake_case convention)
- ✅ Include `type()` output for each variable
- ✅ Run without errors

### Example Output

Your output should look something like this (but with your own values):

```
=== My Profile Card ===
Name: Jordan Lee
City: Portland
Favorite Number: 42
Likes Python: True
========================

=== Type Information ===
Type of name: <class 'str'>
Type of city: <class 'str'>
Type of favorite_number: <class 'int'>
Type of likes_python: <class 'bool'>
```

**[Speaking cues: Set expectations and offer support.]**

You have about 25 minutes for this lab. Start simple—get the basic version working first. Once you've got that, we have some optional extensions if you finish early.

I'll be walking around to answer questions. Remember: if you get an error, *read the error message*. Look at the line number, read what it says, and try to figure out what went wrong. That's a skill we practiced in Hour 2, and it applies here too.

**[Pause for questions]**

Any questions before you start?

**[While students work, circulate and provide support. Use the following guidance.]**

---

### Common Pitfalls to Watch For

As you're helping students, keep an eye out for these common mistakes:

#### 1. **NameError from typos**

Students might define a variable as `name` but then try to print `Name` (with a capital N). Python is case-sensitive, so this will cause a `NameError`.

**How to address it:**
- Point to the error message: `NameError: name 'Name' is not defined`
- Ask: "Look at how you defined the variable. Is the capitalization the same?"
- Reinforce: "Python is case-sensitive. `name` and `Name` are different."

#### 2. **Using quotes when printing a variable**

Students might write `print("name")` instead of `print(name)`.

**How to address it:**
- Ask: "What does it print?"
- They'll say: "It prints the word 'name'."
- Explain: "Right. If you use quotes, Python treats it as literal text. If you want the *value* of the variable, leave off the quotes."

#### 3. **Accidentally overwriting a variable with a different type**

Students might write:
```python
favorite_number = 7
favorite_number = "seven"
```

This is legal in Python, but it's confusing.

**How to address it:**
- Ask: "What type is `favorite_number` now?"
- Run `type(favorite_number)` to show it's a string.
- Explain: "Python allows this, but it can be confusing. Generally, we try to keep a variable holding the same type of data. If you need a different type, consider using a different variable name."

#### 4. **Forgetting to assign a value before using it**

Students might try to print a variable they haven't created yet.

**How to address it:**
- Point to the error: `NameError: name 'age' is not defined`
- Ask: "Did you create the variable `age` before this line?"
- Reinforce: "Python reads your code from top to bottom. You have to assign a value to a variable before you can use it."

---

### Optional Extensions (for students who finish early)

**[Speaking cues: Announce these after about 15 minutes, or individually as students finish.]**

If you've completed the basic lab, here are some optional extensions to try:

#### Extension 1: Add a computed value

Add a variable called `next_favorite_number` that stores `favorite_number + 10`. Print it in your profile card.

```python
favorite_number = 42
next_favorite_number = favorite_number + 10

print("Favorite Number:", favorite_number)
print("Next Favorite Number:", next_favorite_number)
```

#### Extension 2: Add user input for one field

Use the `input()` function to ask the user for their name, rather than hard-coding it.

```python
name = input("Enter your name: ")
print("Name:", name)
```

**Note:** Keep this simple. We'll dive deeper into `input()` in future hours.

---

### Circulating Tips

As you walk around:
- **Ask guiding questions** rather than giving answers. "What does the error message say?" is better than "You forgot a quote."
- **Celebrate small wins.** "Great! You got the strings working. Now let's add the boolean."
- **Encourage experimentation.** "What do you think will happen if you change `likes_python` to `False`? Try it!"
- **Point out good practices.** "I like how you used a descriptive variable name—`favorite_number` is much clearer than `fav_num` or `fn`."

---

## Section 5: Lab Debrief & Common Pitfalls
### Timing: 5 minutes (before wrap-up)

**[Speaking cues: Call the class back together after lab time.]**

Alright, everyone, let's come back together. Hopefully you've got your profile card working!

Let me highlight a few common pitfalls I saw while walking around—these are things *everyone* runs into when learning variables, so if you hit any of these, you're in good company.

### Pitfall 1: Overwriting a Variable with a Different Type

Some of you might have written something like this:

```python
age = 28
age = "twenty-eight"
```

This is legal in Python—Python won't stop you. But it's confusing. Now `age` is a string, not a number. If you later try to do math with it, you'll get an error.

**Best practice:** If you need to store different types of data, use different variable names. For example:

```python
age = 28
age_text = "twenty-eight"
```

### Pitfall 2: NameError from Typos

Python is case-sensitive and spelling-sensitive. If you define `favorite_number` but then try to print `Favorite_Number` or `favourit_number`, Python will say: `NameError: name 'Favorite_Number' is not defined`.

**How to avoid this:** 
- Be consistent with your capitalization.
- If you get a NameError, check the spelling and capitalization of your variable name.
- Use your editor's autocomplete feature—it can help you avoid typos.

### Pitfall 3: Quotes Around Variable Names

If you write:

```python
name = "Alex"
print("name")
```

You'll see:
```
name
```

Not "Alex." Why? Because `"name"` in quotes is literal text—Python prints the word "name."

If you want the *value* of the variable, don't use quotes:

```python
print(name)  # Prints: Alex
```

**[Pause for questions]**

Did anyone run into other issues? [Allow 1-2 students to share.]

---

## Section 6: Wrap-up & Quick Check / Exit Ticket
### Timing: 3-5 minutes

**[Speaking cues: Summarize key concepts.]**

Alright, let's wrap up Hour 3. Here's what we covered today:

1. **Variables** are names that hold values. We create them using the assignment operator `=`.
2. We read assignment statements **from right to left**: "Take the value on the right and store it in the variable on the left."
3. **Identifiers** (variable names) must follow Python's naming rules: start with a letter or underscore, use letters/numbers/underscores, no spaces or special characters.
4. We follow **snake_case** convention for variable names in Python.
5. **Types** categorize data:
   - **Strings** (`str`): text, in quotes
   - **Integers** (`int`): whole numbers
   - **Floats** (`float`): numbers with decimals
   - **Booleans** (`bool`): `True` or `False`
6. We use the **`type()`** function to inspect the type of a value.

**[Transition to exit ticket]**

Before we move to Hour 4, I want you to answer a quick check question. This is your "exit ticket"—it helps me know what's landing and what might need reinforcement.

### Quick Check / Exit Ticket

**Question:** What's the difference between `'5'` and `5`?

**[Pause for students to think or write. Then provide the answer.]**

**Answer:**
- `'5'` (in quotes) is a **string**—the character "5", which is text. You can't do math with it directly.
- `5` (no quotes) is an **integer**—the number 5, which you *can* do math with.

This distinction is crucial. If you're ever confused about why something isn't working the way you expect, check the type with `type()`. You might be working with a string when you thought you had a number, or vice versa.

**[Final encouragement]**

Great work today, everyone. Variables are one of the foundational building blocks of programming. Now that you can store and reuse information, you're ready to start doing more interesting things—like math and calculations, which is exactly what we'll cover in Hour 4.

Take a quick stretch break, and we'll come back in a few minutes to dive into numbers and operators.

---

## Instructor Notes & Tips

### Time Management
- If the lab runs over, it's okay to shorten the debrief. The hands-on practice is more valuable than lecture time.
- If students finish the lab early, point them to the optional extensions.
- If students are struggling, consider doing a quick "live help" session where you debug one student's code on the projector with the class watching.

### Common Questions & Answers

**Q: "Can I use spaces in variable names?"**  
A: No. Use underscores instead. `first_name` not `first name`.

**Q: "Why do we use snake_case instead of camelCase?"**  
A: It's the Python convention (PEP 8). Different languages have different conventions. In Python, we use snake_case for variables and functions. It makes code more readable and consistent.

**Q: "Can I change a variable from an int to a string?"**  
A: Technically yes, but it's confusing and generally not recommended. If you need both, use two different variables.

**Q: "What's the difference between `=` and `==`?"**  
A: Great question! `=` is assignment (store a value). `==` is comparison (check if two values are equal). We'll cover `==` when we get to conditionals. For now, just know that `=` means "assign."

**Q: "Why does `type()` print `<class 'str'>` instead of just `str`?"**  
A: In Python, types are implemented as "classes" under the hood. For now, just focus on the part in quotes—that's the type name. We'll learn about classes much later in the course.

### Differentiation Strategies

**For students who are ahead:**
- Encourage them to experiment: "What happens if you add two strings together? Try `first_name + last_name`."
- Point them to type conversion: "Can you convert a string to an int? Try `int('5')` and see what happens."
- Challenge them to format output more creatively, perhaps using ASCII art.

**For students who are struggling:**
- Break the lab into smaller steps: "Let's just get one variable printed first. Then we'll add the second."
- Pair them with a peer who's a bit ahead.
- Sit with them and narrate what you're doing: "First, I'm going to create the variable. I'll type `name =` and then the value in quotes."

### Connection to Future Hours

Hour 3 sets the stage for:
- **Hour 4 (Numbers & Operators):** Now that we can store numbers in variables, we'll do math with them.
- **Session 2 (Conditionals):** We'll use boolean variables to make decisions (`if likes_python:`).
- **Session 3 (Loops):** We'll use variables to count and track progress in loops.
- **Session 4 (Functions):** We'll pass variables as arguments to functions.

Emphasize that variables aren't just a one-hour topic—they're a foundational concept that everything else builds on.

---

## Additional Resources for Instructors

### Helpful Analogies

**Variables as labeled boxes:**
"A variable is like a labeled box. You can put something inside (assign a value), you can look inside (use the variable), and you can replace what's inside (reassign a new value). The label (variable name) stays the same, but the contents can change."

**Assignment as right-to-left:**
"Think of `=` as an arrow pointing left: `age ← 25`. We're taking the value on the right and putting it into the variable on the left."

**Types as categories:**
"Types are like categories of data. Just like in real life, you wouldn't try to mail a letter in a shoebox—the type matters. You can't do math with a string, and you can't capitalize a number."

### Code Snippets for Quick Demos

**Reassignment:**
```python
x = 10
print(x)  # 10

x = 20
print(x)  # 20

x = x + 5
print(x)  # 25
```

**Type inspection:**
```python
value = 100
print(type(value))  # <class 'int'>

value = "one hundred"
print(type(value))  # <class 'str'>
```

**String vs number:**
```python
a = '5'
b = 5

print(a + a)  # '55' (string concatenation)
print(b + b)  # 10 (addition)
```

---

## Appendix: Full Demo Code

For your reference, here's the complete code from the live demo:

```python
# profile_demo.py
# A simple profile card using variables

# Initial variable assignments
name = "Taylor"
city = "Austin"
age = 28
favorite_number = 7
likes_python = True

# Print the profile card
print("=== Profile Card ===")
print("Name:", name)
print("City:", city)
print("Age:", age)
print("Favorite Number:", favorite_number)
print("Likes Python:", likes_python)
print("====================")

# Demonstrate reassignment
print("\nUpdating profile...")
age = 29
city = "Denver"

# Print updated profile
print("\n=== Updated Profile Card ===")
print("Name:", name)
print("City:", city)
print("Age:", age)
print("Favorite Number:", favorite_number)
print("Likes Python:", likes_python)
print("============================")

# Use type() to inspect types
print("\n=== Type Information ===")
print("Type of name:", type(name))
print("Type of city:", type(city))
print("Type of age:", type(age))
print("Type of favorite_number:", type(favorite_number))
print("Type of likes_python:", type(likes_python))
```

---

## End of Hour 3 Script

**Word Count:** ~4,800 words

**Prepared for:** Python Basics Course, Day 1, Session 1  
**Next Hour:** Hour 4 - Numbers + Operators

