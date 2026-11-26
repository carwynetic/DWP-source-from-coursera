# Module 2: Assessment for Application Cloud Developer — Chiến lược & Cheat Sheet Phòng Thi

> **Tư tưởng cốt lõi:** Kỳ thi cuối khóa (*Final Assessment*) kiểm tra khả năng kết nối kiến thức toàn diện từ Cloud đến Front-End, Back-End, Python/Django và Cloud-Native trên 45 câu hỏi trong 135 phút; nắm vững các bẫy câu hỏi nhiều lựa chọn (`multiple_select`) và đọc chính xác snippet code giúp bạn dễ dàng vượt ngưỡng đạt 70% ($\ge 32/45$ câu).

## 1. Cấu trúc & Quy chế kỳ thi Final Assessment

| Thông số kỳ thi | Giá trị chuẩn theo quy định | Chiến lược phân bổ thời gian |
| --- | --- | --- |
| **Số lượng câu hỏi** | **45 câu trắc nghiệm** (Single Choice & Multiple Select) | Trung bình **3 phút/câu**; ưu tiên làm nhanh câu lý thuyết nhận diện (< 1 phút) để dành thời gian cho câu đọc code & nhiều đáp án |
| **Thời gian làm bài** | **135 phút** (tính giờ liên tục) | Chia 3 chặng: 45 phút đầu quét toàn bộ 45 câu, 60 phút xử lý câu code/multi-select, 30 phút rà soát |
| **Điểm đạt tối thiểu** | **70%** (**ít nhất 32 / 45 câu đúng**) | Bắt buộc hoàn thành toàn bộ 11 khóa tiên quyết đạt $\ge 70\%$ trước khi thi |

## 2. Ma trận Ôn tập Nhanh theo 10 Chủ đề Trọng tâm (Rapid-Recall Matrix)

| Chủ đề | Từ khóa nhận diện nhanh trong đề thi | Đáp án / Quy tắc chốt hạ |
| --- | --- | --- |
| **Cloud Computing** | Essential characteristics (NIST); Exclusive single org; Fiber connection storage; Virtualization engine | *Resource pooling* & *Broad network access*; **Private cloud**; **Block storage**; **Hypervisors**; **Container** = code + libraries + dependencies |
| **HTML / CSS / JS** | Style & appeal; Path user interacts; Logical separations (chapters); Check data type; Global var | CSS = style/appeal; **Route** = path to page; `<section>`; `typeof`; `var` keyword |
| **Git & GitHub** | Keep track of changes; Git model feature; Review proposed changes; Transfer + merge; `git-http-backend` | VCS; **Source code tracking**; **Pull request**; `git pull`; **Repository administrator** |
| **React & Redux** | UI library language; Class creation lifecycle; Where to call Hooks; Why Redux; Redux update elements | **JavaScript**; `constructor` $\rightarrow$ `getDerivedStateFromProps` $\rightarrow$ `render` $\rightarrow$ `componentDidMount`; **Top level**; Optimize large apps; **Actions + Reducer + Center Store** |
| **Node.js & Express** | `require()` return value; Promise definition; Express middleware types; Routing & debugging framework | Object representing module instance; Object returned by async method; **Application-level, Router-level, Error-handling** (+ Built-in, Third-party); **Express** |
| **Python & BS4** | Negative/positive list index; `if/else` branching; `open('a+')`; `soup.prettify()` | `myList[2]` = `myList[-2]` (phần tử thứ 3 trong mảng 4 phần tử); Appending & reading (tạo mới nếu chưa có); In cấu trúc lồng nhau (*nested data structure*) |
| **SQL & Django** | Movie in ER model; Cursor; Django template content; Django project; Bootstrap fluid container | **Entity**; Control structure for iterating rows; **Static HTML elements** (+ Python code); Python package containing settings; Spans entire width of parent |
| **Docker & K8s** | Create image vs run container; Dockerfile; Orchestration functions; `kubectl apply`; OpenShift | `docker build` & `docker run`; Text file instructions; Scale + Health checks + Redundancy; File/dir + Infers new deployment + Declarative; Hybrid-cloud enterprise K8s platform |
| **Microservices & Serverless** | 12-Factor App companion; Google API Gateway; Serverless 3 components; IBM Cloud Code Engine | **Microservices**; **Apigee**; **FaaS + BaaS + API Gateway**; **Handles cluster management** |

## 3. Thực hành Giải nhanh các Dạng câu hỏi Đọc Code & CLI

### Dạng 1: Python Indexing, Branching & OOP

