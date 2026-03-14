# Advanced Day 3, Hour 1: Project Structure, Packages, Imports, and Config

## Learning Objectives
- Organize code into a proper Python package structure.
- Understand and avoid common import pitfalls (like circular imports).
- Configure applications using constants and lightweight environment variables.

## Instructor Script & Talk Points

**(10–20 min)**

Welcome to Day 3! Today, we take a major step forward in professional software development: organizing our work. As our project grows, throwing everything into one or two files just doesn't scale. 

**The `src` Layout Basics:** 
A professional Python application usually puts its core packages inside a `src/` directory. For example, `src/tracker/`. Why do we do this? It isolates your code and prevents accidental import shadowing. It keeps your repository root clean for meta-files like `README.md`, `tests/`, and `.gitignore`.

**Relative vs Absolute Imports:** 
- *Absolute imports* (`from tracker.models import Item`) reference the package from the very top level.
- *Relative imports* (`from .models import Item`) refer to relative locations within the same package.
- *Tip:* Use relative imports inside your package to keep modules tightly coupled and location-independent. Use absolute imports from the outside (like in `tests/` or a root entry script).
- *Pitfall:* If you try to run your module directly (e.g., `python src/tracker/models.py`), Python will complain about relative imports. Always run your code from the root of the project as a top-level script, or use the `-m` flag (e.g., `python -m src.tracker.demo`).

**Configuration:**
Don't hardcode absolute file paths or secrets. Manage configuration via a centralized `config.py` file for constants (like `DATA_DIR`), or use light environment variables via `os.environ.get('DATA_DIR', 'default_path')`.

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Start with `models.py` and `services.py` existing at the root of a folder.
2. Create the `src/` directory, and inside it, a `tracker/` directory.
3. Add a blank `__init__.py` inside `tracker/` to designate it as a package.
4. Move `models.py` and `services.py` into `src/tracker/`.
5. Adjust the imports. If `services.py` needs `models.py`, show how `from .models import ...` works.
6. Create an `app.py` at the root and run the package: `from src.tracker.services import TrackerService`. 
7. Run the `app.py` script to prove everything is wired up correctly. Alternatively, demonstrate the `python -m` execution model.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Restructure**

1. Create a `src/tracker/` package inside your repository, complete with an `__init__.py`.
2. Move your existing capstone files (`models.py`, `services.py`, etc.) into this package.
3. Update imports inside the files. Confirm they correctly import from one another without raising errors.
4. Update your main demo script to import from your new package structure.
5. Confirm the demo script still works as perfectly as it did before.

**Optional Extension:**
Add a `config.py` for defining simple, constant variables like `DATA_DIR` or `DB_PATH`, and update your services to pull from this config instead of hardcoded strings.

**Completion Criteria:**
- The project runs cleanly after the restructure.
- Dependencies between modules are resolved, and imports are clean and consistent.

## Checkpoint

**(5 min)**

**Quick Check:** What usually causes `ModuleNotFoundError` in student projects when they start restructuring?

*Expected answer:* Running the wrong entry file (running a script from inside a package directly instead of from the project root), creating circular imports, or naming a module the same name as a built-in standard library package.
