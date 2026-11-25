# Module 3: Managing Applications with Kubernetes

> **Tư tưởng cốt lõi:** Vận hành ứng dụng ổn định trên Kubernetes đòi hỏi kết hợp **ReplicaSet** (duy trì số bản sao chống điểm lỗi đơn), **3 bộ Autoscaler** (HPA, VPA, CA), **Rolling Updates & Rollbacks không gián đoạn**, **ConfigMaps/Secrets** tách biệt cấu hình khỏi mã nguồn, và **Service Binding** kết nối an toàn tới dịch vụ Cloud bên ngoài.

## 1. ReplicaSet & 3 loại Autoscaling trong Kubernetes

- **ReplicaSet:** Đối tượng Kubernetes chịu trách nhiệm **tạo thêm hoặc xóa bớt Pod** để luôn giữ trạng thái thực tế khớp chính xác với số lượng `replicas` mong muốn — giúp cân bằng tải, loại bỏ Single Point of Failure (SPOF) và đảm bảo tính sẵn sàng cao (High Availability). Có thể tạo trực tiếp từ tệp cấu hình YAML (`kind: ReplicaSet`) bằng `kubectl apply -f replicaset.yaml`, nhưng trong thực tế thường được quản lý gián tiếp thông qua **Deployment**.
- **3 loại Kubernetes Autoscaler (tự động mở rộng theo 2 tầng: Pod level & Cluster/Node level):**

| Loại Autoscaler | Viết tắt | Tầng hoạt động | Cơ chế mở rộng |
| --- | :---: | --- | --- |
| **Horizontal Pod Autoscaler** | **HPA** | Pod level | Tự động **tăng/giảm số lượng Pod replicas** dựa trên mức sử dụng CPU hoặc custom metrics |
| **Vertical Pod Autoscaler** | **VPA** | Pod level | Tự động **tăng/giảm tài nguyên (CPU/RAM)** cấp phát cho từng Pod/máy hiện có |
| **Cluster Autoscaler** | **CA** | **Cluster / Node level** | Tự động **thêm hoặc gỡ bỏ các Worker Node** trong toàn cluster khi Pod thiếu chỗ hoặc node dư thừa |

## 2. Các chiến lược Triển khai (Deployment Strategies), Rolling Updates & Rollback

6 chiến lược triển khai phổ biến trong Kubernetes: **Recreate** (tắt cũ rồi bật mới — có downtime), **Rolling** (thay thế dần từng Pod), **Blue/Green** (chạy song song 2 môi trường rồi chuyển traffic tức thì), **Canary** (chuyển dần một phần nhỏ người dùng thật sang bản mới để kiểm nghiệm), **A/B Testing** (đánh giá 2 phiên bản tính năng), và **Shadow** (nhân bản traffic thật sang bản mới mà không ảnh hưởng phản hồi người dùng).

### Chuẩn bị và thực thi Rolling Update không gián đoạn (100% Availability)

- **Bước chuẩn bị bắt buộc trước khi bật Rolling Update:**
  1. Bổ sung **Liveness Probe** (kiểm tra container còn sống không để tự restart) và **Readiness Probe** (kiểm tra container đã sẵn sàng nhận traffic chưa) vào Deployment.
  2. Cấu hình chiến lược `strategy.type: RollingUpdate` kèm `maxUnavailable` và `maxSurge`.
- **Chiến lược cập nhật đảm bảo 100% Availability:** Thay thế từng phần (one-at-a-time / rolling với `maxUnavailable: 0` và `maxSurge >= 1`) hoặc Blue/Green — luôn đảm bảo có Pod sẵn sàng phục vụ suốt quá trình nâng cấp (ngược lại với Recreate / all-at-once gây gián đoạn).
- **Lệnh cập nhật & hoàn tác (Rollback) khi bản mới gặp sự cố:**

```bash
# Cập nhật image của deployment sang phiên bản mới
kubectl set image deployment/my-app my-container=my-repo/my-app:v2

# Kiểm tra lịch sử và trạng thái rollout
kubectl rollout status deployment/my-app
kubectl rollout history deployment/my-app

# Hoàn tác (Rollback) tức thì về phiên bản ổn định trước đó
kubectl rollout undo deployment/my-app

# Khởi động lại toàn bộ container của deployment
kubectl rollout restart deployment/my-app
```

