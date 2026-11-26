# Module 4: JavaScript Programming for Web Applications

> **Tư tưởng cốt lõi:** JavaScript là ngôn ngữ kịch bản (scripting language) định kiểu động chuẩn ECMAScript, mang lại hành vi tương tác và nội dung động cho trang web tĩnh thông qua việc thao tác trực tiếp cây **DOM** (với `window` ở đỉnh và `document` quản lý các node), kết hợp kiểm soát luồng, xử lý lỗi chuẩn hóa và các thực hành tốt (*best practices*) để tránh xung đột phạm vi toàn cục.

## 1. Biến, Kiểu dữ liệu Nguyên thủy vs. Wrapper Objects & Ép kiểu

JavaScript là ngôn ngữ **định kiểu động (*dynamically typed*)**: biến tự nhận kiểu dữ liệu tại thời điểm chạy dựa trên giá trị được gán.

### A. Khai báo biến (`var`, `let`, `const`) & Quy tắc đặt tên

- **Quy tắc định danh:** Tên biến có **phân biệt hoa/thường (*case-sensitive*)**, chỉ được bắt đầu bằng **chữ cái, dấu gạch dưới (`_`) hoặc ký tự đô-la (`$`)** — **không được bắt đầu bằng chữ số** (vd `10car` là tên biến **không hợp lệ**).
- **`var`:** Phạm vi hàm (**function-level scope**), có từ phiên bản JS đầu tiên.
- **`let` (ES6):** Phạm vi khối (**block-level scope** `{ ... }`), có thể gán lại giá trị nhưng không khai báo lại trong cùng block.
- **`const` (ES6):** Phạm vi khối (**block-level scope**), dùng cho hằng số — không thể gán lại hay khai báo lại.

### B. 5 Kiểu dữ liệu nguyên thủy (Primitives) & Kiểu phức hợp (Composite)

| Nhóm | Kiểu dữ liệu | Đặc điểm & Ví dụ |
| --- | --- | --- |
| **Primitive** | `number` | Biểu diễn cả số nguyên (thập phân `16`, bát phân `020`, thập lục phân `0x10`) lẫn số thực dấu phẩy động 64-bit, cộng thêm `NaN` và `Infinity` |
| **Primitive** | `string` | Chuỗi ký tự đặt trong nháy đơn hoặc nháy kép (vd `var pi = "3.14";` có kiểu **`string`**, không phải `float` hay `number`) |
| **Primitive** | `boolean` | Giá trị logic `true` hoặc `false` |
| **Primitive** | `undefined` | Biến đã khai báo nhưng chưa được gán giá trị (hoặc không tồn tại) |
| **Primitive** | `null` | Giá trị rỗng / vắng mặt đối tượng tường minh |
| **Composite** | `Array` & `Object` | `var array1 = [1, 2, 3];` (danh sách có chỉ số bắt đầu từ 0) và Object lưu cặp key-value |

- **Primitives vs. Wrapper Objects & Bẫy `===`:**
  - Giá trị nguyên thủy (`number`, `string`, `boolean`) không có phương thức riêng; JS có các **Wrapper Objects** viết hoa chữ cái đầu (`Number`, `String`, `Boolean`, `Array`, `Date`, `Error`) bọc giá trị nguyên thủy để cung cấp phương thức (như `(123).toString()` chuyển số thành chuỗi, hay `new Date()` lấy **thời gian cục bộ hiện tại — current local time**).
  - Vì `new String("Hello")` tạo ra một **Object**, còn `"Hello"` là **String primitive**, nên phép so sánh nghiêm ngặt (kiểm tra cả giá trị lẫn kiểu) `===` trả về `false`!

