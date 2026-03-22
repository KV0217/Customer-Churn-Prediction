import streamlit as st
import pandas as pd
import requests

# --- Config ---
API_URL = "https://churn-prediction-api-cbqf.onrender.com"

st.set_page_config(page_title="Churn Predictor", page_icon="📉", layout="wide")
st.title("📉 Customer Churn Predictor")
st.markdown("Real-time churn prediction powered by Random Forest — AUC 0.84 on IBM Telco dataset.")

# --- Check API health ---
try:
    health = requests.get(f"{API_URL}/health", timeout=5).json()
    st.success("API is live and healthy")
except:
    st.error("API is unavailable. Please try again in 30 seconds (free tier waking up).")

tab1, tab2, tab3 = st.tabs(["👤 Single Customer", "📁 Batch Prediction", "💡 Retention Strategies"])

# ── TAB 1: Single Customer ─────────────────────────────────────────────────
with tab1:
    st.markdown("### Enter Customer Details")
    col1, col2 = st.columns(2)

    with col1:
        gender          = st.radio("Gender", ["Male", "Female"], horizontal=True)
        senior          = st.radio("Senior Citizen", ["No", "Yes"], horizontal=True)
        partner         = st.radio("Partner", ["Yes", "No"], horizontal=True)
        dependents      = st.radio("Dependents", ["Yes", "No"], horizontal=True)
        tenure          = st.slider("Tenure (months)", 1, 72, 12)
        monthly_charges = st.slider("Monthly Charges ($)", 18, 120, 65)
        total_charges   = st.number_input("Total Charges ($)", min_value=0.0, value=float(monthly_charges * tenure))

    with col2:
        phone           = st.radio("Phone Service", ["Yes", "No"], horizontal=True)
        multi_lines     = st.radio("Multiple Lines", ["Yes", "No"], horizontal=True)
        internet        = st.radio("Internet Service", ["Fiber optic", "DSL", "No"])
        security        = st.radio("Online Security", ["Yes", "No"], horizontal=True)
        backup          = st.radio("Online Backup", ["Yes", "No"], horizontal=True)
        device          = st.radio("Device Protection", ["Yes", "No"], horizontal=True)
        tech            = st.radio("Tech Support", ["Yes", "No"], horizontal=True)
        tv              = st.radio("Streaming TV", ["Yes", "No"], horizontal=True)
        movies          = st.radio("Streaming Movies", ["Yes", "No"], horizontal=True)
        contract        = st.radio("Contract", ["Month-to-month", "One year", "Two year"])
        paperless       = st.radio("Paperless Billing", ["Yes", "No"], horizontal=True)
        payment         = st.radio("Payment Method", [
            "Electronic check", "Mailed check", "Bank transfer", "Credit card"
        ])

    if st.button("🔍 Predict Churn", type="primary"):
        payload = {
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone,
            "MultipleLines": multi_lines,
            "InternetService": internet,
            "OnlineSecurity": security,
            "OnlineBackup": backup,
            "DeviceProtection": device,
            "TechSupport": tech,
            "StreamingTV": tv,
            "StreamingMovies": movies,
            "Contract": contract,
            "PaperlessBilling": paperless,
            "PaymentMethod": payment,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges
        }

        with st.spinner("Calling prediction API..."):
            try:
                response = requests.post(f"{API_URL}/predict", json=payload, timeout=30)
                result   = response.json()
            except Exception as e:
                st.error(f"API call failed: {e}")
                st.stop()

        st.markdown("---")
        st.markdown("### Prediction Results")

        prob       = result["churn_probability"]
        risk       = result["risk_level"]
        rec        = result["recommendation"]
        risk_score = result.get("risk_score", "-")
        summary    = result.get("summary", "")

        # Metric cards
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Churn Probability", f"{prob*100:.1f}%")
        c2.metric("Risk Level",
                  "🔴 High" if risk == "high" else "🟡 Medium" if risk == "medium" else "🟢 Low")
        c3.metric("Risk Score", f"{risk_score} / 5")
        c4.metric("Decision", "Will Churn" if prob > 0.4 else "Will Stay")

        # Recommendation banner
        if risk == "high":
            st.error(f"⚠️ {rec}")
        elif risk == "medium":
            st.warning(f"⚡ {rec}")
        else:
            st.success(f"✅ {rec}")

        # Improvement suggestions table
        suggestions = result.get("improvement_suggestions", [])
        if suggestions:
            st.markdown(f"### 🎯 Improvement Areas — {summary}")
            df_suggestions = pd.DataFrame(suggestions)

            # Color impact column
            def color_impact(val):
                if val == "High":
                    return "background-color: #ffcccc; color: #8b0000; font-weight: bold"
                elif val == "Medium":
                    return "background-color: #fff3cc; color: #7d5a00; font-weight: bold"
                else:
                    return "background-color: #ccffcc; color: #1a5c1a; font-weight: bold"

            styled = df_suggestions.style.applymap(color_impact, subset=["impact"])
            st.dataframe(styled, use_container_width=True, hide_index=True)

            # Action items as checklist
            st.markdown("### ✅ Recommended Actions")
            for i, row in df_suggestions.iterrows():
                if row["impact"] == "High":
                    st.error(f"🔴 **{row['area']}** — {row['action']} *(Est. churn reduction: {row['estimated_churn_reduction']})*")
                elif row["impact"] == "Medium":
                    st.warning(f"🟡 **{row['area']}** — {row['action']} *(Est. churn reduction: {row['estimated_churn_reduction']})*")
                else:
                    st.info(f"🟢 **{row['area']}** — {row['action']} *(Est. churn reduction: {row['estimated_churn_reduction']})*")

