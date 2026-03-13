# Day 2, Hour 3: Pythonic Class Ergonomics (`repr`/`str`/equality) + Light Type Hints

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 2 (Hour 7 of 48)
- **Focus**: Improving model debuggability and readability with dunder methods and type hints.
- **Prerequisites**: Clear understanding of classes and `__init__`.
- **Goal**: Teach students how and why to implement `__repr__`, `__str__`, and basic type hints to make their code pleasant to work with.

---

## 1. Instructor Talk Points (10–20 minutes)

**Instructor Talk Points:**

- **The Problem with Default Objects**: "If you print a basic custom Python object, it looks like `<__main__.User object at 0x1034f5>`. This is mostly useless for debugging or displaying to users."
- **`__str__` vs. `__repr__`**: 
  - "`__str__` is for the **user**. It should be a readable, informal string representation."
  - "`__repr__` is for the **developer**. It should be an unambiguous representation of the object. Ideally, you should be able to copy the output of `__repr__` and recreate the object in code."
- **Type Hints**: "In older Python, you had to guess what type of argument a function expected. Now we have Type Hints (`str`, `int`, `list`, `dict`). They don't block runtime execution if you get them wrong—but they help your IDE catch errors before you run your code, and they document your intent perfectly for other developers."
- **Equality (`__eq__`)**: "By default, Python checks if two objects are the *exact same instance in memory*. Sometimes, we just want to know if two objects have the *same data values*. That's what `__eq__` is for."

## 2. Live Demo: Class Ergonomics (5–10 minutes)

**Live Demo Steps:**

1. **Setup the Baseline**:
   *(Action: Define a basic class without dunder methods or type hints.)*
   "Here's a standard class. When I print it, it’s not helpful."
   ```python
   # Demo: models.py
   class Task:
       def __init__(self, t_id, title):
           self.id = t_id
           self.title = title

   t1 = Task(1, "Buy Milk")
   print(t1)  # Output: <__main__.Task object at 0x...
   ```

2. **Add Ergonomics**:
   *(Action: Add `__repr__`, `__str__`, and type hints.)*
   "Let's add type hints so everyone knows `t_id` is an `int` and `title` is a `str`. And let's make it print nicely."
   ```python
   class Task:
       def __init__(self, t_id: int, title: str) -> None:
           self.id = t_id
           self.title = title
           
       # For developers (Logging, debugging)
       def __repr__(self) -> str:
           return f"Task(t_id={self.id}, title='{self.title}')"
           
       # For users (printing to terminal UI)
       def __str__(self) -> str:
           return f"[{self.id}] {self.title}"

       # Same Data = Equal Objects
       def __eq__(self, other: object) -> bool:
           if not isinstance(other, Task):
               return False
           return self.id == other.id and self.title == other.title
           
   t1 = Task(1, "Buy Milk")
   t2 = Task(1, "Buy Milk")
   
   print(t1)        # Output: [1] Buy Milk (calls __str__)
   print(repr(t1))  # Output: Task(t_id=1, title='Buy Milk') (calls __repr__)
   
   print(t1 == t2)  # Output: True (calls __eq__)
   ```

## 3. Hands-on Lab: Make Your Model Pleasant to Work With (25–35 minutes)

**Lab Prompt for Students:**
"Let's upgrade the models in your Tracker application."

1. **Add Dunder Methods**:
   - Add a `__repr__` method to your main model. Make it output a string that looks like code instantiation (e.g., `return f"Record(id={self.id}, name='{self.name}')"`).
   - Add a `__str__` method. Make it return a short, friendly summary suitable for a CLI menu.
2. **Add Type Hints**:
   - Add type hints to your model's `__init__` method.
   - Add type hints (`-> str:`, `-> int:`, etc.) to at least 3 methods or standalone functions in your codebase.
   *(Instructor Note: Remind them that `def create() -> None:` is how you hint a function that returns nothing.)*
3. **Write a Serialization Helper (Optional but recommended)**:
   - Add a `to_dict(self) -> dict:` method to your class that converts the object properties into a dictionary. This will be invaluable when we save records to files.

**Instructor: Circulate and check:**
- **Common Pitfall**: Are they overcomplicating typing? Tell them to keep it simple (`int`, `str`, `list`, `dict`). Avoid importing `typing` module complexities unless necessary.
- **Common Pitfall**: Are `__str__` or `__repr__` trying to print to the console? Remind them that dunder string methods must **return a string**, not call `print()`. Look for `TypeError: __str__ returned non-string (type NoneType)`.

## 4. Quick Check / Exit Ticket (5 minutes)

- **Quick Check Question:** "When would you (or your application) rely on the output of `__repr__` versus the output of `__str__`?"
  - *Answer:* We look at `__str__` output when displaying information to a user in a UI or standard `print()` statement. We look at `__repr__` when debugging, looking at objects inside lists/dictionaries, logging errors, or in the Python REPL.
- **Wrap-up:** "Great! Your code is starting to look professional, self-documenting, and robust. Now we are ready for our first major integration checkpoint."
