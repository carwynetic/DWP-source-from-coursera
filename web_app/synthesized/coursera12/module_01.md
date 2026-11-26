# Module 1: Review and Exam Preparation — Tổng ôn Kiến trúc Full-Stack

> **Tư tưởng cốt lõi:** Lập trình viên Full-Stack Cloud-Native kết hợp đồng bộ ba tầng: giao diện tương tác phía Client (HTML5/CSS3/JS/React), dịch vụ xử lý nghiệp vụ & dữ liệu phía Server (Node.js/Express, Python/Flask/Django, SQL/ORM), và hạ tầng triển khai linh hoạt trên Cloud (Docker, Kubernetes, OpenShift, Microservices & Serverless) dưới sự quản lý mã nguồn của Git/GitHub.

## 1. Nền tảng Cloud Computing: Mô hình, Hạ tầng & Bảo mật

Điện toán đám mây cung cấp tài nguyên tính toán theo nhu cầu (**on-demand**) qua Internet theo mô hình trả tiền theo mức sử dụng (**pay-as-you-go**), dựa trên 5 đặc tính cốt lõi (NIST): *On-demand self-service*, *Broad network access*, *Resource pooling*, *Rapid elasticity*, và *Measured service*.

### A. Service Models & Deployment Models

| Phân loại | Mô hình | Trách nhiệm quản lý & Đặc điểm cốt lõi |
| --- | --- | --- |
| **Service Model** | **IaaS** (*Infrastructure as a Service*) | Nhà cung cấp quản lý hạ tầng vật lý (Data Center, Compute, Network, Storage); người dùng tự quản lý OS, runtime và ứng dụng. |
| **Service Model** | **PaaS** (*Platform as a Service*) | Nhà cung cấp quản lý thêm nền tảng (OS, middleware, runtime); giúp tăng tốc độ ra thị trường (*faster time to market*). |
| **Service Model** | **SaaS** (*Software as a Service*) | Nhà cung cấp host và quản lý toàn bộ ứng dụng & dữ liệu theo kiến trúc đa người thuê (*multitenant*), trả phí thuê bao (*subscription*). |
| **Deployment** | **Public Cloud** | Hạ tầng thuộc sở hữu & vận hành bởi Cloud Provider (AWS, IBM, Azure, GCP), chia sẻ tài nguyên ảo hóa cho nhiều tổ chức. |
| **Deployment** | **Private Cloud** | Hạ tầng cấp phát **độc quyền cho một tổ chức duy nhất** (đặt *on-premises* hoặc *VPC* riêng trên public cloud). |
| **Deployment** | **Hybrid Cloud** | Kết nối liền mạch Private Cloud nội bộ và Public Cloud thành một hạ tầng thống nhất; **Hybrid Multi-Cloud** mở rộng tích hợp nhiều nhà cung cấp Public Cloud khác nhau. |
| **Deployment** | **Community Cloud** | Hạ tầng dùng chung cho một nhóm tổ chức có chung mối quan tâm (bảo mật, tuân thủ pháp lý, ngành dọc). |

### B. Ảo hóa, Lưu trữ Đám mây & Bảo mật

- **Virtualization & Hypervisors:** **Hypervisor** là lớp phần mềm cho phép tạo phiên bản ảo hóa của phần cứng vật lý (các loại VM gồm *Shared/Public VMs*, *Transient/Spot VMs*, *Reserved VMs*, *Dedicated Hosts*). Khác với VM cần cả hệ điều hành khách (Guest OS), **Container** đóng gói code + thư viện + dependencies thành đơn vị thực thi gọn nhẹ dùng chung nhân OS của host. **Bare Metal Servers** là máy chủ vật lý đơn người thuê (*single-tenant*) cho tải HPC và yêu cầu bảo mật/tuân thủ cao.
- **4 loại Cloud Storage & CDN:**

| Loại Storage | Cách truy cập & Kết nối | Tốc độ & Đặc trưng |
| --- | --- | --- |
| **Direct Attached (Local)** | Gắn trực tiếp trên chassis/rack của host server | Tốc độ cao, gắn liền vòng đời máy chủ vật lý |
| **File Storage** | Giao thức **NFS** qua mạng Ethernet chuẩn | Chia sẻ thư mục/file cho nhiều compute node |
| **Block Storage** | Kết nối **cáp quang tốc độ cao (high-speed fiber)**, gắn theo volume | Hiệu năng I/O cao, phù hợp database & hệ điều hành |
| **Object Storage** | Truy cập qua **API** (REST/HTTP), không cần compute node bên dưới | Dung lượng gần như vô hạn, trả theo dung lượng dùng, đọc/ghi chậm nhất |

