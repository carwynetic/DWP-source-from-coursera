# Module 2: Web App Deployment using Flask

> **Tư tưởng cốt lõi:** Flask là một **micro-framework** Python gọn nhẹ, linh hoạt và có thể mở rộng (extensible), sử dụng decorator **`@app.route()`** để ánh xạ URL động và các phương thức CRUD, cung cấp hai đối tượng trung tâm **`Request`** và **`Response`** cho mỗi lượt gọi từ client, cùng cơ chế xử lý mã trạng thái HTTP và lỗi tập trung ở cấp ứng dụng.

## 1. Python Libraries vs. Frameworks & So sánh Flask với Django

Trước khi xây dựng web app, cần phân biệt rõ **Library** và **Framework**:
- **Library (Thư viện):** Bộ công cụ giải quyết một tác vụ cụ thể (vd `NumPy` tính toán, `Pandas` xử lý bảng, `Matplotlib` vẽ biểu đồ, `Requests` gửi HTTP request, `BeautifulSoup` cào dữ liệu HTML, `SQLAlchemy` làm ORM, `PyTest` kiểm thử).
- **Framework:** Bộ khung kiến trúc định sẵn luồng điều khiển toàn bộ ứng dụng, tích hợp sẵn công cụ debug, bảo mật, kết nối DB giúp viết ít code hơn (vd `Flask`, `Django`, `Web2Py`).

| Tiêu chí | Flask | Django |
| --- | --- | --- |
| **Phân loại** | **Micro-framework** (gọn nhẹ, tối giản phụ thuộc) | **Full-stack framework** (tích hợp "tất cả trong một") |
| **Triết lý thiết kế** | **Unopinionated / Linh hoạt** — tự do chọn extension dạng plug-and-play | **Opinionated** — định sẵn cấu trúc & quyết định cho lập trình viên |
| **Thành phần lõi mặc định** | Werkzeug (WSGI/server/debugger), Jinja2 (templates), ItsDangerous (ký cookie), Click (CLI) | ORM, Admin UI, Auth, Forms, Template... tích hợp sẵn |
| **Mở rộng phổ biến** | `Flask-SQLAlchemy`, cộng đồng extensions | Hệ sinh thái tích hợp chặt theo chuẩn Django |

## 2. Khởi tạo, Cấu hình & Triển khai ứng dụng Flask cơ bản

Cài đặt bằng `pip install flask` (Flask 2.2.2 yêu cầu Python >= 3.7). Chu trình tối thiểu gồm 3 bước: **Import `Flask` → Khởi tạo `app = Flask(__name__)` → Chạy app** (mặc định trên cổng **5000** với development server Werkzeug).

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Cấu hình trực tiếp qua app.config (hoặc load từ biến môi trường / file JSON via from_file)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "change-this-secret"

# Mặc định @app.route("/") chỉ chấp nhận phương thức GET
@app.route("/")
def hello_world():
    return "<b>My first Flask application in action!</b>"

@app.route("/api/status")
def status():
    return jsonify({"status": "ok"})  # Tự động trả Content-Type: application/json & code 200
```

Chạy server từ terminal bằng **Click CLI**:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development   # Lưu ý: deprecated từ Flask 2.3 (dùng flask --app app run --debug)
flask run                      # Lắng nghe tại http://localhost:5000
```

Các khóa cấu hình quan trọng trong `app.config`: `DEBUG`, `TESTING`, `SECRET_KEY` (ký session cookie bằng ItsDangerous), `SESSION_COOKIE_NAME`, `SERVER_NAME`, và cấu hình JSON. Khi app lớn dần, nên tách thư mục: module mã nguồn chính, tệp cấu hình riêng, `static/` (CSS, JS, ảnh), `templates/` (HTML động Jinja2), `tests/` và virtual environment.

## 3. Routing, CRUD Methods & Dynamic Routes cho RESTful API

Decorator `@app.route(path, methods=[...])` tạo **URL handler**:
- Nếu **không khai báo `methods`**, Flask **mặc định chỉ nhận `GET`**.
- Mapping chuẩn với CRUD: **`POST`** (tạo mới / gửi dữ liệu HTML form), **`GET`** (đọc dữ liệu), **`PUT` / `PATCH`** (cập nhật dữ liệu/database hiện có), **`DELETE`** (xóa dữ liệu).

**Dynamic Routes** cho phép truyền tham số trực tiếp qua URL kèm ép kiểu (`string`, `int`, `float`, `path`, `uuid`) để xây dựng RESTful endpoint hoặc gọi tiếp API ngoài bằng `requests`:

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET", "POST"])
def health():
    return jsonify({"status": "OK", "method": request.method})

# Dynamic route ép kiểu int & gọi OpenLibrary API
@app.route("/book/<int:isbn>")
def get_book_by_isbn(isbn):
    res = requests.get(f"https://openlibrary.org/isbn/{isbn}.json", timeout=5)
    if res.status_code == 200:
        return jsonify(res.json()), 200
    if res.status_code == 404:
        return jsonify({"message": "Something went wrong"}), 404
    return jsonify({"message": "Server error"}), 500

# Dynamic route hỗ trợ kiểu uuid
@app.route("/network/<uuid:net_id>")
def get_network(net_id):
    return jsonify({"network_id": str(net_id)}), 200
