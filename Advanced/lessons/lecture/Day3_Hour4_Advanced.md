# Advanced Day 3, Hour 4: Decorators (Timing / Authorization / Validation)

## Learning Objectives
- Write and implement a Python decorator pattern to decouple shared functionality.
- Recognize when decorators reduce boilerplate and duplicated logic.

## Instructor Script & Talk Points

**(10–20 min)**

We've explored several patterns like Factories and Strategies. Today, we'll talk about *Decorators*. Decorators are a design pattern that allows us to modify or extend the behavior of a function or class without permanently modifying its source code. In Python, we invoke them with the `@` symbol right above a function declaration.

**Decorator Anatomy:**
A typical decorator is essentially a higher-order function: a function that takes *another* function as its argument and returns a new function (the "wrapper"). 
Inside a decorator, you define a `wrapper(*args, **kwargs)` function. This wrapper can execute code before and after calling the original function. The wrapper simply ends up passing through `args` and `kwargs` flexibly so you don't even have to rewrite the argument names.

**Keeping it Readable:**
Decorators should augment generic behavior. A common use is measuring benchmarking (timing how long a function runs), ensuring a user is logged in, or logging arguments. By doing this in a decorator, you don't muddy your service layer code with repetitive `start = time.time()` code in every single method. Keep decorators thin and readable!

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Create a slow function by importing the `time` module and calling `time.sleep(2)`.
2. Write a `@timed` decorator manually.
   ```python
   def timed(func):
       def wrapper(*args, **kwargs):
           start = time.time()
           result = func(*args, **kwargs)
           print(f"[{func.__name__}] took {time.time() - start:.3f}s")
           return result
       return wrapper
   ```
3. Stack the `@timed` above your slow function, and show how Python transparently runs the wrapper to calculate the duration.
4. Show a pseudo-code toy example of `@requires_api_key` to restrict access to a command layer.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Decorator Practice**

1. Inside your Capstone project, build your own `@timed` decorator.
2. Inside your `wrapper(*args, **kwargs)`, use your new `logging` setup from previous hours to log the execution duration alongside the `func.__name__` at the `INFO` or `DEBUG` level safely.
3. Attach this `@timed` decorator to at least two of your core service layer methods (such as retrieving your entire dataset or searching).
4. Make sure your `wrapper` properly executes `func` and explicitly `return`s the result. Run the scripts to review your `app.log` and verify the timing output is present and calculated dynamically. 

**Optional Extension:**
You'll notice that logging `func.__name__` gives you `wrapper` instead of the real name. Import `from functools import wraps`. Decorate your wrapper function natively with `@wraps(func)` to preserve the actual underlying function name correctly.

**Completion Criteria:**
- The decorator functions gracefully without breaking any methods, leaving the signatures transparently intact.
- The logger specifically outputs `INFO` execution benchmarks.

## Checkpoint

**(5 min)**

**Quick Check:** Inside the inner `wrapper` function, what specifically happens if your wrapper forgets to `return` the final result?

*Expected answer:* Any caller of the decorated function will unexpectedly receive `None`. The original function executes normally, but its original return value is thrown away because the wrapper swallowed it.
