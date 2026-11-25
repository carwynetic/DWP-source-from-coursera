# Module 4: Create and Deploy Microservices using Serverless (IBM Cloud Code Engine)

> **Tư tưởng cốt lõi:** Tự vận hành (self-hosting) microservices đòi hỏi quản lý quá nhiều lớp phức tạp từ đóng gói, mạng, cân bằng tải đến auto-scaling; **IBM Cloud Code Engine** là nền tảng Serverless PaaS được quản lý hoàn toàn (xây dựng trên Kubernetes & Knative) cho phép lập trình viên **build container image, triển khai Applications và chạy batch Jobs** chỉ bằng vài lệnh CLI hoặc giao diện Web Console.

## 1. Thách thức của Self-Hosted Microservices & Giá trị của PaaS

Khi tự triển khai (self-host) microservices lên máy chủ/VM thô, đội ngũ phải tự giải quyết hàng loạt bài toán phức tạp:
- Cấu hình phụ thuộc, môi trường thực thi, bảo mật thông tin xác thực (credentials).
- Chọn và quản trị hệ điều hành, web server, mạng, cân bằng tải, cơ sở dữ liệu.
- Tự xử lý **mở rộng động (dynamic scaling)** theo lưu lượng biến thiên (ví dụ mùa khuyến mãi e-commerce tăng đột biến rồi giảm về 0).

**Lợi ích chính của nền tảng PaaS / Serverless như IBM Cloud Code Engine:** Tự động hóa toàn bộ hạ tầng, bảo mật, cân bằng tải và auto-scaling (kể cả scale-to-zero), giúp lập trình viên **chỉ tập trung viết và phát hành mã nguồn microservices**.

## 2. Kiến trúc IBM Cloud Code Engine: 3 Chế độ & 4 Thực thể Cốt lõi

### 3 chế độ triển khai (Deployment Modes / Use Cases) của IBM Cloud Code Engine
1. **Deploy Applications:** Triển khai trực tiếp ứng dụng từ một container image có sẵn trên Registry.
2. **Build and Deploy Applications:** Tự động lấy mã nguồn từ Git repository, build thành container image rồi triển khai thành ứng dụng.
3. **Run Jobs:** Chạy các tác vụ theo lô (batch jobs) thực thi một lần rồi tự kết thúc (ví dụ xử lý dữ liệu, huấn luyện AI, dọn dẹp DB).

### 4 thực thể chính trong Code Engine

| Thực thể | Bản chất & Quan hệ quan trọng |
| --- | --- |
| **Project** | Đơn vị **nhóm logic (grouping)** bao bọc nhiều thực thể Code Engine (`Applications`, `Jobs`, `Builds`) dùng chung cấu hình mạng, không gian tên và quyền truy cập |
| **Application** | Chạy mã nguồn của bạn để **phục vụ các yêu cầu HTTP/HTTPS hoặc kết nối WebSocket**, tự động cấp URL công khai và tự co giãn số instance theo lưu lượng |
| **Build** | Quy trình chuyển đổi mã nguồn thành container image lưu lên Container Registry |
| **Job** | Chạy **một hoặc nhiều thực thể (instances) mã thực thi song song** để hoàn thành một tác vụ tính toán rồi dừng hẳn (không lắng nghe cổng HTTP liên tục như Application) |

> **Hai giao diện chính để thao tác với IBM Cloud Code Engine:** **Web Console (UI)** và **IBM Cloud CLI (`ibmcloud ce`)**.

## 3. Đóng gói Container Image & Triển khai Microservices

### Hai phương pháp build ứng dụng được IBM Cloud Code Engine hỗ trợ
1. **Dockerfile:** Lập trình viên cung cấp tệp `Dockerfile` mô tả chi tiết từng bước dựng image (dòng đầu tiên tiêu chuẩn luôn là chỉ thị **`FROM`** chỉ định base image).
2. **Cloud Native Buildpacks:** Code Engine tự động nhận diện ngôn ngữ lập trình (Python, Node.js, Java, Go...) trong mã nguồn và dựng container image mà **không cần viết Dockerfile**.

### Cách Code Engine truy cập Container Image & Lệnh CLI chuẩn
- Container image sau khi build được đẩy lên **Container Registry** (nơi lưu trữ & phân phối tập trung các container images như Docker Hub, Quay.io, IBM Cloud Container Registry).
- Code Engine truy cập image bằng **Image Reference (tên định danh đầy đủ của image trên registry)** — và nếu là private registry, sử dụng **Registry Access Secret** đã cấu hình trong Project.

```bash
# 1. Chọn Project làm việc trong IBM Cloud Code Engine
ibmcloud ce project select --name my-microservices-project

# 2. Tạo và triển khai một Application từ Container Image
ibmcloud ce application create --name dealer-api --image us.icr.io/my_ns/dealer-api:v1 --port 8080

# 3. Cập nhật ứng dụng đang chạy lên phiên bản image mới hoặc thêm biến môi trường
ibmcloud ce application update --name dealer-api --image us.icr.io/my_ns/dealer-api:v2 --env APP_MODE=prod

# 4. Lấy URL công khai và kiểm thử ứng dụng sau khi triển khai
ibmcloud ce application get --name dealer-api
curl https://dealer-api.<subdomain>.codeengine.appdomain.cloud/health
```

> **Kiểm thử sau khi deploy:** Sau khi triển khai thành công, Code Engine cung cấp một **URL công khai (HTTPS endpoint)**; bạn kiểm thử ngay bằng **trình duyệt web**, **`cURL`**, hoặc **Postman**.

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm lẫn giữa Code Engine Application và Code Engine Job:** Dùng **Application** cho web app / REST API lắng nghe HTTP/WebSocket liên tục; dùng **Job** cho tác vụ chạy xong rồi thoát (batch processing).
2. **Thiếu Registry Secret khi kéo ảnh từ Private Registry:** Code Engine sẽ báo lỗi `ImagePullBackOff` nếu image lưu ở private IBM Cloud CR mà chưa gắn `--registry-secret`.
3. **Không khai báo đúng cổng lắng nghe (`--port`):** Container trong ứng dụng lắng nghe cổng `5000` (Flask) hoặc `3000` (Express) nhưng không truyền `--port` khớp khi chạy `ibmcloud ce application create` sẽ khiến health check thất bại.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- **IBM Cloud Code Engine** hỗ trợ 3 chế độ: **Deploy apps**, **Build & deploy apps**, và **Run jobs**, thông qua **Web Console** hoặc **CLI (`ibmcloud ce`)**.
- **Project** gom nhóm các `Applications`, `Jobs`, `Builds`; 2 phương pháp build hỗ trợ là **Dockerfile** (luôn bắt đầu bằng `FROM`) và **Cloud Native Buildpacks**.
- Lệnh CLI tạo & triển khai ứng dụng: **`ibmcloud ce application create --name <app> --image <image-ref>`**; kiểm thử ngay qua URL công khai bằng trình duyệt, `cURL` hoặc Postman.
