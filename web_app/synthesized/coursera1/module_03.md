# Module 3: Full-stack Django Development

> **Tư tưởng cốt lõi:** Django triển khai kiến trúc **MVT (Model – View – Template)** — biến thể của MVC trong đó bản thân Django framework đóng vai trò Controller định tuyến HTTP Request qua `urls.py` → `views.py` → `models.py` → `templates/` để trả về trang HTML động, đồng thời cung cấp sẵn **Django Admin** cực mạnh để quản trị dữ liệu.

## 1. Kiến trúc MVC vs. Django MVT

| Thành phần | MVC truyền thống | Django MVT | Vai trò cụ thể trong Django |
| --- | --- | --- | --- |
| **Dữ liệu & Logic nghiệp vụ** | **Model** | **Model** (`models.py`) | Ánh xạ bảng DB (ORM), CRUD và business logic |
| **Điều phối & Định tuyến** | **Controller** | **Django Framework + `urls.py`** | Nhận HTTP request, so khớp URL pattern và gọi đúng View |
| **Quyết định hiển thị CÁI GÌ** | Controller/View | **View** (`views.py`) | Hàm/class Python nhận `HttpRequest`, truy vấn Model, trả về `HttpResponse` (HTML, JSON, 404, redirect) |
| **Quyết định hiển thị NHƯ THẾ NÀO** | **View** | **Template** (`templates/`) | File HTML kết hợp Django Template Tags (`{% %}`) và Variables (`{{ }}`) |

> **Luồng xử lý 1 HTTP Request trong Django:**
> `Client Browser` → `Django Server (URLConf: urls.py)` → `View (views.py)` ⇄ `Model (models.py / DB)` → `render(request, template, context)` → `HttpResponse (HTML)` → `Client Browser`.

## 2. Cấu trúc Project vs. App & Quy trình phát triển chuẩn

Một **Django Project** là container chứa cấu hình tổng và nhiều **Django Apps** (mỗi app là một module tính năng có thể tái sử dụng, ví dụ `onlinecourse`).

### Các lệnh khởi tạo & vòng đời phát triển

```bash
# 1. Tạo Project container
django-admin startproject mysite

# 2. Tạo App bên trong Project
cd mysite
python manage.py startapp onlinecourse

# 3. Sinh & kiểm tra & chạy migration sau khi viết models.py
python manage.py makemigrations onlinecourse
python manage.py sqlmigrate onlinecourse 0001   # xem câu SQL thật sẽ chạy
python manage.py migrate

# 4. Tạo tài khoản quản trị & chạy server dev (127.0.0.1:8000)
python manage.py createsuperuser
python manage.py runserver
```

### Bản đồ các file cốt lõi cần nắm chắc

| Phạm vi | File / Thư mục | Vai trò |
| --- | --- | --- |
| **Project (`mysite/`)** | `manage.py` | CLI tương tác với project (`runserver`, `migrate`, `createsuperuser`...) |
| | `settings.py` | Cấu hình toàn cục: `INSTALLED_APPS`, `DATABASES`, `TEMPLATES`, `STATIC_*` |
| | `urls.py` | Root URLConf — phân nhánh URL tới từng app bằng `include()` |
| **App (`onlinecourse/`)** | `models.py` | Định nghĩa ORM models & quan hệ dữ liệu |
| | `views.py` | Xử lý HTTP Request và trả về `HttpResponse` |
| | `urls.py` | URLConf riêng của app (nên khai báo `app_name = 'onlinecourse'`) |
| | `admin.py` | Đăng ký & tùy biến giao diện quản trị Django Admin |
| | `apps.py` | Class cấu hình app (vd `OnlinecourseConfig` thêm vào `INSTALLED_APPS`) |
| | `migrations/` | Các script theo dõi lịch sử thay đổi schema database |

## 3. Django Admin — Quản trị nội dung ít code, tùy biến sâu

Django tách bạch rõ **Content Publishers (Admin/Instructors)** và **End Users (Learners)**. Chỉ cần đăng ký model trong `admin.py`, Django tự sinh widget UI phù hợp theo kiểu field (checkbox cho `BooleanField`, ô số cho `IntegerField`...).

```python
from django.contrib import admin
from .models import Course, Lesson, Instructor

# Inline cho phép thêm/sửa nhiều Lesson ngay trong form tạo Course
class LessonInline(admin.StackedInline):  # hoặc admin.TabularInline
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']   # Chọn & sắp thứ tự field trên form
    inlines = [LessonInline]                       # Nhúng form con
    list_display = ('name', 'pub_date')            # Các cột hiển thị trên bảng danh sách
    list_filter = ['pub_date']                     # Bộ lọc bên phải
    search_fields = ['name', 'description']        # Ô tìm kiếm nhanh

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
```

## 4. Views, URL Routing & HTTP Status Codes

- **Function-Based View (FBV):** Nhận `request` (`HttpRequest` chứa `method`, `headers`, `GET`/`POST` params) và trả về `HttpResponse` (mặc định status `200 OK`, hoặc `404 Not Found` khi không tìm thấy bản ghi).
- **URL Namespacing:** Khai báo `app_name = 'onlinecourse'` trong `onlinecourse/urls.py` và `name='index'` trên từng `path()` giúp tham chiếu an toàn từ template/view bằng `'onlinecourse:index'` — đổi đường dẫn URL mà không gãy code!

```python
# onlinecourse/urls.py
from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path('', views.course_list, name='index'),
    path('<int:course_id>/', views.course_detail, name='course_details'),
]

# onlinecourse/views.py
from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    context = {'course_list': Course.objects.order_by('-pub_date')[:10]}
    return render(request, 'onlinecourse/course_list.html', context)
```

## 5. Django Templates & Static Tags

- **Template Namespacing:** Luôn đặt template theo cấu trúc `onlinecourse/templates/onlinecourse/course_list.html`. Thư mục lồng thứ hai đóng vai trò **namespace** để tránh đụng tên khi nhiều app trong cùng project đều có `index.html`.
- **Template Engine Syntax:**
  - `{{ variable.attr }}` — hiển thị giá trị từ `context` dictionary (hỗ trợ dot notation).
  - `{% if ... %} ... {% else %} ... {% endif %}` và `{% for c in course_list %} ... {% endfor %}` — điều khiển luồng.
  - `{% load static %}` + `{% static 'onlinecourse/course.css' %}` — sinh URL tuyệt đối cho file CSS/JS/Image.

```html
{% load static %}
<link rel="stylesheet" href="{% static 'onlinecourse/course.css' %}">

{% if course_list %}
  <ul>
    {% for course in course_list %}
      <li><h2>{{ course.name }}</h2><p>{{ course.description }}</p></li>
    {% endfor %}
  </ul>
{% else %}
  <p>No courses are available.</p>
{% endif %}
```

## 6. Tối ưu truy vấn & Aggregation (Module 3 Cheat Sheet)

| Phương thức | Chức năng | Ví dụ chuẩn |
| --- | --- | --- |
| `count()` | Đếm số bản ghi | `Course.objects.count()` |
| `aggregate(Sum/Avg/Max/Min)` | Tính tổng / trung bình / lớn nhất / nhỏ nhất | `Course.objects.aggregate(Avg('total_enrollment'))` |
| `order_by('f')` / `order_by('-f')` | Sắp xếp tăng dần / giảm dần | `Course.objects.order_by('-pub_date')` |
| `select_related('fk')` | **SQL INNER JOIN** (dùng cho `ForeignKey` / `OneToOne`, giảm N+1 queries) | `Lesson.objects.select_related('course')` |
| `prefetch_related('m2m')` | **Separate query + Python join** (dùng cho `ManyToMany` / reverse FK) | `Course.objects.prefetch_related('instructors')` |
| `filter(rel__isnull=True)` | Lọc bản ghi không có đối tượng liên kết | `Course.objects.filter(instructors__isnull=True)` |

## 7. Bẫy thường gặp & Điểm cốt lõi cần nhớ

1. **Quên đăng ký app vào `INSTALLED_APPS`:** Nếu tạo app bằng `startapp` nhưng quên thêm `'onlinecourse.apps.OnlinecourseConfig'` vào `settings.py`, Django sẽ bỏ qua cả models, migrations lẫn templates của app đó.
2. **Nhầm lẫn vai trò View trong MVC và MVT:** Trong câu hỏi trắc nghiệm, nhớ kỹ: **Django View = chọn dữ liệu (WHAT)**, **Django Template = trình bày giao diện (HOW)**, **Django Server = Controller**.
3. **Dùng `select_related` cho `ForeignKey`/`OneToOne` và `prefetch_related` cho `ManyToMany`:** Hiểu đúng để tránh lỗi truy vấn N+1 khi render danh sách trong Template.
