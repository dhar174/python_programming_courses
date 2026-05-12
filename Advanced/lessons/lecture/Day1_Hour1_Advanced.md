# Day 1, Hour 1: Advanced Kickoff, Baseline Diagnostic, and Git Workflow

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 1, Hour 1 of 48
- **Focus**: Advanced kickoff, baseline diagnostic, LogicalLabs/CHOICE launch, project folder setup, and first Git workflow.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 1, Hour 1.
- **Prerequisites**: Students should be comfortable with basic Python syntax, variables, conditionals, loops, functions, dictionaries, simple classes, basic exception handling, and basic file I/O.
- **Advanced trajectory**: This course moves learners from a PCAP-level foundation toward PCPP1-style habits: readable design, object-oriented structure, persistence, testing, maintainability, and professional workflow.
- **Instructor goal**: By the end of this hour, every learner has launched the lab, confirmed file persistence, created a project workspace, initialized Git, run a diagnostic script, and made an initial commit or saved the repository locally.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Welcome and advanced framing | 5 min | Set expectations and connect Basics to Advanced |
| LogicalLabs/CHOICE launch and persistence briefing | 7 min | Prevent lab loss and confusion before work begins |
| Git workflow concept briefing | 6 min | Establish the course workflow: clone or init, pull, change, stage, commit, optionally push |
| Live demo: workspace, diagnostic, first commit | 12 min | Model the exact steps learners will repeat |
| Guided lab: setup and baseline diagnostic | 25 min | Learners create their environment and prove readiness |
| Debrief, completion criteria, quick check | 5 min | Confirm outcomes and prepare for Hour 2 |

Adjust the timing based on the room, but keep this as a one-hour delivery plan. If login or browser pop-up issues take longer than expected, protect the 25-minute guided lab by trimming the opening discussion, not by skipping the Save and Suspend explanation.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain how the Advanced course will use lectures, labs, and capstone milestones.
2. Describe the difference between saving a file and saving the full lab session state.
3. Launch the LogicalLabs/CHOICE lab environment and identify the Save and Suspend control.
4. Create a project folder with the standard course subfolders: `src/`, `tests/`, `data/`, and `reports/`.
5. Initialize a Git repository and explain the difference between the working tree, staging area, and commit history.
6. Run a deterministic `diagnostic.py` script that exercises a class, a dictionary, file write/read, and exception handling.
7. Make an initial Git commit using a clear commit message.
8. State one personal learning goal for the first week of Advanced Python.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Confirm the LogicalLabs/CHOICE course lab is available and opens in a new browser tab.
- Confirm pop-ups are allowed in your instructor browser, so you can demonstrate the expected behavior.
- Confirm the lab workspace includes a working terminal, editor, Python 3, and Git.
- Run the instructor preflight commands before class:

```bash
python --version
pip --version
git --version
python -c "import sqlite3"
```

- If the lab image is expected to include course packages, also verify the imports that later sessions will rely on:

```bash
python -c "import requests, flask, pytest, pandas, matplotlib"
```

- If one or more course packages are not installed yet, note that for learners. Do not troubleshoot all future package installs during Hour 1 unless the lab policy says those packages must already be available.
- Prepare to show the Save and Suspend button. Do not assume learners have seen it before.
- Keep this script open in a separate instructor window, not inside the learner demo workspace if possible.
- Decide whether the local terminal command should be `python diagnostic.py` or `python3 diagnostic.py` in the lab. Use the one that works in the environment. If both work, use `python diagnostic.py` for consistency with the course files.
- Be ready to support path confusion. Many early issues in remote labs are not Python issues; they are "I am in the wrong folder" issues.

Suggested board note before the session starts:

```text
Day 1 Hour 1 goals:
1. Launch lab
2. Save file vs Save and Suspend
3. Create project folder
4. Run diagnostic.py
5. Make first Git commit
```

---

## Opening Script: Welcome to Advanced Python (5 minutes)

**Instructor talk track**

"Welcome to Advanced Python. I am glad you are here. If you completed the Basics course or already have equivalent experience, you have the tools to write Python programs that run. In this course, we are going to focus on writing Python programs that are easier to understand, easier to change, easier to test, and easier to grow."

"That is the main difference between beginner Python and advanced Python. Beginner Python often asks, 'Can I make this work?' Advanced Python also asks, 'Can another developer understand this? Can I test it? Can I extend it next week without breaking it? Can I explain why this design is reasonable?'"

