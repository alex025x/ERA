import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_management import load_employee_data

def page_feature_correlation_study_body():
    st.write("### Feature Correlation Study")
    
    # Load the data
    df = load_employee_data()

    st.write(
        f"Correlation analysis helps in identifying the relationships between different features in the dataset and how they relate to employee attrition."
    )
    
    st.write("---")

    # Display correlation heatmap
    st.write("#### Correlation Heatmap")
    corr_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)
    
    st.write(
        f"From the heatmap, we can observe the relationships between different features and identify which ones are strongly correlated with attrition."
    )
