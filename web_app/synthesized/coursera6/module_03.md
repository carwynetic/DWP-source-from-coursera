# Module 3: Serverless Overview

> **Tư tưởng cốt lõi:** Theo CNCF, **Serverless** là mô hình xây dựng và vận hành ứng dụng **không cần quản lý máy chủ (server management)**, kết hợp **FaaS (Function-as-a-Service)** và **BaaS (Backend-as-a-Service)** để tự động mở rộng theo sự kiện và chỉ tính phí theo từng lần thực thi — nhưng cần đánh đổi với các giới hạn như **cold-start latency**, **statelessness**, **vendor lock-in** và gỡ lỗi phân tán phức tạp.

## 1. Bản chất của Serverless Computing (FaaS + BaaS)

- **Định nghĩa của CNCF (Cloud Native Computing Foundation):** Serverless là khái niệm xây dựng và chạy ứng dụng **không đòi hỏi quản lý máy chủ (server management)**; ứng dụng được đóng gói thành một hoặc nhiều hàm (functions), tải lên nền tảng và tự động thực thi, mở rộng (kể cả **scale-to-zero**), và tính phí đúng theo nhu cầu thực tế tại thời điểm chạy.
- **Công thức kiến trúc Serverless:** **`Serverless Stack = FaaS + BaaS + API Gateway`**
  - **FaaS (Function-as-a-Service):** Dịch vụ điện toán đám mây cho phép **thực thi mã nguồn (functions) phản hồi theo sự kiện (event-driven)** mà không cần cấp phát hạ tầng phức tạp. Đặc trưng cốt lõi của một hàm FaaS là **stateless (không lưu trạng thái cục bộ), ngắn hạn (ephemeral/short-lived) và kích hoạt theo sự kiện**.
  - **BaaS (Backend-as-a-Service):** Các dịch vụ đám mây được quản lý sẵn như cơ sở dữ liệu (DynamoDB, Cloudant), lưu trữ đối tượng (S3, COS), xác thực người dùng (Cognito), hàng đợi tin nhắn (Kafka/SQS).

### Phân chia trách nhiệm trong mô hình Serverless

| Trách nhiệm của Nhà cung cấp Cloud (Cloud Provider) | Trách nhiệm của Bạn (Developer / User) |
| --- | --- |
| - Cấp phát & bảo trì **phần cứng / máy chủ vật lý**<br>- Cài đặt & vá lỗi **hệ điều hành, runtime, mạng**<br>- **Tự động mở rộng (auto-scaling)**, chịu lỗi (fault tolerance) và tính sẵn sàng cao (HA) | - Viết và quản lý **mã nguồn ứng dụng (application code & business logic)**<br>- Cấu hình sự kiện kích hoạt (triggers), quyền truy cập (IAM) và dữ liệu ứng dụng |

## 2. Ưu điểm vs. Giới hạn (Pros & Cons) của Serverless

| Ưu điểm nổi bật (Benefits) | Giới hạn & Thách thức (Constraints) |
| --- | --- |
| - **Pay-per-request / Pay-as-you-go:** Chỉ trả tiền khi hàm thực sự chạy, không tốn phí máy chủ nhàn rỗi | - **Cold-start latency:** Độ trễ khởi động khi hàm ngủ dậy → **không phù hợp ứng dụng thời gian thực nhạy độ trễ cực cao (time-critical apps)** |
| - **Built-in High Availability & Auto-scaling:** Tự động co giãn từ 0 đến hàng trăm nghìn request/giây | - **No State Persistence (Stateless):** Không giữ trạng thái trong RAM giữa các lần gọi (phải lưu ngoài vào DB/Cache) |
| - **Giảm thời gian ra thị trường (Faster Time-to-Market):** Đội ngũ tập trung hoàn toàn vào logic nghiệp vụ | - **Vendor Lock-in:** Dễ bị ràng buộc vào dịch vụ & cấu hình riêng của từng nhà cung cấp Cloud<br>- **Giám sát & Debug phức tạp** hơn do kiến trúc phân tán theo sự kiện |

## 3. Serverless Framework & Kiến trúc tham chiếu (Reference Architecture)

- **The Serverless Framework:** Framework mã nguồn mở viết bằng **Node.js** cung cấp CLI chuẩn hóa để định nghĩa và triển khai tự động các kiến trúc hướng sự kiện lên AWS Lambda, Azure Functions, Google Cloud Functions và Apache OpenWhisk.
  - Đơn vị thực thi và triển khai độc lập nhỏ nhất trong Serverless Framework là một **`function`** (mỗi function thực hiện 1 tác vụ đơn lẻ, tương tự microservice).
- **Kiến trúc tham chiếu Web App (ví dụ To-Do App trên AWS):**
  - **Front-End (hosted trên AWS Amplify / CDN):** Chịu trách nhiệm phục vụ toàn bộ **nội dung tĩnh** (HTML, CSS, JavaScript/React, hình ảnh) và giao diện tương tác người dùng.
  - **Back-End Serverless:** API Gateway → AWS Lambda (FaaS xử lý CRUD) → DynamoDB (BaaS lưu dữ liệu) + Amazon Cognito (quản lý định danh user).
- **Các tình huống ứng dụng điển hình (Use Cases):**
  - **Event Streaming:** Thu thập dữ liệu thời gian thực từ cảm biến IoT/clickstream, lọc/biến đổi luồng dữ liệu tức thì và kích hoạt cảnh báo hoặc ghi vào kho dữ liệu.
  - **Post-Processing (Xử lý hậu kỳ bất đồng bộ):** Tự động **tạo ảnh thu nhỏ (thumbnail generation)**, chuyển đổi định dạng video, hoặc quét virus ngay khi người dùng tải tệp lên Object Storage.

## 4. So sánh các nền tảng Serverless phổ biến

| Nền tảng | Nhà cung cấp / Dự án gốc | Điểm khác biệt nổi bật |
| --- | --- | --- |
| **AWS Lambda** | Amazon Web Services | Hệ sinh thái lớn nhất (tích hợp >200 dịch vụ AWS), tính phí theo lượt chạy & truyền dữ liệu |
| **Google Cloud Functions** | Google Cloud Platform | Trải nghiệm lập trình đơn giản, tự động scale-to-zero tức thì |
| **IBM Cloud Functions** | IBM (dựa trên mã nguồn mở **Apache OpenWhisk**) | Nền tảng FaaS mở (giảm vendor lock-in), tích hợp mượt với hệ sinh thái IBM Cloud & Watson |
| **Knative** | **Google** (khởi xướng & đóng góp cộng đồng mã nguồn mở, nay thuộc CNCF) | Nền tảng chạy workload Serverless **ngay trên Kubernetes** (scale-to-zero, eventing, serving) — nền tảng cốt lõi đứng sau **IBM Cloud Code Engine** |

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Serverless = **FaaS + BaaS** (cộng thêm API Gateway), giải phóng lập trình viên khỏi **server management** để chỉ tập trung vào **application code**.
- Trong mô hình FaaS, hàm là **stateless, event-driven**, là đơn vị triển khai độc lập (`function`) trong **Serverless Framework** (viết bằng **Node.js**).
- Nắm rõ các giới hạn: **độ trễ (cold start)** không hợp tác vụ tối mật về thời gian thực, **không lưu state cục bộ**, **vendor lock-in**, và **debug/monitoring phức tạp**.
- **Knative** do **Google** phát triển cho Kubernetes; **IBM Cloud Functions** xây dựng trên mã nguồn mở **Apache OpenWhisk**.
