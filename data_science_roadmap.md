# Data Science Roadmap: Step-by-Step (Analytics-Leaning Track)

A linear, do-this-then-that path from zero to interview-ready for an **analytics-leaning DS role** (product analytics, growth/decision science, BI-adjacent DS). Check items off as you go. Timeline assumes ~10-15 hrs/week — adjust to your pace.

Each step lists **what to learn**, **tools to get hands-on with**, and a **checkpoint** so you know you're ready to move on.

---

## STEP 1: Programming & Git Basics
*(1-2 weeks)*

**Learn:**
- [ ] Python fundamentals: data types, control flow, functions, OOP basics, list/dict comprehensions
- [ ] Git & GitHub: commit, branch, push/pull, pull requests

**Tools:**
- [ ] Python (via Anaconda or plain pip + venv)
- [ ] Jupyter Notebook / Google Colab
- [ ] Git + GitHub account

**Checkpoint:** You can write a Python script with functions and loops from scratch, and push it to a GitHub repo.

---

## STEP 2: Math & Stats Foundations
*(2-3 weeks)*

**Learn:**
- [ ] Linear algebra: vectors, matrices, matrix multiplication, dot products
- [ ] Calculus: derivatives, gradients (conceptual — enough to understand gradient descent)
- [ ] Probability: conditional probability, Bayes' theorem, common distributions, expectation/variance
- [ ] Descriptive statistics: mean/median/variance, correlation vs. causation

**Tools:**
- [ ] NumPy (for matrix/vector operations)

**Checkpoint:** You can explain Bayes' theorem with an example, and compute mean/variance/correlation on a dataset by hand and in code.

---

## STEP 3: Data Manipulation in Python
*(2-3 weeks)*

**Learn:**
- [ ] Pandas: DataFrames, indexing, groupby, merge/join, pivot tables, missing data handling
- [ ] Data cleaning: outliers, duplicates, type conversion, string processing, categorical encoding
- [ ] Exploratory data analysis (EDA) workflow

**Tools:**
- [ ] Pandas, NumPy
- [ ] Matplotlib, Seaborn (basic charts: histograms, scatter, box plots, correlation heatmaps)

**Checkpoint:** Given a messy raw CSV, you can clean it, engineer a couple of features, and produce a short EDA summary with charts — unassisted.

---

## STEP 4: SQL (go deep — this is your top-priority skill)
*(3-4 weeks)*

**Learn:**
- [ ] SELECT, WHERE, GROUP BY, HAVING, ORDER BY
- [ ] JOINs: inner, left, right, full, self-join
- [ ] Subqueries and CTEs (WITH clauses)
- [ ] Window functions: ROW_NUMBER, RANK, LAG/LEAD, running totals
- [ ] CASE WHEN logic, aggregate functions

**Tools:**
- [ ] PostgreSQL or MySQL (local practice)
- [ ] One cloud warehouse: **Snowflake** or **BigQuery** (free tier) — increasingly expected hands-on, not just "SQL in general"
- [ ] Practice platforms: StrataScratch, LeetCode Database, DataLemur

**Checkpoint:** You can write a multi-table join with a window function (e.g., "rank each customer's orders by recency within their region") in under 5 minutes without looking anything up.

---

## STEP 5: Statistics & Experimentation
*(3-4 weeks)*

**Learn:**
- [ ] Hypothesis testing: t-tests, chi-square, ANOVA, z-tests
- [ ] A/B testing: experiment design, sample size/power calculation, statistical vs. practical significance
- [ ] Common A/B testing pitfalls: peeking, multiple comparisons, novelty effects, network effects
- [ ] Confidence intervals, p-values (and how to explain them in plain English)
- [ ] Basics of causal inference: confounders, correlation vs. causation

**Tools:**
- [ ] SciPy / statsmodels (Python)
- [ ] Awareness of experimentation platforms (Statsig, Amplitude, Optimizely) — conceptual familiarity is enough unless a target job lists one

**Checkpoint:** You can design an A/B test end-to-end for a hypothetical product change — including sample size, success metric, and how you'd interpret a null result — and explain it out loud in under 3 minutes.

---

## STEP 6: BI / Data Storytelling
*(1-2 weeks)*

**Learn:**
- [ ] Principles of good chart/dashboard design
- [ ] Turning a query result into a business recommendation, not just a number
- [ ] Building a dashboard that answers a specific business question

