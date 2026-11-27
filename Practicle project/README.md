# 💳 Credit Card Fraud Detection: Supervised Learning

## 📌 Project Overview
Imbalanced classification (fraud = 0.17%) with threshold optimisation. Models: Logistic Regression, Random Forest, XGBoost (tuned).
Imbalance strategies: Original (class_weight), SMOTE, Random Undersampling. Primary metric: **PR-AUC**.

## 📂 Dataset
Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
(284,807 transactions; 50,000 stratified sample used locally.) Dataset repo me upload nahi kiya gaya.

## 🎯 Optimal Threshold Used
**F1-optimal threshold = ___** (Precision = ___, Recall = ___, F1 = ___)
Pipeline me attribute `optimal_threshold` ke roop me saved hai.

## 📊 Key Results
| Model | Precision | Recall | F1 | PR-AUC |
|---|---|---|---|---|
| (final comparison table yahan paste karo) | | | | |

Net benefit per 50,000 transactions: Rs ___

## 🖼️ Screenshots
(PR curves, comparison table aur cost-benefit table ke screenshots yahan add karo)

## ▶️ How to Run
1. `pip install -r requirements.txt`
2. Kaggle se `creditcard.csv` download karke `Data/` folder me rakho
3. `FraudDetection_SupervisedLearning.ipynb` ko Jupyter/VS Code me open karke **Run All** karo
4. Saved model use karne ke liye:
   ```python
   import joblib
   pipe = joblib.load('fraud_detection_model.pkl')
   proba = pipe.predict_proba(new_data)[:, 1]
   label = (proba >= pipe.optimal_threshold).astype(int)
   ```

## 🎥 Video
((https://drive.google.com/file/d/1H1EQ2PkpKl6JO_ezVoy8xq71VHtCwsOf/view?usp=sharing))

## 📁 Files
- `FraudDetection_SupervisedLearning.ipynb`: fully executed notebook
- `fraud_detection_model.pkl`: saved sklearn Pipeline
- `summary_report.md`: theory + cost-benefit + observations
- `requirements.txt`