# AGENTS.md

## Project Overview

This repository contains instructional materials for a comprehensive Python Programming course package (96 hours). It includes two main modules:
- **Module 1: Python Programming (Basic)** – 48 Hours
- **Module 2: Python Programming (Advanced)** – 48 Hours

The content is primarily delivered as slides (generated with Marp), lecture scripts and notes, homework assignments as ipynb notebooks, and multiple choice questions. The course is aligned to the Python Institute certification pathway (PCEP and PCAP).

**Instructor:** Charles Niswander  
**Organization:** GlobalIT

## Repository Structure

### Root Directory

- **[`README.md`](./README.md)** - Main project documentation providing an overview of the 96-hour Python Programming course package, course structure, target audience, prerequisites, technical requirements, and certification alignment.
- **[`Python GIT Training Course Package.md`](./Python%20GIT%20Training%20Course%20Package.md)** - Detailed course package documentation.
- **[`.marprc.yml`](./.marprc.yml)** - Main configuration file for Marp slide generation. Specifies input directory (`./Basics/lessons`), output directory (`./_site/slides`), and output formats (PDF, PPTX, PNG images).
- **[`marp.config.mjs`](./marp.config.mjs)** - Alternative Marp configuration in ES module format (JavaScript). Defines settings like `inputDir`, `output`, `themeSet`, PDF options, and browser settings.
- **[`marp.config.ts`](./marp.config.ts)** - Marp configuration in TypeScript format for type-safe configuration.
- **[`Prompt.md`](./Prompt.md)** - Memory file for the current goals, specification, and deliverables.
- **[`Plans.md`](./Plans.md)** - Memory file for milestones and validation steps.
- **[`Architecture.md`](./Architecture.md)** - Memory file for guiding principles and constraints.
- **[`Implement.md`](./Implement.md)** - Implementation prompt that references `Plans.md` and `Architecture.md`.
- **[`Documentation.md`](./Documentation.md)** - Memory file for milestone status updates and key decisions.

### Long-Term Memory Files

Use these files together to keep long-running work coherent across handoffs:

- **Prompt.md**: Capture the mission, goals, specification, and deliverables at the start of an initiative.
- **Plans.md**: Track milestones plus the validation steps required for each milestone.
- **Architecture.md**: Record principles and constraints that should not drift.
- **Implement.md**: Write the active implementation prompt, explicitly referencing Plans.md and Architecture.md.
- **Documentation.md**: Log milestone status updates and decisions as work progresses.

### Directories

#### [`Basics/`](./Basics/)
Module 1 materials (Python Programming - Basic, 48 hours):

- **[`Basics/Instructor/`](./Basics/Instructor/)** - Instructor resources:
  - [`Python_Basics_Instructor_Runbook_4hr_Days.md`](./Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md) - Detailed instructor runbook with day-by-day, hour-by-hour breakdown of topics, learning objectives, and activities for the Basic module.
  
- **[`Basics/lessons/`](./Basics/lessons/slides/)**
  - Markdown files here are source files for Basic module slides.
  - Output directory for locally generated slides (contains placeholder files). This is where completed html, pptx, and pdf slide files will be saved.

  
- **[`Basics/themes/`](./Basics/themes/)** - CSS theme files for Basic module slides:
  - [`python-dark.css`](./Basics/themes/python-dark.css) - Dark theme for slides.
  - [`python-light.css`](./Basics/themes/python-light.css) - Light theme for slides.
  
- **[`Basics/lessons/lecture/`](./Basics/lessons/lecture)** - Markdown source files for readable Lecture scripts + notes.
  - Lesson files are organized one file per hour following the naming pattern: `DayX_HourY_Basics.md`
  - Example files: `Day1_Hour1_Basics.md` – `Day1_Hour4_Basics.md`, `Day2_Hour5_Basics.md` – `Day2_Hour8_Basics.md`, `Day3_Hour1_Basics.md` – `Day3_Hour4_Basics.md`
  - **All new sessions must use per-hour files** (not combined session files)

