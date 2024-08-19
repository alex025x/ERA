import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_employee_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_predict_tenure_body():

    # load tenure pipeline files
    version = 'v1'
    tenure_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    tenure_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    tenure_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_tenure/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Employee Tenure")
    # display pipeline training summary conclusions
    st.info(
        f"* Initially, the goal was to build a regression model to predict the tenure of an employee "
        f"at risk of leaving, but the regressor's performance did not meet the project requirement of "
        f"0.7 R2 Score on train and test sets. \n"
        f"* Therefore, the target was converted into classes, and the problem was transformed into a classification task. \n"
        f"* The pipeline was tuned to achieve at least 0.8 Recall on the '<4 months' tenure class, "
        f"as it is crucial to detect employees who may leave soon. The classifier achieved 0.8 on both train and test sets.\n"
        f"* Notably, the '<4.0 months' and '>20.0 months' classes performed reasonably well, whereas the '4.0 to 20.0 months' class showed poor performance. This limitation should be considered when interpreting the model's results."
    )
    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to predict tenure for employees at risk of leaving.")
    st.write(tenure_pipe)
    st.write("---")

    # show best features
    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(tenure_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=tenure_pipe,
                    label_map=tenure_labels_map)