"This course is not about memorizing every corner of the language. It is about building professional habits. We will still write a lot of code, but we will also talk about structure, naming, responsibility, validation, testing, persistence, and workflow. Those are the habits that move you from a PCAP-level foundation toward the style of thinking expected in PCPP1-level work."

"Our course rhythm is simple: we will use short lecture segments, live demos, guided labs, and capstone milestones. You will repeatedly build small pieces of a larger tracker-style application. Over time, that application will include object-oriented design, file and database persistence, a user interface, APIs or service boundaries where appropriate, testing, and packaging. Today is not about building all of that. Today is about making sure our environment works and our workflow is reliable."

Pause and ask:

"Before we do anything technical, what makes code feel 'advanced' to you? Is it more syntax, larger programs, cleaner design, better tests, or something else?"

Take two or three short answers. Then connect them:

"Those are all useful answers. In this course, advanced does not mean 'clever.' Advanced means intentional. We want code that communicates clearly."

**Set expectations**

"You will make mistakes in this course. That is expected. A traceback is not a personal failure. A Git mistake is not a disaster. A file path issue is not a sign that you are behind. These are normal parts of software development. Our job is to slow down, read the evidence, and fix the smallest thing that is actually broken."

"The first hour is a setup and baseline diagnostic hour. I am not grading you on whether you remember every detail from Basics. I am looking for signals. Can your environment run Python? Can you create folders and files? Can you use a class, a dictionary, a file, and a try/except block? Can you make a Git commit? If yes, you are ready for the next hour. If not, we will find the issue now, before the work gets larger."

---

## Concept Briefing: Course Workflow and Advanced Expectations (5 minutes)

Use this section to establish the mental model for the course.

**Instructor talk track**

"Here is the workflow we will repeat across Advanced Python."

1. "First, we clarify the problem. What are we trying to build or improve?"
2. "Second, we choose a small design. What data do we need? What class or function owns which responsibility?"
3. "Third, we implement a small piece. Not the whole app at once. A small piece."
4. "Fourth, we run it. We read errors carefully."
5. "Fifth, we save our progress with Git."
6. "Sixth, when appropriate, we test it and improve it."

"If you only take one habit from today, take this: work in small steps and commit working checkpoints. Do not wait until you have three hours of changes before you commit. A commit is a safe checkpoint in your project history."

**Bridge from Basics**

"In Basics, you probably wrote scripts where everything lived in one file. That is fine for learning syntax. In Advanced, we will start separating responsibilities. A file may contain a class. Another file may contain tests. Another file may contain data. Another file may contain application startup logic. That separation is why our project folder matters."

"Today's folder structure is intentionally simple:"

```text
advanced_tracker/
    src/
    tests/
    data/
    reports/
```

"The `src` folder is where application code will eventually go. The `tests` folder is where tests will eventually go. The `data` folder is where small local data files can live during labs. The `reports` folder is where generated outputs can live. We are not using all of these deeply in Hour 1, but we are creating the habit now."

---

## LogicalLabs/CHOICE Launch and Persistence Briefing (7 minutes)

This is one of the most important parts of the hour. Learners can lose time and confidence if they misunderstand how the remote lab persists work.

**Instructor action cue**

Share your screen. Open the CHOICE/LogicalLabs launcher. Start the assigned lab. Narrate slowly.

**Instructor talk track**

"We are using the LogicalLabs environment through CHOICE. When you launch a lab, it may open in a new browser tab. If nothing appears to happen, do not immediately click ten more times. First, check whether your browser blocked a pop-up. Look near the address bar for a pop-up warning. Allow pop-ups for the lab site if needed."

"Once the lab opens, you are working in a remote environment. It may look like a normal desktop or browser-based IDE, but it is a lab session. That means there are two kinds of saving we must understand."

Write or display:

```text
Ctrl+S or File Save = saves the current file
Save and Suspend = saves the full lab session state
```

"Saving a file means the contents of that file are written to disk inside the lab. For example, if I type a line into `diagnostic.py` and press Ctrl+S, the file is saved."

"Saving the lab session state is different. If you are ending for the day, or stepping away for more than about 15 minutes, you must use Save and Suspend. Save and Suspend preserves the whole lab state so you can return later."

**Instructor action cue**

