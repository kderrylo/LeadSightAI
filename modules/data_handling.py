import pandas as pd, io
import streamlit as st

@st.cache_data
def get_company_data():
    try:
        return pd.read_csv('data/company_data.csv')
    except FileNotFoundError:
        st.error("Error: 'data/company_data.csv' not found. please ensure the file exists")

        return pd.DataFrame() 

def filter_data(df, search_term=None, industry=None, location=None):
    filtered_df = df.copy()
    

    if search_term:
        mask = filtered_df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        filtered_df = filtered_df[mask]
    
    if industry and industry!='All':
        filtered_df=filtered_df[filtered_df['Industry'] == industry]
    
    if location and location != 'All':
        filtered_df = filtered_df[filtered_df['Location'] == location]
    
    return filtered_df


def export_to_csv(dataframe):
    csv_buffer =io.StringIO()
    dataframe.to_csv(csv_buffer,index=False)

    return csv_buffer.getvalue()



def export_to_excel(dataframe):
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer,engine='openpyxl') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Companies')

    return excel_buffer.getvalue()