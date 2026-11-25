# Module 2: CSS Overview & HTML5 Elements

> **Tư tưởng cốt lõi:** HTML5 cung cấp các thẻ cấu trúc ngữ nghĩa (`<section>`, `<article>`, `<header>`, `<footer>`, `<figure>`) và hệ thống `<input>` giàu thuộc tính xác thực để nâng cao UX, accessibility và SEO; CSS tách biệt hoàn toàn thiết kế khỏi dữ liệu theo cơ chế xếp tầng (cascading), kết hợp các layout (fixed, fluid, Flexbox, Grid) và hai trường phái framework (Utility-first vs. Component-based).

## 1. Thẻ cấu trúc ngữ nghĩa HTML5 (Semantic Structural Elements)

Trước HTML5, lập trình viên phải chia bố cục hoàn toàn bằng hàng loạt thẻ `<div>` vô nghĩa. HTML5 đưa vào các thẻ **ngữ nghĩa (semantic tags)** mô tả trực tiếp vai trò của khối nội dung — giúp trình duyệt, công cụ tìm kiếm (**SEO**) và công cụ đọc màn hình (**Accessibility**) hiểu chính xác cấu trúc trang:

| Thẻ HTML5 | Vai trò & Ngữ nghĩa | Phân biệt quan trọng |
| --- | --- | --- |
| `<section>` | Nhóm nội dung liên quan có **cùng chủ đề**, thường đi kèm heading riêng (`<h2>`, `<h3>`) | Dùng để tách các khu vực/chương theo chủ đề trong tài liệu |
| `<article>` | Một mục nội dung **độc lập, tự hoàn chỉnh** (bài blog, tin tức, bình luận) có ý nghĩa ngay cả khi tách riêng | Phân biệt với `<section>`: `<article>` có thể phân phối độc lập (syndication) |
| `<header>` | Phần đầu giới thiệu của trang hoặc của một `<section>`/`<article>` (logo, tiêu đề, menu) | Có thể xuất hiện nhiều lần trong cùng một trang |
| `<footer>` | Phần chân trang hoặc chân của một `<section>` (bản quyền, tác giả, liên kết phụ) | Tương tự `<header>`, gắn với khối chứa gần nhất |
| `<nav>` | Khối chứa các **liên kết điều hướng** chính (navigation menu) | Phân biệt nhóm điều hướng (navigation) với nhóm nội dung (grouping) |
| `<aside>` | Nội dung phụ trợ, thanh bên (sidebar), trích dẫn liên quan gián tiếp | Không làm đứt mạch nội dung chính |
| `<figure>` & `<figcaption>` | `<figure>` bọc nội dung tự chứa (ảnh, biểu đồ, sơ đồ, đoạn code); `<figcaption>` là chú thích đi kèm | Giúp gắn kết ngữ nghĩa chặt chẽ giữa hình ảnh và chú thích |
| `<fieldset>` & `<legend>` | Nhóm các trường liên quan trong `<form>` (`<fieldset>`) và đặt nhãn tiêu đề cho nhóm đó (`<legend>`) | Cải thiện mạnh khả năng tiếp cận (screen reader) cho biểu mẫu dài |

```html
<article>
  <header>
    <h2>Hướng dẫn tối ưu HTML5</h2>
  </header>
  <section>
    <h3>1. Minh họa sơ đồ DOM</h3>
    <figure>
      <img src="dom-tree.png" alt="Sơ đồ cây DOM HTML5">
      <figcaption>Hình 1: Cấu trúc phân cấp cây DOM trong trình duyệt.</figcaption>
    </figure>
  </section>
  <footer>
    <p>Tác giả: Nguyễn Văn A</p>
  </footer>
</article>
```

## 2. Thẻ `<input>` trong HTML5 và cơ chế xác thực (Validation)

HTML5 mở rộng mạnh mẽ thuộc tính `type` của thẻ `<input>` nhằm tự động hiển thị bàn phím ảo phù hợp trên di động (ví dụ bàn phím có `@` và `.com` cho `email`) và kiểm tra dữ liệu ngay phía trình duyệt:

