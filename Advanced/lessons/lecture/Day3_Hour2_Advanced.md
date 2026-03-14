# Advanced Day 3, Hour 2: Logging and Error Reporting (Practical)

## Learning Objectives
- Use the built-in `logging` module for diagnostics instead of print statements.
- Configure safe, informative error logging without spamming end users.

## Instructor Script & Talk Points

**(10–20 min)**

Now that our project holds multiple modules in a `src/` directory, simply using `print()` for everything becomes chaotic. Where did the print come from? When did it happen? Is it an error, or just informational? To answer these, we use Python's built-in `logging` module.

**Logging Levels:**
We organize logs by severity.
- `DEBUG`: Exhaustive details for developers.
- `INFO`: Normal operational events (e.g., "Server started.").
- `WARNING`: Something unexpected happened, but the app can recover.
- `ERROR`: A serious issue. A function failed.
- `CRITICAL`: A fatal error. The program usually must crash.

**Formatting and File Logging:**
You don't want logs to just vanish when the terminal closes. We use `logging.basicConfig()` to pipe our logs directly into a file, appending logs over time. We can format these logs to include timestamps and module names natively.

**Do Not Print Stack Traces to End Users:**
End users shouldn't see massive block of Python error text when they use your app. They should see a friendly error message like "Sorry, we couldn't load your document." Meanwhile, your app should quietly write the ugly, detailed traceback to a log file where developers can find and fix it later.

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Open up the service layer from your capstone project.
2. At the top of the file, insert `import logging` and set up a basic logger: `logger = logging.getLogger(__name__)`.
3. In your main entry script, add the configuration:
   ```python
   logging.basicConfig(level=logging.INFO, filename='logs/app.log')
   ```
4. Find an area where a `ValidationError` or `NotFoundError` is raised. Replace any `print()` statements with `logger.error("Item not found", exc_info=True)` or `logger.warning("Invalid input received")`.
5. Run the app, trigger the error on purpose, and open up `logs/app.log` to demonstrate the resulting formatted log output.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Add Logging**

1. Ensure you have a `logs/` directory in your project root, or programmatically secure its creation.
2. Add `logging.basicConfig` to your main demo script, configured to write logs to `logs/app.log`.
3. Instantiate a logger in your service layer using `logger = logging.getLogger(__name__)`.
4. Add at least three log calls across your service layer. Think about adding an `INFO` log when a record is successfully created, and an `ERROR` (or `WARNING`) when an exception is raised.
5. Trigger one of your errors via your main script and open `logs/app.log` to confirm the log was cleanly recorded.

**Optional Extension:**
Add custom string formatting to your config so that your log lines automatically prepend the current localized timestamp and the name of the module that generated the log.

**Completion Criteria:**
- The `app.log` file is successfully created and populated.
- User-facing error messages remain friendly, while developer logs contain technical stack details.

## Checkpoint

**(5 min)**

**Quick Check:** When should you log at `WARNING` versus `ERROR`?

*Expected answer:* `WARNING` is for when something unexpected happened but the application can safely proceed or recover (e.g., disk space is running somewhat low, or an API call took longer than expected). `ERROR` is when a specific operation actually failed and cannot finish its job.
