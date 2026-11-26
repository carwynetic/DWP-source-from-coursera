# Module 6: Final Project and Assignment: Modernize DineEase with Cloud

> **Tư tưởng cốt lõi:** Dự án tổng kết **DineEase** minh họa trọn vẹn quy trình kiến trúc một hệ thống đặt đồ ăn từ **Monolith tự quản lý** sang **Cloud-Native Microservices** trên **IBM Cloud** — lựa chọn chính xác từng dịch vụ Compute, Networking, Database, CDN và Monitoring tương ứng với từng yêu cầu phi chức năng (SLA, độ trễ, bảo mật, co giãn, tối ưu đọc/ghi).

## 1. Bối cảnh & 6 Điểm nghẽn của Kiến trúc Monolith cũ (DineEase 1.0)

**DineEase** gồm ứng dụng di động cho khách hàng đặt món, ứng dụng web cho quản trị/nhà hàng và các luồng kết nối đối tác giao hàng + thanh toán POS. Ban đầu hệ thống được xây dựng dưới dạng **Monolith** với 5 module nghiệp vụ chính (**Menu, Pricing, Ordering, Payment, Dispatch**) trên một **Cơ sở dữ liệu quan hệ (RDBMS)** tự quản trị.

| Vấn đề của DineEase Monolith | Hậu quả thực tế khi tăng trưởng | Yêu cầu cho DineEase 2.0 (Cloud-Native) |
| --- | --- | --- |
| **1. Không thể scale độc lập** | Module **Ordering** quá tải vào sự kiện lớn (Super Bowl, Olympic) nhưng không thể scale riêng | Nền tảng serverless tự động theo dõi request và scale up/down tức thì |
| **2. Độ trễ & High Availability** | **Dispatch** cập nhật vị trí/ETA theo thời gian thực nhưng kiến trúc đơn khối khó đạt SLA vùng | Triển khai đa vùng vật lý độc lập trong cùng Region (**SLA 99.99%**) |
| **3. Tải tính toán chuyên biệt** | **Payment & Fraud Check** nặng tính toán, cần cô lập bảo mật cao và xử lý lượng lớn dữ liệu tức thì | Phần cứng vật lý chuyên biệt (**single-tenant**), không ảo hóa, hỗ trợ **GPU** |
| **4. Cần tách thành API services** | **Search, Menu, Pricing** cần stack công nghệ riêng và giao tiếp qua HTTP API cho mobile/đối tác | Container orchestration hỗ trợ đa stack + API Gateway làm lớp giao tiếp trung gian |
| **5. Nghẽn hiệu năng đọc (Read)** | Hiển thị đánh giá/xếp hạng nhà hàng phải `JOIN` nhiều bảng lớn (`Restaurant`, `Review`, `Rating`) gây chậm | **Document-based NoSQL** linh hoạt schema JSON/BSON, tối ưu tốc độ đọc |
| **6. Quản trị Global DB cồng kềnh** | Một RDBMS tự vận hành toàn cầu khó mở rộng dung lượng và thiếu High-Availability Disaster Recovery | Managed RDBMS phân tán theo vùng tích hợp sẵn **HADR** |

## 2. Bản đồ Kiến trúc DineEase 2.0 trên IBM Cloud (9 Quyết định Kỹ thuật)

```text
[Mobile / Web / POS Clients]
        │
        ├──► [Content Delivery Network (CDN)] ──► Ảnh món ăn, logo nhà hàng (giảm độ trễ)
        │
        ▼
[IBM Cloud Load Balancer (VPC/Classic)] ──► Phân phối tải, tăng uptime & fault tolerance
        │
        ▼
[IBM API Connect] ──► API Gateway: định tuyến, tương tác ngoài, bỏ phụ thuộc cứng
        │
        ├──► [IBM Cloud Code Engine] ──────► Ordering Service (Serverless tự scale theo request)
        ├──► [IBM Cloud Kubernetes Service]► Search, Menu, Pricing (Microservices đa tech stack)
        ├──► [IBM Cloud Bare Metal Servers]► Payment & Fraud Checks (Single-tenant, CPU/GPU mạnh)
        │
        ▼ (Dữ liệu & Giám sát — Triển khai trên Multizone Regions - MZR)
        ├──► [IBM Db2 on Cloud] ───────────► Ordering RDBMS quản lý toàn phần + HADR
        ├──► [IBM Cloudant] ───────────────► Reviews & Ratings (NoSQL Document DB tối ưu đọc)
        └──► [IBM Cloud Monitoring] ───────► Giám sát sức khỏe, hiệu năng, cảnh báo, dashboard
```

