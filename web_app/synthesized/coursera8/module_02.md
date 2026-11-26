# Module 2: Cloud Computing Models

> **Tư tưởng cốt lõi:** Kiến trúc Cloud được định hình bởi hai trục quyết định: **Service Models** (IaaS, PaaS, SaaS — xác định ranh giới trách nhiệm quản lý giữa khách hàng và nhà cung cấp) và **Deployment Models** (Public, Private, Hybrid, Community — xác định hạ tầng đặt ở đâu, ai sở hữu và ai được phép sử dụng).

## 1. Ba Mô hình Dịch vụ (Service Models): IaaS vs. PaaS vs. SaaS

Hãy dùng phép ẩn dụ chiếc xe để hình dung mức độ trừu tượng và trách nhiệm:
- **IaaS (Thuê dài hạn / Lease a car):** Bạn chọn cấu hình xe, tự lái, tự đổ xăng, tự trả phí cầu đường và bảo dưỡng phần mềm chạy trên đó. Người dùng điển hình: **System Admin / IT Admin**.
- **PaaS (Thuê xe ngắn hạn ở sân bay / Rent a car):** Bạn không quan tâm cấu hình hay màu xe, chỉ việc lái (viết code ứng dụng). Người dùng điển hình: **Developer**.
- **SaaS (Đi Taxi / Uber):** Bạn chỉ lên xe đi tới đích, không lái và không lo xăng xe hay bảo dưỡng. Người dùng điển hình: **End-user / Mọi người**.

| Tiêu chí so sánh | IaaS (*Infrastructure-as-a-Service*) | PaaS (*Platform-as-a-Service*) | SaaS (*Software-as-a-Service*) |
| --- | --- | --- | --- |
| **Nhà cung cấp quản lý** | Data center vật lý, điện, làm mát, mạng, server, storage và **lớp ảo hóa / hypervisor** | Toàn bộ phần IaaS + **OS, runtime, middleware, database, dev tools, APIs** | Toàn bộ phần PaaS + **ứng dụng và dữ liệu ứng dụng (application data)** |
| **Khách hàng quản lý** | **OS** (chọn sẵn hoặc tự cài), **middleware, runtime, ứng dụng, dữ liệu, backup** | **Chỉ mã nguồn ứng dụng (application code) và bảo trì logic nghiệp vụ** | Chỉ cấu hình nhẹ (branding, trường dữ liệu, bật/tắt tính năng, quản lý quyền người dùng) |
| **Mức độ kiểm soát & phức tạp** | Cao nhất (can thiệp sâu vào VM, mạng, OS) | Trung bình (trừu tượng hóa hạ tầng, tập trung dev) | Thấp nhất (tùy biến hạn chế, dùng ngay qua trình duyệt/API) |
| **Tính năng đặc trưng** | Cấp phát VMs theo Region/Zone, Auto-scaling, Load balancing, Block/File/Object storage | Runtime environment, **APIs cho dịch vụ** (caching, queuing, identity → **loại bỏ việc phải tích hợp thủ công các thành phần rời rạc**), push-and-run | Kiến trúc **multi-tenant**, ứng dụng chạy trên **remote cloud network**, trả phí **subscription**, nâng cấp bảo toàn tùy biến |
| **Ví dụ tiêu biểu** | AWS EC2, IBM Cloud VPC VMs, Google Compute Engine, Azure VMs | AWS Elastic Beanstalk, Red Hat OpenShift, Cloud Foundry, IBM Cloud Paks | Salesforce, Office 365, Gmail, Workday, SAP SuccessFactors, NetSuite CRM |
| **Use cases điển hình** | Lift-and-shift từ on-prem lên VM, dựng môi trường dev/test, HPC (dự báo thời tiết, mô hình tài chính), DR | Phát triển/thử nghiệm nhanh app web/mobile, thử ngôn ngữ mới với rủi ro thấp | Email, CRM, HCM, cộng tác văn phòng, eCommerce, **SaaS Integration Platforms (SIPs)** |

### Quy tắc vàng khi chọn Service Model
> **"Stay as high on the stack as you can."** — Mặc định ưu tiên **SaaS** nếu phần mềm có sẵn đáp ứng nghiệp vụ (vd: CRM, Email); chuyển xuống **PaaS** khi cần xây ứng dụng tùy biến (vd: React/Node app) mà không muốn quản trị OS; chỉ xuống **IaaS** khi cần kiểm soát tuyệt đối cấu hình compute/network hoặc chạy OS không được PaaS hỗ trợ.

## 2. Rủi ro & Mối quan ngại theo từng Service Model

