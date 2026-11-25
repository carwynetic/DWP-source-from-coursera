# Module 5: CI/CD, Containerize & Deploy to Kubernetes

> **Tư tưởng cốt lõi:** Đưa ứng dụng Full-Stack từ máy phát triển lên chuẩn vận hành sản xuất đa đám mây (tránh **vendor lock-in**): thiết lập **Continuous Integration (GitHub Actions Linting)** để đảm bảo chất lượng mã nguồn liên tục, **Containerize** bằng `Dockerfile` (cùng MongoDB/Express container và Sentiment Analyzer trên Code Engine), và triển khai điều phối trên **Kubernetes** qua `deployment.yaml`.

## 1. Continuous Integration (CI) với GitHub Actions Linting

- **Tại sao cần CI/CD?**
  - **Continuous Integration (CI):** Tự động kiểm tra, lint và test mỗi khi thành viên push code hoặc mở Pull Request, phát hiện lỗi sớm trước khi gộp vào `main`.
  - **Continuous Delivery (CD):** Tự động đóng gói và phát hành bản cập nhật tới người dùng mà không gây gián đoạn.
- **Workflow Linting chuẩn trong `.github/workflows/main.yml`:**
  - **Job 1 — Python Linting (`flake8`):** Quét toàn bộ mã nguồn Django (`server/`) kiểm tra chuẩn PEP 8 (lỗi thụt dòng, dòng quá dài >79 ký tự, biến/import thừa không dùng).
  - **Job 2 — JavaScript Linting (`jshint`):** Quét mã Express/Node.js (`server/database/`) kiểm tra lỗi cú pháp, thiếu dấu `;`, biến chưa khai báo.
- **Quy trình xử lý khi CI báo đỏ (Failed):** Mở tab **Actions** trên GitHub → đọc từng dòng log lỗi file/line cụ thể → sửa triệt để trong mã nguồn → commit & push lại cho đến khi cả hai job đều **xanh (Passed)**.

## 2. Containerizing Ứng dụng & Tránh Vendor Lock-In

Dù **IBM Cloud Code Engine** rất tiện lợi cho Serverless, không phải nhà cung cấp Cloud nào cũng có dịch vụ Code Engine giống hệt nhau. **Containerization (Docker) + Kubernetes** là giải pháp chuẩn mở giúp ứng dụng chạy linh hoạt trên mọi nền tảng Multi-Cloud / Hybrid Cloud.

### Cấu trúc các Container thành phần trong hệ thống

| Thành phần | Cách đóng gói & Chạy |
| --- | --- |
| **MongoDB + Express API** | Chạy bằng Docker / `docker-compose` (cùng container MongoDB lưu dữ liệu đại lý & đánh giá) |
| **Flask + NLTK Sentiment Analyzer** | Triển khai Serverless dưới dạng Application trên **IBM Cloud Code Engine** (phơi bày HTTPS endpoint) |
| **Main Django + React App** | Đóng gói bằng `server/Dockerfile` (chứa React build + Python Django + Gunicorn/entrypoint), đẩy image lên Container Registry và triển khai lên **Kubernetes** |

### Mẫu `Dockerfile` & `deployment.yaml` triển khai Kubernetes

```dockerfile
FROM python:3.12.0-slim-bookworm
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app
WORKDIR $APP

COPY requirements.txt $APP
RUN pip3 install -r requirements.txt
COPY . $APP

EXPOSE 8000
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
```

```bash
# 1. Build và kiểm thử container cục bộ trước khi đẩy lên Kubernetes
docker build -t us.icr.io/$MY_NAMESPACE/dealership:latest .
docker run -p 8000:8000 us.icr.io/$MY_NAMESPACE/dealership:latest

# 2. Đẩy image lên IBM Cloud Container Registry
docker push us.icr.io/$MY_NAMESPACE/dealership:latest

# 3. Triển khai Deployment & Service lên cụm Kubernetes
kubectl apply -f deployment.yaml
kubectl get pods
kubectl get services

# 4. Kiểm thử End-to-End trên cụm Kubernetes (port-forward hoặc Ingress/LoadBalancer URL)
kubectl port-forward deployment.apps/dealership 8000:8000
```

## 3. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Lỗi `entrypoint.sh` không có quyền thực thi hoặc sai ký tự xuống dòng Windows (`CRLF`):** Quên `chmod +x /app/entrypoint.sh` hoặc để định dạng `CRLF` sẽ làm Pod rơi vào trạng thái `CrashLoopBackOff` với lỗi `no such file or directory`.
2. **Đẩy image lên Registry nhưng quên sửa tên image trong `deployment.yaml`:** Kubernetes sẽ cố kéo image mẫu không tồn tại và báo `ErrImagePull` / `ImagePullBackOff`.
3. **Không chạy lại `flake8` cục bộ trước khi push:** Làm lịch sử commit bị rác bởi hàng loạt commit nhỏ kiểu `"fix lint"`; hãy cài và chạy `flake8` cục bộ trước khi push.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- **GitHub Actions** tự động hóa CI Linting (`flake8` cho Python, `jshint` cho JavaScript) ngay mỗi lần push code.
- **Docker + Kubernetes** giải quyết bài toán **portability & multi-cloud**, tránh phụ thuộc độc quyền vào một nhà cung cấp đám mây.
- Luôn kiểm thử end-to-end đầy đủ sau khi triển khai Kubernetes: trang tĩnh, đăng ký/đăng nhập, lọc đại lý theo bang, xem đánh giá kèm phân tích cảm xúc và đăng đánh giá mới.
