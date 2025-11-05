from rag_pipeline import get_embedding_function, load_documents, split_documents
from langchain_chroma import Chroma

SOURCE_DIR = "source_documents"
DB_DIR = "persistent_chroma_db"

def main():
    documents = load_documents(SOURCE_DIR)
    chunks = split_documents(documents)
    embeddings_function = get_embedding_function()

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings_function,
        persist_directory=DB_DIR
    )

if __name__ == "__main__":
    main()