- **CDN (Content Delivery Network):** Mạng máy chủ phân tán địa lý lưu bản sao tạm (cache) nội dung tĩnh/media gần người dùng nhất để giảm độ trễ.
- **Cloud Security (Shared Responsibility):** Bảo mật là trách nhiệm chung giữa Cloud Provider và tổ chức sử dụng. Trụ cột gồm **IAM** (*Identity and Access Management* — xác thực, phân quyền qua Access Groups & Policies), giám sát chủ động (*active monitoring*), và **Cloud Encryption** bảo vệ dữ liệu ở **3 trạng thái**: *Encryption at rest* (lưu trữ), *Encryption in transit* (truyền tải), và *Encryption in use* (xử lý trong bộ nhớ).

## 2. Front-End, Git/GitHub & Hệ sinh thái React/Redux

### A. HTML5, CSS3, JavaScript & Bootstrap

- **HTML5 Semantic Elements:** Thay vì lạm dụng `<div>`, dùng `<section>` để chia các phần logic có chủ đề/chương mục rõ ràng (như các chương đánh số của tài liệu hướng dẫn), `<article>` cho nội dung độc lập, `<nav>` cho thanh điều hướng, `<header>` / `<footer>` cho đầu/chân trang.
- **CSS & Bootstrap Containers:** CSS tạo giao diện đồng nhất và tách biệt thiết kế khỏi dữ liệu. Trong **Bootstrap**, có 2 loại container: `.container` (chiều rộng cố định đáp ứng theo breakpoint) và `.container-fluid` (**trải dài toàn bộ chiều rộng 100% của phần tử cha / viewport**).
- **JavaScript cốt lõi & ES6:**
  - Khai báo biến toàn cục cổ điển dùng `var` (function/global scope), trong khi ES6 bổ sung `let`, `const` (block scope), *arrow functions*, *promises*, và *classes*.
  - Toán tử `typeof x` trả về chuỗi mô tả **kiểu dữ liệu của toán hạng** được truyền vào (`"number"`, `"string"`, `"object"`, `"undefined"`...).
  - **Route:** Đường dẫn tới một trang hoặc điểm cuối mà người dùng/client tương tác.

### B. Git & GitHub Workflow

| Khái niệm / Lệnh | Vai trò & Cơ chế hoạt động |
| --- | --- |
| **DVCS (Git)** | Hệ thống quản lý phiên bản phân tán theo dõi lịch sử thay đổi mã nguồn (*source code tracking*), cho phép nhiều người làm việc trên các nhánh (*branch*) song song. |
| **Pull Request (PR)** | Cơ chế trên GitHub đề xuất thay đổi từ một nhánh/fork để đồng đội **review và merge** vào nhánh chính. |
| `git fetch` vs. `git pull` | `git fetch` chỉ tải thay đổi từ remote về local (không tự merge); `git pull` tải thay đổi từ remote về local **và tự động merge** vào nhánh hiện tại. |
| **Vai trò trong dự án Git lớn** | *Developer* (viết code), *Integrator* (quản lý & tích hợp thay đổi), *Repository Administrator* (cấu hình quyền truy cập, vận hành lệnh phía server như `git-http-backend`). |

### C. React & Redux

- **React:** Thư viện UI viết bằng **JavaScript**, dùng **JSX** để kết hợp cú pháp giống HTML ngay trong JS và nhận thông báo lỗi rõ ràng. Hỗ trợ 4 loại component: *Functional*, *Class*, *Pure*, và *Higher-Order Components (HOC)*.
- **Vòng đời tạo mới (Mounting) của Class Component** theo đúng thứ tự thực thi:
  `constructor()` $\rightarrow$ `getDerivedStateFromProps()` $\rightarrow$ `render()` $\rightarrow$ `componentDidMount()`
