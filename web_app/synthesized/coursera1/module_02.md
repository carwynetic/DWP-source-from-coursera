# Module 2: ORM — Bridging the Gap Between the Real World and Relational Model

> **Tư tưởng cốt lõi:** Lập trình hiện đại dùng OOP (Class/Object/Inheritance) trong khi CSDL quan hệ dùng SQL (Table/Row/Foreign Key). **Django ORM** làm cầu nối ánh xạ trực tiếp Python Class ↔ Database Table, cho phép thực hiện toàn bộ CRUD và truy vấn liên kết đa bảng mà không cần viết SQL thủ công.

## 1. Tổng quan Django Framework ("Batteries Included")

Django là web framework Python mã nguồn mở, bậc cao, nổi tiếng với triết lý **"Batteries Included"** (tích hợp sẵn gần như mọi công cụ cần thiết):
- **ORM Layer:** Định nghĩa schema database bằng Python class.
- **Template Engine:** Tách biệt business logic và presentation logic.
- **Auto-generated Admin Site:** Tự sinh giao diện quản trị từ Models.
- **Built-in Security:** Chống XSS, CSRF, SQL Injection, tự hash mật khẩu và quản lý session.
- **AuthN & AuthZ:** Sẵn hệ thống đăng ký, đăng nhập, phân quyền theo Group/Permission.
- **Stateless ("Share-Nothing") Architecture:** Mỗi instance server xử lý request độc lập, không giữ state cục bộ → dễ dàng scale ngang (horizontal scaling) và chạy trên mọi nền tảng Cloud (platform-agnostic).
- **Hệ sinh thái thực tế:** Instagram, Spotify, YouTube, The Washington Post.

## 2. OOAD & Sự khác biệt giữa OOP và SQL (Impedance Mismatch)

- **OOAD (Object-Oriented Analysis and Design):** Thiết kế phần mềm xoay quanh các **Objects** (chứa *properties/data* và *methods/behaviors*). **Class** là bản thiết kế (blueprint), tạo object từ class gọi là **instantiation**. **UML Class Diagram** biểu diễn cấu trúc tĩnh và quan hệ kế thừa (subclass kế thừa thuộc tính & phương thức của parent class).

| Khía cạnh | Mô hình OOP (Python) | Mô hình SQL (Relational DB) |
| --- | --- | --- |
| **Biểu diễn thực thể** | Class, Object (Instance), Attribute | Table, Row (Record), Column |
| **Biểu diễn quan hệ** | Inheritance, Association, Aggregation | `FOREIGN KEY`, bảng trung gian, `JOIN` |
| **Thao tác CRUD** | Gọi method trên Object / Manager | Lệnh DML (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) |
| **Truy xuất thủ công** | Phải mở Connection → Cursor → `execute()` → `fetchone()` → map từng cột sang attribute | Trả về bảng kết quả thô (Result Set) |

### Đánh giá phản biện: Ưu & Nhược điểm của ORM

| Ưu điểm (Pros) | Nhược điểm & Rủi ro (Cons) |
| --- | --- |
| Thiết kế Class đồng thời định nghĩa luôn Database Schema | **Imperfect mapping:** OOP và SQL là 2 hệ tư duy khác nhau, đôi khi ORM ánh xạ không hoàn hảo |
| Làm việc với DB mà không cần viết SQL thủ công | **Increased code coupling:** Thay đổi DB có thể kéo theo sửa cả logic ứng dụng |
| 1 giao diện ORM thống nhất chạy được trên nhiều hệ DB khác nhau | **Khó debug:** Lớp trừu tượng ẩn chi tiết thực thi bên dưới |
| Tăng tốc độ phát triển & rút ngắn thời gian ra sản phẩm | **Hiệu năng (Performance overhead):** Thêm tầng biên dịch; SQL tự sinh không phải lúc nào cũng tối ưu nhất |

*Các ORM phổ biến khác:* Python (**Django ORM**, SQLAlchemy), Java (Hibernate, OpenJPA), JavaScript (Sequelize, TypeORM).

## 3. Ánh xạ ERD sang Django Models

Trong Django ORM: **1 Model Class = 1 Table**, **1 Instance = 1 Row**, **1 Field = 1 Column** (kèm metadata như `max_length`, `null`, `blank`, `default`, `primary_key`).

### A. 3 kiểu quan hệ trong Django ORM

```python
from django.db import models
from django.conf import settings

# 1. One-to-One (1-1): Mỗi Instructor gắn với 1 User duy nhất
class Instructor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)

# 2. Many-to-One (N-1): Nhiều Project thuộc 1 Course (đặt ForeignKey ở phía "Nhiều")
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # 3. Many-to-Many (N-N): Đặt ở model được chỉnh sửa thường xuyên hơn
    instructors = models.ManyToManyField(Instructor)
    # N-N có bảng trung gian lưu thêm metadata (date_enrolled, mode) dùng `through`
    learners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Enrollment')

class Project(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    grade = models.FloatField()

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
```

### B. 3 chiến lược Model Inheritance trong Django

