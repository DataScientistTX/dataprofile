import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout='wide')

@st.cache_data()
def load_data(file):
    df = pd.read_csv(file)
    return df

st.sidebar.title("Upload data")    
uploaded_file = st.sidebar.file_uploader("Choose a file")

option = st.selectbox(
    'Choose pandas profiling mode:',
    ('Minimal', 'Explorative', 'Default'))

if uploaded_file is None:
    st.write("Please upload your data from the left panel")

if uploaded_file is not None:
    df = load_data(uploaded_file)   
    if option == "Default":
        pr = ProfileReport(df, title="Pandas Profiling Report")

    if option == "Minimal":
        st.write("Selected option: Minimal. Please consider using Explorative if further exploration is required.")
        pr = ProfileReport(df, title="Pandas Profiling Report", minimal=True)

    if option == "Explorative":
        st.write("Selected option: Explorative. This mode might be computationally expensive. Please consider using Minimal if you are experiencing problems.")
        pr = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

    st.title("Pandas Profiling in Streamlit")
    st_profile_report(pr)
