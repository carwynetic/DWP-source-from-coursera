# Module 1: Python Basics

> **Tư tưởng cốt lõi:** Python là ngôn ngữ lập trình bậc cao, cú pháp rõ ràng, xử lý mọi giá trị dưới dạng đối tượng có kiểu dữ liệu xác định (`int`, `float`, `str`, `bool`); hiểu rõ cơ chế ép kiểu (typecasting), thứ tự ưu tiên toán tử (BODMAS), biến tham chiếu và tính bất biến (immutability) của chuỗi là nền tảng cho toàn bộ hệ sinh thái Data Science & AI.

## 1. Tổng quan hệ sinh thái Python & Jupyter Notebook

- **Vì sao chọn Python cho Data Science & AI?** Python là ngôn ngữ mục đích chung (general-purpose), dễ đọc, lượng code ngắn gọn hơn đáng kể so với Java/C++, sở hữu thư viện chuẩn phong phú (tự động hóa, web scraping, xử lý văn bản/ảnh, database) cùng hệ sinh thái chuyên sâu:
  - **Data Science & Scientific Computing:** `Pandas`, `NumPy`, `SciPy`, `Matplotlib`.
  - **AI & Machine Learning:** `Scikit-learn`, `TensorFlow`, `PyTorch`, `Keras`.
  - **NLP:** `NLTK` (Natural Language Toolkit).
  - **Giới hạn lưu ý:** Python *không* phổ biến trong lập trình phần cứng cấp thấp cho vi điều khiển (hardware-level programming for microcontrollers), nơi C/C++/Assembly chiếm ưu thế.
- **Jupyter Notebook / JupyterLab vs. Python Script (`.py`):**
  - Tên **Jupyter** ghép từ **Ju**lia, **Py**thon và **R** — môi trường tính toán tương tác đa ngôn ngữ qua kernel.
  - Khác với file `.py` truyền thống chạy tuần tự toàn bộ script, **Jupyter Notebook** chia thành các **cells** (Code cell & Markdown cell) cho phép thực thi từng phần độc lập, hiển thị ngay kết quả, biểu đồ, phương trình LaTeX và văn bản tường thuật trong cùng một tài liệu.
  - **Phím tắt & thao tác cốt lõi:** `Shift + Enter` để chạy cell hiện tại; nhấn `D` hai lần (`D, D`) để xóa cell đang chọn; dùng nút Stop (shutdown kernel) khi hoàn tất để giải phóng RAM (hiển thị `"no kernel"` ở góc trên phải).

## 2. Kiểu dữ liệu cơ bản (Data Types) & Ép kiểu (Typecasting)

Mọi dữ liệu trong Python đều có kiểu cụ thể, kiểm tra nhanh bằng hàm `type(x)`.

| Kiểu dữ liệu | Tên trong Python | Ví dụ | Đặc điểm & Lưu ý ép kiểu (Typecasting) |
| --- | --- | --- | --- |
| **Integer** | `int` | `-3, 0, 43, 100` | Số nguyên âm, dương hoặc 0. `int(3.99)` cắt phần thập phân thành `3` (**mất dữ liệu**, không làm tròn lên!). |
| **Float** | `float` | `1.0, 3.12323, -0.5` | Số thực dấu phẩy động. `float(2)` → `2.0`. Chuỗi số thực `"22.5"` phải ép bằng `float("22.5")`, nếu dùng `int("22.5")` sẽ báo `ValueError`. |
| **String** | `str` | `"Michael Jackson", '123'` | Chuỗi ký tự Unicode đặt trong nháy đơn hoặc nháy kép; **immutable** (bất biến). `str(22.5)` → `"22.5"`. |
| **Boolean** | `bool` | `True`, `False` | Bắt buộc viết hoa chữ đầu (`T`, `F`). Ép sang số: `int(True) == 1`, `int(False) == 0`, `float(True) == 1.0`. Ngược lại: `bool(0) == False`, mọi số khác 0 (`bool(1)`, `bool(-5)`) → `True`. |