| Chiến lược | Cơ chế bảng DB | Khi nào dùng |
| --- | --- | --- |
| **Multi-table inheritance** | Mỗi model (cha & con) có bảng riêng; Django tự tạo ngầm `OneToOneField` (`<parent>_ptr`) | Kế thừa từ model có sẵn và muốn cha lẫn con đều có bảng độc lập |
| **Abstract Base Classes** | Cha **không tạo bảng**, chỉ truyền field chung xuống các bảng con | Gom các field lặp lại (`created_at`, `updated_at`) cho nhiều model |
| **Proxy Models** | Dùng chung bảng với cha, **không đổi schema** | Chỉ muốn thay đổi hành vi Python (thêm method, đổi `ordering` mặc định) |

## 4. Django Models CRUD & QuerySet API

Mọi truy vấn cấp bảng đều đi qua **Model Manager** (mặc định là `Model.objects`), trả về một **QuerySet** (có thể nối chuỗi `.filter().exclude()` như toán tử `AND` trong SQL `WHERE`).

```python
# --- CREATE ---
course = Course(name="Cloud App Dev", description="Django + SQL")
course.save()

# --- READ ---
all_courses = Course.objects.all()
part_time = Instructor.objects.filter(full_time=False)
# Chaining exclude + filter
top_j = Instructor.objects.exclude(full_time=False).filter(
    total_learners__gt=30000,
    user__first_name__startswith="J"
)
# Lấy đúng 1 đối tượng (báo lỗi nếu 0 hoặc >1 kết quả)
john = Instructor.objects.get(user__first_name="John")

# --- UPDATE ---
course.description = "Updated description"
course.save()

# --- DELETE ---
course.delete()
```

### Bảng Field Lookups cốt lõi (`field__lookup=value`)

| Lookup | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| `exact` / `iexact` | Khớp chính xác (phân biệt / không phân biệt hoa thường) | `filter(name__iexact="django")` |
| `contains` | Chứa chuỗi con | `filter(name__contains="SQL")` |
| `startswith` / `endswith` | Bắt đầu / kết thúc bằng chuỗi | `filter(name__startswith="Intro")` |
| `in` | Nằm trong danh sách giá trị | `filter(id__in=[1, 2, 3])` |
| `gt` / `lt` | Lớn hơn (`>`) / Nhỏ hơn (`<`) | `filter(total_learners__gt=5000)` |
| `related__field` | Truy vấn xuyên bảng (tự sinh SQL JOIN) | `Course.objects.filter(instructors__user__first_name="John")` |

## 5. Related Objects: Forward/Backward Access & `on_delete`

Django chỉ yêu cầu khai báo quan hệ ở **1 phía (Forward / Explicit access)** — phía còn lại (**Backward / Implicit access**) được tự động sinh:
- **Forward (`Project -> Course`):** `project.course`
- **Backward (`Course -> Projects`):** `course.project_set.all()` *(quy tắc `<model_name>_set`)*
- **Multi-table inheritance pointer:** `learner.user_ptr`
- **Các phương thức thao tác tập quan hệ:** `.add(obj)`, `.create(**kwargs)`, `.remove(obj)`, `.clear()`, `.set(new_list)`.

### 5 tùy chọn `on_delete` khi xóa đối tượng cha (ForeignKey)

| Tùy chọn `on_delete` | Hành vi khi xóa bản ghi cha (`Course`) | Lưu ý quan trọng |
| --- | --- | --- |
| `models.CASCADE` | **Xóa luôn** toàn bộ bản ghi con (`Project`) liên quan | Mặc định phổ biến nhất |
| `models.PROTECT` | **Chặn không cho xóa** cha nếu vẫn còn con đang tham chiếu | An toàn cao cho dữ liệu tài chính/học vụ |
| `models.SET_NULL` | Giữ lại bản ghi con, đặt FK thành `NULL` | **Bắt buộc** khai báo kèm `null=True` trên field |
| `models.SET_DEFAULT` / `SET()` | Gán FK sang giá trị mặc định hoặc giá trị từ hàm callback | Cần khai báo `default=...` |
| `models.DO_NOTHING` | Không làm gì cả | **Không khuyến khích** — tạo ra *orphan records* (bản ghi mồ côi trỏ tới ID không tồn tại) |

## 6. Bẫy thường gặp & Điểm cốt lõi cần nhớ

1. **Manager `objects` chỉ gọi trên Class (`Course.objects`), KHÔNG gọi trên Instance (`course.objects`):** Django cố tình tách biệt thao tác cấp bảng (table-level) và cấp bản ghi (record-level).
2. **Đặt `ManyToManyField` ở đâu?** Đặt ở model nào được chỉnh sửa/cập nhật thường xuyên hơn (ví dụ `Course` cập nhật học viên hàng giờ thay vì `Learner` đăng ký hàng tháng).
3. **Migration bắt buộc:** Sau mỗi lần định nghĩa/sửa Model, luôn chạy `python manage.py makemigrations` rồi `python manage.py migrate` để đồng bộ schema DB.
