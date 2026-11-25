# Module 1: HTML Overview

> **Tư tưởng cốt lõi:** HTML (Hypertext Markup Language) là ngôn ngữ đánh dấu chuẩn xác định cấu trúc và nội dung của trang web thông qua các thẻ (tags) tạo thành cây DOM (Document Object Model); HTML5 mở rộng khả năng đa phương tiện, API gốc trình duyệt, sandboxing bảo mật và tương thích ngược, nhưng đòi hỏi kiểm tra mức độ hỗ trợ của từng trình duyệt và không được lệ thuộc tuyệt đối vào scripting.

## 1. Bản chất của HTML, HTML5 và các tổ chức chuẩn hóa

- **HTML (Hypertext Markup Language):** Ngôn ngữ đánh dấu (markup language — *không phải ngôn ngữ lập trình*) ban đầu do **CERN** và **IETF** khởi xướng đầu thập niên 1990 để chia sẻ tài liệu khoa học, sau đó trở thành ngôn ngữ nền tảng của Internet.
- **HTML Elements & Tags:** Các phần tử (elements) là khối xây dựng của trang web (đoạn văn `<p>`, danh sách `<ul>`/`<ol>`, bảng `<table>`, ảnh `<img>`). Trình duyệt **không hiển thị thẻ** mà dùng thẻ để render nội dung.
- **Chuẩn hóa W3C vs. WHATWG:**
  - **W3C (World Wide Web Consortium):** Ban hành các khuyến nghị chuẩn HTML qua nhiều phiên bản; từ năm 2007 thành lập nhóm làm việc hợp tác cùng WHATWG để xây dựng chuẩn **HTML5**.
  - **WHATWG (Web Hypertext Application Technology Working Group):** Duy trì bản đặc tả sống (Living Standard) với giấy phép cởi mở hơn.
- **Tách biệt yêu cầu tuân thủ (Conformance Requirements):** HTML5 tách rõ quy tắc cho **User Agents (trình duyệt)** (phải hỗ trợ tương thích ngược với HTML4 và XHTML1) và cho **Authors (lập trình viên)** (loại bỏ các thẻ/thuộc tính lỗi thời để mã nguồn gọn sạch hơn).

### Khung tài liệu HTML5 chuẩn & `<!DOCTYPE html>`

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Trang HTML5 chuẩn</title>
</head>
<body>
  <h1>Xin chào HTML5</h1>
  <p>Tài liệu được trình duyệt phân tích theo quy tắc HTML5.</p>
</body>
</html>
```

> **Lưu ý:** `<!DOCTYPE html>` **không phải là một thẻ HTML**, mà là một chỉ thị khai báo (declaration) đặt ở dòng đầu tiên để trình duyệt biết phải phân tích tài liệu theo chuẩn HTML5 (Standard Mode) thay vì chế độ cũ (Quirks Mode). Tài liệu gửi kèm MIME type `text/html` sẽ được phân tích bằng HTML parser.

## 2. HTML vs. XML — Khi nào dùng công nghệ nào?

| Tiêu chí | HTML / HTML5 | XML (eXtensible Markup Language) |
| --- | --- | --- |
| **Mục đích chính** | Hiển thị và cấu trúc nội dung trang web cho người dùng trên trình duyệt | Lưu trữ, mô tả và truyền tải dữ liệu có cấu trúc giữa các hệ thống |
| **Hệ thống thẻ (Tags)** | Tập thẻ định nghĩa sẵn (`<h1>`, `<p>`, `<video>`, `<canvas>`) | Tự định nghĩa thẻ tùy ý theo miền dữ liệu (`<order>`, `<price>`) |
| **Độ chặt chẽ cú pháp** | Khoan dung lỗi hơn (trình duyệt cố gắng tự sửa lỗi đóng thẻ) | Rất nghiêm ngặt (phân biệt hoa/thường, bắt buộc đóng mọi thẻ) |
| **Ứng dụng tiêu biểu** | Website, Web App đa nền tảng, giao diện tương tác | Cấu hình hệ thống, RSS, SOAP, trao đổi dữ liệu liên dịch vụ |

## 3. Cây DOM (Document Object Model) và các HTML5 APIs

- **DOM Tree:** Khi trình duyệt tải một trang HTML, nó phân tích các thẻ thành một cấu trúc cây phân cấp gồm các đối tượng (nodes): `document` ở gốc → `<html>` → `<head>` và `<body>` → các thẻ con, thuộc tính và văn bản.
- **Lợi thế xây dựng Web Application của HTML5:**
  - Chạy thống nhất trên hầu hết thiết bị có sẵn trình duyệt (desktop, mobile, tablet) không cần plug-in rời như Flash.
  - Hệ sinh thái **HTML5 APIs** tích hợp sẵn: `<audio>`, `<video>`, `<canvas>` (vẽ đồ họa 2D/3D), Offline Storage / Web Storage, Geolocation, Drag-and-Drop.
  - Giảm số lượng ảnh tĩnh nhờ kết hợp HTML + CSS chuẩn giúp tải trang nhanh hơn và hỗ trợ **SEO** tốt hơn thông qua từ khóa trong thẻ ngữ nghĩa.

## 4. HTML Scripting & Bảo mật với `sandbox`

- **Scripting (thường dùng JavaScript):** Gắn trực tiếp bằng cặp thẻ `<script>...</script>` hoặc nhúng file ngoài qua `<script src="app.js"></script>` để kiểm tra form (validation), thay đổi DOM động và phản hồi sự kiện người dùng.
- **Điều kiện để scripting hoạt động trong trình duyệt:** Phải đồng thời thỏa mãn **2 điều kiện**:
  1. Trình duyệt đang dùng có hỗ trợ scripting.
  2. Người dùng đã bật (enable) tính năng scripting trong cấu hình trình duyệt.
- **Nguyên tắc thiết kế an toàn:** *Sử dụng scripting để nâng cao trải nghiệm, nhưng KHÔNG phụ thuộc hoàn toàn vào scripting* (vì người dùng hoặc thiết bị có thể tắt JavaScript).
- **HTML5 `sandbox` cho nội dung nhúng (`<iframe>`):**
  - Mặc định, một `<iframe>` nhúng nội dung bên thứ ba (mashup, quảng cáo, widget) có thể kế thừa quyền chạy script tương đương trang chính.
  - Thuộc tính `sandbox` kích hoạt chế độ cách ly (extra content restrictions), chặn chạy script, gửi form, mở popup hoặc truy cập cookie/DOM của trang chủ trừ khi được cấp phép tường minh:

```html
<!-- Cách ly hoàn toàn nội dung nhúng từ bên thứ ba -->
<iframe src="https://untrusted.example.com/widget" sandbox></iframe>