- **[`Basics/lessons/`](./Basics/lessons/assignments)** - IPNYB source files for homework assignment notebooks.

- **[`Basics/lessons/`](./Basics/lessons/quizzes)** - Source files for multiple choice quizzes.

- **Syllabus and Course Materials**:
  - [`Python Basics (48h) Syllabus (12x4h) — Pcep_pcap Aligned.pdf`](./Basics/Python%20Basics%20(48h)%20Syllabus%20(12x4h)%20—%20Pcep_pcap%20Aligned.pdf) - PDF version of the syllabus.
  - [`python_basics_48_h_syllabus_12_x_4_h_pcep_pcap_aligned.md`](./Basics/python_basics_48_h_syllabus_12_x_4_h_pcep_pcap_aligned.md) - Markdown version of the syllabus.
  - [`Python Programming - Basic.md`](./Basics/Python%20Programming%20-%20Basic.md) - Additional course documentation.

#### [`Advanced/`](./Advanced/)
Module 2 materials (Python Programming - Advanced, 48 hours):

- **[`Advanced/Instructor/`](./Advanced/Instructor/)** - Instructor resources:
  - [`Python_Advanced_Instructor_Runbook_4hr_Days.md`](./Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md) - Detailed instructor runbook with day-by-day, hour-by-hour breakdown of topics, learning objectives, and activities for the Advanced module.
  
- **[`Advanced/lessons/`](./Advanced/lessons/)** - Markdown source files for Advanced module slides:
  - [`01-intro-to-python.md`](./Advanced/lessons/01-intro-to-python.md) - Introduction to advanced Python topics.
  - Additional lesson files should be created here following the naming pattern: `DayX_HourY_Advanced.md`
  
- **[`Advanced/themes/`](./Advanced/themes/)** - CSS theme files for Advanced module slides:
  - [`python-dark.css`](./Advanced/themes/python-dark.css) - Dark theme for slides.
  - [`python-light.css`](./Advanced/themes/python-light.css) - Light theme for slides.

- **Syllabus and Course Materials**:
  - [`Python Advanced (48h) Syllabus (12x4h) — Pcap_path To Pcpp1.pdf`](./Advanced/Python%20Advanced%20(48h)%20Syllabus%20(12x4h)%20—%20Pcap_path%20To%20Pcpp1.pdf) - PDF version of the syllabus.
  - [`python_advanced_48_h_syllabus_12_x_4_h_pcap_path_to_pcpp_1.md`](./Advanced/python_advanced_48_h_syllabus_12_x_4_h_pcap_path_to_pcpp_1.md) - Markdown version of the syllabus.
  - [`Python Programming Advanced Global IT training package.md`](./Advanced/Python%20Programming%20Advanced%20Global%20IT%20training%20package.md) - Additional course documentation.
  - [`Python_Advanced_Instructor_Runbook_4hr_Days.pdf`](./Advanced/Python_Advanced_Instructor_Runbook_4hr_Days.pdf) - PDF version of the instructor runbook.

#### [`_site/`](./_site/)
Output directory for generated HTML/PDF slides:

- **[`_site/slides/`](./_site/slides/)** - Generated slide files in various formats (HTML, PDF, PPTX) created by the Marp build process.

#### [`.github/`](./.github/)
GitHub-specific configuration and automation:

- **[`.github/workflows/`](./.github/workflows/)** - GitHub Actions workflows:
  - [`marp-action.yml`](./.github/workflows/marp-action.yml) - CI/CD workflow for building and publishing slides to GitHub Pages. Triggers on pushes to `main` branch that affect lesson files or configuration.
  
- **[`.github/ISSUE_TEMPLATE/`](./.github/ISSUE_TEMPLATE/)** - Issue templates for GitHub:
  - [`add--scope-guardrails---basics-advanced--to-slides---notes.md`](./.github/ISSUE_TEMPLATE/add--scope-guardrails---basics-advanced--to-slides---notes.md)
  - [`build-slides--python-advanced--day-x.md`](./.github/ISSUE_TEMPLATE/build-slides--python-advanced--day-x.md)
  - [`build-slides--python-basics--day-x.md`](./.github/ISSUE_TEMPLATE/build-slides--python-basics--day-x.md)
  - [`coverage-audit--advanced-slides-vs-official-module-outline.md`](./.github/ISSUE_TEMPLATE/coverage-audit--advanced-slides-vs-official-module-outline.md)
  - [`coverage-audit--basics-slides-vs-official-module-outline.md`](./.github/ISSUE_TEMPLATE/coverage-audit--basics-slides-vs-official-module-outline.md)
  
