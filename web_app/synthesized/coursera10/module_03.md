# Module 3: Python Programming Fundamentals

> **Tư tưởng cốt lõi:** Tư duy lập trình Python xoay quanh việc điều khiển luồng thực thi bằng điều kiện (`if/elif/else`) và vòng lặp (`for`, `while`), đóng gói logic tái sử dụng qua hàm (`def`, phân biệt local/global scope), bảo vệ chương trình khỏi sự cố runtime bằng `try-except-else-finally`, và mô hình hóa thực thể qua lập trình hướng đối tượng (`class`, `object`, `__init__`, `self`).

## 1. Điều kiện & Rẽ nhánh (Conditions & Branching)

- **Toán tử so sánh:** `==` (bằng), `!=` (khác), `>`, `<`, `>=`, `<=`. Tất cả đều trả về `bool` (`True`/`False`).
  - Lưu ý: `1 = 2` gây `SyntaxError: can't assign to literal` (dùng nhầm phép gán `=` thay cho `==`).
  - So sánh chuỗi **phân biệt chữ hoa/thường**: `'a' == 'A'` trả về `False`.
- **Toán tử logic:** `and` (True khi cả hai vế True), `or` (True khi ít nhất 1 vế True), `not` (đảo ngược giá trị Boolean).
- **Cấu trúc `if - elif - else`:** Kiểm tra tuần tự từ trên xuống; nhánh `elif` chỉ được kiểm tra khi các điều kiện `if`/`elif` phía trước đều `False`; nhánh `else` không có điều kiện và chạy khi mọi điều kiện trước đều sai.

```python
signal_state = "Red"
if signal_state == "Green":
    print("Walk")
else:
    print("Wait")
print("Look both ways")  # Ngoài khối if-else nên LUÔN chạy → in "Wait" rồi "Look both ways"

# So sánh chuỗi & gán kết quả biểu thức Boolean
current_temp = 18
current_temp = current_temp > 25  # False (so sánh trước, gán sau)
```

## 2. Vòng lặp (Loops): `for`, `while`, `range()` & `enumerate()`

| Công cụ | Cơ chế & Khi nào dùng | Ví dụ chuẩn |
| --- | --- | --- |
| **`range(start, stop, step)`** | Sinh dãy số nguyên lười (lazy sequence trong Python 3) từ `start` đến **`stop - 1`** | `range(3)` → `0, 1, 2`; `range(1, 5)` → `1, 2, 3, 4`; `range(1, 11, 2)` → số lẻ `1..9` |
| **`for` loop** | Lặp khi **biết trước số lần** hoặc duyệt trực tiếp từng phần tử của iterable (`list`, `tuple`, `str`, `range`) | `for x in ['A', 'B', 'C']: print(x + 'A')` → `AA`, `BA`, `CA` |
| **`enumerate(seq)`** | Trả về từng cặp `(index, value)` cùng lúc trong mỗi bước lặp | `for i, x in enumerate(['A', 'B', 'C']): print(i, x)` → `0 A`, `1 B`, `2 C` |
| **`while` loop** | Lặp khi **chưa biết trước số lần**, dừng ngay khi điều kiện trở thành **`False`** | Dừng khi gặp ô không phải màu cam hoặc đếm tới ngưỡng |
| **`break` & `continue`** | `break` thoát hẳn vòng lặp; `continue` bỏ qua phần còn lại của lượt hiện tại để sang lượt kế | Kiểm soát luồng sớm bên trong vòng lặp |

```python
# Kết hợp range() và điều kiện
for i in range(1, 5):
    if i != 2:
        print(i)    # Output: 1, 3, 4 (không có 2 và không có 5!)

# While loop luôn phải có bước cập nhật điều kiện để tránh lặp vô tận
squares = ["orange", "orange", "purple", "blue"]
new_squares = []
i = 0
while i < len(squares) and squares[i] == "orange":
    new_squares.append(squares[i])
    i += 1
```

## 3. Hàm (Functions) & Phạm vi biến (Variable Scope)

- **Lợi ích:** Tái sử dụng (reusability), mô-đun hóa (modularity), dễ đọc và dễ gỡ lỗi (debugging).
- **Hàm dựng sẵn (Built-in functions):**
  - `len(seq)`: trả về độ dài (`len([sum([1, 1, 1])]) == len([3]) == 1`).
  - `sum(iterable)`, `min()`, `max()`.
  - `sorted(L)` tạo list mới; khác với method `L.sort()` sửa trực tiếp list gốc.
- **Định nghĩa hàm với `def`:**
  - Tham số (**parameters**) là biến trong định nghĩa hàm; đối số (**arguments**) là giá trị truyền vào khi gọi.
  - Dùng `"""docstring"""` ngay dưới dòng `def` để `help(func)` hiển thị tài liệu.
  - Từ khóa `pass` đóng vai trò placeholder (no-op) khi chưa viết thân hàm.
  - Hàm không có `return` mặc định trả về `None`.
  - **Cộng chuỗi trong hàm:** Nếu `def add(x): return x + x`, gọi `add('1')` trả về `'11'` (nối chuỗi), không phải `2`!