```javascript
// 1. Bẫy so sánh Wrapper Object vs. Primitive
var a = new String("Hello"); // typeof a === "object"
var b = "Hello";             // typeof b === "string"
if (a === b) {
  alert("Same");
} else {
  alert("Different");        // Kết quả chạy thực tế: "Different"
}

// 2. Bẫy cộng số và chuỗi từ trái sang phải (Type Coercion)
var total = 10 + 1 + " 3";   // 10 + 1 = 11 -> 11 + " 3" = "11 3" (Quiz Coursera ghi "113")
var strNum = (123).toString(); // Chuyển số 123 -> "123"
```

## 2. Kiểm soát luồng (Control Flow), Hàm (Functions) & Xử lý lỗi (Errors)

- **Câu lệnh điều kiện:** `if ... else if ... else`, *nested if-else*, **ternary operator** (`age >= 18 ? "yes" : "no"`), và **`switch` statement** (tối ưu nhất khi so sánh một giá trị với nhiều `case` khả dĩ và chạy khối lệnh của nhánh khớp đầu tiên).
- **Vòng lặp `for` chuẩn:** `for (var i = minVal; i < maxVal; i++) { ... }` (gồm 3 phần cách nhau bởi dấu `;`: khởi tạo; điều kiện; bước tăng). Ngoài ra có `while`.
- **Định nghĩa hàm không tham số chuẩn:** `function myFunction() { }` (dùng từ khóa `function`, tên hàm, cặp ngoặc đơn `()`, thân hàm `{ }`).
- **Hệ thống Error Objects trong JavaScript:**
  - Ngoài `Error` chung, JavaScript có **6 loại lỗi cốt lõi (6 core types of errors)**: `EvalError`, `RangeError` (giá trị/tham số số nằm ngoài khoảng hợp lệ), `ReferenceError`, `SyntaxError`, `TypeError`, `URIError`.
  - Mỗi instance của `Error` chứa **2 thuộc tính** mô tả lỗi: **`name`** (tên loại lỗi) và **`message`** (mô tả chi tiết lỗi) — *không phải chỉ 1 thuộc tính*.
  - Để ném lỗi tùy biến, dùng `throw new Error("Thông báo lỗi")` hoặc kế thừa lớp `Error` (`class InputError extends Error {}`), **không** truyền 2 chuỗi kiểu `new Error("InputError", "msg")` để mong đặt `name`.

## 3. Client-Side Scripting, Event Binding & Hệ phân cấp DOM

### A. Nhúng Script, `<noscript>` và Event Binding

```html
<!-- Cách 1: Nhúng file JS ngoài (khuyến nghị cho script dài / dùng chung nhiều trang) -->
<script src="/source/script.js"></script>

<!-- Cách 2: Dự phòng khi người dùng tắt JS hoặc trình duyệt không hỗ trợ -->
<noscript>Trình duyệt của bạn đang tắt JavaScript. Vui lòng bật để dùng đầy đủ tính năng.</noscript>

<!-- Event Binding: gắn hàm xử lý vào sự kiện phần tử -->
<button onclick="showAnswers()">Xem đáp án</button>
```

- **Sự kiện (Event Binders) hợp lệ trong JS:** `onclick`, `onload` (khi trang tải xong), `onmouseover` (khi di chuột vào phần tử). *(Cẩn thận bẫy: **`onhover` KHÔNG tồn tại** trong JavaScript — hover là pseudo-class `:hover` của CSS!)*

### B. Cây DOM, `window` & `document` APIs

```text
window (Global Container: alert, confirm, prompt, open, dump, scrollTo)
 ├── history   (lịch sử duyệt trang: back, forward)
 ├── location  (thông tin URL hiện tại)
 ├── navigator (thông tin trình duyệt / user-agent - không đồng nhất giữa các trình duyệt)
 ├── screen    (kích thước màn hình người dùng - hữu ích cho thiết bị di động)
 └── document  (truy cập toàn bộ cây phần tử HTML của trang)
```

