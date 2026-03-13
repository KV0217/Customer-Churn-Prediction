# 📉 Customer Churn Prediction

Predicts which telecom customers are likely to churn using XGBoost (AUC: 0.86+) on real IBM Telco data. Features SMOTE balancing, SHAP explainability, KMeans segmentation, and a live interactive Streamlit web app.

## 🔍 What Makes This Unique
- **Live Streamlit App** — interactive web app for single + batch churn prediction
- **SHAP Force Plot** — explains exactly *why* each customer is predicted to churn
- **KMeans Segmentation** — groups customers into 4 risk segments via PCA
- **Feature Engineering** — AvgMonthlySpend, RiskScore, IsNewCustomer, ChargesPerTenure
- **SMOTE** — handles class imbalance for better recall on churn cases
- **Batch CSV Upload** — predict churn for multiple customers at once

## 📊 Dataset
IBM Telco Customer Churn — 7,043 customers × 21 features | Churn rate ~26.5%

## 🛠️ Tech Stack
Python · XGBoost · Scikit-learn · SHAP · Imbalanced-learn · Streamlit · Power BI

## 📁 Project Structure
| File | Description |
|------|-------------|
| `Customer_Churn_Prediction_FIXED.ipynb` | Full notebook |
| `churn_app.py` | Streamlit web application |
| `churn_final_dataset.csv` | Dataset for Power BI dashboard |
| `requirements.txt` | Dependencies |

## 🔍 Key Sections
| # | Section | What it does |
|---|---------|-------------|
| 1 | Libraries | All imports |
| 2 | Load Dataset | Real IBM Telco CSV from Kaggle |
| 3 | EDA | 6 charts — churn by contract, tenure, charges |
| 4 | Feature Engineering | 5 engineered features + RiskScore |
| 5 | SMOTE | Class imbalance handling |
| 6 | Model Comparison | LR, RF, Gradient Boosting, XGBoost |
| 7 | ROC Curve | All models compared |
| 8 | Hyperparameter Tuning | RandomizedSearchCV on XGBoost |
| 9 | SHAP | Feature importance + beeswarm + force plot |
| 10 | KMeans | 4 customer segments via PCA |
| 11 | Streamlit App | Live web app deployment |

## 📈 Results
| Model | AUC |
|-------|-----|
| Logistic Regression | ~0.78 |
| XGBoost | ~0.83.2 |
| Gradient Boosting | ~0.81 |
| Random Forest (tuned) | **0.8387+** |

## 🔑 Key Insights
- Month-to-month contracts have 3x higher churn rate than 2-year contracts
- Electronic check payment customers churn most
- New customers (tenure ≤ 6 months) are highest risk
- No OnlineSecurity + No TechSupport = strong churn signal
- Top SHAP drivers: Contract · Tenure · MonthlyCharges · TechSupport

## 🚀 Streamlit App Features
- **Tab 1** — Single customer prediction with risk factors
- **Tab 2** — Batch CSV upload and bulk prediction
- **Tab 3** — Business strategy recommendations

## 🖥️ Run Locally
```bash
pip install -r requirements.txt
streamlit run churn_app.py
```

## 👤 Author
**YOUR NAME**
[LinkedIn](www.linkedin.com/in/kavin-venkat-1710s0202)
