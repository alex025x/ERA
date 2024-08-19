import streamlit as st

def page_project_conclusions_body():
    st.write("### Project Conclusions")

    st.info(
        f"* The analysis identified key factors that contribute to employee attrition, such as job satisfaction, income, and tenure.\n"
        f"* The predictive model developed was effective in identifying employees at risk of leaving, with a good balance between precision and recall.\n"
        f"* These insights can help the HR department to implement strategies to improve employee retention, such as offering better incentives or addressing job satisfaction concerns."
    )

    st.write("---")

    st.write(
        f"Moving forward, the model can be further refined with additional data, and strategies can be implemented to retain high-risk employees."
    )