Create a quick file in the editor named `course_preflight_demo.txt`, type one line, save it, close the editor tab, reopen the file, and show that the file contents are still present.

Use this exact simple content:

```text
Instructor preflight demo
```

**Instructor talk track**

"This demonstrates file saving. The file is still here after closing and reopening the editor pane. But this is not the same as suspending the lab. If I am finished for the day or taking a long break, I also need Save and Suspend."

**Instructor action cue**

Point to the Save and Suspend control in the lab launcher or lab interface. Do not click it if clicking would end your demo unless you know it is safe. Just show where it is.

**Instructor talk track**

"Please remember this phrase: file save protects the file; Save and Suspend protects the session. If you ask me later, 'I saved my file, why is my lab gone?' this distinction is usually where we start."

**Ask for confirmation**

"Everyone, before we continue, please locate the Save and Suspend control in your own lab. You do not need to click it right now. Just point to it or give me a thumbs-up when you know where it is."

Wait long enough for learners to actually locate it. This may feel slow, but it prevents bigger issues later.

---

## Concept Briefing: Git Workflow for This Course (6 minutes)

Keep this beginner-friendly. This hour is not a full Git course.

**Instructor talk track**

"Now we are going to use Git. Git is version control. It records snapshots of your project over time. In this course, Git gives us a reliable way to save checkpoints and recover from experiments."

"There are six Git words I want you to understand today. We will use only a few deeply today, but you should recognize all six because they appear in the course workflow."

```text
Clone: copy a remote repository to your lab workspace
Pull: bring remote changes into your local repository before you work
Working tree: the files you are editing right now
Staging area: the list of changes you plan to include in the next commit
Commit: a saved checkpoint in local Git history
Push: sending local commits to a remote repository such as GitHub
```

"A common beginner misunderstanding is that `git add` saves the project permanently. It does not. `git add` stages changes. The commit is the local checkpoint. If a remote repository is configured, `git push` sends that checkpoint to the remote."

"If your instructor gives you a repository URL, the first command is usually `git clone URL`, then `git pull` before you start new work. If the lab starts from an empty folder, as this demo does, the first command is `git init`. Both flows are valid; the key is to know whether you are starting from a provided repository or creating a new local one."

```bash
# Provided repository flow
git clone REPOSITORY_URL
cd REPOSITORY_FOLDER
git pull

# Empty-folder flow for today's demo
git init
```

"For Hour 1, the required workflow is simple:"

```bash
git status
git add diagnostic.py data/diagnostic_report.txt src/.gitkeep tests/.gitkeep reports/.gitkeep
git commit -m "chore: initial setup"
git status
```

"If your environment already has a remote repository configured, you may also push. If it does not, do not panic. The runbook allows the first commit to be pushed or saved locally. The important thing today is that the repository exists and has at least one commit."

"We may use branches later. Branching is a powerful professional habit, but it is optional today. Today we are focusing on the first reliable local checkpoint."

**Mini-check**

Ask:

"What is the difference between `git add` and `git commit`?"

Expected answer:

"`git add` stages changes for the next checkpoint. `git commit` creates the checkpoint in local history."

If students answer "add saves it," gently correct:

"That is a very common first guess. `git add` prepares the snapshot. `git commit` records it."

---

## Live Demo: Project Folder, Diagnostic Script, and First Commit (12 minutes)

This demo should be direct and reproducible. Type the commands rather than pasting everything instantly if time allows. The purpose is to model pace and habits.

### Demo Step 1: Create the project folder

**Instructor action cue**

Open a terminal in the lab workspace. Run:

```bash
pwd
mkdir advanced_tracker
cd advanced_tracker
mkdir src tests data reports
touch src/.gitkeep tests/.gitkeep reports/.gitkeep
```

If `pwd` is not available in the lab shell, use the environment's equivalent command. In many terminals used for these labs, `pwd` will work.

**Instructor talk track**

"I start with `pwd` because I want to know where I am. Many setup errors are path errors. If you create files in the wrong folder, Python and Git may appear broken even though they are fine."

"Now I create a project folder called `advanced_tracker`. You can use this name, or if your instructor has given a specific naming convention, follow that convention. Inside it, I create four folders: `src`, `tests`, `data`, and `reports`. I also create small `.gitkeep` placeholder files in the folders that would otherwise be empty, because Git tracks files, not empty folders."

