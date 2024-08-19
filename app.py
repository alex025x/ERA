import streamlit as st
from app_pages.multipage import MultiPage  # Import the MultiPage class

# Import your page functions
from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_feature_correlation_study import page_feature_correlation_study_body
from app_pages.page_employee_retention_analyzer import page_employee_retention_analyzer_body
from app_pages.page_model_performance import page_model_performance_body
from app_pages.page_project_conclusions import page_project_conclusions_body

# Create an instance of the app
app = MultiPage(app_name="Employee Retention Analyzer")

# Add your app pages here
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Feature Correlation Study", page_feature_correlation_study_body)
app.add_page("Employee Retention Analyzer", page_employee_retention_analyzer_body)  # New page
app.add_page("Model Performance", page_model_performance_body)
app.add_page("Project Conclusions", page_project_conclusions_body)

# Run the app
app.run()
