# Module 1: Introduction to Application Development

> **Tư tưởng cốt lõi:** Phát triển ứng dụng Web và Cloud chia thành hai mặt trận phối hợp chặt chẽ: **Front-end (Client-side)** kiến tạo giao diện & trải nghiệm người dùng bằng HTML/CSS/JavaScript và **Back-end (Server-side)** xử lý nghiệp vụ, xác thực, API và cơ sở dữ liệu; kết nối với nhau qua vòng đời SDLC chuẩn mực gồm Version Control (Git), Libraries/Frameworks, Build Tools, Package Managers và quy trình CI/CD tự động hóa.

## 1. Kiến trúc Web & Cloud Application: Client-Side vs. Server-Side

Khi người dùng nhập URL (như `www.ibm.com`) vào trình duyệt (Chrome, Edge, Firefox, Safari), trình duyệt gửi yêu cầu (HTTP request) tới máy chủ (server). Máy chủ trả về dữ liệu để trình duyệt dựng trang web:
- **Nội dung tĩnh (Static Content):** Tài nguyên được lưu sẵn trên server và gửi nguyên trạng về client (HTML thuần, ảnh, file CSS).
- **Nội dung động (Dynamic Content):** Dữ liệu được sinh hoặc tổng hợp theo từng yêu cầu của người dùng, thường truy vấn từ cơ sở dữ liệu (database) hoặc dịch vụ Back-end khác. Phần lớn website kết hợp cả tĩnh và động.
- **Cloud Applications:** Hoạt động tương tự website nhưng gắn trực tiếp với hạ tầng Back-end, lưu trữ và xử lý trên Cloud (như Cloud Functions/Serverless), mang lại khả năng mở rộng (**scalability**) và phục hồi (**resilience**) vượt trội.

### So sánh vai trò Front-End, Back-End & Full-Stack

| Vai trò | Phạm vi & Trách nhiệm chính | Ngôn ngữ & Công nghệ tiêu biểu |
| --- | --- | --- |
| **Front-End Developer** | Mọi thứ chạy ở **client-side** (trình duyệt): cấu trúc, giao diện, tương tác, khả năng hiển thị trên desktop & mobile (*responsive design*) | **HTML, CSS** (SASS/LESS, Bootstrap), **JavaScript** (React.js, Vue.js, Angular, jQuery, Backbone.js) — *không yêu cầu Java* |
| **Back-End Developer** | Mọi thứ chạy ở **server-side**: logic nghiệp vụ, **API** cung cấp dữ liệu, **xác thực & phân quyền** (authentication/authorization), **làm việc với Database (SQL/NoSQL) & ORM** | **Python** (Django, Flask), **Node.js / Express.js** (JavaScript chạy trên V8 engine đơn luồng bất đồng bộ), Java (Spring), Ruby (Rails), PHP, Elixir (Phoenix) |
| **Full-Stack Developer** | Thành thạo cả Front-End lẫn Back-End; có thể tự xử lý xuyên suốt từ nút bấm UI đến API xác thực và truy vấn database | Kết hợp cả hai hệ sinh thái cùng kỹ năng **Git/GitHub**, IDE (**VS Code**) & Cloud deployment |

> **API & ORM trong Back-End:** **API** (*Application Programming Interface*) là đoạn mã xử lý dữ liệu và cung cấp cơ chế để phần mềm truy cập tài nguyên từ Back-end. Ngoài **SQL**, lập trình viên dùng **ORM** (*Object-Relational Mapping*) để ánh xạ bảng CSDL thành đối tượng OOP giúp truy vấn an toàn và nhanh hơn.

## 2. Bộ công cụ của Lập trình viên (Developer Workbench)

### A. Code Editors, IDEs & Linters

- **Code Editor & IDE:** Công cụ soạn thảo, tích hợp, build, biên dịch và debug mã nguồn (như **VS Code**, Sublime Text, Atom, Vim, Visual Studio, Eclipse, NetBeans; trên server terminal dùng `vi`/`nano`).
- **Auto-formatting & Linting:** Các extension như **Prettier** và **ESLint** (hoặc **XO**) giúp chuẩn hóa phong cách code theo nhóm, phát hiện lỗi sớm và giảm xung đột khi merge trên Git.

### B. Version Control Systems (VCS — Git & GitHub)

- Hệ thống quản lý phiên bản (như **Git**) theo dõi chính xác **3 thông tin**: **(1) Thay đổi gì đã được thực hiện**, **(2) Ai thực hiện**, và **(3) Thực hiện khi nào**, đồng thời hỗ trợ phân nhánh (*branching*), hoàn tác (*revert*) và giải quyết xung đột (*conflict resolution*).
- *Lưu ý:* **Git là công cụ quản lý phiên bản**, giúp theo dõi lịch sử thay đổi chứ **không phải** công cụ debug lỗi code và cũng **không phải** development framework.

### C. Libraries vs. Frameworks — Quyền kiểm soát thuộc về ai?

