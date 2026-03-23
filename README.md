# 📉 Customer Churn Prediction
  Predicts which telecom customers are likely to leave using Random Forest (AUC: 0.84) on real IBM Telco data. Features SQL EDA, SMOTE class balancing, SHAP explainability, KMeans segmentation, and a               live interactive Streamlit web app deployed .

## Live Deployments
| App | URL |
|-----|-----|
| Streamlit Dashboard | https://customer-churn-prediction-kv.streamlit.app |
| REST API | https://churn-prediction-api-cbqf.onrender.com |
| API Docs | https://churn-prediction-api-cbqf.onrender.com/docs |

> Note: API is on free tier — first request may take 30 seconds to wake up.



## 🔍 What Makes This Unique
- **Live Streamlit App** — 3-tab interactive web app deployed via ngrok
- **Personalized Retention Recommendations** — dynamic suggestions based on each customer's specific risk factors (contract type, payment method, tenure)
- **SQL EDA** — same analysis done in both Python and SQL showing dual skill
- **SHAP Force Plot** — explains exactly *why* each customer is predicted to churn
- **KMeans Segmentation** — 4 customer risk segments with churn rates (0.035 → 0.547)
- **SMOTE** — handles 26.5% class imbalance for better churn recall
- **Revenue at Risk** — quantifies annual revenue impact of churning customers

## 📊 Dataset
IBM Telco Customer Churn — 7,043 customers × 20 features | Churn rate: 26.5%

## 🛠️ Tech Stack
Python · Random Forest · XGBoost · Scikit-learn · SHAP · SMOTE · SQLite · Streamlit · ngrok

## 📁 Project Structure
| File | Description |
|------|-------------|
| `churn-prediction.ipynb` | Full notebook — EDA, ML, SQL, SHAP, KMeans |
| `churn_app.py` | Streamlit web application |
| `requirements.txt` | Dependencies |

## 🔍 Key Sections
| # | Section | What it does |
|---|---------|-------------|
| 1 | Libraries + Load Data | IBM Telco CSV, data cleaning |
| 2 | EDA | 6 charts — churn by contract, charges, tenure, internet |
| 2b | SQL EDA | Same insights via SQL — CTEs, Window Functions, CASE WHEN |
| 3 | Feature Engineering | AvgMonthlySpend · IsNewCustomer · RiskScore · HasSupport |
| 4 | SMOTE | Class balancing — 1,495 → 4,139 churn samples |
| 5 | Model Comparison | LR · RF · Gradient Boosting · XGBoost pipeline |
| 6 | ROC Curve | All 4 models compared |
| 7 | Hyperparameter Tuning | RandomizedSearchCV on Random Forest |
| 8 | SHAP | Feature importance + beeswarm + force plot |
| 9 | KMeans | 4 customer segments via PCA |
| 10 | Streamlit App | Live deployment with ngrok |

## 📈 Model Results
| Model | AUC |
|-------|-----|
| Logistic Regression | 0.8283 |
| Random Forest | 0.8355 |
| Gradient Boosting | 0.8323 |
| XGBoost | 0.8315 |
| **Random Forest (Tuned)** | **0.8387** |

## 🗄️ SQL Highlights
```sql
-- High Risk Customer Tiers (CTE + CASE WHEN)
WITH risk_scored AS (
    SELECT *,
        CASE
            WHEN Contract='Month-to-month' AND tenure<=12
             AND MonthlyCharges>65 THEN '🔴 Very High Risk'
            WHEN Contract='Month-to-month' THEN '🟡 High Risk'
            ELSE '✅ Low Risk'
        END AS risk_tier
    FROM telco
)
SELECT risk_tier, COUNT(*), ROUND(AVG(Churn)*100,2) AS churn_pct
FROM risk_scored GROUP BY risk_tier
```

## 🔑 Key Insights
- Month-to-month contracts churn 3x more than 2-year contracts
- Electronic check payment customers have highest churn rate
- Customers with no OnlineSecurity + no TechSupport = highest risk
- New customers (tenure ≤ 6 months) are most volatile
- Top SHAP drivers: Contract · tenure · MonthlyCharges · TechSupport

## 🚀 Streamlit App Features
- **Tab 1** — Single customer prediction with personalized retention advice
- **Tab 2** — Batch CSV upload for bulk prediction
- **Tab 3** — Business strategy recommendations

## 💰 Business Impact
- Annual revenue at risk identified from churning customers
- If 30% retained → significant revenue saved
- Personalized recommendations per risk factor

## 👤 Author
**KAVIN VENKAT**
[LinkedIn](www.linkedin.com/in/kavin-venkat-1710s0202) 
[Streamlit](https://husbandless-marvin-roughish.ngrok-free.dev)
