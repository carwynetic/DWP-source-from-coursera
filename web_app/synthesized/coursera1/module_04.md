# Module 4: Consolidate and Deploy Your Django App

> **Tư tưởng cốt lõi:** Hoàn thiện một ứng dụng Django chuẩn production gồm 4 trụ cột: nâng cấp View sang **Class-Based / Generic Views**, triển khai **Authentication & Authorization** dựa trên Session/Cookie, tích hợp **Bootstrap & Static Files (`collectstatic`)**, và triển khai lên Web Server (**WSGI / ASGI**) kết hợp hạ tầng Cloud an toàn.

## 1. Function-Based Views (FBV) vs. Class-Based Views (CBV) & Generic Views

Cả FBV và CBV về bản chất **đều là Python callable (function)**: với CBV, `MyView.as_view()` trả về một inner callable chuyển request sang `dispatch()`, sau đó `dispatch()` tự gọi đúng method `get()` hoặc `post()`.

```python
from django.views import generic
from .models import Course

# Generic ListView & DetailView: Chỉ vài dòng code thay vì viết tay toàn bộ GET logic
class CourseListView(generic.ListView):
    model = Course
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail_bootstrap.html'

# Trong urls.py luôn gọi .as_view()
# path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details')
```

### So sánh phản biện: Khi nào dùng FBV vs. CBV?

