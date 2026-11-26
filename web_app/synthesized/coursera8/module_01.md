# Module 1: Overview of Cloud Computing

> **Tư tưởng cốt lõi:** Cloud Computing là mô hình cung cấp tài nguyên tính toán theo nhu cầu qua mạng (on-demand, pay-as-you-go) dựa trên nền tảng ảo hóa và **5 đặc tính cốt lõi của NIST**; không chỉ là chiến lược IT, Cloud đóng vai trò bệ phóng hạ tầng cho các công nghệ đột phá như **IoT, AI, Blockchain và Analytics**.

## 1. Định nghĩa chuẩn NIST & 5 Đặc tính cốt lõi (Essential Characteristics)

Theo **NIST** (*US National Institute of Standards and Technology*), Cloud Computing là mô hình cho phép truy cập mạng thuận tiện, theo nhu cầu tới **một nhóm tài nguyên tính toán có thể cấu hình dùng chung** (*a shared pool of configurable computing resources* — gồm networks, servers, storage, applications, services) có thể được cấp phát và thu hồi nhanh chóng với nỗ lực quản lý hoặc tương tác tối thiểu từ nhà cung cấp.

Mô hình NIST gồm **5 đặc tính cốt lõi**, **3 mô hình dịch vụ** (IaaS, PaaS, SaaS) và **4 mô hình triển khai** (Public, Private, Hybrid, Community):

| Đặc tính cốt lõi | Bản chất kỹ thuật & kinh tế | Ví dụ thực tế |
| --- | --- | --- |
| **On-demand self-service** | Người dùng tự cấp phát tài nguyên qua portal/API 24/7 không cần chờ bộ phận mua sắm hay IT duyệt thủ công | Lập trình viên tự tạo VM hoặc DB trong vài phút như dùng máy ATM |
| **Broad network access** | Truy cập dịch vụ qua mạng chuẩn từ nhiều thiết bị (laptop, tablet, smartphone, wearable) | Public Cloud bắt buộc có Internet; Private Cloud nội bộ có thể dùng Intranet |
| **Resource pooling** | Gom tài nguyên vật lý phục vụ nhiều khách hàng (**multi-tenant model**), gán động theo nhu cầu | Mang lại **economies of scale** và tiết kiệm chi phí đáng kể cho người dùng |
| **Rapid elasticity** | Mở rộng/thu hẹp tài nguyên tức thì: **scale-up/down** (vertical) hoặc **scale-out/in** (horizontal) | Sàn e-commerce tăng năng lực dịp Black Friday rồi giảm lại sau sale |
| **Measured service** | Đo lường mức tiêu thụ và tính phí theo thực tế sử dụng (**utility model / pay-as-you-go**) | Trả tiền điện toán theo giờ/giây dùng thực (trừ dịch vụ miễn phí như Gmail hay bản trial) |

## 2. Lịch sử tiến hóa: Từ Mainframe thập niên 1950 đến Cloud hiện đại

```text
[1950s: Mainframes + Time-sharing]
   └─► Nhiều người dùng qua dumb terminals chia sẻ CPU & storage trên 1 mainframe
        │
[1970s: Virtual Machine (VM) OS]
   └─► Cho phép nhiều môi trường độc lập cùng chạy trên một phần cứng vật lý
        │
[Hypervisor Layer]
   └─► Tách biệt logic các VM (CPU, RAM, disk); một VM lỗi không làm sập VM khác
        │
[Modern Cloud + Pay-as-you-go]
   └─► Chuyển từ CapEx (đầu tư phần cứng lớn trả trước) ──► OpEx (chi phí vận hành theo mức dùng)
```

- **Động lực kinh tế cốt lõi:** Thay vì bỏ vốn lớn (**CapEx**) mua máy chủ vật lý dư thừa để đón đỉnh tải, doanh nghiệp chuyển sang mô hình **OpEx** (trả tiền theo mức dùng thực tế như hóa đơn điện/nước), giảm rào cản gia nhập cho cả startup lẫn tập đoàn lớn.

## 3. Các yếu tố cân nhắc, Lợi ích & Rủi ro khi áp dụng Cloud

### A. Lợi ích phân theo 3 trụ cột
1. **Flexibility (Tính linh hoạt):** Tự chọn mức độ kiểm soát qua các mô hình *as-a-Service*, mở rộng/thu hẹp theo nhu cầu, truy cập mọi nơi.
2. **Efficiency (Hiệu quả vận hành):** Đưa ứng dụng ra thị trường trong vài giờ thay vì vài tuần/tháng; giảm chi phí bảo trì phần cứng; **lỗi phần cứng không gây mất dữ liệu nhờ bản sao lưu (backups) duy trì trên mạng**.
3. **Strategic Value (Giá trị chiến lược):** Tiếp cận nhanh công nghệ tiên tiến (AI, Analytics) để tập trung vào năng lực cốt lõi (*core business*) thay vì quản trị hạ tầng.

