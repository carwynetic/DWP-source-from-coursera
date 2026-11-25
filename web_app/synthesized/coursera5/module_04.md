# Module 4: The Kubernetes Ecosystem — OpenShift, Istio & Operators

> **Tư tưởng cốt lõi:** Hệ sinh thái mở rộng xung quanh Kubernetes giải quyết các bài toán cấp doanh nghiệp: **Red Hat OpenShift** cung cấp nền tảng Hybrid Cloud hoàn chỉnh tích hợp sẵn CI/CD (`BuildConfig`, `ImageStream`, S2I) và bảo mật; **Operators & CRDs** tự động hóa vòng đời ứng dụng phức tạp; còn **Istio Service Mesh** tách biệt hoàn toàn quản lý lưu lượng, bảo mật mTLS và giám sát giữa các microservices thông qua sidecar proxy.

## 1. Red Hat OpenShift — Kubernetes cấp Doanh nghiệp cho Hybrid Cloud

- **Bản chất:** **Red Hat OpenShift** là nền tảng container Kubernetes cấp doanh nghiệp (enterprise-ready) được thiết kế chuyên biệt cho chiến lược **Open Hybrid Cloud** (quản lý đồng nhất Public, Private, Multi-Cloud và Edge).
- **Giá trị bổ sung của OpenShift so với Kubernetes thuần:**
  - Giao diện Web Console trực quan, dễ dùng hơn và cơ chế tự phục vụ (self-service provisioning) cho lập trình viên.
  - Tích hợp sẵn công cụ CI/CD (như **Jenkins**), **Container Registry nội bộ**, **ImageStreams**, **Builds (S2I)**, **Routes** (thay vì phải tự cài đặt Ingress Controller rời), cùng chính sách bảo mật chặt chẽ mặc định.
  - Công cụ dòng lệnh **`oc` CLI** (mở rộng từ `kubectl`, hỗ trợ lệnh như `oc project`, `oc get`, `oc version`, `oc new-app`).

## 2. OpenShift Builds, ImageStreams & Build Triggers

- **Build & BuildConfig:** *Build* là quá trình chuyển đổi đầu vào thành đối tượng kết quả (thường là biến mã nguồn thành Container Image). **`BuildConfig`** là bản thiết kế khai báo **Build Input Sources** (vd: **Git repository**, **Dockerfile inline**, **Binary inputs / Image inputs**) và **Build Strategy**:
  - **Source-to-Image (S2I):** Tự động tiêm mã nguồn ứng dụng vào builder image tạo thành container image hoàn chỉnh mà **không cần viết Dockerfile**.
  - **Docker Strategy:** Build trực tiếp từ `Dockerfile`.
  - **Custom Strategy:** Dùng custom builder image tự định nghĩa.
- **ImageStream:** Lớp trừu tượng trong OpenShift để tham chiếu và theo dõi nhiều container image/tag tại một địa chỉ thống nhất. **2 tính năng cốt lõi của ImageStream:**
  1. Cung cấp một **địa chỉ tham chiếu ảo duy nhất** che giấu vị trí vật lý thực của image trong registry ngoài/nội bộ.
  2. **Tự động phát hiện khi image gốc cập nhật phiên bản mới** để kích hoạt build hoặc triển khai lại ứng dụng.
- **3 loại Build Triggers tự động hóa build trong OpenShift:**
  1. **Webhook Trigger:** Kích hoạt build tự động mỗi khi có commit mới đẩy lên GitHub/GitLab.
  2. **Image Change Trigger:** Tự động rebuild khi base image trong `ImageStream` có phiên bản mới (vá lỗ hổng bảo mật tự động).
  3. **Configuration Change Trigger:** Tự động chạy build ngay khi một tài nguyên `BuildConfig` mới được tạo.

## 3. Operators, CRDs & Operator Framework

| Khái niệm | Vai trò trong mở rộng Kubernetes |
| --- | --- |
| **CRD (Custom Resource Definition)** | Cho phép **mở rộng Kubernetes API** bằng các loại tài nguyên tùy chỉnh mà không cần biên dịch lại API Server; hoạt động theo mô hình khai báo (declarative) và có thể quản lý trực tiếp bằng `kubectl` |
| **Custom Controller** | Vòng lặp điều khiển theo dõi Custom Resource và liên tục đồng bộ trạng thái thực tế về trạng thái mong muốn |
| **Operator** | Kết hợp **CRD + Custom Controller** (chạy trong Pod giao tiếp với API Server) để **đóng gói, triển khai và tự động quản lý toàn bộ vòng đời ứng dụng gốc Kubernetes** (backup, upgrade, failover theo thời gian thực) |
| **Operator Framework (3 thành phần)** | Bộ công cụ mã nguồn mở gồm: **Operator SDK** (xây dựng & kiểm thử Operator), **Operator Lifecycle Manager — OLM** (cài đặt, nâng cấp, quản lý vòng đời Operator trên cluster), và **Operator Metering** (đo lường sử dụng tài nguyên) — phân phối qua **OperatorHub.io** |

## 4. Service Mesh & Istio cho kiến trúc Microservices

- **Service Mesh là gì?** Là một tầng hạ tầng chuyên biệt nằm tách biệt khỏi mã nguồn ứng dụng, giúp giao tiếp giữa các dịch vụ (service-to-service) trở nên tin cậy và an toàn với **3 chức năng cốt lõi**:
  1. **Traffic Management:** Kiểm soát định tuyến lưu lượng (Canary, A/B testing, retry, timeout, **Circuit Breaking** chống lỗi lan truyền).
  2. **Security:** Mã hóa giao tiếp giữa các dịch vụ (mutual TLS — mTLS), xác thực và phân quyền.
  3. **Observability:** Thu thập nhật ký, phân tích dấu vết (tracing) và số liệu giám sát.
- **Kiến trúc Istio (Control Plane vs. Data Plane):**
  - **Data Plane:** Chịu trách nhiệm trực tiếp **xử lý toàn bộ giao tiếp mạng giữa các dịch vụ** thông qua các **Envoy Sidecar Proxy** được tiêm vào từng Pod.
  - **Control Plane (`istiod`):** Quản lý cấu hình, chứng chỉ bảo mật và tự động lập trình/cập nhật cho toàn bộ các proxy ở Data Plane.
- **4 trụ cột Istio hỗ trợ:** **Connect** (kết nối & định tuyến), **Secure** (bảo mật), **Control / Enforce** (thực thi chính sách), **Observe** (giám sát).
- **4 chỉ số giám sát giao tiếp cơ bản (Golden Signals trong Istio):** **Latency** (độ trễ), **Traffic** (lưu lượng), **Errors** (tỉ lệ lỗi), và **Saturation** (độ bão hòa tài nguyên).

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Red Hat OpenShift** xây dựng cho chiến lược **Open Hybrid Cloud**, bổ sung S2I Builds, ImageStreams, Jenkins CI/CD, bảo mật mặc định và `oc` CLI trên nền Kubernetes.
- **3 Build Triggers trong OpenShift:** Webhook, Image Change, Configuration Change.
- **Operators** dùng **CRDs + Custom Controllers** để đóng gói, triển khai và tự động vận hành ứng dụng phức tạp trên Kubernetes.
- Trong **Istio**, **Data Plane (Envoy proxies)** trực tiếp xử lý giao tiếp giữa các service; Service Mesh cung cấp **Traffic Management, Security, Observability** cùng 4 chỉ số vàng: **Latency, Traffic, Errors, Saturation**.
