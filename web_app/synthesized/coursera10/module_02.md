# Module 2: Python Data Structures

> **Tư tưởng cốt lõi:** Python cung cấp 4 cấu trúc dữ liệu ghép (compound data structures) cốt lõi cho mọi bài toán dữ liệu: **Tuple** (có thứ tự, bất biến), **List** (có thứ tự, khả biến), **Dictionary** (ánh xạ key bất biến duy nhất → value), và **Set** (tập hợp không thứ tự, phần tử duy nhất hỗ trợ toán tập hợp).

## 1. So sánh 4 cấu trúc dữ liệu cốt lõi

| Cấu trúc | Cú pháp khởi tạo | Thứ tự (Ordered) | Khả biến (Mutable) | Trùng lặp phần tử | Truy cập phần tử |
| --- | --- | --- | --- | --- | --- |
| **Tuple** | `(1, 2, 'a')` | Có (Indexed) | **Không** (Immutable) | Cho phép | Theo index `t[0]`, `t[-1]` |
| **List** | `[1, 2, 'a']` | Có (Indexed) | **Có** (Mutable) | Cho phép | Theo index `L[0]`, `L[-1]` |
| **Dictionary** | `{"k": 1, "m": 2}` | Có thứ tự chèn (Python 3.7+) | **Có** (Key bất biến & duy nhất) | Key: **Không**; Value: Có | Theo key `d["k"]` |
| **Set** | `{"a", "b"}`, `set()` | **Không** (Unordered) | **Có** (Thêm/xóa phần tử) | **Không** (Tự loại trùng) | Không dùng index; kiểm tra bằng `in` |

> **Lưu ý khởi tạo rỗng:** `{}` tạo ra một **Dictionary rỗng**, *không phải* Set rỗng! Muốn tạo Set rỗng bắt buộc viết `set()`.

## 2. Tuples — Chuỗi bất biến (Immutable Sequences)

- **Đặc trưng:** Gom nhiều kiểu dữ liệu (`int`, `float`, `str`, thậm chí `list` và `tuple` lồng nhau) vào dấu ngoặc tròn `(...)`.
- **Bất biến (Immutability):** Không thể thay đổi, thêm hay xóa phần tử sau khi tạo. Nếu muốn sắp xếp một tuple, hàm `sorted(t)` không sửa `t` mà trả về một **list mới** đã sắp xếp.
- **Lồng nhau (Nesting) & Slicing:**
  - `A = ((11, 12), [21, 22])` → `A[1]` là `[21, 22]`; `A[1][0]` là `21`.
  - `say_what = ('say', 'what', 'you', 'will')` → `say_what[-1]` là `'will'`.
  - `A = (1, 2, 3, 4, 5)` → `A[1:4]` trả về `(2, 3, 4)` (từ index 1 đến 3).

```python
ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
print(len(ratings))              # 9
print(ratings.count(10))         # 2
print(ratings.index(6))          # 2 (vị trí xuất hiện đầu tiên)

sorted_ratings = sorted(ratings) # Trả về LIST [2, 5, 6, 6, 8, 9, 9, 10, 10], ratings giữ nguyên!

# Cẩn thận tuple lồng list: bản thân tuple không đổi reference, nhưng list bên trong vẫn sửa được
nested = ((1), [2, 3], [4])
print(nested[2])                 # [4]
```

## 3. Lists — Chuỗi khả biến & Bẫy Aliasing

List dùng ngoặc vuông `[...]`, có thể chứa phần tử hỗn hợp và lồng ghép (`B = [1, 2, [3, 'a'], [4, 'b']]` → `B[3][1] == 'b'`).

### A. Phương thức biến đổi List quan trọng

| Thao tác / Phương thức | Hành vi | Ví dụ & Kết quả |
| --- | --- | --- |
| `L.append(x)` | Thêm `x` làm **1 phần tử duy nhất** vào cuối list (in-place) | `A = [1]; A.append([2, 3, 4, 5])` → `len(A) == 2`, `A == [1, [2, 3, 4, 5]]` |
| `L.extend(iter)` | Bung từng phần tử của `iter` nối vào cuối list (in-place) | `A = [1]; A.extend([2, 3])` → `len(A) == 3`, `A == [1, 2, 3]` |
| `L + L2` | Nối 2 list tạo ra **list mới** | `[1, 2, 3] + [1, 1, 1]` → `[1, 2, 3, 1, 1, 1]` |
| `L.insert(i, x)` | Chèn `x` vào vị trí `i` | `L.insert(2, 6)` |
| `del(L[i])` / `L.pop(i)` | `del` xóa tại index `i`; `pop(i)` xóa và **trả về** giá trị bị xóa (mặc định phần tử cuối) | `A = ["hard rock", 10, 1.2]; del(A[1])` → `["hard rock", 1.2]` |
| `L.remove(val)` | Xóa phần tử **đầu tiên** có giá trị bằng `val` (lỗi `ValueError` nếu không thấy) | `L.remove(30)` |
| `L.sort()` vs `sorted(L)` | `L.sort()` sắp xếp **trực tiếp trên `L`** (trả về `None`); `sorted(L)` trả về **list mới** | `B.sort(reverse=True)` |
| `s.split(delim)` | Chuyển chuỗi thành list theo ký tự phân cách `delim` (mặc định khoảng trắng) | `"A,B,C".split(",")` → `["A", "B", "C"]` |

### B. Aliasing vs. Cloning (Bản sao độc lập)

- **Aliasing:** Khi viết `B = A` với `A` là list, cả `A` và `B` **cùng trỏ về một vùng nhớ duy nhất**. Sửa `A[0] = "banana"` sẽ làm `B[0]` tự động đổi theo!
- **Cloning:** Để tạo bản sao độc lập (shallow copy), dùng `B = A[:]` hoặc `B = A.copy()`. Khi đó thay đổi `A` không ảnh hưởng đến `B`.

