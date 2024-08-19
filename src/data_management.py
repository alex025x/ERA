import streamlit as st
import pandas as pd
import joblib

@st.cache_data
def load_employee_data():
    """
    Function to load the employee attrition dataset.
    """
    df = pd.read_csv("inputs/datasets/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df

@st.cache_resource
def load_pkl_file(file_path):
    """
    Function to load a pickled file, such as a model or pipeline.
    """
    return joblib.load(filename=file_path)
