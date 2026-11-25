# Module 4: Final Project — Single-Page Portfolio Website

> **Tư tưởng cốt lõi:** Tổng hợp toàn bộ kỹ năng HTML5 ngữ nghĩa, CSS layout/styling và JavaScript thao tác DOM để xây dựng một trang Portfolio cá nhân hoàn chỉnh (Single-Page Web Application) có điều hướng mượt, danh sách kỹ năng/dự án và tính năng thêm lời giới thiệu (recommendations) động không cần tải lại trang.

## 1. Kiến trúc tổng thể của dự án Portfolio (HTML + CSS + JS)

Trong Final Project của Khóa 2, bạn áp dụng mô hình **tách biệt 3 tầng (Separation of Concerns)** chuẩn front-end:

```text
portfolio/
├── index.html   --> Cấu trúc ngữ nghĩa (Header/Nav, About Me, Skills, Projects, Recommendations)
├── style.css    --> External Stylesheet (Flexbox/Grid, hover states, card styling, nút scroll-to-top)
└── script.js    --> Xử lý sự kiện form, tạo DOM element động, hiển thị modal/popup xác nhận
```

### Ánh xạ các yêu cầu cốt lõi sang kiến thức Module 1–3

| Phần chức năng | Công nghệ HTML5 / CSS3 / JS áp dụng | Yêu cầu kỹ thuật trọng tâm |
| --- | --- | --- |
| **Thanh điều hướng (Navbar)** | `<header>`, `<nav>`, Flexbox, pseudo-class `:hover` | Hiển thị tên/thông tin liên hệ bên trái, các liên kết neo (`#about-me`, `#skills`, `#projects`, `#recommendations`) đổi kiểu chữ (đậm + gạch chân) khi di chuột |
| **Khu vực About Me & Skills** | `<section>`, `<figure>`, CSS Grid / Flexbox cards | Trình bày ảnh đại diện, tiểu sử ngắn và lưới thẻ kỹ năng (logo + tên công nghệ + số năm kinh nghiệm) |
| **Danh sách Projects** | `<article>` / `<section>`, danh sách có thứ tự rõ ràng | Tách biệt từng dự án với tiêu đề và mô tả ngắn gọn, căn lề thống nhất |
| **Recommendations động** | `document.getElementById()`, `document.createElement()`, `appendChild()` | Khi người dùng nhập lời nhận xét và bấm Submit: thêm thẻ mới vào DOM ngay lập tức mà **không reload trang**, sau đó bật hộp thoại xác nhận (popup) |
| **Nút quay về đầu trang** | `<a href="#home">` kèm biểu tượng SVG cố định (`position: fixed`) | Trải nghiệm điều hướng thuận tiện trên trang dài |

## 2. Mẫu luồng xử lý DOM động cho tính năng Recommendations

```javascript
function addRecommendation() {
  const input = document.getElementById("new_recommendation");
  const text = input.value.trim();
  if (!text) return;

  // 1. Tạo phần tử DOM mới và gán nội dung an toàn bằng textContent
  const card = document.createElement("div");
  card.className = "recommendation-card";
  card.textContent = `“${text}”`;

  // 2. Chèn vào danh sách hiện có trên trang
  document.getElementById("all_recommendations").appendChild(card);

  // 3. Xóa ô nhập liệu & hiện popup xác nhận
  input.value = "";
  showPopup(true);
}
```

> **Lưu ý bảo mật (XSS Prevention):** Khi chèn văn bản do người dùng nhập vào DOM, ưu tiên dùng `textContent` thay vì `innerHTML` để tránh trình duyệt thực thi mã HTML/script độc hại nếu người dùng cố tình nhập thẻ `<script>`.

## 3. Checklist kiểm thử trước khi nộp dự án

1. **Validate HTML & CSS:** Không thiếu thẻ đóng, không sai tên thuộc tính, có `<!DOCTYPE html>` ở dòng đầu.
2. **Kiểm tra đa trình duyệt & Responsive:** Mở thử ở màn hình desktop và thu nhỏ cửa sổ để chắc chắn không bị tràn ngang (horizontal overflow).
3. **Kiểm tra trạng thái rỗng (Edge Case):** Bấm nút gửi Recommendation khi ô nhập trống không được tạo thẻ rỗng.
4. **Kiểm tra DevTools Console:** Đảm bảo 0 lỗi JavaScript runtime (`TypeError`, `ReferenceError`).

## 4. Liên kết lộ trình sang các khóa tiếp theo trong DWP301c

- **Khóa 3 (Git & GitHub):** Đưa mã nguồn Portfolio lên GitHub Repository, quản lý nhánh (branch), commit lịch sử sạch và xuất bản bằng GitHub Pages.
- **Khóa 4 (React & Redux):** Chuyển đổi từ thao tác DOM thủ công (`createElement`, `appendChild`) sang mô hình **Component khai báo (Declarative UI)** và **Virtual DOM** của React.
- **Khóa 5–7 (Docker, Kubernetes, Microservices & Capstone):** Kết nối ứng dụng Front-End với các dịch vụ Back-End và triển khai Cloud-Native hoàn chỉnh.
