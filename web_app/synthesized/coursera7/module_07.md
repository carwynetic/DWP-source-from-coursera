# Module 7: Enhancement of Car Dealership Portal & Enterprise Integration

> **Tư tưởng cốt lõi:** Vượt qua phiên bản MVP của Capstone để mở rộng cổng thông tin **Best Cars Dealership** theo tiêu chuẩn doanh nghiệp: bổ sung tính năng tìm kiếm/lọc nâng cao phía React, gia cố bảo mật & hiệu năng, và hiểu cách các tổ chức kết nối đa ứng dụng, API, sự kiện và dữ liệu xuyên suốt **Hybrid Cloud** bằng các nền tảng tích hợp cấp doanh nghiệp như **IBM Cloud Pak for Integration**.

## 1. Các hướng nâng cấp kỹ thuật trực tiếp cho Car Dealership Portal

Sau khi hoàn thiện MVP ở Module 1–6, kỹ sư Full-Stack có thể mở rộng cổng thông tin đại lý theo 4 trục thực tế:

| Trục nâng cấp | Cải tiến cụ thể trên kiến trúc hiện có | Giá trị mang lại |
| --- | --- | --- |
| **1. Trải nghiệm Tìm kiếm & Lọc (React UX)** | Thay dropdown lọc bang đơn giản bằng **ô tìm kiếm đa tiêu chí thời gian thực** (tìm theo tên đại lý, thành phố, bang, địa chỉ) kết hợp phân trang (pagination) và xử lý trạng thái loading/empty state | Giảm thao tác tìm kiếm khi số lượng đại lý tăng từ vài chục lên hàng nghìn |
| **2. Chống nghẽn cổ chai Sentiment Analysis** | Hiện tại `get_dealer_reviews` gọi tuần tự API Sentiment cho từng bình luận → chuyển sang **chấm điểm cảm xúc ngay tại thời điểm `POST /add_review`** và lưu luôn trường `sentiment` vào MongoDB (hoặc xử lý bất đồng bộ qua Message Queue) | Giảm độ trễ đọc trang chi tiết đại lý từ `O(N)` lời gọi HTTP xuống **`O(1)`**! |
| **3. Bảo mật & Quan sát (Hardening)** | Bật HTTPS/TLS, cấu hình CSRF/CORS chặt chẽ, giới hạn tần suất gọi API (rate limiting), chuyển SQLite sang PostgreSQL Managed DB và thêm Health Check (`/healthz`) + Readiness Probe trong `deployment.yaml` | Đạt chuẩn vận hành production ổn định, tự phục hồi khi có sự cố |
| **4. Tự động hóa CD (Continuous Deployment)** | Mở rộng GitHub Actions từ chỉ chạy Linting (CI) sang **tự động build Docker image, push lên Registry và cập nhật Kubernetes Deployment** khi merge vào `main` | Khép kín quy trình CI/CD hoàn toàn không thao tác tay |

## 2. Tích hợp ứng dụng cấp Doanh nghiệp với IBM Cloud Pak for Integration

Trong doanh nghiệp lớn, một hệ thống không chỉ có 3 microservices như Capstone mà gồm hàng trăm ứng dụng cũ (legacy), dịch vụ Cloud-Native, cơ sở dữ liệu và luồng sự kiện (event streams). **IBM Cloud Pak for Integration** (chạy trên Red Hat OpenShift) giải quyết bài toán kết nối toàn diện trên môi trường **Hybrid Cloud** qua 5 năng lực cốt lõi:

1. **API Management:** Quản lý vòng đời API, bảo mật, phân tích lưu lượng và cổng developer portal tập trung.
2. **Application Integration:** Kết nối mượt mà giữa ứng dụng SaaS, hệ thống nội bộ (on-premises) và microservices mới.
3. **Enterprise Messaging:** Đảm bảo truyền tải thông điệp đáng tin cậy, không mất dữ liệu (như IBM MQ) cho giao dịch quan trọng.
4. **Event Streaming:** Xử lý luồng sự kiện thời gian thực thông lượng cao (dựa trên Apache Kafka) để tách rời (decouple) hoàn toàn giữa nhà sản xuất và người tiêu dùng dữ liệu.
5. **High-Speed Data Transfer:** Truyền tải tập dữ liệu lớn an toàn, tốc độ cao xuyên vùng địa lý.

## 3. Toàn cảnh hành trình 7 Khóa học DWP301c

Hoàn thành Module 7 cũng là hoàn tất toàn bộ bản đồ kiến thức **DWP301c — Full Stack Cloud-Native Development**:
- **Khóa 1:** SQL, RDBMS vs. NoSQL, Django ORM, Full-Stack Django MVC/MVT.
- **Khóa 2:** HTML5 ngữ nghĩa, CSS Layouts & Frameworks, JavaScript ES6 & DOM APIs.
- **Khóa 3:** Git DVCS, Branching/Merging, Fork/Clone, Pull Request & GitHub Workflow.
- **Khóa 4:** React Components, Virtual DOM, Hooks (`useState`/`useEffect`), Redux Toolkit.
- **Khóa 5:** Docker Containers, Kubernetes Orchestration, Autoscaling, OpenShift & Istio.
- **Khóa 6:** Twelve-Factor, Microservices Patterns, REST/GraphQL, Serverless & IBM Cloud Code Engine.
- **Khóa 7:** Tích hợp toàn bộ thành hệ thống **Best Cars Dealership** hoàn chỉnh với CI/CD và Kubernetes.
