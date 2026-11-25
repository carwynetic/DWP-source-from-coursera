# Module 1: Introduction to Microservices

> **Tư tưởng cốt lõi:** Kiến trúc **Microservices** tách ứng dụng thành các dịch vụ nhỏ độc lập theo năng lực nghiệp vụ, giao tiếp qua API nhẹ, cho phép dùng đa dạng công nghệ (polyglot) và mở rộng độc lập; kết hợp **Twelve-Factor App Methodology** (3 giai đoạn Code – Deploy – Operate) cùng các mẫu kiến trúc (Strangler, BFF, SPA) và tránh anti-patterns giúp xây dựng ứng dụng SaaS Cloud-Native bền vững.

## 1. Twelve-Factor App Methodology (Phương pháp luận 12 yếu tố cho SaaS)

Phương pháp luận Twelve-Factor do Heroku đề xuất giúp xây dựng các ứng dụng **Software-as-a-Service (SaaS)** hiện đại có khả năng di động, tự động hóa và mở rộng cao. *(Lưu ý: Microservices không phải điều kiện bắt buộc để áp dụng Twelve-Factor, nhưng hai tư tưởng này thường đi cặp rất ăn ý.)*

### Ánh xạ 12 yếu tố vào 3 giai đoạn của vòng đời phần mềm (SDLC)

| Giai đoạn SDLC | Các yếu tố Twelve-Factor tương ứng | Nội dung cốt lõi cần nhớ |
| --- | --- | --- |
| **1. Code** | 1. Codebase<br>2. Dependencies<br>3. Backing services | Một codebase quản lý bằng VCS cho nhiều bản deploy; khai báo tường minh mọi thư viện phụ thuộc; coi DB/queue/cache là tài nguyên gắn ngoài (attached resources) |
| **2. Deploy** | 4. Config<br>5. Build, release, run<br>6. Processes<br>7. **Port binding**<br>8. Disposability | Lưu cấu hình trong **biến môi trường** (không hard-code); tách rạch ròi 3 bước build/release/run; **Processes phải stateless & share-nothing**; tự phơi bày dịch vụ qua **Port binding**; khởi động nhanh & tắt êm (graceful shutdown) |
| **3. Operate** | 9. Concurrency<br>10. **Dev/Prod parity**<br>11. Logs<br>12. Admin processes | **Concurrency:** mở rộng ngang bằng cách chạy nhiều process song song; **Dev/Prod parity:** giữ môi trường phát triển, staging và production giống nhau nhất có thể; coi log như luồng sự kiện (event streams); chạy tác vụ quản trị (migration) như tiến trình một lần |

## 2. So sánh phản biện: Monolith vs. SOA vs. Microservices

| Tiêu chí | Monolithic Architecture | Service-Oriented Architecture (SOA) | Microservices Architecture |
| --- | --- | --- | --- |
| **Cấu trúc thành phần** | Các thành phần **gắn kết chặt chẽ (tightly coupled)** trong một khối triển khai duy nhất | Các dịch vụ dùng chung cấp doanh nghiệp, kết nối qua **Enterprise Service Bus (ESB)** | Các dịch vụ nhỏ, độc lập, **tách theo năng lực nghiệp vụ (business capabilities)**, giao tiếp qua REST/gRPC/Event |
| **Thành phần thiết kế** | Một codebase + một DB chung | 4 thành phần cốt lõi: **Service Provider**, **Service Consumer**, **Service Registry**, và **Service Contract** (định nghĩa cách Provider và Consumer tương tác) | Mỗi service sở hữu **cơ sở dữ liệu riêng (database per service)** & triển khai độc lập |
| **Công nghệ & Scale** | Một tech stack duy nhất; phải scale cả khối dù chỉ 1 chức năng quá tải | Chia sẻ tầng ESB trung tâm dễ thành điểm nghẽn | Tự do chọn công nghệ phù hợp từng service (Python, Node.js, Go...); **scale riêng từng service** |
| **Rủi ro & Cô lập lỗi** | Lỗi ở 1 module có thể đánh sập toàn hệ thống; triển khai chậm | Phức tạp ở ESB trung tâm | Lỗi ở 1 service **không tất yếu đánh sập** các service khác; phát hành nhanh, giảm rủi ro thay đổi |

## 3. Các mẫu thiết kế Microservices (Patterns) & Anti-Patterns

### Các Microservices Patterns trọng yếu

| Pattern | Mục đích & Khi nào áp dụng |
| --- | --- |
| **Strangler Pattern (Strangler Fig)** | **Di trú dần từ Monolith sang Microservices** một cách an toàn: từng tính năng mới hoặc được tách ra sẽ chạy trên microservice mới và định tuyến qua proxy/gateway, "bóp nghẹt" dần hệ thống cũ cho đến khi thay thế hoàn toàn mà không cần đập đi viết lại một lần |
| **Backend for Frontend (BFF)** | Tạo một tầng backend trung gian **chuyên biệt cho từng loại giao diện người dùng** (vd 1 BFF cho Mobile App, 1 BFF cho Web Desktop) để tổng hợp và định dạng dữ liệu tối ưu, giảm số lần gọi API từ client |
| **Single Page Application (SPA)** | Ứng dụng web tải **một trang HTML duy nhất** và cập nhật động nội dung qua JavaScript/AJAX mà không reload toàn trang; tương tác trực tiếp với Microservices thông qua APIs |
| **Service Discovery & Circuit Breaker** | Tự động định vị địa chỉ động của các service và ngắt mạch khi một service phụ thuộc gặp sự cố để tránh sụp đổ dây chuyền (cascading failure) |

### Khi nào nên tách nhỏ service & Các Anti-Patterns cần tránh
- **Khi nào tách dịch vụ lớn thành nhỏ hơn?** Khi một dịch vụ trở nên quá phức tạp để một nhóm nhỏ bảo trì, có tốc độ thay đổi khác nhau, hoặc cần mở rộng tải (scaling) độc lập.
- **Microservices Anti-Patterns phổ biến:**
  1. **Distributed Monolith:** Tách thành nhiều service nhưng lại phụ thuộc chặt chẽ và phải deploy đồng bộ cùng lúc → nhận đủ phức tạp của hệ phân tán mà mất hết lợi ích của Microservices!
  2. **Shared Database:** Nhiều microservice cùng đọc/ghi trực tiếp vào chung một bảng DB làm mất tính tự chủ dữ liệu.
  3. **Nano-services (Tách quá vụn):** Mỗi hàm nhỏ thành 1 service làm tăng vọt độ trễ mạng (network overhead) và chi phí vận hành.
  4. **Thiếu tự động hóa CI/CD & Giám sát tập trung:** Triển khai thủ công hàng chục service chắc chắn dẫn tới sai sót.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- Twelve-Factor yêu cầu **Processes phải stateless & share-nothing**; **Port binding** thuộc giai đoạn **Deploy**; **Dev/Prod parity** yêu cầu môi trường dev và prod càng giống nhau càng tốt.
- Monolith có các thành phần **tightly coupled**; trong SOA, **Service Contract** định nghĩa cách Provider và Consumer tương tác.
- **Strangler Pattern** dùng để chuyển đổi dần từ Monolith sang Microservices; **BFF (Backend for Frontend)** tối ưu tầng API riêng cho từng loại client (Web/Mobile).
