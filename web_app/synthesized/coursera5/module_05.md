# Module 5: Final Assignment — Containerize, Scale & Rollout Guestbook on Kubernetes

> **Tư tưởng cốt lõi:** Thực hành trọn vẹn chu trình Cloud-Native thực chiến từ đóng gói ứng dụng **Guestbook** bằng Docker, đẩy image lên IBM Cloud Container Registry, triển khai lên Kubernetes bằng Deployment & Service, kích hoạt **Horizontal Pod Autoscaler (HPA)** chịu tải, cho đến thực hiện **Rolling Update** và **Rollback** không gián đoạn.

## 1. Kiến trúc & Quy trình End-to-End của Final Project (Guestbook App)

Dự án cuối khóa đưa ứng dụng web Guestbook (cho phép người dùng nhập và lưu lời nhắn) đi qua 5 giai đoạn cốt lõi của toàn bộ Khóa 5:

```text
[1. Source Code + Dockerfile]
        │  docker build . -t us.icr.io/$MY_NAMESPACE/guestbook:v1
        ▼
[2. IBM Cloud Container Registry (ICR)]
        │  docker push us.icr.io/$MY_NAMESPACE/guestbook:v1
        ▼
[3. Kubernetes Deployment & Service]
        │  kubectl apply -f deployment.yml  (Pods + ReplicaSet + Service)
        ▼
[4. Horizontal Pod Autoscaler (HPA)]
        │  kubectl autoscale deployment guestbook --cpu-percent=5 --min=1 --max=10
        │  (Giả lập tải bằng vòng lặp curl -> quan sát Pod tự scale tăng lên)
        ▼
[5. Rolling Update (v1 -> v2) & Rollback (v2 -> v1)]
           kubectl set image / kubectl apply -> kubectl rollout undo deployment/guestbook
```

## 2. Bộ lệnh thực chiến kiểm tra từng hạng mục chấm điểm

| Giai đoạn | Lệnh CLI trọng tâm | Kết quả kỳ vọng cần kiểm chứng |
| --- | --- | --- |
| **1. Build & Push Image** | `docker build . -t us.icr.io/$MY_NAMESPACE/guestbook:v1`<br>`docker push us.icr.io/$MY_NAMESPACE/guestbook:v1`<br>`ibmcloud cr images` | Image `guestbook:v1` xuất hiện trong IBM Cloud Container Registry |
| **2. Deploy lên Kubernetes** | `kubectl apply -f deployment.yml`<br>`kubectl get deployments -o wide`<br>`kubectl get pods` | Deployment đạt trạng thái `READY` (vd `1/1` hoặc `3/3`), Pod `Running` |
| **3. Kích hoạt HPA & Load Test** | `kubectl autoscale deployment guestbook --cpu-percent=5 --min=1 --max=10`<br>`kubectl get hpa` | Khi chạy vòng lặp gọi HTTP tăng tải CPU vượt 5%, số lượng `REPLICAS` tự động tăng lên (≤ 10) và tự giảm khi hết tải |
| **4. Rolling Update lên `v2`** | Chỉnh giao diện (vd đổi tiêu đề Guestbook v2), build & push `:v2`, cập nhật Deployment và chạy `kubectl rollout status deployment/guestbook` | Pod mới chạy song song, thay thế dần Pod cũ mà ứng dụng không bị ngắt kết nối |
| **5. Rollback về `v1`** | `kubectl rollout history deployment/guestbook`<br>`kubectl rollout undo deployment/guestbook` | Ứng dụng lập tức quay lại phiên bản `v1` ổn định trước đó |

## 3. Bẫy thường gặp khi làm Final Assignment

1. **Quên định nghĩa `resources.requests.cpu` trong `deployment.yml`:** Nếu Deployment không khai báo mức CPU request, **HPA sẽ hiện `<unknown>/5%` và KHÔNG thể tự động scale Pod**!
2. **Quên đăng nhập Container Registry trước khi push:** Luôn chạy `ibmcloud cr region-set` và `ibmcloud cr login` trước khi `docker push`.
3. **Trùng tag `:v1` khi cập nhật phiên bản mới:** Nếu sửa code nhưng vẫn build đè tag `:v1` mà `imagePullPolicy` không đặt `Always`, Kubernetes sẽ không nhận biết có bản mới để Rolling Update. Luôn tăng tag rõ ràng (`:v1` → `:v2`).

## 4. Liên kết lộ trình sang Khóa 6 & Khóa 7

Nắm vững Docker, Kubernetes, OpenShift và Istio ở Khóa 5 là bàn đạp trực tiếp cho **Khóa 6 (Microservices & Serverless với REST/GraphQL và IBM Cloud Code Engine)** và bước triển khai CI/CD + Kubernetes cuối cùng của **Khóa 7 (Full-Stack Capstone Project)**.
