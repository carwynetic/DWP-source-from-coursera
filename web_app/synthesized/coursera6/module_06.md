# Module 6: Optional — OpenShift Essentials & Working with OpenShift and Istio

> **Tư tưởng cốt lõi:** Ôn tập và đào sâu cách triển khai **Microservices trên Red Hat OpenShift** (nền tảng Kubernetes doanh nghiệp chạy đa môi trường on-premises & cloud với quy trình build tự động bằng Jenkins/S2I) kết hợp **Istio Service Mesh** làm lớp chuyên biệt điều phối lưu lượng, mã hóa **mTLS** và thu thập **Telemetry** cho toàn bộ các dịch vụ.

## 1. Red Hat OpenShift — Bản chất & Ẩn dụ so sánh với Kubernetes

- **OpenShift chạy ở đâu?** Là nền tảng **Hybrid Cloud**, OpenShift có thể chạy linh hoạt trên cả **On-premises** lẫn **Public/Private Cloud**.
- **Ẩn dụ kinh điển (OpenShift vs. Kubernetes):** Trong bài giảng *Red Hat OpenShift Recap*, **Kubernetes** được ví như **động cơ (engine)** mạnh mẽ (hoặc **nhân Linux — Linux kernel**), còn **Red Hat OpenShift** là **chiếc xe hoàn chỉnh** (hoặc **bản phân phối Linux doanh nghiệp** như RHEL) bọc quanh nhân đó với đầy đủ công cụ build, CI/CD, bảo mật, giám sát và quản trị vòng đời ứng dụng.
- **Các tính năng gia tăng nổi bật trên OpenShift cho Microservices:**
  - Hỗ trợ thao tác song song qua **CLI (`oc`)** và **Web Console** trực quan.
  - Tự động tạo **Jenkins Job** (hoặc OpenShift Pipelines) để **build mã nguồn microservice thành container image**.
  - Tự động **đẩy (push) container image vừa build lên Container Registry** và **triển khai (deploy) container đó vào Cluster**.
  - Tích hợp sẵn công cụ **monitoring, logging, routing và quản lý dự án** giúp tăng năng suất lập trình viên.

## 2. Service Mesh & Istio trên OpenShift

### Tại sao Microservices cần Service Mesh?
Dù Microservices cho phép cập nhật độc lập, dùng đa ngôn ngữ và mở rộng riêng từng thành phần, nó kéo theo 3 bài toán vận hành khó:
1. Làm sao **mã hóa và xác thực giao tiếp giữa hàng chục service** an toàn mà không sửa code từng service?
2. Làm sao **điều hướng lưu lượng có kiểm soát** (traffic shifting cho Canary / A/B testing)?
3. Làm sao **quan sát (observability/telemetry)** toàn cảnh luồng gọi phân tán để tìm lỗi?

- **Service Mesh:** Là một **lớp hạ tầng chuyên biệt (dedicated infrastructure layer)** điều phối toàn bộ giao tiếp service-to-service, cung cấp các năng lực cốt lõi:
  - **Traffic Shifting / Management** (phân luồng lưu lượng theo tỷ lệ phiên bản v1/v2, retry, circuit breaking).
  - **Mutual TLS (mTLS) Security:** Tự động **mã hóa lưu lượng và xác thực hai chiều** giữa các microservices. *(Lưu ý quan trọng: OpenShift KHÔNG tự mặc định mã hóa mTLS giữa mọi service thay cho Istio — chính **Istio** cung cấp năng lực mTLS này!)*
  - **Telemetry & Observability:** Thu thập tập trung **metrics, distributed tracing và access logs** *(không chỉ đơn thuần là logging)*.

### Các tài nguyên cấu hình chính của Istio (Core Istio Resources)

| Tài nguyên Istio (CRD) | Vai trò điều phối lưu lượng |
| --- | --- |
| **`Gateway`** | Cấu hình bộ cân bằng tải ở biên của Mesh (edge load balancer) để nhận lưu lượng HTTP/HTTPS đi vào hoặc đi ra cụm |
| **`VirtualService`** | Định nghĩa **quy tắc định tuyến lưu lượng** (routing rules): ví dụ chia 90% traffic tới phiên bản `v1` và 10% tới `v2`, cấu hình timeout/retry |
| **`DestinationRule`** | Định nghĩa các **chính sách áp dụng sau khi định tuyến** tới đích: chia tập con (`subsets: v1, v2`), thuật toán cân bằng tải, cấu hình **mTLS** và circuit breaker |

```yaml
# Ví dụ Istio VirtualService chia lưu lượng Canary 80% v1 / 20% v2
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews-route
spec:
  hosts:
    - reviews
  http:
    - route:
        - destination:
            host: reviews
            subset: v1
          weight: 80
        - destination:
            host: reviews
            subset: v2
          weight: 20
```

## 3. Bẫy thường gặp (Critical Pitfalls — Hay gặp trong Quiz!)

1. **Cho rằng "Istio không mã hóa lưu lượng vì OpenShift đã làm sẵn":** **SAI!** Chính Istio cung cấp lớp bảo mật **mutual TLS (mTLS)** tự động mã hóa và xác thực giao tiếp giữa các microservice bên trong cụm.
2. **Cho rằng "Service Mesh chỉ là lớp cung cấp logging cho OpenShift":** **SAI / THIẾU!** Service Mesh là lớp điều phối toàn diện gồm **Security (mTLS) + Traffic Management (traffic shifting) + Telemetry (metrics, tracing, logging)**.
3. **Nhầm lẫn vai trò `VirtualService` và `DestinationRule`:** `VirtualService` quyết định *request đi đâu* (routing rules/weights); `DestinationRule` định nghĩa *các phiên bản đích (`subsets`) và chính sách kết nối (load balancing, TLS)* tại điểm đến.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- **OpenShift** = Kubernetes + hệ sinh thái công cụ doanh nghiệp (tạo **Jenkins job** tự build container → **push lên Registry → deploy lên Cluster**), chạy được cả **on-premises và cloud**.
- **Istio** cấu hình chủ yếu qua `Gateway`, `VirtualService`, và `DestinationRule` để mang lại **Traffic Shifting**, **mTLS Security**, và **Telemetry** cho hệ thống Microservices.