- **Quy tắc Hooks (Rules of Hooks):** Chỉ được gọi Hooks **ở cấp cao nhất (top level) của React function component** hoặc custom hook — tuyệt đối không gọi bên trong `if`, vòng lặp, hay hàm lồng nhau.
- **Redux:** Thư viện quản lý trạng thái tập trung, **tối ưu hiệu năng cho ứng dụng lớn** với luồng dữ liệu một chiều (*unidirectional data flow*). **3 thành phần Redux trực tiếp tham gia cập nhật thuộc tính/state** là: **Actions** (mô tả sự kiện), **Reducer** (hàm thuần tính toán state mới), và **Center Store** (kho lưu trữ state duy nhất). Dữ liệu bất đồng bộ được xử lý qua **Middleware**.

## 3. Back-End: Node.js/Express, Python, SQL & Django

### A. Node.js & Express

```javascript
// CommonJS (require): gọi ở mọi nơi, liên kết động, đồng bộ; trả về object đại diện module
const express = require("express");
const app = express();

// 5 loại Middleware trong Express: Application-level, Router-level, Error-handling, Built-in, Third-party
app.use(express.json()); // Built-in middleware

app.get("/api/health", (req, res) => {
  res.json({ status: "ok" });
});

// Error-handling middleware luôn có đủ 4 tham số (err, req, res, next)
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});
```

- **`require` vs `import`:** `require()` gọi được bất kỳ đâu trong file, liên kết động (*dynamically bound*) và đồng bộ (*synchronous*), trả về **một JavaScript object đại diện cho instance của module** (`module.exports`). Ngược lại, `import` phải đặt ở đầu file, liên kết tĩnh (*statically bound*) và bất đồng bộ.
- **Promise & JSON:** **Promise** là một **đối tượng được trả về bởi một phương thức bất đồng bộ** (đại diện cho kết quả hoàn thành hoặc thất bại trong tương lai). **JSON** (*JavaScript Object Notation*) trao đổi dữ liệu qua `JSON.parse()` và `JSON.stringify()`.
- **Express:** Framework web cho Node.js hỗ trợ routing, middleware, cơ chế debug tìm lỗi nhanh và xử lý bất đồng bộ đồng thời nhiều request; xác thực JWT dùng gói `jsonwebtoken`.

### B. Python, File I/O, Web Scraping & Cơ sở dữ liệu

```python
# 1. Python Class & Object
class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("x=", self.x, " y=", self.y)

p1 = Points("Q", "Z")
p1.print_point()  # Output: x= Q  y= Z (coursera quiz chuẩn hóa: x=Q y=Z)

# 2. List Indexing dương & âm
myList = ["John", "Ralph", "Leia", "Simone"]
print(myList[2])   # "Leia"
print(myList[-2])  # "Leia"

# 3. File mode 'a+': Đọc và ghi nối thêm vào cuối file; tự tạo file mới nếu chưa tồn tại
with open("log.txt", "a+") as f:
    f.write("New entry\n")

# 4. BeautifulSoup: In cấu trúc HTML lồng nhau đẹp mắt
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html><body><p>Hi</p></body></html>", "html.parser")
print(soup.prettify())
```

- **Entity-Attribute Model & Cursor:** Trong mô hình ER, đối tượng thực thể độc lập (như *Movie*) là một **Entity** (ánh xạ thành Table), đặc tính của nó là **Attribute** (ánh xạ thành Column). **Cursor** là cấu trúc dữ liệu điều khiển đặc biệt dùng để duyệt qua từng dòng (*iterate over rows*) trong kết quả truy vấn database.
- **Django Framework (MVT — Model-View-Template):**
  - **Django Project:** Một Python package chứa toàn bộ file cấu hình (`settings.py`, `urls.py`, `manage.py`) cho một instance ứng dụng Django.
  - **Django Template:** Kết hợp **các phần tử HTML tĩnh** với **thẻ/biến Python đặc biệt** để sinh trang web động.
  - **Django ORM:** Cầu nối giữa OOP và SQL; gọi `.save()` để chèn/cập nhật bản ghi, dùng Manager & QuerySet để đọc, `.delete()` để xóa. Triển khai production qua chuẩn **WSGI** hoặc **ASGI**.

## 4. Containers, Kubernetes, OpenShift, Microservices & Serverless

- **Docker Architecture & CLI:** Gồm Docker Client, Docker Host (Dockerfile, Images, Containers, Networks, Volumes) và Container Registry. **Dockerfile** là tập tin văn bản chứa các chỉ thị từng bước để build container image.
  - `docker build`: tạo image từ Dockerfile; `docker run`: tạo và chạy container từ image; `docker tag`, `docker images`, `docker push`, `docker pull`.
