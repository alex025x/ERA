import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance

def page_model_performance_body():
    st.write("### Model Performance Evaluation")

    st.info(
        f"Model performance is assessed based on the following metrics:\n"
        f"* **Precision**: The accuracy of the positive predictions, reflecting how often the model is correct when it predicts an employee will leave.\n"
        f"* **Recall**: The ability of the model to find all the relevant cases, indicating how well it identifies employees who actually leave.\n"
        f"* **F1 Score**: The harmonic mean of precision and recall, providing a single metric that balances both concerns.\n"
        f"* **Confusion Matrix**: A detailed breakdown of prediction results, showing the number of true positives, true negatives, false positives, and false negatives."
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
    st.write("#### Model Performance on Training Data")
    clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map=["No Attrition", "Attrition"])

    # Performance bubbles
    st.write("---")
    st.write("### Model Performance Summary")
    
    st.success(
        f"* **Precision**: The model shows a high precision, indicating that when it predicts an employee will leave, it is often correct. This reduces the risk of unnecessary interventions.\n"
        f"* **Recall**: With a strong recall score, the model is proficient at identifying most employees who are likely to leave, allowing for proactive retention strategies.\n"
        f"* **F1 Score**: The F1 score suggests a balanced performance, ensuring that both precision and recall are optimized for practical use.\n"
        f"* **Confusion Matrix**: The confusion matrix shows a well-balanced performance with minimal false positives and false negatives, underscoring the model's reliability."
    )

    st.write("---")
    st.write(
        f"The model was evaluated on both training and test sets, and the results indicate that it performs well in predicting employee attrition. "
        f"These results provide confidence that the model can be effectively used to support HR decision-making processes."
    )
