# Module 3: CSS Overview & HTML5 Elements

> **Tư tưởng cốt lõi:** HTML5 cung cấp các thẻ cấu trúc ngữ nghĩa (*semantic elements*) và thẻ `<input>` thông minh tích hợp sẵn kiểm tra dữ liệu, giúp trang web chuẩn **Accessibility** và thân thiện **SEO**; trong khi **CSS** tách biệt hoàn toàn phần trình bày khỏi dữ liệu theo cơ chế kế thừa *Cascading*, từ Plain CSS đến các framework *Utility-first* (Tailwind) và *Component-based* (Bootstrap).

## 1. HTML5 Semantic & Structural Elements

Khác với thẻ `<div>` hay `<span>` vốn **không mang ý nghĩa ngữ nghĩa** (chỉ dùng để chia vùng gom nhóm áp dụng CSS), HTML5 bổ sung các thẻ ngữ nghĩa giúp cả trình duyệt, trình đọc màn hình (*assistive technologies*) và công cụ tìm kiếm hiểu chính xác vai trò từng khối nội dung:

| Thẻ HTML5 | Ý nghĩa & Mục đích sử dụng chuẩn | Lưu ý phân biệt |
| --- | --- | --- |
| `<div>` | Chia tài liệu thành các vùng/khối logic (*divisions*) để định dạng bố cục | Thẻ gom nhóm chung, **không phải** thẻ ngữ nghĩa chuyên biệt |
| `<article>` | Nội dung **độc lập, tự hoàn chỉnh ý nghĩa** (bài báo, bài blog, bình luận) | Có thể tách riêng ra vẫn hiểu được trọn vẹn |
| `<section>` | Phân chia logic theo **chủ đề/chương mục** (thường có heading riêng, vd: các chương sách hướng dẫn) | Nhóm các nội dung liên quan chung một chủ đề |
| `<header>` / `<footer>` | Phần đầu (tiêu đề, logo) và phần chân trang/bài viết (bản quyền, tác giả) | Có thể dùng cho cả `<body>` lẫn bên trong `<article>` |
| `<aside>` | Nội dung phụ liên quan gián tiếp đến nội dung chính (sidebar, ghi chú bên lề) | Không làm gián đoạn luồng đọc chính |
| `<nav>` | Nhóm các liên kết điều hướng chính giữa các trang hoặc các phần trong trang | Chỉ bọc khối điều hướng chính |
| `<figure>` & `<figcaption>` | `<figure>` bọc nội dung độc lập được tham chiếu từ bài chính (ảnh, biểu đồ, đoạn code); `<figcaption>` là chú thích đi kèm | Dùng `<figure>` để nhóm khối nội dung trực quan độc lập, không nhầm với `<img>` đơn thuần |

```html
<article>
  <header>
    <h1>Xu hướng Web Development 2025</h1>
  </header>
  <section>
    <h2>1. Tách biệt dữ liệu và giao diện</h2>
    <p>HTML cung cấp cấu trúc chuẩn để công cụ tìm kiếm lập chỉ mục dễ dàng.</p>
    <figure>
      <img src="architecture.png" alt="Sơ đồ HTML và CSS">
      <figcaption>Hình 1: Tách biệt tầng dữ liệu HTML và tầng trình bày CSS.</figcaption>
    </figure>
  </section>
  <footer>Tác giả: Web Team</footer>
</article>
```

## 2. Thẻ `<input>` trong HTML5 & Cơ chế Validation Fallback

HTML5 bổ sung hàng loạt giá trị `type` và thuộc tính mới cho `<input>`, giúp trình duyệt hiển thị bàn phím ảo phù hợp trên di động (vd bàn phím có `@` và `.com` cho email) và tự kiểm tra định dạng trước khi gửi form:

| Thuộc tính / Type | Chức năng & Hành vi trình duyệt | Lưu ý & Fallback |
| --- | --- | --- |
| `type="email"` | Kiểm tra định dạng địa chỉ email cơ bản | Chỉ cảnh báo khi sai cú pháp; *chú ý:* kiểm tra định dạng chặt chẽ vẫn cần JS/Server (vd giá trị như `hello@com` có thể lọt qua kiểm tra tối thiểu nếu không có pattern/server validation) |
| `type="number"` | Nhập số kèm giới hạn `min`, `max`, `step` (vd `min="5" max="25"` cho độ tuổi 5–25) | Có nút tăng/giảm; khác với `range` |
| `type="range"` | Thanh trượt chọn số trong khoảng `min`–`max` | Chỉ hiện thanh trượt; **cần thêm JavaScript** để hiển thị giá trị số hiện tại |
| `type="date"` / `datetime-local"` | Bộ chọn ngày / ngày-giờ (không có múi giờ) | Rơi về text field ở trình duyệt cũ |
| `type="color"` | Hộp thoại chọn màu sắc | Trình duyệt không hỗ trợ hiện ô text nhập mã màu |
| `type="tel"` | Nhập số điện thoại | **Không tự ép chỉ nhập số** (vì SĐT có `+`, `-`); phải kèm thuộc tính **`pattern`** nếu muốn validate |
| `type="url"` / `"search"` | Kiểm tra URL hợp lệ / Ô tìm kiếm có lịch sử trên WebKit | `search` khác `text` chủ yếu ở kiểu dáng |
| `list="id"` + `<datalist>` | Gợi ý tự động điền (*autocomplete*) bằng các `<option>` | Chỉ là **gợi ý** (khác `<select>` bắt buộc chọn) |
| `placeholder` & `required` | `placeholder` hiện chữ mờ gợi ý (không được gửi khi submit); `required` bắt buộc nhập dữ liệu | Kể cả có `placeholder`, ô có `required` vẫn bắt buộc phải gõ chữ |