| `type` của `<input>` | Chức năng & Hành vi | Thuộc tính kiểm soát phổ biến |
| --- | --- | --- |
| `email` | Nhập địa chỉ email, kích hoạt kiểm tra định dạng cơ bản | `required`, `pattern` (regex kiểm tra domain đầy đủ như `hello@domain.com`), `multiple` |
| `tel` | Nhập số điện thoại (hiển thị bàn phím số trên mobile) | `pattern`, `placeholder` |
| `number` | Nhập giá trị số có nút tăng/giảm (spinner) | `min`, `max`, `step` (vd giới hạn tuổi từ 5–25: `min="5" max="25"`) |
| `range` | Thanh trượt chọn giá trị trong khoảng | `min`, `max`, `step`, `value` |
| `date` / `datetime-local` | Chọn ngày (hoặc ngày + giờ địa phương, không kèm múi giờ) | `min`, `max` |
| `color` | Bộ chọn màu (color picker); rơi về ô text ở trình duyệt không hỗ trợ | `value="#1a73e8"` |
| `url` / `search` | Nhập đường dẫn web / ô tìm kiếm có nút xóa nhanh | `required`, `placeholder` |

```html
<form action="/register" method="POST">
  <fieldset>
    <legend>Thông tin học viên</legend>

    <label for="email">Email:</label>
    <!-- Dùng pattern để chặn chuỗi sai kiểu "hello@com" thiếu TLD -->
    <input id="email" name="email" type="email"
           pattern="^[^\s@]+@[^\s@]+\.[^\s@]+$" required>

    <label for="age">Tuổi (5–25):</label>
    <input id="age" name="age" type="number" min="5" max="25" step="1" required>
  </fieldset>
  <button type="submit">Đăng ký</button>
</form>
```

## 3. Bản chất của CSS (Cascading Style Sheets) & Thứ tự ưu tiên

- **Tách biệt Dữ liệu và Thiết kế (Separation of Concerns):** HTML mang dữ liệu và ngữ nghĩa; CSS phủ lớp trình bày lên trên. Nhờ đó:
  - Người dùng khiếm thị có thể tắt CSS và nghe nội dung qua trình đọc màn hình (speech synthesizer).
  - Các bot/máy tìm kiếm lập chỉ mục dữ liệu dễ dàng mà không bị nhiễu bởi mã trình bày.
- **Tại sao gọi là "Cascading" (Xếp tầng)?**
  - Một quy tắc CSS có thể tạo diện mạo đồng nhất cho toàn bộ các phần tử trên nhiều trang web thông qua file CSS ngoài (external stylesheet).
  - Phần tử con/cháu thường **kế thừa (inherit)** style từ phần tử cha (ví dụ `font-family`, `color`), dù có ngoại lệ (như `border`, `padding`, `margin`).
  - Khi nhiều quy tắc cùng tác động lên một phần tử, trình duyệt phân giải xung đột theo **thứ tự ưu tiên (Cascade & Specificity)**:

| Mức ưu tiên (Cao → Thấp) | Cách khai báo CSS | Ghi chú thực tế |
| --- | --- | --- |
| **1 (Cao nhất)** | **Inline CSS** (`<p style="color: red;">`) | Ghi đè cả internal và external stylesheet — rất dễ gây lỗi "sửa file CSS ngoài mà không ăn"! |
| **2** | **Internal CSS** (`<style>...</style>` trong `<head>`) | Chỉ áp dụng cho 1 trang HTML hiện tại |
| **3 (Chuẩn khuyến nghị)** | **External CSS** (`<link rel="stylesheet" href="styles.css">`) | Tái sử dụng toàn site, dễ bảo trì và cache trình duyệt |
| **4 (Thấp nhất)** | **Browser Default** (User-Agent stylesheet) | Giao diện mặc định của từng trình duyệt |

### So sánh các mô hình bố cục (CSS Layouts)

