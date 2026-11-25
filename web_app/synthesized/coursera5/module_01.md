# Module 1: Containers and Containerization

> **Tư tưởng cốt lõi:** Container đóng gói mã nguồn ứng dụng cùng toàn bộ thư viện và phụ thuộc thành một đơn vị chuẩn hóa, di động và cô lập chạy chia sẻ nhân hệ điều hành; **Docker** chuẩn hóa quy trình *Build → Ship → Run* qua kiến trúc Client–Host–Registry và tập đối tượng cốt lõi (Dockerfile, Image, Container, Network, Volume).

## 1. Container là gì? So sánh Container vs. Máy ảo (Virtual Machine)

- **Container:** Đơn vị phần mềm tiêu chuẩn đóng gói mã nguồn cùng mọi phụ thuộc (runtime, thư viện hệ thống, cấu hình) để ứng dụng chạy đồng nhất từ máy dev đến môi trường production. Giống như **container vận tải biển (shipping containers)** chuẩn hóa kích thước giúp vận chuyển trơn tru qua tàu, xe tải, cần cẩu mà không phụ thuộc hàng hóa bên trong.
- **Đặc tính cốt lõi:** Nhẹ (lightweight), khởi động tính bằng giây, tính di động cao (portable — không bị trói vào một OS/nền tảng cụ thể nhờ cơ chế tương thích container runtime), tận dụng tối đa tài nguyên phần cứng, lý tưởng cho **Microservices** và CI/CD.
- **Công nghệ container phổ biến:** **Docker**, **Podman**, **LXC**, **Vagrant** (quản lý môi trường VM/container).

| Tiêu chí | Container (Docker) | Virtual Machine (VM) |
| --- | --- | --- |
| **Cách ly & Hệ điều hành** | Chia sẻ **OS Kernel** của máy chủ; chỉ cô lập tiến trình & không gian người dùng | Mỗi VM mang theo **một Guest OS đầy đủ** chạy trên Hypervisor |
| **Kích thước & Tốc độ khởi động** | Vài chục MB; khởi động trong tích tắc (mili-giây / giây) | Hàng GB; khởi động mất hàng phút |
| **Ứng dụng phù hợp** | Microservices, ứng dụng stateless, CI/CD, cloud-native | Ứng dụng **monolithic** khổng lồ hoặc workload đòi hỏi cách ly bảo mật/hiệu năng phần cứng tuyệt đối (khi Docker không phải lựa chọn tối ưu nhất) |

## 2. Kiến trúc Docker & Công nghệ nền tảng

### 3 thành phần chính của kiến trúc Client–Server Docker

```text
┌───────────────────┐    REST API     ┌───────────────────────────────────┐     pull/push     ┌──────────────────────┐
│   Docker Client   │ ──────────────> │        Docker Host                │ <───────────────> │  Container Registry  │
│  (docker CLI)     │                 │  - Docker Daemon (dockerd)        │                   │  (Docker Hub,        │
│                   │                 │  - Images, Containers,            │                   │   IBM Cloud CR)      │
│                   │                 │    Networks, Storage Volumes      │                   │                      │
└───────────────────┘                 └───────────────────────────────────┘                   └──────────────────────┘
```

- **Kiến trúc Client–Server** cho phép Docker Client giao tiếp với Docker Daemon cục bộ hoặc điều khiển Docker Host từ xa qua REST API/socket.
- **3 trụ cột công nghệ nền tảng của Docker (Linux kernel features):**
  1. **Namespaces:** Cô lập tiến trình, mạng, hệ thống tệp, người dùng cho từng container.
  2. **Control Groups (cgroups):** Giới hạn và đo lường tài nguyên phần cứng (CPU, RAM, I/O) cấp cho mỗi container.
  3. **Union File System (UnionFS):** Cấu trúc phân lớp (layered filesystem) giúp các image dùng chung các lớp read-only, tiết kiệm dung lượng và tăng tốc build.

## 3. Đối tượng Docker (Docker Objects) & Dockerfile

| Đối tượng | Vai trò & Đặc điểm |
| --- | --- |
| **Dockerfile** | Tệp văn bản chứa các chỉ thị tuần tự (`FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`) để tự động tạo **Container Image** |
| **Docker Image** | Khuôn mẫu bất biến (read-only template) gồm nhiều lớp (layers) dùng để sinh ra container. Định danh chuẩn gồm: **`[registry/][namespace/]repository:tag`** (vd `us.icr.io/my_ns/guestbook:v1`) |
| **Docker Container** | Một **thể hiện đang chạy (runnable instance)** của Image, có thêm một lớp đọc-ghi (read-write layer) trên cùng |
| **Docker Network** | Cô lập và điều phối giao tiếp mạng giữa các container và với thế giới bên ngoài |
| **Volumes & Bind Mounts** | **Lưu trữ dữ liệu bền vững (data persistence)** để dữ liệu không bị mất khi container dừng hoặc bị xóa |
| **Plugins** | Mở rộng tính năng Docker (ví dụ **storage plugins** kết nối hệ thống lưu trữ ngoài) |

### Quy trình tạo và chạy Container (3 bước chuẩn)

```dockerfile
# Bước 1: Viết Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]
```

```bash
# Bước 2: Build image từ Dockerfile và gắn tag
docker build . -t myapp:v1

# Bước 3: Chạy container từ image và ánh xạ cổng (host:container)
docker run -d -p 8080:8080 myapp:v1

# Các lệnh quản lý vòng đời thiết yếu
docker images                      # Liệt kê danh sách images
docker ps                          # Liệt kê containers đang chạy
docker ps -a                       # Liệt kê cả containers đã thoát (exited)
docker stop $(docker ps -q)        # Dừng toàn bộ containers đang chạy
docker container rm <id>           # Xóa container
docker tag myapp:v1 registry/ns/myapp:v1
docker push registry/ns/myapp:v1   # Đẩy image lên Container Registry
```

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Lưu dữ liệu quan trọng trực tiếp trong container mà không gắn Volume/Bind Mount:** Khi container bị xóa (`docker rm`), toàn bộ dữ liệu trên lớp read-write của container sẽ **bốc hơi vĩnh viễn**.
2. **Nhầm `docker run` chỉ dùng để "chạy lại" container cũ:** Thực chất `docker run` **tạo một container hoàn toàn mới từ Image** (nếu máy chưa có image sẽ tự `pull`) và thực thi lệnh khởi chạy bên trong nó.
3. **Nhầm lẫn công dụng của `docker ps` và `docker ps -a`:** Container chạy xong tác vụ ngắn và thoát sẽ không hiện trong `docker ps`; phải dùng `docker ps -a` để kiểm tra.
4. **Dùng container cho mọi bài toán bất kể ngữ cảnh:** Các hệ thống monolithic quá nặng hoặc workload cần cô lập phần cứng/bảo mật cực nghiêm ngặt đôi khi phù hợp với VM hơn container.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- 3 thành phần kiến trúc Docker: **Docker Client**, **Docker Host** (chứa Daemon + Objects), và **Container Registry**.
- 3 công nghệ nền tảng: **Namespaces** (cô lập), **cgroups** (giới hạn tài nguyên), **UnionFS** (hệ thống tệp phân lớp).
- Quy trình cốt lõi: Viết **Dockerfile** → `docker build` tạo **Image** → `docker run` khởi chạy **Container** (kèm **Volume/Bind Mount** nếu cần lưu dữ liệu lâu dài).
