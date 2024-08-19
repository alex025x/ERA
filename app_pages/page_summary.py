import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* An **employee** is a person who works for an organization.\n"
        f"* **Attrition** refers to employees leaving the organization.\n"
        f"* **Retention** is the ability of an organization to keep its employees over time.\n"
        f"* **Tenure** is the duration (in months or years) that an employee has worked for the organization.\n"
        f"* A **prospective churned employee** is an employee who is likely to leave the organization.\n"
        f"* **Job Satisfaction**, **Work-Life Balance**, and **Monthly Income** are some key factors "
        f"that might influence an employee's decision to stay or leave."
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/YourUsername/Employee-Retention-Analyzer).")

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in understanding the patterns in the employee base "
        f"to identify the most relevant variables that are correlated with employee attrition.\n"
        f"* 2 - The client wants to predict whether a given employee is likely to leave the organization. "
        f"If so, the client is interested to know when the employee might leave. Additionally, the client "
        f"wants to understand which cluster the employee belongs to within the organization, "
        f"and identify potential factors that could help retain the employee."
    )
