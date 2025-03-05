import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA



try:
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro-latest")  # Missing API Key?
except Exception as e:
    print("Error initializing LLM:", e)

# Load Instructor Embeddings
try:
    embedding_function = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
except Exception as e:
    print("Error initializing embeddings:", e)

vector_db_filepath = "faiss_index"


def create_vector_db():
    try:
        df = pd.read_csv("faqs.csv", encoding="utf-8")

        df.columns = df.columns.str.strip()  # Remove extra spaces or hidden characters
        df.to_csv("faqs_clean.csv", index=False, encoding="utf-8")

        # Load CSV data
        loader = CSVLoader(file_path="faqs_clean.csv", source_column="prompt")
        docs = loader.load()
        print(f"Loaded {len(docs)} documents from CSV.")

        # Create FAISS vector database
        vector_db = FAISS.from_documents(docs, embedding_function)

        # Save FAISS database for future use
        vector_db.save_local(vector_db_filepath)

        print("FAISS vector database created and saved successfully!")

    except Exception as e:
        print("Error in create_vector_db:", e)

def load_qa_chain():
    # Loading the vector database from the local folder
    vectordb = FAISS.load_local(vector_db_filepath, embedding_function, allow_dangerous_deserialization=True)

    # Creating a retriever to retrieve information from our vector database
    retriever = vectordb.as_retriever()

    # Creating a prompt template and chain
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain




if __name__ == "__main__":
    chain = load_qa_chain()
    print(chain("Do you provide internships and do you have any EMI options?"))
