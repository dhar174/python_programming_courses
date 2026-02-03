# Day 1, Hour 1: Orientation + Environment Readiness
**Python Programming Basics – Session 1**

---

## Timing Overview
**Total Time:** 60 minutes  
- Welcome & Course Overview: 5 minutes
- Platform Setup & Navigation: 10-15 minutes
- The "Why Python?" Conversation: 5 minutes
- Understanding Your Environment: 10 minutes
- Live Demo: 5-10 minutes
- Hands-On Lab: 25-35 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Successfully access the lab environment and launch your Python workspace
2. Understand the two-key redemption process and why it matters
3. Create a workspace folder following our course standards
4. Run your first Python script from both terminal and IDE
5. Explain the difference between the Python REPL and running a .py file
6. Adopt the "Save and Suspend" culture for lab persistence

---

## Section 1: Welcome & Course Overview (5 minutes)

### Opening

**[Instructor speaks:]**

Welcome, everyone! I'm so excited to have you here for Python Programming Basics. Whether you're completely new to programming or you've dabbled a bit and want a solid foundation, you're in the right place.

Let me start by saying something important: **learning to code is a skill, not a talent.** It's something you build through practice, mistakes, and small wins. Over the next 48 hours together, we're going to build that skill step by step.

### What This Course Is (and Isn't)

This is a 48-hour course delivered in 12 sessions of 4 hours each. That's a lot of time—and it's intentional. We're not rushing through concepts. We're building **real competence** through:

- **Practice density**: You'll write code almost every hour
- **Guided progression**: We start simple and build complexity only when you're ready
- **Debugging culture**: We teach you how to read errors and fix problems yourself
- **Real projects**: You'll build small programs that actually do something useful

By the end of this course, you'll be able to:
- Set up and run Python programs confidently
- Work with the core building blocks: variables, data structures, control flow
- Write organized code using functions and modules
- Handle files, directories, and common errors gracefully
- Build a small command-line project you can show others

**This course does NOT require any prior programming experience.** If you've never written a line of code, that's perfectly fine. We start at square one.

### Course Philosophy: Small Wins Build Confidence

Here's how we'll work together:

1. **Lecture** (10-15 min): I'll explain a concept and show you why it matters
2. **Demo** (5-10 min): I'll code it live and talk through my thinking
3. **Lab** (25-35 min): You'll practice immediately with exercises
4. **Debrief** (5 min): We'll share solutions and learn from each other

**Important mindset shift:** When you hit an error (and you will—we all do), that's not failure. That's feedback. Errors tell us exactly what to fix. We're going to get very comfortable reading error messages together.

---

## Section 2: Platform Setup & Navigation (10-15 minutes)

### Understanding Your Learning Environment

**[Instructor speaks:]**

Before we write any code, we need to make sure everyone can access the environment where we'll be working. We're using two connected systems: **LogicalCHOICE** and **LogicalLabs**. Let me explain how they work together and why this matters.

### The Two-Platform System

**LogicalCHOICE** is your content hub. Think of it like your course homepage. It contains:
- All the lesson materials
- Reference documents
- The launch tile that opens your lab environment

**LogicalLabs** is where the actual hands-on work happens. It's a remote virtual machine (VM) with Python already installed. When you click the lab tile in LogicalCHOICE, it opens LogicalLabs **in a new browser tab**.

### Critical Setup Step: The Two-Key Process

Here's where many people get stuck on Day 1, so let's be crystal clear:

**You have TWO different keys:**

1. **Course Content Key (CHOICE Key)**: This unlocks access to the course materials in LogicalCHOICE. You probably already used this to get here.

2. **Lab Access Key**: This provisions your actual virtual machine where you'll write code. **You must redeem this separately.**

**[Show on screen if possible while speaking:]**

Here's how to redeem your Lab Access Key:

1. Go to LogicalCHOICE
2. Look for **"Current Training"** (usually in the navigation menu)
3. Find the button that says **"Redeem Training Key"**
4. Enter your Lab Access Key
5. Wait for confirmation that your lab is provisioned

**Why two keys?** Because course content and lab infrastructure are managed separately. The content is like your textbook; the lab is like your hands-on workbench. You need both.

**[Pause here - check for questions]**

Let me see a show of hands: **Who has successfully redeemed both keys?**

