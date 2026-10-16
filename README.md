# Prompt Versioning and A/B Testing Platform

## About the Project

When building applications with large language models (LLMs), even a small change in a prompt can affect the quality of the response. However, it can be difficult to know which prompt works better without testing them properly.

This project aims to solve that problem by building a platform where different versions of prompts can be managed, tested, and compared using measurable results.

Instead of choosing a prompt based only on personal judgment, the platform will help evaluate its performance and make decisions based on the results.

I am building this project as part of my AI engineering learning journey, with a focus on prompt management, backend development, experimentation, and statistical evaluation.

**Current status:** The GitHub repository, initial project structure, Python virtual environment, and dependency installation have been completed and verified. The application features are still under development.

## What I Plan to Build

The platform is planned to include the following features:

- **Prompt versioning:** Save different versions of a prompt and keep track of changes.
- **Prompt rollback:** Restore an earlier prompt version when needed.
- **Prompt templates:** Create reusable prompt templates for different tasks.
- **Audit history:** Keep a record of important changes made to prompts and experiments.
- **A/B testing:** Compare two prompt variants to understand which performs better.
- **Consistent experiment assignment:** Use stable hash-based assignment so that requests can be assigned consistently to experiment variants.
- **Performance tracking:** Record model responses, response time, errors, and token usage when reliable information is available.
- **Statistical evaluation:** Compare results using appropriate statistical tests and confidence intervals.
- **Evaluation runner:** Support resumable evaluations, caching, and a manifest to track evaluation progress and results.
- **Interactive dashboard:** Display prompt versions, experiment progress, performance metrics, and comparison results.
- **Automated testing:** Test the main components and verify that they work as expected.

These features will be implemented gradually and tested as the project progresses.

## Technologies I Plan to Use

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Groq | Access to a language model |
| FastAPI | Build the backend API |
| PostgreSQL | Store prompts, experiments, requests, and results |
| Streamlit | Build the interactive dashboard |
| pandas and scikit-learn | Organize data and calculate evaluation metrics |
| SciPy and statsmodels | Perform statistical analysis |
| SQLAlchemy and psycopg | Connect Python to PostgreSQL |
| Pydantic and pydantic-settings | Validate data and manage application settings |
| pytest | Test the application |
| Git and GitHub | Track changes and manage the project |

## How the Platform Will Work

The planned workflow is:

1. Create a prompt and save its first version.
2. Make changes and save new versions without losing earlier ones.
3. Configure an experiment to compare two prompt variants.
4. Define the experiment settings and evaluation plan before analysing the results.
5. Send requests through the API and assign them consistently to the appropriate variant.
6. Send the selected prompt to the Groq model client and receive a response.
7. Store the response and relevant performance measurements in PostgreSQL.
8. Evaluate the results using performance metrics and statistical methods.
9. View the comparison in the dashboard and use the findings to decide whether a prompt change is worth keeping.

Groq will be used for live model requests. During development and automated testing, a simulated model client will also be used so that tests do not require a real API call every time.

## How I Plan to Evaluate Prompts

A prompt that produces a good response once may not perform well consistently. Therefore, the project will focus on measurable results rather than relying on a few examples.

The planned evaluation includes:

- **Accuracy:** The primary outcome for the main A/B experiment.
- **Fisher's exact test:** To compare success rates where appropriate.
- **95% confidence intervals:** To show the uncertainty around the results.
- **McNemar's exact test:** For suitable paired offline evaluations where both prompt variants are tested on the same examples.
- **Response latency:** To understand how quickly the model responds.
- **Error rate:** To track failed requests.
- **Token usage:** To measure usage when reliable information is available.

Before running the main experiment, I will plan the sample size and minimum detectable effect (MDE), where appropriate. The primary metric and analysis plan will be defined in advance. I will avoid repeatedly checking results and stopping early simply because one variant temporarily appears better.

The statistical analysis will consider the assumptions of the selected tests and the amount of data available. A higher score alone will not automatically be treated as proof that a prompt is better.

## Evaluation Dataset and Workflow

The project will use labelled customer-support examples to evaluate prompt performance.

The data will be separated according to its purpose:

- **Development data:** Used to develop and improve prompts.
- **Few-shot examples:** Used as examples within prompts when required.
- **Held-out evaluation data:** Reserved for evaluation and kept separate from prompt development to reduce data leakage.

The evaluation runner will track its configuration, progress, and results through a manifest. It will also support caching and resuming interrupted evaluations so that completed requests do not need to be repeated unnecessarily.

The held-out evaluation data will not be used to repeatedly adjust prompts or tune the experiment.

## Project Structure

```text
prompt-ab-testing-platform/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── experiments/
│   ├── metrics/
│   ├── stats/
│   └── dashboard/
├── data/
├── docs/
│   ├── architecture.md
│   └── project_plan.md
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The code is organized into separate folders so that API endpoints, database operations, prompt management, experiment logic, statistical analysis, and dashboard functionality can be developed and maintained independently.

## Setting Up the Project

### Requirements

- Python 3.11
- Git
- Visual Studio Code
- PostgreSQL for database-backed features
- A Groq API key for live model inference

### Create a virtual environment

On Windows, run:

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate
```

### Install the required packages

```bat
python -m pip install -r requirements.txt
```

### Configure the application

The `.env.example` file provides a template for the required environment variables. A local `.env` file will be used for settings such as the Groq API key, model name, and database connection.

The Groq model name and access details will be verified before live inference is implemented. PostgreSQL must also be installed or otherwise made available and configured before database-backed features can run.

API keys and passwords must remain private and must never be committed to GitHub.

## Testing

Automated tests will be added as each feature is developed.

The test suite can be run using:

```bat
python -m pytest
```

Testing will cover prompt version management, experiment assignment, API behaviour, database operations, metric calculations, statistical methods, and error handling.

I will test individual components first and then check whether the complete workflow works correctly. Simulated model responses will be used wherever possible to make testing repeatable and avoid unnecessary live API calls.

## Current Limitations and Future Work

The project is still in its initial setup stage. Prompt version management, database integration, live model requests, A/B experiment execution, statistical reporting, the evaluation runner, and the dashboard have not yet been implemented.

The project will be developed and tested incrementally. Once the local application works reliably, Docker-based setup and other deployment improvements can be considered.

The results will also depend on the quality of the evaluation data, the chosen metrics, the experiment design, and the available sample size. These limitations will be documented as the project develops.

## Project Goal

By completing this project, I aim to gain practical experience in building an AI application that goes beyond simply calling a language model.

I want to understand how prompts can be managed, tested, evaluated, and improved through a structured engineering workflow, and how statistical evidence can help make prompt-related decisions more reliable.