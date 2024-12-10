import streamlit as st
import pandas as pd
import numpy as np
import joblib

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

def calculate_risk_score(data):
    """
    Calculate risk score based on employee parameters
    """
    score = 0
    
    # Major negative factors
    if data['satisfaction_level'].iloc[0] < 0.5: score += 30
    if data['average_montly_hours'].iloc[0] > 250: score += 20
    if data['number_project'].iloc[0] > 5: score += 20
    
    # Additional negative factors
    if data['salary'].iloc[0] == 'low': score += 10
    if data['Work_accident'].iloc[0] == 1: score += 10
    if data['promotion_last_5years'].iloc[0] == 0 and data['time_spend_company'].iloc[0] > 3: score += 10
    
    # Positive factors (reduce risk)
    if data['satisfaction_level'].iloc[0] > 0.7: score -= 20
    if data['promotion_last_5years'].iloc[0] == 1: score -= 15
    if data['salary'].iloc[0] == 'high': score -= 15
    if data['average_montly_hours'].iloc[0] < 220: score -= 10
    if data['Work_accident'].iloc[0] == 0: score -= 5
    
    return score

def calculate_adjusted_probabilities(risk_score, original_prob):
    """
    Calculate adjusted probabilities based on risk score and model probability
    """
    base_leave_prob = original_prob[1]
    
    # Adjust probability based on risk score
    if risk_score > 30:
        adj_factor = 1.2
    elif risk_score > 10:
        adj_factor = 1.0
    else:
        adj_factor = 0.8
        
    adjusted_leave_prob = min(max(base_leave_prob * adj_factor, 0.1), 0.9)
    return adjusted_leave_prob

def page_employee_retention_analyzer_body():
    """
    Display the employee retention analyzer page
    """
    st.write("### Employee Retention Analyzer")

    # Project Overview
    st.info(
        f"""
        ### Model Overview:
        This tool analyzes employee retention risk based on key performance indicators 
        and workplace satisfaction metrics. It provides insights into potential retention 
        issues and suggests targeted interventions.
        """
    )

    # Load trained model
    try:
        model = joblib.load('outputs/models/best_model_pipeline.pkl')
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return

    # Define features
    st.write("### Enter Employee Information")
    st.write("Please provide the following information to analyze retention risk:")

    col1, col2 = st.columns(2)

    with col1:
        # Satisfaction and Evaluation Metrics
        st.write("#### Satisfaction Metrics")
        satisfaction_level = st.slider('Satisfaction Level', 0.0, 1.0, 0.7, 0.01,
                                     help="Employee's last satisfaction survey score")
        last_evaluation = st.slider('Last Evaluation Score', 0.0, 1.0, 0.8, 0.01,
                                  help="Score from most recent performance evaluation")
        
        # Project and Time Metrics
        st.write("#### Workload Metrics")
        number_project = st.slider('Number of Projects', 2, 7, 4,
                                 help="Number of projects employee is involved in")
        average_montly_hours = st.slider('Average Monthly Hours', 96, 310, 180,
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
            risk_score = calculate_risk_score(input_data)
            departure_prob = calculate_adjusted_probabilities(risk_score, prediction_proba[0])
            retention_prob = 1 - departure_prob
            
            # Determine risk level based on score
            if risk_score > 30:
                st.error("### ⚠️ High Risk of Departure")
                st.write(f"Estimated probability of departure: {departure_prob:.1%}")
                st.write(f"Estimated probability of retention: {retention_prob:.1%}")
                
                st.write("#### Critical Risk Factors:")
                if satisfaction_level < 0.5:
                    st.write("* Critical: Very low satisfaction level")
                if average_montly_hours > 250:
                    st.write("* Critical: Excessive workload")
                if number_project > 5:
                    st.write("* Critical: Project overload")
                if salary == 'low' and time_spend_company > 2:
                    st.write("* Critical: Compensation concerns")
                if Work_accident == 1:
                    st.write("* Critical: Workplace safety incident")
                
                st.write("#### Immediate Actions Required:")
                st.write("""
                * Schedule urgent manager discussion
                * Review workload and project distribution
                * Assess compensation package
                * Create retention action plan
                """)
                
            elif risk_score > 10:
                st.warning("### ⚠️ Moderate Risk of Departure")
                st.write(f"Estimated probability of departure: {departure_prob:.1%}")
                st.write(f"Estimated probability of retention: {retention_prob:.1%}")
                
                st.write("#### Areas of Concern:")
                if satisfaction_level < 0.7:
                    st.write("* Below optimal satisfaction level")
                if average_montly_hours > 220:
                    st.write("* Higher than ideal workload")
                if number_project > 4:
                    st.write("* Elevated project load")
                if salary == 'low':
                    st.write("* Compensation review recommended")
                
                st.write("#### Recommended Actions:")
                st.write("""
                * Schedule manager check-in
                * Review workload balance
                * Discuss career development
                * Consider compensation adjustment
                """)
                
            else:
                st.success("### ✅ Low Risk of Departure")
                st.write(f"Estimated probability of retention: {retention_prob:.1%}")
                st.write(f"Estimated probability of departure: {departure_prob:.1%}")
                
                st.write("#### Positive Factors:")
                if satisfaction_level >= 0.7:
                    st.write("* High satisfaction level")
                if Work_accident == 0:
                    st.write("* Good safety record")
                if promotion_last_5years == 1:
                    st.write("* Recent career advancement")
                if average_montly_hours < 220:
                    st.write("* Good work-life balance")
                if salary in ['medium', 'high']:
                    st.write("* Competitive compensation")
                
                st.write("#### Retention Strategies:")
                st.write("""
                * Maintain regular feedback
                * Continue development support
                * Monitor engagement
                * Plan future opportunities
                """)

if __name__ == "__main__":
    page_employee_retention_analyzer_body()