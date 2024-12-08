import streamlit as st

def page_project_hypothesis_body():
    st.write("## Project Hypotheses and Validation")

    st.info(
        "This project aims to identify the key factors that contribute to employee attrition. I have formulated several hypotheses about the potential drivers of employee turnover, which we validated through statistical analysis and predictive modeling."
    )

    st.write("---")

    # Hypothesis 1
    st.write("### Hypothesis 1: Satisfaction Level")
    st.write("**Hypothesis:** Employees with low satisfaction levels are more likely to leave the organization.")

    st.write("**Validation Approach:**")
    st.markdown(
        """
        1. Conducted a Spearman and Pearson correlation analysis between the 'satisfaction_level' feature and the 'left' target variable to assess the strength and direction of the relationship.
        2. Included 'satisfaction_level' as a key predictor in predictive models to evaluate its contribution to employee attrition.
        3. Analyzed feature importance scores to determine the impact of satisfaction level on the likelihood of employees leaving the organization.
        """
    )

    st.write("**Findings:**")
    st.write(
        "The analysis demonstrated a significant negative correlation between satisfaction level and attrition. Employees with lower satisfaction levels were found to have a higher likelihood of leaving the organization. Predictive models consistently identified 'satisfaction_level' as a critical predictor of employee attrition."
    )

    st.write("---")

    # Hypothesis 2
    st.write("### Hypothesis 2: Time Spent in the Company")
    st.write("**Hypothesis:** Employees with shorter durations in the company are more likely to leave.")

    st.write("**Validation Approach:**")
    st.markdown(
        """
        1. Analyzed the distribution of 'time_spend_company' for employees who stayed versus those who left.
        2. Performed statistical tests to detect significant differences in tenure between the two groups.
        3. Included 'time_spend_company' in predictive models to assess its importance in predicting employee attrition.
        """
    )

    st.write("**Findings:**")
    st.write(
        "Employees with shorter tenures showed a higher propensity to leave the organization. Both statistical tests and predictive models indicated that 'time_spend_company' is a key factor influencing attrition."
    )

    st.write("---")

    # Hypothesis 3
    st.write("### Hypothesis 3: Salary Level")
    st.write("**Hypothesis:** Employees with lower salaries are more likely to leave the organization.")

    st.write("**Validation Approach:**")
    st.markdown(
        """
        1. Analyzed the relationship between 'salary' levels (e.g., low, medium) and the 'left' variable using correlation coefficients.
        2. Visualized the associations between salary levels and attrition using heatmaps.
        3. Included salary features in the predictive models and evaluated their importance.
        """
    )

    st.write("**Findings:**")
    st.write(
        "A strong negative correlation was found between lower salary levels and employee retention. Employees in the 'low' salary category were more likely to leave, as confirmed by predictive models and feature importance analysis."
    )

    st.write("---")

    st.write(
        "The insights gained from validating these hypotheses provide valuable guidance for HR to design effective retention strategies. Further refinement of predictive models and ongoing analysis will ensure sustained improvements in employee retention."
    )
