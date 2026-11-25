# Module 2: Application — User Management (Django Auth + React Client)

> **Tư tưởng cốt lõi:** Tích hợp hệ thống **Xác thực (Authentication) & Phân quyền (Authorization)** hoàn chỉnh giữa **Django Back-End** (`django.contrib.auth`) và **React Front-End** (Login, Logout, Register), đồng thời build và cấu hình React client để chạy mượt ngay dưới cùng nguồn gốc (origin) của máy chủ Django.

## 1. Luồng phân quyền & Quản trị người dùng

Hệ thống Best Cars Dealership phân biệt rõ 2 nhóm người dùng:
- **Anonymous User (Khách vãng lai):** Chỉ xem được trang tĩnh, danh sách đại lý và đọc đánh giá hiện có.
- **Authenticated / Registered User (Người dùng đã đăng nhập):** Có thêm quyền **viết và gửi đánh giá mới (Post Review)** cho các đại lý; ngoài ra **Superuser / Admin** có quyền truy cập `/admin/` để quản trị dữ liệu.

## 2. Thiết lập Django Superuser & Build React Client

```bash
# 1. Tạo tài khoản quản trị viên cho Django Admin (/admin)
python manage.py createsuperuser

# 2. Build ứng dụng React để Django phục vụ trực tiếp
cd server/frontend
npm install
npm run build
```

- Kiểm tra cấu hình `settings.py` để Django nhận diện thư mục `frontend/build` và `frontend/build/static` trong `TEMPLATES['DIRS']` và `STATICFILES_DIRS`.
- Trong `urls.py`, ánh xạ các đường dẫn SPA (`/login/`, `/register/`) tới `TemplateView.as_view(template_name="index.html")` để React Router đảm nhiệm render giao diện.

## 3. Ba API Views cốt lõi trong `djangoapp/views.py`

| Endpoint | View Function | Cơ chế xử lý chuẩn Django Auth |
| --- | --- | --- |
| `POST /djangoapp/login` | `login_user(request)` | Đọc `userName` & `password` từ `json.loads(request.body)` → gọi `authenticate(username=..., password=...)` → nếu hợp lệ gọi `login(request, user)` và trả JSON `{"userName": username, "status": "Authenticated"}` |
| `GET /djangoapp/logout` | `logout_request(request)` | Gọi `logout(request)` xóa phiên đăng nhập trên server → trả JSON `{"userName": ""}` |
| `POST /djangoapp/register` | `registration(request)` | Kiểm tra `User.objects.get(username=...)` tránh trùng lặp → nếu chưa tồn tại gọi `User.objects.create_user(...)` → tự động gọi `login(request, user)` và trả JSON `{"userName": username, "status": "Authenticated"}` |

```python
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    return JsonResponse({"userName": username})
```

### Tích hợp phía React Client (`Login.jsx` & `Register.jsx`)
- **Navbar động:** Đọc `sessionStorage.getItem("username")`. Nếu chưa đăng nhập hiển thị **Login / Register**; nếu đã đăng nhập hiển thị tên tài khoản kèm nút **Logout**.
- **Trang `Register.jsx`:** Thu thập `username`, `password`, `firstName`, `lastName`, `email` → gửi `POST /djangoapp/register` → lưu `sessionStorage.setItem("username", json.userName)` và chuyển hướng về trang chủ; hiển thị thông báo rõ nếu tài khoản đã tồn tại.

## 4. Kiểm thử API Auth bằng `cURL` & Bẫy thường gặp

```bash
# Kiểm thử đăng nhập trực tiếp qua cURL (cũng là deliverable cho Task 5 trong bài nộp)
curl -X POST http://127.0.0.1:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d '{"userName": "admin", "password": "yourpassword"}'
```

### Bẫy thường gặp (Critical Pitfalls)
1. **Quên chạy lại `npm run build` sau khi sửa code React:** Vì Django phục vụ bản tĩnh từ `frontend/build`, mọi chỉnh sửa trong `src/` sẽ **không xuất hiện** trên trình duyệt cho đến khi bạn build lại!
2. **Dùng `User.objects.create()` thay vì `User.objects.create_user()`:** `create()` lưu mật khẩu dạng văn bản thuần (plain text) khiến `authenticate()` luôn thất bại; bắt buộc dùng `create_user()` để Django băm (hash) mật khẩu chuẩn.
3. **Không xóa `sessionStorage` khi Logout:** Dẫn đến server đã đăng xuất nhưng thanh điều hướng React vẫn hiển thị tên người dùng cũ.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Xác thực Full-Stack gồm 3 luồng khép kín: **Login** (`authenticate` + `login`), **Logout** (`logout` + xóa `sessionStorage`), và **Register** (`create_user` + chống trùng username + tự động đăng nhập).
- Luôn đồng bộ route giữa `djangoproj/urls.py`, `djangoapp/urls.py` và `App.js` của React Router.
