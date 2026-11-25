# Module 3: JavaScript Programming for Web Applications

> **Tư tưởng cốt lõi:** JavaScript là ngôn ngữ kịch bản động chạy trên trình duyệt giúp thao tác cây DOM, xử lý sự kiện và biến trang web tĩnh thành ứng dụng tương tác; làm chủ ES6 (`let`/`const`, arrow functions, array methods), cơ chế ép kiểu động, Prototype và chuẩn DOM APIs là nền tảng bắt buộc trước khi bước sang React.

## 1. Vai trò của JavaScript, cách nhúng vào HTML và cơ chế xuất dữ liệu

- **Vai trò cốt lõi:** JavaScript chạy phía client (client-side script) ngay trong trình duyệt để:
  - Thao tác cấu trúc, nội dung và kiểu dáng của **DOM** động mà không cần tải lại toàn bộ trang.
  - Xử lý **sự kiện (Event Handling)**: click chuột, nhập liệu, submit form, cuộn trang.
  - Xác thực dữ liệu biểu mẫu (form validation) theo thời gian thực.
- **Hai cách nhúng `<script>` vào HTML:**
  1. **Internal script:** `<script>/* mã ngắn */</script>` — chỉ phù hợp đoạn mã rất ngắn.
  2. **External script (Khuyến nghị):** `<script src="app.js"></script>` — tái sử dụng qua nhiều trang, dễ bảo trì, tận dụng cache trình duyệt.
- **Thẻ `<noscript>`:** Cung cấp nội dung thông báo hoặc phương án thay thế hiển thị cho người dùng khi trình duyệt **tắt JavaScript** hoặc không hỗ trợ script.
- **Các cách hiển thị / xuất thông tin chuẩn trong JavaScript:**
  - `console.log(...)`: In ra bảng điều khiển DevTools (dùng nhiều nhất khi debug).
  - `window.alert(...)`: Hiện hộp thoại cảnh báo.
  - `element.innerHTML = "..."` / `element.textContent = "..."`: Ghi nội dung động trực tiếp vào phần tử HTML trên trang (`innerHTML` phân tích cả thẻ HTML để định dạng).
  - `document.write(...)`: Ghi trực tiếp vào luồng tài liệu (chỉ dùng thử nghiệm, tránh dùng sau khi trang đã load xong).

## 2. Biến (`var`, `let`, `const`), Quy tắc đặt tên và Kiểu dữ liệu động

### So sánh 3 từ khóa khai báo biến

| Từ khóa | Phạm vi (Scope) | Gán lại giá trị (Reassign) | Khuyến nghị ES6+ |
| --- | --- | --- | --- |
| `var` | **Function-scoped** (phạm vi hàm) | Có | Hạn chế dùng (dễ lỗi hoisting & rò rỉ scope khỏi `if`/`for`) |
| `let` | **Block-scoped** (phạm vi `{ ... }`) | Có | Dùng mặc định cho biến có thay đổi giá trị |
| `const` | **Block-scoped** (phạm vi `{ ... }`) | **Không** (không thể gán lại tham chiếu) | Dùng mặc định cho hằng số, hàm, mảng/object không gán lại tham chiếu |

- **Quy tắc đặt tên biến hợp lệ:**
  - Chỉ bắt đầu bằng chữ cái (`a-z`, `A-Z`), dấu gạch dưới `_` hoặc `$` — **KHÔNG được bắt đầu bằng chữ số** (vd: `10car` là **KHÔNG hợp lệ**!).
  - Phân biệt chữ hoa/thường (`userName` ≠ `username`), không dùng từ khóa ngôn ngữ (`let`, `return`, `class`).
- **Kiểu dữ liệu động (Dynamic Typing) & Ép kiểu ngầm (Type Coercion):**
  - Biến và tham số hàm trong JavaScript không khai báo kiểu cố định; kiểu được xác định theo giá trị tại thời điểm chạy (runtime).
  - Toán tử `+` thực hiện **cộng số học** nếu hai vế là số, nhưng thực hiện **nối chuỗi (concatenation)** ngay khi gặp một chuỗi (đánh giá từ trái sang phải):

