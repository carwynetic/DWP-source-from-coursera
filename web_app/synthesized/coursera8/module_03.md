# Module 3: Components of Cloud Computing

> **Tư tưởng cốt lõi:** Hạ tầng Cloud được tổ chức phân tầng từ **Regions → Availability Zones → Data Centers**, vận hành trên các đơn vị tính toán (**VMs, Bare Metal Servers, Containers**), kết nối qua **Software-Defined Networking (VPC, Subnets, ACLs, Security Groups)** và lưu trữ bằng **4 loại Cloud Storage** kết hợp **CDN** để tối ưu chi phí, hiệu năng và độ trễ.

## 1. Cấu trúc vật lý toàn cầu: Region, Availability Zone & Data Center

| Khái niệm | Định nghĩa & Vai trò kiến trúc | Ví dụ / Tên gọi |
| --- | --- | --- |
| **Cloud Region** | Khu vực/vị trí địa lý nơi nhà cung cấp **tập trung cụm hạ tầng (clusters its infrastructure)**; các Region cô lập nhau để chống thảm họa tự nhiên diện rộng | `NA South`, `US East` |
| **Availability Zone (AZ)** | Các **vị trí vật lý tách biệt trong một Region**, gồm một hoặc nhiều Data Center với **nguồn điện, làm mát và mạng độc lập** — loại bỏ *single point of failure*, tăng fault tolerance | `DAL-09`, `us-east-1` |
| **Data Center** | Phòng máy/nhà kho khổng lồ chứa các pod và rack thiết bị tính toán (servers), lưu trữ và mạng | Kết nối liên thông qua đường truyền băng thông cực cao |

## 2. Ảo hóa (Virtualization), Hypervisors & Các loại Virtual Machines (VMs)

### A. So sánh Type 1 vs. Type 2 Hypervisor
Hypervisor là lớp phần mềm nằm trên máy chủ vật lý giúp kéo tài nguyên phần cứng (CPU, RAM, disk) chia cho nhiều VM độc lập, mang lại **3 lợi ích lớn**: (1) **Tiết kiệm chi phí** nhờ hợp nhất máy chủ, (2) **Tốc độ & linh hoạt** khi dựng môi trường dev/test, (3) **Giảm downtime** nhờ di chuyển nhanh VM sang host khác khi phần cứng lỗi.

| Tiêu chí | Type 1 Hypervisor (*Bare-metal*) | Type 2 Hypervisor (*Hosted*) |
| --- | --- | --- |
| **Kiến trúc cài đặt** | Cài **trực tiếp trên phần cứng vật lý** (không qua Host OS trung gian) | Có **lớp Host OS** nằm giữa phần cứng và hypervisor |
| **Hiệu năng & Bảo mật** | **Độ trễ thấp hơn, bảo mật cao hơn**, phổ biến nhất trên Cloud/Enterprise | Độ trễ cao hơn, chủ yếu dùng cho **end-user virtualization** trên máy cá nhân |
| **Ví dụ điển hình** | **VMware ESXi**, **Microsoft Hyper-V**, **Open-source KVM** | **Oracle VirtualBox**, **VMware Workstation** |

### B. 4 loại Virtual Machine (VM / VSI) trên Cloud

| Loại VM | Cơ chế cấp phát & Giá | Use case phù hợp nhất |
| --- | --- | --- |
| **Shared / Public Cloud VMs** | Multi-tenant dùng chung phần cứng vật lý; cấu hình định sẵn hoặc tùy chỉnh; tính phí theo giờ/giây hoặc tháng | Web app thông thường, workload biến động linh hoạt *(lưu ý: gói tháng hủy giữa chừng vẫn trả đủ tháng)* |
| **Transient / Spot VMs** | Tận dụng **tài nguyên nhàn rỗi (unused capacity)** trong data center với **giá rẻ hơn rất nhiều**; **CSP có thể thu hồi bất kỳ lúc nào** | Workload **non-production**, dev/test, xử lý stateless, kiểm thử khả năng mở rộng, Big Data / HPC chịu lỗi gián đoạn |
| **Reserved Virtual Server Instances** | Đặt trước và **đảm bảo sẵn sàng tài nguyên** trong tương lai theo hợp đồng **1 năm hoặc 3 năm**, giá rẻ hơn theo giờ | Workload có mức tải nền ổn định dài hạn cần cam kết dung lượng tại data center chỉ định |
| **Dedicated Hosts** | **Single-tenant isolation** — chỉ VM của bạn chạy trên host vật lý đó, kiểm soát vị trí đặt (data center & POD) | Đáp ứng quy định tuân thủ pháp lý, bảo mật nghiêm ngặt hoặc điều khoản cấp phép phần mềm (*licensing*) |

## 3. Bare Metal Servers vs. Virtual Machines vs. Containers