## 3. Quản lý Cấu hình & Bảo mật: ConfigMaps vs. Secrets

Nguyên tắc vàng Cloud-Native: **Không bao giờ hard-code cấu hình hay mật khẩu trong mã nguồn hoặc Docker Image.**

| Tiêu chí | `ConfigMap` | `Secret` |
| --- | --- | --- |
| **Loại dữ liệu** | Dữ liệu **không nhạy cảm** (non-confidential) dạng cặp `key: value` (URL, cổng, cờ tính năng) | Thông tin **nhạy cảm** (mật khẩu, OAuth token, API key, SSH key — mã hóa base64/encryption at rest) |
| **3 cách tạo chuẩn** | 1. Từ **literal values** (`--from-literal`)<br>2. Từ **file cấu hình** (`--from-file`)<br>3. Từ **thư mục** hoặc file **manifest YAML** (`kubectl apply -f`) | 1. Từ **literal values** (`--from-literal`)<br>2. Từ **file** (`--from-file`)<br>3. Từ **manifest YAML** (`kind: Secret`, giá trị base64) |
| **Cách Pod tiêu thụ** | Biến môi trường (`env` / `envFrom`), tham số dòng lệnh, hoặc mount thành file qua Volume | Tương tự ConfigMap (biến môi trường hoặc mount volume trong bộ nhớ `tmpfs`) |

> **Lưu ý giới hạn ConfigMap:** ConfigMap **không cung cấp mã hóa hay bảo mật** và có giới hạn kích thước tối đa **1 MiB** — không dùng để lưu dữ liệu lớn hay mật khẩu!

## 4. Service Binding — Kết nối dịch vụ Cloud ngoài vào Cluster

- **Service Binding là gì?** Là quy trình kết nối ứng dụng trong Kubernetes Cluster với các **backing services bên ngoài** (REST API, cơ sở dữ liệu, event bus, dịch vụ AI như IBM Tone Analyzer) sao cho thông tin cấu hình và thông tin xác thực (**credentials**) được tự động tiêm vào ứng dụng một cách an toàn qua Kubernetes Secret mà không cần chép tay mật khẩu vào code.
- **3 bước chuẩn để bind dịch vụ IBM Cloud Service vào Cluster:**
  1. **Tạo (Provision) thực thể dịch vụ** trên IBM Cloud Catalog.
  2. **Bind dịch vụ vào Kubernetes Cluster** (`ibmcloud ks cluster service bind ...`) — thao tác này tự động tạo một **Kubernetes Secret** chứa API key & endpoint URL trong namespace mục tiêu.
  3. **Tham chiếu Secret đó trong Deployment YAML** (mount thành file hoặc biến môi trường) để mã ứng dụng đọc thông tin kết nối.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Lưu mật khẩu/API key trong `ConfigMap`:** ConfigMap lưu dạng văn bản thuần (plaintext) không mã hóa — luôn dùng **`Secret`** cho mọi thông tin nhạy cảm.
2. **Thực hiện Rolling Update nhưng quên khai báo `readinessProbe`:** Kubernetes sẽ chuyển traffic vào Pod mới ngay khi tiến trình vừa khởi động dù ứng dụng bên trong chưa nạp xong, gây lỗi 502/503 cho người dùng.
3. **Nhầm HPA, VPA và CA:** HPA mở rộng **số lượng Pod**; VPA mở rộng **CPU/RAM của Pod**; **Cluster Autoscaler (CA)** mở rộng **số lượng Worker Node trong Cluster**.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **ReplicaSet** thêm/xóa Pod để đảm bảo scaling và dự phòng (redundancy).
- **HPA** (số Pod), **VPA** (tài nguyên Pod), **CA** (số Node của Cluster).
- Hoàn tác phiên bản lỗi bằng lệnh **`kubectl rollout undo`**; chuẩn bị Rolling Update bằng **Liveness Probe** và **Readiness Probe**.
- **ConfigMap** cho cấu hình thường; **Secret** cho thông tin nhạy cảm; **Service Binding** tự động cấp credentials dịch vụ ngoài cho ứng dụng một cách bảo mật.
