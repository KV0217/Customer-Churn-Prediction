📉 Customer Churn Prediction

Predicts which telecom customers are likely to churn using Random Forest (AUC: 0.83+).
Built on IBM Telco dataset with SMOTE balancing, SHAP explainability, and deployed as a live Streamlit app.

🔗 Live Demo
[👉 Click here to open the app](https://husbandless-marvin-roughish.ngrok-free.dev/)

📊 Project Overview
- **Dataset:** IBM Telco Customer Churn — 7,043 customers × 21 features
- **Churn Rate:** 26.5%
- **Best Model:** Random Forest with 83.87%
- **Tuning:** RandomizedSearchCV — 25 combinations × 5-fold CV

🛠️ Tech Stack
          Python · Pandas · Scikit-learn · XGBoost · SHAP · Imbalanced-learn · Streamlit · Power BI

📁 Project Structure
            File                          - | Description |

 `Customer_Churn_Prediction_FIXED.ipynb`  - | Full notebook — EDA, models, SHAP, KMeans |
 `churn_app.py`                           - | Streamlit web app |
 `requirements.txt`                       - | Dependencies |
 `Churn prediction.pbix`                  - | Power BI |

🔍 Key Steps
        1. EDA       —   Churn by Contract, Tenure, Payment Method, Internet Service
        2. SMOTE     —   Balanced class imbalance for training
        3. Models    —   Logistic Regression, Random Forest, Gradient Boosting, XGBoost
        4. Tuning    —   RandomizedSearchCV on XGBoost
        5. SHAP      —   Feature importance + beeswarm + force plot
        6. KMeans    —   4 customer segments via PCA
        7. Streamlit —   Live web app with single + batch prediction

📈 Results
        Model             -       AUC 

Logistic Regression       -      0.8231 
Random Forest             -      0.8387+
Gradient Boosting         -      0.8352 
XGBoost (tuned)           -      0.8243

## 💡 Top Churn Drivers
- Month-to-Month Contract
- Short Tenure (< 12 months)
- Electronic Check Payment
- No Online Security or Tech Support
- DSL Internet

#📊 Power BI Dashboard
Built an interactive dashboard using `churn_final_dataset.csv`

Visuals included:
- KPI Cards — Total Customers, Churned, Churn Rate %, Avg Monthly Charges
- Donut Chart — Churn Distribution (Yes/No)
- Bar Chart — Churn Rate by Contract Type
- Bar Chart — Churn Rate by Payment Method
- Line Chart — Churn Rate by Tenure Band
- Bar Chart — Support Calls vs Churn Rate
- Slicers — Contract, Internet Service, Senior Citizen

Dataset columns :  26 columns including engineered features
(TenureBand, ChurnRisk, AvgMonthlySpend, RiskScore, IsNewCustomer etc.)

KAVIN VENKAT V R
[LinkedIn](www.linkedin.com/in/kavin-venkat-1710s0202) ·