- **Phạm vi biến (Scope — Local vs. Global):**
  - Biến gán bên trong hàm thuộc **Local Scope** — tách biệt hoàn toàn với biến cùng tên ở **Global Scope** (trừ khi khai báo `global var`). Nếu hàm chỉ *đọc* một biến chưa gán cục bộ, Python tự tìm ra Global Scope.

```python
total_budget = 1000  # Global scope

def calculate_remaining(spent):
    total_budget = 500  # Local scope (che khuất biến global, không sửa global)
    return total_budget - spent

print(calculate_remaining(200))  # 300
print(total_budget)              # 1000 (biến global không đổi)
```

## 4. Xử lý ngoại lệ (Exception Handling)

- **Error vs. Exception:** *Errors* (như `SyntaxError`) thường do sai cú pháp hoặc hệ thống và khó bắt khi chạy; *Exceptions* (như `ZeroDivisionError`, `ValueError`, `FileNotFoundError`, `IndexError`, `KeyError`, `TypeError`, `AttributeError`, `ImportError`, `IOError`) xảy ra trong lúc thực thi (runtime) và có thể bắt để chương trình không bị sập.
- **Khối `try - except - else - finally`:**
  - `try`: chứa đoạn code có nguy cơ phát sinh ngoại lệ.
  - `except SpecificError`: bắt và xử lý đúng loại lỗi tương ứng (tránh dùng `except:` chung chung vì sẽ che giấu nguyên nhân lỗi khi debug).
  - `else`: chỉ chạy khi khối `try` **không** có lỗi nào xảy ra.
  - `finally`: **luôn luôn chạy** dù có lỗi hay không (thường dùng để đóng file/kết nối).

```python
try:
    b = int(input("Nhập số chia: "))
    result = 10 / b
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
else:
    print("Thành công! Kết quả =", result)
finally:
    print("Hoàn tất khối xử lý.")
```

## 5. Đối tượng & Lớp (Objects and Classes — OOP)

Mọi giá trị trong Python (`int`, `str`, `list`, `dict`...) đều là **object** (instance của một **class**), có **type** (`type(obj)`), **attributes** (dữ liệu/trạng thái) và **methods** (hàm gắn với đối tượng). Dùng `dir(obj)` để liệt kê toàn bộ thuộc tính và phương thức của đối tượng.

- **Class (`class ClassName:`):** Bản thiết kế (blueprint) định nghĩa thuộc tính chung (**class attributes**) và hành vi của đối tượng.
- **`__init__(self, ...)` (Constructor):** Phương thức đặc biệt tự chạy khi khởi tạo đối tượng (`obj = ClassName(...)`), dùng `self` để gán giá trị vào **instance attributes** riêng biệt cho từng đối tượng.

```python
class Circle(object):
    # Constructor với giá trị mặc định
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Instance method luôn nhận self làm tham số đầu tiên
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

c1 = Circle(4, 'yellow')   # radius=4, color='yellow'
c2 = Circle()              # dùng mặc định: radius=3, color='blue'
c2.radius = 10             # cập nhật trực tiếp attribute → radius=10, color vẫn là 'blue'
```

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Thụt lề (Indentation) sai ở khối `if/else` và vòng lặp:** Một lệnh `print()` không thụt lề sau `else:` sẽ luôn chạy bất kể nhánh nào được chọn.
2. **Quên `stop` không được bao gồm trong `range(start, stop)`:** `range(1, 5)` chỉ sinh `1, 2, 3, 4` (không có `5`).
3. **Ghi đè tham số truyền vào trong `__init__`:** Nếu viết `self.id = id` rồi ngay sau đó `self.id = 80`, mọi instance dù truyền `Graph(200)` vẫn có `val.id == 80`.
4. **Dùng `except:` trần (bare except) trong codebase lớn:** Bắt tất cả ngoại lệ mà không phân loại sẽ khiến bạn mất hàng giờ debug vì không biết lỗi thực sự là `FileNotFoundError`, `ValueError` hay `TypeError`. Hãy bắt từng exception cụ thể!
5. **Nhầm `sorted(L)` sửa list gốc:** `sorted(L)` không thay đổi `L`; nếu viết `L = [1, 3, 2]; sorted(L)`, giá trị của `L` vẫn là `[1, 3, 2]`.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- `if/elif/else` điều hướng rẽ nhánh theo biểu thức Boolean; so sánh chuỗi phân biệt hoa-thường.
- `for` phù hợp duyệt sequence/range biết trước; `enumerate()` cung cấp đồng thời cả index lẫn giá trị; `while` lặp theo điều kiện dừng.
- Biến trong hàm mặc định thuộc local scope; luôn viết docstring và dùng `try-except-else-finally` với từng exception cụ thể.
- Class là khuôn mẫu tạo Object; `__init__` khởi tạo instance attributes qua `self`, còn method thay đổi trạng thái nội bộ mà vẫn giữ nguyên kiểu của object.