<!-- Chỉ cho phép chạy script trong phạm vi cách ly (không truy cập cùng origin) -->
<iframe src="https://partner.example.com/chart" sandbox="allow-scripts"></iframe>
```

## 5. Khả năng hỗ trợ trình duyệt (Browser Support) & Fallback

Không phải mọi trình duyệt đều hỗ trợ đầy đủ mọi tính năng HTML5/CSS3 giống nhau — ví dụ kinh điển trong bài giảng là `<input type="date">`:

| Trình duyệt | Cách hiển thị `<input type="date">` & Lưu ý |
| --- | --- |
| **Google Chrome** | Hiển thị lịch chọn ngày trực quan (calendar picker), định dạng chuẩn hóa |
| **Microsoft Edge** | Hiển thị hộp xoay chọn số (spinning boxes), khác định dạng hiển thị (`mm/dd/yyyy` vs `yyyy-mm-dd`) |
| **Firefox (bản cũ) / Trình duyệt không hỗ trợ** | Rơi về ô nhập văn bản thuần (`text field`), dễ phát sinh lỗi định dạng và cần validation dự phòng |

- **Browser Support Tables (ví dụ `caniuse.com`):** Bảng tra cứu mức độ hỗ trợ theo từng phiên bản trình duyệt bằng mã màu:
  - **Xanh lá (Green):** Hỗ trợ đầy đủ (Full support).
  - **Vàng ô-liu (Olive):** Hỗ trợ một phần (Partial support).
  - **Đỏ (Red):** Không hỗ trợ (No support).
- **Kiểm tra & Cơ chế dự phòng (Feature Detection & Fallback):**
  - Dùng JavaScript kiểm tra xem trình duyệt có hỗ trợ phần tử/API mới hay không trước khi dùng.
  - Luôn cung cấp **fallback** (ví dụ đặt link tải video bên trong thẻ `<video>` nếu trình duyệt không hỗ trợ HTML5 Video).
  - Thường xuyên kiểm tra cú pháp bằng **HTML/CSS Validator** và **Browser DevTools**.

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm `<!DOCTYPE html>` là thẻ HTML:** Thực chất đây là khai báo document type giúp trình duyệt chọn đúng bộ phân tích HTML5, không phải phần tử nằm trong cây DOM.
2. **Nhúng `<iframe>` bên thứ ba mà quên `sandbox`:** Vô tình trao quyền thực thi script ngang hàng trang chính cho nguồn không tin cậy (rủi ro XSS, chèn quảng cáo trái phép).
3. **Tin rằng mọi trình duyệt render HTML5 giống hệt nhau:** Cùng một thẻ `<input type="date">` nhưng Chrome, Edge, Safari và các bản cũ hiển thị khác nhau; luôn kiểm tra `caniuse.com` và viết kiểm tra dữ liệu phía server.
4. **Cố căn giữa bằng CSS thủ công kiểu cũ:** Khi mới học HTML/CSS, thay vì dùng các mẹo margin/float dễ vỡ layout, hãy làm chủ **Flexbox** và **CSS Grid**.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- HTML tạo **cấu trúc & nội dung**, CSS lo **giao diện & bố cục**, JavaScript lo **hành vi & tương tác**.
- DOM Tree là mô hình đối tượng dạng cây biểu diễn toàn bộ cấu trúc trang HTML trong bộ nhớ trình duyệt.
- Scripting chỉ chạy khi **trình duyệt hỗ trợ VÀ người dùng cho phép**; luôn có phương án dự phòng khi scripting bị tắt.
- Dùng thuộc tính `sandbox` để cô lập nội dung nhúng không tin cậy trong `<iframe>`, và dùng Browser Support Tables để thiết kế tương thích đa trình duyệt.
