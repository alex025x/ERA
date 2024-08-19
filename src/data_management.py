import streamlit as st
import pandas as pd
import joblib
import os

@st.cache_data
def load_employee_data():
    """
    Function to load the employee attrition dataset.
    """
    file_path = "inputs/datasets/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        st.error(f"File not found: {file_path}")
        return None

@st.cache_resource
def load_pkl_file(file_path):
    """
    Function to load a pickled file, such as a model or pipeline.
    """
    if os.path.exists(file_path):
        return joblib.load(filename=file_path)
    else:
        st.error(f"File not found: {file_path}")
        return None

@st.cache_data
def load_csv_file(file_path):
    """
    Function to load a CSV file.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        st.error(f"File not found: {file_path}")
        return None
