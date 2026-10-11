<h1 align="center">🏠 Predictive Insight Engine</h1>

<p align="center">
  <b>Predicting house prices with Regression, Gradient Descent and Bias-Variance analysis</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Best%20Model-Polynomial%20(Degree%202)-2ea44f" alt="Best Model">
  <img src="https://img.shields.io/badge/Test%20R%C2%B2-0.966-2ea44f" alt="R2">
</p>

---

## 📌 Overview

**Predictive Insight Engine** is a supervised learning project that estimates house prices (in INR) from features such as area, bedrooms, bathrooms, location score, property age and distance from the city.

The project builds and compares **Simple, Multiple and Polynomial Regression** models, implements **Batch, Stochastic and Mini-Batch Gradient Descent from scratch**, and studies **overfitting, underfitting and the bias-variance trade-off** to explain *why* some models perform better than others.

**Duration:** 6 hours &nbsp;|&nbsp; **Role:** Junior Data Scientist at a real estate analytics firm

## 📑 Table of Contents

- [Objectives](#-objectives)
- [Dataset](#-dataset)
- [Project Workflow](#-project-workflow)
- [Results](#-results)
- [Key Findings](#-key-findings)
- [Business Insights](#-business-insights)
- [Visual Highlights](#-visual-highlights)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Deliverables](#-deliverables)
- [Limitations and Future Work](#-limitations-and-future-work)
- [Author](#-author)

## 🎯 Objectives

- Understand, implement and evaluate supervised learning algorithms, with a focus on regression.
- Compare Simple, Multiple and Polynomial Regression using MSE, MAE, RMSE, R² and Adjusted R².
- Validate the assumptions of Linear Regression using plots and statistical tests.
- Implement Batch, Stochastic and Mini-Batch Gradient Descent from scratch and compare them.
- Diagnose bias and variance, and select the model with the best balance.
- Translate the results into practical business insights.

## 📊 Dataset

- **File:** `data/house_price_data.csv` (4,200 houses, 12 columns)
- **Target:** `house_price_inr`
- **Data quality:** no missing values, no duplicate rows
- **Split:** 80% training (3,360 rows) and 20% testing (840 rows), `random_state=42`

| Feature | Description |
|---|---|
| `area_sqft` | Built-up area of the house (sq.ft) |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `location_score` | Location quality score (higher is better) |
| `age_years` | Age of the property in years |
| `distance_city_km` | Distance from the city centre (km) |
| `lot_size_sqft` | Plot size (sq.ft) |
| `has_garage` | 1 if the house has a garage, else 0 |
| `has_pool` | 1 if the house has a pool, else 0 |
| `renovation_years_ago` | Years since the last renovation |
| `house_price_inr` | **Target:** house price in INR |

> `house_id` is only an identifier and is dropped before modelling.

## 🧭 Project Workflow

| Part | Topic | Key Output |
|---|---|---|
| A | Conceptual understanding (theory) | [`docs/theory_concepts.pdf`](docs/theory_concepts.pdf) |
| B | Dataset understanding and preparation | Variables, EDA plots, train-test split |
| C | Simple Linear Regression | Regression line, slope and intercept, assumption checks |
| D | Model evaluation metrics | MSE, MAE, RMSE, R², Adjusted R² |
| E | Multiple Linear Regression | Coefficients, VIF, comparison with Simple LR |
| F | Polynomial Regression (degree 2 and 3) | Curve comparison, overfitting signs |
| G | Gradient Descent from scratch | Batch, SGD and Mini-Batch convergence and timing |
| H | Bias-variance and model diagnostics | Bias², variance, cross-validation, complexity curve |
| I | Final analysis and reporting | Final comparison, business interpretation, conclusion |

## 🏆 Results

All scores are on the **test set**. Errors are in lakh INR (1 lakh = 100,000).

| Model | R² | Adjusted R² | RMSE (lakh) | MAE (lakh) |
|---|---|---|---|---|
| Simple Linear Regression (area only) | 0.563 | 0.562 | 81.8 | 62.9 |
| Multiple Linear Regression | 0.918 | 0.917 | 35.5 | 26.0 |
| **Polynomial Regression (Degree 2)** 🏆 | **0.966** | **0.964** | **22.7** | **16.6** |
| Polynomial Regression (Degree 3) | 0.965 | 0.946 | 23.3 | 17.1 |

**Gradient Descent (Linear Regression, all features):**

| Method | R² | RMSE (lakh) | Convergence behaviour |
|---|---|---|---|
| Batch GD | 0.918 | 35.5 | Smooth and stable, needs the most epochs (about 50) |
| Stochastic GD | 0.916 | 36.0 | Very fast in epochs (about 2), but noisy |
| Mini-Batch GD | 0.916 | 35.8 | Smooth and fast (about 6 epochs), best balance |

All three Gradient Descent methods reach almost the same quality as the closed-form Multiple Linear Regression (R² 0.918).

## 🔍 Key Findings

- **Best model:** Polynomial Regression (Degree 2). It has the lowest test error and the lowest total error (Bias² + Variance).
- **Underfitting:** Simple Linear Regression is too simple. Train R² (0.572) and test R² (0.563) are both low, and its Bias² is the highest.
- **Overfitting:** Degree 3 shows early signs (variance about 5 times higher than Degree 2). Degree 4 with 1,000 features clearly overfits: train R² 0.978 but test R² only 0.927.
- **Complexity curve:** Test error follows a U-shape, with its minimum at Degree 2.
- **Gradient Descent:** Matches the closed-form solution. Mini-Batch GD gives the best balance of speed, stability and accuracy.
- **Assumptions:** Linearity, independence and normality of residuals hold reasonably well. Heteroscedasticity is present (error spread grows with price).

## 💼 Business Insights

**What drives price** (Multiple Linear Regression, other features fixed):

| Change | Effect on price |
|---|---|
| +1 point in location score | about +₹30.7 lakh |
| +100 sq.ft of area | about +₹13.8 lakh |
| Having a pool | about +₹4.5 lakh |
| +1 km distance from the city | about −₹1 lakh |
| +10 years of property age | about −₹6.6 lakh |

**How accurate is the best model?**

- Average house price in the test set: about ₹2.41 crore
- Typical error: about 6% (median), with an average error of about ₹16.6 lakh
- About 75% of predictions are within 10% of the real price, and 97% are within 20%

**Recommended use:** quick fair-price estimates, screening of under-priced or over-priced listings, and support for negotiations. The model should assist human valuers, not replace them.

## 🖼️ Visual Highlights

<table>
  <tr>
    <td align="center"><img src="images/03_correlation_heatmap.png" width="420"><br><sub>Correlation heatmap</sub></td>
    <td align="center"><img src="images/05_slr_regression_line.png" width="420"><br><sub>Simple Linear Regression line</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="images/15_overfitting_check.png" width="420"><br><sub>Train vs test R² by polynomial degree</sub></td>
    <td align="center"><img src="images/19_gd_comparison.png" width="420"><br><sub>Gradient Descent convergence and time</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="images/21_complexity_vs_error.png" width="420"><br><sub>Model complexity vs prediction error</sub></td>
    <td align="center"><img src="images/22_final_comparison.png" width="420"><br><sub>Final comparison of all models</sub></td>
  </tr>
</table>

More graphs are available in the [`images/`](images/) folder and notebook screenshots in [`screenshots/`](screenshots/).

## 📁 Project Structure

```
predictive-insight-engine/
├── data/
│   └── house_price_data.csv
├── notebooks/
│   └── predictive_insight_engine.ipynb   # main notebook (Parts B to I)
├── results/                              # result tables (CSV)
├── docs/
│   └── theory_concepts.pdf               # Part A: theory
└── README.md
```

## 🚀 Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/predictive-insight-engine.git
cd predictive-insight-engine
```

**2. Create a virtual environment (recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the notebook**

```bash
jupyter notebook notebooks/predictive_insight_engine.ipynb
```

> In VS Code, you can also open the notebook directly, select the `venv` kernel and click **Run All**. The notebook reads the data from `../data/house_price_data.csv`, so run it from inside the `notebooks/` folder.

**Tech stack:** Python, NumPy, Pandas, Matplotlib, Seaborn, SciPy, Statsmodels, Scikit-learn, Jupyter

## 📦 Deliverables

| Deliverable | Location |
|---|---|
| Source code (Jupyter Notebook) | [`notebooks/predictive_insight_engine.ipynb`](notebooks/predictive_insight_engine.ipynb) |
| Model evaluation results | [`results/`](results/) |
| Graphs and plots | [`images/`](images/) |
| Theory concepts (PDF) | [`docs/theory_concepts.pdf`](docs/theory_concepts.pdf) |
| Final report | [`report/final_report.pdf`](report/final_report.pdf) |
| Project video | [Watch here](PASTE-YOUR-VIDEO-LINK) |

## ⚠️ Limitations and Future Work

- The data has only 10 features. Details such as floor, neighbourhood name, house condition and market date are missing.
- The model is reliable only for houses of about 450 to 4,200 sq.ft, the range seen in the data.
- Errors in rupees are larger for expensive houses (heteroscedasticity).
- **Next steps:** try Ridge and Lasso regularization, tree-based models (Random Forest, Gradient Boosting), and retrain regularly with fresh market data.


## 🎥 Video Explanation

A short walkthrough of the project, explaining each task with its graphs and calculations, is available here:

👉 [Watch the project video](https://drive.google.com/file/d/1_gUDEX9_EsM9-7n0bSSlkXe7SW6lxnvW/view?usp=sharing)

