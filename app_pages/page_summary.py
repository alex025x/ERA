import streamlit as st

def page_summary_body():
    st.write("## Project Overview")
    
    st.info(
        "This project aims to analyze employee retention data and identify the key factors that contribute to employee attrition. The goal is to help the HR team develop strategies to improve employee retention and reduce turnover."
    )

    st.write(
        "The dataset used in this analysis includes various attributes related to employee demographics, job satisfaction, performance, and other relevant factors. It contains information about current and former employees, which will allow us to gain insights into the differences between those who stayed and those who left the organization."
    )
    
    st.success(
        "The main objectives of this project are:\n"
        "1. Understand the key drivers of employee attrition.\n"
        "2. Build predictive models to identify employees at risk of leaving the organization.\n"
        "3. Provide actionable insights to the HR team for improving employee retention."
    )

    st.write("### Potential Insights")
    st.write(
        "By analyzing the employee data, we hope to uncover insights that can help the HR team make more informed decisions about employee management and retention strategies. Some of the potential insights we aim to explore include:")

    st.markdown(
        """
        - Identifying the most influential factors contributing to employee attrition (e.g., job satisfaction, work-life balance, compensation, career development opportunities)
        - Understanding how employee demographics (age, tenure, department, etc.) impact retention rates
        - Detecting patterns or trends in employee turnover, such as seasonal variations or department-specific challenges
        - Developing predictive models to proactively identify employees at high risk of leaving the organization
        - Recommending targeted interventions or programs to address the root causes of employee attrition
        """
    )

    st.write("### Expected Outcomes")
    st.write(
        "The insights and models developed through this project are expected to provide the HR team with valuable tools and information to enhance their employee retention strategies. By understanding the key factors influencing attrition, the organization can implement more effective policies, programs, and interventions to improve employee satisfaction, engagement, and loyalty, ultimately leading to a more stable and productive workforce."
    )