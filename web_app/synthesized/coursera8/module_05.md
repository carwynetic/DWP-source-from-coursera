# Module 5: Cloud Security, Monitoring, Case Studies, Jobs

> **Tư tưởng cốt lõi:** Bảo mật Cloud vận hành theo **Shared Responsibility Model** với **IAM là phòng tuyến đầu tiên (First Line of Defense)** và **Cloud Encryption là phòng tuyến cuối cùng (Last Line of Defense)**; kết hợp **Cloud Monitoring** toàn diện (Metrics, Logs, Alarms, Events, API Audit Trails) để duy trì tính sẵn sàng, tối ưu chi phí và thúc đẩy chuyển đổi số doanh nghiệp.

## 1. Thách thức Bảo mật Cloud & Shared Responsibility Model

### A. Thách thức & Mối đe dọa đặc trưng trên Cloud
- **4 thách thức kiến trúc:** (1) Thiếu tầm nhìn (*lack of visibility*) trên Public Cloud, (2) Rủi ro **multitenancy** (bị vạ lây khi kẻ tấn công nhắm vào tenant khác cùng hạ tầng), (3) Quản lý truy cập & **Shadow IT**, (4) **Misconfigurations** (cấu hình sai quyền riêng tư, giữ mật khẩu mặc định — nguyên nhân hàng đầu gây lộ dữ liệu; được giải quyết nhờ **CSPM — Cloud Security Posture Management**).
- **Các mối đe dọa phổ biến:**
  - **Insider Threats:** Nhân viên cũ/hiện tại, đối tác lạm dụng quyền truy cập hợp pháp (vô hình trước tường lửa ngoài).
  - **DDoS (Distributed Denial-of-Service):** Làm quá tải máy chủ bằng lưu lượng khổng lồ từ nhiều hệ thống đồng bộ (thường lợi dụng giao thức **SNMP**; phòng chống bằng *AWS Shield*, *Google Cloud Armor*).
  - **Data Breach:** Rò rỉ dữ liệu nhạy cảm gây thiệt hại tài chính và uy tín.

### B. Shared Responsibility Model (Mô hình Trách nhiệm Chia sẻ)
> **Nguyên tắc vàng:** Áp dụng mô hình trách nhiệm chia sẻ kết hợp **giám sát chủ động liên tục (active monitoring)** cho bảo mật và tuân thủ — không phải giám sát định kỳ thụ động (*periodic*).

| Lớp trách nhiệm | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| **Hạ tầng vật lý & Data Center** | Cloud Provider | Cloud Provider | Cloud Provider |
| **OS, Platform, Runtime, Subscriptions** | **Customer** | Cloud Provider | Cloud Provider |
| **Application Code & Dữ liệu tạo ra** | **Customer** | **Customer** | Cloud Provider *(CSP quản lý app & data)* |
| **Thông tin đăng nhập (Login credentials) & Access Policy** | **Customer** | **Customer** | **Customer** |

- **NIST Cybersecurity Framework (5 trụ cột):** **Identify → Protect → Detect → Respond → Recover**.

## 2. Identity and Access Management (IAM) — Phòng tuyến đầu tiên

Theo khảo sát Cybersecurity Insiders, mối lo số 1 là rò rỉ dữ liệu và lỗ hổng lớn nhất là truy cập trái phép qua lạm dụng thông tin xác thực. **IAM (Access Control)** là **first line of defense** giúp xác thực và phân quyền người dùng.

### A. 3 nhóm người dùng & 3 thành phần của Access Policy
- **3 loại người dùng:** **Administrative Users** (quản trị tạo/xóa tài nguyên, xem hoạt động nhóm — rủi ro cao nhất nếu bị chiếm quyền), **Developer Users** (đọc dữ liệu nhạy cảm, tạo/sửa/xóa app qua CLI/API), **Application Users** (người dùng cuối của ứng dụng).
- **Cấu trúc một Access Policy:** `Subject` (User / Service ID / Access Group) + `Target` (Tài nguyên / dịch vụ được cấp quyền) + `Role` (Hành động được phép thực hiện trên Target).
- **Lợi ích của Access Groups:** Gom nhóm các user và service ID có cùng nhu cầu để gán chung policy — **giảm số lượng policy trong tài khoản và chuẩn hóa việc cấp quyền**.