```python
# Mẫu 1: List indexing hai chiều
myList = ["John", "Ralph", "Leia", "Simone"]
# Chỉ số dương:   0        1       2        3
# Chỉ số âm:     -4       -3      -2       -1
assert myList[2] == "Leia" and myList[-2] == "Leia"

# Mẫu 2: Câu lệnh điều kiện rẽ nhánh
def check_branch(x):
    if x == "B":
        print("Hello")
    else:
        print("Bye")
    print("Hillary")

# Để in ra "Bye\nHillary", điều kiện (x == "B") PHẢI sai:
# -> x = "C" hoặc x = "Bye" đều cho output "Bye\nHillary".
# Cẩn thận bẫy: `x == "B"` là biểu thức so sánh, không phải phép gán!
```

### Dạng 2: JavaScript, React & Docker/Kubernetes CLI

```bash
# 1. Docker workflow chuẩn trong đề thi:
docker build -t myapp:1.0 .   # Tạo container image từ Dockerfile
docker run -d -p 8080:8080 myapp:1.0  # Tạo và chạy container từ image

# 2. Kubernetes declarative deployment:
kubectl apply -f deployment.yaml
# Đặc điểm cần nhớ:
# - Là lệnh declarative (khai báo trạng thái mong muốn)
# - Yêu cầu truyền file hoặc thư mục chứa manifest (-f)
# - Tự suy luận tạo Deployment mới nếu chưa tồn tại (không giới hạn chỉ namespace-scoped)
```

## 4. Định hướng Nghề nghiệp & Bước tiếp theo sau Chứng chỉ

Sau khi vượt qua bài thi *Final Assessment*, tài liệu định hướng của chương trình khuyến nghị 3 bước hoàn thiện năng lực nghề nghiệp:
1. **Chuẩn bị hồ sơ & Phỏng vấn kỹ thuật:** Rút trích dự án Capstone và các bài lab (Portfolio, React/Redux, Node/Express, Django, Containerized Microservices) thành portfolio rõ ràng kèm README, kiến trúc hệ thống và demo chạy được.
2. **Mở rộng chuyên sâu DevOps & Cloud:** Có thể học tiếp lộ trình *IBM DevOps and Software Engineering* để đào sâu CI/CD pipelines, Infrastructure as Code và quan sát hệ thống (*observability*).
3. **Phát triển kỹ năng mềm (*Soft Skills*):** Luyện kỹ năng thuyết trình kỹ thuật, làm việc nhóm đa vai trò (*Developer – Integrator – Ops*), giao tiếp yêu cầu khách hàng và giải quyết sự cố có hệ thống.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Mất điểm đáng tiếc ở câu `multiple_select` vì chọn thiếu 1 ý:** Trong bài thi Coursera, câu nhiều lựa chọn thường chấm từng checkbox hoặc yêu cầu đúng tuyệt đối. Ví dụ câu hỏi về **Redux elements** chỉ cần chọn đủ 3 thành phần (`Actions`, `Reducer`, `Center store`) và loại `UI components`; câu **Middleware** chọn `Error handling`, `Application level`, `Router level` và loại `Branching`.
2. **Đọc nhầm dấu `==` và `=` trong câu hỏi Python:** Khi đề hỏi giá trị khởi tạo `x` để chạy nhánh `else`, lựa chọn `x=="B"` là sai cú pháp gán (đó là phép so sánh), phải chọn phép gán `x="C"` hoặc `x="Bye"`.
3. **Nhầm `Component` của Bootstrap với `Container`:** Bootstrap có 2 loại container (`.container` có chiều rộng cố định theo breakpoint và `.container-fluid` rộng 100% phần tử cha), đừng nhầm với bảng hay card-grid.
4. **Nhầm tên API Gateway của các hãng Cloud:** **Apigee** thuộc Google; *Azure API Management* thuộc Microsoft; *Gloo* và *Apache APISIX* là giải pháp độc lập/open-source.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- Kỳ thi gồm **45 câu / 135 phút**, cần **$\ge 70\%$ (32 câu)** để đạt chứng chỉ *IBM Full Stack Software Developer Professional Certificate*.
- Luôn kiểm tra kỹ các câu **Select two / Select all that apply**: đối chiếu từng phương án với định nghĩa chuẩn trong giáo trình (NIST Cloud, Redux 3 thành phần, Express 5 middleware, Orchestration, Serverless Stack).
- Nắm chắc cặp lệnh/khái niệm đối lập: `docker build` vs `docker run`, `git fetch` vs `git pull`, `require()` vs `import`, `Private` vs `Public` vs `Hybrid` cloud, `Block` vs `Object` vs `File` storage.