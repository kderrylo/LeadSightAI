import streamlit as st
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from config import RAG_TEMPLATE, MODEL_NAME
from modules.scraping import load_page, split_text

@st.cache_resource
def init_models():
    embeddings = OllamaEmbeddings(model=MODEL_NAME)
    vector_store = InMemoryVectorStore(embeddings)
    model = OllamaLLM(model=MODEL_NAME)

    return embeddings,vector_store, model

embeddings, vector_store, model = init_models()

def index_docs(documents):
    st.session_state.vector_store=vector_store

    st.session_state.vector_store.add_documents(documents)
    st.session_state.documents_loaded = True

def retrieve_docs(query):
    if st.session_state.vector_store:
        return st.session_state.vector_store.similarity_search(query)
    return []

def answer_question(question, context):
    prompt = ChatPromptTemplate.from_template(RAG_TEMPLATE)
    chain = prompt | model

    return chain.invoke({"question": question, "context": context})

def initialize_company_rag(company_name, website):
    st.session_state.current_company = company_name
    st.session_state.chat_history = []
    
    
    with st.spinner(f"Loading information about {company_name}..."):
        documents = load_page(website)
        if documents:
            chunked_documents = split_text(documents)
            index_docs(chunked_documents)
            
            initial_question = f"Explain about {company_name}!"
            retrieve_documents = retrieve_docs(initial_question)
            context = "\n\n".join([doc.page_content for doc in retrieve_documents])
            
            if context:
                answer = answer_question(initial_question, context)
                st.session_state.chat_history.append({
                    "question": initial_question,
                    "answer": answer
                })
        else:
            st.error(f"Failed to load information from {website}")