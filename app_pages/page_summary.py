import streamlit as st

def page_summary_body():
    st.write("### Quick Project Summary")
    
    st.info(
        f"* This project is focused on analyzing employee retention to identify patterns and predict which employees are likely to leave. "
        f"The goal is to help the HR team in identifying factors that contribute to employee attrition and to implement strategies to improve retention."
    )

    st.write(
        f"* The dataset used includes various attributes related to employee demographics, job satisfaction, income, and other factors."
    )
    
    st.success(
        f"The project has the following objectives:\n"
        f"* 1 - Understand the key factors that influence employee attrition.\n"
        f"* 2 - Build predictive models to identify employees at risk of leaving.\n"
        f"* 3 - Provide actionable insights for improving employee retention."
    )
