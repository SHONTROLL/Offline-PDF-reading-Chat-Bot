
import streamlit as st
from services.pdf_processor import process_pdf
from services.vectorstore import get_vectorstore
from services.llm import get_answer
import os

st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("📄 Simple PDF Chatbot (Streamlit)")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing PDF..."):
        chunks = process_pdf(file_path)
        vs = get_vectorstore(chunks)

    st.subheader("Ask a question about the PDF")
    user_query = st.text_input("Your question", "")

    if user_query:
        with st.spinner("Thinking..."):
            response = get_answer(vs, user_query)
            st.markdown(f"**Answer:** {response}")
