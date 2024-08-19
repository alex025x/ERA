import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance

def page_model_performance_body():
    st.write("### Model Performance Evaluation")

    st.info(
        f"Model performance is assessed based on the following metrics:\n"
        f"* **Precision**: The accuracy of the positive predictions.\n"
        f"* **Recall**: The ability of the model to find all the relevant cases within a dataset.\n"
        f"* **F1 Score**: The balance between precision and recall.\n"
        f"* **Confusion Matrix**: To show the number of true positives, true negatives, false positives, and false negatives."
    )

    st.write("---")

    # Load the necessary files
    version = 'v2'  # Adjust version if needed
    base_path = f'outputs/ml_pipeline/classification_model/{version}/'

    X_train = pd.read_csv(f"{base_path}/X_train.csv")
    X_test = pd.read_csv(f"{base_path}/X_test.csv")
    y_train = pd.read_csv(f"{base_path}/y_train.csv").values
    y_test = pd.read_csv(f"{base_path}/y_test.csv").values
    pipeline = load_pkl_file(f"{base_path}/classification_pipeline.pkl")

    # Insert the performance evaluation code here
    clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map=["No Attrition", "Attrition"])

    st.write(
        f"The model was evaluated on both training and test sets, and the results indicate that it performs well in predicting employee attrition."
    )