| Mô hình | Rủi ro / Mối quan ngại chính |
| --- | --- |
| **IaaS** | Thiếu minh bạch trong cấu hình/quản trị hạ tầng vật lý; **phụ thuộc bên thứ ba (third-party dependency)** đối với tính sẵn sàng và hiệu năng của workload; chi phí cao hơn và tự chịu trách nhiệm quản trị VM/OS |
| **PaaS** | Rủi ro bảo mật thông tin, downtime của nhà cung cấp ảnh hưởng trực tiếp dịch vụ; **không kiểm soát trực tiếp** khi nhà cung cấp thay đổi chiến lược, dịch vụ hoặc công cụ |
| **SaaS** | **Quyền sở hữu và an toàn dữ liệu** (*data ownership & data safety*) khi giao dữ liệu trọng yếu cho bên thứ ba; phụ thuộc chất lượng kết nối mạng; khả năng tùy biến bị giới hạn |

## 3. Bốn Mô hình Triển khai (Deployment Models)

```text
+-----------------------+---------------------------------------------------------------+
| Deployment Model      | Ai sở hữu / Vận hành & Phạm vi sử dụng                        |
+-----------------------+---------------------------------------------------------------+
| 1. Public Cloud       | CSP sở hữu & vận hành; chia sẻ multi-tenant qua Internet      |
| 2. Private Cloud      | Dành riêng cho 1 tổ chức (chạy On-prem hoặc qua VPC trên CSP) |
| 3. Hybrid Cloud       | Kết nối Private Cloud (on-prem) + Public Cloud thành 1 thể    |
| 4. Community Cloud    | Dành riêng cho nhóm tổ chức có chung mối quan tâm/tuân thủ    |
+-----------------------+---------------------------------------------------------------+
```

### A. Public Cloud
- **Đặc điểm:** Kiến trúc **multi-tenant ảo hóa** ngoài tường lửa doanh nghiệp; người dùng **không sở hữu máy chủ**, không quản lý vận hành server mà thuê qua console/API theo mô hình pay-as-you-go hoặc subscription.
- **Lợi ích:** Giảm mạnh **TCO** (*Total Cost of Ownership*), **economies of scale** lớn nhất, tài nguyên khổng lồ đáp ứng biến động tải, tính sẵn sàng cao (*high availability*).
- **Use cases chuẩn:**
  - Tăng tốc phát triển/kiểm thử để **giảm time-to-market** cho sản phẩm & dịch vụ.
  - Ứng dụng có nhu cầu tải **biến động thất thường (fluctuating capacity)** *(không phải tải ổn định quanh năm)*.
  - Hạ tầng dự phòng cho **Disaster Recovery (DR), bảo vệ dữ liệu và Business Continuity**.
  - Thuê ngoài các nền tảng **ít trọng yếu và đã chuẩn hóa** (*less critical and standardized platforms*).
- **Quan ngại:** Bảo mật (data breach, account hijacking, lỗ hổng hệ thống) và **tuân thủ chủ quyền dữ liệu (data sovereignty compliance)** xuyên biên giới.

### B. Private Cloud & Virtual Private Cloud (VPC)
- **Định nghĩa NIST:** Hạ tầng đám mây cấp phát **độc quyền cho một tổ chức duy nhất** (gồm nhiều đơn vị thành viên), có thể đặt tại chỗ (**on-premises**) hoặc thuê ngoài (**off-premises**).
- **Virtual Private Cloud (VPC):** Là dạng *external private cloud* triển khai trên một phân vùng **cô lập logic (logically isolated)** của Public Cloud — kết hợp tính co giãn/sẵn sàng của Public Cloud với bảo mật tùy biến riêng.
- **Lợi ích cốt lõi:**
  - Tận dụng hạ tầng do chính tổ chức **kiểm soát trực tiếp** (*directly controlled by organization*) và tối ưu phần cứng/phần mềm sẵn có.
  - Đảm bảo **application portability** (xây dựng và di chuyển ứng dụng linh hoạt mà không hy sinh bảo mật/tuân thủ).
  - Đáp ứng quy định khắt khe với dữ liệu nhạy cảm.

### C. Hybrid Cloud — 3 Trụ cột & Phân loại
Hybrid Cloud kết nối Private Cloud (on-prem) với Public Cloud của bên thứ ba thành một hạ tầng thống nhất linh hoạt. Lý tưởng cho **ứng dụng cực kỳ nhạy cảm/trọng yếu nhưng có nhu cầu hiệu năng và dung lượng biến động khó lường** (chạy phần lõi nhạy cảm ở Private, phần tải đột biến đẩy sang Public).

