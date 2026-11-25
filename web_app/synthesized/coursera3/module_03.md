# Module 3: Final Project and Assessment (& GitHub Copilot)

> **Tư tưởng cốt lõi:** Ứng dụng trọn vẹn quy trình Git/GitHub thực chiến (Fork → Clone → Branch → Commit → Push → Pull Request → Merge) để xây dựng và hoàn thiện một dự án mã nguồn mở hoàn chỉnh (kèm License, Code of Conduct, Contributing guide và kịch bản tính toán), đồng thời tận dụng trợ lý AI **GitHub Copilot** một cách có kiểm soát.

## 1. Quy trình tổng hợp trong Final Project (Open-Source Collaboration Workflow)

Trong bài đánh giá cuối khóa, bạn thực hành đóng vai người đóng góp cho một dự án mã nguồn mở tiêu chuẩn trên GitHub theo chuỗi thao tác khép kín:

| Giai đoạn | Thao tác thực hiện | Mục tiêu kiểm tra |
| --- | --- | --- |
| **1. Thiết lập dự án chuẩn** | Tạo repository công khai, thêm `LICENSE` (Apache 2.0), `README.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` | Chứng minh nắm vững tiêu chuẩn tài liệu & pháp lý của dự án open-source |
| **2. Viết script & Commit** | Thêm tập lệnh nghiệp vụ (ví dụ `simple-interest.sh`) trên nhánh làm việc | Thực hành `git add`, `git commit -m "..."` với thông điệp rõ ràng |
| **3. Fork & Clone** | Fork kho mẫu của tổ chức về tài khoản cá nhân → `git clone` về môi trường phát triển | Phân biệt rõ `upstream` (kho gốc) và `origin` (bản fork cá nhân) |
| **4. Branch & Fix** | Tạo nhánh sửa lỗi (`git checkout -b bug-fix-typo`), chỉnh sửa lỗi nhỏ trong `README.md`, commit & `git push origin bug-fix-typo` | Không chỉnh sửa trực tiếp trên `main`, giữ lịch sử nhánh sạch |
| **5. Pull Request & Merge** | Mở Pull Request từ nhánh sửa lỗi vào nhánh đích, thực hiện review & merge, sau đó đồng bộ lại local bằng `git pull` | Hoàn tất vòng đời cộng tác nhóm chuẩn công nghiệp |

```bash
# Kiểm tra nhanh cấu hình remote và lịch sử nhánh trước khi nộp bài
git remote -v
git branch -a
git log --oneline --graph --all
```

## 2. GitHub Copilot — Trợ lý lập trình AI trong quy trình GitHub

Module 3 giới thiệu **GitHub Copilot** — công cụ AI hoạt động như plug-in trong các trình soạn thảo mã nguồn (như Visual Studio Code, JetBrains, Neovim) nhằm tăng tốc quá trình lập trình:

- **Tính năng cốt lõi:**
  - **Code Auto-Completion theo ngữ cảnh (Contextual Suggestions):** Tự động gợi ý từng dòng hoặc toàn bộ hàm, lớp, vòng lặp dựa trên tên biến, tên hàm, comment và ngữ cảnh file hiện tại (ví dụ: khai báo biến `total_quantity` trong Python → Copilot gợi ý luôn cấu trúc vòng lặp `for` và phép tính liên quan).
  - **Hỗ trợ đa ngôn ngữ & đa framework:** Python, JavaScript, TypeScript, HTML/CSS, Bash, Go, Java...
  - **Giảm thời gian viết mã lặp lại (boilerplate):** Nhanh chóng sinh khung hàm, test case cơ bản, biểu thức chính quy (regex) hoặc tài liệu docstring.
- **Quy trình sử dụng Copilot hiệu quả & có phản biện:**
  1. Viết comment hoặc tên hàm/biến rõ ràng, giàu ngữ nghĩa để cung cấp ngữ cảnh chuẩn xác cho AI.
  2. Xem xét kỹ từng đoạn mã gợi ý trước khi chấp nhận (`Tab`).
  3. **Luôn tự kiểm thử (Unit Test) và rà soát bảo mật/logic:** Copilot có thể sinh mã trông hợp lý nhưng sai trường hợp biên (edge cases), dùng API cũ hoặc tiềm ẩn lỗ hổng bảo mật. Trách nhiệm chất lượng mã nguồn cuối cùng luôn thuộc về lập trình viên.

## 3. Checklist tự đánh giá trước khi hoàn thành Khóa 3

- Đã phân biệt rõ **Git** (DVCS cục bộ) và **GitHub** (nền tảng lưu trữ & cộng tác).
- Không còn nhầm lẫn giữa **Clone** (tải về máy cục bộ) và **Fork** (sao chép trên tài khoản GitHub).
- Thành thạo toàn bộ bộ lệnh cốt lõi: `init`, `clone`, `status`, `add`, `commit`, `branch`, `checkout`, `merge`, `fetch`, `pull`, `push`, `revert`, `log`.
- Biết sử dụng Pull Request để code review trước khi hợp nhất vào `main`.
