import streamlit as st
import numpy as np
import joblib
import os

# ---------- App UI ----------
st.title("Salary Prediction App")
st.divider()

st.write(
    "This is a simple salary prediction app built using Streamlit. "
    "Enter your years of experience to predict the salary."
)

# ---------- Input ----------
experience_years = st.number_input(
    "Enter the experience in years",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

# ---------- Load Model (CORRECT WAY) ----------
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model.pkl")

model = joblib.load(MODEL_PATH)


# ---------- Prediction ----------
if st.button("Predict Salary"):
    X = np.array([[experience_years]])
    salary = model.predict(X)

    st.success(f"The predicted salary is: {salary[0]:,.2f}")