### Bảng ánh xạ chi tiết 9 Task Kiến trúc trong Dự án DineEase

| Task | Yêu cầu bài toán | Dịch vụ IBM Cloud được chọn | Lý do kiến trúc cốt lõi |
| --- | --- | --- | --- |
| **1. Low Latency & HA (99.99%)** | Dịch vụ **Dispatch** cần độ trễ thấp theo vùng và chống sập khi 1 data center gặp sự cố | **Multizone Regions (MZR)** | MZR gồm 3+ Availability Zones tách biệt vật lý trong cùng Region (khác với *Single campus* dễ chung điểm lỗi) |
| **2. Dedicated Workload** | **Payment & Fraud checks** tính toán nặng, cần bảo mật cô lập tuyệt đối, không qua hypervisor, hỗ trợ GPU | **IBM Cloud Bare Metal Servers** | Truy cập trực tiếp phần cứng vật lý single-tenant, không chia sẻ CPU/RAM, không chịu *hypervisor overhead* |
| **3. Flexible API Microservices** | **Search, Menu, Pricing** dùng tech stack khác nhau, vòng đời build/deploy độc lập, tự phục hồi (*self-healing*) | **IBM Cloud Kubernetes Service (IKS)** | Điều phối containers nhẹ & di động cho từng microservice, tự động scale và tự phục hồi |
| **4. Ordering Scalability** | **Ordering** cần tự theo dõi incoming requests để scale up/down (tới 0 khi rảnh) mà không phải quản lý server | **IBM Cloud Code Engine** | Nền tảng **fully managed serverless** chạy container/code theo nhu cầu HTTP/event |
| **5. API Gateway Layer** | Giao tiếp giữa các dịch vụ API nội bộ với thế giới bên ngoài, **loại bỏ phụ thuộc cứng** (*rigid dependencies*) và định tuyến | **IBM API Connect** | Lớp API Gateway & quản lý vòng đời API hoàn chỉnh (khác với *App Connect* tích hợp ứng dụng hay *Event Streams* Kafka) |
| **6. Optimized Reads (Reviews)** | Đọc nhanh đánh giá/xếp hạng nhà hàng với schema linh hoạt cho dữ liệu phi cấu trúc/lồng nhau, tránh `JOIN` nặng | **IBM Cloudant** | **Document-based NoSQL** (JSON) tối ưu cho tốc độ đọc, scale tức thì và có kiến trúc **offline-first** tích hợp sẵn |
| **7. Managed Relational DB** | CSDL giao dịch cho **Ordering** cần SQL/ACID, nhà cung cấp quản lý toàn phần, hiệu năng doanh nghiệp và **HADR** | **IBM Db2 on Cloud** | Managed RDBMS hỗ trợ OLTP tốc độ cao, tự động mở rộng dung lượng và tích hợp sẵn **HADR** (*High-Availability Disaster Recovery*) |
| **8. Media Distribution** | Phân phối ảnh món ăn, logo nhà hàng tại nhiều node địa lý gần người dùng, giảm tải web server, hỗ trợ nén & cache | **Content Delivery Network (CDN)** | Lưu cache nội dung tĩnh tại các PoP gần người dùng cuối, rút ngắn quãng đường truyền và tối ưu theo thiết bị |
| **9. Traffic Balancing & Health Monitoring** | Cân bằng lưu lượng tăng uptime; theo dõi sức khỏe vận hành, tạo dashboard và cảnh báo (*alerts*) | **IBM Cloud Load Balancer** & **IBM Cloud Monitoring** | Load Balancer phân phối traffic & phát hiện lỗi node; Cloud Monitoring cung cấp khả năng quan sát (*observability*) hiệu năng & sức khỏe hệ thống |

## 3. Minh họa chuyển đổi dữ liệu: Từ Relational Tables sang Document DB (Cloudant)

Trong Monolith cũ, việc lấy 1 nhà hàng kèm review mới nhất và điểm sao đòi hỏi `JOIN` nhiều bảng (`Restaurant`, `Review`, `Rating`). Với **IBM Cloudant** (Document-based NoSQL), toàn bộ thông tin liên quan được nhúng gọn trong 1 tài liệu JSON tự chứa:

```json
{
  "id": "Yb5xwX",
  "name": "Flavors & Tales",
  "latestReviews": [
    {
      "at": "2023-07-01T16:22:01.090Z",
      "text": "Wow! F&T has won my heart with their mouthwatering dishes."
    },
    {
      "at": "2023-06-24T21:02:54.989Z",
      "text": "The Smoky Ribs were fall-off-the-bone tender, and the BBQ sauce was finger-licking good."
    }
  ],
  "starRatings": {
    "totalRatings": 34,
    "stars": [9, 20, 5, 0, 0],
    "average": 4.1
  }
}
```

