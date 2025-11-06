# ingest.py
from rag_pipeline import load_documents, split_documents, store_embeddings

def main():
    print("Bắt đầu xử lý tài liệu PDF...")
    docs = load_documents("source_documents")
    print(f"Đã tải {len(docs)} trang PDF.")
    
    split_docs = split_documents(docs)
    print(f"Đã chia thành {len(split_docs)} đoạn văn bản (chunks).")
    
    store_embeddings(split_docs)
    print("Quá trình nhập liệu hoàn tất!")

if __name__ == "__main__":
    main()
