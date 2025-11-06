# app.py
from rag_pipeline import load_vectorstore
from langchain_community.llms import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

def main():
    print("Đang tải cơ sở dữ liệu đã lưu...")
    vectordb = load_vectorstore("persistent_chroma_db")
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    # Mô hình LLM từ Ollama (chạy local)
    llm = Ollama(model="ontocord/vinallama")

    # Prompt cho quá trình hỏi – đáp
    prompt = ChatPromptTemplate.from_template("""
    Hãy trả lời câu hỏi của người dùng bằng tiếng Việt dựa trên ngữ cảnh dưới đây.
    Nếu không có thông tin phù hợp, hãy trả lời "Tôi không chắc chắn về điều đó."

    Ngữ cảnh:
    {context}

    Câu hỏi:
    {input}
    """)

    # Tạo chuỗi xử lý tài liệu trước khi đưa vào LLM
    question_answer_chain = create_stuff_documents_chain(llm, prompt)

    # Kết hợp chuỗi hỏi đáp và bộ truy xuất dữ liệu (RAG)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    print("Hệ thống sẵn sàng! Gõ 'exit' để thoát.\n")
    while True:
        query = input("Câu hỏi: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Tạm biệt!")
            break

        result = rag_chain.invoke({"input": query})
        print(f"💡 Trả lời: {result['answer']}\n")

if __name__ == "__main__":
    main()
