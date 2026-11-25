# Module 5: Final Project — Dealer Evaluation Microservices on Serverless

> **Tư tưởng cốt lõi:** Tổng hợp toàn bộ kiến thức Khóa 6 (Twelve-Factor, RESTful API với Flask/Express, đóng gói Docker, và triển khai Serverless trên **IBM Cloud Code Engine**) để hoàn thiện và triển khai hệ thống đa dịch vụ (**Back-End Microservices + Front-End**) hoạt động thực tế trên nền tảng đám mây.

## 1. Kiến trúc hệ thống Microservices trong Final Project

Trong dự án cuối khóa, bạn kết nối nhiều microservice độc lập cùng chạy trên **IBM Cloud Code Engine** — mô hình kiến trúc trực tiếp chuẩn bị cho **Khóa 7 (Full Stack Capstone)**:

```text
[ User Browser / Front-End Web App ]
                 │
                 ▼  (HTTPS REST API)
┌──────────────────────────────────────────────────────────┐
│           IBM Cloud Code Engine Project                  │
│                                                          │
│  ┌──────────────────────┐    ┌────────────────────────┐  │
│  │ Products / Dealer    │    │ Dealer Evaluation /    │  │
│  │ Details Microservice │    │ Pricing Microservice   │  │
│  │ (Node.js / Express)  │    │ (Python / Flask)       │  │
│  └──────────────────────┘    └────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

## 2. Quy trình End-to-End triển khai dự án cuối khóa

1. **Xây dựng & Kiểm thử cục bộ (Local Testing):**
   - Hoàn thiện các REST API endpoints (`GET`, `POST`, `PUT`, `DELETE`) trên từng microservice độc lập.
   - Kiểm tra phản hồi JSON bằng **`cURL`** hoặc **Postman** và xác minh tài liệu **Swagger / OpenAPI**.
2. **Đóng gói Container Image (Containerization):**
   - Viết `Dockerfile` chuẩn cho từng microservice (`FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`).
   - Build và đẩy image lên Container Registry (`docker build`, `docker push`) hoặc dùng trực tiếp chế độ **Build & Deploy** từ Git của Code Engine.
3. **Triển khai Serverless lên IBM Cloud Code Engine:**
   - Tạo từng Application bằng `ibmcloud ce application create --name <svc> --image <ref> --port <port>`.
   - Truyền URL của back-end microservices vào front-end qua **biến môi trường (Config — Twelve-Factor #4)** thay vì hard-code `localhost`.
4. **Xác minh & Cập nhật không gián đoạn:**
   - Gọi kiểm thử từng endpoint công khai (`curl <app-url>/...`), kiểm tra giao diện web hiển thị đúng dữ liệu từ các microservice.
   - Thực hiện cập nhật phiên bản mới bằng `ibmcloud ce application update` khi có thay đổi.

## 3. Bẫy thường gặp khi ghép nối nhiều Microservices Serverless

1. **Quên cấu hình CORS (Cross-Origin Resource Sharing):** Khi Front-End và Back-End chạy trên 2 subdomain khác nhau của Code Engine, trình duyệt sẽ chặn request `fetch()` nếu Back-End không trả về header `Access-Control-Allow-Origin` phù hợp (`flask-cors` hoặc `cors` trong Express).
2. **Hard-code địa chỉ `http://localhost:5000` trong mã Front-End:** Khi deploy lên cloud, `localhost` trỏ về chính máy người dùng chứ không phải microservice; luôn cấu hình endpoint thông qua biến môi trường.
3. **Cold start lần gọi đầu tiên:** Do Code Engine tự scale-to-zero khi không có tải, request đầu tiên sau thời gian nghỉ có thể mất vài giây — cần đảm bảo client xử lý trạng thái loading và timeout hợp lý.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- Dự án cuối Khóa 6 chứng minh năng lực thiết kế, đóng gói và vận hành **Polyglot Microservices** trên hạ tầng **Serverless** mà không cần quản trị server thủ công.
- Đây là mảnh ghép hạ tầng cuối cùng trước khi bước vào **Khóa 7: Full Stack Application Development Capstone Project**.