### B. Thách thức & Yếu tố cân nhắc chiến lược
- **Cân nhắc nền tảng:** Chi phí hạ tầng & mức độ sẵn sàng của workload (không phải workload cũ nào cũng đưa lên Cloud nguyên trạng); cân nhắc giữa mua phần mềm đóng gói (*off-the-shelf software* + chi phí nâng cấp) với **SaaS và nền tảng phát triển (development platforms)**.
- **Rủi ro cần kiểm soát:** Bảo mật và mất mát/gián đoạn dữ liệu (*data security & availability*), chủ quyền dữ liệu & tuân thủ pháp lý (*governance, sovereignty, regulatory compliance*), thiếu chuẩn hóa liên thông giữa các nền tảng (*lack of standardization*), chọn sai mô hình triển khai/dịch vụ hoặc nhà cung cấp, và bài toán *Business Continuity & Disaster Recovery*.

## 4. Hệ sinh thái các Nhà cung cấp dịch vụ Cloud (CSPs) tiêu biểu

| Nhà cung cấp | Thế mạnh & Dịch vụ đặc trưng được nhấn mạnh |
| --- | --- |
| **AWS (Amazon Web Services)** | Tiên phong trong thị trường Cloud; hệ sinh thái IaaS/PaaS đồ sộ (compute, DevOps, ML, serverless, robotics) theo mô hình metered pay-as-you-go |
| **Microsoft Azure** | Phủ sóng toàn cầu mạnh mẽ; hỗ trợ đa dạng ngôn ngữ/công cụ cả hệ sinh thái Microsoft lẫn bên thứ ba qua IaaS, PaaS, SaaS |
| **Google Cloud Platform (GCP)** | Dùng chính hạ tầng nội bộ của Google Search & YouTube; nổi bật với **Google App Engine** (tự động cấp phát/thu hồi tài nguyên theo tải) và G Suite |
| **IBM Cloud** | Full-stack qua Public/Private/Hybrid; nổi bật với Bare Metal, VMware, Cloud Paks hiện đại hóa ứng dụng và thương vụ **Red Hat** định vị dẫn đầu Hybrid Cloud |
| **Alibaba Cloud** | Nhà cung cấp Cloud lớn nhất Trung Quốc; phục vụ hệ sinh thái thương mại điện tử Alibaba và khách hàng toàn cầu |
| **Oracle Cloud** | Nổi tiếng về **SaaS** (ERP, SCM, HCM, CX) và **Oracle Data Cloud** — một trong những nền tảng quản lý dữ liệu đám mây lớn nhất thế giới |
| **Salesforce** | Chuyên sâu về **SaaS CRM** (Sales Cloud, Service Cloud, Marketing Cloud) kết hợp phân tích thời gian thực và lắng nghe mạng xã hội |
| **SAP** | Doanh nghiệp phần mềm lõi (ERP, CRM, HR, Finance) trên Cloud cùng nền tảng SAP Cloud Platform |

## 5. Business Case & Case Studies chuyển đổi số với Cloud

Theo khảo sát **IDC**, lượng dữ liệu số toàn cầu dự báo đạt **163 zettabytes** vào năm 2025 (30% là dữ liệu thời gian thực). Khả năng đưa ra **quyết định dựa trên dữ liệu (data-driven decisions)** khiến Cloud trở thành điều kiện sinh tồn. Doanh nghiệp không tích hợp Cloud vào chiến lược kinh doanh sẽ đối mặt nguy cơ thiếu tốc độ, sự linh hoạt, khả năng đổi mới và **năng lực ra quyết định (decision-making capacity)**.

| Doanh nghiệp | Thách thức ban đầu | Giải pháp Cloud & Kết quả đạt được |
| --- | --- | --- |
| **American Airlines** | Ứng dụng monolithic cứng nhắc, chậm ra mắt công cụ tự phục vụ cho hành khách | Chuyển sang kiến trúc **cloud-native microservices** trên IBM Cloud → phát hành app nhanh hơn, tăng độ tin cậy, giảm chi phí nâng cấp |
| **UBank** | Tổ chức tinh gọn giới hạn nhân sự, cần rút ngắn đường từ ý tưởng đến production | Áp dụng mô hình **PaaS** + trợ lý ảo IBM Watson cho hồ sơ vay mua nhà → trao quyền cho dev, rút ngắn *time-to-market* |
| **Bitly** | Chuyển từ startup rút gọn link sang sản phẩm enterprise toàn cầu với độ trễ thấp | Di chuyển **25 tỷ links** và 1 tỷ tương tác lên hạ tầng Cloud đa POPs + Cloud Object Storage → mở rộng linh hoạt, kiểm soát chi phí |
| **ActivTrades** | Giao dịch tài chính đa thị trường đòi hỏi độ trễ cực thấp và tốc độ xử lý tức thời | Di chuyển 3 hệ thống giao dịch lõi lên **IBM Cloud for VMware** → tăng hiệu năng tới **3X**, khởi tạo tài nguyên trong vài giờ thay vì vài ngày |