**Tools:**
- [ ] **Tableau** or **Looker** — pick one and build 2-3 real dashboards
- [ ] Plotly (for interactive charts in Python, optional)

**Checkpoint:** You have one polished, shareable dashboard (in Tableau or Looker) built on a real dataset, with a one-paragraph business narrative attached.

---

## STEP 7: Core Machine Learning
*(5-7 weeks)*

**Learn:**
- [ ] Supervised vs. unsupervised learning; bias-variance tradeoff; overfitting/regularization (L1/L2)
- [ ] Train/validation/test splits, cross-validation
- [ ] Feature engineering and selection
- [ ] Evaluation metrics: accuracy, precision, recall, F1, ROC-AUC, RMSE, MAE — and when to use which
- [ ] Algorithms: linear/logistic regression, decision trees, Random Forest, gradient boosting, KNN, Naive Bayes, K-Means, PCA
- [ ] Ensemble methods: bagging, boosting, stacking

**Tools:**
- [ ] scikit-learn (pipelines, GridSearchCV, preprocessing)
- [ ] XGBoost or LightGBM (very common in applied/business ML: churn, propensity, fraud)
- [ ] SHAP or feature-importance tools for interpretability

**Checkpoint:** You can build, tune, and evaluate a classification model (e.g., churn prediction) end-to-end from raw data to a business-readable output, and explain the bias-variance tradeoff from scratch.

---

## STEP 8: Applied GenAI / LLM Literacy
*(1-2 weeks)*

**Learn:**
- [ ] Practical LLM API usage: prompting, structured outputs, evaluating LLM output quality
- [ ] What embeddings are and how they're used
- [ ] What RAG (Retrieval-Augmented Generation) is, conceptually

**Tools:**
- [ ] OpenAI or Anthropic API (basic usage)
- [ ] A vector database at a conceptual/hands-on-basics level: **Pinecone**, **Weaviate**, or **pgvector**

**Checkpoint:** You can describe how a RAG system works end-to-end, and have made at least one API call to an LLM to solve a small task (e.g., summarizing or classifying text data).

**Why this step exists:** GenAI/LLM mentions in DS job postings grew from near-zero in 2023 to roughly a third of postings by 2026 — this is now baseline, not a specialization.

---

## STEP 9: Deep Learning (light touch for this track)
*(2-3 weeks — lighter than a DL-focused track)*

**Learn:**
- [ ] Neural network fundamentals: perceptrons, activation functions, backpropagation (conceptual)
- [ ] What CNNs and RNNs/Transformers are used for, at a high level

**Tools:**
- [ ] PyTorch (basic — "can read and lightly modify" depth is enough for this track)

**Checkpoint:** You can explain what a neural network is doing during training to a non-technical person, and have run one existing PyTorch example end-to-end.

---

## STEP 10: Cloud, Pipelines & Data Engineering Literacy
*(2-3 weeks)*

**Learn:**
- [ ] Batch vs. streaming pipelines (conceptual)
- [ ] What orchestration means (DAGs, scheduling)
- [ ] MLOps vocabulary: experiment tracking, model versioning, monitoring for drift

**Tools:**
- [ ] One cloud platform: **AWS**, **GCP**, or **Azure** — basic storage/compute/managed-DB familiarity
- [ ] **dbt** basics — signals you can transform data yourself, not just wait on data engineers
- [ ] **Airflow** basics — read and understand a DAG, don't need to build production pipelines
- [ ] Docker basics (optional, lighter priority for this track)

**Checkpoint:** You can describe what happens to data from raw ingestion to a dashboard, naming which tool would typically handle each stage.

---

## STEP 11: Coding & Algorithms (run in parallel from Step 1 onward)
*(Ongoing, ~2-3 hrs/week throughout)*

**Learn:**
- [ ] Data structures: arrays, hash maps, linked lists, stacks/queues, trees, graphs
- [ ] Algorithms: sorting, searching, recursion, two-pointer, sliding window, BFS/DFS, basic DP
- [ ] Big-O complexity analysis

**Tools:**
- [ ] LeetCode (easy-medium, Python)

**Checkpoint:** You can solve a medium LeetCode problem in Python in under 25 minutes and explain your solution's time complexity.

---

## STEP 12: Portfolio Projects
*(3-4 weeks, can overlap with Steps 7-10)*