- **[`.github/agents/`](./.github/agents/)** - Custom AI agent configurations:
  - [`frontend-slides-batch.agent.md`](./.github/agents/frontend-slides-batch.agent.md) - Agent for batch-generating HTML slides.
  - [`presentations-marp-writer.agent.md`](./.github/agents/presentations-marp-writer.agent.md) - Agent for writing Marp presentations.
  - [`presentations-orchestrator.agent.md`](./.github/agents/presentations-orchestrator.agent.md) - Agent for orchestrating presentation builds.
  - [`python_educator.agent.md`](./.github/agents/python_educator.agent.md) - Agent specialized in Python educational content.
  - [`technical-content-evaluator.agent.md`](./.github/agents/technical-content-evaluator.agent.md) - Agent for evaluating technical content quality.
  
- **[`.github/prompts/`](./.github/prompts/)** - Prompt templates:
  - [`create-agentsmd.prompt.md`](./.github/prompts/create-agentsmd.prompt.md) - Prompt template for creating AGENTS.md file.

## Configuration Files

### Marp Configuration

The repository uses Marp (Markdown Presentation Ecosystem) to generate slides from Markdown files. Three configuration files are available:

1. **`.marprc.yml`** (Primary) - YAML configuration used by CI/CD:
   - Input: `./Basics/lessons` (Note: currently only Basics module is configured for automatic builds)
   - Output: `./_site/slides`
   - Formats: HTML, PDF, PPTX, PNG
   - Features: PDF outlines, notes, loose YAML disabled

2. **`marp.config.mjs`** - JavaScript ES module configuration:
   - More flexible configuration options
   - Theme set locations: `./Basics/themes` and `./Advanced/themes`
   - Browser automation settings

3. **`marp.config.ts`** - TypeScript configuration:
   - Type-safe configuration alternative

## Setup and Development

### Prerequisites

- **Python 3.x**: For running course code examples and notebooks.
- **Node.js**: Required for building slides with Marp (if using local build).
- **Code Editor**: VS Code with "Marp for VS Code" extension recommended for live preview.

### Installation

Since `package.json` is not present in the repository, use `npx` to run Marp CLI directly:

