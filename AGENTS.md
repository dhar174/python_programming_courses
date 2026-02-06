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
  
- **[`Basics/lessons/`](./Basics/lessons/lecture)** - Markdown source files for readable Lecture scripts + notes.
  - Lesson files should be created here following the naming pattern: `DayX_HourY_Basics.md`

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
   - Basic topics: `Basics/lessons/DayX_HourY_Basics.md`
   - Advanced topics: `Advanced/lessons/DayX_HourY_Advanced.md`

2. **Naming Convention**:
   - `Day1_Hour1_Basics.md` - Day 1, Hour 1 of Basic module
   - `Day3_Hour2_Advanced.md` - Day 3, Hour 2 of Advanced module

3. **Content Requirements**:
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

## Additional Resources

- **Marp Documentation**: https://marp.app/
- **Marp CLI**: https://github.com/marp-team/marp-cli
- **Python Institute**: https://pythoninstitute.org/
- **PEP 8 Style Guide**: https://pep8.org/
- **Markdown Guide**: https://www.markdownguide.org/

## Support

For questions or issues:
1. Check this AGENTS.md file for guidance
2. Review instructor runbooks for content questions
3. Check GitHub Issues for similar problems
4. Create a new issue using appropriate template

---

**Last Updated**: 2026-02-02  
**Repository**: https://github.com/dhar174/python_programming_courses
