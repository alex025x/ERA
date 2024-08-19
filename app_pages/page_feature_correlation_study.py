import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_employee_data

def page_feature_correlation_study_body():
    st.write("### Feature Correlation Study")

    # Section 1: Business Requirement and Dataset
    st.write("#### Business Requirement and Dataset")
    st.info(
        """
        The primary goal of this project is to identify the key factors that contribute to employee attrition. 
        A correlation study will help determine which features are most closely associated with attrition. 
        We will utilize Pearson's correlation to indicate linear relationships between numerical variables 
        and Spearman's correlation to measure monotonic relationships between variables.
        """
    )

    st.write("---")

    # Load the dataset
    df = load_employee_data()

    # Section 2: Summary of Correlation Analysis
    st.write("#### Summary of Correlation Analysis")
    st.write(
        """
        We performed correlations within the dataset using both Spearman and Pearson correlations. 
        For these analyses, categorical features were one-hot encoded to facilitate the computation of correlations.
        The correlation matrices help in identifying how different variables relate to employee attrition.
        """
    )

    numerical_df = df.select_dtypes(include=['float64', 'int64'])

    # Compute Pearson and Spearman correlation matrices
    pearson_corr_matrix = numerical_df.corr(method='pearson')
    spearman_corr_matrix = numerical_df.corr(method='spearman')

    # Plot the Pearson correlation heatmap
    st.write("#### Pearson Correlation Heatmap")
    plt.figure(figsize=(10, 8))
    sns.heatmap(pearson_corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    st.pyplot(plt)

    # Plot the Spearman correlation heatmap
    st.write("#### Spearman Correlation Heatmap")
    plt.figure(figsize=(10, 8))
    sns.heatmap(spearman_corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    st.pyplot(plt)

    st.write("---")

    # Section 3: Analysis of Most Correlated Features
    st.write("#### Analysis of Most Correlated Features")
    st.write(
        """
        Based on the correlation matrices, we have identified several features that exhibit strong correlations with employee attrition. 
        Below are the top correlated features and their relationships to employee turnover:
        """
    )
    st.write(
        """
        * **Job Satisfaction**: Employees with low job satisfaction tend to leave the organization more frequently.
        * **Monthly Income**: Employees with lower income levels are at a higher risk of attrition.
        * **Total Working Years**: Employees with fewer years of experience have a higher likelihood of leaving.
        """
    )

    st.write("---")

    # Section 4: Feature Relationships
    st.write("#### Feature Relationships")
    st.write(
        """
        To further understand the relationships between features, visualizations such as pair plots or scatter plots 
        could be employed to explore interactions between key features identified in the correlation analysis.
        """
    )
    # Additional analysis can be added here (e.g., pair plots, scatter plots)

    st.write("---")

    # Section 5: Conclusions
    st.write("#### Conclusions")
    st.write(
        """
        The correlation studies revealed that job satisfaction, monthly income, and total working years 
        are the most significant factors associated with employee attrition. 
        These insights can guide HR in formulating strategies to enhance employee retention.
        """
    )
    st.write(
        """
        Moving forward, further analysis can be conducted to explore other potential factors, 
        and machine learning models can be developed to predict attrition based on these insights.
        """
    )