If you haven't done this yet, that's okay—we're going to take care of it in the next few minutes during setup time.

### Important: Pop-Up Blockers and New Tabs

When you click the lab tile in LogicalCHOICE, it opens LogicalLabs in a **new browser tab**. 

**Common problem:** Many browsers block pop-ups by default. If you click the tile and nothing happens, look for a pop-up blocker notification in your browser's address bar. You'll need to allow pop-ups for the LogicalCHOICE domain.

**Which browsers work best?**
- Chrome: Excellent support
- Firefox: Excellent support  
- Safari: Works well
- Edge: Works well

**What you need:**
- JavaScript must be enabled (it usually is by default)
- Cookies should be allowed for these domains
- Pop-ups allowed for LogicalCHOICE

### The "Save and Suspend" Culture

Here's something crucial that will save you frustration: **Always save your work before taking breaks.**

Here's how the lab environment works:
- **Your files persist** even if you disconnect or close the browser tab
- **Your session state** (open windows, terminal sessions) does NOT persist

**Best practice before any break longer than 15 minutes:**

1. **Save All** in your IDE (usually Ctrl+K, Ctrl+S or Cmd+K, Cmd+S, or File → Save All)
2. Close your browser tab if needed
3. When you return: relaunch from the LogicalCHOICE tile
4. Your files will be right where you left them

**[Speaking point]:** Think of it like this: the lab VM is like a library study room. You can leave your books (files) there overnight, but the desk setup resets when you come back. Your work is safe; you just need to reopen things.

### Workspace Standards: Stay Organized from Day 1

We're going to establish a **workspace standard** right now that will prevent 90% of the common "my code won't run" problems beginners hit.

**The standard:**
- Create **one main folder** for this entire course (I recommend naming it `python_basics` or `python_course`)
- Put ALL your scripts in this folder (or in organized subfolders inside it)
- Later, we'll create a `/data` subfolder for files we read and write

**Why does this matter?**
- File paths are relative to where you run your code
- If your files are scattered across different directories, Python won't know where to find them
- Imports (when we get to modules) only work cleanly when files are in predictable locations

**[Key point]:** Stay organized from Day 1. Future-you will thank present-you.

---

## Section 3: The "Why Python?" Conversation (5 minutes)

### Why Are We Learning Python?

**[Instructor speaks:]**

Before we dive into the technical setup, let's talk about **why Python** and **why it's the right first language** for beginners.

Python is:

**1. Readable**  
Python code looks close to plain English. Compare this to other languages, and you'll see the difference immediately. Python was designed to be read by humans first.

**2. Powerful**  
Despite being beginner-friendly, Python runs some of the world's most important systems:
- Data science and machine learning (NumPy, pandas, TensorFlow)
- Web applications (Django, Flask)
- Automation and scripting
- Scientific computing
- Game development
- Cloud infrastructure

**3. In-demand**  
Python is consistently in the top 3 most popular programming languages worldwide. Employers in almost every industry need Python developers.

**4. Forgiving**  
Python lets you experiment. You can type a single line and run it. You can test ideas quickly. This tight feedback loop makes learning faster.

### What You'll Actually Be Able to Do

By the end of this course, you'll be able to build programs that:
- Process and analyze data from files
- Automate repetitive tasks on your computer
- Build command-line tools that solve real problems
- Read and write JSON data (the format most APIs use)
- Handle errors gracefully instead of crashing

These aren't toy programs. These are real, practical skills.

---

## Section 4: Understanding Your Environment (10 minutes)

### How Python Executes: Interpreter vs. Script Files

**[Instructor speaks:]**

Let's talk about what's actually happening when you "run Python code." There are two main ways to interact with Python:

#### 1. The REPL (Interactive Mode)

REPL stands for **Read-Eval-Print Loop**. It's a live conversation with Python:
- You type a line
- Python reads it, evaluates it, prints the result
- Then waits for your next line

**When to use the REPL:**
- Testing quick ideas
- Checking syntax
- Exploring how something works
- Doing calculations

**To open the REPL:** Just type `python` (or `python3` on some systems) in your terminal and press Enter.

#### 2. Script Files (.py files)

