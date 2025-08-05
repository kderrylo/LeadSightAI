import streamlit as st
from datetime import datetime
from modules.data_handling import export_to_csv, export_to_excel

def render_sidebar():
    with st.sidebar:
        st.markdown("""
            <div class="logo-container">
                <span style="font-size: 2rem;">🦎</span>
                <span class="logo-text">LeadSightAI</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")

        page = st.selectbox(
            "🧭 Navigation",
            ["🏢 Search", "💬 ChatRAG"],
            index=0 if st.session_state.current_company is None else 1,
            key="sidebar_navigation"
        )
        
        st.markdown("**💡 Tips:**")
        st.markdown(" • Use filters to narrow down results ")
        st.markdown(" • Export data in CSV or Excel format ")
        st.markdown(" • Click 💬 to get AI-powered insights ")
        st.markdown(" • Chat naturally about company information ")
        st.markdown(" • Use specific questions for better answers ")
    return page

def render_company_search(df, initialize_company_rag):
    from modules.data_handling import filter_data

    st.markdown("""
        <div class="main-header">
             <h1>🦎 LeadSightAI Dashboard</h1>
            <p>AI-Powered Lead Generation & Business Intelligence</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("### 🔍 Filter & Search Companies")
    col1,col2,col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("🔍 Search", placeholder="Company name, industry, etc...")
    with col2 :
        industries = ['All'] + sorted(df['Industry'].unique().tolist())
        selected_industry = st.selectbox("🏭 Industry", industries)
    with col3:
        locations = ['All'] + sorted(df['Location'].unique().tolist())
        selected_location = st.selectbox("📍 Location", locations)
    
    
    
    filtered_df = filter_data(df, search_term, selected_industry, selected_location)
    if not filtered_df.empty:
        st.markdown("---")
        st.markdown("### 📊 Export Data")
        col1, col2, col3 = st.columns([1, 1, 4])
        
        with col1:
            csv_data = export_to_csv(filtered_df)
            st.download_button(
                label="📄 Download CSV",
                data=csv_data,
                file_name=f"companies_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                help="Export filtered data to CSV format"
            )
        
        with col2:
            excel_data = export_to_excel(filtered_df)
            st.download_button(
                label="📊 Download Excel",
                data=excel_data,
                file_name=f"companies_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                help="Export filtered data to Excel format"
            )
    
    st.markdown("---")
    
    if not filtered_df.empty:
        st.markdown(f"### 🏢 Companies ({len(filtered_df)} found)")
        cols = st.columns([2, 2, 1.5, 3, 1, 1, 2, 1.5])
        headers = ['Company', 'Industry', 'Location', 'Address', 'Rate', 'Phone', 'Website', 'ChatRAG']
        for i, header in enumerate(headers):
            cols[i].markdown(f"**{header}**")
        
        st.markdown("---")
        
        for idx, row in filtered_df.iterrows():
            cols = st.columns([2, 2, 1.5, 3, 1, 1, 2, 1.5])
            cols[0].markdown(f"**{row['Company']}**")
            cols[1].markdown(row['Industry'])
            cols[2].markdown(row['Location'])
            cols[3].markdown(row['Address'])
            cols[4].markdown(f"⭐ {row['Rate']}")
            cols[5].markdown(row['Phone'])
            cols[6].markdown(f"[ {row['Website']}](https://{row['Website']})")
            
            if cols[7].button("💬 Chat", key=f"summary_{idx}", help="Get AI Summary"):
                initialize_company_rag(row['Company'], row['Website'])
                st.session_state.page = "💬 ChatRAG"
                st.rerun()
            
            st.markdown("---")
    else:
        st.info("🔍  No companies found matching your search criteria. Try adjusting your filters.")


def render_chat_rag():
    if st.session_state.current_company:
        st.title(f"💬 Chat about {st.session_state.current_company}")
        
        if st.button("← Back to Search"):
            st.session_state.current_company = None
            st.session_state.chat_history = []
            st.session_state.documents_loaded = False
            st.rerun()
        
        st.markdown("---")
        
        if st.session_state.documents_loaded:
            for chat in st.session_state.chat_history:
                with st.chat_message("user"):
                    st.write(chat['question'])
                with st.chat_message("assistant"):
                    st.write(chat['answer'])
            
            if question := st.chat_input("Ask anything about this company..."):
                with st.chat_message("user"):
                    st.write(question)
                
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        from modules.chat_rag import retrieve_docs, answer_question
                        retrieve_documents = retrieve_docs(question)
                        context = "\n\n".join([doc.page_content for doc in retrieve_documents])
                        answer = answer_question(question, context) if context else "I don't have enough information to answer that question about this company."
                        st.write(answer)
                
                st.session_state.chat_history.append({
                    "question": question,
                    "answer": answer
                })
                st.rerun()
        else:
            st.warning("⚠️ Company information is still loading. Please wait...")
            if st.button("🔄 Retry Loading"):
                st.rerun()
    else:
        st.title("💬 RAG Chat")
        st.info("👈 Please select a company from the search page to start chatting!")
        if st.button("Go to Company Search"):
            st.rerun()