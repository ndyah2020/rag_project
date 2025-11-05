from rag_pipeline import get_embedding_function
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM as Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


DB_DIR = "persistent_chroma_db"


def create_rag_chain():
    template = """
        Bạn là một trợ lý AI hữu ích. 
        Chỉ trả lời câu hỏi dựa trên nội dung được cung cấp dưới đây. 
        Nếu nội dung không chứa câu trả lời, hãy nói "Tôi không tìm thấy thông tin trong tài liệu."

        Nội dung:
        {context}

        Câu hỏi:
        {question}
    """
    embedding_function = get_embedding_function()

    vector_store = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding_function
    )

    chunks = vector_store.as_retriever(search_kwargs={"k": 5})
    
    prompt = ChatPromptTemplate.from_template(template)
    llm = Ollama(model="ontocord/vinallama")
    
    rag_chain = (
        {"context": chunks, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

def main():
    rag_chain = create_rag_chain()
    while True:
        try :
            query = input("\nYour question: ")
            if query.lower() == 'exit':
                break
            if not query.strip():
                continue
            
            print("Quering...")     
            for chunk in rag_chain.stream(query):
                print(chunk, end="", flush=True) 
            print()
            
        except EOFError:
            break
        except KeyboardInterrupt:
            break
     
if __name__ == "__main__":
   main()