```bash
npx @marp-team/marp-cli --version
```

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhar174/python_programming_courses.git
   cd python_programming_courses
   ```

2. **Install VS Code Marp extension (optional but recommended):**
   - Open VS Code
   - Install "Marp for VS Code" extension
   - Open any `.md` file in `Basics/lessons/` or `Advanced/lessons/`
   - Click the Marp preview icon to see live preview

## Development Workflow

### Source of Truth: Instructor Runbooks

Use the following runbooks as the primary source of truth for content creation:

- **Basics**: [`Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md`](./Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md)
- **Advanced**: [`Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`](./Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md)

These runbooks define:
- Day-by-day breakdown (12 days per module)
- Hour-by-hour topics (4 hours per day)
- Learning objectives
- Activities and exercises
- Assessment criteria

### Writing Lecture Scripts

Each hour receives its own dedicated Markdown file formatted for direct instructor delivery:

1. **Location**:
   - Basic topics: `Basics/lessons/lecture/DayX_HourY_Basics.md`
   - Advanced topics: `Advanced/lessons/lecture/DayX_HourY_Advanced.md`

2. **Naming Convention**:
   - `Day1_Hour1_Basics.md` - Day 1, Hour 1 of Basic module
   - `Day2_Hour5_Basics.md` - Day 2, Hour 5 of Basic module
   - `Day3_Hour2_Advanced.md` - Day 3, Hour 2 of Advanced module

3. **Per-Hour File Structure (Standard)**:
   All session content **must** be split into one file per hour. Do not combine multiple hours into a single file. This enables:
   - Granular instructional agent automation
   - Easy per-hour updates without touching adjacent hours
   - Clear curriculum traceability

   Example — Day 2, Session 2 files:
   - `Basics/lessons/lecture/Day2_Hour5_Basics.md` (String Fundamentals)
   - `Basics/lessons/lecture/Day2_Hour6_Basics.md` (String Methods)
   - `Basics/lessons/lecture/Day2_Hour7_Basics.md` (Input/Output + Type Conversion)
   - `Basics/lessons/lecture/Day2_Hour8_Basics.md` (Checkpoint 1 + Session Wrap-Up)

4. **Content Requirements**:
   - Comprehensive coverage of topics for that hour
   - Readable verbatim during instruction
   - Minimal paraphrasing required
   - Well-structured lecture notes and speaking guide
   - Code examples with explanations
   - Practice exercises where appropriate

### Writing Homework Assignment Notebooks

Create Jupyter notebooks (`.ipynb`) for hands-on coding assignments:

1. **Location**: 
   - `Basics/assignments/Basics_DayX_homework.ipynb`
   - `Advanced/assignments/Advanced_DayX_homework.ipynb`

2. **Content Sources**:
   - Use corresponding runbook for learning objectives
   - Reference lesson content from that day's hours
   - Target key concepts from each hour

3. **Requirements**:
   - One coding assignment notebook per day
   - Exercises should progressively build skills
   - Include problem descriptions, starter code, and test cases

### Autograder & GitHub Classroom Integration

Homework notebooks are graded automatically by the **Global Autograder**. Each assignment requires configuration files placed alongside the notebook.

1. **Required files per assignment** (e.g., Day 1):
   - `Basics/assignments/Basics_Day1_homework.ipynb` — the student notebook
   - `Basics/assignments/Basics_Day1_homework/criteria.json` — test specifications (command, stdin, expected_stdout, points)
   - `Basics/assignments/Basics_Day1_homework/setup.json` — dependency install, notebook-to-script conversion, file assertions
   - `Basics/assignments/Basics_Day1_homework/feedback.json` *(optional)* — custom feedback settings

2. **Workflow overview**:
    - The autograder workflow (`.github/workflows/autograder.yml`, introduced in PR #114) runs on push/PR to `main`, plus manual `workflow_dispatch`.
    - The workflow uses `webtech-network/autograder@v1`.
    - For v1 compatibility, CI generates `submission/.github/autograder/setup.json` at runtime and copies `Basics_DayX_homework.ipynb` into `submission/` for pre-flight file checks.
    - The workflow also parses `Basics_Day1_Quiz.html` and `Basics_Day2_Quiz.html` (from `Basics/quizzes/Basics_Day1/` or `Basics/quizzes/`) and writes consolidated grading summaries to `submission/.github/autograder/assignment_grades.json` and `submission/.github/autograder/quiz_grades.json`.
    - Quiz submissions are JSON answer exports (`Basics_Day1_Quiz_answers.json`, `Basics_Day2_Quiz_answers.json`) rather than notebook/script execution, unlike assignment grading.
    - Quiz answer exports are discovered from either the quiz subfolder (same directory as the HTML) or `Basics/quizzes/` root and must include `student_answers` with numeric string question IDs.
    - Exported quiz payloads can include metadata fields (`quiz_id`, `title`, `exported_at`) and `criteria_like_tests`; grading uses `student_answers` mapped against `expectedAnswers` embedded in the HTML quiz.
    - When the workflow is run manually via `workflow_dispatch`, it commits/pushes autograder output changes to a timestamped `autograder-results-*` branch.
    - `setup.json` installs `nbconvert`, converts the notebook to a Python script, and verifies the output file exists.
    - `criteria.json` defines test cases that run the converted script and compare stdout against canonical strings.
    - All outputs must be **deterministic** — no randomness, no live date/time, no unseeded state.
    - Numeric values must match the **exact precision** specified in `criteria.json` (e.g., `85.50`, not `85.5`).

3. **Notebook compatibility**:
   - Notebooks must be self-contained (no external files or state).
   - The kernel must be Python 3.x.
   - The final code cell should contain only standard Python (no IPython magics such as `%%writefile`) so that `nbconvert` can convert it directly into the grading script. If you want to show a `day1.py` example to students, use a Markdown fenced code block in the notebook, not notebook magics.

4. **Local testing**:
   ```bash
   # 1. Navigate to the assignment's config directory
   cd Basics/assignments/Basics_Day1_homework/

   # 2. Install dependencies and convert notebook (mimics setup.json)
   python -m pip install nbconvert
   jupyter nbconvert --to script ../Basics_Day1_homework.ipynb --output day1.py

   # 3. Run the script and check output
   python day1.py
   Compare output to the canonical strings in `criteria.json`.

