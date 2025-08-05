from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from config import CHUNK_SIZE, CHUNK_OVERLAP

def load_page(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        loader = SeleniumURLLoader(urls=[url])
        documents = loader.load()
        return documents
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        return []

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)