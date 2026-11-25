# Module 3: Back End Services (Express/MongoDB + Django ORM + Flask Sentiment AI)

> **Tư tưởng cốt lõi:** Xây dựng tầng Back-End đa dịch vụ (Polyglot Microservices) thực chiến: **Node.js + Express + MongoDB** phục vụ CRUD đại lý & đánh giá, **Django ORM + SQLite** quản lý danh mục hãng/dòng xe (`CarMake`, `CarModel`), **Flask + NLTK** phân tích cảm xúc bình luận trên **IBM Cloud Code Engine**, và lớp proxy `restapis.py` trong Django kết nối thống nhất toàn bộ dữ liệu cho React Front-End.

## 1. Dịch vụ Express + MongoDB (Dealerships & Reviews Microservice)

Dịch vụ viết bằng Node.js/Express (chạy trong Docker cùng MongoDB qua `docker-compose.yml`) cung cấp các REST endpoints sau:

| Endpoint Express | Chức năng |
| --- | --- |
| `GET /fetchReviews` | Trả về toàn bộ đánh giá trong collection MongoDB |
| `GET /fetchReviews/dealer/:id` | Trả về tất cả đánh giá của một đại lý theo `dealership` ID |
| `GET /fetchDealers` | Trả về danh sách toàn bộ các đại lý xe |
| `GET /fetchDealers/:state` | Lọc danh sách đại lý theo bang (ví dụ `/fetchDealers/Kansas`) |
| `GET /fetchDealer/:id` | Trả về thông tin chi tiết của 1 đại lý theo ID |
| `POST /insert_review` | Tính ID mới (`max + 1`) và chèn bản ghi đánh giá mới vào MongoDB |

## 2. Django ORM Models (`CarMake` & `CarModel`) & Django Admin

Vì danh mục hãng xe và dòng xe tương đối ổn định (ít biến động), chúng được lưu cục bộ trong SQLite qua Django ORM (`djangoapp/models.py`):

```python
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Quan hệ 1-N
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)],
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
```

- Đăng ký cả `CarMake` và `CarModel` trong `djangoapp/admin.py` bằng `admin.site.register(...)` để tạo/chỉnh sửa dữ liệu trực tiếp qua Django Admin, và cung cấp endpoint `get_cars` (tự động chạy `initiate()` nạp dữ liệu mẫu nếu bảng rỗng).

## 3. Lớp Proxy Service (`restapis.py`) & Django Proxy Views (`views.py`)

Thay vì để trình duyệt gọi trực tiếp sang nhiều backend khác nhau (gây lộ URL nội bộ và phức tạp CORS), Django đóng vai trò **Backend-for-Frontend / Proxy Service**:

| Hàm trong `restapis.py` | Mục đích & Dịch vụ đích |
| --- | --- |
| `get_request(endpoint, **kwargs)` | Gửi HTTP `GET` sang `backend_url` (Express/MongoDB) kèm tham số query và trả về JSON |
| `analyze_review_sentiments(text)` | Gửi HTTP `GET` sang `sentiment_analyzer_url` (**Flask + NLTK trên IBM Cloud Code Engine**) để phân loại bình luận thành `positive`, `neutral` hoặc `negative` |
| `post_review(data_dict)` | Gửi HTTP `POST` sang `backend_url + "/insert_review"` để lưu đánh giá mới vào MongoDB |

### Các Django Views & Routes tương ứng (`djangoapp/urls.py`)

| Route Django | View Function | Luồng xử lý chính |
| --- | --- | --- |
| `/djangoapp/get_dealers` & `/djangoapp/get_dealers/<str:state>` | `get_dealerships(request, state="All")` | Gọi `get_request("/fetchDealers")` hoặc `/fetchDealers/{state}` |
| `/djangoapp/dealer/<int:dealer_id>` | `get_dealer_details(request, dealer_id)` | Gọi `get_request(f"/fetchDealer/{dealer_id}")` |
| `/djangoapp/reviews/dealer/<int:dealer_id>` | `get_dealer_reviews(request, dealer_id)` | Lấy danh sách reviews từ Express, sau đó duyệt từng review gọi **`analyze_review_sentiments(review["review"])`** để gắn thêm trường `sentiment` trước khi trả về React |
| `/djangoapp/add_review` | `add_review(request)` | Kiểm tra `if not request.user.is_anonymous:` rồi gọi `post_review(data)` |

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Quên cập nhật biến môi trường `backend_url` và `sentiment_analyzer_url` trong `.env`:** Khi khởi động lại Cloud IDE hoặc deploy lên Code Engine, URL dịch vụ thay đổi — nếu để URL cũ, mọi hàm trong `restapis.py` sẽ báo `ConnectionError`.
2. **Bỏ qua kiểm tra đăng nhập trong `add_review`:** Phải kiểm tra `request.user.is_anonymous == False` phía server (không chỉ ẩn nút ở React) để chặn người dùng ẩn danh gửi `POST` trực tiếp bằng `cURL`.
3. **Không xử lý ký tự đặc biệt trong URL khi gọi Sentiment Analyzer:** Văn bản bình luận chứa khoảng trắng, dấu hỏi `?` hay ký tự đặc biệt nên được URL-encode an toàn trước khi nối vào đường dẫn `analyze/<text>`.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Dữ liệu tĩnh (`CarMake`, `CarModel`) lưu ở **Django ORM (SQLite)**; dữ liệu đại lý & đánh giá lưu ở **MongoDB** qua **Express API**; phân tích sắc thái chạy trên **Flask/NLTK Serverless (Code Engine)**.
- **`restapis.py`** gom 3 hàm cầu nối cốt lõi: `get_request`, `analyze_review_sentiments`, và `post_review`.
- 4 Django proxy views trọng tâm: `get_dealerships`, `get_dealer_details`, `get_dealer_reviews`, `add_review`.
