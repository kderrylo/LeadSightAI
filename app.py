import streamlit as st
from modules.data_handling import get_company_data, filter_data
from modules.ui_components import render_sidebar,render_company_search, render_chat_rag
from modules.chat_rag import initialize_company_rag

if 'chat_history' not in st.session_state:
    st.session_state.chat_history= []
if 'current_company' not in st.session_state:
    st.session_state.current_company = None
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'documents_loaded' not in st.session_state:
    st.session_state.documents_loaded = False

with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

page = render_sidebar()

if page == "🏢 Search":
    df=get_company_data()
    filtered_df=filter_data(df)
    render_company_search(filtered_df ,initialize_company_rag)
elif page == "💬 ChatRAG":
    render_chat_rag()