**Build:**
- [ ] Project 1: A classic ML project on tabular data (e.g., churn or pricing model) with a clear business narrative, not just accuracy metrics
- [ ] Project 2: A project using a dataset you sourced and cleaned yourself, with a Tableau/Looker dashboard
- [ ] Project 3: A SQL/analytics storytelling piece — a real business question answered with SQL + visualization + a written recommendation

**Checkpoint:** All three projects live on GitHub with clean READMEs, and you can walk through each one's business impact in under 3 minutes.

---

## STEP 13: Interview-Specific Preparation
*(4-6 weeks)*

**Prepare:**
- [ ] Statistics/ML explainer drills: explain any algorithm or concept from Steps 5 & 7 from scratch, in under 2 minutes
- [ ] SQL speed practice: StrataScratch, DataLemur under time pressure
- [ ] Case study / product sense framework: clarify goal → define metrics → identify data needed → propose analysis/experiment → discuss tradeoffs
- [ ] Practice common prompts: "how would you measure success of X," "metric dropped 20%, how do you investigate?"
- [ ] Behavioral stories using the STAR method (a failed project, a stakeholder disagreement, a time data changed a decision)
- [ ] Mock interviews (with a peer, mentor, or platform like Pramp/Interviewing.io)

**Checkpoint:** You can complete a full 45-minute mock interview covering SQL, one ML concept, and a case study — without needing to look anything up mid-interview.

---

## Suggested Overall Timeline

| Steps | Focus | Duration |
|---|---|---|
| 1-3 | Programming, math, data manipulation | ~5-8 weeks |
| 4-6 | SQL, statistics, BI (your highest-leverage block) | ~7-10 weeks |
| 7-10 | ML, GenAI, DL, cloud/pipelines | ~10-15 weeks |
| 11 | Coding practice | ongoing throughout |
| 12-13 | Portfolio + interview prep | ~7-10 weeks (can overlap with 7-10) |

**Total: roughly 5-7 months** to go from scratch to genuinely interview-ready for an analytics-leaning DS role, at 10-15 hrs/week.

---

### How to use this checklist
Work top to bottom, but start Step 11 (coding practice) in parallel from week one — a little bit weekly beats a cram at the end. Steps 12 (portfolio) and 13 (interview prep) should start once Step 7 is done, running alongside Steps 8-10 rather than strictly after them.

---

## Free Video Resources (by step)

All full courses, all free, all on YouTube unless noted.

