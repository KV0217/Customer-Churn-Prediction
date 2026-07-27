# 📉 Customer Churn Prediction
  Predicts which telecom customers are likely to leave using Random Forest (AUC: 0.84) on real IBM Telco data. Features SQL EDA, SMOTE class balancing, SHAP explainability, KMeans segmentation, and a               live interactive Streamlit web app deployed .

## Live Deployments
| App | URL |
|-----|-----|
| Streamlit Dashboard | https://customer-churn-prediction-kv.streamlit.app |
| REST API | https://churn-prediction-api-cbqf.onrender.com |
| API Docs | https://churn-prediction-api-cbqf.onrender.com/docs |

> Note: API is on free tier — first request may take 30 seconds to wake up.

## Screenshots
### Streamlit Dashboard
![App Demo](https://raw.githubusercontent.com/KV0217/Customer-Churn-Prediction/main/screenshots/streamlit_churn_demo.png)

## What's Inside
- EDA with visualisations
- Feature engineering (RiskScore, AvgMonthlySpend, IsNewCustomer)
- SMOTE for class imbalance · 4-model comparison
- Hyperparameter tuning with RandomizedSearchCV
- SHAP explainability — per-customer force plots
- KMeans segmentation — 15x churn-rate gap between clusters (3.5%→54.7%)
- SQL EDA: CTEs, window functions, cohort analysis

## API Usage
```python
import requests
response = requests.post(
    "https://churn-prediction-api-cbqf.onrender.com/predict",
    json={
        "gender": "Male", "SeniorCitizen": "No", "Partner": "No",
        "Dependents": "No", "tenure": 2, "PhoneService": "Yes",
        "MultipleLines": "No", "InternetService": "Fiber optic",
        "OnlineSecurity": "No", "OnlineBackup": "No",
        "DeviceProtection": "No", "TechSupport": "No",
        "StreamingTV": "Yes", "StreamingMovies": "Yes",
        "Contract": "Month-to-month", "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 85.0, "TotalCharges": 170.0
    }
)
print(response.json())
```

## Sample Response
```json
{
  "churn_probability": 0.823,
  "risk_level": "high",
  "recommendation": "Immediate outreach — offer contract upgrade or discount",
  "risk_score": 5,
  "improvement_suggestions": [...],
  "summary": "3 area(s) identified for retention improvement"
}
```


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

## Tech Stack
Python · Pandas · Scikit-learn · XGBoost · SHAP · SMOTE · FastAPI · Docker · Streamlit · Power BI · SQLite · Render


## 📈 Model Results
| Model | AUC |
|-------|-----|
| Logistic Regression | 0.8283 |
| Random Forest | 0.8355 |
| Gradient Boosting | 0.8323 |
| XGBoost | 0.8315 |
| **Random Forest (Tuned)** | **0.8387** |


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
[LinkedIn](https://www.linkedin.com/in/kvsherly17100210) 
[Github](www.github.com/KV0217)
