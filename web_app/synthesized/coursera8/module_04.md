# Module 4: Emergent Trends and Practices

> **Tư tưởng cốt lõi:** Điện toán đám mây hiện đại đang hội tụ quanh ba xu hướng kiến trúc — **Hybrid Multicloud**, **Microservices** và **Serverless** — kết hợp cùng phương pháp **Cloud Native**, quy trình **DevOps (CI/CD/CM)** và **Application Modernization** (chuyển đổi đồng bộ cả Kiến trúc, Hạ tầng và Cách thức làm việc).

## 1. Hybrid Multicloud: Chiến lược liên thông đa đám mây

- **Hybrid Cloud:** Kết nối **Private Cloud tại chỗ (on-premises)** với **Public Cloud của bên thứ ba** thành một hạ tầng thống nhất.
- **Multi-cloud:** Chiến lược áp dụng Cloud kết hợp nhiều mô hình dịch vụ (Public, Private, Managed) từ **nhiều nhà cung cấp khác nhau** (vd: Email từ hãng A, CRM từ hãng B, hạ tầng từ hãng C) nhằm **tránh vendor lock-in** và tự do di chuyển workload.
- **Hybrid Multicloud:** Khai thác thế mạnh của cả Hybrid và Multi-cloud để ứng dụng chạy xuyên suốt liền mạch qua hạ tầng on-prem, private và nhiều public cloud.

### 4 Use cases điển hình của Hybrid Multicloud
| Use case | Bài toán & Cách giải quyết (qua ví dụ trong bài giảng) |
| --- | --- |
| **1. Cloud Scaling** | Dịch vụ giao hoa gặp đỉnh tải theo mùa lễ hội → mở rộng tự động lên Public Cloud khi tăng tải và thu hồi tài nguyên khi hết lễ, tránh đầu tư phần cứng on-prem dư thừa |
| **2. Composite Cloud** | Phân tán các thành phần của **cùng một ứng dụng** qua nhiều môi trường/vùng địa lý (vd: Web UI, Billing API, Rewards đặt phân tán để đáp ứng lưu lượng và quy định khu vực như EU) |
| **3. Application Modernization** | Ngành hàng không kết nối hệ thống đặt vé/vận hành legacy với các dịch vụ Cloud mới để hiện đại hóa từng phần |
| **4. Data & AI** | Hãng hàng không kết nối dữ liệu lịch sử bảo trì khổng lồ (chiếm 30% nguyên nhân trễ chuyến) với dịch vụ Machine Learning/AI trên Cloud để thực hiện **predictive analytics** |

## 2. Kiến trúc Microservices: Chia nhỏ để tăng tốc & co giãn độc lập

**Microservices architecture** là cách tiếp cận trong đó **một ứng dụng duy nhất (single application)** được cấu thành từ nhiều thành phần nhỏ **liên kết lỏng lẻo (loosely coupled)** và **triển khai độc lập (independently deployable)**.

| Tiêu chí | Monolithic Architecture | Microservices Architecture |
| --- | --- | --- |
| **Cấu trúc** | Một khối phần mềm khổng lồ gắn chặt UI, business logic và data layer trên cùng codebase | Phân rã ứng dụng lớn thành các **core functions** đơn nhiệm (vd: Search, Recommendations, Product Catalog) |
| **Công nghệ & Đóng gói** | Dùng chung 1 tech stack cho toàn bộ ứng dụng | Mỗi microservice tự chọn tech stack, runtime riêng; thường đóng gói trong **Containers** (cắm-và-chạy / *plug-and-play*) |
| **Giao tiếp** | Gọi hàm nội bộ trong cùng tiến trình | Kết hợp **3 phương thức**: **APIs**, **Event Streaming**, và **Message Brokers** |
| **Mở rộng & Cập nhật** | Phải scale và build lại cả khối; một lỗi nhỏ có thể ảnh hưởng toàn bộ app | Scale độc lập từng dịch vụ chịu tải cao; cập nhật song song (như dịch vụ Dream Game nâng cấp *Recommendations* mà *Search* không gián đoạn) |

