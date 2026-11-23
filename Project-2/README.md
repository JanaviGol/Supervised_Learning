# 🏠 House Price Prediction using Machine Learning

![Banner](banner.png)

A complete end-to-end Machine Learning regression project that predicts **House Prices (in INR ₹)** using property attributes, location indicators, neighborhood safety, and proximity metrics, deployed with an interactive **Streamlit** web application[cite: 1, 3, 6].

---

## 📌 Table of Contents
- [📖 Project Overview](#-project-overview)
- [📊 Dataset Description](#-dataset-description)
- [🗂️ Project Workflow](#️-project-workflow)
- [🤖 Models & Techniques Used](#-models--techniques-used)
- [📈 Model Evaluation & Comparison](#-model-evaluation--comparison)
- [🌐 Streamlit Web Application](#-streamlit-web-application)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 How to Run Locally](#-how-to-run-locally)
- [📁 Project Structure](#-project-structure)
- [💡 Key Findings & Business Insights](#-key-findings--business-insights)

---

## 📖 Project Overview
Estimating accurate residential property prices depends on multiple structural, locational, and environmental factors[cite: 3]. This project explores and compares **Regularized Linear Models**, **Tree-Based Ensemble Models**, and **Support Vector Regression (SVR)** across multiple **Cross-Validation strategies** to build a reliable house price predictor[cite: 4, 5].

---

## 📊 Dataset Description
The real estate dataset contains historical property sale records with the following features[cite: 1, 3]:

| Feature | Type | Description |
| :--- | :--- | :--- |
| `property_id` | Identifier | Unique ID for each property (excluded from modeling)[cite: 1] |
| `sale_date` | Date | Date of property sale (`YYYY-MM-DD`)[cite: 1] |
| `area_sqft` | Numerical | Total built-up area in square feet[cite: 1] |
| `bedrooms` | Numerical | Number of bedrooms[cite: 1] |
| `bathrooms` | Numerical | Number of bathrooms[cite: 1] |
| `location_score` | Numerical | Neighborhood desirability score (1–10)[cite: 1] |
| `property_age` | Numerical | Age of the property in years[cite: 1] |
| `distance_city_km` | Numerical | Distance from the city center in kilometers[cite: 1] |
| `near_school` | Binary (`0`/`1`) | Whether a school is nearby[cite: 1] |
| `near_metro` | Binary (`0`/`1`) | Whether a metro station is nearby[cite: 1] |
| `crime_rate_index` | Numerical | Local crime rate index[cite: 1] |
| **`house_price_inr`** | **Target** | **Selling price of the house in INR (₹)**[cite: 1, 3] |

---

## 🗂️ Project Workflow

1. **🧠 Conceptual Foundation:** Analyzed L1 vs. L2 regularization, cross-validation techniques, and feature scaling requirements[cite: 2].
2. **🧪 Data Understanding & Preprocessing:** Checked missing values, separated features and target (`house_price_inr`), performed train–test split, and applied `StandardScaler` where required[cite: 3].
3. **📉 Regularized Linear Models:** Implemented **Ridge (L2)** and **Lasso (L1)** regression, tuned $\alpha$ via cross-validation, and compared coefficient shrinkage.
4. **🔁 Cross-Validation Strategies:** Evaluated model stability using:
   - K-Fold Cross-Validation[cite: 5]
   - Stratified K-Fold Cross-Validation (by binning target values)[cite: 5]
   - Leave-One-Out Cross-Validation (LOOCV)[cite: 5]
   - Time Series Split (ordered by `sale_date`)[cite: 1, 5]
5. **🌳 Tree-Based Models:** Trained **Decision Tree Regressor** (with `max_depth` and `min_samples` tuning) and **Random Forest Regressor**[cite: 5].
6. **📐 Support Vector Regression (SVR):** Built SVR models with Linear and RBF kernels and tuned hyperparameters ($C$, $\gamma$, $\epsilon$)[cite: 5].
7. **📊 Evaluation & Overfitting Analysis:** Compared all models using **MSE, MAE, RMSE, and $R^2$ Score**, inspecting train vs. test error gaps.
8. **🚀 Deployment:** Built an interactive **Streamlit** app for real-time house price estimation.

---

## 🤖 Models & Techniques Used
- **Linear Models:** Ridge Regression (L2), Lasso Regression (L1)[cite: 4]
- **Tree-Based Models:** Decision Tree Regressor, Random Forest Regressor[cite: 5]
- **Kernel Methods:** Support Vector Regression (`linear` & `rbf` kernels)[cite: 5]
- **Validation & Tuning:** `GridSearchCV`, `KFold`, `StratifiedKFold`, `LeaveOneOut`, `TimeSeriesSplit`[cite: 5]

---

## 📈 Model Evaluation & Comparison

> *(Update the table below with your final notebook output values)*

| Model | Train RMSE (₹) | Test RMSE (₹) | Test MAE (₹) | Test $R^2$ Score | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Ridge Regression (Tuned)** | `[___]` | `[___]` | `[___]` | `[___]` | Baseline Linear[cite: 4, 6] |
| **Lasso Regression (Tuned)** | `[___]` | `[___]` | `[___]` | `[___]` | Feature Selection[cite: 4, 6] |
| **Decision Tree (Tuned)** | `[___]` | `[___]` | `[___]` | `[___]` | Pruned Tree[cite: 5, 6] |
| **Random Forest (Tuned)** | `[___]` | `[___]` | `[___]` | `[___]` | Ensemble[cite: 5, 6] |
| **SVR (Tuned)** | `[___]` | `[___]` | `[___]` | `[___]` | Kernel Regressor[cite: 5, 6] |

---

## 🌐 Streamlit Web Application
The Streamlit interface allows users to enter property details (`area_sqft`, `bedrooms`, `bathrooms`, `location_score`, `property_age`, `distance_city_km`, `near_school`, `near_metro`, and `crime_rate_index`) via sliders and dropdowns to get an instant price prediction in **INR (₹)**.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Manipulation:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn
- **Web App / UI:** Streamlit[cite: 6]

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/house-price-prediction.git](https://github.com/your-username/house-price-prediction.git)
   cd house-price-prediction

🎥 Video Explanation

([Replace the placeholder URL below with your YouTube, Google Drive, or Loom walkthrough/demo link](https://drive.google.com/file/d/1hjysr8HIL2VMnIAWgYKMKhDuqmW1mp9U/view?usp=sharing))


📺 Project Walkthrough & Demo: Watch Video Explanation Here

house-price-prediction/
├── data/
│   └── house_prices.csv          # Real estate dataset[cite: 1, 3]
├── notebooks/
│   └── house_price_analysis.ipynb # Full EDA, CV, modeling & evaluation[cite: 6]
├── models/
│   └── best_model.pkl            # Saved best regressor & scaler
├── app.py                        # Streamlit web application[cite: 6]
├── banner.png                    # Project header banner
└── README.md                     # Project documentation

