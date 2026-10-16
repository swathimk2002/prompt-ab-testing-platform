# Project Plan — Prompt Versioning and A/B Testing Platform

## 1. Project Overview

This project aims to build a platform for managing AI prompt versions and comparing their performance through structured evaluation and A/B testing.

The platform will use Python, FastAPI, Groq, PostgreSQL, and Streamlit. It will be developed in small stages so that each component can be implemented, tested, and understood before moving to the next stage.

**Current status:** The GitHub repository, Python virtual environment, initial project structure, dependency installation, and initial documentation have been prepared. The application features listed below are planned work and should not be considered completed until implemented and verified.

## 2. Development Principles

The project will follow these principles:

1. Initialize GitHub and the development environment before application coding.
2. Keep the implementation modular and understandable.
3. Complete and verify one small task before moving to the next.
4. Use a fake model client for most automated tests to avoid unnecessary API calls.
5. Keep API keys and database credentials out of Git.
6. Commit and push completed work regularly.
7. Test statistical calculations with controlled examples.
8. Keep documentation consistent with the actual implementation.
9. Use VS Code breakpoints and Step Into when debugging is useful.
10. Introduce Docker only after the main application works locally.

Every function and class should have a multiline docstring directly below its definition explaining its purpose, parameters, return value, and relevant side effects or exceptions.

## 3. Planned Development Phases

### Phase 1 — Repository and Environment Setup

**Goal:** Prepare the project for development.

Tasks:

- Create the GitHub repository.
- Create and verify the `main` and `feature-dev` branches.
- Clone the repository and open it in VS Code.
- Create the Python `.venv` environment.
- Configure `.gitignore`.
- Create the initial application directories and files.
- Add `requirements.txt` and `.env.example`.
- Install dependencies and verify imports.
- Prepare the README, architecture document, and project plan.

**Verification:** Confirm the Python version, successful dependency imports, correct Git branch, and clean Git state after committing the setup.

**Status:** Repository, environment, initial structure, and dependencies have been prepared. Documentation updates are being completed and must be committed before this phase is marked fully complete.

### Phase 2 — Configuration and Application Foundation

**Goal:** Build the minimum foundation needed for the application.

Tasks:

- Load configuration from environment variables.
- Configure application settings.
- Add the initial FastAPI application.
- Add a health-check endpoint.
- Establish a consistent error-handling approach.
- Add initial pytest tests.
- Confirm that the application starts locally.

**Verification:** Start the application and call the health endpoint successfully. Run the initial automated tests.

### Phase 3 — Database Setup

**Goal:** Store application records persistently.

Tasks:

- Prepare PostgreSQL for local development.
- Configure the database connection through environment variables.
- Set up SQLAlchemy.
- Define the initial database models.
- Create the required tables or migrations.
- Add basic database operations and tests.

Planned data includes prompts, prompt versions, templates, experiments, evaluation records, and audit events.

**Verification:** Connect to PostgreSQL and verify that records can be created, retrieved, and updated as expected.

### Phase 4 — Prompt Registry and Versioning

**Goal:** Manage prompts and their history.

Tasks:

- Create prompts.
- Save prompt versions.
- Retrieve specific versions.
- Compare versions.
- Implement rollback to a previous version.
- Add reusable templates.
- Record important changes in an audit history.

**Verification:** Automated tests should demonstrate that versions remain distinguishable, rollback selects the intended version, and audit records are created appropriately.

### Phase 5 — Groq Client and Completion API

**Goal:** Generate model responses through a controlled backend.

Tasks:

- Check current Groq documentation for available models, limits, and applicable pricing.
- Select a verified model configuration.
- Load the API key securely.
- Implement a model-client interface.
- Implement the Groq client.
- Implement a fake client for tests.
- Add request validation and error handling.
- Implement `POST /v1/completions`.
- Record relevant request, response, latency, and usage information.

**Verification:** Test normal requests, invalid inputs, provider failures, and fake-client behaviour.