# ── TAB 2: Batch Prediction ────────────────────────────────────────────────
with tab2:
    st.markdown("### Batch Churn Prediction via API")
    st.markdown("Upload a CSV with customer details — results include churn probability + recommendations for each.")

    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        batch_df = pd.read_csv(uploaded)
        st.write(f"Loaded {len(batch_df)} customers")
        st.dataframe(batch_df.head())

        required_cols = ["gender","SeniorCitizen","Partner","Dependents","tenure",
                         "PhoneService","MultipleLines","InternetService","OnlineSecurity",
                         "OnlineBackup","DeviceProtection","TechSupport","StreamingTV",
                         "StreamingMovies","Contract","PaperlessBilling","PaymentMethod",
                         "MonthlyCharges","TotalCharges"]

        missing = [c for c in required_cols if c not in batch_df.columns]
        if missing:
            st.error(f"Missing columns: {missing}")
        else:
            if st.button("Run Batch Prediction"):
                payload = batch_df[required_cols].to_dict(orient="records")
                with st.spinner(f"Predicting for {len(payload)} customers..."):
                    try:
                        response = requests.post(f"{API_URL}/predict/batch", json=payload, timeout=60)
                        results  = response.json()["predictions"]
                        out_df   = batch_df.copy()
                        out_df["churn_probability"] = [r["churn_probability"] for r in results]
                        out_df["risk_level"]        = [r["risk_level"] for r in results]
                        out_df["recommendation"]    = [r["recommendation"] for r in results]
                        out_df["risk_score"]        = [r["risk_score"] for r in results]
                        st.success(f"Done! Predicted for {len(results)} customers.")
                        st.dataframe(out_df, use_container_width=True)
                        csv = out_df.to_csv(index=False)
                        st.download_button("Download Results CSV", csv,
                                           "churn_predictions.csv", "text/csv")
                    except Exception as e:
                        st.error(f"Batch prediction failed: {e}")

# ── TAB 3: Retention Strategies ───────────────────────────────────────────
with tab3:
    st.markdown("### 📊 Business Insights & Churn Reduction Strategies")

    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
        #### 1. Contract Length
        - Month-to-month contracts have the highest churn rate
        - **Action:** Offer 10% discount for annual contract upgrade

        #### 2. Payment Methods
        - Manual payments correlate with higher churn
        - **Action:** Offer $5/month credit for auto-pay setup

        #### 3. New Customers (tenure < 6 months)
        - Churn is highest in the first 6 months
        - **Action:** 30-60-90 day onboarding programme
        """)
    with colB:
        st.markdown("""
        #### 4. Value-Added Services
        - No security/tech support = higher churn
        - **Action:** Bundle security + tech support at discount

        #### 5. High Spenders
        - High charges without perceived value = churn risk
        - **Action:** Proactively offer loyalty credits

        #### 6. Fiber Optic Users
        - Highest churn among internet service types
        - **Action:** Prioritise quality checks for fiber customers
        """)

    st.markdown("---")
    st.markdown("### 📈 Impact Summary")
    impact_data = {
        "Strategy": ["Contract upgrade", "Auto-pay setup", "Security bundle",
                     "Onboarding programme", "Loyalty credits"],
        "Estimated Churn Reduction": ["25-35%", "10-15%", "8-12%", "15-20%", "5-10%"],
        "Cost to Implement": ["Low", "Low", "Medium", "Medium", "Low"],
        "Priority": ["High", "High", "Medium", "High", "Medium"]
    }
    st.dataframe(pd.DataFrame(impact_data), use_container_width=True, hide_index=True)
