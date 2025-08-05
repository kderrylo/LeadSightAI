RAG_TEMPLATE ="""
You are an assistant for question-answering tasks about companies. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Keep the answer informative but concise.
Question: {question} 
Context: {context} 
Answer:
"""

MODEL_NAME="llama3.2:3b"
CHUNK_SIZE=1000
CHUNK_OVERLAP=200