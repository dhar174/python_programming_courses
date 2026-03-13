# Day 1, Hour 1: Advanced Kickoff, Baseline Diagnostic, and Git Workflow

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 1 (Hour 1 of 48)
- **Focus**: Advanced kickoff, baseline diagnostic, and Git workflow
- **Prerequisites**: Comfort with basic Python variables, control flow, functions, basic classes, file I/O.
- **Goal**: Confirm environment setup, establish a Git workflow, verify baseline skills.

---

## 1. Advanced Kickoff (10 minutes)

**Instructor Talk Points:**

- **Welcome to Advanced Python!** "Hello everyone, and welcome to the Advanced Python course. You've conquered the basics—variables, loops, functions, and reading files. Now, we're going to build professional-grade software."
- **Course Workflow:** "Over the next 48 instructional hours, we will explore advanced Object-Oriented Programming, design patterns, Graphical User Interfaces (GUIs), databases, APIs, data analysis, and testing. Every session involves lectures, live demos, and a hands-on lab. You will be building a capstone project—a Full-stack Tracker—throughout the course."
- **Advanced Expectations:** "The leap from 'Basic' to 'Advanced' is all about readability, structure, and a testing mindset. Code is read more often than it's written. We won't just learn *how* to write code, but how to write *good*, maintainable code."
- **Environment Setup:** "We are using the LogicalLabs (CHOICE remote lab) environment. Your labs will open in a new browser tab. If they don't open, please check your browser to ensure pop-ups aren't blocked."
  - *Crucial difference:* "There is a massive difference between saving your files and saving the lab state. Pressing `Ctrl+S` saves your file to the virtual disk. However, if you step away for more than 15 minutes or finish for the day, you MUST use the **Save and Suspend** feature in the lab launcher so your entire session state is preserved."

## 2. Live Demo: Lab Environment and Git Basics (10 minutes)

**Live Demo Steps:**

1. **Lab Launch:** 
   *(Action: Share screen and launch the lab from CHOICE. Point out that it opens in a new tab.)*
   "Notice how the lab environment opens in a new tab. Make sure your browser allows this."
2. **File Persistence Demo:**
   *(Action: Create a text file, write to it, and hit Save. Close the editor pane and reopen it.)*
   "See how saving works? The file persists on the disk. But remember, for longer breaks, use **Save and Suspend** here." *(Action: Highlight the Save and Suspend button.)*
3. **Repository Initialization:**
   *(Action: Open a terminal inside the lab workspace.)*
   "Now, let's set up our project repository. This is where your capstone will live."
   ```bash
   mkdir capstone_tracker
   cd capstone_tracker
   git init
   ```
   "We use Git for version control. It's an industry standard. The workflow is: you do some work, you stage it, and you commit it."
4. **Baseline Script:**
   *(Action: Create `diagnostic.py`.)*
   "Let's create a quick script to make sure Python is running correctly."
   ```python
   # diagnostic.py
   class Hello:
       def __init__(self, name):
           self.name = name
       def greet(self):
           print(f"Hello, {self.name}!")

   try:
       h = Hello("Advanced Learner")
       h.greet()
       
       # Dictionary test
       data = {"status": "ready"}
       print(data["status"])
       
       # File I/O test
       with open("test.txt", "w") as f:
           f.write("System OK.")
           
   except Exception as e:
       print(f"Error: {e}")
   ```
   *(Action: Run the script. Verify output. Commit the changes.)*
   ```bash
   python diagnostic.py
   git add diagnostic.py test.txt
   git commit -m "chore: initial setup and diagnostic script"
   ```

## 3. Hands-on Lab: Setup and Diagnostic (25-35 minutes)

**Lab Prompt for Students:**
"Now it's your turn to establish your workspace and prove your environment is working."

1. **Preflight Check:** Create a file named `course_preflight.txt`. Write today's date, time, and your name. Save it. Confirm it's visible after closing and reopening the editor pane.
2. **Project Structure:** Create a new folder for your project. Inside it, create the following standard subfolders: `src/`, `tests/`, `data/`, `reports/`.
3. **Git Initialization:** Initialize Git in your project folder (`git init`) and make your first commit.
4. **Diagnostic Script:** Write and run a short diagnostic Python script. Your script must:
   - Define and instantiate a basic class.
   - Read from or write to a file.
   - Catch an exception.
   - Interact with a dictionary.
5. **Goal Setting:** At the top of your diagnostic script or in a `README.md`, record one personal goal for this week (e.g., 'get comfortable with Object-Oriented class design').

**Instructor: Circulate and check:**
- Is the correct Python interpreter selected in their IDE?
- Did they actually run a `git commit` or just `git add`?
- Check for workspace path issues in the VM.
- Remind them: "If you need to step away for a break, hit Save and Suspend!"

*Optional Extensions for fast finishers:*
- Create a virtual environment (`venv`) and freeze requirements.
- Add a `.gitignore` file (ignoring `__pycache__`, `venv`, `.db`, `reports/`).

## 4. Debrief and Quick Check (5 minutes)

- **Debrief:** Ask a student to share what their personal goal is for the week.
- **Quick Check Question:** "What is the difference between `git commit` and `git push`?"
  - *Answer:* `commit` saves changes to your local repository history. `push` uploads those commits to a remote remote repository (like GitHub).
- **Wrap-up:** "Great work setting up. Next hour, we will dive into translating requirements into professional, object-oriented class structures."