### Step 1 — Programming & Git
- [Python for Beginners – freeCodeCamp (full course)](https://www.youtube.com/@freecodecamp)
- [Corey Schafer – Python Tutorials](https://www.youtube.com/@coreymschafer) (excellent for OOP, functions, clean code habits)
- [Git & GitHub for Beginners – freeCodeCamp](https://www.youtube.com/@freecodecamp)

### Step 2 — Math & Stats Foundations
- [3Blue1Brown – Essence of Linear Algebra](https://www.youtube.com/@3blue1brown) (the best visual intuition for vectors/matrices you'll find anywhere)
- [3Blue1Brown – Essence of Calculus](https://www.youtube.com/@3blue1brown)
- [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) — the single best channel for visual, plain-English stats and probability explanations; use this constantly through Steps 2, 5, and 7
- [Khan Academy – Statistics and Probability](https://www.youtube.com/@khanacademy)

### Step 3 — Data Manipulation in Python
- [Corey Schafer – Pandas Tutorials](https://www.youtube.com/@coreymschafer)
- [Keith Galli – Complete Pandas Tutorial](https://www.youtube.com/@KeithGalli)
- [Luke Barousse – Python for Data Analytics (full course)](https://www.youtube.com/@LukeBarousse) — built around real job-posting data, very practical

### Step 4 — SQL
- [Alex The Analyst – SQL for Data Analysts (full playlist)](https://www.youtube.com/@AlexTheAnalyst) — widely regarded as the best free SQL-for-analytics series
- [freeCodeCamp – SQL Full Course](https://www.youtube.com/@freecodecamp)
- [techTFQ](https://www.youtube.com/@techTFQ) — great for window functions and interview-style SQL problems
- [Snowflake official YouTube – Getting Started](https://www.youtube.com/@SnowflakeInc) and [Google Cloud – BigQuery for beginners](https://www.youtube.com/@googlecloudtech) for warehouse basics

### Step 5 — Statistics & Experimentation
- [StatQuest – Hypothesis Testing & p-values](https://www.youtube.com/@statquest)
- [Luke Barousse / Ken Jee – A/B Testing explainers](https://www.youtube.com/@KenJee_ds)
- [365 Data Science – A/B Testing Free Course](https://www.youtube.com/@365DataScience)

### Step 6 — BI / Data Storytelling
- [Alex The Analyst – Tableau Full Course](https://www.youtube.com/@AlexTheAnalyst)
- [Tableau official YouTube – Tableau Training](https://www.youtube.com/@tableausoftware)
- [Looker/Google Cloud – Looker Basics](https://www.youtube.com/@googlecloudtech)

### Step 7 — Core Machine Learning
- [StatQuest – Machine Learning playlist](https://www.youtube.com/@statquest) — best visual explanations of every core algorithm (regression, trees, boosting, PCA, etc.)
- [Krish Naik – Complete Machine Learning Playlist](https://www.youtube.com/@krishnaik06)
- [freeCodeCamp – Machine Learning with Python (full course)](https://www.youtube.com/@freecodecamp)
- [StatQuest – XGBoost and Gradient Boosting explained](https://www.youtube.com/@statquest)

### Step 8 — Applied GenAI / LLM Literacy
- [3Blue1Brown – But what is a GPT? / attention mechanism visualized](https://www.youtube.com/@3blue1brown)
- [freeCodeCamp – Prompt Engineering / LLM full courses](https://www.youtube.com/@freecodecamp)
- [Andrej Karpathy – Let's build GPT / intro to LLMs](https://www.youtube.com/@AndrejKarpathy) (deeper dive if you want it, still free and excellent)

### Step 9 — Deep Learning (light touch)
- [StatQuest – Neural Networks playlist](https://www.youtube.com/@statquest)
- [3Blue1Brown – Neural Networks series](https://www.youtube.com/@3blue1brown)
- [freeCodeCamp – PyTorch for Deep Learning (full course)](https://www.youtube.com/@freecodecamp)

### Step 10 — Cloud, Pipelines & Data Engineering Literacy
- [freeCodeCamp – AWS/Azure/GCP Fundamentals (full courses)](https://www.youtube.com/@freecodecamp)
- [freeCodeCamp – Apache Airflow Tutorial](https://www.youtube.com/@freecodecamp)
- [dbt Labs official YouTube – dbt Fundamentals](https://www.youtube.com/@dbt-labs)

### Step 11 — Coding & Algorithms
- [freeCodeCamp – Data Structures and Algorithms in Python (full course)](https://www.youtube.com/@freecodecamp)
- [NeetCode – algorithm walkthroughs](https://www.youtube.com/@NeetCode) — the go-to channel for LeetCode-style explanations
- [Abdul Bari – Algorithms](https://www.youtube.com/@abdul_bari) (very strong for DP, graphs, and complexity intuition)

### Step 12 — Portfolio Projects
- [Ken Jee – Data Science Project from Scratch](https://www.youtube.com/@KenJee_ds)
- [Luke Barousse – Real-world Data Analyst Portfolio Project (SQL + Python)](https://www.youtube.com/@LukeBarousse)
- [Alex The Analyst – Data Analyst Portfolio Projects](https://www.youtube.com/@AlexTheAnalyst)

### Step 13 — Interview Prep
- [Ken Jee – Data Science Interview series](https://www.youtube.com/@KenJee_ds)
- [StrataScratch – free YouTube mock interview breakdowns](https://www.youtube.com/@stratascratch)
- [DataInterview / Exponent – DS case study walkthroughs](https://www.youtube.com/@tryexponent)

### General/anchor channels worth subscribing to for the whole journey
- **StatQuest with Josh Starmer** — best-in-class for visual stats/ML intuition, use throughout
- **freeCodeCamp** — full-length free courses on nearly everything above
- **Alex The Analyst** — SQL, Tableau, portfolio, and analytics-career-specific content
- **Ken Jee** — career roadmap, projects, and interview prep from an analytics-leaning lens (closest match to your track)
- **Luke Barousse** — practical, job-posting-data-driven Python/SQL/analytics content
- **3Blue1Brown** — unmatched visual intuition for the underlying math

*Note: search these channel names directly on YouTube if a link doesn't resolve — channel URLs occasionally change, but the names above are stable and easy to find.*
