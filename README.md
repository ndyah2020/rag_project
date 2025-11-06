# AI Chính xác
## 1. Mục đích
Xây dựng một hệ thống Hỏi-Đáp (RAG) có khả năng đọc và hiểu một tài liệu PDF để trả lời các câu hỏi của người dùng dựa trên nội dung tài liệu đó.

## 2. Nguồn dữ liệu thử nghiệm
- Báo cáo Chỉ số Thương mại điện tử Việt Nam 2025: [Báo cáo EBI 2025](https://drive.google.com/file/d/18hUNrKSJXQmKOQl7mLhqhV1bg2MiKcmN/view)

## 3. Cấu trúc thư mục

rag_project/                     <br>
├── source_documents/            <br>
│   └── BaoCaoEBI2025.pdf        <br>
├── persistent_chroma_db/        <br>
├── ingest.py                    <br>
├── app.py                       <br>
├── rag_pipeline.py              <br>
└── requirements.txt             <br>

- Trong đó
    + **source_documents** chứa file pdf là nguồn thông tin
    + **persistent_chroma_db** được tạo tự động (không cần tạo thủ công)

## 4. Các bước chạy dự án
### 4.1. Cài python (>= 3.10)
- Kiểm tra phiên bản Python hiện tại
  ```
  python --version
  ```
- Nếu chưa có: [Download Python](https://www.python.org/downloads/)

### 4.2. Cài Ollama
- Tải Ollama: [Download Ollama](https://ollama.com/download)
- Kiểm tra:
  ```
  ollama --version
  ```

### 4.3. Tải các model cần thiết
- Tải model
  ```
  ollama pull nomic-embed-text
  ollama pull ontocord/vinallama
  ```

- Kiểm tra các mô hình hiện có
  ```
  ollama list
  ```

### 4.4. Tạo môi trường ảo
- Mở thư mục chứa dự án
- Ở Command Prompt, chạy lệnh sau để tạo môi trường ảo
  ```
  python -m venv venv
  ```
- Vào môi trường ảo
  ```
  venv\Scripts\activate
  ```

*Lưu ý: Cách thoát khỏi môi trường ảo (sau khi đã chạy xong dự án)*
```
deactivate
```

### 4.5. Cài các thư viện cần thiết
```
pip install -r requirements.txt
```

### 4.6. Thêm nguồn tìm kiếm
- Đặt file muốn sử dụng làm nguồn tìm kiếm thông tin vào thư mục **source_documents** (ví dụ EBI 2025 ở trên)

### 4.7. Chạy chương trình
- Chạy ingest.py
  ```
  python ingest.py
  ```

- Sau đó chạy app.py
  ```
  python app.py
  ```