- **Lợi ích:** Truy xuất toàn bộ màn hình chi tiết nhà hàng chỉ trong **1 lần đọc (single read)** không cần `JOIN`, schema dễ tiến hóa mà không phá vỡ dữ liệu cũ, trong khi dữ liệu giao dịch đặt hàng/thanh toán vẫn giữ tính toàn vẹn **ACID** trên **IBM Db2 on Cloud** (**Polyglot Persistence**).

## 4. Lời khuyên nghề nghiệp thực chiến (Career Roadmap từ Chuyên gia)

1. **Nắm chắc nền tảng trước công cụ:** Hiểu sự khác biệt giữa phát triển app trên laptop/single-server với kiến trúc phân tán trên Cloud (tách monolith thành services).
2. **Thực hành "Get your hands dirty":** Phần lớn công cụ Cloud Native là mã nguồn mở hoặc có gói miễn phí (Docker, Kubernetes, tài khoản Cloud trial). Tạo dự án thực tế và đẩy lên **GitHub**.
3. **Chứng chỉ + Guided Projects + LinkedIn:** Nếu chưa có nhiều năm kinh nghiệm thực chiến, chứng chỉ từ AWS / IBM / Azure / GCP kết hợp các dự án thực hành (2 giờ hoặc tự build chuỗi *Function → Queue → Function*) và cập nhật lên LinkedIn giúp nhà tuyển dụng tìm thấy bạn ngay lập tức.
4. **Sẵn sàng học hỏi liên tục:** Hệ sinh thái CNCF và các dịch vụ Cloud thay đổi hàng tháng — sự thoải mái với thay đổi và khả năng tự nâng cấp kỹ năng là lợi thế cạnh tranh lớn nhất.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **IBM API Connect vs. IBM App Connect vs. Event Streams:** Khi đề bài hỏi dịch vụ **tương tác với API và thế giới bên ngoài, loại bỏ phụ thuộc cứng và thêm lớp giao tiếp/định tuyến**, đáp án là **IBM API Connect** (API Management/Gateway), không phải *App Connect* (tích hợp ứng dụng SaaS/Enterprise) hay *Event Streams* (Kafka messaging).
2. **IBM Cloudant vs. IBM Db2 on Cloud vs. MongoDB:**
   - Cần **tối ưu đọc (optimized reads)** cho *reviews & ratings*, schema linh hoạt + offline-first → **IBM Cloudant**.
   - Cần **RDBMS quản lý toàn phần + OLTP + HADR** → **IBM Db2 on Cloud**.
3. **IBM Cloud Monitoring vs. IBM Cloud Activity Tracker vs. IBM Log Analysis:**
   - Theo dõi **hiệu năng và sức khỏe vận hành (performance and health)**, dashboard, alerts → **IBM Cloud Monitoring**.
   - Ghi nhận nhật ký kiểm toán hành động API (*audit trail*) → *Activity Tracker*; phân tích log → *Log Analysis*.
4. **IBM Cloud Code Engine vs. IBM Cloud Kubernetes Service (IKS):**
   - **Code Engine:** Fully managed **serverless** tự scale theo incoming HTTP requests (dùng cho *Ordering*).
   - **IKS:** Điều phối **containers/microservices** với yêu cầu linh hoạt đa tech stack (dùng cho *Search, Menu, Pricing*).
5. **Multizone Regions (MZR) vs. Single campus:** Để chống sập toàn bộ khi 1 data center gặp sự cố và đạt **99.99% availability**, luôn chọn **Multizone Regions (MZR)** chứ không phải *Single campus*.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Polyglot Architecture trong DineEase 2.0:** Chọn đúng dịch vụ cho đúng bài toán thay vì ép tất cả vào 1 công nghệ duy nhất.
- **Compute:** Serverless (*Code Engine*) cho *Ordering* + Containers (*IKS*) cho *Search/Menu/Pricing* + Dedicated Physical (*Bare Metal*) cho *Payment*.
- **Data:** RDBMS có HADR (*Db2 on Cloud*) cho giao dịch + Document NoSQL (*Cloudant*) cho reviews/ratings.
- **Networking & Ops:** *MZR* (HA 99.99%) + *API Connect* + *CDN* + *Load Balancer* + *IBM Cloud Monitoring*.