A script file is a text file containing multiple Python statements saved with a `.py` extension. When you run a script:
- Python reads the entire file top to bottom
- Executes every statement in order
- Then exits (unless there's a loop or error)

**When to use scripts:**
- Building actual programs
- Saving your work
- Running code multiple times
- Sharing code with others

**To run a script:** Type `python script_name.py` in your terminal.

**[Key distinction]:** The REPL is for **exploring**. Scripts are for **building**.

### Where Files Live in the Lab

**[Instructor speaks:]**

In your lab VM, you have a file system just like on any computer. You need to know:

1. **Your home directory**: This is usually `/home/username` or something similar. Your course folder should live here.

2. **Your working directory**: This is where Python looks for files when you run a script. When you're in the terminal, you can check your current location with:
   ```bash
   pwd
   ```
   (That stands for "print working directory")

3. **Absolute vs. relative paths**:
   - **Absolute**: Full path from the root: `/home/username/python_basics/hello.py`
   - **Relative**: Path from where you currently are: `hello.py` (if you're already in `python_basics/`)

**[Important note]:** When you run a script, Python's working directory is wherever your terminal is currently located. This is why we keep everything in one course folder—it prevents path confusion.

### Naming Conventions and File Organization

**[Instructor speaks:]**

Let's establish good habits now:

**File naming:**
- Use lowercase letters
- Separate words with underscores: `my_first_script.py` (NOT `MyFirstScript.py` or `my-first-script.py`)
- Be descriptive: `calculate_average.py` is better than `script1.py`
- Always use the `.py` extension for Python scripts

**Folder organization:**
```
python_basics/          ← Your main course folder
├── hello_course.py     ← Hour 1 work
├── greeter.py          ← Hour 2 work
├── variables_demo.py   ← Hour 3 work
└── data/               ← (We'll create this later for file I/O)
```

**Why this matters:** Consistency helps you find things fast. Six weeks from now, you'll know exactly where your old scripts are.

---

## Section 5: Live Demo (5-10 minutes)

### Demo Script: Your First Python Experience

**[Instructor speaks:]**

Alright, now I'm going to walk through the entire process live. I want you to **watch first, then you'll do it yourself** in the lab exercise. I'll narrate what I'm doing and why.

**[Start live demo - speak as you type]:**

---

**Step 1: Launch the Lab Environment**

"Okay, I'm in LogicalCHOICE. I'm going to click on the lab tile. Notice that it opens in a **new browser tab**. If nothing happened, I'd check for a pop-up blocker notification."

**[Wait for lab to load]**

"The lab is loading... and there we go. I'm now in the LogicalLabs environment."

---

**Step 2: Open the Terminal**

"First thing I need is a terminal. In most lab environments, there's a terminal icon in the taskbar or I can search for 'terminal' in the application menu."

**[Open terminal]**

"Great, terminal is open. Let's verify Python is installed."

---

**Step 3: Check Python Version**

**[Type this command]:**
```bash
python --version
```

**[Or if that doesn't work]:**
```bash
python3 --version
```

**[Speak while output appears]:**

"I'm running `python --version` to check which version of Python is installed. I should see something like `Python 3.11` or `Python 3.10`—any Python 3.x version is fine for this course."

**[Expected output]:** `Python 3.11.x` (or similar)

"Perfect! Python is installed and accessible. If you saw an error here, you'd need to troubleshoot your Python installation—but in this lab, it's pre-configured."

---

**Step 4: Create Your Course Folder**

**[Type these commands]:**
```bash
pwd
```

**[Explain]:**  
"First I'm checking where I am with `pwd`. This tells me my current working directory."

**[Then create folder]:**
```bash
mkdir python_basics
```

**[Explain]:**  
"`mkdir` means 'make directory.' I'm creating a folder called `python_basics` right here in my home directory. All my course work will live inside this folder."

**[Verify it was created]:**
```bash
ls
```

**[Explain]:**  
"`ls` lists directory contents. I should see `python_basics` in the list now."

**[Navigate into the folder]:**
```bash
cd python_basics
```

**[Explain]:**  
"`cd` means 'change directory.' Now I'm inside my course folder. Any files I create will be created here."

---

**Step 5: Create Your First Script**

**[Speak as you work]:**

"Now I need to open an IDE or text editor. I'm going to use VS Code, which should be available in the lab."

**[Open VS Code or alternative IDE]**

"In VS Code, I'll do File → Open Folder → select `python_basics`."

"Now I'll create a new file: File → New File. I'll name it `hello_course.py`."

**[Type this code in the file]:**
```python
# My first Python script
# This program prints a simple greeting

print("Hello, Python Basics course!")
print("Today we're starting our programming journey.")
print("Let's do this!")
```

**[Explain as you type]:**

"Notice a few things:
- Lines starting with `#` are **comments**—they're notes for humans, Python ignores them
- `print()` is a function that displays text to the screen
- The text inside quotes is called a **string**—it's literal text
- Each `print()` statement goes on its own line"

**[Save the file]:**

"Now I'll save this. I can use Ctrl+S (or Cmd+S on Mac) or File → Save. Notice the file is saved inside my `python_basics` folder."

---

**Step 6: Run the Script from Terminal**

**[Return to terminal]:**

"Back to the terminal. I'm already inside the `python_basics` folder. Now I'll run my script:"

**[Type this command]:**
```bash
python hello_course.py
```

**[Expected output]:**
```
Hello, Python Basics course!
Today we're starting our programming journey.
Let's do this!
```

**[Explain]:**

"Boom! My program ran. I told Python to execute the `hello_course.py` script, and it printed exactly what I told it to print. This is the fundamental workflow:
1. Write code in a `.py` file
2. Save the file
3. Run it with `python filename.py`
4. See the output"

---

**Step 7: Run the Script from the IDE (if available)**

**[In VS Code]:**

"Many IDEs have a built-in way to run scripts. In VS Code, I can right-click the file and select 'Run Python File' or click the play button in the top-right corner."

**[Click run button]**

"See the output appear in the integrated terminal at the bottom? Same result. This is convenient because you don't have to switch windows."

---

**Step 8: Verify File Persistence**

**[Speak as you demonstrate]:**

"Now here's the important part about the lab environment. I'm going to close this file, close VS Code, and then reopen it to confirm I can find my file again."

**[Close editor, reopen, navigate to file]:**

"File → Open Folder → `python_basics` → there's my `hello_course.py`. Opening it... and my code is still here. Perfect!"

"This confirms file persistence is working. My work is saved. Even if I disconnect from the lab and come back tomorrow, this file will be here."

---

**[End of demo]**

"That's the complete workflow. In the next 25-35 minutes, you're going to do this yourself. I'll be circulating to help if you hit any snags."

---

## Section 6: Hands-On Lab Exercise (25-35 minutes)

### Lab: Environment Check + First Run

**[Instructor speaks:]**

Alright, now it's your turn! Here's what I want you to accomplish in this lab session. Take your time, follow the steps, and raise your hand if you get stuck.

### Lab Objectives

You will:
1. Launch LogicalLabs from the LogicalCHOICE tile
2. Verify Python is installed and accessible
3. Create a course folder called `python_basics`
4. Create a script called `hello_course.py` that prints a personalized greeting
5. Run your script from both the terminal AND the IDE
6. Close and reopen your file to verify you can locate it

### Detailed Instructions

**Part 1: Access Your Lab Environment (5 minutes)**

1. Open LogicalCHOICE in your browser
2. Navigate to your course
3. Click the lab tile to launch LogicalLabs
4. Verify the lab opens in a new tab
5. If it doesn't open, check your pop-up blocker settings

**Part 2: Verify Python Installation (2 minutes)**

6. Open a terminal in the lab VM
7. Run: `python --version` (or `python3 --version`)
8. Confirm you see Python 3.x

**Part 3: Create Your Workspace (5 minutes)**

9. Check your current location: `pwd`
10. Create a folder: `mkdir python_basics`
11. Verify it was created: `ls`
12. Move into the folder: `cd python_basics`

**Part 4: Write Your First Script (10 minutes)**

13. Open VS Code (or your IDE)
14. Open the `python_basics` folder in the IDE
15. Create a new file called `hello_course.py`
16. Write a Python program that prints:
    - Your name
    - Today's date (just type it as a string for now—we'll learn to generate it automatically later)
    - One sentence about why you're taking this course

**Example (but make it your own!):**
```python
# My first Python script
# Author: [Your name]

print("Hello! My name is Jordan.")
print("Today is January 13, 2026.")
print("I'm learning Python to build data analysis tools.")
```

17. Save the file (Ctrl+S or Cmd+S)

**Part 5: Run Your Script (10 minutes)**

18. From the terminal, run: `python hello_course.py`
19. Verify you see your output
20. From the IDE, use the "Run" button or right-click → "Run Python File"
21. Verify you see the same output in the IDE's terminal

**Part 6: Test File Persistence (3 minutes)**

22. Close the file in your IDE
23. Close VS Code completely
24. Reopen VS Code
25. Open the `python_basics` folder
26. Open `hello_course.py`
27. Confirm your code is still there

### Success Criteria

You've completed this lab when:
- ✅ Your script runs without errors from the terminal
- ✅ Your script runs without errors from the IDE
- ✅ You see the correct output (your personalized greeting)
- ✅ You can locate your script file after closing and reopening your editor
- ✅ You can explain (to yourself or a neighbor) where your course folder is located

### What If You Get Stuck?

**Problem: "I can't launch the lab"**
- Check pop-up blockers
- Verify you're clicking the correct tile in LogicalCHOICE
- Make sure you've redeemed your Lab Access Key

**Problem: "Python not found"**
- Try `python3` instead of `python`
- Verify you're in the lab VM, not on your local computer
- Ask for help—this is an installation issue

**Problem: "My script won't run"**
- Check for typos in the filename
- Make sure you're in the correct directory (`pwd` to check, `cd python_basics` if needed)
- Verify the file has a `.py` extension

**Problem: "I get a syntax error"**
- Check that strings are enclosed in matching quotes (`"` or `'`)
- Verify every `print(` has a closing `)`
- Look at the line number in the error message—that's where Python got confused

---

## Section 7: Debrief & Common Pitfalls (5 minutes)

### Group Share-Out

**[Instructor speaks:]**

Alright, let's come back together. I'd love to hear from 2-3 people about their experience.

**[Call on volunteers]:**

- "What did you name your script?"
- "What did you include in your greeting?"
- "Did anyone hit an error? How did you fix it?"

**[Affirm student responses]:**

"Excellent! I love that you [specific positive note]. That's exactly the right approach."

### Common Pitfalls We Want to Watch For

**[Instructor speaks:]**

Based on years of teaching this course, here are the most common issues beginners hit in Hour 1:

#### 1. Wrong Interpreter Selected in IDE

**What happens:** You click "Run" in VS Code but see an error like "Python not found" even though Python IS installed.

**Why:** Your IDE might be configured to use a different Python interpreter than the one installed in your lab.

**Fix:** In VS Code, look at the bottom-left corner where it shows the Python version. Click it and select the correct interpreter (usually the one with the highest version number).

#### 2. Saving File Outside the Workspace

**What happens:** You create a script but can't find it later, or it won't run.

**Why:** You saved it in a different folder (maybe Documents or Desktop) instead of inside `python_basics`.

**Fix:** Always use "Open Folder" in your IDE and work inside the `python_basics` folder. When you save, double-check the location.

#### 3. Confusing Terminal Path vs. File Path

**What happens:** You try to run `python hello_course.py` but get "No such file or directory."

**Why:** Your terminal is in a different directory than where the file is saved.

**Fix:** Use `pwd` to check where you are. Use `cd python_basics` to navigate to your course folder. THEN run the script.

#### 4. Using Smart Quotes from Copy/Paste

**What happens:** You copy code from a slide or PDF and get a syntax error.

**Why:** Word processors use "smart quotes" (`"` and `"`) instead of straight quotes (`"`). Python only understands straight quotes.

**Fix:** Retype the quotes manually in your code editor, or change your editor settings to convert smart quotes automatically.

---

## Section 8: Exit Ticket & Looking Ahead (5 minutes)

### Quick Check Question

**[Instructor speaks:]**

Before we move to Hour 2, I want to make sure everyone understands one key distinction. Here's your exit ticket question:

**"What's the difference between running Python in the REPL (interactive mode) and running a .py script file?"**

**[Give students 30 seconds to think, then call on 1-2 people for answers]**

**[Expected answer - affirm when you hear it]:**

"Great! Exactly right. The REPL is for quick exploration—you type one line at a time and get immediate feedback. A script file is for building programs—you write multiple lines, save them, and run the whole file at once."

**[If students are uncertain, clarify]:**

"Think of it this way:
- **REPL** = having a conversation with Python (back-and-forth, one line at a time)
- **Script** = giving Python a written set of instructions to follow (run the whole thing top to bottom)"

### What's Next in Hour 2

**[Instructor speaks:]**

In the next hour, we're going to write our first real scripts. You'll learn:
- How to use `print()` effectively
- Why comments matter and how to write good ones
- How to READ error messages (this is a superpower!)
- The five most common beginner errors and how to fix them in 30 seconds

You'll write a "greeter" program that prints a multi-line welcome message. And here's the fun part: we're going to **intentionally create errors** and practice debugging them.

### Before We Break

**[Instructor speaks:]**

Quick reminders before we take a 5-minute break:

1. **Save your work**: Ctrl+S (or Cmd+S) to save all open files
2. **Remember your folder location**: Your `python_basics` folder is in your home directory
3. **You can experiment**: Try changing your script and running it again! You can't break anything.

If you finish the lab early, here are two optional extensions you can try:

**Extension 1:** Add a second script called `date_demo.py` that imports Python's `datetime` module and prints today's date automatically. Here's starter code:
```python
from datetime import date

today = date.today()
print(f"Today is {today}")
```

**Extension 2:** Add a "run instructions" comment header to your script. Make it look professional:
```python
# hello_course.py
# Description: My first Python script - prints a personalized greeting
# Author: [Your name]
# Date: [Today's date]
# How to run: python hello_course.py

print("Hello, Python!")
```

---

## Instructor Notes & Troubleshooting

### Time Management Tips

- If platform issues eat into time, compress the "Why Python?" section to 3 minutes
- The live demo can be condensed to 5 minutes if students are anxious to start
- Extend lab time to 40 minutes if many students are struggling
- The debrief can be shortened to 3 minutes if needed

### Watch for These Red Flags

🚩 **Student can't launch lab**: Help immediately—they can't proceed without it

🚩 **Student is in the wrong directory**: Walk them through `pwd` and `cd`

🚩 **Student's output doesn't appear**: Check if they're looking at the right terminal/output pane

🚩 **Student seems lost**: Sit with them 1-on-1 and walk through the demo steps again

### Differentiation Strategies

**For students who finish early:**
- Suggest the extension exercises
- Ask them to help a neighbor (peer teaching reinforces learning)
- Challenge them to add emoji to their output using Unicode

**For students who are struggling:**
- Pair them with a buddy who finished
- Offer to screenshare your own screen and walk through together
- Simplify the script requirement—just get ONE line to print successfully

### Accessibility Considerations

- Ensure terminal font size is readable for screensharing
- Describe what you're clicking during demos (for screen reader users)
- Provide a text version of all commands in the chat or a shared document
- Offer alternative editors if VS Code isn't accessible for a student

---

## Recap: What We Accomplished

In this first hour together, you:
✅ Successfully accessed the lab environment  
✅ Learned the two-key redemption process  
✅ Created an organized workspace folder  
✅ Wrote and ran your first Python script  
✅ Understood the difference between REPL and script execution  
✅ Experienced the full workflow: write → save → run → see output  

**This is a HUGE milestone.** You're no longer a "non-programmer." You've written code. You've made a computer do something you told it to do. That's real.

In Hour 2, we build on this foundation and start making our programs more interactive and useful.

**Great work, everyone. See you in five minutes!**

---

## Quick Reference Card (for students)

**Essential Commands:**
- Check Python version: `python --version`
- Check current directory: `pwd`
- List directory contents: `ls`
- Create directory: `mkdir folder_name`
- Change directory: `cd folder_name`
- Run a Python script: `python script_name.py`

**Course Folder Structure:**
```
python_basics/
├── hello_course.py
└── (more scripts as we progress)
```

**Save and Suspend Checklist:**
- [ ] Save all files (Ctrl+S or Cmd+S)
- [ ] Know where your `python_basics` folder is located
- [ ] Close browser tab if needed
- [ ] Relaunch from LogicalCHOICE tile when you return

**Getting Help:**
- Raise your hand during lab time
- Ask a neighbor (peer learning is powerful!)
- Check the error message—it tells you the line number and problem
- Review the demo recording if available

---

**End of Hour 1 Script**
