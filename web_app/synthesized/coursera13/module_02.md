# Module 2: HTML Overview

> **Tư tưởng cốt lõi:** HTML (*Hypertext Markup Language*) là ngôn ngữ đánh dấu tạo khung xương cấu trúc và nội dung trang web thông qua các phần tử (*elements*) xếp thành cây **DOM** (*Document Object Model*); chuẩn **HTML5** hợp nhất sức mạnh đa phương tiện gốc trình duyệt, `Web Workers`, cơ chế cách ly bảo mật `sandbox` và khả năng tương thích ngược, đòi hỏi lập trình viên kết hợp kiểm tra hỗ trợ trình duyệt (*Browser Support Tables*) và viết fallback an toàn.

## 1. Bản chất HTML5 & Các tổ chức chuẩn hóa

- **HTML & HTML Elements:** HTML được khởi xướng đầu thập niên 1990 bởi **CERN** và **IETF** để chia sẻ tài liệu khoa học, sau đó phát triển thành ngôn ngữ nền tảng của Web. Các khối xây dựng cơ bản của một trang HTML gọi là **HTML Elements** (được biểu diễn bằng các cặp thẻ như `<p>`, `<table>`, `<img>`, `<br>` để xuống dòng, `<!-- comment -->` để ghi chú ẩn khỏi giao diện người dùng). Trình duyệt không hiển thị thẻ mà dựa vào thẻ để render nội dung.
- **W3C & WHATWG:** Từ năm **2007**, **W3C** (*World Wide Web Consortium*) thành lập nhóm làm việc hợp tác cùng **WHATWG** (*Web Hypertext Application Technology Working Group*) để phát triển chuẩn **HTML5**.
- **Mục tiêu cốt lõi của HTML5:**
  - Định nghĩa một ngôn ngữ thống nhất có thể viết bằng cú pháp **HTML** (`text/html`) hoặc **XML/XHTML** (`application/xml`).
  - Xác định mô hình xử lý tương thích ngược với các phiên bản HTML4 và XHTML1 trước đây (tách rõ chuẩn cho **User Agents/trình duyệt** giữ tương thích cũ và cho **Authors/lập trình viên** loại bỏ thẻ lỗi thời).
  - Tích hợp sẵn markup & API cho **video, audio, canvas, web storage, offline apps, drag-and-drop** mà không cần plug-in ngoài (như Flash).

### Cấu trúc chuẩn một tài liệu HTML5 & Bảng biểu (`<table>`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="keywords" content="HTML5, CSS3, JavaScript, Web Development">
  <title>Sample Page</title>
</head>
<body>
  <!-- Ghi chú HTML: Không hiển thị trên trình duyệt -->
  <img src="assets/logo.png" alt="Company Logo"><br>

  <table>
    <tr>
      <th>Date</th>
      <th>Language</th>
    </tr>
    <tr>
      <td>2014</td>
      <td>HTML5</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>CSS3</td>
    </tr>
    <tr>
      <td>1995</td>
      <td>JavaScript</td>
    </tr>
  </table>