| Phương thức / Thuộc tính DOM | Mục đích & Kết quả |
| --- | --- |
| `window.alert("msg")` / `window.confirm("msg")` / `window.prompt("msg")` | Hiện hộp thoại thông báo / **hộp thoại xác nhận OK-Cancel** / hộp thoại nhập liệu (có thể lược bỏ tiền tố `window.`) |
| `document.getElementById("example_id")` | Trả về **node object** duy nhất có `id="example_id"` *(nhớ quy ước: `id` duy nhất, đặt trong ngoặc kép, không bắt đầu bằng số)* |
| `document.getElementsByTagName("p")` | Trả về `NodeList` chứa tất cả phần tử có tên thẻ khớp |
| `document.createElement(tag)` + `appendChild()` / `insertBefore()` / `replaceChild()` | Tạo mới một node phần tử và chèn/thay thế vào vị trí mong muốn trong DOM |
| `el.innerHTML` / `el.style` / `el.setAttribute()` | Đọc/ghi nội dung HTML, sửa CSS inline, cập nhật thuộc tính phần tử |
| **W3C DOM Level 2 Node Types** | `ELEMENT_NODE` = **1**, `ATTRIBUTE_NODE` = **2**, `TEXT_NODE` = **3** (bao gồm cả khoảng trắng/xuống dòng trong DOM Level 2), `COMMENT_NODE` = **8** |

## 4. JavaScript Best Practices

1. **Tránh biến và hàm toàn cục (Global Variables):** Toàn bộ script và thư viện bên thứ ba dùng chung ngữ cảnh toàn cục `window`; biến toàn cục làm chậm chương trình (tồn tại tới khi đóng cửa sổ) và dễ gây **xung đột tên (*name collision*)** ghi đè lẫn nhau.
2. **Dùng IDE + Linter + Kiểm thử:** Sử dụng VS Code / WebStorm kèm linter (**ESLint**, **XO**) để thống nhất chuẩn code nhóm; cân nhắc **TypeScript** để kiểm tra kiểu tĩnh; viết *unit test* và *integration test*.
3. **Tối ưu hiệu năng tải trang & vòng lặp:** Đặt thẻ `<script>` ở cuối `<body>` để không chặn render HTML; lưu trước `arr.length` vào biến ngoài vòng `for` thay vì đọc lại ở mỗi lượt lặp; tận dụng cú pháp **ES6** (arrow functions, spread `...`).

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm `var pi = "3.14";` là số thực (`float`/`number`):** Dấu ngoặc kép biến `"3.14"` thành kiểu **`string`**, mọi phép cộng `+` với chuỗi sẽ thành nối chuỗi.
2. **Tưởng `onhover` là JS Event:** JavaScript dùng **`onmouseover`** (cùng `onclick`, `onload`), còn `:hover` chỉ là CSS selector.
3. **Bẫy tên biến bắt đầu bằng số & cú pháp hàm/nhúng script:** `10car` sai quy tắc đặt tên biến; khai báo hàm không có dấu `=` (`function myFunction() {}`); nhúng file JS ngoài dùng thuộc tính `src` (`<script src="..."></script>`), không phải `ref`, `name` hay `<include>`.
4. **Nhầm số lượng thuộc tính & loại lỗi của `Error`:** JS có **6 core error types** ngoài `Error` (`EvalError`, `RangeError`, `ReferenceError`, `SyntaxError`, `TypeError`, `URIError`) và mỗi object lỗi có **2 thuộc tính** (`name` và `message`).

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- Biến khai báo bằng `let`/`const` (block scope) hoặc `var` (function scope); tên biến không được bắt đầu bằng số.
- Dùng `===` để so sánh nghiêm ngặt cả giá trị lẫn kiểu; chú ý `new String("Hello") === "Hello"` trả về `false` vì một bên là `object`, một bên là `string`.
- Cây DOM có **`window`** ở gốc (chứa `alert`, `confirm`, `prompt`, `location`, `history`, `navigator`, `screen`) và **`document`** để truy vấn/tạo/sửa node (`getElementById`, `createElement`, `appendChild`).
- Luôn giới hạn phạm vi biến (tránh global), dùng linter và `<noscript>` cho kịch bản tắt JavaScript.