```python
# Kiểm tra kiểu dữ liệu và ép kiểu
print(type(43))         # <class 'int'>
print(type(1.0))        # <class 'float'>
print(type(True))       # <class 'bool'>

# Ép kiểu an toàn vs. mất thông tin
print(int(3.99))        # 3 (cắt bỏ .99, KHÔNG làm tròn thành 4)
print(float("22.5"))    # 22.5 (dùng để tính toán từ dữ liệu API dạng chuỗi)
print(int(True), bool(0), bool(1))  # 1 False True
```

## 3. Biểu thức (Expressions), Toán tử & Biến (Variables)

- **Biểu thức** gồm **operands** (toán hạng) và **operators** (toán tử), thực thi theo quy ước toán học **BODMAS** (Ngoặc `()` → Lũy thừa `**` → Nhân/Chia `*`, `/`, `//`, `%` → Cộng/Trừ `+`, `-`).
- **Phép chia trong Python 3:**
  - `/` (Division): **luôn trả về `float`**, kể cả khi chia hết (`4 / 2` → `2.0`, `25 / 5` → `5.0`, `11 / 2` → `5.5`).
  - `//` (Floor / Integer Division): chia lấy phần nguyên (cắt phần thập phân hướng xuống âm vô cực): `11 // 2` → `5`, `25 // 6` → `4`.
  - `%` (Modulo): trả về phần dư (`9 % 4` → `1`).
- **Biến (Variables) & Tái gán (Reassignment):**
  - Toán tử gán `=` liên kết tên biến với giá trị. Python dùng **dynamic typing** — biến có thể được gán lại sang giá trị mới (thậm chí khác kiểu), ghi đè giá trị cũ.
  - Quy ước đặt tên: dùng `snake_case` rõ nghĩa (`total_min`, `total_hour`).

```python
# Thứ tự ưu tiên & biểu thức thực tế
total_bill = (40 + 12) * 1.15     # 59.8 (phải có ngoặc để cộng trước khi nhân 15% phí)
y = 2 * x * x - 3                 # Biểu diễn đúng cho y = 2x^2 - 3 (hoặc 2 * x**2 - 3)

# Tái gán và phép chia
x = 4
x = x / 2                         # x trở thành 2.0 (kiểu float!)
print(11 // 2, 11 / 2, 11 % 2)    # 5  5.5  1
```

## 4. Thao tác chuỗi (String Operations) & Định dạng chuỗi

Chuỗi là một **ordered sequence** (chuỗi có thứ tự), hỗ trợ đánh chỉ số dương từ `0` và chỉ số âm từ `-1` (ký tự cuối cùng).

### A. Indexing, Slicing & Stride

- **Indexing:** `name = "Michael Jackson"` (độ dài `len(name) == 15`) → `name[0] == "M"`, `name[-1] == "n"`, `name[-15] == "M"`.
- **Slicing `s[start:end]`:** Lấy từ `start` đến **`end - 1`** (không bao gồm `end`). Ví dụ với `text = "Hello World"`, `text[0:5]` trả về `"Hello"` (chỉ số 0, 1, 2, 3, 4 — không gồm khoảng trắng ở chỉ số 5).
- **Stride `s[start:end:step]`:** `name[::2]` lấy mỗi ký tự cách 2 bước; `name[0:5:2]` lấy các ký tự ở vị trí `0, 2, 4` → `"Mca"`.

### B. Tính bất biến (Immutability), Escape Sequences & Raw String

