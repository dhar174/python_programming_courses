# Day 2, Hour 4: Checkpoint 1: Domain + Service Layer Milestone

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 2 (Hour 8 of 48)
- **Focus**: Integrating domain models and service logic into a cohesive milestone (Checkpoint 1)
- **Prerequisites**: Custom exceptions, Factory pattern, Class ergonomics, basic validation
- **Goal**: Review the rubric and expectations, grade progress efficiently, and have students deliver a stable core package that runs a demo script.

---

## 1. Instructor Talk Points (10–20 minutes)

**Instructor Talk Points:**

- **The Goal of Checkpoint 1**: "In professional development, we don't build massive systems in one go and hope they work at the end. We build them in stages, or milestones. Checkpoint 1 is your first major milestone: a stable, headless 'Core' library."
- **Layer Separation**: "By 'Core', we mean your domain models (the 'nouns' of your app) and your service layer (the functions that create, read, update, and delete those models). Notice what isn't included: no GUI, no database, no HTTP APIs. If your core logic is solid, attaching a UI later is trivial."
- **Checkpoint Expectations and Rubric**:
  - **Models**: "You need at least 2 model classes (e.g., `Task` and `Category`) OR 1 model and 1 helper class (e.g., `Record` and `Validator`)."
  - **Service Layer**: "You need functions to add, list, search, update, and delete."
  - **Exceptions**: "I expect to see your custom exceptions raised when I try to save invalid data."
  - **Serialization**: "Your objects must implement a `to_dict` or similar helper so we can save them to a file later."
- **Testing Approach**: "Before you call me over to grade, run your demo script. Does it show the 'Happy Path' (valid data works)? Does it show the 'Sad Path' (invalid data fails cleanly)?"

## 2. Live Demo: Fast Grading Procedure (5–10 minutes)

**Live Demo Steps:**

1. **Demonstrate the Grading Expectations**:
   *(Action: Open an example demo script that you will use to show what a "good" turn-in looks like.)*
   "When I grade your Checkpoint, here is precisely what I am going to do. I will run your main demo script."

   ```python
   # Demo: checkpoint_demo.py
   
   from services import TaskService
   from models import TaskFactory
   from error_handlers import ValidationError, NotFoundError
   
   print("--- Starting Checkpoint 1 Demo ---")
   
   service = TaskService()
   
   print("\n1. Happy Path: Adding valid records...")
   try:
       task1 = TaskFactory.from_dict({"title": "Buy Milk", "priority": 1})
       service.add_task(task1)
       print("Success:", task1)
   except ValidationError as e:
       print("Failed:", e)
       
   print("\n2. Sad Path: Missing required fields...")
   try:
       task2 = TaskFactory.from_dict({"priority": 2}) # missing title
       service.add_task(task2)
   except ValidationError as e:
       print("Caught expected validation error:", e)
       
   print("\n3. Sad Path: Updating a missing record...")
   try:
       service.update_task(999, {"title": "New Title"})
   except NotFoundError as e:
       print("Caught expected not found error:", e)
       
   print("\n4. Serialization Check...")
   print(task1.to_dict())
   ```

2. **Execute and Review**:
   *(Action: Run the script.)*
   "Notice how my demo script proves every requirement of the rubric is met without me having to dig through 500 lines of code? Make it easy for me to give you a perfect score."

## 3. Hands-on Lab: Checkpoint 1 Assessment (45–60 minutes)

**Lab Prompt for Students:**
"It is time to deliver Checkpoint 1: Build your Core Tracker Library."

1. **Review your existing code**: Ensure you have separated your models and your services.
2. **Implement Missing Pieces**:
   - Do you have custom exceptions?
   - Do you have a factory method or robust validation?
   - Do you have CRUD operations in your service layer?
3. **Write the Demo**: Create a small `demo.py` or script at the bottom of your file that proves your code handles both valid operations and expected errors cleanly.
4. **Deliverable**: A completed `src/` core module that runs end-to-end via your small demo script.

**Instructor: Circulate and check (Grading):**
- **Common Pitfall**: Are they using global variables (`global data_list`) everywhere instead of passing state or instantiating a service class?
- **Common Pitfall**: Do they have UI code (like `input()` or `print()` prompts) mixed directly inside their service methods? Remember, the service layer should *return* data or *raise* errors, while the UI layer handles `print()` and `input()`.
- **Common Pitfall**: Do they fail to handle 'missing records' (e.g., trying to delete an ID that doesn't exist just crashes with an `IndexError`)?
- *(Optional Extension for fast finishers: Wrap the service layer in a simple interactive loop (`while True: menu()`) to create a light CLI.)*

## 4. Quick Check / Exit Ticket (5 minutes)

- **Quick Check Question:** "What part of your base design are you happiest with, and why?"
  - *(Have 1-2 students share their answers to celebrate milestones.)*
- **Wrap-up:** "Congratulations on completing Checkpoint 1! You now have a stable foundation. Our next steps involve packaging this up properly, saving data dynamically to disk, and adding robust logging. See you in Session 3!"
