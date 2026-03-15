# 🏥 ML-Driven Healthcare Premium Predictor

A **Machine Learning powered Healthcare Insurance Premium Prediction System** built using **Python, Scikit-Learn, and Streamlit**.

The system predicts the **expected health insurance premium** based on personal, lifestyle, and medical risk factors.

It uses **different ML models for young individuals and older individuals** to improve prediction accuracy.

---

# 🚀 Live Streamlit App

Try the live application here:

👉 https://ml-driven-healthcare-premium-predictor-project.streamlit.app/

---

# 🧠 Project Overview

Insurance companies calculate premiums based on **risk factors** such as age, medical history, income, and lifestyle habits.

This project builds a **machine learning system that predicts insurance premiums automatically** using historical data and risk scoring.

The application provides a **user-friendly Streamlit interface** where users can enter their information and instantly receive a predicted premium.

---

# ✨ Features

✔ Predict healthcare insurance premium  
✔ Interactive **Streamlit dashboard UI**  
✔ Automatic **data preprocessing and feature engineering**  
✔ Risk score calculation from medical history  
✔ Separate ML models for **young vs older individuals**  
✔ Scalable deployment using **Streamlit Cloud**

---
User Input
│
▼
Streamlit Web Interface
│
▼
Feature Engineering
│
▼
Risk Score Calculation
│
▼
Data Preprocessing
│
▼
Feature Scaling
│
▼
ML Model Selection
(Age ≤ 25 → Young Model
Age > 25 → General Model)
│
▼
Premium Prediction

---

# 📊 Input Features

The model considers multiple **demographic, lifestyle, and medical factors**:

### Personal Information
- Age
- Gender
- Marital Status
- Region
- Employment Status

### Financial Information
- Income
- Insurance Plan

### Health Information
- BMI Category
- Smoking Status
- Genetic Risk
- Medical History
- Number of Dependants

---

# 🧮 Risk Score Calculation

Medical history is converted into a **normalized risk score**.

Example risk values:

| Disease | Risk Score |
|-------|------|
| Diabetes | 6 |
| Heart Disease | 8 |
| High Blood Pressure | 6 |
| Thyroid | 5 |
| No Disease | 0 |

The combined score is **normalized between 0 and 1** and used as an input feature.

---

# 🧠 Model Strategy

To improve prediction accuracy, the system uses **two separate models**:

| Age Group | Model Used |
|------|------|
| Age ≤ 25 | Young Population Model |
| Age > 25 | General Population Model |

This approach captures **different risk patterns across age groups**.

---

# 📈 Example Prediction

Input:
Age: 35
Income: 10 Lakhs
Smoking Status: Regular
Medical History: Diabetes
Insurance Plan: Gold

Output:
Predicted Health Insurance Cost: ₹ 12,540

---

# 📥 Installation

Clone the repository:
git clone https://github.com/yourusername/healthcare-premium-predictor.git

Install dependencies:
pip install -r requirements.txt

Run the Streamlit application:
streamlit run app.py

---

# 🌐 Deployment

The application is deployed using **Streamlit Cloud**.

Live App:

👉 https://ml-driven-healthcare-premium-predictor-project.streamlit.app/

---