# Module 2: Kubernetes Basics

> **Tư tưởng cốt lõi:** Khi số lượng container tăng lên hàng trăm đến hàng nghìn, **Kubernetes (K8s)** — hệ thống điều phối container (container orchestration) mã nguồn mở chuẩn công nghiệp — tự động hóa việc triển khai, mở rộng, tự phục hồi (self-healing), đóng gói tài nguyên tối ưu (automated bin packing) và định tuyến mạng theo mô hình khai báo (Declarative YAML/JSON) giữa **Control Plane** và **Worker Nodes**.

## 1. Container Orchestration & Các năng lực cốt lõi của Kubernetes

- **Container Orchestration:** Quá trình tự động hóa toàn bộ vòng đời container (triển khai, nối mạng, cân bằng tải, mở rộng, phục hồi lỗi) trên 3 loại môi trường: **On-premises (Private Cloud)**, **Public Cloud**, và **Hybrid Cloud**.
- **Kubernetes (K8s):** Khởi nguồn từ Google, hiện do **CNCF** duy trì, là công cụ điều phối container phổ biến nhất hiện nay.
- **Các năng lực trọng tâm của Kubernetes:**
  - **Automated Bin Packing:** Tự động xếp đặt container lên các node dựa trên yêu cầu CPU/RAM để tối ưu hóa hiệu suất sử dụng tài nguyên và tiết kiệm chi phí.
  - **Self-Healing:** Tự động khởi động lại container bị lỗi, thay thế và lập lịch lại Pod khi node chết.
  - **Automated Rollouts & Rollbacks:** Cập nhật phiên bản ứng dụng mượt mà và hoàn tác ngay nếu phát hiện lỗi.
  - **Service Discovery & Load Balancing**, **Horizontal Scaling**, **Storage Orchestration**, **Secret & Configuration Management**, **Batch Execution**, **IPv4/IPv6 Dual-Stack**.

## 2. Kiến trúc Kubernetes Cluster: Control Plane vs. Worker Plane

```text
┌─────────────────── CONTROL PLANE (Master Node) ───────────────────┐
│  kube-apiserver  │  etcd (key-value DB)  │  kube-scheduler        │
│  kube-controller-manager  │  cloud-controller-manager             │
└───────────────────────────────┬───────────────────────────────────┘
                                │ (duy trì Desired State = Actual State)
┌─────────────── WORKER NODE 1 ──────────────┐  ┌─── WORKER NODE N ──┐
│  kubelet (agent đảm bảo container chạy)    │  │  kubelet           │
│  kube-proxy (quản lý quy tắc mạng/Service) │  │  kube-proxy        │
│  Container Runtime (containerd / CRI-O)    │  │  Container Runtime │
│  [Pod A]  [Pod B]                          │  │  [Pod C]           │
└────────────────────────────────────────────┘  └────────────────────┘
```

| Tầng | Thành phần | Vai trò chính |
| --- | --- | --- |
| **Control Plane** | **API Server (`kube-apiserver`)** | Cổng giao tiếp trung tâm tiếp nhận mọi yêu cầu REST từ `kubectl` và nội bộ cluster |
| | **`etcd`** | Cơ sở dữ liệu key-value phân tán lưu trữ toàn bộ trạng thái cấu hình cluster |
| | **Scheduler (`kube-scheduler`)** | Chọn Worker Node phù hợp nhất để gán Pod mới dựa trên tài nguyên & ràng buộc |
| | **Controllers** | Các vòng lặp điều khiển (control loops) liên tục đưa **Actual State** khớp với **Desired State** |
| **Worker Node** | **`kubelet`** | Agent chạy trên mỗi Worker Node, **đảm bảo các container trong Pod đang chạy đúng như cấu hình mong muốn** |
| | **`kube-proxy`** | Quản lý quy tắc mạng và chuyển tiếp lưu lượng tới các Pod |
| | **Container Runtime** | Phần mềm trực tiếp chạy container (containerd, CRI-O, Docker Engine) |

## 3. Các đối tượng cốt lõi (Kubernetes Objects) & Labels

Mọi cấu hình Kubernetes được viết bằng **YAML** hoặc **JSON**.