**Important:** Do not commit a real API key. Do not assume that token usage or cost is available if the provider response does not supply sufficient information.

### Phase 6 — Experiment Management and Variant Assignment

**Goal:** Run reproducible comparisons between prompt versions.

Tasks:

- Define experiment configuration.
- Select control and treatment prompt versions.
- Configure traffic allocation.
- Implement deterministic hash-based variant assignment.
- Keep assignments stable for a given assignment key and unchanged configuration.
- Record experiment status and configuration.
- Define the primary metric, guardrails, planned sample size, and analysis rules before evaluating the final results.

**Verification:** Repeated assignments should be reproducible, and experiment records should identify the correct prompt versions.

### Phase 7 — Evaluation Dataset and Runner

**Goal:** Evaluate prompts using labelled examples.

Tasks:

- Prepare a labelled synthetic customer-support dataset.
- Validate the dataset structure and labels.
- Separate development, few-shot, and held-out evaluation data.
- Prevent held-out examples from being repeatedly used to tune prompts.
- Build a small smoke test of approximately 20 examples.
- Run a pilot evaluation before expanding the workload.
- Save results and evaluation configuration.
- Create a manifest recording the dataset, prompt versions, model settings, and relevant evaluation details.
- Add safe caching and resume support for interrupted runs.

**Verification:** Confirm that evaluation runs use the intended data split and configuration, and that interrupted runs can resume without incorrectly duplicating completed work.

### Phase 8 — Metrics and Statistical Analysis

**Goal:** Compare performance using suitable statistical methods.

Tasks:

- Calculate accuracy.
- Calculate macro-F1.
- Generate a confusion matrix.
- Measure latency and error rate.
- Record token usage when reliable information is available.
- Calculate cost only from verified usage and pricing information.
- Implement Fisher's exact test for suitable independent binary outcomes.
- Calculate Wilson confidence intervals for individual proportions.
- Calculate a Newcombe-Wilson confidence interval for the difference between proportions.
- Define a defensible sample-size and minimum detectable effect calculation.
- Use the exact McNemar test for suitable paired offline correctness outcomes.
- Add guardrail checks.

The initial labelled classification evaluation will use accuracy as the primary metric, with macro-F1 and operational measurements as supporting metrics.

The analysis plan will specify a significance level of 0.05 and appropriate stopping rules. Repeated unplanned checks should not be used to stop an experiment simply because a favourable result appears.

**Verification:** Test statistical functions with small, controlled datasets whose expected results can be checked independently.

### Phase 9 — Streamlit Dashboard

**Goal:** Make experiment results understandable through a simple interface.

Tasks:

- Display available prompt versions.
- Show experiment configuration and status.
- Compare control and treatment metrics.
- Display confidence intervals and statistical test results.
- Show latency and error summaries.
- Display evaluation history.
- Present guardrail results and relevant warnings.

**Verification:** Confirm that the dashboard displays stored results accurately and does not present an unsupported winner.

### Phase 10 — Integration and Reliability Testing

**Goal:** Verify that the components work together.

Tasks:

- Test prompt management and rollback.
- Test experiment creation and assignment.
- Test the completion API.
- Test database operations.
- Test model-client failures.
- Test evaluation and resume behaviour.
- Test metric calculations and statistical analysis.
- Test API and dashboard workflows.
- Run the complete pytest suite.
- Fix and retest identified issues.

**Verification:** Record the test results and known limitations. Do not claim a feature works merely because its code exists.

### Phase 11 — Docker and Reproducible Setup

**Goal:** Make the working application easier to run in a consistent environment.

Tasks:

- Create a Dockerfile.
- Add Docker Compose configuration where appropriate.
- Configure application and database services.
- Document environment variables and startup commands.
- Test the setup from a clean environment.

**Prerequisite:** The core application must already work locally. Containerization should not distract from implementing the main functionality.

### Phase 12 — Portfolio and Final Review

**Goal:** Present the project clearly and honestly.