- **Strings are immutable:** Không thể sửa trực tiếp `s[0] = "J"` (sẽ gây `TypeError`). Phải tạo chuỗi mới bằng phép nối (`+`) hoặc nhân bản (`*`).
- **Phân biệt `+` trên `str` và số:** Với chuỗi, `+` là **concatenation** (ghép nối văn bản, không cộng toán học: `"1" + "1" == "11"`); với số, `+` là phép cộng đại số.
- **Escape sequences (`\`):** `\n` xuống dòng, `\t` tab, `\\` in ra một dấu gạch chéo ngược `\`.
- **Raw string (`r"..."`):** Vô hiệu hóa escape sequence — cực kỳ hữu ích cho đường dẫn Windows hoặc biểu thức chính quy (`r"C:\new_folder\file.txt"`).

```python
# Escape sequence vs Raw string cho đường dẫn Windows
path1 = "C:\\Users\\name\\Documents"    # Escape từng dấu \
path2 = r"C:\Users\name\Documents"      # Raw string: giữ nguyên literal \
print(path1 == path2)                   # True

print("AB\nC\nDE")
# Output:
# AB
# C
# DE
```

### C. Phương thức chuỗi (String Methods) & Format Strings

| Phương thức / Cú pháp | Chức năng | Ví dụ & Kết quả |
| --- | --- | --- |
| `s.upper()` / `s.lower()` | Đổi toàn bộ sang chữ HOA / thường (trả về chuỗi mới) | `"Hello".upper()` → `"HELLO"` |
| `s.replace(old, new)` | Thay thế chuỗi con | `"Michael Jackson".replace("Michael", "Janet")` |
| `s.find(sub)` | Trả về **index bắt đầu** của `sub` nếu thấy; **`-1` nếu không thấy** | `"helloMike".find("Mike")` → `5`; `"EMILY".find("L")` → `3` |
| `s.split(delim)` | Tách chuỗi theo `delim` thành **list** | `"1,2,3,4".split(",")` → `['1', '2', '3', '4']` |
| `s.strip()` | Xóa khoảng trắng thừa ở đầu và cuối chuỗi | `"  hi  ".strip()` → `"hi"` |
| `f"...{expr}..."` | **f-string** (Python 3.6+): nhanh, đọc dễ, hỗ trợ biểu thức bên trong `{}` | `f"Sum: {10 + 20}"` → `"Sum: 30"` |
| `"...{}".format(...)` | Định dạng bằng placeholder `{}` | `"Age: {}".format(30)` → `"Age: 30"` |
| `"...%s %d" % (...)` | Kiểu cũ (`%s` chuỗi, `%d` số nguyên) | `"%s is %d" % ("John", 30)` |

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm `11 // 2` với `11 / 2`:** `11 / 2` cho `5.5` (`float`), nhưng `11 // 2` là chia lấy nguyên nên kết quả là `5` (`int`), không làm tròn lên. Tương tự `int(3.99)` là `3`, không phải `4`.
2. **Viết thiếu dấu `\\` trong đường dẫn Windows:** Chuỗi `"C:\Users\name\Documents"` chỉ có một dấu `\`, khiến `\n` trong `\name` bị hiểu thành ký tự xuống dòng và `\U` gây `SyntaxError` (Unicode escape) trong Python! Phải dùng `"C:\\Users\\name\\Documents"` hoặc `r"C:\Users\name\Documents"`.
3. **Nhầm chỉ số kết thúc trong Slicing:** `s[0:5]` chỉ lấy 5 ký tự từ index `0` đến `4`, **không bao gồm** index `5`.
4. **Cố nối chuỗi với số bằng `+`:** `"Age: " + 25` gây `TypeError`. Phải ép `str(25)` hoặc dùng f-string `f"Age: {25}"`.
5. **Quên `find()` phân biệt hoa-thường & trả về `-1`:** `"helloMike".find("mike")` trả về `-1` vì `"M"` viết hoa khác `"m"`; `"helloMike".find("Mike")` mới trả về `5` (`h:0, e:1, l:2, l:3, o:4, M:5`).

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- Bốn kiểu dữ liệu nền tảng: `int`, `float`, `str`, `bool`; kiểm tra kiểu bằng `type()`.
- Phép `/` luôn sinh `float`; `//` cắt phần thập phân trả về phần nguyên; Python tuân thủ thứ tự BODMAS.
- String là chuỗi ký tự có thứ tự và **immutable**; hỗ trợ negative indexing (`-1` là phần tử cuối) và slicing `s[start:end:step]`.
- Mọi string method (`upper`, `replace`, `strip`, `split`) đều trả về đối tượng mới, không làm thay đổi chuỗi gốc.
- Ưu tiên **f-strings** cho chèn biến/biểu thức và **raw strings (`r"..."`)** khi xử lý chuỗi chứa nhiều dấu `\`.
