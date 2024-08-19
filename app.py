import streamlit as st
from app_pages.multipage import MultiPage

# Import the correct page module
from app_pages.page_summary import page_summary_body
from app_pages.page_employee_attrition_study import page_employee_attrition_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_attrition import page_predict_attrition_body
from app_pages.page_predict_tenure import page_predict_tenure_body
from app_pages.page_cluster_analysis import page_cluster_analysis_body

app = MultiPage(app_name="Employee Retention Analyzer")

# Add your app pages here
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Employee Attrition Study", page_employee_attrition_study_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict Attrition", page_predict_attrition_body)
app.add_page("ML: Predict Tenure", page_predict_tenure_body)
app.add_page("ML: Cluster Analysis", page_cluster_analysis_body)

app.run()
