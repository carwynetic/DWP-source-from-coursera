# Module 1: Git and GitHub Fundamentals

> **Tư tưởng cốt lõi:** Git là hệ thống quản lý phiên bản phân tán (DVCS) mã nguồn mở giúp mỗi lập trình viên giữ toàn bộ lịch sử mã nguồn trên máy cục bộ và phát triển phi tuyến tính qua các nhánh (branches); GitHub là nền tảng lưu trữ web cho các kho chứa Git, bổ sung quy trình cộng tác qua Pull Request, quản lý tổ chức (Organization) và bản quyền (License).

## 1. Version Control, Git và GitHub — Phân biệt rõ bản chất

- **Version Control System (VCS):** Hệ thống theo dõi mọi thay đổi của mã nguồn theo thời gian, giúp **khôi phục phiên bản cũ** khi có lỗi và **cộng tác nhóm** mà không ghi đè công việc của nhau.
- **Git (DVCS — Distributed Version Control System):**
  - Phần mềm mã nguồn mở phân phối theo giấy phép **GNU GPL**, do **Linus Torvalds** cùng cộng đồng Linux phát triển năm 2005 sau khi BitKeeper chuyển sang thu phí.
  - Là hệ thống **phân tán (distributed)**: mỗi lập trình viên sở hữu một bản sao đầy đủ cả mã nguồn lẫn toàn bộ lịch sử commit trên máy cá nhân.
  - **6 đặc trưng cốt lõi của mô hình Git Repository:**
    1. Hỗ trợ mạnh mẽ phát triển **phi tuyến tính (non-linear development)** thông qua branching & merging.
    2. Phát triển **phân tán (distributed)**.
    3. Tương thích với các hệ thống và giao thức hiện có.
    4. Xử lý hiệu quả các dự án quy mô lớn.
    5. **Xác thực mật mã lịch sử (cryptographic authentication of history)** (SHA hash) đảm bảo mọi bản sao có lịch sử đồng nhất.
    6. Chiến lược hợp nhất linh hoạt (**pluggable merge strategies**).
- **Git vs. GitHub:**

| Tiêu chí | Git | GitHub |
| --- | --- | --- |
| **Bản chất** | Công cụ/phần mềm DVCS chạy cục bộ (CLI/Desktop) | Dịch vụ lưu trữ nền web (web-hosted platform) cho các kho chứa Git |
| **Chức năng chính** | Theo dõi thay đổi, tạo commit, branch, merge lịch sử mã nguồn | Lưu trữ remote repository, quản lý **Pull Request**, Issue Tracking, Organization, Code Review, GitHub Actions/Pages |
| **Quan hệ** | Công cụ nền tảng | Nền tảng cộng tác xây dựng xoay quanh Git |

## 2. Cấu trúc cốt lõi trên GitHub: Repository, Organization, Working Directory & License

- **Repository (Repo):** Cấu trúc lưu trữ chứa tài liệu, mã nguồn ứng dụng cùng toàn bộ lịch sử phiên bản do Git theo dõi. Có thể đặt chế độ hiển thị **Public** (công khai) hoặc **Private** (riêng tư), thường khởi tạo kèm file `README.md`.
- **Organization (Tổ chức):** Tập hợp các tài khoản người dùng cùng sở hữu các repository; có một hoặc nhiều **owners** nắm quyền quản trị chung.
- **Working Directory (Thư mục làm việc):** Thư mục trên máy cục bộ chứa các tệp dự án bạn đang trực tiếp chỉnh sửa trước khi đưa vào staging area và commit.
- **Commit:** Hành động **lưu lại một ảnh chụp (snapshot)** các thay đổi vào lịch sử repository kèm thông điệp mô tả (commit message) giúp truy vết ai sửa gì, khi nào và tại sao.
- **License (Giấy phép mã nguồn):** Tệp văn bản quy định rõ quyền và giới hạn pháp lý cho người khác khi **sử dụng, sửa đổi và phân phối lại** mã nguồn trong repository (vd: MIT, Apache 2.0, GNU GPL).
- **Tạo tệp Python trực tiếp trên GitHub Web UI:** Mở repo → chọn **Add file** → **Create new file** → đặt tên có phần mở rộng `.py` (vd: `firstpython.py`) → nhập nội dung → điền commit message → bấm **Commit changes**.

## 3. Nhánh (Branches) và Pull Request (PR)

```text
main (nhánh chính — luôn chứa phiên bản ổn định, sẵn sàng triển khai)
  o─────────o───────────────────────o  (Merge sau khi review PR)
             \                     /
              o─────────o─────────o    (child/feature branch: phát triển & kiểm thử độc lập)
```

- **Main Branch:** Nhánh mặc định (mang tính chuẩn mực/definitive) lưu trữ **phiên bản mã nguồn hoàn chỉnh, sẵn sàng triển khai (deployable version)**.
- **Child / Feature Branch:** Một ảnh chụp (snapshot) tách ra từ `main` để lập trình viên phát triển tính năng, sửa lỗi hoặc thử nghiệm **mà không ảnh hưởng đến nhánh `main` hay công việc của thành viên khác**. Khi có nhiều nhánh cùng phát triển song song, điểm đầu mới nhất của mỗi nhánh gọi là **tip**.
- **Pull Request (PR):** Cơ chế **thông báo cho các thành viên khác** về các thay đổi bạn đã thực hiện trên nhánh con và **yêu cầu họ xem xét (code review), thảo luận và phê duyệt (approve)** trước khi hợp nhất (merge) vào nhánh chính (`main`).
- **Quyền sở hữu nhánh trên GitHub:** Nếu bạn cố gắng chỉnh sửa tệp trên một repository mà **bạn không sở hữu (không có quyền ghi trực tiếp)**, GitHub sẽ tự động tạo một **bản fork** thuộc tài khoản của bạn, lưu thay đổi trên nhánh của bản fork đó, rồi gợi ý mở **Pull Request** gửi về kho gốc.

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm Git và GitHub là một:** Git là công cụ DVCS quản lý phiên bản; GitHub là dịch vụ lưu trữ kho Git trên nền web cung cấp thêm PR, Issue, Organization.
2. **Sửa code trực tiếp trên nhánh `main`:** Phá vỡ tính ổn định của phiên bản deployable và dễ gây xung đột khi làm việc nhóm. Luôn tạo nhánh mới cho từng tính năng hoặc bản vá.
3. **Commit thiếu mô tả rõ ràng:** Commit message sơ sài (`"update"`, `"fix"`) làm mất giá trị truy vết lịch sử. Hãy viết ngắn gọn, nêu rõ mục đích thay đổi.
4. **Công khai repo mã nguồn mở nhưng quên thêm `LICENSE`:** Về mặt pháp lý, mã không có giấy phép mặc định giữ toàn bộ bản quyền, khiến cộng đồng không thể hợp pháp sử dụng hay đóng góp.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Git là **Distributed Version Control System (DVCS)** hỗ trợ phát triển phi tuyến tính và xác thực lịch sử bằng mật mã.
- Nhánh **`main`** lưu bản mã **deployable**; nhánh con dùng để phát triển và kiểm thử cô lập.
- **Commit** lưu thay đổi vào kho chứa; **Pull Request** yêu cầu nhóm review & phê duyệt trước khi merge vào nhánh chính.
- **Organization** quản lý tập hợp người dùng & repo; **License** xác định điều kiện pháp lý cho người dùng mã nguồn.
