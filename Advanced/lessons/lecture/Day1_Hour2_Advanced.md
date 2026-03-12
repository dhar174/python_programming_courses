# Day 1, Hour 2: Designing Classes from Requirements

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 1 (Hour 2 of 48)
- **Focus**: Translating requirements into classes and responsibilities. Identifying where validation and business rules should live.
- **Goal**: Transition from writing script-like functions to Responsibility-Driven Design (RDD).

---

## 1. Designing Classes from Requirements (10-20 minutes)

**Instructor Talk Points:**

- **Responsibility-Driven Design:** "In professional Python, we don't just dump variables and dictionaries into a file and call it an app. We use 'Responsibility-Driven Design'. What does the object *know*? What does the object *do*?"
- **Separation of Concerns:** "A crucial principle you must adopt today: Keep your UI (User Interface) separate from your core logic. If your `User` class has `print()` or `input()` inside it, you've tangled UI with business logic. Your model shouldn't care if the user is in a terminal, a web browser, or a GUI."
- **Small and Testable:** "Keep your functions and methods small. A method should do one thing, and do it well. This makes it testable and easy to maintain."

## 2. Live Demo: Sketching a Domain Model (5-10 minutes)

**Live Demo Steps:**

1. **Requirements to Classes:**
   *(Action: Start a new file or use a whiteboard/comment block.)*
   "Let's say we are building a Task Tracker. Here are our requirements: Users can create tasks, assign priorities, and mark them as complete."
   "What classes do we need? Let's sketch it out."
   ```python
   # 1. Task
   #    - knows: title, description, priority, is_complete
   #    - does: complete(), update_priority()
   
   # 2. Project (or TaskManager)
   #    - knows: name, list of tasks
   #    - does: add_task(), get_pending_tasks()
   ```

2. **Basic Implementation:**
   *(Action: Write a simple class outline in Python.)*
   ```python
   class Task:
       def __init__(self, title, description, priority="Medium"):
           self.title = title
           self.description = description
           self.priority = priority
           self.is_complete = False
           
       def complete(self):
           self.is_complete = True
           # No print statements here! Just logic.
           
   # A simple service layer function using the class
   def display_task_summary(task):
       status = "Done" if task.is_complete else "Pending"
       print(f"[{status}] {task.title} (Priority: {task.priority})")

   t = Task("Learn Classes", "Study responsibility-driven design")
   display_task_summary(t)
   t.complete()
   display_task_summary(t)
   ```
   "Notice how the `Task` complete method just flips a boolean. It doesn't print 'Task marked complete!'. We leave the printing to a separate helper function. This is separation of concerns."

## 3. Hands-on Lab: Domain Modeling (25-35 minutes)

**Lab Prompt for Students:**

"It's time to start planning your capstone project—the Full-stack Tracker. You will model the core classes."

1. **Pick a Capstone Theme:** Choose a domain. Some examples: Tasks, Inventory, Contacts, Notes, or Expenses.
2. **Requirements List:** Jot down a short requirements list (5–8 bullets) detailing what your app needs to do.
3. **Class Blueprinting:** Define 3–5 core classes for your tracker using comments or a simple diagram. List what each class *knows* (attributes) and what it *does* (methods).
4. **Implementation:** Implement at least ONE of these classes in Python with an `__init__` method and at least one behavior method.
5. **Demonstration:** Write a small separate block of code testing the object (instantiating it and calling its method).

**Instructor: Circulate and check:**
- **Pitfall Warning:** Are students putting `input()` or `print()` inside their business objects? Correct this immediately. Remind them to keep UI separate from core logic.
- Are classes getting too complicated with massive inheritance trees? Keep it simple.

*Optional Extensions for fast finishers:*
- Add type hints for your model attributes.
- Implement the `__str__` magic method for a friendly display when the object is printed.

## 4. Debrief and Quick Check (5 minutes)

- **Debrief:** Have one or two students share what domain they picked and what their primary class looks like. Review whether the class has clear, separated responsibilities.
- **Quick Check Question:** "Where should validation or error messages live: in the UI layer, the service layer, or the model?"
  - *Answer:* Business rules and validation should live in the model or service layer, but displaying the actual error message format (printing to the screen or a GUI alert) belongs in the UI layer. The model raises an exception; the UI catches it and displays it nicely.
- **Wrap-up:** "Excellent planning. Now that we have basic objects, we need to protect them from bad data. Next hour, we will dive into properties, invariants, and custom exceptions to bulletproof our models."
