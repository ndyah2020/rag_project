from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import os

def load_documents(source_dir):
    documents = []
    for filename in os.listdir(source_dir): 
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(source_dir, filename)
            loader = PyMuPDFLoader(pdf_path)
            documents.extend(loader.load())
    return documents

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000, 
        chunk_overlap = 200)
    return text_splitter.split_documents(documents)

def get_embedding_function():
    return OllamaEmbeddings(model="nomic-embed-text")
