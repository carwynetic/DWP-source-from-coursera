# Module 1: Python Coding Practices and Packaging Concepts

> **Tư tưởng cốt lõi:** Phát triển phần mềm Python chuyên nghiệp tuân thủ vòng đời 7 giai đoạn từ thu thập yêu cầu đến bảo trì, kết hợp chuẩn định dạng **PEP 8** và phân tích mã tĩnh **PyLint**, kiểm thử tự động bằng **`unittest`**, và đóng gói module thành **Package** có cấu trúc thông qua tệp **`__init__.py`**.

## 1. Vòng đời phát triển ứng dụng (Application Development Lifecycle)

Mọi ứng dụng thực tế — từ app quản lý công việc đến hệ thống đặt phòng khách sạn — đều phải đi qua **7 giai đoạn** chuẩn trước khi đến tay người dùng cuối:

| Giai đoạn | Mục tiêu & Hoạt động cốt lõi | Ví dụ (App đặt phòng khách sạn) |
| --- | --- | --- |
| **1. Requirement Gathering** | Thu thập **User requirements**, **Business requirements**, **Technical requirements** và ràng buộc chi phí/thiết kế | User xem phòng/tiện nghi; Business tính phí tiện ích; Technical chạy mọi trình duyệt/mobile |
| **2. Analysis** | Phân tích tính khả thi và đối chiếu các yêu cầu/ràng buộc | Đánh giá chi phí đồng bộ trạng thái phòng real-time |
| **3. Design** | Thiết kế kiến trúc tổng thể qua nhiều vòng kiểm chứng và chỉnh sửa | Thiết kế luồng dữ liệu, DB, API & giao diện |
| **4. Code and Test** | Chia nhỏ chức năng thành nhiều tệp riêng gọi qua chương trình trung tâm; viết code & unit test | Tách file xử lý phòng, thanh toán, xác thực |
| **5. User and System Test** | **User testing** (usability), **Integration testing** (tích hợp hệ thống), và **Performance testing** (kiểm thử hiệu năng/hiệu suất) | Kiểm tra cổng thanh toán mới hoạt động mượt & hiệu quả với hệ thống hiện có |
| **6. Production** | Phát hành ứng dụng cho toàn bộ người dùng cuối | Triển khai lên server sản phẩm |
| **7. Maintenance** | Nâng cấp tính năng, vá lỗi người dùng hoặc sự cố hệ thống | Cập nhật bảo mật, sửa lỗi phát sinh |

*Nguyên tắc tổ chức mã nguồn:* Tách mỗi chức năng vào một tệp riêng và gọi thông qua tệp trung tâm để dễ bảo trì và thêm tính năng mới mà không làm gián đoạn toàn bộ ứng dụng.

## 2. Web Applications vs. APIs

Một **Web Application** là chương trình lưu trên máy chủ từ xa, chạy qua trình duyệt (không cần cài đặt cục bộ) với 3 thành phần: **Web server** (tiếp nhận request), **App server** (chạy logic) và **Database** (lưu trữ dữ liệu).

- **API (Application Programming Interface):** Thành phần trung gian với bộ quy tắc chuẩn giúp hai phần mềm độc lập giao tiếp dữ liệu (ví dụ app đồng hồ thông minh lấy dự báo thời tiết qua Weather API mà không tự thu thập dữ liệu khí tượng).
- **Quan hệ bao hàm:** **Mọi Web App đều là API** (vì kết nối front-end và back-end qua HTTP để chia sẻ dữ liệu), nhưng **không phải mọi API đều là Web App** (vì API có thể chạy offline/cục bộ không cần mạng).
- API hỗ trợ chuẩn **CRUD** qua các HTTP verbs (`POST`, `GET`, `PUT`, `DELETE`) theo kiến trúc **REST** hoặc **SOAP**.

## 3. Chuẩn PEP 8 & Phân tích mã tĩnh (Static Code Analysis)

**PEP 8 (Python Enhancement Proposal 8)** là bộ quy chuẩn giúp code Python sạch, đồng nhất và dễ đọc cho cả đội ngũ:

| Quy tắc PEP 8 | Chuẩn bắt buộc | Ví dụ đúng |
| --- | --- | --- |
| **Thụt lề (Indentation)** | Dùng **4 dấu cách (spaces)** cho mỗi cấp, **không dùng Tab** (vì mỗi IDE hiểu độ rộng Tab khác nhau) | `    return x * 2` |
| **Khoảng trắng** | Cách dòng trống tách hàm & class; có khoảng trắng quanh toán tử và sau dấu phẩy | `a = b + c`, `func(x, y)` |
| **Tên hàm & tên file** | `lowercase_with_underscores` (snake_case) | `get_user_name()`, `my_module.py` |
| **Tên Class** | `CamelCase` (PascalCase) | `class UserClass:` |
| **Tên Hằng số (Constants)** | `ALL_CAPS_WITH_UNDERSCORES` | `MAX_FILE_UPLOAD_SIZE = 10`, `DATE_OF_BIRTH` |