- **Kubernetes (K8s) Orchestration:** Tự động hóa triển khai, **scaling & load balancing**, **health checks & self-healing**, và **redundancy/high availability** giảm thiểu downtime.
  - **Control Plane:** API Server, `etcd`, Scheduler, Controller Manager. **Worker Plane:** Nodes, `kubelet`, Container Runtime, `kube-proxy`.
  - **`kubectl apply -f <file|dir>`:** Lệnh **khai báo (declarative)**, yêu cầu đầu vào là file hoặc thư mục chứa manifest YAML/JSON, tự động suy luận tạo Deployment/tài nguyên mới nếu chưa tồn tại (hoặc cập nhật nếu đã có).
  - **Services:** `ClusterIP` (nội bộ cluster), `NodePort` (mở port trên node), `LoadBalancer` (tạo bộ cân bằng tải ngoài), `ExternalName`.
- **Red Hat OpenShift & Istio:** **OpenShift** là nền tảng Kubernetes cấp doanh nghiệp sẵn sàng cho **Hybrid Cloud** (*enterprise-ready Kubernetes container platform*), bổ sung CI/CD (Jenkins), ImageStream, Build, Operators/CRDs. **Istio** là **Service Mesh** cung cấp quản lý traffic, bảo mật (mTLS), thực thi chính sách và quan sát (*observability*: latency, traffic, errors, saturation).
- **Microservices & 12-Factor App:** Chia nhỏ ứng dụng thành các dịch vụ ghép nối lỏng lẻo, giao tiếp qua **REST API** (HTTP `GET/POST/PUT/DELETE`, tài liệu hóa bằng OpenAPI/Swagger) thông qua **API Gateway** (vd: **Apigee** do Google quản lý). Thường áp dụng kèm phương pháp luận **Twelve-Factor App** để xây dựng ứng dụng SaaS hiện đại.
- **Serverless Stack:** Gồm 3 thành phần chính: **FaaS** (*Function as a Service* — AWS Lambda, IBM Cloud Functions), **BaaS** (*Backend as a Service* — Firebase, Auth/DB quản lý sẵn), và **API Gateway**. **IBM Cloud Code Engine** là nền tảng serverless được quản lý hoàn toàn giúp lập trình viên chạy app/build/job mà **không phải tự quản lý Kubernetes cluster**.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm lẫn các thành phần Redux khi cập nhật State/Props:** Chỉ có **Actions**, **Reducer** và **Center Store** là 3 thành phần cốt lõi của Redux tham gia luồng cập nhật state — *UI Components* thuộc tầng React tiêu thụ state từ Store, không phải thành phần xử lý cập nhật bên trong Redux.
2. **Nhầm `git fetch` với `git pull`:** `git fetch` chỉ đồng bộ dữ liệu remote về kho local mà chưa gộp vào nhánh làm việc; chỉ `git pull` mới thực hiện cả tải về lẫn merge tự động.
3. **Nhầm phạm vi của `kubectl apply`:** `kubectl apply` là lệnh *declarative* cần file/thư mục manifest và có thể áp dụng cho cả tài nguyên cấp cluster (không chỉ giới hạn ở *namespace-scoped*).
4. **Phân biệt `open()` mode `'w+'` và `'a+'` trong Python:** `'w+'` cắt cụt (xóa sạch) nội dung file cũ nếu đã tồn tại, còn `'a+'` giữ nguyên dữ liệu cũ để ghi nối tiếp và vẫn cho phép đọc/tạo file mới nếu chưa có.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Cloud & Containers:** Virtualization dùng **Hypervisor**; Container dùng **Docker** (`Dockerfile` $\rightarrow$ `build` $\rightarrow$ `run`); Orchestration dùng **Kubernetes** / **OpenShift** (`kubectl apply` là declarative); Serverless Stack = **FaaS + BaaS + API Gateway**.
- **Front-End & Git:** `<section>` chia chương/phần logic; Bootstrap `.container-fluid` rộng 100% phần tử cha; React Class mount theo thứ tự `constructor` $\rightarrow$ `getDerivedStateFromProps` $\rightarrow$ `render` $\rightarrow$ `componentDidMount`; Hooks luôn gọi ở top-level.
- **Back-End & Data:** Node.js `require()` trả về object đại diện module; Promise là object trả về từ hàm bất đồng bộ; Express có 5 loại middleware; Django Project là package chứa cấu hình, Template trộn HTML tĩnh với code Python.