```javascript
var total = 10 + 1 + "3";
// Bước 1: 10 + 1 = 11 (number)
// Bước 2: 11 + "3" = "113" (string!)
console.log(total); // "113"
```

## 3. Hàm (Functions), Đối tượng (Objects) và Prototypes

- **Parameterized vs. Non-parameterized Functions:**
  - *Non-parameterized:* Không nhận tham số đầu vào, tự thực thi dựa trên logic nội bộ hoặc trạng thái ngoài.
  - *Parameterized:* Nhận một hoặc nhiều tham số đầu vào để xử lý linh hoạt; **không khai báo kiểu tham số hay kiểu trả về** — một hàm `add(a, b)` có thể trả về `number` nếu truyền số hoặc `string` nếu truyền chuỗi.
- **Function Declaration vs. Function Expression:**

```javascript
// 1. Function Declaration
function add(a, b) {
  return a + b;
}

// 2. Function Expression — gán hàm (thường là hàm ẩn danh) vào một biến
const multiply = function (a, b) {
  return a * b;
};

// 3. ES6 Arrow Function
const square = (x) => x * x;
```

- **Constructor Function, Custom Objects & Prototypes:**
  - Có thể thêm thuộc tính/phương thức cho một đối tượng cụ thể bằng dấu chấm (`house.color = "blue"`) hoặc ngoặc vuông (`house["color"] = "blue"`).
  - **Prototype:** Cho phép định nghĩa thuộc tính/phương thức dùng chung cho **toàn bộ các thể hiện (instances)** tạo ra từ cùng một hàm khởi tạo:

```javascript
function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
}

// Gắn phương thức chung qua prototype (tiết kiệm bộ nhớ cho mọi instance)
Car.prototype.describe = function () {
  return `${this.year} ${this.make} ${this.model}`;
};

const c = new Car("Meridian", "Saber GT", 2012);
c.color = "Red";       // Cách 1: dot notation
c["owner"] = "Kevin";  // Cách 2: bracket notation
```

## 4. Mảng (Arrays) và 5 Phương thức Mảng Cốt Lõi (Array Methods)

Mảng trong JavaScript có chỉ số bắt đầu từ **0 (zero-indexed)** và có thể chứa hỗn hợp nhiều kiểu dữ liệu.

| Phương thức | Chức năng chính | Trả về mảng mới? | Trường hợp sử dụng điển hình |
| --- | --- | --- | --- |
| `forEach(cb)` | Duyệt từng phần tử và thực thi hành động (side-effect) | Không (`undefined`) | Gửi email chào mừng cho từng user, ghi log |
| `map(cb)` | Biến đổi từng phần tử theo hàm ánh xạ | **Có** (cùng độ dài) | Trích xuất danh sách tên từ mảng object, render list UI |
| `filter(cb)` | Lọc giữ lại các phần tử thỏa điều kiện `true` | **Có** (độ dài ≤ gốc) | Lọc sản phẩm còn hàng, lọc đơn giá > 100 |
| `reduce(cb, init)` | Gộp toàn bộ mảng thành **một giá trị duy nhất** | Không (trả giá trị tích lũy) | **Tính tổng giá trị đơn hàng**, đếm tần suất |
| `find(cb)` | Tìm và trả về **phần tử đầu tiên** thỏa điều kiện | Không (1 phần tử hoặc `undefined`) | Tìm user theo `id` hoặc `email` |

```javascript
const orders = [{ id: 1, price: 120 }, { id: 2, price: 80 }, { id: 3, price: 200 }];

// Tính tổng toàn bộ giá đơn hàng bằng reduce()
const totalRevenue = orders.reduce((acc, item) => acc + item.price, 0); // 400
```

## 5. Cây DOM, Đối tượng Trình duyệt (BOM) và Node Types

### Hệ phân cấp DOM & BOM cơ bản