5. **Important warnings**:
    - **Do not rename** the notebook, config files, or move the assignment directory — this will break the autograder workflow.
    - All config files must use the exact canonical file names (`criteria.json`, `setup.json`, `feedback.json`).
    - All paths in `setup.json` are relative to the config directory (`Basics/assignments/Basics_Day1_homework/`). The notebook sits one level up, so use `../Basics_Day1_homework.ipynb` to reference it.
    - Keep notebook filenames in the `Basics_DayX_homework.ipynb` / `Advanced_DayX_homework.ipynb` pattern so workflow runtime checks can find them.

### Writing Multiple Choice Quizzes

Create quiz files to assess understanding:

1. **Location**:
   - `Basics/quizzes/Basics_DayX_Quiz.md`
   - `Advanced/quizzes/Advanced_DayX_Quiz.md`

2. **Requirements**:
   - 20-40 questions per quiz
   - One quiz per day
   - Cover key concepts from all hours of that day
   - Include correct answers and explanations

### Editing Slides

1. Navigate to the appropriate lessons directory:
   ```bash
   cd Basics/lessons/
   # or
   cd Advanced/lessons/
   ```

2. Create or edit `.md` files following Marp syntax:
   ```markdown
   ---
   marp: true
   theme: default
   ---
   
   # Slide Title
   
   Content goes here
   
   ---
   
   # Next Slide
   
   More content
   ```

3. Use VS Code with Marp extension for live preview.

### Building Slides Locally

To replicate the CI build process locally:

```bash
# Build slides using the .marprc.yml configuration
npx @marp-team/marp-cli -c .marprc.yml

# Or build a specific file
npx @marp-team/marp-cli Basics/lessons/01-intro-to-python.md -o output.html

# Build with PDF output
npx @marp-team/marp-cli Basics/lessons/01-intro-to-python.md -o output.pdf --pdf

# Build with PPTX output
npx @marp-team/marp-cli Basics/lessons/01-intro-to-python.md -o output.pptx --pptx
```

### Watch Mode for Development

For continuous rebuilding during development:

```bash
# Watch for changes and rebuild automatically
npx @marp-team/marp-cli -w -c .marprc.yml
```

## Build and Deployment

### CI/CD Pipeline

The project uses GitHub Actions for automated builds (`.github/workflows/marp-action.yml`):

**Trigger Conditions**:
- Push to `main` branch
- Changes to `Basics/lessons/**.md`
- Changes to `Advanced/lessons/**.md`
- Changes to `.marprc.yml`
- Manual workflow dispatch

**Build Process**:
1. Checks out code
2. Sets up GitHub Pages
3. Uses `KoharaKazuya/marp-cli-action@v4` to build slides with `.marprc.yml` configuration
4. Uploads artifacts to `_site` directory
5. Deploys to GitHub Pages

**Output**:
- HTML slides
- PDF documents
- PPTX presentations
- PNG images

**Published URL**: Slides are published to GitHub Pages at the repository's Pages URL.

### Manual Deployment

If you need to deploy manually:

1. Build slides locally:
   ```bash
   npx @marp-team/marp-cli -c .marprc.yml
   ```

2. The output will be in `_site/slides/` directory.

3. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update slides"
   git push origin main
   ```

4. GitHub Actions will automatically deploy to Pages.

## Code Style and Standards

### Markdown Style

- **Follow standard Markdown syntax**
- **Marp-specific directives**:
  - Use `---` for slide separators
  - Front matter with `marp: true` to enable Marp
  - Theme selection with `theme: default` or custom theme names
- **Headers**: Use `#` for slide titles, `##` for section headers
- **Code blocks**: Use triple backticks with language identifier
  ```python
  def hello():
      print("Hello, World!")
  ```
- **Lists**: Use `-` for unordered, `1.` for ordered lists
- **Images**: Use `![alt text](path/to/image.png)` syntax

### Python Code Style

- **Follow PEP 8 guidelines** for all Python code snippets and examples
- **Naming conventions**:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
- **Documentation**: Use docstrings for functions and classes
- **Comments**: Explain complex logic, not obvious code
- **Imports**: Standard library first, third-party second, local last

### Jupyter Notebook Style

- **Clear cell organization**: One concept per cell
- **Markdown cells**: Use for explanations and instructions
- **Code cells**: Keep focused and testable
- **Output**: Include expected outputs for verification

## Pull Request Guidelines

### Before Submitting

1. **Test slides locally**: Ensure Markdown renders correctly
2. **Preview with Marp**: Use VS Code extension to check formatting
3. **Build locally**: Run `npx @marp-team/marp-cli -c .marprc.yml` to verify no errors
4. **Check links**: Verify all internal and external links work
5. **Validate content**: Cross-reference with instructor runbooks

### PR Title Format

Use descriptive titles indicating the module and change:

- ✅ "Basics: Add Day 1 Hour 1 lecture script"
- ✅ "Advanced: Update OOP design patterns slides"
- ✅ "Docs: Fix typos in README"
- ✅ "Config: Update Marp theme settings"

### PR Description

Include:
- **Summary**: Brief description of changes
- **Module**: Which module is affected (Basics/Advanced/Both)
- **Files changed**: List of key files modified
- **Testing**: How you verified the changes
- **Screenshots**: If applicable (especially for slides)

### Review Checklist

- [ ] Content aligns with instructor runbook
- [ ] Slides render correctly (no syntax errors)
- [ ] Code examples follow PEP 8
- [ ] Markdown formatting is consistent
- [ ] All links work correctly
- [ ] Images load properly (if applicable)
- [ ] No spelling or grammar errors

## Testing

### Manual Testing

1. **Slide Rendering**:
   ```bash
   npx @marp-team/marp-cli Basics/lessons/your-file.md -o test-output.html
   ```
   Open `test-output.html` in a browser to verify rendering.

2. **PDF Generation**:
   ```bash
   npx @marp-team/marp-cli Basics/lessons/your-file.md -o test-output.pdf --pdf
   ```
   Open `test-output.pdf` to verify PDF formatting.

3. **Theme Application**:
   Verify that themes from `Basics/themes/` or `Advanced/themes/` apply correctly.

### Jupyter Notebook Testing

1. **Run all cells**: Ensure no errors
2. **Verify outputs**: Check that outputs match expectations
3. **Test with fresh kernel**: Restart kernel and run all cells

## Common Tasks

### Adding a New Lesson

1. Create markdown file in appropriate directory:
   ```bash
   # For Basics
   touch Basics/lessons/DayX_HourY_Basics.md
   
   # For Advanced
   touch Advanced/lessons/DayX_HourY_Advanced.md
   ```

2. Add Marp front matter:
   ```markdown
   ---
   marp: true
   theme: default
   ---
   
   # Lesson Title
   
   Your content here...
   ```

3. Test locally with Marp

4. Commit and push to trigger CI build

### Adding a New Theme

1. Create CSS file in themes directory:
   ```bash
   touch Basics/themes/my-custom-theme.css
   ```

2. Define theme styles following Marp theme syntax

3. Reference in markdown front matter:
   ```markdown
   ---
   marp: true
   theme: my-custom-theme
   ---
   ```