| Đối tượng (Object) | Chức năng & Trường hợp sử dụng |
| --- | --- |
| **Namespace** | Phân tách logic các nhóm tài nguyên trong cùng một cluster (vd: `dev`, `staging`, `prod`) |
| **Pod** | Đơn vị triển khai nhỏ nhất trong K8s — bao bọc 1 (hoặc vài) container dùng chung IP và volume |
| **ReplicaSet** | Duy trì cố định số lượng bản sao (replicas) Pod đang chạy theo cấu hình |
| **Deployment** | Đối tượng chuẩn cho **ứng dụng Stateless** — quản lý ReplicaSet và cung cấp cập nhật cuốn chiếu (rolling update) / rollback |
| **StatefulSet** | Quản lý **ứng dụng Stateful** (như cơ sở dữ liệu) cần danh tính mạng ổn định và lưu trữ bền vững theo thứ tự |
| **DaemonSet** | Đảm bảo **mọi Worker Node** (hoặc nhóm node chọn lọc) đều chạy ít nhất 1 bản sao Pod (vd: log collector, monitoring agent) |
| **Job** | Chạy tác vụ theo lô (batch) một lần cho đến khi hoàn thành thành công |
| **Label** | Cặp `key: value` gắn vào đối tượng K8s để phân loại, tìm kiếm và liên kết (vd Service chọn Pod thông qua `selector` khớp Label) |

## 4. Kết nối mạng: 4 loại Kubernetes Service & Ingress

**Service** là đối tượng REST tạo lớp trừu tượng ổn định (IP cố định + cân bằng tải) phía trước tập Pod (vốn có IP thay đổi mỗi khi khởi tạo lại):

| Loại Service / Routing | Phạm vi & Cơ chế hoạt động |
| --- | --- |
| **`ClusterIP`** *(Mặc định)* | Chỉ cấp IP nội bộ cho **giao tiếp liên dịch vụ bên trong cluster (inter-service communication)** |
| **`NodePort`** | Mở một cổng cố định trên mọi Worker Node và tự động định tuyến yêu cầu ngoài vào `ClusterIP` |
| **`LoadBalancer`** | Tự động cấp bộ cân bằng tải ngoài (External Load Balancer của Cloud Provider), kéo theo tạo sẵn `NodePort` và `ClusterIP` |
| **`ExternalName`** | Ánh xạ Service sang một tên miền DNS bên ngoài (đại diện kho lưu trữ ngoài hoặc kết nối chéo giữa các Namespace) |
| **`Ingress` + `Ingress Controller`** | Quản lý định tuyến HTTP/HTTPS từ bên ngoài vào nhiều Service theo đường dẫn URL/host, hỗ trợ **SSL/TLS termination** và cân bằng tải lớp ứng dụng |

## 5. `kubectl` CLI & Kubernetes Anti-Patterns

- **`kubectl` (Kube Command Line Tool):** Công cụ CLI chính giao tiếp với Kubernetes API Server qua **3 kiểu quản lý**: Imperative commands (`kubectl run`), Imperative object configuration, và **Declarative object configuration** (`kubectl apply -f deploy.yaml` — khuyến nghị cho production).

```bash
kubectl config get-contexts         # Xem context cluster hiện tại
kubectl apply -f deployment.yaml    # Áp dụng cấu hình khai báo (YAML/JSON)
kubectl get pods -o wide            # Xem danh sách Pod kèm IP và Node
kubectl describe pod <pod-name>     # Kiểm tra chi tiết sự kiện & lỗi của Pod
kubectl expose deployment app --type=NodePort --port=8080
```

- **Anti-Pattern kinh điển cần tránh:** **Không nhúng cứng cấu hình (configuration) vào bên trong container image** — một image duy nhất phải chạy được xuyên suốt `dev → staging → prod`, còn cấu hình môi trường phải tách riêng ra `ConfigMap`/`Secret`.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Control Plane** điều phối & duy trì trạng thái mong muốn; **`kubelet`** trên **Worker Node** đảm bảo container chạy đúng như đặc tả.
- Chọn đúng Workload Object: **Deployment** cho ứng dụng **stateless**; **StatefulSet** cho ứng dụng có trạng thái; **DaemonSet** cho agent chạy trên mọi node.
- Nhớ chính xác 4 loại Service: **`ClusterIP`** (nội bộ), **`NodePort`** (cổng trên node), **`LoadBalancer`** (cân bằng tải cloud), **`ExternalName`** (ánh xạ dịch vụ ngoài / chéo namespace).
- File cấu hình Kubernetes viết bằng **YAML** hoặc **JSON**; **Label** là cặp `key-value` gắn thẻ để chọn lọc và gom nhóm tài nguyên.