## 3. Serverless Computing: Trừu tượng hóa máy chủ tới từng hàm (FaaS)

**Serverless** KHÔNG có nghĩa là không có máy chủ — mà là **chuyển giao toàn bộ trách nhiệm quản trị hạ tầng phổ thông** (provisioning, scaling, scheduling, patching OS/runtime) cho nhà cung cấp Cloud để lập trình viên chỉ tập trung viết business logic.

- **Cơ chế hoạt động:** Mã nguồn chạy dưới dạng các hàm đơn lẻ bên trong **stateless container**; chỉ thực thi **on-demand theo từng request/sự kiện**, tự scale trong suốt và **không tính phí thời gian nhàn rỗi (never pay for idle capacity)** (khác hoàn toàn VM tính phí liên tục miễn là VM còn bật).
- **Nền tảng tiêu biểu:** **IBM Cloud Functions** (dựa trên Apache OpenWhisk), **AWS Lambda**, **Microsoft Azure Functions**.

| Phù hợp với Serverless | KHÔNG phù hợp với Serverless (Giới hạn & Rủi ro) |
| --- | --- |
| Hàm **stateless chạy ngắn hạn** (vài giây hoặc vài phút) | **Tác vụ chạy dài hạn (long-running processes)** — dùng server truyền thống đơn giản & rẻ hơn |
| Workload có **tính mùa vụ** với thời gian nhàn rỗi (idle time) lớn | Ứng dụng đòi hỏi **độ trễ cực thấp tuyệt đối** (vd: giao dịch tài chính) do **cold start** (khởi động từ số 0) |
| **Xử lý sự kiện bất đồng bộ**, **stream processing** (IoT, log, market data), chuyển đổi dữ liệu (PDF, audio, thumbnail, video transcoding) và **microservices dạng stateless** | Hệ thống nhạy cảm với **vendor lock-in** (phụ thuộc auth, scaling, monitoring của nền tảng serverless) |

## 4. Cloud Native Applications & Tầng hạ tầng dịch vụ

**Cloud Native Application** là ứng dụng được thiết kế ngay từ đầu cho Cloud (hoặc refactor theo chuẩn Cloud Native), **cấu thành từ các Microservices** đóng gói trong **Containers** và vận hành tự động qua **Orchestration (Kubernetes, OpenShift, Knative, Istio)**.

### 3 Nguyên tắc phát triển Cloud Native cốt lõi
1. Áp dụng kiến trúc **Microservices** — tách ứng dụng thành các dịch vụ đơn chức năng.
2. Đóng gói **Containers** để đạt tính linh hoạt, mở rộng và di động (*portability*) tối đa.
3. Áp dụng phương pháp **Agile** — cải tiến lặp nhanh dựa trên phản hồi người dùng.

### Dịch vụ cấp hệ thống bắt buộc trong hệ sinh thái Microservices
Vì hệ thống microservices có rất nhiều thành phần chuyển động (*moving parts*), ứng dụng Cloud Native cần chuẩn hóa logging/events, *distributed tracing* và tận dụng 3 dịch vụ lõi ở tầng điều phối (như **Istio / Knative**):
- **Load Balancing** (cân bằng tải)
- **Service Discovery** (tạo "bản đồ định vị" để các microservices tìm thấy và giao tiếp với nhau)
- **Routing** (định tuyến yêu cầu)

## 5. DevOps trên Cloud & Mối quan hệ cộng sinh (Symbiotic Relationship)

**DevOps** kết hợp Development + Operations + QA + Business Owners cùng nguyên lý Agile/Lean để phân phối phần mềm liên tục với tốc độ và độ tin cậy cao. **DevOps và Cloud có mối quan hệ cộng sinh (symbiotic relationship)**: Cloud cung cấp hạ tầng lập trình được gần như vô hạn, còn DevOps cung cấp tự động hóa và quy trình để kiểm soát độ phức tạp của Cloud.