**Static Code Analysis (Phân tích mã tĩnh):** Đánh giá mã nguồn theo chuẩn phong cách và phát hiện lỗi cú pháp, biến chưa khai báo, lỗ hổng bảo mật **mà không cần chạy chương trình**. Công cụ chuẩn trong khóa học là **PyLint**:

```bash
pip install pylint
pylint my_module.py   # Chấm điểm tuân thủ PEP 8 trên thang 10 và liệt kê cảnh báo
```

## 4. Kiểm thử đơn vị (Unit Testing) với `unittest`

**Unit testing** xác minh từng đơn vị code nhỏ nhất (hàm/phương thức) chạy đúng như thiết kế theo 2 pha: kiểm thử cục bộ trên máy dev → kiểm thử trên **CI/CD test server** trước khi gộp vào codebase chính.

- Tệp test nên có tiền tố/hậu tố `test_` (vd `test_mymodule.py` cho `mymodule.py`).
- Gom các hàm test (bắt đầu bằng **`test_`**) vào trong một class kế thừa `unittest.TestCase` để tạo **một điểm vào duy nhất (single entry point)** chạy toàn bộ bộ test.

```python
# mymodule.py
def square(number):
    """Return the square of a number."""
    return number ** 2

def doubler(number):
    """Return twice the value of a number."""
    return number * 2

# test_mymodule.py
import unittest
from mymodule import square, doubler

class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)

    def test_doubler(self):
        self.assertEqual(doubler(3), 6)

if __name__ == "__main__":
    unittest.main()
```

Nếu `doubler(3)` trả về `9` thay vì `6`, `assertEqual(doubler(3), 6)` sẽ báo **FAIL** (`AssertionError: 9 != 6`), chỉ ra ngay lỗi logic nằm trong hàm `doubler` trước khi deploy.

## 5. Đóng gói Python: Module, Package và Library

| Khái niệm | Định nghĩa chuẩn | Ví dụ |
| --- | --- | --- |
| **Module** | Một tệp `.py` duy nhất chứa hàm, class, câu lệnh Python | `module1.py`, `data_tools.py` |
| **Package** | Thư mục chứa một hoặc nhiều module **kèm tệp `__init__.py`** | Thư mục `myproject/` có `__init__.py`, `module1.py` |
| **Library** | Tập hợp nhiều package (hoặc một package lớn); thực tế thường dùng thay thế cho package | `NumPy`, `Pandas`, `PyTorch` |

### Quy trình 4 bước tạo & kiểm chứng Package

```text
myproject/
├── __init__.py
├── module1.py   # chứa square(), doubler()
└── module2.py   # chứa mean()
```

```python
# 1. Nội dung myproject/__init__.py (tham chiếu các module trong package)
from . import module1
from . import module2

# 2. Sử dụng từ script test.py ở thư mục cha
from myproject.module1 import square, doubler
from myproject.module2 import mean

print(square(4))       # 16
print(mean([2, 1, 3])) # 2.0

# Hoặc import trực tiếp để gọi dạng package.module.function(...)
import myproject
print(myproject.module1.square(2)) # 4
```

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm Integration Testing với Performance Testing:** Kiểm thử khả năng ghép nối giữa module mới (vd cổng thanh toán) với hệ thống hiện tại là *Integration testing*; nhưng câu hỏi yêu cầu kiểm tra **hiệu suất/hiệu năng (efficiency)** khi vận hành cùng hệ thống là **Performance testing**.
2. **Dùng Tab lẫn Space trong Python:** Dẫn đến `TabError` hoặc sai logic khối lệnh khi mở trên IDE khác; luôn cấu hình editor đổi Tab thành **4 spaces**.
3. **Thiếu `__init__.py` hoặc quên khai báo `from . import ...`:** Khi `import mypackage`, bạn sẽ không gọi được `mypackage.my_module.func()` nếu chưa import module con trong `__init__.py` hoặc import tường minh `from mypackage import my_module`.
4. **Đặt tên hàm test không bắt đầu bằng `test_`:** `unittest.main()` chỉ tự động phát hiện và chạy các phương thức có tiền tố **`test_`**.
5. **Chạy PyLint nhưng tưởng code đang được thực thi:** PyLint là công cụ **static code analysis** — nó chỉ đọc cấu trúc AST/văn bản để tìm lỗi logic tiềm ẩn và vi phạm PEP 8 chứ không chạy code.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- Vòng đời ứng dụng có **7 pha**: Requirement Gathering → Analysis → Design → Code & Test → User & System Test → Production → Maintenance.
- **Mọi Web App là API, nhưng không phải mọi API đều là Web App**; cả hai đều kết nối hai thành phần hệ thống.
- **PEP 8**: 4 spaces, `snake_case` cho hàm/file, `CamelCase` cho class, `UPPER_CASE` cho hằng số; kiểm tra tự động bằng **PyLint**.
- **Package** = thư mục chứa các `.py` module + tệp **`__init__.py`** tham chiếu module; kiểm thử từng unit bằng **`unittest.TestCase`** trước khi đưa lên CI/CD.
