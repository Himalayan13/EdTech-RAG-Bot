import streamlit as st
from langchain_helper import load_qa_chain, create_vector_db

# Set page configuration
st.set_page_config(
    page_title="Custom Database Ed Tech Services Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .stMarkdown {
        font-size: 18px;
    }
    .stHeader {
        font-size: 24px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("Custom Database Ed Tech Services Chatbot 🤖")
st.markdown("Welcome to the Ed Tech Services Chatbot! Ask any question related to your educational needs, and the chatbot will provide you with the best answers.")

# Button to create a new knowledge base
btn = st.button("Create New Knowledge Base")
if btn:
    st.success("New Knowledge Base created successfully!")

# Input for the question
question = st.text_input("Question:", placeholder="Type your question here...")

# If a question is asked, process it and display the answer
if question:
    chain = load_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])

# Footer
st.markdown("---")
st.markdown("© 2023 Ed Tech Services. All rights reserved.")