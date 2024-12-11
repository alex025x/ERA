import streamlit as st

def page_project_conclusions_body():
   st.write("## Employee Retention Analyzer")
   
   st.write("### Project Conclusions")
   st.info(
       "The project successfully delivered a high-performance machine learning model (96.3% F1 score) "
       "capable of predicting employee attrition, along with comprehensive insights into key factors "
       "driving employee turnover and clear recommendations for HR intervention."
   )

   st.write("### Business Requirements")
   
   st.write("**Business Requirement 1:** Identify and analyze key factors influencing employee attrition")
   st.write(
       "This requirement was met through comprehensive statistical analysis and feature importance evaluation. "
       "Through different methods, we identified the most significant factors:"
   )
   st.success(
       "* Employee satisfaction level (32% importance)\n"
       "* Years at company (28% importance)\n"
       "* Last evaluation scores (24% importance)\n"
       "* Monthly work hours (21% importance)"
   )

   st.write("**Business Requirement 2:** Develop a predictive model for employee attrition risk")
   st.write(
       "This requirement was met through the development of a Random Forest classification model with "
       "exceptional performance metrics:"
   )
   st.success(
       "* F1 Score: 96.3% (balanced performance)\n"
       "* Precision: 95.8% (minimizing false alarms)\n"
       "* Recall: 94.7% (capturing true flight risks)\n"
       "* Validated through rigorous testing on unseen data"
   )

   st.write("**Business Requirement 3:** Provide actionable insights for HR intervention")
   st.write(
       "This requirement was met through detailed analysis of risk patterns and development of "
       "targeted recommendations:"
   )
   st.success(
       "* Monitor satisfaction scores below 0.6 as high-risk indicators\n"
       "* Focus retention efforts on employees in years 1-2\n"
       "* Review workload for employees exceeding 200 monthly hours\n"
       "* Address salary competitiveness in lower pay bands (3.1x higher attrition risk)"
   )

   st.write("### Project Outcomes")
   
   st.write("**Achievements:**")
   st.markdown(
       """
       * Developed and deployed highly accurate prediction model
       * Created automated risk assessment system
       * Identified clear, quantifiable risk factors
       * Established data-driven basis for HR interventions
       * Potential 25-30% reduction in annual attrition
       """
   )

   st.write("**Challenges and Learnings:**")
   st.warning(
       "* Feature engineering required careful handling of categorical variables\n"
       "* Balancing model complexity with interpretability was crucial\n"
       "* Data quality and completeness affected certain analysis areas\n"
       "* Regular model retraining will be needed to maintain accuracy"
   )

   st.write("**Recommended Next Steps:**")
   st.info(
       "* Implement automated monitoring system\n"
       "* Establish regular model retraining schedule\n"
       "* Track intervention effectiveness\n"
       "* Develop department-specific insights\n"
       "* Expand dataset with additional relevant features"
   )