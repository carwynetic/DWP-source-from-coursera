# Module 5: Career Opportunities & Final Project

> **Tư tưởng cốt lõi:** Chuyển hóa kiến thức HTML5, CSS3 và JavaScript thành năng lực nghề nghiệp đòi hỏi hai trụ cột: **(1) Thực chiến tích hợp toàn bộ front-end stack vào Final Project hoàn chỉnh** để xây dựng portfolio thực tế, và **(2) Tư duy kỹ sư Cloud-Native bền vững** — chọn sâu một tech stack thay vì làm hời hợt nhiều dự án rời rạc, rèn thói quen bảo mật từ đầu và chủ động thích nghi với tốc độ đổi mới liên tục của công nghệ đám mây.

## 1. Kiến thức & Kỹ năng Cốt lõi của Lập trình viên Web / Cloud-Native

Từ góc nhìn của các kỹ sư và chuyên gia IBM trong bài giảng *Career Paths for Web Application Development*, một lập trình viên Web / Full-Stack Cloud-Native cần hội tụ đồng thời cả **năng lực kỹ thuật** và **kỹ năng nghề nghiệp**:

| Trụ cột năng lực | Yêu cầu cụ thể trong thực tế doanh nghiệp |
| --- | --- |
| **Tư duy học tập & Thích nghi (*Comfort with Ambiguity*)** | Kỹ năng quan trọng nhất: **luôn sẵn sàng học cái mới và thoải mái khi làm việc với dịch vụ chưa từng dùng**. Nền tảng Cloud cập nhật tính năng liên tục — nắm bắt dịch vụ mới giúp tận dụng giải pháp có sẵn thay vì tự viết lại từ đầu. |
| **Kỹ năng Kỹ thuật Full-Stack** | Làm chủ **Front-end** (HTML, CSS, JS), **Back-end & APIs** (thành thạo ít nhất 1 ngôn ngữ như **Python** hoặc **Node.js**), **Databases** (SQL/NoSQL), **Web Architecture**, thiết kế UI cơ bản và **Git**. |
| **Hệ sinh thái Cloud-Native** | Hiểu bức tranh tổng quan dịch vụ của ít nhất một Cloud Provider lớn; nắm **Containers (Docker)**, **Container Orchestration (Kubernetes, OpenShift)** *(đường cong học tập dốc nhưng rất giá trị)* và **Serverless** *(triển khai theo từng hàm đơn nhiệm, dễ tiếp cận và mở rộng)*. |
| **Bảo mật (*Security Mindset*)** | Bảo mật hiện diện ở mọi lớp (từ client-side XSS/sandbox đến API auth & hạ tầng). Không bao giờ để lại lỗ hổng bảo mật trong ứng dụng vì thiếu hiểu biết quy chuẩn an toàn. |
| **Kỹ năng Mềm & Quy trình** | Quản lý thời gian & dự án, chú ý đến tiểu tiết (*attention to detail*), giao tiếp rõ ràng và thấu hiểu yêu cầu khách hàng gắn với tầm nhìn kinh doanh tổng thể. |

## 2. Chiến lược Học tập & Định vị Nghề nghiệp (Career Advice)

Các chuyên gia đưa ra 3 lời khuyên chiến lược cho người mới bước vào ngành Web & Cloud Development:

1. **Chọn một Stack và đào sâu đến mức thành thạo (*Pick a stack and stick with it*):**
   - *Sai lầm phổ biến:* Làm 12 ứng dụng "To-Do List" bằng 12 ngôn ngữ/framework khác nhau nhưng không làm chủ sâu bất kỳ công nghệ nào.
   - *Cách đúng:* Chọn một tổ hợp rõ ràng (ví dụ **HTML/CSS/JS + React + Node.js/Express** hoặc **Python + Django/Flask**) và xây dựng dự án có chiều sâu với xử lý lỗi, kiểm thử, xác thực và triển khai thực tế.
2. **Đào sâu một mũi nhọn (Front-End hoặc Back-End) trước khi dàn trải:**
   - Thực tế rất khó để xuất sắc đồng thời cả UI/UX tinh xảo lẫn thiết kế API/data pipeline phức tạp. Hãy đạt trình độ vững chắc ở một phía (Front-end hoặc Back-end/Microservices gắn với Cloud infrastructure) rồi mở rộng sang phía còn lại để thành Full-Stack thực thụ.
3. **Xây dựng Portfolio & Mạng lưới kết nối (*Networking*):**
   - Hoàn thành các bài thực hành hands-on và đưa mã nguồn sạch lên **GitHub** kèm tài liệu mô tả để nhà tuyển dụng kiểm chứng năng lực thực tế.
   - Tận dụng networking chuyên nghiệp (ngay cả kết nối bậc 2 — *second-degree connections*) để hồ sơ của bạn nổi bật giữa hàng trăm CV nộp trực tuyến.

## 3. Tổng hợp Kỹ thuật cho Final Project (HTML5 + CSS3 + JavaScript)

