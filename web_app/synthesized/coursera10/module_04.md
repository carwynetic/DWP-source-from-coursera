# Module 4: Working with Data in Python

> **Tư tưởng cốt lõi:** Làm việc với dữ liệu trong Python trải qua 3 tầng công cụ: đọc/ghi file thô an toàn bằng `with open()`, xử lý dữ liệu dạng bảng có nhãn (`Series`, `DataFrame`) với **Pandas**, và tính toán đại số tuyến tính/mảng đa chiều hiệu năng cao (vectorization, matrix multiplication) với **NumPy**.

## 1. Đọc và ghi tệp với `open()` & `with` Context Manager

Hàm dựng sẵn `open(file_path, mode)` tạo ra một **file object** để tương tác với file trên đĩa. Thực hành chuẩn luôn dùng khối **`with open(...) as f:`** vì Python tự động đóng file ngay khi thoát khối thụt lề (kể cả khi gặp ngoại lệ), tránh rò rỉ tài nguyên.

### A. Các chế độ mở file (File Modes)

| Mode | Ý nghĩa | Hành vi khi file đã tồn tại / chưa tồn tại |
| --- | --- | --- |
| `'r'` | **Read** (mặc định text) | Chỉ đọc; báo `FileNotFoundError` nếu file chưa tồn tại |
| `'w'` | **Write** | Tạo file mới nếu chưa có; **ghi đè xóa sạch** nội dung cũ nếu đã tồn tại |
| `'a'` | **Append** | Tạo file mới nếu chưa có; **ghi nối tiếp vào cuối** file mà không xóa dữ liệu cũ |
| `'x'` | **Exclusive create** | Tạo file mới để ghi; báo lỗi nếu file đã tồn tại |
| `'rb'` / `'wb'` | **Binary** read / write | Đọc/ghi dữ liệu nhị phân (ảnh, âm thanh, model) |
| `'r+'` / `'w+'` / `'a+'` | Đọc & Ghi kết hợp | Đọc-ghi từ đầu (`r+`), ghi đè rồi đọc (`w+`), nối cuối và đọc (`a+`) |

### B. Thuộc tính & Phương thức đọc/ghi

- **Thuộc tính file object:** `file1.name` trả về tên/đường dẫn file; `file1.mode` trả về chế độ đang mở (`'r'`, `'w'`...); `file1.closed` kiểm tra đã đóng chưa.
- **Đọc dữ liệu:**
  - `file1.read()` đọc toàn bộ file thành 1 `str` (hoặc `file1.read(n)` đọc `n` ký tự tiếp theo).
  - `file1.readline()` đọc **1 dòng** mỗi lần gọi (gọi lần 1 được dòng 1, gọi lần 2 được dòng 2).
  - `file1.readlines()` đọc toàn bộ thành **list các chuỗi** (mỗi phần tử là 1 dòng kèm `\n`).
  - `file1.seek(offset)` di chuyển con trỏ đọc/ghi tới vị trí byte mong muốn.
- **Ghi dữ liệu:** `file1.write("Line A\n")` ghi chuỗi (cần `\n` để xuống dòng); `file1.writelines(list_of_lines)` ghi cả danh sách chuỗi.

```python
# Đọc 2 dòng đầu tiên an toàn với 'with'
with open("Example1.txt", "r") as file1:
    for _ in range(2):
        print(file1.readline().strip())

# Sao chép nội dung từ source sang destination
with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
    for line in src:
        dst.write(line)
```

## 2. Pandas — Xử lý dữ liệu bảng (Series & DataFrame)

Pandas (`import pandas as pd`) xây dựng trên nền NumPy, cung cấp hai cấu trúc chính: **`Series`** (mảng 1 chiều có nhãn/index) và **`DataFrame`** (bảng 2 chiều gồm các hàng và cột có nhãn, kiểu dữ liệu từng cột có thể khác nhau).

### A. Nạp, khởi tạo & lưu DataFrame