```text
[Bare Metal Server]              [Virtual Machines (VMs)]         [Containers]
+-------------------+            +----------+  +----------+       +--------+ +--------+
| App / Hypervisor  |            |  App A   |  |  App B   |       | App A  | | App B  |
+-------------------+            | Bins/Libs|  | Bins/Libs|       |Bins/Lib| |Bins/Lib|
| Customer OS       |            | Guest OS |  | Guest OS |       +--------+ +--------+
+-------------------+            +----------+  +----------+       |  Container Engine |
| Physical Hardware |            |       Hypervisor       |       |   (Docker / K8s)  |
| (Single-Tenant)   |            +------------------------+       +-------------------+
+-------------------+            |  Host OS / Hardware    |       | Host OS / Hardware|
                                 +------------------------+       +-------------------+
```

| Tiêu chí | Bare Metal Server | Virtual Machine (VM) | Container |
| --- | --- | --- | --- |
| **Bản chất** | Máy chủ vật lý **single-tenant** dành riêng cho 1 khách hàng, không chia sẻ CPU/RAM | Máy tính phần mềm chạy đầy đủ **Guest OS** riêng trên Hypervisor | Đơn vị thực thi đóng gói **code + libraries + dependencies**, **dùng chung nhân Host OS** (từ Linux cgroups 2008) |
| **Kích thước & Khởi tạo** | Cấp phát chậm nhất: **20–40 phút** (dựng sẵn) hoặc **3–4 giờ** (tùy biến phần cứng) | Kích thước **vài GB**, khởi động trong **vài giây/phút** | Nhẹ (**vài MB**), khởi động trong **mili-giây** |
| **Hiệu năng & Chi phí** | **Hiệu năng cao nhất, bảo mật nhất**, hỗ trợ **GPU**, không có *hypervisor tax* hay *noisy neighbor*; giá cao, tải cố định | Cân bằng chi phí, co giãn tốt nhưng bị giới hạn thông lượng do chia sẻ phần cứng | Tối ưu mật độ & tài nguyên dư (chia sẻ tài nguyên nhàn rỗi giữa các container), chi phí rất thấp |
| **Tính di động & Cô lập** | Gắn chặt cấu hình vật lý, toàn quyền truy cập phần cứng & kernel | Di chuyển qua lại giữa hypervisor, nhưng phụ thuộc OS/thư viện nên kém linh hoạt hơn container | **Cực kỳ di động (chạy mọi nơi)**; cô lập ứng dụng giúp **mã độc ở 1 container không ảnh hưởng container khác** |
| **Use cases vàng** | HPC, Big Data, Deep Learning/AI (GPU), ERP/CRM lõi, tài chính/game độ trễ cực thấp, yêu cầu compliance khắt khe | Lift-and-shift ứng dụng truyền thống, chạy đa OS khác nhau (Windows trên Linux) | **Microservices**, **Cloud-native apps**, CI/CD đa môi trường (Dev/QA/Prod), Hybrid/Multicloud (Docker/K8s/OpenShift) |

## 4. Secure Cloud Networking (Software-Defined Networking - SDN)

Trong Cloud, thiết bị mạng vật lý được ảo hóa thành **dịch vụ lập trình được qua API (SDN)** (vd: NIC vật lý → **vNIC**). Để xây dựng kiến trúc mạng đa tầng an toàn (3-tier web app):

1. **VPC (Virtual Private Cloud):** Phân vùng mạng cô lập logic, xác định dải IP riêng trên Public Cloud.
2. **Subnets:** Chia VPC thành các phân đoạn nhỏ hơn — **Subnets là khu vực chính nơi bảo mật được triển khai trên Cloud**.
3. **2 lớp tường lửa bảo vệ trong Subnet:**
   - **ACLs (Access Control Lists):** Đóng vai trò **tường lửa ở cấp độ Subnet** (*subnet-level firewall*).
   - **Security Groups (SGs):** Đóng vai trò **bảo vệ ở cấp độ Instance / VSI** (*instance-level security*) — vd: tách 3 Security Groups riêng cho Web tier, App tier và Database tier.
4. **Cổng kết nối & Cân bằng tải:**
   - **Public Gateway:** Cho phép các VSI ở tầng Web truy cập Internet.
   - **Load Balancers:** Phân phối lưu lượng đều giữa các máy chủ, đảm bảo băng thông và độ sẵn sàng.
   - **VPN & Dedicated Connections (vd: IBM Cloud Direct Link):** Mở rộng kết nối bảo mật tốc độ cao từ trung tâm dữ liệu on-premises lên Cloud.

## 5. Cloud Storage & Content Delivery Networks (CDNs)

### A. So sánh 4 loại Cloud Storage cốt lõi