## 6. Công nghệ mới nổi được tăng tốc bởi Cloud (IoT, AI, Blockchain, Analytics)

### A. Quan hệ cộng sinh 3 chiều (Three-way Symbiotic Relationships)
1. **IoT + AI + Cloud:**
   - **IoT** đóng vai trò nguồn thu thập luồng dữ liệu khổng lồ từ cảm biến/thiết bị.
   - **Cloud** là **điểm thu thập động, có khả năng mở rộng (dynamic & scalable collection point)** nằm gần thiết bị để giảm độ trễ, lưu trữ và xử lý dữ liệu IoT.
   - **AI** khai phá dữ liệu từ IoT để tạo ra **insights** và điều phối ngược lại hành vi thiết bị (vd: trợ lý ảo thông minh).
2. **Blockchain + AI + Cloud:**
   - **Blockchain** cung cấp **nguồn chân lý phi tập trung, bất biến và đáng tin cậy** (*trusted, decentralized source of truth*), ghi nhận dữ liệu và biến số đầu vào giúp quyết định của AI minh bạch, giải trình được.
   - **AI** thực hiện phân tích và ra quyết định từ dữ liệu thu thập được.
   - **Cloud** cung cấp tài nguyên tính toán phân tán toàn cầu, mở rộng linh hoạt và tối ưu chi phí cho cả hai.

### B. Case studies công nghệ mới nổi trên Cloud
- **Welgevonden (Nam Phi — IoT):** Gắn cảm biến IoT kết nối Cloud lên ngựa vằn và linh dương để phát hiện hướng chạy trốn khi có kẻ săn trộm tê giác, cảnh báo kiểm lâm kịp thời.
- **USTA / US Open (AI):** Dùng IBM Cloud + Watson mở rộng đáp ứng mức tăng **5.000% lưu lượng web**, chạy Slam Tracker phân tích hơn 26 triệu điểm dữ liệu và AI Highlights tự động cắt ghép video theo tiếng reo hò.
- **Nông trại rau diếp Salinas (Blockchain):** Truy xuất nguồn gốc lô hàng trong vài giây khi có đợt thu hồi thực phẩm, tránh phải tiêu hủy toàn bộ kệ hàng lành mạnh.
- **KONE (Analytics & IoT):** Thu thập dữ liệu thang máy/thang cuốn phục vụ **hơn 1 tỷ người/ngày**, xử lý theo kiến trúc hướng sự kiện với **Cloud Functions** để làm **bảo trì dự đoán (predictive maintenance)**.

## 7. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm lẫn các đặc tính NIST:** *Resource pooling* (multi-tenant) là yếu tố trực tiếp tạo **tiết kiệm chi phí nhờ phục vụ nhiều khách hàng**; đừng nhầm với *On-demand self-service* (tự cấp phát 24/7) hay *Broad network access* (truy cập qua mạng).
2. **Hiểu sai vai trò của Cloud vs. AI trong IoT:** Cloud cung cấp hạ tầng **thu thập, lưu trữ và xử lý** dữ liệu IoT; còn **rút ra insights** (*draws insights*) từ dữ liệu đó là vai trò của **AI / Analytics**.
3. **Biệt hóa giữa rủi ro Cloud và rủi ro không lên Cloud:** *Data security*, *Compliance issues*, *Lack of standardization* là rủi ro khi **vận hành Cloud**; còn **thiếu tốc độ, đổi mới và năng lực ra quyết định** là rủi ro khi **không tích hợp Cloud vào chiến lược**.
4. **Đừng nhầm Hypervisor với Scaling:** Nhiệm vụ cốt lõi của Hypervisor là **cho phép nhiều hệ điều hành chạy song song trên 1 máy vật lý và tách biệt logic các VM**, không phải tự động scale workload.

## 8. Điểm cốt lõi cần nhớ (Key Takeaways)

- **NIST Cloud:** 5 đặc tính (*On-demand self-service, Broad network access, Resource pooling, Rapid elasticity, Measured service*).
- **Nền tảng lịch sử:** Time-sharing trên mainframe thập niên 1950 → VM thập niên 1970 → Hypervisor → Pay-as-you-go (CapEx → OpEx).
- **Tam giác IoT–AI–Cloud & Blockchain–AI–Cloud:** IoT tạo dữ liệu / Blockchain bảo chứng sự thật phi tập trung; AI tạo phân tích & quyết định; Cloud cấp tài nguyên lưu trữ & tính toán phân tán toàn cầu.
- **Nhà cung cấp tiêu biểu:** Salesforce dẫn đầu SaaS CRM; Oracle mạnh về Data Cloud & SaaS; GCP chạy Search/YouTube/App Engine trên chính hạ tầng của mình; IBM + Red Hat nhấn mạnh Hybrid Cloud.
