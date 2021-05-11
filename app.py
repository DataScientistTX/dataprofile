import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def load_data(file):
    df = pd.read_csv(file)
    return df

st.sidebar.title("Upload data")    
uploaded_file = st.sidebar.file_uploader("Choose a file")

option = st.selectbox(
    'Choose pandas profiling mode:',
    ('Minimal', 'Explorative', 'Default'))

st.write(option)

if uploaded_file is None:
    st.write("Please upload your data from the left panel")

if uploaded_file is not None:
    df = load_data(uploaded_file)   
    if option == "Default":
        pr = ProfileReport(df, title="Pandas Profiling Report")

    if option == "Minimal":
        pr = ProfileReport(df, title="Pandas Profiling Report", minimal=True)

    if option == "Explorative":
        pr = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

    st.title("Pandas Profiling in Streamlit")
    st_profile_report(pr)