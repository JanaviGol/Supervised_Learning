# Credit Card Fraud Detection: Summary Report

## 1. Business Problem
Ek digital payments company (Paytm/Razorpay jaisi) me roz lakhon transactions hote hain aur sirf ~0.17% fraud hote hain.
Ek bhi fraud miss hone par lakhon rupaye ka nuksaan aur customer ka bharosa kam hota hai.
Standard accuracy yahan fail hoti hai, kyunki sab kuch "Not Fraud" bolne par bhi 99.83% accuracy mil jaati hai
jabki ek bhi fraud nahi pakda jaata. Isliye hum PR-AUC, Precision, Recall aur F1 (Fraud class) use karte hain.

## 2. Imbalance Handling
Maine 3 strategies test ki: Original (class_weight), SMOTE (fraud ko majority ka 10% tak) aur Random Undersampling (10%).
Logistic Regression par comparison me **___** ka PR-AUC sabse achha (___) raha, isliye Random Forest isi strategy par train kiya.
Test set ko kabhi resample nahi kiya gaya (sirf training data modify hua) taaki evaluation honest rahe.

## 3. Models aur Recommendation
Logistic Regression, Random Forest aur XGBoost (baseline + RandomizedSearchCV tuning) compare kiye.
Best model: **XGBoost Tuned** (PR-AUC = ___). Recommended threshold: **___** (F1-optimal),
jis par Precision = ___, Recall = ___, F1 = ___. Agar risk team ko Recall >= 0.90 chahiye to threshold ___ par
Recall ___ milta hai lekin Precision ___ tak girti hai.

## 4. Cost-Benefit Result
Assumptions: average fraud = Rs 4,500, investigation cost = Rs 150 per flagged transaction.
Recommended threshold par test set (10,000 transactions) me Net Benefit = Rs ___,
yaani **50,000 transactions par lagbhag Rs ___** ka net fayda.
Sabse zyada Net Benefit threshold ___ par mila, jo F1-optimal threshold se ___ (same / alag) hai.
Isse seekh: ML metrics aur business metrics alag ho sakte hain.

## 5. Production me kya improve karenge
- **Real-time scoring:** Model ko API (FastAPI) ke roop me deploy karke har transaction ko millisecond me score karenge.
- **Model drift monitoring:** Fraud patterns badalte rehte hain, isliye PR-AUC aur fraud rate ko regularly monitor karenge aur retrain karenge.
- **Feedback loop:** Analysts ke confirmed fraud/legit decisions ko wapas training data me daalenge.
- **Threshold review:** Business cost badalne par (fraud value, analyst cost) threshold dobara tune karenge.
- Zyada fraud examples (poora 284,807 dataset) aur cost-sensitive learning try karenge.