```

## 4. Hai đối tượng trung tâm: `Request` và `Response`

Mỗi khi client gửi HTTP request, Flask cung cấp đối tượng **`request`** (từ `flask.Request`) và tạo đối tượng **`response`** trả về client:

| Thuộc tính / Phương thức `request` | Ý nghĩa thực chiến |
| --- | --- |
| `request.method` / `request.is_json` | Kiểm tra HTTP verb (`POST`, `GET`) và payload có phải JSON hay không |
| `request.args.get("q")` | Lấy query parameter an toàn (tránh `KeyError` nếu thiếu như `request.args["q"]`) |
| `request.access_route` | Danh sách **tất cả địa chỉ IP** đã chuyển tiếp request (rất quan trọng khi qua proxy/audit) |
| `request.full_path` / `request.is_secure` | Đường dẫn đầy đủ kèm query string / kiểm tra HTTPS hoặc WSS |
| `request.headers` / `request.cookies` | Đọc `User-Agent`, `Accept`, `Host`, `Cache-Control`, cookies |

| Thuộc tính / Hàm `Response` | Ý nghĩa thực chiến |
| --- | --- |
| `status_code` | Mã trạng thái HTTP 3 chữ số |
| `content_type` / `mime_type` / `content_length` | Loại dữ liệu & **kích thước phần thân (bytes)** của response gửi về client |
| `set_cookie()` / `delete_cookie()` | Gắn hoặc xóa cookie trên trình duyệt |
| `make_response()` / `jsonify()` | Chủ động tùy chỉnh response (header, status code) |
| `redirect(url)` / `abort(code)` | Chuyển hướng (`302`) hoặc ngắt ngay với mã lỗi HTTP |

## 5. HTTP Status Codes & Xử lý lỗi cấp ứng dụng

Mọi HTTP response đều mang **mã trạng thái gồm 3 chữ số** từ `100` đến `599`:
- `1xx`: Thông tin đã nhận request.
- `2xx`: Thành công — **`200 OK`** (mặc định khi `return` hoặc `jsonify`), **`201 Created`**, **`202 Accepted`** (batch processing), **`204 No Content`** (thành công nhưng không trả nội dung, giữ nguyên trang).
- `3xx`: Chuyển hướng (vd `302`).
- `4xx`: Lỗi phía Client — **`400 Bad Request`** (thiếu/sai tham số), **`401 Unauthorized`** (thiếu/sai thông tin xác thực), **`403 Forbidden`** (không đủ quyền), **`404 Not Found`**, **`405 Method Not Allowed`**, **`422 Unprocessable Entity`** (thiếu input hợp lệ như thiếu tham số `q`).
- `5xx`: Lỗi phía Server — **`500 Internal Server Error`**.

```python
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

# Trả về status code tường minh bằng tuple hoặc make_response()
@app.route("/search")
def search():
    q = request.args.get("q")
    if not q:
        return jsonify({"error": "input parameter missing"}), 422
    # Giả lập tìm DB
    item = None
    if item is None:
        return make_response(jsonify({"error": "resource not found"}), 404)
    return jsonify(item), 200

# Application-level error handlers cho toàn bộ ứng dụng
@app.errorhandler(404)
def api_not_found(error):
    return jsonify({"message": "API not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"message": "Something went wrong on the server"}), 500
```

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Gửi `POST` vào route không khai báo `methods`:** Mặc định `@app.route('/path')` chỉ nhận `GET`; gửi `POST` sẽ bị Flask từ chối với lỗi **`405 Method Not Allowed`**.
2. **Dùng `request.args["key"]` thay vì `request.args.get("key")`:** Nếu client quên truyền query param, truy cập kiểu dictionary sẽ ném `BadRequestKeyError` (400) hoặc làm sập logic nếu không bắt lỗi.
3. **Kiểm tra IP client sau Reverse Proxy bằng `request.remote_addr`:** Khi app đứng sau Nginx/Load Balancer, `remote_addr` chỉ là IP của proxy; cần dùng **`request.access_route`** để thu thập toàn bộ chuỗi IP chuyển tiếp.
4. **Quên trả về mã lỗi khi gọi API bên ngoài thất bại:** Khi `requests.get(...)` trả 404/500 mà không kiểm tra `res.status_code == 200`, server Flask sẽ mặc định trả 200 OK kèm dữ liệu lỗi cho client.
5. **Dùng `FLASK_ENV=development` trên Flask >= 2.3:** Biến môi trường này đã bị loại bỏ từ Flask 2.3; thay bằng cờ `--debug` khi chạy `flask run --debug`.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Flask** là micro-framework nhẹ (khác với full-stack **Django**), cung cấp sẵn server dev, debugger, routing, Jinja2 template, error handling và dễ mở rộng.
- `@app.route()` tạo **URL handler** (mặc định chỉ `GET`), hỗ trợ dynamic routes (`<int:...>`, `<uuid:...>`) cho **RESTful endpoints**.
- Hai đối tượng cốt lõi cho mỗi request là **`Request`** (headers, `args`, `is_json`, `access_route`) và **`Response`** (`status_code`, `content_length`, `content_type`, `set_cookie`).
- Flask mặc định trả mã **`200`** nếu không chỉ định; dùng tuple `(body, code)`, `make_response()`, và `@app.errorhandler()` để kiểm soát chuẩn mã HTTP 3 chữ số.