```text
window (đỉnh cao nhất, điều khiển môi trường trình duyệt)
 ├── document  (tài liệu HTML hiện tại — cổng vào cây DOM)
 │     ├── forms["form1"]["field1"]
 │     ├── images, links, anchors
 │     └── getElementById(), getElementsByTagName(), querySelector()
 ├── history   (lịch sử duyệt trang: back(), forward())
 ├── location  (thông tin URL hiện tại: href, pathname, reload())
 └── navigator (thông tin trình duyệt & thiết bị người dùng)
```

### Bảng hằng số `nodeType` trong W3C DOM Level 2 (rất hay hỏi trong Quiz!)

| Tên hằng số (`Node.*`) | Giá trị số nguyên | Ý nghĩa trong cây DOM |
| --- | :---: | --- |
| `ELEMENT_NODE` | **`1`** | Thẻ phần tử HTML (vd: `DIV`, `P`, `IMG`) |
| `ATTRIBUTE_NODE` | **`2`** | Thuộc tính của thẻ (vd: `id="div123"`) |
| `TEXT_NODE` | **`3`** | Chuỗi văn bản bên trong phần tử (`nodeName = "#text"`) |
| `COMMENT_NODE` | **`8`** | Chú thích HTML (`<!-- ... -->`) không hiển thị ra giao diện |
| `DOCUMENT_NODE` | **`9`** | Gốc tài liệu (`document`) |

### Các hàm truy xuất & thao tác DOM thiết yếu

```javascript
// 1. Lấy duy nhất 1 phần tử theo ID và đổi viền/nội dung có định dạng
const box = document.getElementById("example_id");
box.style.border = "2px solid red";
box.innerHTML = "<strong>Đã cập nhật nội dung!</strong>";

// 2. Lấy toàn bộ phần tử theo tên thẻ (trả về HTMLCollection / NodeList)
const allImages = document.getElementsByTagName("img");

// 3. Truy cập trường "field1" nằm trong form "form1"
const fieldValue = document.forms["form1"]["field1"].value;
```

## 6. Best Practices & Bẫy thường gặp (Critical Pitfalls)

- **Best Practices từ chuyên gia:**
  1. Sử dụng **IDE hiện đại** (VS Code, WebStorm) để tận dụng autocomplete và tra cứu tài liệu tại chỗ.
  2. Dùng **Linter** (như ESLint) để giữ chuẩn code đồng nhất trong nhóm, giảm xung đột khi merge Git.
  3. **Mô-đun hóa mã nguồn (Modularization):** Tách nhỏ hàm/module để dễ viết Unit Test và tái sử dụng.
- **Bẫy thường gặp:**
  1. **Nhầm `10 + 1 + "3"` ra `14`:** Do JavaScript đánh giá từ trái sang phải, `10 + 1` là `11`, sau đó `11 + "3"` bị ép sang nối chuỗi thành `"113"`.
  2. **Nhầm `getElementById` (số ít) với `getElementsByTagName` (số nhiều):** `getElementById` trả về 1 phần tử; `getElementsByTagName` trả về danh sách (NodeList/HTMLCollection).
  3. **Đặt tên biến bắt đầu bằng số (`10car`):** Gây `SyntaxError` ngay lập tức.
  4. **Gán lại biến `const`:** Sẽ ném `TypeError: Assignment to constant variable`. (Lưu ý: với object/array khai báo `const`, không thể gán lại biến sang object khác nhưng *có thể* sửa thuộc tính bên trong).

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- Ưu tiên `const` và `let` (block scope) thay vì `var` (function scope).
- Nhớ chính xác 4 mã số DOM Node hay thi: `ELEMENT_NODE = 1`, `ATTRIBUTE_NODE = 2`, `TEXT_NODE = 3`, `COMMENT_NODE = 8`.
- `reduce()` để tính tổng/gộp giá trị; `filter()` để lọc; `map()` để biến đổi; `forEach()` để duyệt thực hiện hành động.
- Truy cập form theo chuẩn DOM: `document.forms["form1"]["field1"]`; chèn nội dung kèm định dạng HTML dùng `innerHTML`; luôn bọc thông báo dự phòng bằng `<noscript>`.