| Tiêu chí | Code Library (Thư viện) | Application Framework (Khung ứng dụng) |
| --- | --- | --- |
| **Bản chất** | Tập hợp các hàm/chương trình con giải quyết một tác vụ cụ thể | Bộ khung kiến trúc hoàn chỉnh định nghĩa luồng chạy của toàn ứng dụng |
| **Quyền điều khiển** | **Lập trình viên gọi thư viện** khi cần (*You call the library*) | **Framework gọi code của bạn** theo quy ước sẵn có — gọi là **Inversion of Control (IoC)** |
| **Tính linh hoạt** | Linh hoạt cao; có thể tích hợp nhiều thư viện vào dự án bất kỳ lúc nào | Kém linh hoạt hơn (*opinionated*), phải chọn ngay từ đầu dự án |
| **Ví dụ điển hình** | **jQuery** (DOM), **Axios** (HTTP requests), `email-validator`, Apache Commons | **Angular**, **Vue.js**, **Django**, **Flask**, Express.js, Ruby on Rails, Spring *(React.js là thư viện UI)* |

## 3. Build Tools, Package Managers & Quy trình CI/CD

```text
[Viết Code & Commit] --> [CI: Tự động Build + Chạy Test] --> [CD: Đóng gói & Triển khai lên Staging/Production]
```

- **CI/CD (Continuous Integration / Continuous Delivery & Deployment):**
  - **CI (Tích hợp liên tục):** Tự động **build và chạy test** mã nguồn mỗi khi lập trình viên tích hợp thay đổi (hàng giờ/hàng ngày) để đảm bảo các thành phần phối hợp trơn tru.
  - **CD (Chuyển giao/Triển khai liên tục):** Bắt đầu ngay sau khi CI kết thúc, tự động triển khai bản build đã vượt qua kiểm thử lên môi trường *testing*, *staging* hoặc *production*.
- **Build Automation Tools:** Tự động hóa các tác vụ: **tải dependencies**, **biên dịch mã nguồn thành mã nhị phân (binary)**, **đóng gói binary code**, **chạy test** và **triển khai lên production** (vd: **Webpack** — module bundler, **Babel** — JS compiler, **WebAssembly**). *(Cẩn thận bẫy: Build tool biên dịch source code thành binary, KHÔNG phải biên dịch binary thành source code!)*
- **Packages vs. Package Managers:**
  - **Package:** File nén chứa các tệp ứng dụng, hướng dẫn cài đặt và metadata (phiên bản, mô tả, dependencies).
  - **Package Manager:** Công cụ **phân phối ứng dụng đã đóng gói**, tự động **tìm kiếm, cài đặt, cập nhật, gỡ bỏ** gói phần mềm, kiểm tra checksum/chữ ký số và giải quyết dependencies:
    - Ngôn ngữ: **npm** (Node.js/JS), **pip / conda** (Python), **Maven / Gradle** (Java), **RubyGems** (Ruby).
    - Hệ điều hành: **DPKG / RPM** (Linux), **Homebrew / MacPorts** (macOS), **Chocolatey** (Windows).

## 4. Vòng đời phát triển Web (Web Development Lifecycle)

1. **Conception & Architecture:** Thiết kế tư duy (*design thinking*), lấy yêu cầu người dùng, chọn kiến trúc & dịch vụ Cloud phù hợp.
2. **Development:** Phân công Front-end / Back-end, lập kế hoạch sprint, viết code với IDE, linter và Git.
3. **Testing (QA):** Kiểm thử đơn vị (*unit test*), tích hợp (*integration test*) và sửa lỗi.
4. **Deployment:** Tự động hóa phát hành qua CI/CD lên môi trường thực tế.
5. **Maintenance:** Giai đoạn tối quan trọng nhưng dễ bị xem nhẹ — giám sát, vá lỗi và nâng cấp liên tục.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm lẫn vai trò giữa Front-End và Back-End khi xử lý sự cố:** Lỗi hiển thị lệch trên mobile vs desktop do **Front-end Developer** xử lý; lỗi xác thực đăng nhập (*authentication failure*) hoặc truy vấn CSDL do **Back-end** hoặc **Full-stack Developer** xử lý.
2. **Nhầm `Package` với `Package Manager`:** File chứa app + hướng dẫn cài đặt + metadata là **Package**; còn công cụ tìm, cài đặt, bảo trì, gỡ bỏ và phân phối gói mới là **Package Manager**.
3. **Nhầm lẫn chiều biên dịch của Build Automation:** Build tool biên dịch *source code $\rightarrow$ binary code*, không phải *binary $\rightarrow$ source*.
4. **Đánh đồng Git là một Framework:** **Git** là hệ thống quản lý phiên bản (VCS), không phải framework như Angular, Vue.js hay Django.
5. **Nhầm vai trò giữa CI và CD:** **CI** chịu trách nhiệm tự động **build & test**; **CD** chịu trách nhiệm tự động **deploy** bản build sau khi CI thành công.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **HTML** tạo cấu trúc, **CSS** định dạng giao diện, **JavaScript** tạo tương tác động ở Front-end và cũng chạy được ở Back-end nhờ **Node.js** (V8 engine, kiến trúc đơn luồng bất đồng bộ).
- Framework áp dụng **Inversion of Control** (framework gọi code của bạn), khác với Library (bạn chủ động gọi thư viện).
- Hệ sinh thái Front-End nổi bật: **React.js, Vue.js, Angular**; Back-End nổi bật: **Node.js, Express, Django, Flask**.
- VCS theo dõi **cái gì thay đổi, ai sửa, sửa khi nào**; CI/CD + Build Tools + Package Managers đảm bảo vòng đời giao hàng phần mềm nhanh và đáng tin cậy.