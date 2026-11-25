# Module 2: Git Commands and Managing GitHub Projects

> **Tư tưởng cốt lõi:** Làm chủ quy trình Git chuẩn từ máy cục bộ lên remote (`clone/init → branch → add → commit → push → PR → pull`), phân biệt rạch ròi giữa Clone và Fork, đồng thời nắm vững bộ lệnh theo 3 vai trò dự án: Developer, Integrator và Repository Administrator.

## 1. Quy trình làm việc chuẩn (Standard Git Workflow)

Một quy trình cộng tác an toàn giúp tránh xung đột mã nguồn và không ghi đè công việc của đồng đội gồm 8 bước:

```text
[Remote GitHub Repo] ──(git clone)──▶ [Local Repo]
                                          │
                           (git checkout -b feature-x)
                                          ▼
                   [Working Dir] ──(git add)──▶ [Staging Area] ──(git commit)──▶ [Local Branch]
                                                                                       │
                   [Local main] ◀──(git pull)── [GitHub PR & Merge] ◀──(git push)──────┘
```

1. **Clone hoặc Init:** Tải bản sao kho chứa từ GitHub (`git clone <url>`) hoặc khởi tạo kho mới cục bộ (`git init`).
2. **Staging & Initial Commit:** Đưa tệp vào vùng đệm (`git add`) và thực hiện **Initial Commit** (commit đầu tiên xác lập điểm mốc cơ sở/baseline cho lịch sử kho chứa).
3. **Branching:** Tạo không gian làm việc tách biệt (`git branch <name>` / `git checkout -b <name>`) để phát triển tính năng mà không ảnh hưởng nhánh chính.
4. **Stage & Commit:** Kiểm tra trạng thái (`git status`), đưa thay đổi vào staging (`git add`), lưu snapshot (`git commit -m "..."`).
5. **Push:** Đẩy các commit cục bộ lên kho từ xa (`git push origin <branch>`).
6. **Pull Request & Merge:** Mở PR trên GitHub để review và hợp nhất vào `main`.
7. **Sync:** Kéo bản cập nhật mới nhất về máy cục bộ (`git pull`).

## 2. Bảng lệnh Git CLI thiết yếu (Local & Remote)

| Nhóm lệnh | Lệnh Git | Chức năng chính |
| --- | --- | --- |
| **Khởi tạo & Kiểm tra** | `git init` | Khởi tạo kho Git mới trong thư mục hiện tại (tạo `.git/`) |
| | `git status` | Xem trạng thái **Working Directory** và **Staging Area** (file đã sửa, đã stage, chưa theo dõi) |
| | `git log` | Xem toàn bộ **lịch sử commit** (hash, tác giả, thời gian, message) |
| **Lưu thay đổi** | `git add <file>` / `git add .` | Đưa thay đổi từ Working Directory vào **Staging Area** |
| | `git commit -m "msg"` | Lưu ảnh chụp đã staged vào lịch sử local repository |
| **Nhánh (Branching)** | `git branch <name>` | Tạo nhánh mới (hoặc liệt kê các nhánh nếu không truyền tên) |
| | `git checkout <branch>` | Chuyển sang và **kích hoạt (make active)** nhánh chỉ định (`git checkout -b <name>` để tạo + chuyển ngay) |
| | `git merge <branch>` | Hợp nhất lịch sử của `<branch>` vào nhánh hiện tại |
| **Kho từ xa (Remote)** | `git clone <url>` | Tạo bản sao hoàn chỉnh (code + toàn bộ lịch sử Git) về máy cục bộ |
| | `git push` | Đẩy các commit cục bộ lên remote repository (GitHub) |
| | `git fetch` | Tải thông tin commit mới từ remote về máy nhưng **chưa tự động merge** |
| | `git pull` | Thực hiện **fetch + merge trong một bước duy nhất** để đồng bộ với upstream/remote |
| **Hoàn tác an toàn** | `git revert <commit>` | Tạo một commit mới đảo ngược thay đổi của commit lỗi (**an toàn cho lịch sử chung**, không xóa lịch sử cũ) |