```python
import pandas as pd

# 1. Đọc từ file CSV hoặc Excel
df = pd.read_csv("songs.csv")
df_xls = pd.read_excel("songs.xlsx")

# 2. Tạo DataFrame từ Dictionary (keys -> tên cột, values là list -> các hàng)
songs = {
    "Artist": ["AC/DC", "Michael Jackson", "Pink Floyd"],
    "Released": [1980, 1982, 1973],
    "Length": ["00:42:11", "00:42:19", "00:42:49"],
    "Genre": ["Rock", "Pop", "Prog Rock"]
}
df = pd.DataFrame(songs)

# 3. Xem nhanh & xuất file
df.head(5)     # 5 dòng đầu; df.tail(5) xem 5 dòng cuối; df.info(), df.describe()
df.to_csv("output.csv", index=False)
```

### B. Truy xuất, lọc & trích xuất dữ liệu

| Thao tác | Cú pháp | Lưu ý quan trọng |
| --- | --- | --- |
| **Chọn 1 cột (DataFrame)** | `df[['Artist']]` | Ngoặc kép đôi `[[]]` trả về `DataFrame`; ngoặc đơn `df['Artist']` trả về `Series` |
| **Chọn nhiều cột** | `y = df[['Artist', 'Length', 'Genre']]` | Tạo DataFrame mới chỉ chứa các cột liệt kê |
| **Truy cập theo vị trí số (`iloc`)** | `df.iloc[0, 0]`, `df.iloc[6, 4]` | Chỉ số **bắt đầu từ 0**: hàng thứ 7, cột thứ 5 là `df.iloc[6, 4]` |
| **Truy cập theo nhãn (`loc`)** | `df.loc[1, 'Artist']`, `df.loc[2:5, 'Album']` | Với `loc`, lát cắt `2:5` **bao gồm cả index 5** (hàng thứ 3 đến hàng thứ 6)! |
| **Giá trị duy nhất** | `df['Released'].unique()` | Trả về mảng các giá trị không trùng lặp trong cột |
| **Lọc theo điều kiện** | `df1 = df[df['Released'] > 1979]` | Kết hợp nhiều điều kiện bằng `&` (và), `\|` (hoặc) kèm dấu ngoặc `(...)` |
| **Làm sạch & tổng hợp** | `df.dropna()`, `df.duplicated()`, `df.drop(..., axis=1)` | `axis=1` là cột, `axis=0` là hàng; `groupby(...).agg(...)`, `pd.merge()` |

## 3. NumPy — Mảng 1D, 2D & Đại số tuyến tính

NumPy (`import numpy as np`) là thư viện nền tảng của Pandas và khoa học dữ liệu, triển khai bằng C/Fortran nên nhanh và tiết kiệm bộ nhớ hơn Python list nhiều lần. Mọi phần tử trong `numpy.ndarray` **cùng một kiểu dữ liệu** (`dtype`).

### A. Thuộc tính cốt lõi của `ndarray`

- `a.ndim`: Số chiều (rank) — `1` với vector 1D, `2` với ma trận 2D.
- `a.shape`: Tuple kích thước từng chiều — `(5,)` với vector 5 phần tử; `(3, 3)` với ma trận 3 hàng 3 cột.
- `a.size`: Tổng số phần tử trong mảng (`a.size == số hàng * số cột`).
- `a.dtype`: Kiểu phần tử (`int64`, `float64`...).

### B. Phép toán 1D (Vector) & 2D (Matrix)