### Updating Configuration

1. Edit `.marprc.yml` for primary configuration
2. Test locally to verify changes work
3. Commit and push - CI will use updated configuration

## Troubleshooting

### Slides Not Building

- **Check Marp syntax**: Ensure `---` slide separators are correct
- **Verify front matter**: Must include `marp: true`
- **Check file paths**: Ensure files are in correct directory
- **Review CI logs**: Check GitHub Actions workflow for error messages

### Theme Not Applying

- **Verify theme file exists**: Check `Basics/themes/` or `Advanced/themes/`
- **Check theme name**: Must match filename without `.css`
- **Review CSS syntax**: Ensure valid CSS in theme file

### PDF/PPTX Not Generating

- **Check configuration**: Verify `.marprc.yml` has `pdf: true` and `pptx: true`
- **Browser issues**: Marp requires headless browser for PDF generation
- **Memory constraints**: Large presentations may timeout

## Autograder & GitHub Classroom Integration

This repository is integrated with the **Global Autograder** for automated grading of Python assignments. The autograder provides automated feedback on student submissions, making it easier to assess homework assignments and exercises.

### Workflow Configuration

The autograder workflow is configured in [`.github/workflows/autograder.yml`](./.github/workflows/autograder.yml) and runs automatically on:
- Pushes to the `main` branch
- Pull requests targeting the `main` branch
- Manual `workflow_dispatch` from the Actions UI
- It uses `webtech-network/autograder@v1`, prepares runtime files under `submission/.github/autograder/` for v1 adapter compatibility, parses Day 1/Day 2 quiz HTML, writes consolidated grading summaries (`assignment_grades.json`, `quiz_grades.json`), and commits/pushes autograder output changes to timestamped `autograder-results-*` branches only for manual `workflow_dispatch` runs.

### How to Use the Autograder

#### Assignment Configuration Files

To use the autograder for your assignments, you need to create configuration files in your assignment directories:

1. **`criteria.json`** (Required): Defines the grading criteria and test cases for the assignment
2. **`setup.json`** (Optional): Specifies setup commands or environment configuration
3. **`feedback.json`** (Optional): Customizes the feedback messages provided to students

#### Template Configuration

The workflow is configured with the **`io` template preset** by default, which is ideal for Python scripts that use standard input/output. This template:
- Tests programs that read from standard input and write to standard output
- Compares actual output against expected output
- Provides detailed feedback on test case results

If you need a different testing approach, you can:
- Modify the `template_preset` value in `.github/workflows/autograder.yml`
- Use the `custom` template option for complete control over test execution

#### Documentation and Examples

For detailed information on configuring the autograder, including:
- How to write `criteria.json` files
- Available template presets
- Custom template creation
- Advanced configuration options

Please refer to the **official autograder documentation**:  
📚 [Global Autograder Getting Started Guide](https://github.com/webtech-network/autograder/blob/main/docs/system/getting_started.md)

### Example Use Cases

- **Homework Assignments**: Automatically grade student submissions from Jupyter notebooks converted to Python scripts
- **Practice Exercises**: Provide immediate feedback on coding exercises
- **GitHub Classroom**: Integrate with GitHub Classroom assignments for automated assessment
- **HTML Quizzes**: Grade Day 1/Day 2 exported answer JSON files and emit consolidated grading summaries (`assignment_grades.json`, `quiz_grades.json`)

## Additional Resources

- **Marp Documentation**: https://marp.app/
- **Marp CLI**: https://github.com/marp-team/marp-cli
- **Python Institute**: https://pythoninstitute.org/
- **PEP 8 Style Guide**: https://pep8.org/
- **Markdown Guide**: https://www.markdownguide.org/
- **Global Autograder**: https://github.com/webtech-network/autograder

## Support

For questions or issues:
1. Check this AGENTS.md file for guidance
2. Review instructor runbooks for content questions
3. Check GitHub Issues for similar problems
4. Create a new issue using appropriate template

---

**Last Updated**: 2026-02-11  
**Repository**: https://github.com/dhar174/python_programming_courses
