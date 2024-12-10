import streamlit as st
import pandas as pd
import numpy as np
import joblib
from src.data_management import load_pkl_file

def run_prediction(model, input_data: pd.DataFrame):
    """
    Make prediction using the trained model pipeline
    """
    try:
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        return prediction, prediction_proba
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None, None

def page_employee_retention_analyzer_body():
    """
    Display the employee retention analyzer page
    """
    st.write("### Employee Retention Analyzer")

    # Project Overview
    st.info(
        f"""
        ### Model Performance Metrics:
        * Best Model: Random Forest with Pipeline (Scaling + Model)
        * Validation F1 Score: 0.963
        * Handles both numerical and categorical features
        * Trained on balanced dataset using SMOTE
        
        The model predicts whether an employee is likely to leave based on key features 
        identified through our analysis.
        """
    )

    # Load trained model
    try:
        model = joblib.load('/workspace/ERA/outputs/models/best_model_pipeline.pkl')
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return

    # Define features (based on your engineered dataset)
    st.write("### Enter Employee Information")
    st.write("Please provide the following information to analyze retention risk:")

    col1, col2 = st.columns(2)

    with col1:
        # Satisfaction and Evaluation Metrics
        st.write("#### Satisfaction Metrics")
        satisfaction_level = st.slider('Satisfaction Level', 0.0, 1.0, 0.5, 0.01,
                                     help="Employee's last satisfaction survey score")
        last_evaluation = st.slider('Last Evaluation Score', 0.0, 1.0, 0.7, 0.01,
                                  help="Score from most recent performance evaluation")
        
        # Project and Time Metrics
        st.write("#### Workload Metrics")
        number_project = st.slider('Number of Projects', 2, 7, 4,
                                 help="Number of projects employee is involved in")
        average_montly_hours = st.slider('Average Monthly Hours', 96, 310, 200,
                                       help="Average working hours per month")

    with col2:
        # Career Metrics
        st.write("#### Career Metrics")
        time_spend_company = st.slider('Years in Company', 2, 10, 3,
                                     help="Total years employed at the company")
        Work_accident = st.selectbox('Had Work Accident', [0, 1],
                                   help="Whether employee had a workplace accident (0=No, 1=Yes)")
        promotion_last_5years = st.selectbox('Promoted in Last 5 Years', [0, 1],
                                           help="Whether employee was promoted in last 5 years (0=No, 1=Yes)")
        salary = st.selectbox('Salary Level', ['low', 'medium', 'high'],
                            help="Employee's salary category")

    # Create input dataframe
    input_data = pd.DataFrame({
        'satisfaction_level': [satisfaction_level],
        'last_evaluation': [last_evaluation],
        'number_project': [number_project],
        'average_montly_hours': [average_montly_hours],
        'time_spend_company': [time_spend_company],
        'Work_accident': [Work_accident],
        'promotion_last_5years': [promotion_last_5years],
        'salary': [salary]
    })

    # Make prediction when button is clicked
    if st.button('Analyze Retention Risk'):
        prediction, prediction_proba = run_prediction(model, input_data)
        
        if prediction is not None:
            # Display prediction
            if prediction[0] == 1:
                st.error("### ⚠️ High Risk of Departure")
                risk_probability = prediction_proba[0][1]
                st.write(f"Probability of leaving: {risk_probability:.2%}")
                
                st.write("#### Risk Factors:")
                if satisfaction_level < 0.5:
                    st.write("* Low satisfaction level")
                if average_montly_hours > 250:
                    st.write("* High workload")
                if time_spend_company > 5 and promotion_last_5years == 0:
                    st.write("* Lack of career progression")
                
                st.write("#### Recommended Actions:")
                st.write("""
                * Schedule immediate manager discussion
                * Review workload distribution
                * Consider development opportunities
                * Evaluate compensation package
                """)
            else:
                st.success("### ✅ Low Risk of Departure")
                retention_probability = prediction_proba[0][0]
                st.write(f"Probability of staying: {retention_probability:.2%}")
                
                st.write("#### Positive Indicators:")
                if satisfaction_level > 0.7:
                    st.write("* High satisfaction level")
                if Work_accident == 0:
                    st.write("* Good safety record")
                if promotion_last_5years == 1:
                    st.write("* Recent career advancement")
                
                st.write("#### Retention Strategies:")
                st.write("""
                * Maintain regular feedback sessions
                * Continue professional development
                * Monitor workload balance
                * Consider for future advancement opportunities
                """)

    # Add feature importance note
    st.info("""
    ### Key Factors in Order of Importance:
    1. Satisfaction Level
    2. Time in Company
    3. Number of Projects
    4. Last Evaluation
    5. Monthly Hours
    
    Based on Random Forest feature importance analysis
    """)