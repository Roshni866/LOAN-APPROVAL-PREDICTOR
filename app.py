import streamlit as st
import numpy as np
import joblib
model=joblib.load("loan_approval_model.pkl")

st.set_page_config(page_title="LOAN APPROVAL PREDICTOR")
st.title("Loan Approval Predictor")
st.write("Enter Applicants details below")


no_of_dependents = st.number_input("Number of Dependents", min_value=0, step=1)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

income_annum = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (months)", min_value=0)
cibil_score = st.number_input("CIBIL Score", min_value=0)

residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0)


education_num = 1 if education == "Graduate" else 0
self_employed_num = 1 if self_employed == "Yes" else 0

input_data = np.array([[no_of_dependents, education_num, self_employed_num, income_annum,
                        loan_amount, loan_term, cibil_score, residential_assets_value,
                        commercial_assets_value, luxury_assets_value, bank_asset_value]])
if st.button("Predict Approval"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")