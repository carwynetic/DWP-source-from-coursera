# Module 5: Final Project — Enhance Online Course App with New Features

> **Tư tưởng cốt lõi:** Tổng hợp toàn bộ kiến thức từ Module 1–4 để mở rộng một ứng dụng học trực tuyến (Online Course MVP) bằng **tính năng thi trắc nghiệm và chấm điểm tự động (Assessment Feature)** hoàn chỉnh từ thiết kế Models, Admin Inlines, Views, Templates đến kiểm thử end-to-end.

## 1. Kiến trúc dữ liệu của bài toán Online Course Assessment

Dựa trên dự án thực tế trong `coursera1/onlinecourse/`, hệ thống kết hợp đầy đủ 3 loại quan hệ ORM đã học ở Module 2:

```text
User (Django Auth)
 ├──< Instructor (FK) >──< Course (M2M)
 ├──< Learner (FK)
 └──< Enrollment (FK to User & Course; through table)
        └──< Submission (FK to Enrollment) >──< Choice (M2M)

Course
 ├──< Lesson (FK)
 └──< Question (FK to Course; M2M to Lesson)
        └──< Choice (FK to Question; is_correct: Boolean)
```

### 3 Model mới cốt lõi cần xây dựng trong Final Project

| Model | Quan hệ chính | Trường dữ liệu & Phương thức trọng tâm |
| --- | --- | --- |
| **`Question`** | `ForeignKey(Course)` + `ManyToManyField(Lesson)` | `question_text`, `question_point` (hoặc `grade`), phương thức `is_get_score(selected_ids)` kiểm tra học viên chọn đúng **toàn bộ** đáp án đúng và **không** chọn đáp án sai |
| **`Choice`** | `ForeignKey(Question)` | `choice_text`, `is_correct` (`BooleanField(default=False)`) |
| **`Submission`** | `ForeignKey(Enrollment)` + `ManyToManyField(Choice)` | Lưu lại toàn bộ tập `Choice` học viên đã tick trong một lần nộp bài |

## 2. Logic chấm điểm (Grading Algorithm) & Luồng Request

Một bẫy kinh điển khi chấm câu hỏi nhiều lựa chọn (multi-select) là chỉ đếm số đáp án đúng mà quên trừ/loại trường hợp chọn thêm đáp án sai. Logic chuẩn trong `Question.is_get_grade(selected_ids)`:

```python
def is_get_grade(self, selected_ids):
    all_answers = self.choice_set.filter(is_correct=True).count()
    selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
    selected_incorrect = self.choice_set.filter(is_correct=False, id__in=selected_ids).count()
    return all_answers > 0 and all_answers == selected_correct and selected_incorrect == 0
```

### Luồng End-to-End của tính năng Exam

1. **Admin Setup (`admin.py`):** Dùng `QuestionInline` trong `CourseAdmin` và `ChoiceInline` trong `QuestionAdmin` để tạo nhanh khóa học, câu hỏi và các phương án trả lời ngay trên giao diện Admin.
2. **Course Detail (`course_detail_bootstrap.html`):** Hiển thị danh sách bài học; nếu user đã đăng nhập (`user.is_authenticated`), hiển thị nút **Start Exam** mở form câu hỏi dạng collapse Bootstrap (gửi `POST` kèm `{% csrf_token %}` tới `onlinecourse:submit`).
3. **Submit View (`submit(request, course_id)`):**
   - Tìm `Enrollment` theo `(user, course)`.
   - Tạo bản ghi `Submission(enrollment=enrollment)`.
   - Trích xuất tất cả `choice_<id>` từ `request.POST`, gán vào `submission.choices.add(*selected_choices)`.
   - `redirect` sang `onlinecourse:show_exam_result` với `(course.id, submission.id)`.
4. **Result View (`show_exam_result(request, course_id, submission_id)`):**
   - Duyệt toàn bộ `course.question_set.all()`, cộng điểm cho từng câu đạt `is_get_score()`, tính phần trăm `grade = int(student_score / max_points * 100)`.
   - Render `exam_result_bootstrap.html`: báo **Passed** (≥ 80%) hoặc **Failed** (kèm nút Re-test), đồng thời tô màu xanh/vàng/đỏ từng phương án để học viên đối chiếu.

## 3. Liên kết lộ trình sang các khóa tiếp theo trong DWP301c

Hoàn thành Khóa 1 (SQL + Relational Databases + Full-Stack Django), kiến thức của bạn sẽ nối tiếp trực tiếp vào chuỗi khóa sau của chứng chỉ IBM Full Stack Software Developer:
- **Khóa 2 & 4 (HTML/CSS/JS & React):** Nâng cấp tầng giao diện từ Django Templates tĩnh/Bootstrap sang Single-Page Application hiện đại với React & Redux.
- **Khóa 3 (Git & GitHub):** Quản lý phiên bản, branching, merging, pull request cho toàn bộ mã nguồn.
- **Khóa 5 & 6 (Docker, Kubernetes, OpenShift & Microservices/Serverless):** Đóng gói ứng dụng Django/Node/Flask thành container, triển khai tự động trên IBM Cloud Code Engine & K8s.
- **Khóa 7 (Capstone Project):** Ghép toàn bộ stack **React + Django + Express/MongoDB + Flask Sentiment AI + CI/CD** thành một hệ thống hoàn chỉnh.