| Loại Storage | Cách gắn kết & Giao thức | Độ bền & Tính chia sẻ | Tốc độ & Chi phí | Phù hợp / Không phù hợp |
| --- | --- | --- | --- | --- |
| **Direct Attached (Local)** | Gắn trực tiếp trong chassis hoặc cùng rack của server | **Ephemeral (không bền vững)** — mất khi hủy compute; **không chia sẻ** được | Rất nhanh | Chỉ nên chứa **OS** hoặc dữ liệu tạm |
| **File Storage (NFS)** | Gắn vào compute node qua **mạng Ethernet** chuẩn (**NAS / NFS**) | Bền vững (trên appliance có mã hóa); **gắn đồng thời tới ~80+ compute nodes** | Tốc độ có thể **dao động theo tải mạng Ethernet**; rẻ hơn Block | Chia sẻ file phòng ban, *landing zone*, web hosting trộn text + media |
| **Block Storage** | Chia file thành các khối (blocks) có địa chỉ riêng; gắn qua **cáp quang (high-speed fiber)** | Bền vững (appliance có encryption at rest & in transit); **thường chỉ gắn vào 1 compute node tại một thời điểm** | **Nhanh và ổn định nhất**, cấu hình được **IOPS**; giá cao nhất | **Transactional / Relational Databases**, mail servers, VM boot volumes *(không dùng để share disk giữa nhiều node)* |
| **Object Storage** | **Không gắn vào compute node**; truy cập qua **HTTP RESTful API (chuẩn S3 API)** | Cực kỳ bền vững; **dung lượng gần như vô hạn (infinite)**; cấu trúc phẳng (**Buckets → Objects + Metadata**, không lồng bucket) | **Chậm nhất**, **không có tùy chọn IOPS**; **rẻ nhất** (vài xu/GB/tháng) | Dữ liệu tĩnh phi cấu trúc (ảnh, video, log, IoT, VM images, backup/DR thay thế băng từ). **KHÔNG thể chạy OS hay database** |

> **Lưu ý về Snapshot & IOPS:**
> - **Snapshot:** Chụp tức thời trạng thái File/Block storage bằng metadata (không gây downtime, các snapshot sau chỉ lưu thay đổi); dùng để khôi phục toàn bộ volume, **không dùng để khôi phục từng file đơn lẻ**.
> - **IOPS (Input/Output Operations Per Second):** Tốc độ đọc/ghi của đĩa vật lý (khác với tốc độ mạng). IOPS quá thấp gây nghẽn cổ chai; quá cao gây lãng phí chi phí.
> - **Object Storage Tiers:** Chia theo tần suất truy cập — **Standard** (truy cập thường xuyên, giá lưu trữ cao nhất), **Vault / Archive** (1–2 lần/tháng), **Cold Vault** (1–2 lần/năm, giá siêu rẻ nhưng lấy dữ liệu có thể mất hàng giờ; phí retrieval cao hơn). Hỗ trợ **automatic archiving rules** dựa trên metadata.

### B. Content Delivery Network (CDN)
- **Định nghĩa:** Mạng máy chủ phân tán toàn cầu lưu bản sao tạm (**cached copies**) nội dung tĩnh (ảnh, video, CSS/JS) dựa trên vị trí địa lý người dùng.
- **Cơ chế tăng tốc:** Thay vì user ở Sydney phải đi khứ hồi 17.200 dặm tới server gốc ở Dallas (RTT ~170 ms), user lấy dữ liệu trực tiếp từ node CDN gần nhất.
- **3 lợi ích gián tiếp ngoài việc giảm độ trễ:** (1) Giảm tải băng thông & công suất cho origin server ở Dallas, (2) Tăng uptime của hệ thống gốc, (3) **Security through obscurity** vì người dùng không giao tiếp trực tiếp với server gốc.

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Region vs. Availability Zone vs. Data Center:** *Region* là khu vực địa lý nơi CSP **cụm hóa hạ tầng** (*clusters its infrastructure*); *AZ* là các vị trí vật lý độc lập trong 1 Region (chứa 1 hoặc nhiều Data Center); *Data Center* là phòng máy/nhà kho chứa pod & rack.
2. **File Storage vs. Block Storage:** Câu hỏi nhắc *"mounted on multiple compute nodes at once / disk sharing"* → **File Storage (NFS)**; câu hỏi nhắc *"one node at a time / consistent fast access / databases / fiber"* → **Block Storage**.
3. **Subnets vs. Security Groups vs. ACLs:** *Subnets* là **khu vực chính** triển khai bảo mật; *ACLs* bảo vệ **ở cấp Subnet**; **Security Groups (SGs)** bảo vệ **ở cấp Virtual Instance (VSI)** bên trong subnet.
4. **Hạn chế của Object Storage:** Luôn nhớ rằng trên Object Storage **không thể chạy hệ điều hành (OS) hoặc cơ sở dữ liệu (databases)** và **không thể lồng bucket trong bucket**.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Hypervisors:** Type 1 (ESXi, Hyper-V, KVM — chạy trực tiếp trên phần cứng, hiệu năng/bảo mật cao) vs. Type 2 (VirtualBox, VMware Workstation — hosted qua Host OS).
- **4 loại VM:** Shared/Public, Transient/Spot (giá rẻ từ tài nguyên dư, có thể bị thu hồi), Reserved (cam kết 1–3 năm), Dedicated Hosts (cô lập 1 khách hàng).
- **Bare Metal:** Hiệu năng & bảo mật tối đa, hỗ trợ GPU, không hypervisor, cấp phát lâu (20 phút–4 giờ). **Containers:** Nhẹ (MB), khởi động ms, dùng chung Host OS, cô lập tiến trình.
- **Storage Matrix:** Ephemeral = *Direct Attached*; Shared Ethernet = *File (NFS)*; Fast 1-node Fiber = *Block*; Infinite API S3 = *Object*.
