# README: Question -> Data -> Insight in Data Science

## 1. Explaining the Lifecycle
In practice, data science is not a straight line from dataset to dashboard. It is a reasoning cycle:

- Start with a question worth answering.
- Gather and understand data that can act as evidence.
- Explore that evidence until you can produce an insight that supports a decision.

Each step shapes the next one. If the question is vague, data collection becomes random. If data is poorly understood, insights are fragile. If insights are not tied back to the question, analysis becomes interesting but not useful.

## Start with a clear question
A clear question defines the decision context. It tells us:

- Who needs the answer
- What action might change based on the answer
- What success looks like

For example, "How can we improve employee experience in the next quarter?" is clearer than "Analyze employee sentiment." The first version points to a timeline, an audience, and possible interventions. The second only asks for description.

This is critical because the question sets boundaries. It prevents us from collecting irrelevant data and over-analyzing metrics that do not affect real decisions.

## Data is evidence, not just a file
After defining the question, data becomes the evidence we use to test explanations. But before any modeling or charting, we need to understand what the data actually means.

Understanding data includes:

- Source: where it came from and how it was collected
- Structure: what each field represents and at what level (employee-level, department-level, monthly summary, etc.)
- Quality: missing values, duplicates, inconsistent labels, sampling bias, timing issues
- Relevance: whether this data can truly answer the question

This step matters because analysis quality is limited by evidence quality. Clean plots cannot fix misaligned or biased data.

## Insights emerge from exploration
Insights are not automatic outputs from tools. They emerge when patterns are interpreted in context.

An exploration might show that negative sentiment spikes in two departments. That is a finding. It becomes an insight only when we connect it to operational reality, such as workload peaks, manager turnover, or policy changes during the same period.

Useful insights have three properties:

- They answer the original question
- They explain "why this matters"
- They suggest a decision or next action

So the lifecycle is connected: question focuses the evidence, evidence supports exploration, and exploration produces actionable insight.

## Quick project checklist
To keep the lifecycle practical in real projects, use this short checklist:

- Write one decision-focused question before analysis begins.
- List the exact data sources and what each source proves.
- Record at least one data quality issue and how it was handled.
- Summarize the final insight in one sentence with a recommended action.

When these four points are documented, your analysis is easier to review, explain, and improve.


# Data Science Project Repository Guide

## Overview

This repository is designed to help readers understand how to effectively navigate and interpret a data science project. Rather than focusing only on code and outputs, this project emphasizes understanding the intent, structure, and decision-making behind the work.

The goal is to build the ability to read a repository as a cohesive story—connecting problem definition, data, analysis, and results.

---

## Objectives

By exploring this repository, you will learn how to:

* Understand the problem a data science project is solving
* Navigate a repository using its structure and documentation
* Identify different stages of the data science lifecycle
* Interpret notebooks and scripts with purpose
* Recognize assumptions, limitations, and gaps in analysis

---

## Project Structure

```
├── data/
│   ├── raw/              # Original datasets (unaltered)
│   └── processed/        # Cleaned and transformed data
│
├── notebooks/            # Jupyter notebooks for exploration & analysis
│
├── src/                  # Reusable scripts and core logic
│
├── models/               # Saved models or training outputs
│
├── reports/
│   ├── figures/          # Visualizations and plots
│   └── summaries/        # Key findings and insights
│
├── README.md             # Project overview and guide
└── requirements.txt      # Dependencies
```

---

## How to Approach This Repository

### 1. Start with the README

This file provides:

* Problem statement
* Dataset overview
* Approach and workflow
* Key insights

Ask yourself:

* Is anything missing?
* Does it clearly explain the project’s purpose?

---

### 2. Understand the Workflow

Follow the typical data science lifecycle:

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Modeling / Analysis
5. Evaluation
6. Reporting Insights

Try to map each folder or file to one of these stages.

---

### 3. Explore the Data

* Check the `data/` folder
* Identify raw vs processed data
* Look for assumptions (missing values, filtering, etc.)

---

### 4. Read Notebooks Strategically

When opening notebooks:

* Don’t focus on every line of code
* Look for:

  * Where data is loaded
  * How it is cleaned
  * Key transformations
  * Visualizations and conclusions

Focus on why steps were taken, not just how.

---

### 5. Review Code in `src/`

* Contains reusable logic
* Typically more structured than notebooks
* Helps separate experimentation from production-ready code

---

### 6. Analyze Outputs

Check:

* `models/` → trained models
* `reports/figures/` → visualizations
* `reports/summaries/` → conclusions

Ask:

* What insights were discovered?
* Are they clearly supported by the analysis?

---

## Key Things to Look For

### Assumptions

* Are there implicit assumptions about the data?
* Any preprocessing choices that could affect results?

### Limitations

* Missing data?
* Small dataset?
* Potential bias?

### Gaps

* What is not answered?
* What could be improved or extended?

---

## How to Contribute

When contributing:

* Do not modify raw data
* Add new analysis in separate notebooks
* Keep code modular inside `src/`
* Update documentation when adding features

Suggested contributions:

* Improve README clarity
* Add visualizations
* Extend analysis
* Refactor code

---

## Key Takeaways

After exploring this repository, you should be able to:

* Understand the goal of a data science project
* Navigate project structure with confidence
* Interpret analysis without getting lost in code
* Identify assumptions and missing pieces
* Contribute thoughtfully and responsibly

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Final Note

A data science repository is more than code—it is a record of decisions, experiments, and insights. Learning to read it effectively is a critical skill for real-world collaboration.

Focus on understanding the story behind the work, not just the files.

---

# Environment Verification Milestone (Python + Conda + Jupyter)

# Jupyter Kernel Control and Debugging Milestone