```python
import numpy as np

# 1D Vector & Universal Functions (ufuncs)
u = np.array([1, 0])
v = np.array([0, 1])
print(u + v)               # array([1, 1]) - cộng từng phần tử (vector addition)
print(u * 2)               # array([2, 0]) - nhân vô hướng (scalar multiplication / broadcasting)

a = np.array([0, 1, 0, 1, 0])
b = np.array([1, 0, 1, 0, 1])
print(a * b)               # array([0, 0, 0, 0, 0]) - Hadamard product (nhân từng phần tử!)
print(np.dot(np.array([-1, 1]), np.array([1, 1])))  # 0 - Dot product (-1*1 + 1*1)

# Tạo lưới đều & hàm lượng giác
x = np.linspace(0, 2 * np.pi, num=100)
y = np.sin(x)              # Áp dụng sin() lên từng phần tử (element-wise)

# 2D Matrix & Truy cập
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(M[1, 2])             # 6 (hàng index 1, cột index 2)
print(M[:, 1])             # array([2, 5, 8]) (toàn bộ cột 1)

# Phép nhân ma trận (Matrix Multiplication)
A = np.array([[1, 2], [3, 4]])       # shape (2, 2)
B = np.array([[5, 6], [7, 8]])       # shape (2, 2)
C = np.dot(A, B)                     # Điều kiện: số cột của A == số hàng của B!
```

| Phép toán NumPy | Cú pháp | Ý nghĩa toán học & Điều kiện hình dạng |
| --- | --- | --- |
| **Cộng / Trừ phần tử** | `A + B`, `A - B` | Cùng `shape` (hoặc tương thích broadcasting) |
| **Hadamard Product** | `A * B` | Nhân **từng cặp phần tử tương ứng** (element-wise), giữ nguyên `shape` |
| **Scalar / Broadcasting** | `a + 1`, `a * 2` | Áp dụng phép toán lên mọi phần tử trong mảng |
| **Dot Product / Nhân ma trận** | `np.dot(A, B)` | Tích vô hướng (1D → 1 số vô hướng) hoặc nhân ma trận `(m, n) · (n, p) → (m, p)`; **bắt buộc số cột `A` == số hàng `B`** |
| **Thống kê & biến đổi** | `np.sum()`, `np.mean()`, `np.max()`, `A.T`, `A.reshape()` | Tổng, trung bình, cực đại, chuyển vị, đổi kích thước |

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Mở file bằng `'w'` khi chỉ muốn thêm dòng:** Mode `'w'` xóa sạch toàn bộ nội dung file cũ ngay khi mở! Luôn dùng `'a'` (append) để ghi nối tiếp.
2. **Lệch chỉ số 0-based trong `iloc` và `loc`:** Hàng thứ 7 và cột thứ 5 tương ứng với `df.iloc[6, 4]` (không phải `[7, 5]`). Đặc biệt `iloc` nhận index số nguyên (`df.iloc[6, 'Genre']` gây lỗi!), còn `loc` dùng nhãn (`df.loc[1, 'artist']` lấy hàng thứ 2 với index mặc định `0, 1, 2...`).
3. **Nhầm `A * B` với `np.dot(A, B)` trong NumPy:** Toán tử `*` thực hiện **Hadamard product** (nhân từng phần tử tương ứng), KHÔNG phải phép nhân ma trận trong đại số tuyến tính!
4. **Nhân ma trận sai kích thước:** Trước khi gọi `np.dot(A, B)`, luôn kiểm tra `A.shape[1] == B.shape[0]` (số cột của `A` bằng số hàng của `B`), không cần hai ma trận phải vuông hay cùng `shape`.
5. **Quên `index=False` khi xuất CSV:** `df.to_csv("out.csv")` mặc định ghi thêm cột index `0, 1, 2...` thành cột không tên trong file CSV.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Dùng `with open(path, mode) as f:` để tự động giải phóng file; phân biệt rõ `'r'`, `'w'`, `'a'` và `read()`, `readline()`, `readlines()`.
- Trong Pandas: tạo DataFrame từ `dict` hoặc `pd.read_csv()`; truy xuất bằng `iloc[row_idx, col_idx]` (vị trí) hoặc `loc[row_label, col_label]` (nhãn); lọc dữ liệu qua biểu thức Boolean và trích xuất giá trị riêng biệt bằng `.unique()`.
- Trong NumPy: `ndarray` chứa dữ liệu đồng nhất, thao tác vector hóa cực nhanh; nắm vững `ndim`, `shape`, `size`, `dtype`, phép `*` (element-wise) và `np.dot()` (dot/matrix product).
