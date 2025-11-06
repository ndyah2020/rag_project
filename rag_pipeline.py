# rag_pipeline.py
import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def load_documents(source_dir="source_documents"):
    pdf_paths = [os.path.join(source_dir, f) for f in os.listdir(source_dir) if f.endswith(".pdf")]
    documents = []
    for path in pdf_paths:
        loader = PyMuPDFLoader(path)
        docs = loader.load()
        documents.extend(docs)
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)

def create_embeddings():
    return OllamaEmbeddings(model="nomic-embed-text")

def store_embeddings(docs, persist_directory="persistent_chroma_db"):
    embeddings = create_embeddings()
    vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory=persist_directory)
    vectordb.persist()
    print(f"Đã lưu dữ liệu vào thư mục: {persist_directory}")
    return vectordb

def load_vectorstore(persist_directory="persistent_chroma_db"):
    embeddings = create_embeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectordb
