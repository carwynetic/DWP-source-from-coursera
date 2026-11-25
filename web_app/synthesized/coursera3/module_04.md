# Module 4: [Optional] Working with GitHub from Your Windows Desktop

> **Tư tưởng cốt lõi:** Chuyển dịch từ Cloud IDE sang môi trường làm việc thực tế trên máy tính cá nhân (Windows/macOS/Linux) bằng cách cài đặt Git CLI (Git Bash trên Windows), định danh người dùng toàn cục và thiết lập cặp khóa xác thực **SSH Key** để đẩy/kéo mã nguồn an toàn với GitHub mà không cần nhập mật khẩu mỗi lần.

## 1. Cài đặt Git trên các hệ điều hành phổ biến

| Hệ điều hành | Cách cài đặt / kích hoạt chuẩn | Ghi chú quan trọng |
| --- | --- | --- |
| **Linux (RPM: Red Hat / Fedora)** | `sudo dnf install git-all` | Thường có sẵn Git trên đa số bản phân phối Linux |
| **Linux (Debian / Ubuntu)** | `sudo apt install git-all` | Cài đầy đủ gói Git và các tiện ích đi kèm |
| **macOS** | Chạy `git version` để kích hoạt Xcode Command Line Tools (hoặc tải **MacOS Git Installer** bản mới nhất) | Kiểm tra lại phiên bản bằng `git --version` sau khi cài |
| **Windows** | Tải và cài **Git for Windows** → sử dụng **Git Bash** (hoặc cài thêm **GitHub Desktop** cho giao diện đồ họa GUI) | **Git Bash** cung cấp sẵn các lệnh Linux Bash quen thuộc (`ls`, `pwd`, `cat`, `mkdir`, `cd`) cùng toàn bộ lệnh `git` |

## 2. Cấu hình định danh Git và Thiết lập SSH Key kết nối GitHub

Khi làm việc từ máy cá nhân, GitHub không còn cho phép xác thực bằng mật khẩu tài khoản qua HTTPS; phương pháp chuẩn và tiện lợi nhất là dùng **SSH Key** (hoặc Personal Access Token).

```bash
# Bước 1: Khai báo tên và email gắn với mọi commit của bạn
git config --global user.name "Your Full Name"
git config --global user.email "your_email@example.com"

# Bước 2: Tạo cặp khóa SSH mới (thuật toán hiện đại Ed25519)
ssh-keygen -t ed25519 -C "your_email@example.com"
# Nhấn Enter để lưu mặc định tại ~/.ssh/id_ed25519 (và ~/.ssh/id_ed25519.pub)

# Bước 3: Khởi động ssh-agent và nạp private key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Bước 4: Hiển thị nội dung PUBLIC key để sao chép lên GitHub
cat ~/.ssh/id_ed25519.pub
```

### Bước 5: Thêm Public Key vào GitHub & Kiểm tra kết nối

1. Đăng nhập GitHub → **Settings** → **SSH and GPG keys** → **New SSH key**.
2. Dán toàn bộ nội dung tệp `.pub` (bắt đầu bằng `ssh-ed25519 ...`) → bấm **Add SSH key**.
3. Kiểm tra kết nối từ Git Bash:

```bash
ssh -T git@github.com
# Kết quả thành công: "Hi <username>! You've successfully authenticated, but GitHub does not provide shell access."
```

## 3. Bẫy thường gặp & Lưu ý bảo mật (Critical Pitfalls)

1. **Chia sẻ nhầm Private Key thay vì Public Key:** Chỉ bao giờ dán nội dung file có đuôi **`.pub`** (`id_ed25519.pub`) lên GitHub; **tuyệt đối không** chia sẻ hay commit file khóa riêng (`id_ed25519`).
2. **Clone bằng URL HTTPS nhưng lại cấu hình SSH:** Để sử dụng SSH key vừa tạo, hãy copy đường dẫn tab **SSH** (`git@github.com:user/repo.git`) khi chạy `git clone` hoặc đổi URL bằng `git remote set-url origin git@github.com:user/repo.git`.
3. **Quên đặt `user.email` khớp email GitHub:** Nếu email trong `git config` không khớp email đã xác minh trên tài khoản GitHub, các commit đẩy lên sẽ không được tính vào biểu đồ đóng góp (contribution graph) của bạn.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- Trên Windows, **Git Bash** (đi kèm Git for Windows) là công cụ dòng lệnh tiêu chuẩn vừa chạy được lệnh Git vừa chạy được lệnh Linux shell (`ls`, `pwd`, `cat`).
- **GitHub Desktop** là lựa chọn GUI trực quan cho cả Windows và macOS nếu muốn thao tác nhánh/commit bằng giao diện.
- Thiết lập **SSH Key** một lần giúp kết nối an toàn, nhanh chóng giữa máy trạm cá nhân và mọi kho lưu trữ trên GitHub.
