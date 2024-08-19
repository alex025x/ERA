import streamlit as st

def page_project_hypotheses_body():
    st.write("### Project Hypotheses")
    
    st.info(
        f"The project is guided by the following hypotheses:\n"
        f"* **Hypothesis 1**: Employees with lower job satisfaction are more likely to leave the company.\n"
        f"* **Hypothesis 2**: Employees with lower monthly income are more prone to attrition.\n"
        f"* **Hypothesis 3**: Employees with shorter tenure or fewer years at the company have a higher likelihood of leaving.\n"
        f"* **Hypothesis 4**: Certain job roles have higher attrition rates than others."
    )
    
    st.write(
        f"These hypotheses will be tested using the employee attrition data through correlation analysis and predictive modeling."
    )
