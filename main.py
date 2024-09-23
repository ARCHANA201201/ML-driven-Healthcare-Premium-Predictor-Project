# codebasics ML course: codebasics.io, all rights reserved

import streamlit as st
from prediction_helper import predict

# Inject custom CSS for styling
st.markdown("""
    <style>
    /* General styles */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f6;
    }

    /* Customize the title */
    .stTitle {
        font-size: 2.5em;
        color: #0066cc;
        text-align: center;
        font-weight: bold;
        padding-bottom: 0.5em;
    }

    /* Style input elements */
    input {
        background-color: #f9f9f9;
        border-radius: 5px;
        padding: 0.5em;
        border: 1px solid #cccccc;
    }

    /* Style selectbox */
    select {
        background-color: #f9f9f9;
        border-radius: 5px;
        padding: 0.5em;
        border: 1px solid #cccccc;
    }

    /* Button styles */
    .stButton>button {
        background-color: #008cba;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 1.2em;
        border: none;
    }

    .stButton>button:hover {
        background-color: #006f9a;
        cursor: pointer;
    }

    /* Success message styles */
    .stAlert {
        background-color: #e6fffa;
        color: #00695c;
        font-size: 1.2em;
    }

    /* Style the layout of the columns */
    .css-1aumxhk {
        padding-left: 5%;
        padding-right: 5%;
    }

    /* Box shadow around form fields */
    .stNumberInput, .stSelectbox {
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }

    </style>
""", unsafe_allow_html=True)

# Define the page layout
# Display the title with an icon (assuming 'icon.png' is in the same directory as your Streamlit script)
st.markdown("""
    <style>
    /* Customize the title with larger font and red color */
    .title {
        font-size: 3em;  /* Increased font size for the title */
        color: red;
        text-align: center;
        font-weight: bold;
        padding-bottom: 0.5em;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Add some margin and adjust icon size */
    .title img {
        width: 80px;  /* Increased the size of the icon */
        margin-right: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the title with an icon (Ensure the image is in the same directory or provide the correct path)
st.markdown("""
    <div class="title">
        Healthcare Premium Predictor
    </div>
""", unsafe_allow_html=True)
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')
