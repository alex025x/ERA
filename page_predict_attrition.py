import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance

def page_predict_attrition_body():

    version = 'v2'  # Updated to match the correct version
    base_path = f'outputs/ml_pipeline/classification_model/{version}/'

    # Load the necessary files
    attrition_pipe_dc_fe = load_pkl_file(
        f'{base_path}/data_cleaning_and_feat_engineering_pipeline.pkl')
    attrition_pipe_model = load_pkl_file(
        f"{base_path}/classification_pipeline.pkl")
    attrition_feat_importance = plt.imread(
        f"{base_path}/features_importance.png")
    X_train = pd.read_csv(
        f"{base_path}/X_train.csv")
    X_test = pd.read_csv(
        f"{base_path}/X_test.csv")
    y_train = pd.read_csv(
        f"{base_path}/y_train.csv").values
    y_test = pd.read_csv(
        f"{base_path}/y_test.csv").values

    st.write("### ML Pipeline: Predict Employee Attrition")
    
    # Introduction to the section
    st.write(
        f"In this section, we delve into the machine learning pipeline developed to predict employee attrition. "
        f"The objective of this model is to identify employees at risk of leaving the company, allowing the HR department to take proactive measures."
    )

    # Display pipeline training summary conclusions
    st.info(
        f"* The pipeline was carefully tuned to achieve a high recall for the 'Yes Attrition' class, "
        f"as the primary goal is to maximize the detection of employees who are likely to leave. \n"
        f"* The performance metrics show that the model achieved a recall of 0.90 on the training set and 0.85 on the test set, indicating a good balance between generalization and overfitting."
    )

    # Show pipelines
    st.write("---")
    st.write("#### ML Pipeline Structure")

    st.write(
        f"The machine learning process for predicting attrition is broken down into two key pipelines:\n"
        f"1. **Data Cleaning and Feature Engineering Pipeline:** This pipeline is responsible for preprocessing the raw data, handling missing values, encoding categorical variables, and generating any additional features that improve model performance.\n"
        f"2. **Feature Scaling and Modeling Pipeline:** This pipeline scales the features and applies the trained classification model to predict employee attrition."
    )

    st.write("##### Data Cleaning and Feature Engineering Pipeline")
    st.write(attrition_pipe_dc_fe)

    st.write("##### Feature Scaling and Modeling Pipeline")
    st.write(attrition_pipe_model)

    # Show feature importance plot
    st.write("---")
    st.write("#### Feature Importance")

    st.write(
        f"The following chart displays the importance of each feature as determined by the model. "
        f"These insights can help the HR team to focus on the most influential factors when developing retention strategies."
    )
    st.write(X_train.columns.to_list())
    st.image(attrition_feat_importance)

    # Evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance Evaluation")

    st.write(
        f"The following section evaluates the performance of the model on both the training and test datasets. "
        f"This evaluation helps to ensure that the model generalizes well to unseen data and maintains its predictive power across different employee scenarios."
    )
    
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=attrition_pipe_model,
                    label_map=["No Attrition", "Yes Attrition"])

    st.write(
        f"The results above indicate the model's ability to correctly identify employees who are likely to leave (Yes Attrition) and those who are likely to stay (No Attrition). "
        f"These metrics are critical in assessing the reliability and effectiveness of the attrition prediction model."
    )

