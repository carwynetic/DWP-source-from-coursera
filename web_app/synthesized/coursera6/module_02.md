# Module 2: Web API Essentials — REST API and GraphQL

> **Tư tưởng cốt lõi:** Microservices giao tiếp với thế giới bên ngoài và với nhau qua Web APIs: **REST** cung cấp giao diện đồng nhất, phi trạng thái (stateless) dựa trên tài nguyên và động từ HTTP (`POST`, `GET`, `PUT`, `DELETE`); **API Gateway** đóng vai trò cổng vào duy nhất cho backend; **Flask**, **cURL**, **Postman** và **Swagger (OpenAPI)** hợp thành bộ công cụ xây dựng, kiểm thử và tài liệu hóa API; trong khi **GraphQL** giải quyết bài toán over-fetching/under-fetching qua một endpoint duy nhất.

## 1. Kiến trúc RESTful API & Các phương thức HTTP

- **REST (Representational State Transfer):** Phong cách kiến trúc chuẩn quy định cách các hệ thống giao tiếp qua HTTP.
- **Đặc trưng cốt lõi của RESTful API:**
  1. **Uniform Interface (Giao diện đồng nhất):** Mọi tài nguyên được định danh bằng URI chuẩn (vd `/products`, `/products/42`).
  2. **Stateless (Phi trạng thái):** Mỗi request từ client phải chứa đầy đủ thông tin để server xử lý (token, tham số); server không lưu session của client giữa các request → dễ mở rộng ngang (scalable).
  3. **Client–Server & Cacheable:** Tách biệt rõ giao diện người dùng và lưu trữ dữ liệu; phản hồi (thường là JSON/XML) có thể cache để tăng tốc.

### Bảng ánh xạ HTTP Methods ↔ Thao tác CRUD

| HTTP Method | Mục đích CRUD | Ví dụ Endpoint & Lệnh `cURL` chuẩn |
| --- | --- | --- |
| **`POST`** | **Create** (tạo tài nguyên mới) | `curl -X POST http://api.example.com/products -H "Content-Type: application/json" -d '{"name":"Laptop"}'` |
| **`GET`** | **Read** (truy vấn danh sách hoặc 1 tài nguyên) | `curl -X GET http://api.example.com/products` (hoặc đơn giản `curl http://api.example.com/products`) |
| **`PUT`** | **Update** (cập nhật toàn bộ tài nguyên theo ID) | `curl -X PUT http://api.example.com/products/1 -H "Content-Type: application/json" -d '{"name":"Laptop Pro"}'` |
| **`DELETE`** | **Delete** (xóa tài nguyên theo ID) | `curl -X DELETE http://api.example.com/products/1` |

## 2. API Gateway — Cổng vào duy nhất cho Microservices

- **Vai trò:** **API Gateway** đóng vai trò **"cánh cửa duy nhất" (single entry point / reverse proxy)** đứng trước toàn bộ hệ thống backend microservices, định tuyến request đến đúng dịch vụ đích và cho phép cắm thêm các tính năng dùng chung:
  - Xác thực/Phân quyền (Authentication/Authorization — lưu ý trong hệ thống microservices, **User / Identity Microservice** chịu trách nhiệm định danh người dùng).
  - Rate limiting, caching, logging, SSL termination, protocol translation.
  - Giúp dễ dàng **mở rộng hoặc thay thế** các dịch vụ backend mà không làm gãy ứng dụng client.
- **Nhược điểm tiềm ẩn (Drawbacks) cần đánh đổi:**
  1. Có thể trở thành **Single Point of Failure (điểm lỗi đơn)** hoặc **nút thắt cổ chai hiệu năng (performance bottleneck)** nếu không thiết kế dự phòng/scale tốt.
  2. Tăng **độ phức tạp vận hành và thêm một bước nhảy mạng (extra network hop / latency)**.

## 3. Bộ công cụ xây dựng, kiểm thử & tài liệu hóa API

| Công cụ / Chuẩn | Bản chất & Công dụng chính |
| --- | --- |
| **Flask** | **Micro web framework** nhẹ của Python dùng để xây dựng nhanh các REST API và dịch vụ web (không ép buộc ORM hay cấu trúc cồng kềnh) |
| **cURL** | Công cụ dòng lệnh (CLI) truyền tải dữ liệu qua URL (HTTP/HTTPS, FTP...), lý tưởng để test nhanh API hoặc nhúng vào script tự động |
| **Postman** | Ứng dụng giao diện đồ họa chuyên dùng để **tạo, gửi, kiểm thử tự động và quản lý bộ sưu tập (collections)** các yêu cầu API |
| **Swagger & OpenAPI Specification** | **OpenAPI Specification (OAS)** định nghĩa một **giao diện chuẩn hóa, độc lập ngôn ngữ** mô tả toàn bộ endpoints, tham số, schema request/response của REST API (bằng YAML/JSON); **Swagger** là bộ công cụ tuân theo chuẩn OpenAPI để tự động sinh tài liệu tương tác (Swagger UI) và test trực tiếp trên trình duyệt |

*(Lưu ý kiến thức Python bổ trợ xuất hiện trong ngữ cảnh bài học: thư viện **SciPy** trong Python dùng cho tính toán khoa học & kỹ thuật — tối ưu hóa, đại số tuyến tính, thống kê, xử lý tín hiệu.)*

## 4. So sánh phản biện: REST API vs. GraphQL

| Tiêu chí | RESTful API | GraphQL |
| --- | --- | --- |
| **Bản chất** | Phong cách kiến trúc hướng tài nguyên (resource-based) | **Ngôn ngữ truy vấn (query language)** cho API, độc lập ngôn ngữ lập trình (language-agnostic) |
| **Số lượng Endpoint** | Nhiều endpoint theo từng tài nguyên (`/users`, `/orders`, `/products`) | **Duy nhất 1 endpoint** (thường là `/graphql`) |
| **Kiểm soát dữ liệu trả về** | Server quyết định cấu trúc trả về → dễ xảy ra **Over-fetching** (dư thừa trường) hoặc **Under-fetching** (phải gọi nhiều request liên tiếp) | **Client chỉ định chính xác đúng các trường cần lấy** trong 1 lần gọi duy nhất (khai báo kiểu dữ liệu dưới dạng nodes trong **Schema**) |
| **Khi nào chọn** | API công khai đơn giản, tận dụng tốt HTTP caching, chuẩn mực rộng rãi | Ứng dụng di động/phức tạp cần gom dữ liệu từ nhiều tài nguyên lồng nhau và tiết kiệm băng thông |

```graphql
# Ví dụ GraphQL Query: chỉ lấy đúng trường name của sản phẩm, không trả về dữ liệu thừa
query {
  product(id: "101") {
    name
    price
  }
}
```

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- **RESTful API** có đặc trưng **stateless, scalable, uniform interface**; giao tiếp bằng các phương thức chuẩn: `POST` (tạo mới), `GET` (đọc), `PUT` (cập nhật), `DELETE` (xóa).
- **API Gateway** là cổng vào duy nhất cho backend giúp dễ thay thế/scale dịch vụ, nhưng cần đề phòng rủi ro **single point of failure** và **độ trễ/độ phức tạp tăng thêm**.
- **Flask** là micro web framework Python; **Swagger** tuân theo chuẩn **OpenAPI Specification**; **Postman** & **cURL** dùng để gửi và kiểm thử API; **GraphQL** dùng 1 endpoint duy nhất cho phép client lấy chính xác dữ liệu cần thiết.