Dự án cuối khóa yêu cầu vận dụng phối hợp 3 công nghệ nền tảng theo đúng nguyên tắc **tách biệt trách nhiệm (Separation of Concerns)** đã học qua các Module 1–4:

```text
project-root/
├── index.html   # Cấu trúc HTML5 ngữ nghĩa: <header>, <nav>, <section>, <article>, <figure>, <footer>
├── style.css    # External CSS: Thiết lập base styles, Fluid/Flexbox/Grid layout, trạng thái :hover
└── script.js    # JavaScript & DOM API: Xử lý sự kiện (onclick/onsubmit), validate form, tạo/chèn node động
```

### Checklist Rà soát Kỹ thuật trước khi Hoàn thành Final Project

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="keywords" content="Portfolio, Web Developer, HTML5, CSS3, JavaScript">
  <title>Developer Portfolio</title>
  <!-- Ưu tiên External CSS để tách biệt giao diện khỏi dữ liệu -->
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <nav><!-- Các liên kết điều hướng nội trang --></nav>
  </header>

  <main>
    <section id="about"><!-- Thông tin cá nhân dùng figure/figcaption --></section>
    <section id="projects"><!-- Mỗi dự án có thể bọc bằng article --></section>
    <section id="contact">
      <form onsubmit="return validateForm(event)">
        <input id="emailInput" type="email" placeholder="name@example.com" required>
        <button type="submit">Send</button>
      </form>
    </section>
  </main>

  <!-- Đặt script ở cuối body để không chặn quá trình render HTML -->
  <script src="script.js"></script>
  <noscript>Vui lòng bật JavaScript để gửi biểu mẫu tương tác.</noscript>
</body>
</html>
```

```javascript
// Mẫu thao tác DOM an toàn & tránh biến toàn cục trong script.js
(function () {
  function validateForm(event) {
    event.preventDefault();
    const emailEl = document.getElementById("emailInput");
    const emailValue = emailEl.value.trim();
    if (!emailValue) {
      window.alert("Vui lòng nhập email hợp lệ.");
      return false;
    }
    const output = document.createElement("p");
    output.textContent = "Đã ghi nhận liên hệ: " + emailValue; // Dùng textContent để phòng tránh XSS
    document.getElementById("contact").appendChild(output);
    return true;
  }
  window.validateForm = validateForm;
})();
```

## 4. Lộ trình Học tiếp trong Chương trình IBM Full-Stack

Sau khóa *Introduction to Web Development with HTML, CSS, JavaScript*, tài liệu khóa học gợi ý 3 hướng mở rộng trực tiếp:
- **Developing Cloud Native Applications:** Tư duy Cloud Native, CNCF, hạ tầng Hybrid Cloud, hiện đại hóa ứng dụng (*application modernization*) và CI/CD.
- **Developing Cloud Apps with Node.js and React:** Đào sâu JavaScript phía server với Node.js (nền tảng được 51.4% lập trình viên sử dụng theo khảo sát Stack Overflow 2020) và kiến trúc component với React.
- **IBM Full Stack Software Developer Professional Certificate:** Lộ trình trọn bộ từ Git/GitHub, React, Node/Express, Python/Flask/Django đến Docker, Kubernetes, OpenShift, Microservices và Capstone Project.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Học lan man quá nhiều công nghệ cùng lúc:** Chuyển framework liên tục chỉ để làm các app đơn giản khiến bạn thiếu chiều sâu khi phỏng vấn kỹ thuật; hãy chọn 1 stack chuẩn và đào sâu.
2. **Xem nhẹ Validation phía Server & XSS khi làm Final Project:** HTML5 `type="email"` hoặc `required` chỉ là lớp kiểm tra tiện ích trên trình duyệt (có thể bị tắt hoặc khác nhau giữa các trình duyệt); luôn kết hợp kiểm tra JS và server, đồng thời dùng `textContent` thay cho `innerHTML` khi chèn dữ liệu người dùng vào DOM.
3. **Bỏ qua kiểm tra đa trình duyệt & Fallback:** Trước khi chốt giao diện dự án, luôn đối chiếu tính năng mới trên `caniuse.com`, kiểm tra HTML/CSS bằng validator và kiểm tra Console trên DevTools.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- Tố chất hàng đầu của Cloud-Native / Full-Stack Developer là **thoải mái với sự thay đổi (ambiguity)**, học tập liên tục và nắm vững một stack cốt lõi (như **Python** hoặc **Node.js** kèm **Docker/K8s/Serverless**).
- Hoàn thiện **Final Project** chuẩn 3 tầng tách biệt (**HTML5 ngữ nghĩa – External CSS – JS DOM an toàn**) là viên gạch đầu tiên xây dựng Portfolio chuyên nghiệp.
- Kết hợp năng lực kỹ thuật với **tư duy bảo mật**, **kỹ năng mềm** và **networking** để bứt phá trong lộ trình *IBM Full Stack Software Developer*.