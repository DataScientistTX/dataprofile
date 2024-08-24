import streamlit as st
from utils import load_data, generate_profile_report
from config import LAYOUT, TITLE, FILE_UPLOADER_TEXT, PROFILE_OPTIONS

st.set_page_config(layout=LAYOUT)

def main():
    st.sidebar.title(TITLE)
    uploaded_file = st.sidebar.file_uploader(FILE_UPLOADER_TEXT)

    option = st.selectbox('Choose pandas profiling mode:', PROFILE_OPTIONS)

    if uploaded_file is None:
        st.write("Please upload your data from the left panel")
        return

    df = load_data(uploaded_file)
    pr = generate_profile_report(df, option)

    st.title("Pandas Profiling in Streamlit")
    st_profile_report(pr)

if __name__ == "__main__":
    main()