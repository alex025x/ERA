import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file
from sklearn.pipeline import Pipeline

def run_prediction(pipeline: Pipeline, input_data: pd.DataFrame):
    return pipeline.predict(input_data)

def page_employee_retention_analyzer_body():

    st.write("### Employee Retention Analyzer")

    st.info(
        """
        The client is interested in predicting whether an employee is at risk of leaving the company. 
        A machine learning model was built using a binary classification model with the following success metrics:
        - At least 80% recall for attrition on train and test sets (no more than 20% missed positive predictions).
        - At least 75% precision for no attrition (reducing the number of false positives).
        """
    )

    # Load the necessary pipeline
    version = 'v2'  # Adjust version if needed
    base_path = f'outputs/ml_pipeline/classification_model/{version}/'
    pipeline = load_pkl_file(f"{base_path}/classification_pipeline.pkl")

    # Define the features in the exact order expected by the model
    feature_names = [
        'Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education',
        'EducationField', 'EnvironmentSatisfaction', 'Gender', 'JobInvolvement',
        'JobLevel', 'JobRole', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked',
        'OverTime', 'JobSatisfaction', 'PerformanceRating', 'RelationshipSatisfaction',
        'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
        'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
        'YearsSinceLastPromotion', 'YearsWithCurrManager', 'DailyRate',
        'EmployeeCount', 'EmployeeNumber', 'HourlyRate', 'MonthlyRate', 'StandardHours',
        'Over18', 'PercentSalaryHike'
    ]

    # Collect input data
    input_data = pd.DataFrame({
        'Age': [st.slider('Age', 18, 65, 30)],
        'BusinessTravel': [st.selectbox('Business Travel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])],
        'Department': [st.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])],
        'DistanceFromHome': [st.slider('Distance From Home (miles)', 1, 30, 10)],
        'Education': [st.slider('Education', 1, 5, 3)],
        'EducationField': [st.selectbox('Education Field', ['Life Sciences', 'Medical', 'Marketing', 
                                                            'Technical Degree', 'Human Resources', 'Other'])],
        'EnvironmentSatisfaction': [st.slider('Environment Satisfaction', 1, 4, 3)],
        'Gender': [st.selectbox('Gender', ['Male', 'Female'])],
        'JobInvolvement': [st.slider('Job Involvement', 1, 4, 3)],
        'JobLevel': [st.slider('Job Level', 1, 5, 2)],
        'JobRole': [st.selectbox('Job Role', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 
                                              'Manufacturing Director', 'Healthcare Representative', 
                                              'Manager', 'Sales Representative', 'Research Director', 
                                              'Human Resources'])],
        'MaritalStatus': [st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])],
        'MonthlyIncome': [st.slider('Monthly Income', 1000, 20000, 5000)],
        'NumCompaniesWorked': [st.slider('Number of Companies Worked', 0, 10, 1)],
        'OverTime': [st.selectbox('Over Time', ['Yes', 'No'])],
        'JobSatisfaction': [st.slider('Job Satisfaction', 1, 4, 3)],
        'PerformanceRating': [st.slider('Performance Rating', 1, 4, 3)],
        'RelationshipSatisfaction': [st.slider('Relationship Satisfaction', 1, 4, 3)],
        'StockOptionLevel': [st.slider('Stock Option Level', 0, 3, 1)],
        'TotalWorkingYears': [st.slider('Total Working Years', 0, 40, 10)],
        'TrainingTimesLastYear': [st.slider('Training Times Last Year', 0, 6, 3)],
        'WorkLifeBalance': [st.slider('Work Life Balance', 1, 4, 3)],
        'YearsAtCompany': [st.slider('Years at Company', 0, 40, 5)],
        'YearsInCurrentRole': [st.slider('Years in Current Role', 0, 18, 4)],
        'YearsSinceLastPromotion': [st.slider('Years Since Last Promotion', 0, 15, 2)],
        'YearsWithCurrManager': [st.slider('Years with Current Manager', 0, 17, 5)],
        'DailyRate': [st.slider('Daily Rate', 100, 1500, 800)],
        'EmployeeCount': [1],  # Constant value
        'EmployeeNumber': [12345],  # Example value
        'HourlyRate': [st.slider('Hourly Rate', 30, 100, 50)],
        'MonthlyRate': [st.slider('Monthly Rate', 2000, 30000, 15000)],
        'StandardHours': [80],  # Assuming standard across all employees
        'Over18': ['Yes'],  # Assuming all employees are over 18
        'PercentSalaryHike': [st.slider('Percent Salary Hike', 0, 25, 10)],
    })

    # Ensure input_data matches the order and content of feature_names
    input_data = input_data[feature_names]

    # Run prediction
    if st.button('Run Predictive Analysis'):
        prediction = run_prediction(pipeline, input_data)
        if prediction[0] == 1:
            st.error("The model predicts this employee is at risk of attrition.")
        else:
            st.success("The model predicts this employee is not at risk of attrition.")
