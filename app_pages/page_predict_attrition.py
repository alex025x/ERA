import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance

def page_predict_attrition_body():

    version = 'v1'
    # Load the necessary files
    attrition_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_attrition/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    attrition_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_attrition/{version}/clf_pipeline_model.pkl")
    attrition_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_attrition/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_attrition/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_attrition/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_attrition/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_attrition/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Employee Attrition")
    # Display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned to achieve a high recall on the 'Yes Attrition' class, "
        f"as the goal is to identify employees at risk of leaving. \n"
        f"* The pipeline's performance on the training and test sets is 0.90 and 0.85, respectively."
    )

    # Show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(attrition_pipe_dc_fe)

    st.write("* The second is for feature scaling and modeling.")
    st.write(attrition_pipe_model)

    # Show feature importance plot
    st.write("---")
    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(attrition_feat_importance)

    # Evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=attrition_pipe_model,
                    label_map=["No Attrition", "Yes Attrition"])