| Loại Layout | Cách hoạt động | Ưu & Nhược điểm |
| --- | --- | --- |
| **Fixed Layout** | Kích thước cố định bằng `px` (không đổi khi resize trình duyệt) | Kiểm soát pixel chính xác, nhưng dễ bị **thanh cuộn ngang** trên màn hình nhỏ hoặc dư khoảng trắng trên màn hình lớn |
| **Fluid Layout** | Kích thước tương đối bằng `%`, `vw`, `em` co giãn theo viewport | Tự thích ứng nhiều kích thước màn hình, nhưng nếu không giới hạn `max-width`/`min-width` văn bản có thể bị kéo quá rộng hoặc nén quá hẹp |
| **Flexbox** | Bố cục 1 chiều (hàng hoặc cột), căn giữa và phân bổ không gian cực linh hoạt | Lý tưởng cho navbar, card row, thanh công cụ |
| **CSS Grid** | Bố cục 2 chiều (cả hàng và cột đồng thời) | Lý tưởng cho cấu trúc trang phức tạp, dashboard, lưới sản phẩm |

## 4. CSS Frameworks: Vanilla CSS vs. Utility-First vs. Component-Based

| Tiêu chí | Vanilla CSS (Thuần) | Utility-First Framework (vd: **Tailwind CSS**) | Component Framework (vd: **Bootstrap**, Bulma, Foundation) |
| --- | --- | --- | --- |
| **Triết lý** | Tự viết toàn bộ CSS từ đầu | Cung cấp các **class tiện ích nguyên tử** (mỗi class ánh xạ 1 thuộc tính CSS như `p-4`, `text-center`, `hover:bg-blue-600`) | Cung cấp bộ **component dựng sẵn** (navbar, modal, card, carousel, button) |
| **Ưu điểm** | Tự do tuyệt đối, 0 dung lượng thư viện thừa | Thiết kế linh hoạt không bị rập khuôn; hỗ trợ mạnh **modifiers** cho trạng thái (`hover:`, `focus:`, `md:`) ngay trong HTML | Dựng giao diện cực nhanh, đồng nhất, tích hợp sẵn responsive grid |
| **Nhược điểm** | Tốn nhiều thời gian & công sức cho mọi thành phần | HTML nhiều class dài dòng, cần thời gian làm quen hệ thống tên class | Các trang web dễ trông **giống nhau (generic look)**; tùy biến sâu hoặc ghi đè style mặc định phức tạp; kèm nhiều CSS/JS dư thừa không dùng tới |

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **File CSS ngoài không có tác dụng vì bị Inline Style ghi đè:** Khi debug thấy rule trong `styles.css` không hiển thị, hãy kiểm tra ngay trong DevTools xem phần tử có thuộc tính `style="..."` trực tiếp hay không.
2. **`input type="email"` vẫn chấp nhận `hello@com`:** Theo đặc tả HTML5 mặc định, `hello@com` được xem là hợp lệ (vì chấp nhận tên miền nội bộ không có dấu chấm). Để yêu cầu định dạng email chuẩn có TLD (`.com`, `.vn`), cần bổ sung thuộc tính `pattern` hoặc kiểm tra bằng JavaScript + Backend validation.
3. **Nhầm lẫn `<section>` và `<article>`:** Dùng `<section>` để phân chia các vùng chủ đề trong trang; dùng `<article>` cho nội dung hoàn chỉnh có thể đứng độc lập (như 1 bài báo, 1 bài đăng blog).
4. **Dùng Component Framework mà quên đánh giá khả năng tùy biến:** Với các sản phẩm cần nhận diện thương hiệu riêng (như startup e-commerce), Bootstrap giúp ra MVP nhanh nhưng dễ bị "đụng hàng" giao diện và khó ghi đè kiến trúc CSS về sau.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- Luôn ưu tiên **HTML5 Semantic Tags** (`<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`, `<figure>`, `<figcaption>`) thay vì lạm dụng `<div>` để đạt chuẩn SEO và Accessibility.
- Kết hợp `min`, `max`, `step`, `required`, `pattern` trên thẻ `<input>` và luôn có **validation fallback** ở JavaScript và Server.
- Đặt CSS ở **External Stylesheet** để đảm bảo tính xếp tầng (cascading) đồng bộ toàn website.
- Chọn đúng công cụ styling: **Component framework** (Bootstrap) khi cần tốc độ & UI chuẩn sẵn; **Utility-first** (Tailwind) khi cần tốc độ kèm tùy biến cao và modifier theo trạng thái (`hover`, `focus`).
