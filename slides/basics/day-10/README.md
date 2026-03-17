# Day 10 — Session 10: Intro to Object-Oriented Programming

**Course:** Python Programming (Basic)  
**Day:** 10 · Session 10  
**Hours covered:** 37–40  
**Slides:** [`day-10-session-10.html`](day-10-session-10.html) &nbsp;(62 slides)

---

## Session Overview

| Hour | Topic | Key Concept |
|------|-------|-------------|
| 37 | Intro to classes — objects, attributes, methods | Blueprint vs instance, `__init__`, `self` |
| 38 | Collections of objects + searching | List of objects, search by attribute, update |
| 39 | Basic encapsulation + data validation | Validation in methods, separation of concerns |
| 40 | Checkpoint 5 — Functions, modules & intro OOP | CLI Organizer across multiple files |

---

## Learning Outcomes

By the end of Session 10, learners can:

### Hour 37 — Intro to classes: objects, attributes, methods
- Create a basic class with `__init__`
- Define instance attributes using `self`
- Write and call methods on objects
- Instantiate multiple objects from one class

### Hour 38 — Collections of objects + searching
- Store a collection of objects in a list
- Search a list of objects by attribute value
- Update an object's attribute after retrieval
- Handle the "not found" case explicitly

### Hour 39 — Basic encapsulation + data validation
- Add validation logic inside class methods
- Use methods to enforce business rules in one place
- Return a status value (e.g., True/False) and let the caller show a message for invalid input
- Keep UI code separate from validation logic

### Hour 40 — Checkpoint 5: Functions, modules & intro OOP
- Demonstrate modular code organization across multiple files
- Use at least one custom class to store records
- Build a CLI application that adds, lists, and searches records

---

## Labs

| Hour | Lab | Timebox | Description |
|------|-----|---------|-------------|
| 37 | Contact Class | 30 min | Create `Contact` class with `__init__` and `display()`, store objects in a list |
| 38 | Refactor Contact Manager | 30 min | Replace dict-based contacts with `Contact` objects; implement search and update |
| 39 | Add Validation | 30 min | Add phone validation method; handle invalid input in menu without crashing |
| 40 | Checkpoint 5: CLI Organizer | 50 min | Menu-driven app with 3+ functions, 1 module, 1 class; add/list/search; no file I/O |

---

## Files

| File | Description |
|------|-------------|
| [`day-10-session-10.html`](day-10-session-10.html) | Self-contained HTML slide deck (62 slides) |
| [`index.html`](index.html) | Session index / landing page |
| [`README.md`](README.md) | This file |

---

## Navigation

Inside the slide deck, use:

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| Swipe left/right | Mobile navigation |

---

## Scope Guardrail

This session stays within the **Basics** course scope.

Topics coming **later in Basics**:
- Exception handling with try/except (Session 11)
- File I/O — reading and writing files (Session 11)
- More OOP patterns (Session 11–12)

Topics **excluded** (covered in the Advanced course):
- Inheritance and subclassing
- Magic/dunder methods beyond `__init__` (e.g., `__str__`, `__repr__`)
- `@property` decorators
- `@classmethod` / `@staticmethod`
- Multiple inheritance
- Abstract base classes (ABC)
- Lambda functions, list comprehensions, generators

---

*Generated from `Basics/lessons/slides/day-10/day-10-session-10.md`*