Run:

```bash
ls
```

If `ls` is not available, use the file explorer or the environment's equivalent. Do not spend much time on shell differences. The key is that learners can see the folders.

### Demo Step 2: Initialize Git

Run:

```bash
git init
git status
```

**Instructor talk track**

"`git init` turns this folder into a Git repository. It creates the hidden Git metadata that stores history. Then I immediately run `git status`. `git status` is your friend. When you are unsure, run `git status` before guessing."

"Right now, Git sees our placeholder files and any files we create during the demo. Git does not track empty folders by themselves, so the `.gitkeep` files are a simple way to preserve the intended project structure in the first commit."

### Demo Step 3: Create the diagnostic script

**Instructor action cue**

Create a file named `diagnostic.py` in the project root, not inside `src` for this first diagnostic. Explain that later code may move into `src`, but today's diagnostic belongs at the root so learners can run it easily.

Use this complete code:

```python
from pathlib import Path


class LearnerProfile:
    """Small class used to confirm object creation and method calls."""

    def __init__(self, name: str, goal: str) -> None:
        self.name = name
        self.goal = goal

    def summary(self) -> str:
        return f"{self.name} is practicing: {self.goal}"


def write_status_report(path: Path, profile: LearnerProfile, status: dict[str, str]) -> None:
    lines = [
        "Advanced Python Diagnostic",
        profile.summary(),
        f"Python status: {status['python']}",
        f"Git status: {status['git']}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_status_report(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> None:
    profile = LearnerProfile(
        name="Advanced Learner",
        goal="build readable, testable Python programs",
    )
    status = {
        "python": "ready",
        "git": "ready for first commit",
    }
    report_path = Path("data") / "diagnostic_report.txt"

    try:
        write_status_report(report_path, profile, status)
        report_text = read_status_report(report_path)
        print(report_text)
        print("Diagnostic complete.")
    except OSError as error:
        print(f"File operation failed: {error}")
    except KeyError as error:
        print(f"Missing diagnostic status key: {error}")


if __name__ == "__main__":
    main()
```

**Instructor talk track while typing or reviewing**

"This script is intentionally small, but it checks several important baseline skills."

"First, it defines a class called `LearnerProfile`. The class has an initializer, stores attributes, and has a method named `summary`. That confirms we remember the basic shape of a Python class."

"Second, it uses a dictionary named `status`. The dictionary has two string keys: `python` and `git`. We access those keys when building the report."

"Third, it writes to a file and reads from a file using `pathlib`. We are using `Path('data') / 'diagnostic_report.txt'` so the output file lands inside the `data` folder we created."

"Fourth, it handles possible errors. If the file operation fails, we catch `OSError`. If a dictionary key is missing, we catch `KeyError`. We are not using a broad `except Exception` here because one advanced habit is to catch the errors we actually expect when we can."

"Fifth, the script is deterministic. It does not ask for input. It does not depend on the current date or a random value. If the environment is working, it should produce the same kind of output every time."

### Demo Step 4: Run the diagnostic

Run:

```bash
python diagnostic.py
```

Expected output:

```text
Advanced Python Diagnostic
Advanced Learner is practicing: build readable, testable Python programs
Python status: ready
Git status: ready for first commit

Diagnostic complete.
```

**Instructor talk track**

"The exact blank line before 'Diagnostic complete' is okay. The report text ends with a newline, and then we print another line. The important part is that the script ran, wrote a file, read the file, printed the contents, and finished without a traceback."

Run:

```bash
ls data
```

Point out `diagnostic_report.txt`.

### Demo Step 5: Make the first commit

Run:

```bash
git status
git add diagnostic.py data/diagnostic_report.txt src/.gitkeep tests/.gitkeep reports/.gitkeep
git status
git commit -m "chore: initial setup"
git status
```

**Instructor talk track**

"Notice the order. I check status before staging. I stage the files I want. I check status again. Then I commit with a short message. The message `chore: initial setup` is not magic. It is just clear. It says this commit is setup work, not a feature."

"For today's lab, it is also acceptable to use `git add .` if you are sure you are in the project folder and only have relevant files. I am showing explicit file names to reinforce awareness."

"After the commit, `git status` should say that there is nothing to commit or that the working tree is clean. If it does not, read the message. Git usually tells you what it sees."

### Demo Step 6: Optional push explanation