| Tiêu chí | Function-Based Views (FBV) | Class-Based Views (CBV) & Generic Views |
| --- | --- | --- |
| **Ưu điểm** | Đơn giản, tường minh, dễ đọc từng dòng logic | Tái sử dụng & mở rộng cao (kế thừa), tách bạch `get()`/`post()`, có sẵn `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| **Nhược điểm** | Khó kế thừa/tái sử dụng; xử lý nhiều HTTP method bằng nhiều nhánh `if/elif` dễ rối | Logic ngầm nằm trong lớp cha — khó đọc hơn, đôi khi phải tra mã nguồn Django |
| **Nên chọn khi** | Logic đặc thù, một lần dùng, quy trình tùy biến phức tạp | Các mẫu CRUD/danh sách/chi tiết lặp lại nhiều lần |

## 2. Authentication (Xác thực) & Authorization (Phân quyền)

- **Authentication (AuthN):** Xác minh *bạn là ai* (username/password, OTP, SSO, sinh trắc học).
- **Authorization (AuthZ):** Kiểm tra *bạn được phép làm gì* trên tài nguyên sau khi đã đăng nhập.

### Cơ chế Session & Cookie trong Django Auth

1. Client gửi `POST` (username, password) tới Login View.
2. View gọi `user = authenticate(username=..., password=...)` → trả về đối tượng `User` nếu khớp, hoặc `None` nếu sai.
3. Gọi `login(request, user)` → Django tạo **Session ID** duy nhất lưu trạng thái user phía server (`request.session`) và gửi `sessionid` về trình duyệt qua **Cookie** (`request.COOKIES`) để các request sau không cần đăng nhập lại.
4. Đăng xuất chỉ cần gọi `logout(request)`. Đăng ký user mới dùng `User.objects.create_user(...)` (tự động hash mật khẩu — **không bao giờ lưu mật khẩu dạng plain text!**).
5. Bảo vệ view yêu cầu đăng nhập bằng decorator `@login_required`.

### Mô hình phân quyền 3 thực thể: `User` – `Group` – `Permission`

- Mặc định với mỗi Model, Django tự tạo **4 quyền (Permissions)**: `view`, `add`, `change`, `delete`.
- Thay vì gán lẻ từng quyền cho từng user, gom quyền vào **Group** (ví dụ nhóm `Instructors` có đủ `add/change/delete/view`, nhóm `Learners` chỉ có `view`), rồi thêm user vào Group qua Django Admin hoặc API.

## 3. Tích hợp Bootstrap & Quản lý Static Files

### A. Bootstrap trong Django Template
- Nhúng nhanh qua CDN trong `<head>` (CSS) và cuối `<body>` (JS).
- Các thành phần cốt lõi trong khóa học:
  - **Navbar:** `navbar`, `navbar-nav`, `nav-item`, `nav-link`, kết hợp inline login form (`form-control`, `btn btn-primary`, `btn btn-link`).
  - **Layout Container:** `.container` (chiều rộng cố định responsive) vs. `.container-fluid` (tràn 100% chiều rộng).
  - **Card & Card Deck:** `.card-deck` bọc nhiều `.card` (`.card-body`, `.card-title`, `.card-text`) có chiều cao đều nhau.
  - **Table:** `.table`, `<thead>`, `<tbody>`, `<tr>`, `<td>`.

### B. Static Files: Development vs. Production

| Môi trường | Cơ chế hoạt động | Cấu hình liên quan (`settings.py`) |
| --- | --- | --- |
| **Development** | Mỗi app chứa `static/<app_name>/...` (namespacing chống trùng tên); Django dùng `STATICFILES_FINDERS` (`AppDirectoriesFinder`, `FileSystemFinder`) tìm và serve trực tiếp | `STATIC_URL = '/static/'`, `STATICFILES_DIRS = [...]`, `django.contrib.staticfiles` trong `INSTALLED_APPS` |
| **Production** | Chạy `python manage.py collectstatic` gom toàn bộ static files từ mọi app vào **1 thư mục duy nhất** để web server (Nginx) hoặc **CDN / Cloud Storage** phục vụ trực tiếp | `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` |

## 4. Triển khai (Deployment): WSGI vs. ASGI & Hạ tầng Cloud

`python manage.py runserver` **chỉ dùng cho phát triển** — không an toàn và không chịu tải production. Vì Nginx/Apache không viết bằng Python, Django cần lớp giao tiếp chuẩn:

| Giao thức | Ý nghĩa | Mô hình xử lý | File mặc định | Web Server phổ biến |
| --- | --- | --- | --- | --- |
| **WSGI** | Web Server Gateway Interface | **Đồng bộ (Synchronous only)** | `wsgi.py` (`application`) | Gunicorn, uWSGI, Apache + `mod_wsgi` |
| **ASGI** | Asynchronous Server Gateway Interface | **Bất đồng bộ (Async + WebSockets + Sync)** | `asgi.py` (`application`) | Uvicorn, Daphne, Hypercorn |

### 3 mô hình Cloud Hosting cho Django
1. **Virtual Machine (IaaS):** Tự thuê VM (Ubuntu), tự cài Python, Nginx, DB, cấu hình bảo mật — kiểm soát tối đa nhưng tốn công vận hành.
2. **Platform-as-a-Service (PaaS — vd Heroku, Render):** Push code Git lên, nền tảng tự build và chạy.
3. **Containers & Serverless (Docker + Kubernetes / IBM Cloud Code Engine):** Đóng gói app + dependencies vào container image, tự động scale và giảm tải vận hành.

### 7 Best Practices bắt buộc khi lên Production

1. **Production Database:** Dùng PostgreSQL / MySQL / MariaDB / Oracle — **tuyệt đối tránh SQLite ở production** (không chịu được concurrency/traffic cao).
2. **Bảo mật thông tin nhạy cảm:** Lưu DB credentials, `SECRET_KEY` trong **Environment Variables**, không bao giờ hardcode vào mã nguồn.
3. **HTTPS:** Mã hóa toàn bộ giao tiếp giữa client và server.
4. **Static & Media via CDN / Cloud Storage:** Giảm tải trực tiếp cho Django app server.
5. **Load Balancing:** Tận dụng kiến trúc **stateless** của Django để phân tải traffic qua nhiều instance.
6. **Horizontal Scaling:** Thiết kế app sẵn sàng thêm container/instance khi lượng truy cập tăng đột biến.
7. **Monitoring & Logging:** Giám sát lỗi, độ trễ và log tập trung để phát hiện sự cố sớm.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Luôn gọi `.as_view()` khi gắn CBV vào `urls.py`.
- `authenticate()` chỉ kiểm tra thông tin đăng nhập; phải gọi thêm `login(request, user)` để tạo session.
- `TEMPLATES[0]['APP_DIRS'] = True` cho phép Django tự tìm template bên trong từng app; `collectstatic` gom toàn bộ static file vào `STATIC_ROOT` trước khi deploy.
