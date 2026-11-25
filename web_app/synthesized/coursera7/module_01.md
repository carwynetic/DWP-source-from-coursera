# Module 1: Application — Static Pages (Best Cars Dealership Capstone)

> **Tư tưởng cốt lõi:** Khởi động dự án Capstone **Best Cars Dealership** — một ứng dụng Full-Stack Cloud-Native kết hợp **Django + React + Express/MongoDB + Flask/NLTK + Docker/Kubernetes/Code Engine** — bắt đầu bằng việc Fork/Clone mã nguồn mẫu, chạy máy chủ Django cục bộ và xây dựng các trang tĩnh (`Home`, `About Us`, `Contact Us`) chuẩn Bootstrap.

## 1. Kiến trúc tổng thể của Hệ thống Best Cars Dealership

Dự án Capstone tổng hợp trọn vẹn công nghệ từ toàn bộ 6 khóa trước thành một hệ thống phân tán thực tế:

```text
                        ┌────────────────────────────────────┐
                        │    Browser (HTML/Bootstrap/React)  │
                        └─────────────────┬──────────────────┘
                                          │ HTTP / JSON
                        ┌─────────────────▼──────────────────┐
                        │   Main App: Python / Django        │
                        │   - Auth (Login/Logout/Register)   │
                        │   - SQLite (CarMake, CarModel)     │
                        │   - Static Pages & React Bundle    │
                        │   - Proxy Views (restapis.py)      │
                        └───────┬────────────────────┬───────┘
                                │                    │
           ┌────────────────────▼───┐          ┌─────▼─────────────────────┐
           │ Express + MongoDB      │          │ Flask + NLTK Microservice │
           │ (Dockerized Service)   │          │ (IBM Cloud Code Engine)   │
           │ - Dealerships & Reviews│          │ - Sentiment Analyzer API  │
           └────────────────────────┘          └───────────────────────────┘
```

### Bản đồ công nghệ toàn dự án

| Tầng hệ thống | Công nghệ sử dụng | Vai trò trong Capstone |
| --- | --- | --- |
| **Version Control & CI/CD** | Git, GitHub, GitHub Actions | Quản lý nhánh/commit, tự động lint Python (`flake8`) & JS (`jshint`) |
| **Static & Dynamic Front-End** | HTML5, CSS3, Bootstrap, **React** | Trang tĩnh (`Home`, `About`, `Contact`) và các component động (`Login`, `Register`, `Dealers`, `Dealer`, `PostReview`) |
| **Main Back-End & Proxy** | **Python, Django, SQLite** | Xác thực người dùng, quản trị `CarMake`/`CarModel`, định tuyến & proxy gọi các microservices |
| **Dealerships & Reviews API** | **Node.js, Express, MongoDB** | Dịch vụ lưu trữ và truy vấn danh sách đại lý xe & đánh giá khách hàng (đóng gói Docker) |
| **AI Sentiment Microservice** | **Python, Flask, NLTK** | Phân tích sắc thái bình luận (*positive / neutral / negative*), triển khai Serverless trên IBM Cloud Code Engine |
| **Container & Orchestration** | **Docker, Kubernetes** | Đóng gói đa đám mây (tránh vendor lock-in), triển khai và mở rộng bằng `deployment.yaml` |

## 2. Nhiệm vụ trọng tâm của Module 1 (Static Pages)

1. **Fork & Clone Repository mẫu:** Tạo bản fork trên GitHub cá nhân và clone về môi trường phát triển.
2. **Thiết lập môi trường ảo & Chạy Django Development Server:**
   ```bash
   cd server
   python3 -m venv djangoenv
   source djangoenv/bin/activate
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
3. **Tạo và định tuyến các trang tĩnh (`server/frontend/static/`):**
   - `Home.html`: Trang chủ với thanh điều hướng Bootstrap (`Home`, `About Us`, `Contact Us`).
   - `About.html`: Trang giới thiệu đội ngũ Best Cars với liên kết CSS chính xác (`bootstrap.min.css`, `style.css`), hình ảnh thực tế, tên, chức danh, mô tả ngắn và email liên hệ.
   - `Contact.html`: Trang liên hệ với thanh điều hướng đánh dấu active tại `Contact Us`, hình ảnh minh họa và đầy đủ thông tin bộ phận chăm sóc khách hàng/PR/kinh doanh.
4. **Khai báo URL Routing trong `server/djangoproj/urls.py`:** Ánh xạ `/about/` → `TemplateView.as_view(template_name="About.html")` và `/contact/` → `TemplateView.as_view(template_name="Contact.html")`.
5. **Commit & Push** toàn bộ thay đổi lên repository GitHub đã fork.

## 3. Bẫy thường gặp & Lưu ý kiểm thử (Critical Pitfalls)

1. **Sai đường dẫn tệp tĩnh (`/static/style.css`):** Nếu viết thiếu tiền tố `/static/` hoặc cấu hình sai `STATICFILES_DIRS` trong `settings.py`, trang `About.html` và `Contact.html` sẽ mất hoàn toàn giao diện Bootstrap.
2. **Quên đánh dấu trạng thái `active` trên Navbar:** Ở trang `Contact.html`, mục `Contact Us` cần có class `active` (thay vì giữ `active` ở `Home`) để đáp ứng tiêu chí đánh giá UI.
3. **Chưa lưu output terminal chạy server:** Bài nộp cuối khóa yêu cầu dán output của `python manage.py runserver` (lưu trong tệp `django_server`), nên cần kiểm tra chạy không lỗi ngay từ Module 1.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- Django đóng vai trò ứng dụng trung tâm phục vụ cả trang tĩnh, xác thực người dùng, dữ liệu danh mục xe (SQLite) và proxy gọi các microservices ngoài.
- Hoàn thiện vững chắc bước Fork/Clone, chạy Django và chuẩn hóa các trang tĩnh `Home`, `About`, `Contact` là nền móng sạch cho 5 module kế tiếp.