Tasks:

- Update the README to reflect the final implementation.
- Document architecture and setup instructions.
- Add screenshots of verified working features.
- Record a short demonstration video if practical.
- Document design decisions, limitations, and future improvements.
- Prepare resume bullet points based on actual completed work.
- Prepare interview questions and answers covering architecture, testing, prompt evaluation, statistics, trade-offs, and limitations.
- Review Git history and ensure secrets are not committed.
- Provide a concise progress summary for the professor or project reviewer.

**Verification:** A new user should be able to understand the project, follow the setup instructions, and distinguish completed features from planned improvements.

## 4. Statistical Evaluation Rules

The project will distinguish two evaluation designs.

### Independent A/B evaluation

The independent comparison is intended for suitable binary outcomes from separate control and treatment groups.

The planned analysis includes Fisher's exact test, a 0.05 significance level, Wilson confidence intervals, and a Newcombe-Wilson confidence interval for the difference in proportions.

The sample-size plan and minimum detectable effect must be documented using defensible assumptions before the final comparison.

### Paired offline evaluation

When both prompt versions are tested on the same labelled examples, the results are paired.

The planned method is the exact McNemar test for suitable paired binary correctness outcomes.

The independent and paired analyses must be reported separately because they answer different experimental questions.

## 5. Git and Documentation Workflow

- Work on `feature-dev` for the current development workflow unless the team later agrees to another approach.
- Check `git status` before committing.
- Stage only the files intended for the current commit.
- Use meaningful commit messages.
- Push completed commits to GitHub.
- Never commit `.env`, virtual-environment files, credentials, or other secrets.
- Update the documentation when implementation decisions change.
- Keep a record of completed tasks, test results, errors, and fixes.

A feature should be described as complete only after its expected behaviour has been verified.

## 6. Known Risks and Mitigations

| Risk | Planned mitigation |
|---|---|
| Groq API limits or model availability change | Verify current provider documentation before integration and use a fake client for most tests |
| API calls consume credits or fail | Start with a small smoke test and expand only after verification |
| Secrets accidentally enter Git | Use `.env`, `.gitignore`, and placeholder values in `.env.example` |
| Database configuration causes setup problems | Test the local database connection separately before integrating the full application |
| Held-out data leaks into prompt tuning | Keep development, few-shot, and held-out datasets separate |
| Statistical results are misleading | Predefine metrics, sample-size assumptions, analysis methods, and stopping rules |
| Evaluation is interrupted | Store progress and use a manifest with safe caching and resume behaviour |
| The scope becomes too large | Complete the core local workflow before optional deployment or advanced features |
| Documentation overstates progress | Update completion claims only after tests or direct verification |

## 7. Current Status

The initial repository and development environment have been prepared successfully.

Completed and verified:
- GitHub repository created, with `main` and `feature-dev` branches.
- Python 3.11 virtual environment created and verified.
- `.gitignore` configured to exclude the virtual environment and `.env` file.
- Initial application directory structure created.
- Project dependencies installed and checked successfully.
- README, architecture document, and project plan updated, committed, and pushed to `feature-dev`.

Latest documentation commit: `860e977` — Update project documentation and architecture.

The working tree was clean after the documentation commit was pushed.

The actual application features are not implemented yet. The FastAPI backend, database integration, prompt registry, Groq client, experiments, evaluation runner, statistical analysis, and dashboard remain planned work until they are implemented and tested.

## 8. Definition of Project Completion

The core project will be considered complete when:

- Prompt versions can be created, retrieved, compared, and rolled back.
- Experiments can be configured with reproducible variant assignment.
- The completion API can use the configured model client.
- Relevant results are stored persistently.
- The evaluation runner can execute and resume evaluations.
- Metrics and statistical tests work on validated inputs.
- The dashboard presents the stored results accurately.
- Automated tests cover important success and failure cases.
- Setup instructions work in a clean local environment.
- Documentation, screenshots, and the final demonstration reflect the verified implementation.