### B. Thành phần cốt lõi & Tiêu chuẩn IAM
- **Cloud Directory Services:** Quản lý an toàn **hồ sơ người dùng và thông tin xác thực (user profiles & credentials)** trên Cloud.
- **Audit and Compliance:** Xác thực các kiểm soát đã triển khai có tuân thủ đúng chính sách hay không.
- **Authentication & MFA:** Xác thực qua Cloud Directory, Social IdP hoặc Enterprise IdP (qua **SAML** trên nền XML cho SSO, hoặc **OpenID Connect** trên nền OAuth 2.0 dùng ID token); tăng cường bảo mật bằng **MFA** (TOTP, token, risk-based authentication) và **Principle of Least Privilege** (chỉ cấp quyền tối thiểu cần thiết).

## 3. Cloud Encryption — Phòng tuyến cuối cùng (Last Line of Defense)

- **Định nghĩa:** **Mã hóa (Encryption)** là quá trình xáo trộn dữ liệu khiến nó trở nên không thể đọc được (*illegible*). Một hệ thống mã hóa gồm **2 thành phần chính**: **Encryption Algorithm** (quy tắc biến đổi) và **Decryption Key** (chìa khóa giải mã).
- **3 trạng thái dữ liệu cần mã hóa:**
  1. **Encryption at rest:** Bảo vệ dữ liệu khi lưu trữ trên đĩa/CSDL (AES, Cloud KMS, Azure Key Vault).
  2. **Encryption in transit:** Bảo vệ dữ liệu khi truyền qua mạng bằng **SSL / TLS** (kể cả truyền nội bộ giữa các service trên Cloud).
  3. **Encryption in use:** Bảo vệ dữ liệu ngay khi đang xử lý tính toán trong bộ nhớ (*in memory*) mà không cần giải mã lộ nguyên bản.
- **Server-side vs. Client-side Encryption:**
  - *Server-side:* Mã hóa sau khi Cloud nhận dữ liệu nhưng trước khi ghi xuống đĩa (hỗ trợ *Customer-supplied keys* hoặc *Customer-managed keys* qua KMS — **BYOK / KYOK**).
  - *Client-side:* Mã hóa **trước khi gửi lên Cloud**, CSP không thấy key và gần như không thể giải mã dữ liệu.

> **Sự thật quan trọng về Encryption:** Mã hóa giúp chỉ người được ủy quyền mới đọc được dữ liệu (A), khiến dữ liệu bị đánh cắp trở nên vô nghĩa (B), và bảo vệ dữ liệu cả 3 trạng thái at rest/in transit/in use (C) — **NHƯNG mã hóa KHÔNG loại bỏ hoàn toàn rủi ro bảo mật dữ liệu (D sai)**; nó chỉ **tách rủi ro khỏi dữ liệu sang việc bảo vệ Encryption Keys**. Do đó phải lưu key tách biệt dữ liệu, sao lưu off-site, xoay vòng key định kỳ (*key rotation*) và bật MFA cho master/recovery keys.

## 4. Cloud Monitoring: Giám sát toàn diện & Theo dõi API

**Cloud Monitoring** đánh giá **3 lĩnh vực chính**: **Data, Applications, và Infrastructure** (xét trên hiệu năng, phân bổ tài nguyên, tính sẵn sàng mạng, tuân thủ và rủi ro bảo mật).

- **3 nhóm công cụ chính:** **Infrastructure monitoring**, **Database monitoring**, và **APM (Application Performance Monitoring)** (giúp đạt SLA, giảm downtime và chi phí).
- **Kỹ thuật cốt lõi:** Alarms (cảnh báo ngưỡng), Logs, Metrics (baseline), Events, **Infrastructure as Code (IaC) monitoring** (phát hiện *configuration drift*), và **Network Flow Logs + Security Events** (đánh giá security posture, compliance và threat).
- **Theo dõi API Calls để Audit (Audit Trail):** Ghi lại danh tính người gọi, thời gian, tham số:
  - AWS: **AWS CloudTrail** | GCP: **Cloud Audit Logging** | Azure: **Azure Activity Logs** | Salesforce: **Event Monitoring**.
