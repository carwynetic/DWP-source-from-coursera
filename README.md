# Coursera Multiple-Choice Quiz Raw Crawler (DWP301c)

Script Python dùng **Playwright + Microsoft Edge** để mở trình duyệt thật, cho bạn **tự đăng nhập Coursera**, sau đó tự động quét toàn bộ các module của khóa học, vào từng bài **Practice Quiz / Graded Quiz dạng trắc nghiệm** (chỉ đọc, không bao giờ bấm Submit) và lưu dữ liệu thô ra file JSON + TXT.

## Cách chạy

Mở PowerShell tại thư mục `Source_from_Coursera`:

### 1. Chạy thử nghiệm trên Khóa 1 (khuyên dùng `--wait-enter` để không bị timeout khi đăng nhập)

```powershell
python coursera_quiz_crawler.py --course coursera1 --wait-enter
```

- Trình duyệt Microsoft Edge sẽ mở trang đăng nhập Coursera.
- Bạn tự đăng nhập tài khoản Coursera (phiên đăng nhập được lưu tại `%LOCALAPPDATA%\coursera_quiz_crawler_profile` để các lần chạy sau không cần đăng nhập lại).
- Sau khi đăng nhập xong, quay lại terminal nhấn **Enter** → script sẽ tự động quét toàn bộ các module và thu thập dữ liệu thô các câu hỏi trắc nghiệm.

### 2. Chỉ lấy Practice Quiz (bỏ qua Graded Quiz)

```powershell
python coursera_quiz_crawler.py --course coursera1 --only-practice --wait-enter
```

### 3. Chạy cho các khóa học tiếp theo (`coursera2` đến `coursera7`)

```powershell
python coursera_quiz_crawler.py --course coursera2
python coursera_quiz_crawler.py --course coursera3
python coursera_quiz_crawler.py --course coursera4
python coursera_quiz_crawler.py --course coursera5
python coursera_quiz_crawler.py --course coursera6
python coursera_quiz_crawler.py --course coursera7
```

Hoặc truyền trực tiếp URL khóa học bất kỳ:

```powershell
python coursera_quiz_crawler.py --url "https://www.coursera.org/learn/<course-slug>" --wait-enter
```

## Kết quả đầu ra

Dữ liệu thô được lưu tự động (và cập nhật sau mỗi bài quiz) tại:

```text
output/<course_key>_<course_slug>/
├── raw_quizzes.json   # Dữ liệu thô có cấu trúc (quiz, prompt, options, raw_block_text, raw_page_text)
└── raw_quizzes.txt    # Bản text thô dễ đọc để kiểm tra nhanh
```
