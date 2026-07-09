import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("models/insurance_pipeline.pkl")

st.set_page_config(page_title="Medical Insurance Cost Prediction", page_icon="🏥")

st.title("🏥 Medical Insurance Cost Prediction")
st.write("Enter the details below to predict insurance charges.")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

sex = st.selectbox("Gender", ["male", "female"])

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.selectbox("Smoker", ["yes", "no"])

region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# -------------------------
# Feature Engineering
# -------------------------

family_size = children + 1

# BMI Category
if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

# Age Group
if age <= 30:
    age_group = "Young"
elif age <= 45:
    age_group = "Adult"
elif age <= 60:
    age_group = "Middle"
else:
    age_group = "Senior"

# Prediction
if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region],
        "bmi_category": [bmi_category],
        "age_group": [age_group],
        "family_size": [family_size]
    })

    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Insurance Cost: ₹ {prediction[0]:,.2f}")