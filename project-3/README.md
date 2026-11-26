<div align="center">

# 🚨 Risk Alert Classifier

### An Early-Warning System to Detect High-Risk Banking Customers

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

</div>

---

## 🎥 Project Explanation Video

▶️ **Watch the full walkthrough here:** [Click to watch on.....](<https://drive.google.com/file/d/1tC4P6y0gf3j0s6ZCmp04AXCU1Sj4kG00/view?usp=sharing>)

---

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Objectives](#-objectives)
- [📊 Dataset Description](#-dataset-description)
- [🛠️ Tech Stack](#️-tech-stack)
- [🔄 Project Workflow](#-project-workflow)
- [🤖 Models Implemented](#-models-implemented)
- [📈 Results](#-results)
- [💼 Business Interpretation](#-business-interpretation)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🚀 Run the Streamlit App](#-run-the-streamlit-app)
- [✅ Key Learnings](#-key-learnings)

---

## 📌 Project Overview

A digital banking platform wants an **early-warning system** that identifies **high-risk customers** who are likely to **default on payments** or **engage in fraudulent behavior**.

The dataset is **highly imbalanced**, because risky customers are a small minority. This project builds a **robust classification pipeline** that:

- ✅ Accurately identifies high-risk customers
- ✅ Handles class imbalance effectively
- ✅ Evaluates models using the right classification metrics
- ✅ Improves performance using hyperparameter tuning
- ✅ Provides a working **Streamlit web app** for live predictions

---

## 🎯 Objectives

| # | Objective |
|---|-----------|
| 1 | Understand classification metrics beyond accuracy |
| 2 | Prepare data using stratified split, scaling and **KNN Imputer** |
| 3 | Build a **Logistic Regression** baseline model |
| 4 | Handle imbalance using **Under-Sampling, Over-Sampling, SMOTE, ADASYN** |
| 5 | Train **Decision Tree** and **Random Forest** models |
| 6 | Tune models using **RandomizedSearchCV** and **GridSearchCV** |
| 7 | Evaluate using **ROC Curve and AUC-ROC** |
| 8 | Select the best model by **minimizing false negatives** |
| 9 | Deploy a **Streamlit app** |

---

## 📊 Dataset Description

- 📄 **File:** `Risk_Alert.csv`
- 🧾 **Records:** 4,600 customers
- 🎯 **Target:** `Risk Status` → `0` = Low Risk, `1` = High Risk

| Category | Features |
|----------|----------|
| 👤 Demographic | `age`, `gender`, `region`, `employment_type` |
| 💰 Financial | `annual_income_inr`, `credit_score`, `credit_utilization_ratio` |
| 💳 Credit Behavior | `missed_payments`, `avg_late_payment_days`, `cash_advance_count` |
| 🔄 Transactions | `monthly_transactions`, `monthly_spend_inr` |
| ⚠️ Risk Signals | `complaints_last_6m`, `failed_login_attempts`, `account_tenure_months` |

> ⚠️ The dataset contains **missing values** and is **highly imbalanced**.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Programming language |
| 🐼 Pandas, NumPy | Data handling |
| 📊 Matplotlib, Seaborn | Visualization |
| 🤖 Scikit-learn | Models, tuning, metrics |
| ⚖️ Imbalanced-learn | SMOTE, ADASYN, sampling |
| 🌐 Streamlit | Web app |
| 📓 Jupyter Notebook | Development |

---

## 🔄 Project Workflow

```text
Data Loading
     ↓
Missing Value Check
     ↓
Stratified Train-Test Split
     ↓
Encoding → Scaling → KNN Imputation
     ↓
Baseline Logistic Regression
     ↓
Imbalance Handling (Under / Over / SMOTE / ADASYN)
     ↓
Decision Tree & Random Forest
     ↓
Hyperparameter Tuning (Randomized + Grid Search)
     ↓
ROC-AUC Evaluation & Best Model Selection
     ↓
Streamlit App Deployment
```

---

## 🤖 Models Implemented

- 📈 Logistic Regression (Baseline)
- ⚖️ Logistic Regression + Under-Sampling
- ⚖️ Logistic Regression + Over-Sampling
- ⚖️ Logistic Regression + SMOTE
- ⚖️ Logistic Regression + ADASYN
- 🌲 Decision Tree
- 🌳 Random Forest
- 🔧 Tuned Decision Tree (RandomizedSearchCV)
- 🔧 Tuned Random Forest (RandomizedSearchCV)
- 🏆 Final Random Forest (GridSearchCV)

---

## 📈 Results

### 📊 Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| LR Baseline | `<value>` | `<value>` | `<value>` | `<value>` | `<value>` |
| LR + SMOTE | `<value>` | `<value>` | `<value>` | `<value>` | `<value>` |
| Decision Tree | `<value>` | `<value>` | `<value>` | `<value>` | `<value>` |
| Random Forest | `<value>` | `<value>` | `<value>` | `<value>` | `<value>` |
| 🏆 Final RF (Grid Search) | `<value>` | `<value>` | `<value>` | `<value>` | `<value>` |

### 🏆 Best Model

**`<Best Model Name>`** was selected because it achieved the **highest Recall**, which means it **misses the fewest high-risk customers**.

### 🔍 Key Findings

- ⚠️ The baseline model had high accuracy but **low recall** for high-risk customers.
- ⚖️ Balancing techniques (especially **SMOTE**) improved minority-class recall significantly.
- 🌳 Random Forest generalized better than a single Decision Tree (less overfitting).
- 🔧 Hyperparameter tuning improved F1-Score and AUC-ROC.

---

## 💼 Business Interpretation

| Error Type | Meaning | Business Impact |
|------------|---------|-----------------|
| ❌ **False Negative (Type-II)** | A risky customer is predicted as safe | 💸 Default or fraud loss, **most costly** |
| ⚠️ **False Positive (Type-I)** | A safe customer is flagged as risky | 😕 Extra checks, customer inconvenience |

> 🎯 Since missing a risky customer is more harmful, the final model was selected to **minimize false negatives (maximize Recall)**.

---

## 📁 Project Structure

## 📁 Project Structure

```text
project-3/
├── Data/
│   └── Risk_Alert.csv                          # Dataset
├── Notebook/
│   ├── app.py                                  # Streamlit web app
│   ├── Risk_Alert.ipynb                        # Full analysis & model building
│   └── risk_model.pkl                          # Saved final model + preprocessing
├── README.md                                   # Project documentation
└── Risk_Alert_Classifier_Project_Report.pdf    # Detailed project report (PDF)
```

| 📂 Folder / File | 📝 Description |
|---|---|
| `Data/` | Contains the dataset used in the project |
| `Notebook/` | Contains the notebook, the Streamlit app and the saved model |
| `README.md` | Project overview, setup steps and results |
| `Risk_Alert_Classifier_Project_Report.pdf` | Full project report with all details |

---

## ⚙️ Installation & Setup 

**1️⃣ Install required libraries**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn streamlit joblib
```

**2️⃣Run the notebook**

Open `Notebook/Risk_Alert.ipynb` and run all cells. This creates the `risk_model.pkl` file.

---

## 🚀 Run the Streamlit App

From the **project root folder**, run this in the terminal:

```bash
streamlit run Notebook/app.py
```

Then open 👉 **http://localhost:8501** in your browser.

### 🖥️ How to Use

1. Enter customer details in the **sidebar**
2. Click **🔍 Predict Risk**
3. See the result:
   - ✅ **Low Risk Customer**
   - ⚠️ **High Risk Customer** (with probability)

---

## ✅ Key Learnings

- 📌 Accuracy alone is misleading on imbalanced data
- 📌 Recall, F1-Score and AUC-ROC are better metrics for risk prediction
- 📌 Resampling must be applied **only on training data** to avoid data leakage
- 📌 Random Forest with tuning gives strong, stable performance
- 📌 Model selection should follow **business requirements**

---

<div align="center">

### ⭐ If you like this project, please give it a star! ⭐

Made with ❤️ using Python & Machine Learning

</div>