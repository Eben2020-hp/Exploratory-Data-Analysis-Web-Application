import streamlit as st
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web Application Title
st.title("Pandas EDA Application")
st.markdown('''
___
### This is the **EDA App** created in Streamlit using **Pandas-Profiling**.
**Credit:** App Built in 'Python' + 'Streamlit' by [Eben Emmanuel]
___
''')

# Sidebar to Upload Data
with st.sidebar.header('Upload Data Here (**only csv**)'):
    uploaded_file = st.sidebar.file_uploader("Drag and Drop Your Data here")
    st.sidebar.markdown("""
    
    [Download Data from Kaggle](https://www.kaggle.com/datasets)   
    """)

# Pandas Profile Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        df = pd.read_csv(uploaded_file, encoding= 'unicode_escape')
        return df
    data = load_csv()
    prof = ProfileReport(data, explorative= True)
    st.header('**Input DataFrame**')
    st.write(data)
    st.write('___')
    st.header('**Profile Report**')
    st_profile_report(prof)

else:
    st.info('Awaiting for File to be Loaded')
    if st.button('Press to use Sample Dataset'):
        url = (r'https://raw.githubusercontent.com/Eben2020-hp/Titanic-Machine-Learning/main/Titanic%20Data/train.csv')
        @st.cache
        def load_csv():
            df_sample = pd.read_csv(url)
            return df_sample
        data_sample = load_csv()
        prof = ProfileReport(data_sample, explorative= True)
        st.header('**Titanic DataFrame**')
        st.write(data_sample)
        st.write('___')
        st.header('**Profile Report**')
        st_profile_report(prof)