- **3 nguyên lý cốt lõi của Hybrid Cloud:**
  1. **Interoperability (Tính liên thông):** Các dịch vụ Public và Private Cloud **hiểu được API, cấu hình, định dạng dữ liệu, cũng như cơ chế authentication & authorization của nhau**.
  2. **Scalability & Cloud Bursting:** Khi nhu cầu tăng đột biến vượt ngưỡng Private Cloud, workload tự động mở rộng sang mượn tài nguyên Public Cloud và **trả lại về Private Cloud khi hết đợt cao điểm** — kỹ thuật này gọi là **Cloud Bursting**.
  3. **Portability (Tính di động):** Không bị khóa chặt vào một nhà cung cấp (*vendor lock-in*), tự do di chuyển app và dữ liệu giữa on-prem và nhiều nhà cung cấp Cloud.

| Biến thể Hybrid Cloud | Đặc điểm kiến trúc |
| --- | --- |
| **Hybrid Monocloud** | Mô hình Hybrid chỉ kết nối với **một** nhà cung cấp Public Cloud duy nhất |
| **Hybrid Multicloud** | Sử dụng stack dựa trên **chuẩn mở (open standards-based)** có thể triển khai trên **bất kỳ** hạ tầng Public Cloud nào |
| **Composite Multicloud** | Biến thể chi tiết hơn của Hybrid Multicloud: **phân tán các thành phần của cùng một ứng dụng** qua nhiều nhà cung cấp và dịch vụ Cloud khác nhau |

### D. Community Cloud (Truyền thống vs. Software-Defined)
Theo NIST SP 800-145, **Community Cloud** phục vụ độc quyền một **cộng đồng các tổ chức có chung mối quan tâm** (sứ mệnh, bảo mật, chính sách, tuân thủ — vd: chính phủ, y tế, tài chính).

| Khía cạnh | Traditional Community Cloud | Software-Defined Community Cloud (vd: GCP Assured Workloads) |
| --- | --- | --- |
| **Cách cô lập** | Tách biệt vật lý (data center & phần cứng riêng) | Mỗi **Project** là một *enclave* cô lập logic & mật mã từ hạ tầng chung |
| **Kiểm soát nhân sự hỗ trợ** | Nhân sự phải ngồi tại cơ sở vật lý chuyên biệt | Access management giới hạn hỗ trợ theo thuộc tính (quốc tịch, vị trí làm việc, nhân thân) |
| **Bản địa hóa dữ liệu (Data localization)** | Thiết bị lưu trữ chuyên dụng cho cộng đồng | Thực thi bằng phần mềm (*enforced by software*) theo policy |
| **Tốc độ cập nhật dịch vụ mới** | Chậm vì phụ thuộc phần cứng tách riêng | Nhanh, tận dụng ngay phần cứng và cải tiến dịch vụ mới từ quy mô Public Cloud |

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Public Cloud KHÔNG dành cho mọi workload ổn định:** Public Cloud tỏa sáng ở **giảm time-to-market**, **DR/backup** và **tải biến động**; nếu câu hỏi nhắc đến *"applications with stable capacity"* hay *"business critical platforms"* có yêu cầu kiểm soát/nhạy cảm cao, đó không phải thế mạnh đặc trưng của Public Cloud thuần túy.
2. **Nhạy cảm + Trọng yếu + Tải khó lường = Hybrid Cloud:** Nếu đề bài vừa đòi hỏi bảo mật cao cho hệ thống trọng yếu (*highly sensitive and mission-critical*) vừa có nhu cầu tài nguyên biến động khó đoán (*unpredictable capacity*), đáp án tối ưu là **Hybrid Cloud** (không phải Private Cloud thuần túy hay Public Cloud thuần túy).
3. **Phân biệt Interoperability vs. Cloud Bursting:** *Interoperability* là hiểu chung API, data format, config và auth giữa Public & Private; còn *Cloud Bursting* là hành động **mở rộng tạm thời sang Public Cloud khi quá tải rồi quay về Private Cloud khi hết đỉnh tải**.
4. **Trong PaaS, thứ giúp loại bỏ tích hợp rời rạc là "APIs for services":** Đừng nhầm với *Runtime environment* (nơi thực thi code) hay *Rapid deployment mechanisms* (push-and-run).

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- **IaaS** (CSP quản lý hạ tầng + hypervisor; khách hàng quản lý OS, middleware, app) → **PaaS** (CSP quản lý thêm OS, runtime, middleware, DB; khách hàng chỉ quản lý code ứng dụng) → **SaaS** (CSP quản lý cả ứng dụng và dữ liệu ứng dụng trên mạng Cloud từ xa).
- **VPC** là hình thức Private Cloud cô lập logic nằm trên hạ tầng Public Cloud.
- **Hybrid Cloud** dựa trên 3 trụ cột: **Interoperability, Scalability (Cloud Bursting), Portability**.
- **Software-Defined Community Cloud** thay thế tách biệt vật lý cứng nhắc bằng cô lập logic/mật mã theo policy và kiểm soát truy cập theo thuộc tính.