```bash
# Ví dụ trọn bộ 3 bước đẩy thay đổi cục bộ lên GitHub
git add index.html
git commit -m "Add responsive header section"
git push origin PATCH-1-ADDING-HEADERS

# Đồng bộ nhánh hiện tại với upstream trong 1 bước (fetch + merge)
git pull upstream main
```

## 3. Clone vs. Fork — Khi nào dùng cách nào?

| Tiêu chí | `git clone` (Cloning) | Fork (Forking) |
| --- | --- | --- |
| **Vị trí thực hiện** | Tạo bản sao từ remote xuống **máy cục bộ (local machine)** | Tạo bản sao độc lập từ kho gốc (**upstream**) sang **tài khoản GitHub của bạn** trên server |
| **Cách thực hiện** | Bằng lệnh CLI `git clone <HTTPS/SSH URL>` | **Chỉ có trên giao diện web GitHub** (nút **Fork** ở góc trên trang repo — *không có lệnh `git fork` gốc*) |
| **Mục đích sử dụng** | Tham gia phát triển trực tiếp cùng nhóm trên cùng một repo và đồng bộ hai chiều | Tạo bản phái sinh/mở rộng dự án mà **không làm ảnh hưởng kho gốc**, hoặc đóng góp vào dự án mã nguồn mở bạn không có quyền push trực tiếp |
| **Lưu ý Download ZIP** | `Download ZIP` chỉ tải code hiện tại, **mất hoàn toàn thông tin version control (`.git`)** | Sau khi Fork trên GitHub, bạn thường `git clone` bản fork về máy để làm việc và dùng `git pull` từ `upstream` để cập nhật |

## 4. Ba vai trò quản lý dự án trên GitHub & Lệnh tương ứng

| Vai trò | Trách nhiệm chính | Bộ lệnh Git đặc trưng |
| --- | --- | --- |
| **Developer (Participant)** | Viết code, tạo nhánh, đồng bộ thay đổi với kho chung và gửi yêu cầu tích hợp | `git clone`, `git fetch`, `git pull`, `git push`, `git request-pull` |
| **Integrator** | Nhận thay đổi từ các lập trình viên, review, hợp nhất (merge), **hoàn tác các commit lỗi (botched commits)** và xuất bản bản phát hành | `git pull`, **`git revert`**, `git push` |
| **Repository Administrator** | Tổ chức cấu trúc kho chứa, phân quyền người dùng, cấu hình server/web services, thiết lập email/index và quản trị hệ thống | Quản trị cấu hình server, quyền truy cập & chính sách nhánh |

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm `Download ZIP` với `git clone`:** Tải ZIP không có thư mục `.git`, không thể `git status`, `git log` hay `git push`.
2. **Tìm lệnh `git fork` trong terminal:** Fork là tính năng của nền tảng GitHub (nút **Fork** trên web), không phải lệnh Git bản địa.
3. **Nhầm `git fetch` và `git pull`:** `git fetch` chỉ kéo dữ liệu về để xem trước mà không đụng vào working tree; `git pull` thực hiện cả `fetch` lẫn `merge` ngay lập tức.
4. **Dùng `git reset --hard` trên nhánh chung thay vì `git revert`:** Integrator cần dùng **`git revert`** để hoàn tác commit hỏng vì `revert` bảo toàn lịch sử minh bạch và không gây lỗi xung đột lịch sử cho các thành viên khác.
5. **Quên `git add` trước khi `git commit`:** Git chỉ đóng gói các tệp nằm trong **Staging Area**; file mới sửa ở Working Directory chưa `git add` sẽ không nằm trong commit.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- 3 lệnh phổ biến nhất làm việc với remote repository: **`git clone`**, **`git push`**, **`git pull`** (cùng `git fetch`).
- 3 bước đẩy thay đổi cục bộ lên GitHub: `git add` → `git commit` → **`git push`**.
- `git status` kiểm tra Working Directory & Staging Area; `git log` xem lịch sử commit; `git checkout <branch>` kích hoạt nhánh.
- Integrator dùng **`git revert`** để hoàn tác commit lỗi; Developer dùng **`git pull`** / **`git fetch`** để cập nhật theo `upstream`.
