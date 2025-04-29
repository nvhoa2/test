# System Patterns

**Kiến trúc tổng thể:**  
- Kiểu client-server: Frontend (Vue 3) giao tiếp với Backend (FastAPI) qua HTTP API.
- Backend đóng vai trò trung gian: fetch dữ liệu từ GitHub, gửi tới AI (mock), trả kết quả cho frontend.

**Các quyết định kỹ thuật chính:**  
- Sử dụng FastAPI cho backend để dễ mở rộng, async, tích hợp tốt với Python ecosystem.
- Sử dụng Vue 3 Composition API cho frontend để code ngắn gọn, dễ bảo trì.
- Mock AI response ở giai đoạn MVP để phát triển nhanh, dễ kiểm thử.

**Mối quan hệ thành phần:**  
- Frontend gửi request tới endpoint `/ask` của backend.
- Backend fetch README từ GitHub, gửi nội dung + câu hỏi tới AI agent (mock).
- Backend trả về phản hồi cho frontend hiển thị.