Only do this if a remote is configured and appropriate in your environment. Otherwise explain verbally.

**Instructor talk track**

"If a remote repository is configured, pushing would look like this:"

```bash
git push
```

"If Git says there is no remote, that is not a Python problem and it is not a failure for this hour. The completion standard for today is at least one commit pushed or saved locally, depending on the lab setup."

---

## Guided Practice Lab: Setup and Diagnostic (25 minutes)

Read the lab prompt aloud, then keep it visible. Learners should work in their own lab environment while you circulate.

### Lab Prompt for Learners

"Your task is to create a reliable starting point for Advanced Python. You will prove that you can use the lab environment, create files, organize a project folder, run a baseline Python script, and save your work with Git."

Complete these steps:

1. Launch the assigned LogicalLabs/CHOICE lab. If it does not open, check for a blocked pop-up.
2. Locate the Save and Suspend control. Do not use it yet unless you are stepping away.
3. Create a file named `course_preflight.txt`.
4. In `course_preflight.txt`, write:
   - your name
   - today's date
   - the current time
   - one sentence describing what you want to improve in Advanced Python
5. Save the file. Close and reopen the editor pane to confirm the file is still visible.
6. Create a project folder. Recommended name: `advanced_tracker`.
7. Inside the project folder, create these subfolders:
   - `src/`
   - `tests/`
   - `data/`
   - `reports/`
8. Add `.gitkeep` placeholder files in `src/`, `tests/`, and `reports/` so Git can preserve the standard folder structure in the first commit.
9. Initialize Git in the project folder.
10. Create `diagnostic.py` in the project root.
11. Write a diagnostic script that exercises:
    - a class
    - a dictionary
    - file write and read
    - exception handling
12. Run the script successfully.
13. Make a first commit with the message:

```bash
git commit -m "chore: initial setup"
```

14. If your lab repository has a remote configured and your instructor asks you to push, push the commit. Otherwise, a local commit is enough for Hour 1.

### Student Starter Commands

Learners may use these commands if the lab terminal supports them:

```bash
mkdir advanced_tracker
cd advanced_tracker
mkdir src tests data reports
touch src/.gitkeep tests/.gitkeep reports/.gitkeep
git init
```

Then after creating and running `diagnostic.py`:

```bash
python diagnostic.py
git status
git add diagnostic.py data/diagnostic_report.txt src/.gitkeep tests/.gitkeep reports/.gitkeep
git commit -m "chore: initial setup"
git status
```

### Student Diagnostic Script Option

Students may write their own diagnostic script, or use this version and personalize the `name` and `goal` fields:

```python
from pathlib import Path


class LearnerProfile:
    def __init__(self, name: str, goal: str) -> None:
        self.name = name
        self.goal = goal

    def summary(self) -> str:
        return f"{self.name} is practicing: {self.goal}"


def main() -> None:
    profile = LearnerProfile("Your Name", "your Advanced Python goal")
    status = {"python": "ready", "files": "ready", "git": "ready for first commit"}
    report_path = Path("data") / "diagnostic_report.txt"

    try:
        report_path.write_text(
            f"{profile.summary()}\nStatus: {status['python']}\n",
            encoding="utf-8",
        )
        print(report_path.read_text(encoding="utf-8"))
        print(f"Dictionary check: {status['git']}")
        print("Diagnostic complete.")
    except OSError as error:
        print(f"Could not write or read the diagnostic file: {error}")
    except KeyError as error:
        print(f"Missing expected key: {error}")


if __name__ == "__main__":
    main()
```

Expected output will vary by learner name and goal, but it should include:

```text
Diagnostic complete.
```

The script should also create:

```text
data/diagnostic_report.txt
```

---

## Instructor Circulation Guide

As learners work, circulate with a consistent pattern: environment, folder, Python, Git, reflection.

### Questions to ask at each station

Ask one or two questions per learner. Avoid turning every check-in into a long private lecture.

1. "Show me where your Save and Suspend control is."
2. "What folder are you currently in?"
3. "Where did you create `diagnostic.py`?"
4. "What command did you use to run the script?"
5. "What file did the script create?"
6. "What does `git status` say right now?"
7. "Did you commit yet, or only stage?"
8. "What is your personal learning goal for this week?"

### Fast diagnosis flow

If a learner is stuck, use this sequence:

1. "Read the exact message on the screen."
2. "What command did you just run?"
3. "What folder are you in?"
4. "What did you expect to happen?"
5. "What is the smallest thing we can test next?"

This models professional debugging. It also keeps you from immediately taking the keyboard and fixing everything for them.

### What to praise

Praise process, not just correct output:

- "Good job checking `git status` before guessing."
- "Nice, you read the traceback instead of deleting random code."
- "Good folder organization. That will help later."
- "I like that your commit message explains the checkpoint."
- "You used a specific exception type. That is an advanced habit."

---

## Common Pitfalls and How to Respond

### Pitfall 1: Pop-up blocked during lab launch

**Symptom**: Student clicks launch, but no lab appears.

**Instructor response**

"Check the browser address bar for a pop-up blocked icon. The lab often opens in a new tab. Allow pop-ups for this site, then launch once more."

Avoid letting the learner repeatedly click launch without checking the browser.

### Pitfall 2: Confusing file save with Save and Suspend

**Symptom**: Student says, "I saved it, so I can close the lab, right?"

**Instructor response**

"You saved the file. That protects the file inside the current lab session. If you are ending for the day or stepping away for more than about 15 minutes, use Save and Suspend to preserve the session."

Ask them to point to the Save and Suspend control again.

### Pitfall 3: Wrong working directory

**Symptom**: `python diagnostic.py` fails with a message like "No such file or directory."

**Instructor response**

"This is likely a folder location issue, not a Python issue. Run `pwd` and list the files in the current folder. We need to either move into the folder that contains `diagnostic.py` or run Python with the correct path."

Useful commands:

```bash
pwd
ls
cd advanced_tracker
python diagnostic.py
```

### Pitfall 4: Missing `data` folder

**Symptom**: The script fails when trying to write `data/diagnostic_report.txt`.

**Instructor response**

"The script expects a folder named `data`. Create that folder, then run the script again."

Useful command:

```bash
mkdir data
```

Then:

```bash
python diagnostic.py
```

### Pitfall 5: Wrong Python command

**Symptom**: `python diagnostic.py` is not recognized, or it runs the wrong version.

**Instructor response**

"Some environments use `python`, and some use `python3`. Try checking the version."

Useful commands:

```bash
python --version
python3 --version
```

Use whichever command reports Python 3 in the lab. Do not spend this hour teaching virtual environments in depth unless it is necessary.

### Pitfall 6: `git commit` fails because identity is not configured

**Symptom**: Git asks for `user.name` and `user.email`.

**Instructor response**

"Git needs a name and email to label the commit. Use the identity format required by your course or lab. If no specific identity is required, use your training name and training email."

Example:

```bash
git config user.name "Your Name"
git config user.email "your.name@example.com"
git commit -m "chore: initial setup"
```

If the course requires global configuration and the environment allows it, the commands may use `--global`, but local repository configuration is enough for this lab.

### Pitfall 7: Student runs `git add` but not `git commit`

**Symptom**: `git status` says changes are staged for commit.

**Instructor response**

"You have prepared the snapshot, but you have not recorded it yet. The next step is the commit."

Command:

```bash
git commit -m "chore: initial setup"
```

### Pitfall 8: Broad exception handling hides useful details

**Symptom**: Student uses `except Exception:` and prints only "error."

**Instructor response**

"That works as a rough safety net, but it hides the reason. In Advanced, we prefer specific exceptions when we know what might fail. For this script, `OSError` is useful for file problems, and `KeyError` is useful for missing dictionary keys."

Encourage them to print the error object:

```python
except OSError as error:
    print(f"File operation failed: {error}")
```

---

## Completion Criteria

Use these criteria to determine whether a learner has successfully completed Hour 1.

Required:

- The learner can launch the LogicalLabs/CHOICE lab.
- The learner can identify the Save and Suspend control.
- `course_preflight.txt` exists and contains name, date/time, and a personal goal or improvement statement.
- The project folder exists.
- The project folder contains `src/`, `tests/`, `data/`, and `reports/`.
- Git has been initialized in the project folder.
- `diagnostic.py` exists in the project root.
- The diagnostic script runs successfully.
- The diagnostic script exercises:
  - a class
  - a dictionary
  - file write/read
  - exception handling
- At least one Git commit exists locally, or the commit has been pushed if the lab requires a remote.

Recommended verification commands:

```bash
git status
git log --oneline -1
python diagnostic.py
```

Expected Git result:

```text
abc1234 chore: initial setup
```

The exact commit hash will differ for every learner.

---

## Optional Extensions for Fast Finishers

Keep optional work inside the scope of Hour 1. Do not move ahead into Hour 2 class design yet unless the whole room is ready.

### Extension 1: Add a `.gitignore`

Create a `.gitignore` file in the project root:

```text
__pycache__/
.venv/
venv/
*.db
reports/
```

Then commit it:

```bash
git add .gitignore
git commit -m "chore: add gitignore"
```

Instructor note: If the course expects generated reports to be submitted later, discuss whether `reports/` should be ignored. For Hour 1, this is optional and should not block completion.

### Extension 2: Create a virtual environment if allowed

Only use this if the lab environment allows virtual environments and learners are not struggling with the main setup.

```bash
python -m venv .venv
```

Activation differs by shell and operating system. Do not make activation troubleshooting the center of this hour. If activation creates confusion, pause the extension and return to the required criteria.

### Extension 3: Add a second diagnostic key

Ask fast finishers to add one new key to the `status` dictionary, such as:

```python
"course": "Advanced Python"
```

Then print it in the report and rerun the script.

This reinforces dictionary access without introducing new tooling.

---

## Quick Checks and Exit Ticket

Use these during the final five minutes. You can ask verbally, use chat, or have learners write answers in their notes.

### Quick check 1

**Question**: What is the difference between saving a file and using Save and Suspend?

**Expected answer**: Saving a file writes that file's contents to disk inside the lab. Save and Suspend preserves the full lab session state for returning later, especially at the end of the day or before breaks longer than about 15 minutes.

### Quick check 2

**Question**: What is the difference between `git commit` and `git push`?

**Expected answer**: `git commit` saves a checkpoint in the local repository history. `git push` sends local commits to a remote repository such as GitHub.

### Quick check 3

**Question**: In today's diagnostic script, why did we use a dictionary?

**Expected answer**: To confirm that we can store and retrieve values by key, which is a core Python skill used in configuration, JSON-like data, API responses, and many application structures.

### Quick check 4

**Question**: Why is it useful for the diagnostic script to be deterministic?

**Expected answer**: A deterministic script gives predictable output, which makes environment problems easier to spot and debug.

### Exit ticket prompt

"Before you leave Hour 1, write one sentence answering this: What is one habit you want to practice in Advanced Python that will make your code more professional?"

Examples:

- "I want to commit smaller working checkpoints."
- "I want to write clearer class responsibilities."
- "I want to read tracebacks more carefully."
- "I want to separate application logic from display code."

---

## Wrap-Up Script

**Instructor talk track**

"Let's bring it back together. Today we did not try to build a full application. We did something more foundational: we created a reliable starting point. You launched the lab, confirmed how saving works, located Save and Suspend, created a project folder, initialized Git, ran a Python diagnostic, and made a first commit."

"That may sound simple, but it is the base of the whole course. If your environment is unreliable, every later lesson feels harder. If your Git workflow is unclear, every experiment feels risky. If your baseline Python skills are rusty, larger object-oriented design will feel confusing. Today gives us a clean starting line."

"Remember the three habits from this hour."

```text
Know where you are.
Run small checks.
Commit working checkpoints.
```

"Know where you are means check your folder. Run small checks means run the script before changing five more things. Commit working checkpoints means preserve progress when the project is in a known good state."

"In the next hour, we will start moving from script thinking to design thinking. We will look at requirements and decide which classes should exist, what each object should know, and what each object should do. That is where Advanced Python begins to feel different from Basics: not just more code, but better organized code."

"Before the break, if you are stepping away for more than about 15 minutes, use Save and Suspend. If you are staying in the lab for the next hour, keep your project open and be ready to build on it."

---

## Instructor After-Class Notes

After the hour, record any patterns you noticed:

- How many learners had lab launch or pop-up issues?
- How many learners confused file save with Save and Suspend?
- How many learners could commit without Git identity configuration?
- Which Python baseline skill seemed weakest: class syntax, dictionaries, file I/O, or exception handling?
- Should Hour 2 start with a brief review of any setup issue before class design begins?

Use these observations to adjust the first five minutes of Hour 2. Keep the focus narrow: resolve only the setup blockers needed for class design, then move forward.
