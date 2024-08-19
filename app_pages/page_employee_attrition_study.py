import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_employee_data  # Updated function to load employee data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def page_employee_attrition_study_body():
    # Load data
    df = load_employee_data()

    # Selected variables for analysis
    vars_to_study = ['JobRole', 'MonthlyIncome', 'TotalWorkingYears', 'Attrition']

    st.write("### Employee Attrition Study")
    st.info(
        f"* The client is interested in understanding the patterns in employee data "
        f"to identify the most relevant variables correlated with employee attrition."
    )

    # Inspect data
    if st.checkbox("Inspect Employee Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Below are the first 10 rows of the dataset."
        )
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted to better understand how "
        f"the variables are correlated with attrition levels. \n"
        f"The most correlated variables are: **{vars_to_study}**"
    )

    # Summary of findings from the attrition study
    st.info(
        f"The following key insights were identified: \n"
        f"* Employees with lower monthly income are more likely to leave. \n"
        f"* Employees with shorter tenures are more likely to leave. \n"
        f"* Certain job roles show higher attrition rates compared to others."
    )

    # Code to filter and visualize the selected variables
    df_eda = df.filter(vars_to_study)

    # Individual plots per variable
    if st.checkbox("Attrition Levels per Variable"):
        attrition_level_per_variable(df_eda)

    # Parallel plot to visualize multivariate relationships
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* The information in yellow highlights the profiles of employees who are more likely to leave."
        )
        parallel_plot_attrition(df_eda)


# Function to plot attrition levels per variable
def attrition_level_per_variable(df_eda):
    target_var = 'Attrition'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


# Function to plot categorical variables
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


# Function to plot numerical variables
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


# Function to create a parallel plot
def parallel_plot_attrition(df_eda):
    # Discretize tenure for better visualization
    tenure_map = [-np.Inf, 5, 10, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'TotalWorkingYears': tenure_map})
    df_parallel = disc.fit_transform(df_eda)

    # Define labels for discretized bins
    n_classes = len(tenure_map) - 1
    classes_ranges = disc.binner_dict_['TotalWorkingYears'][1:-1]
    LabelsMap = {}
    for n in range(0, n_classes):
        if n == 0:
            LabelsMap[n] = f"≤{classes_ranges[0]} years"
        elif n == n_classes - 1:
            LabelsMap[n] = f">{classes_ranges[-1]} years"
        else:
            LabelsMap[n] = f"{classes_ranges[n-1]}-{classes_ranges[n]} years"

    df_parallel['TotalWorkingYears'] = df_parallel['TotalWorkingYears'].replace(LabelsMap)
    fig = px.parallel_categories(
        df_parallel, color="Attrition", width=750, height=500)
    st.plotly_chart(fig)
