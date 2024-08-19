import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance

def page_predict_attrition_body():
    version = 'v1'
    # Load the necessary files
    attrition_pipe = load_pkl_file(
        f'outputs/ml_pipeline/predict_attrition/{version}/clf_pipeline.pkl')
    attrition_feat_importance = plt.imread(
        f'outputs/ml_pipeline/predict_attrition/{version}/features_importance.png')
    X_train = pd.read_csv(
        f'outputs/ml_pipeline/predict_attrition/{version}/X_train.csv')
    X_test = pd.read_csv(
        f'outputs/ml_pipeline/predict_attrition/{version}/X_test.csv')
    y_train = pd.read_csv(
        f'outputs/ml_pipeline/predict_attrition/{version}/y_train.csv')
    y_test = pd.read_csv(
        f'outputs/ml_pipeline/predict_attrition/{version}/y_test.csv')

    st.write("### ML Pipeline: Predict Employee Attrition")
    
    # Display pipeline training summary conclusions
    st.info(
        f"* The pipeline was optimized to achieve a high recall score for predicting employee attrition.\n"
        f"* The performance on the training set was 0.85, while on the test set it achieved 0.80."
    )
    
    # Show pipeline steps
    st.write("---")
    st.write("* ML pipeline steps for predicting employee attrition.")
    st.write(attrition_pipe)

    # Show feature importance
    st.write("---")
    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(attrition_feat_importance)

    # Evaluate performance on the training and test sets
    st.write("---")
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=attrition_pipe,
                    label_map=["No Attrition", "Attrition"])