```python
A = ["hard rock", 10, 1.2]
B = A          # Aliasing: cùng tham chiếu 1 list
C = A[:]       # Cloning (hoặc A.copy()): tạo list mới độc lập

A[0] = "banana"
print(B[0])    # "banana" (bị ảnh hưởng!)
print(C[0])    # "hard rock" (an toàn!)
```

## 4. Dictionaries — Ánh xạ Key-Value

Dictionary lưu dữ liệu theo cặp `key: value` trong `{...}`:
- **Key:** Phải **duy nhất** (unique) và **bất biến** (immutable — như `str`, `int`, `tuple`), đóng vai trò như "địa chỉ" tra cứu $O(1)$.
- **Value:** Có thể bất biến hoặc khả biến (`list`, `tuple`, `dict` khác...) và được phép trùng lặp.

```python
inventory = {"shirt": 45, "pants": 20, "shoes": 15, "hat": 5}

# Tra cứu, thêm mới, cập nhật và xóa
print(inventory["shirt"])         # 45 (dùng inventory.get("coat") để tránh KeyError)
inventory["scarf"] = 12           # Thêm key mới
inventory["hat"] = 10             # Ghi đè value cũ nếu key đã tồn tại
del inventory["pants"]            # Xóa cặp key-value (raises KeyError nếu thiếu)

# Kiểm tra key & trích xuất danh sách
print("shirt" in inventory)       # True (chỉ kiểm tra trong KEYS, không kiểm tra values!)
keys_list = list(inventory.keys())      # ['shirt', 'shoes', 'hat', 'scarf']
vals_list = list(inventory.values())    # [45, 15, 10, 12]
items_list = list(inventory.items())    # [('shirt', 45), ...]
```

## 5. Sets — Tập hợp duy nhất & Toán tập hợp (Venn Diagram)

Set là tập hợp **không có thứ tự** (không hỗ trợ index `s[0]`) và **chỉ chứa phần tử duy nhất** (tự động loại bỏ bản sao khi khởi tạo hoặc ép kiểu `set(my_list)`).

| Thao tác / Phương thức | Toán tử tương đương | Ý nghĩa | Ví dụ |
| --- | --- | --- | --- |
| `S.add(x)` | — | Thêm `x` vào `S` (trả về `None`, không làm gì nếu `x` đã có) | `V = {'A', 'B'}; V.add('C')` → `V` thành `{'A', 'B', 'C'}` |
| `S.remove(x)` | — | Xóa `x` khỏi `S` (**báo `KeyError`** nếu `x` không tồn tại) | `S.remove('A')` |
| `A.intersection(B)` | `A & B` | Giao: phần tử có trong **cả A và B** | `{'a', 'b'} & {'a'}` → `{'a'}` |
| `A.union(B)` | `A \| B` | Hợp: toàn bộ phần tử duy nhất từ **A hoặc B** | `A.union(B)` |
| `A.difference(B)` | `A - B` | Hiệu: phần tử thuộc `A` nhưng **không thuộc `B`** | `{'a', 'b'} - {'a'}` → `{'b'}` |
| `A.symmetric_difference(B)` | `A ^ B` | Phần tử chỉ nằm ở 1 trong 2 tập | `A.symmetric_difference(B)` |
| `A.issubset(B)` / `A.issuperset(B)` | `A <= B` / `A >= B` | Kiểm tra tập con / tập cha (`True`/`False`) | `{'A'}.issubset({'A', 'B'})` → `True` |

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm `append()` với `extend()`:** `A = [1]; A.append([2, 3, 4, 5])` tạo ra list lồng `[1, [2, 3, 4, 5]]` có **`len(A) == 2`**, KHÔNG phải `5`! Muốn nối phẳng từng phần tử phải dùng `extend()`.
2. **Gán `L2 = L1.sort()`:** `list.sort()` sửa trực tiếp danh sách gốc và **trả về `None`**, nên `L2` sẽ nhận `None`! Nếu cần giữ list gốc và nhận list mới đã sắp xếp, hãy dùng `L2 = sorted(L1)`.
3. **Aliasing ngoài ý muốn khi truyền List vào biến/hàm:** Viết `b = a` không tạo bản sao; hãy dùng `a.copy()` hoặc `a[:]` khi cần tách biệt trạng thái.
4. **Dùng toán tử `+` trên Set:** `A + B` trên hai Set gây `TypeError`! Để hợp hai tập hợp phải dùng `A.union(B)` hoặc `A | B`.
5. **Bẫy `V.add('C')` và `set()` rỗng:** `V.add('C')` thay đổi tập `V` tại chỗ (in-place) thành `{'A', 'B', 'C'}` (giá trị trả về của lời gọi hàm là `None`). Ngoài ra, `{'A', 'A'}` tự rút gọn thành `{'A'}`.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Tuple** `( )` dùng cho dữ liệu cố định (immutable, có thứ tự); **List** `[ ]` dùng cho chuỗi thay đổi được (mutable, có thứ tự).
- **Dictionary** `{k: v}` ánh xạ key bất biến-duy nhất tới value bất kỳ; dùng `list(d.keys())`, `list(d.values())`, `list(d.items())` để trích xuất danh sách.
- **Set** `{x, y}` hoặc `set(list_obj)` loại bỏ trùng lặp tức thì và tối ưu cho phép kiểm tra `in` cũng như giao (`&`), hợp (`|`), hiệu (`-`), tập con (`issubset()`).
- Luôn phân biệt thao tác **in-place** (`append`, `sort`, `add`, `remove`) với thao tác **trả về đối tượng mới** (`+`, `sorted()`, `copy()`, `union()`).