- **Lợi ích & Best Practices:**
  - Tăng tốc chẩn đoán và xử lý sự cố hiệu năng, phát cảnh báo chủ động (*proactive notifications*) và gỡ lỗi (*troubleshoot*) ứng dụng/hạ tầng.
  - **Best practices:** Dùng **end-user experience monitoring** (đo hiệu năng từ góc nhìn người dùng cuối), **theo dõi mức dùng & chi phí tài nguyên Cloud**, gom private/public/hybrid về một nền tảng giám sát thống nhất, tự động hóa và diễn tập giả lập sự cố (*simulate outages & breaches*).

## 5. Case Studies Đa Ngành & Cơ hội Nghề nghiệp (Cloud Jobs)

| Doanh nghiệp / Ngành | Giải pháp Cloud & Thành quả nổi bật |
| --- | --- |
| **The Weather Company** | Di chuyển sang **IBM Cloud Kubernetes Services** → tận dụng data center địa phương giảm độ trễ và co giãn cực nhanh khi bão đổ bộ (từ 30 triệu lên >100 triệu người dùng, 250 tỷ dự báo/ngày, 150k req/s); giảm **80%** quy trình DevOps |
| **LiquidPower** | Tách khỏi công ty mẹ, chọn chạy **SAP trên Cloud** thay vì tự vận hành hạ tầng on-prem → triển khai nhanh, mở rộng dễ dàng |
| **Cementos Pacasmayo / Welch** | Ứng dụng Cloud để đạt xuất sắc vận hành, mở rộng thị trường và khai thác giá trị Hybrid Cloud |

### 6 Vai trò nghề nghiệp tiêu biểu trong kỷ nguyên Cloud (CAGR 14.1%, đạt $1,554.94 tỷ năm 2030)
1. **Cloud Developer / Cloud Software Engineer:** Phát triển front-end/back-end trên Cloud (Python, JS, Java, SQL/NoSQL, hệ thống phân tán).
2. **Cloud Integration Specialist:** Tích hợp hệ thống nội bộ và dịch vụ Cloud mới, đảm bảo chuẩn SLA.
3. **Cloud Data Engineer:** Thiết kế, triển khai data pipelines mở rộng kết nối nguồn dữ liệu tới mô hình AI/ML.
4. **Cloud Security Engineer:** Bảo vệ mọi tầng hạ tầng, IAM, mã hóa, phát hiện mối đe dọa.
5. **Cloud DevOps Engineer:** Tự động hóa CI/CD, containerization (Docker, Kubernetes), tối ưu độ tin cậy vận hành.
6. **Cloud Solutions Architect:** Chuyển hóa yêu cầu kinh doanh thành kiến trúc Cloud toàn diện (am hiểu thiết kế phần mềm, mạng, bảo mật, DevOps).

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Encryption KHÔNG "eliminates data security risk":** Bất kỳ đáp án nào khẳng định mã hóa xóa bỏ hoàn toàn rủi ro bảo mật đều **SAI**. Chỉ chọn A, B, C (bảo vệ at rest, in transit, in use và làm dữ liệu bị chặn trở nên vô nghĩa).
2. **Active Monitoring vs. Periodic Monitoring:** Để bảo vệ Cloud, phải áp dụng **Shared Responsibility Model** và **Active (continuous) monitoring** — không phải chạy công cụ kiểm tra định kỳ (*periodic basis*).
3. **Phân biệt IAM vs. Encryption vs. Monitoring:**
   - **Cloud Directory Services + Audit & Compliance** thuộc **IAM**.
   - **End-user experience monitoring + Track usage and cost** là best practice của **Cloud Monitoring** (không phải xác thực user hay mã hóa).
   - **Flow logs + Security events** giúp theo dõi posture, compliance và threats (không phải hypervisors).
4. **The Weather Company vs. American Airlines:** *The Weather Company* hưởng lợi từ **giảm độ trễ nhờ data center địa phương và co giãn xử lý đột biến lưu lượng (elasticity)**; còn *phát hành app nhanh và công cụ tự phục vụ* là case study của **American Airlines**.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- **3 lĩnh vực Cloud Monitoring đánh giá:** **Data, Applications, Infrastructure**.
- **2 thành phần hệ thống mã hóa:** **Encryption Algorithm + Decryption Key**; bảo vệ 3 trạng thái **at rest, in transit (SSL/TLS), in use**.
- **Access Groups** giảm số lượng policy trong tài khoản và cấp quyền nhất quán cho nhóm users/service IDs.
- **Cloud Computing** là trụ cột của chiến lược **chuyển đổi số (digital transformation)** doanh nghiệp.