This milestone teaches you how to safely run, restart, and interrupt Jupyter kernels for reliable, reproducible analysis. Follow these steps to master kernel management:

## 1. Run Cells in Sequence
- Click each code cell and press Shift+Enter to run it.
- If you run a cell that uses a variable before the cell that defines it, you’ll get an error.
- Run cells in the correct order to see the expected output.

## 2. Restart the Kernel
- Use the Jupyter menu ("Kernel" > "Restart" or the circular arrow icon) to restart the kernel.
- After restarting, all variables and memory are cleared.
- Try running a cell that uses a variable before redefining it—you’ll get an error because the variable is gone.
- Rerun all cells from the top to restore the notebook state.

## 3. Interrupt Execution
- Run a cell with a long-running operation (like a loop with time.sleep).
- While it’s running, use the Jupyter menu ("Kernel" > "Interrupt" or the stop icon) to interrupt.
- Confirm that execution stops and the notebook remains responsive.

## 4. Decide When to Restart vs. Interrupt
- Use "Interrupt" if a cell is taking too long or is stuck.
- Use "Restart" if the kernel is unresponsive, or if you want to clear all variables and start fresh.
- If you see strange errors or unexpected variable values, restart and rerun all cells in order.

Practicing these steps will help you maintain a clean, predictable notebook state and debug issues systematically.

This section documents verification of the local Data Science setup.

## Verification Date
- 2026-03-24

## Operating System
- Windows 10

## 1. Python Verification
- Status: PASS
- Command:
  ```powershell
  python --version
  ```
- Output:
  ```text
  Python 3.11.9
  ```
- Command:
  ```powershell
  python -c "import sys,platform; print('executable:', sys.executable); print('platform:', platform.platform())"
  ```
- Output:
  ```text
  executable: C:\Users\Hi\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe
  platform: Windows-10-10.0.19045-SP0
  ```

## 2. Conda Verification
- Status: PASS
- Environment used: base
- Command:
  ```powershell
  C:\Users\Hi\miniconda3\Scripts\conda.exe --version
  C:\Users\Hi\miniconda3\Scripts\conda.exe env list
  ```
- Output:
  ```text
  conda 26.1.1

  # conda environments:
  #
  # * -> active
  # + -> frozen
  base                     C:\Users\Hi\miniconda3
  ```

## 3. Jupyter Verification
- Status: PASS
- Command:
  ```powershell
  C:\Users\Hi\miniconda3\python.exe -m jupyter --version
  ```
- Output:
  ```text
  Selected Jupyter core packages...
  IPython          : 9.11.0
  ipykernel        : 7.2.0
  jupyter_client   : 8.8.0
  jupyter_core     : 5.9.1
  jupyter_server   : 2.17.0
  jupyterlab       : 4.5.3
  nbconvert        : 7.17.0
  nbformat         : 5.10.4
  notebook         : 7.5.3
  ```

- Launch proof command:
  ```powershell
  C:\Users\Hi\miniconda3\python.exe -m jupyter notebook --no-browser --port 8899
  ```
- Launch output excerpt:
  ```text
  Jupyter Server 2.17.0 is running at:
  http://localhost:8899/tree?token=...
  http://127.0.0.1:8899/tree?token=...
  ```

- Notebook execution proof command:
  ```powershell
  C:\Users\Hi\miniconda3\Scripts\jupyter-execute.exe --inplace docs\jupyter_verification.ipynb
  ```
- Executed cell output (from notebook):
  ```text
  Jupyter verification successful
  ```

## Overall Verification Result
- Current state: FULLY VERIFIED
- Ready for sprint baseline: YES

## Milestone Completion Checklist
1. Python callable and stable: PASS
2. Conda environment available and listable: PASS
3. Jupyter installed and executable in Conda environment: PASS
4. Notebook cell executed successfully: PASS

---

# Jupyter Notebook Navigation & Management Milestone

This milestone ensures you can confidently launch, navigate, and manage Jupyter Notebooks in your project. Mastering these basics prevents common workflow mistakes and keeps your work organized.

## Why This Matters
- Prevents creating notebooks in the wrong folder
- Ensures your data, notebooks, and scripts stay organized
- Avoids confusion about environments and kernels

## What You Should Be Able to Do
1. **Launch Jupyter Notebook from the terminal**
   - Activate the correct Conda environment
   - Navigate to your project root
   - Run `jupyter notebook` and confirm it opens in your browser
2. **Understand the Jupyter Home interface**
   - Identify file/folder listing, navigation breadcrumbs, new file buttons, and file type indicators
3. **Navigate project folders**
   - Move into/out of directories
   - Locate your project folder and understand how navigation maps to your local file system
4. **Create and open a notebook**
   - Create a notebook in the correct folder
   - Confirm the correct Python kernel is active
   - Run a simple cell to verify execution
5. **Notebook file management basics**
   - Rename, save, close, and reopen notebooks safely

## Best Practices
- Always launch Jupyter from your project root to avoid misplaced files
- Double-check the folder before creating new notebooks
- Use meaningful names for notebooks
- Save and close notebooks before shutting down Jupyter

## Documentation
See `docs/jupyter_navigation_basics.ipynb` for a step-by-step walkthrough with screenshots.

## Data Organization

This project uses a disciplined folder structure to separate raw data, processed data, and output artifacts:

- **data/raw/**: Contains original, unmodified data files. Treat as read-only.
- **data/processed/**: Contains cleaned or transformed datasets derived from raw data.
- **data/output/**: Contains final results, plots, reports, or models.

**Why?**
- Prevents accidental overwrites and data contamination
- Supports reproducibility and auditability
- Makes it easy to identify data at each stage

See `data/README.md` for more details and best practices.

