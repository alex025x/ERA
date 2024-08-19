import streamlit as st
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

    # Insert the performance evaluation code here
    clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map=["No Attrition", "Attrition"])

    st.write(
        f"The model was evaluated on both training and test sets, and the results indicate that it performs well in predicting employee attrition."
    )