| Thành phần quy trình DevOps | Cơ chế kỹ thuật & Công cụ tiêu biểu |
| --- | --- |
| **Continuous Integration (CI)** | Hợp nhất code thường xuyên vào repo chung (Git); tạo bản build đóng gói thành **immutable images** — **mọi sửa đổi đều phải thay thế toàn bộ component bằng phiên bản mới** chứ không vá trực tiếp |
| **Continuous Delivery (CD)** | Giữ mã nguồn luôn ở trạng thái sẵn sàng phát hành bất kỳ lúc nào với can thiệp thủ công tối thiểu (Jenkins, Bamboo) |
| **Continuous Deployment (CDep)** | Tự động đẩy thẳng các bản build đạt kiểm thử qua toàn bộ vòng đời lên môi trường production nhanh nhất có thể |
| **Continuous Monitoring (CM)** | Theo dõi hiệu năng & tính sẵn sàng theo thời gian thực ngay cả trước khi lên production (Prometheus, ELK Stack) |
| **Delivery Pipeline** | Chuỗi bước tự động khép kín: `Ideation → Coding → Building → Deploying → Managing → Continuous Improvement` |

**Dịch vụ DevOps trên các Cloud lớn:** AWS (*CodePipeline, Elastic Beanstalk, Lambda*), Azure (*Azure DevOps, AKS, Azure Functions*), GCP (*Cloud Build, GKE, Cloud Functions*), IBM Cloud (*Continuous Delivery, IKS, IBM Functions*).

## 6. Application Modernization (AppMod): 3 Chuyển đổi đồng thời

Hiện đại hóa ứng dụng đòi hỏi doanh nghiệp phải thực hiện **đồng bộ cả 3 trục chuyển đổi** (nếu chỉ đổi 1 trục sẽ không phát huy hiệu quả):

```text
1. Kiến trúc (Architecture):   Monolith / SOA   ──►  Microservices
2. Hạ tầng (Infrastructure):   Physical / VMs   ──►  Cloud Infrastructure (Containers / Serverless)
3. Cách làm việc (Delivery):   Waterfall / Agile──►  DevOps & SRE (Programmable Infrastructure)
```

- **Tại sao DevOps là mắt xích sống còn của AppMod?** Vì DevOps cung cấp **hạ tầng lập trình được (programmable infrastructure)** hỗ trợ tốc độ triển khai, khả năng phục hồi (*resiliency*) và dựng nhanh môi trường test giống hệt production.

## 7. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Đừng nhầm Serverless với "Không có Server":** Serverless **không loại bỏ server khỏi môi trường**, mà chỉ **chuyển giao trách nhiệm quản trị hạ tầng** (*offloads responsibility for common infrastructure management tasks*) cho nhà cung cấp.
2. **3 phương thức giao tiếp Microservices:** Nhớ chính xác bộ ba **APIs, Event Streaming, và Message Brokers** (không phải *cloud monitoring* hay *cloud encryption*).
3. **Bản chất của Immutable Images trong CI:** Vì image là bất biến (*immutable*), khi cần chỉnh sửa, bạn **phải thay thế toàn bộ component** (*replacing the entire component*), tuyệt đối không patch trực tiếp lên deployment đang chạy.
4. **3 dịch vụ cấp hệ thống cho Cloud Native Microservices:** Bộ ba chuẩn trong bài giảng là **Load balancing, Service discovery, và Routing** (nhờ Istio/Knative).

## 8. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Microservices:** Một **single application** gồm nhiều dịch vụ nhỏ **loosely coupled**, triển khai độc lập, giao tiếp qua **APIs + Event streaming + Message brokers**.
- **Serverless:** Stateless, chạy theo request/event, không trả tiền khi idle; **tránh dùng cho long-running processes** và tác vụ siêu nhạy cảm cold-start.
- **Cloud Native:** Cấu thành từ **Microservices** (đóng gói trong Containers), vận hành bằng **DevOps** (mối quan hệ **symbiotic** với Cloud).
- **Application Modernization toàn diện:** Dịch chuyển đồng thời từ **Monolith/SOA → Microservices**, **Physical/VM → Cloud**, và **Waterfall/Agile → DevOps**.