- **Validation Fallback:** Với trình duyệt cũ không hỗ trợ HTML5 validation, cần dùng **JavaScript/jQuery** gắn vào sự kiện `submit` phía client và luôn **xác thực cuối cùng ở phía Server**.

## 3. CSS: Nguyên lý Cascading, Thứ tự Ưu tiên & Layouts

- **Tại sao gọi là "Cascading" (Thác đổ)?** Vì các quy tắc CSS áp dụng đồng nhất xuyên suốt website và **các phần tử con/cháu kế thừa (inherit) kiểu dáng được định nghĩa cho phần tử cha** (trừ một số thuộc tính ngoại lệ như `border`, `margin`).
- **Tách biệt Dữ liệu và Thiết kế:** HTML giữ dữ liệu (giúp người khiếm thị dùng trình đọc màn hình và công cụ tìm kiếm index chính xác mà không bị thiết kế cản trở), còn CSS phủ lớp giao diện lên trên.
- **3 cách nhúng CSS & Thứ tự ưu tiên (từ cao nhất xuống thấp nhất):**
  1. **Inline CSS** (thuộc tính `style="..."` trực tiếp trên thẻ HTML) — **Ưu tiên cao nhất**, ghi đè các cách khác.
  2. **Internal CSS** (thẻ `<style>...</style>` trong `<head>`) — ưu tiên thứ hai; làm tăng thời gian tải nếu lặp lại trên nhiều trang.
  3. **External CSS** (file `.css` ngoài liên kết bằng `<link rel="stylesheet" href="style.css">` trong `<head>`) — **Được khuyến nghị nhất** để giữ HTML sạch và tái sử dụng toàn site.
  4. *Mặc định của trình duyệt (Browser default stylesheet)* — ưu tiên thấp nhất.

### Layout Approaches: Fixed vs. Fluid

- **Fixed Layout:** Dùng đơn vị cố định (như `px`); **kích thước không thay đổi** bất kể thiết bị có màn hình lớn hay nhỏ.
- **Fluid Layout:** Dùng đơn vị tương đối (`%`, `em`, `rem`, `vw`) cho phép các phần tử **co giãn linh hoạt theo kích thước màn hình** (nền tảng của Responsive Design cùng với **Flexbox** và **CSS Grid**).

## 4. Vanilla CSS vs. Utility-First vs. Component Frameworks

| Hướng tiếp cận | Đại diện | Cơ chế & Ưu điểm | Nhược điểm & Giới hạn |
| --- | --- | --- | --- |
| **Plain / Vanilla CSS** | CSS thuần | Tự viết toàn bộ style; **tự do tuyệt đối (complete freedom)** thiết kế mọi thứ theo ý muốn | Tốn nhiều thời gian, công sức viết và bảo trì từng component |
| **Utility-First Framework** | **Tailwind CSS** | Cung cấp các **Utility Classes** đơn mục đích ánh xạ thẳng tới thuộc tính CSS (vd `text-center`) + **Modifiers** theo trạng thái (`hover:`, `focus:`) | **Làm mã HTML dài dòng (verbose)** vì trộn lẫn class định dạng trực tiếp vào nội dung markup |
| **Component Framework** | **Bootstrap**, Foundation, Materialize, UIKit | Cung cấp sẵn các **component & template đã style đẹp** (buttons, navbars, forms, `.link-danger`), đảm bảo đồng nhất giao diện và ít cần chuyên sâu CSS | **Giới hạn khả năng tùy biến thiết kế** trong khuôn khổ các component có sẵn của framework |

> **Modifier trong CSS Framework:** Là lớp chuyên biệt điều chỉnh giao diện phần tử bằng cách áp dụng CSS theo một điều kiện/trạng thái xác định (như `hover`, `focus` hoặc breakpoint kích thước màn hình).

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm đặc điểm của Utility-First Framework với Vanilla CSS:** Utility-first (Tailwind) dùng **Utility Classes** và **làm HTML rườm rà khi trộn style vào markup**, nhưng chỉ **Plain/Vanilla CSS** mới cho phép *tự do hoàn toàn (complete freedom)* mà không bị giới hạn bởi bộ class dựng sẵn.
2. **Nhầm `type="range"` và `type="number"` khi giới hạn tuổi (vd 5–25):** Ô nhập số có `min`/`max` hiển thị hộp số chuẩn là `<input type="number" min="5" max="25">`; còn `range` tạo thanh kéo trượt và tự thân không hiện con số.
3. **Nhầm `<div>` với `<section>` và `<article>`:** `<div>` chỉ tách vùng phục vụ bố cục/CSS; `<section>` gom các phần có chung chủ đề/tiêu đề; `<article>` đại diện một khối nội dung độc lập tự đứng vững một mình.
4. **Nhầm thứ tự ghi đè CSS:** Khi cả External, Internal và Inline CSS cùng trỏ vào một phần tử, **Inline CSS** luôn có độ ưu tiên cao nhất và sẽ ghi đè hai loại còn lại.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Cascading** có nghĩa là phần tử con kế thừa style từ phần tử cha; luôn ưu tiên viết CSS ở **External Stylesheet** để tách biệt thiết kế khỏi dữ liệu HTML.
- Dùng đúng thẻ ngữ nghĩa HTML5 (`<article>`, `<section>`, `<figure>`, `<figcaption>`, `<nav>`, `<aside>`) để tối ưu **SEO** và **Accessibility**.
- **Bootstrap** (Component framework) nhanh và đồng nhất nhưng hạn chế tùy biến; **Tailwind CSS** (Utility-first) linh hoạt nhờ utility classes & modifiers nhưng làm HTML verbose.
- **Fluid layout** dùng đơn vị tương đối để co giãn theo màn hình; **Fixed layout** giữ kích thước cố định bất chấp thiết bị.