</body>
</html>
```

- **`<!DOCTYPE html>`:** Không phải thẻ HTML mà là chỉ thị khai báo đặt ở dòng đầu tiên giúp trình duyệt phân tích đúng chuẩn HTML5.
- **`<meta>` trong `<head>`:** Cung cấp metadata và **từ khóa (keywords)** cho công cụ tìm kiếm (**SEO**).
- **`<img>`:** Là thẻ rỗng (self-closing), dùng thuộc tính **`src`** để nhúng ảnh (`<img src="assets/logo.png">`), **không dùng** `href` hay `<image>`.
- **`<table>`:** Mỗi hàng dùng `<tr>` (*table row*), ô tiêu đề dùng `<th>` (*table header*), ô dữ liệu dùng `<td>` (*table data*). Không tồn tại thẻ `<tc>`!

## 2. HTML vs. XHTML (XML Syntax)

| Tiêu chí | HTML (MIME `text/html`) | XHTML / XML (MIME `application/xml`) |
| --- | --- | --- |
| **Tính chặt chẽ cú pháp** | Khoan dung: chấp nhận chữ hoa/thường, có thể bỏ qua một số thẻ đóng hoặc dấu ngoặc | **Rất nghiêm ngặt (*well-formed*):** bắt buộc chữ thường, mọi thẻ phải đóng, mọi thuộc tính phải có giá trị bọc trong dấu ngoặc kép/đơn |
| **Xử lý lỗi** | Trình duyệt tự sửa và tiếp tục render | Bộ phân tích XML **dừng xử lý ngay lập tức** khi gặp lỗi cú pháp |
| **Ứng dụng** | Website & Web App thông thường | Khi cần biến đổi tài liệu bằng **XSLT** hoặc trao đổi dữ liệu XML chuẩn xác |

## 3. DOM Tree, HTML Document API & Web Workers

Khi tải một trang HTML, trình duyệt tạo đối tượng `Document` trong bộ nhớ — chính là cây **DOM** (*Document Object Model*) chứa các node: DOCTYPE node, element nodes, text nodes và comment nodes.

| API / Tính năng HTML5 | Chức năng & Giá trị trả về |
| --- | --- |
| `document.head` | Trả về thẻ `<head>` đầu tiên là con của `<html>` (hoặc `null`) |
| `document.images` | Thuộc tính DOM của HTML Document API trả về tập hợp (`HTMLCollection`) các thẻ `<img>` trong tài liệu |
| `document.scripts` | Trả về `HTMLCollection` toàn bộ thẻ `<script>` trong tài liệu |
| `document.getElementById('id')` | Trả về **1 phần tử duy nhất** khớp thuộc tính `id` (thường dùng lấy giá trị ô nhập liệu trong form khi bấm nút) |
| `document.getElementsByTagName('tag')` | Trả về `NodeList` chứa tất cả phần tử có tên thẻ khớp tham số |
| **`Web Workers`** | API của HTML5 cho phép chạy các tác vụ tính toán nặng ở luồng nền **mà không làm đơ/chặn giao diện người dùng (non-blocking UI)** |

## 4. HTML Scripting & Bảo mật nhúng bằng `sandbox`

- **Điều kiện để Scripting hoạt động trong trình duyệt:**
  1. **Trình duyệt đang dùng có hỗ trợ scripting** (*The browser supports scripting*).
  2. **Người dùng đã bật scripting** trong ngữ cảnh trình duyệt hiện tại (*User has scripting enabled*).
- **Nguyên tắc vàng:** Dùng scripting để tăng tính tương tác, nhưng **không lệ thuộc hoàn toàn** vào nó vì người dùng có thể tắt JavaScript.
- **Bảo mật với `sandbox` cho `<iframe>` mashups:** Nếu nhúng `<iframe>` bên thứ ba mà **không có thuộc tính `sandbox`**, nội dung nhúng sẽ có quyền chạy script ngang hàng với trang chính (nguy cơ chèn quảng cáo trái phép, đánh cắp dữ liệu). Thêm `sandbox` sẽ áp đặt các giới hạn nội dung nghiêm ngặt:

```html
<!-- Cách ly hoàn toàn nội dung nhúng không tin cậy -->
<iframe src="https://thirdparty.example.com/widget" sandbox></iframe>
```

## 5. Browser Support Tables & Kiểm tra tương thích bằng JS

Không phải trình duyệt nào cũng hỗ trợ mọi tính năng HTML5 giống nhau. Ví dụ với `<input type="date">`:
- **Google Chrome:** Hiển thị lịch chọn ngày trực quan (*calendar picker*).
- **Microsoft Edge:** Hỗ trợ đầy đủ với **hộp xoay chọn số (*spinning boxes*)** (lưu ý khác định dạng hiển thị `mm/dd/yyyy` vs `yyyy-mm-dd`).
- **Firefox (bản cũ) / Trình duyệt không hỗ trợ:** Rơi về ô nhập văn bản thuần (*fallback text field*).

Trên các bảng hỗ trợ trình duyệt như **`caniuse.com`**:
- **Xanh lá (Green):** Hỗ trợ đầy đủ (*Full support*).
- **Vàng ô-liu (Olive):** Hỗ trợ một phần (*Partial support*).
- **Đỏ (Red):** Không hỗ trợ (*No support*).

```javascript
// Kiểm tra khả năng hỗ trợ <input type="date"> bằng JavaScript
const testInput = document.createElement("input");
testInput.setAttribute("type", "date");
// Nếu trình duyệt không hỗ trợ, thuộc tính .type sẽ rơi về "text"
const isDateSupported = testInput.type === "date";
```

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm tên thẻ HTML khi nhúng ảnh và tạo bảng:** Ảnh luôn dùng `<img src="...">` (không phải `<image>` hay `href`); hàng bảng luôn dùng `<tr>` bọc `<th>`/`<td>`, tuyệt đối không đặt `<tr>` bên trong `<td>` hay bịa thẻ `<tc>`.
2. **Nhầm cú pháp comment của HTML với Python/JS/CSS:** HTML comment bắt buộc là `<!-- ... -->` (không dùng `#`, `/* ... */` hay `"""..."""`).
3. **Nhầm `document.getElementById` với `document.getElementsByTagName`:** Để lấy giá trị từ 1 ô input cụ thể có `id` khi bấm nút submit, luôn dùng `document.getElementById('id')` (không có chữ `s` ở `Element`).
4. **Bỏ quên `sandbox` trên `<iframe>` nhúng ngoài:** Khiếu khuyết bảo mật phổ biến khiến script bên thứ ba kế thừa quyền thực thi của trang chủ.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Elements** là khối xây dựng của HTML; chuẩn **HTML5** do **W3C và WHATWG** hợp tác phát triển từ 2007, hỗ trợ đa nền tảng với video/audio/storage tích hợp sẵn.
- **Web Workers** xử lý tác vụ nặng không chặn UI; `<meta>` cung cấp từ khóa SEO; `<br>` ngắt dòng; `document.images` trả về danh sách ảnh qua DOM API.
- Luôn kiểm tra tính tương thích trên **Browser Support Tables** (`caniuse.com`), dùng `document.createElement()` để dò tính năng và chuẩn bị **fallback** cho trình duyệt cũ.