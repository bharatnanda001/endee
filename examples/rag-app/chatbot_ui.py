import streamlit as st
from chatbot import generate_answer

st.title("RAG AI Chatbot")

query = st.text_input("Ask a question")

if query:
    response = generate_answer(query)
    st.write(response)
