# Module 6: Share Your Project (Documentation, Verification & Submission Rubric)

> **Tư tưởng cốt lõi:** Một dự án Full-Stack hoàn chỉnh không chỉ chạy đúng trên máy lập trình viên mà còn phải có **tài liệu minh bạch, bằng chứng kiểm thử tái lập được (cURL outputs, terminal logs, CI/CD pass, URL triển khai)** và sẵn sàng đưa vào Portfolio nghề nghiệp chuyên nghiệp.

## 1. Cấu trúc Bộ hồ sơ nộp bài & Tiêu chí đánh giá (50-Point AI-Graded Rubric)

Dự án Capstone được đánh giá dựa trên 4 nhóm bằng chứng kỹ thuật thực tế từ repository công khai của bạn:

| Nhóm bằng chứng (Artifacts) | Nội dung cốt lõi cần kiểm chứng |
| --- | --- |
| **1. Public GitHub Repository** | - `README.md` mô tả rõ tên dự án & kiến trúc<br>- `server/frontend/static/About.html` và `Contact.html` (đúng CSS links, navbar active, ảnh & thông tin thực tế)<br>- Mã nguồn Django Models (`CarMake`, `CarModel`), Views, `restapis.py`, Express API, React Components, `Dockerfile`, `deployment.yaml`<br>- Tab **GitHub Actions** thể hiện workflow linting **Passed** |
| **2. Terminal & Server Logs** | - Tệp `django_server`: output chạy máy chủ Django không lỗi<br>- Output kiểm chứng Docker container & Kubernetes Pods/Services đang ở trạng thái `Running` |
| **3. cURL API Outputs** | - `loginuser`: lệnh `cURL` & phản hồi JSON chứng minh đăng nhập hợp lệ<br>- `logoutuser`: lệnh `cURL` chứng minh đăng xuất thành công<br>- Các lệnh `cURL` truy vấn `get_dealers`, `get_dealers/<state>`, `get_dealer_reviews`, `analyze/<text>` |
| **4. Live Deployment & Screenshots** | - URL ứng dụng đã triển khai (Kubernetes / Code Engine)<br>- Ảnh chụp màn hình kiểm thử end-to-end: Trang chủ, About, Contact, Đăng ký, Đăng nhập, Danh sách đại lý (có lọc bang), Chi tiết đại lý (kèm icon sentiment) và Đăng đánh giá mới thành công |

## 2. Checklist kiểm chứng cuối cùng trước khi nộp (Pre-Submission Audit)

1. **Kiểm tra quyền truy cập Repository:** Repo GitHub phải ở chế độ **Public** để hệ thống chấm bài / nhà tuyển dụng truy cập được trực tiếp các đường dẫn tệp (`README.md`, `About.html`, `Contact.html`).
2. **Kiểm tra không lộ Secrets:** Rà soát toàn bộ commit chắc chắn không đẩy nhầm mật khẩu production, IBM Cloud API Key hay tệp `.env` chứa thông tin nhạy cảm lên repo Public.
3. **Kiểm tra tính nhất quán giữa URL và Log:** URL triển khai khai báo phải khớp với URL xuất hiện trong các bản log kiểm thử và ảnh chụp màn hình.
4. **Chuẩn hóa Portfolio & Định hướng nghề nghiệp:**
   - Viết `README.md` có sơ đồ kiến trúc hệ thống, danh sách công nghệ (Django, React, Express, MongoDB, Flask/NLTK, Docker, Kubernetes, GitHub Actions) và hướng dẫn chạy cục bộ từng bước để đưa vào CV/Portfolio.
   - Bước tiếp theo trong lộ trình chứng chỉ IBM là hoàn thành bài đánh giá tổng hợp (**Full Stack Software Developer Assessment**) và chuẩn bị kỹ năng phỏng vấn kỹ thuật (System Design, Git workflow, API & Cloud-Native debugging).

## 3. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Bằng chứng xác minh thực tế** (CI xanh, `cURL` JSON outputs, Kubernetes `Running` pods, E2E screenshots) quan trọng ngang bằng với việc viết code chạy được.
- Bảo mật mã nguồn (không commit API keys/secrets) và tài liệu `README.md` rõ ràng là chuẩn mực bắt buộc của kỹ sư Full-Stack chuyên nghiệp.
