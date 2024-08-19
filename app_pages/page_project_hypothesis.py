import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypotheses and Validation")

    st.info(
        "This project focuses on understanding the key factors that contribute to employee attrition. "
        "We have formulated several hypotheses about the factors that might influence employee turnover. "
        "The aim is to validate these hypotheses with statistical analysis and predictive modeling to guide HR strategies."
    )

    st.write("---")
    
    # Hypothesis 1
    st.write("#### Hypothesis 1")
    st.write("**We suspect that job satisfaction is the most significant factor influencing employee attrition.**")

    st.write("**Findings:**")
    st.write(
        "* The analysis showed that job satisfaction indeed has a strong correlation with employee attrition.\n"
        "* Employees with low job satisfaction are significantly more likely to leave the company.\n"
        "* This hypothesis was confirmed by both the correlation analysis and the predictive modeling."
    )

    st.write("---")
    
    # Hypothesis 2
    st.write("#### Hypothesis 2")
    st.write("**We suspect that income level plays a major role in whether an employee decides to stay or leave.**")

    st.write("**Findings:**")
    st.write(
        "* Income was found to have a moderate correlation with employee attrition.\n"
        "* Employees with lower income levels showed a higher tendency to leave the company, but the correlation was not as strong as job satisfaction.\n"
        "* The hypothesis was partially confirmed. While income is a factor, it is not the sole or strongest predictor of attrition."
    )

    st.write("---")
    
    # Hypothesis 3
    st.write("#### Hypothesis 3")
    st.write("**We suspect that employees with shorter tenures are more likely to leave the company.**")

    st.write("**Findings:**")
    st.write(
        "* The analysis confirmed that employees with shorter tenures have a higher likelihood of leaving.\n"
        "* The predictive model indicated that tenure is a significant predictor of attrition, particularly for employees in their first few years.\n"
        "* This hypothesis was confirmed by both the statistical analysis and the predictive model."
    )

    st.write("---")

    st.write(
        "The next steps involve refining the model with more data and continually monitoring the results to ensure that the strategies implemented are effectively reducing attrition."
    )

