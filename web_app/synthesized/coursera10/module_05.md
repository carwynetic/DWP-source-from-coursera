# Module 5: APIs and Data Collection

> **Tư tưởng cốt lõi:** Thu thập dữ liệu hiện đại trong Python dựa trên ba trụ cột: giao tiếp với dịch vụ web qua **REST API & giao thức HTTP** (`requests`, `GET/POST`, JSON), trích xuất dữ liệu phi cấu trúc từ trang web qua **Web Scraping** (`BeautifulSoup` duyệt cây HTML DOM hoặc `pd.read_html` đọc bảng), và chuẩn hóa nhiều định dạng tệp khác nhau (`CSV`, `JSON`, `XML`, `XLSX`) về DataFrame phân tích.

## 1. APIs & REST APIs — Cơ chế giao tiếp Client–Server

- **API (Application Programming Interface):** Tập quy tắc cho phép hai phần mềm trao đổi dữ liệu qua đầu vào (input) và đầu ra (output) mà không cần biết chi tiết cài đặt bên trong (ví dụ: Pandas là API kết nối Python với thư viện C bên dưới; `pycoingecko` là client/wrapper bọc CoinGecko API).
- **REST API (Representational State Transfer):** Giao tiếp qua Internet thông qua giao thức **HTTP**. Chương trình Python của bạn là **Client**, dịch vụ web là **Resource** được định danh qua **Endpoint (URL)**, và dữ liệu trao đổi phổ biến nhất nằm dưới dạng **JSON** (ánh xạ trực tiếp sang `dict`/`list` trong Python).

### Cấu trúc URL & Thông điệp HTTP

Một URL chuẩn `http://www.ibm.com/images/IDSNlogo.png` gồm 3 thành phần:
1. **Scheme (Giao thức):** `http://` (hoặc `https://`).
2. **Internet Address / Base URL:** `www.ibm.com`.
3. **Route (Đường dẫn tài nguyên trên server):** `/images/IDSNlogo.png`.

**Thông điệp HTTP Request & Response** gồm 3 phần:
- **Start / Status line:** Request có method + path (`GET /index.html HTTP/1.0`); Response có version + **status code** + cụm mô tả (`HTTP/1.0 200 OK`).
  - Mã trạng thái: `1xx` (Informational), `2xx` (Success — `200 OK`), `4xx` (Client Error — `401 Unauthorized`, `404 Not Found`), `5xx` (Server Error — `501 Not Implemented`).
- **Headers:** Metadata bổ sung (như `Content-Type`, `Date`, `Authorization: Bearer TOKEN`).
- **Body:** Nội dung truyền tải (HTML, JSON, ảnh...; `GET` thường không có request body).

| HTTP Method | Mục đích chính | Vị trí gửi tham số / dữ liệu | Thao tác `requests` trong Python |
| --- | --- | --- | --- |
| **`GET`** | Lấy/đọc dữ liệu từ server | Qua URL **Query String** (`?name=Joseph&ID=123`) | `requests.get(url, params=payload)` |
| **`POST`** | Gửi dữ liệu mới (tạo tài nguyên / form nhạy cảm) | Nằm trong **Request Body** (không lộ trên URL!) | `requests.post(url, data=payload)` |
| **`PUT`** | Cập nhật tài nguyên đã có trên server | Request Body | `requests.put(url, data=payload)` |
| **`DELETE`** | Xóa tài nguyên chỉ định trên server | URL / Body | `requests.delete(url)` |

```python
import requests

# GET với Query Parameters (tạo URL .../get?name=John&ID=123, r.request.body là None)
payload = {"name": "John", "ID": "123"}
r_get = requests.get("https://httpbin.org/get", params=payload)
print(r_get.status_code)          # 200
print(r_get.headers["Content-Type"])
data = r_get.json()               # Parse JSON thành Python dict -> data["args"]

# POST gửi dữ liệu nhạy cảm qua Request Body (không xuất hiện trên URL)
r_post = requests.post("https://httpbin.org/post", data=payload)
print(r_post.json()["form"])      # {'ID': '123', 'name': 'John'}
```

### Ví dụ Time Series từ API (CoinGecko + Pandas + Plotly)

Khi nhận chuỗi thời gian chứa **UNIX timestamp** (mili-giây kể từ `1970-01-01 00:00:00 UTC`), dùng `pd.to_datetime(df['TimeStamp'], unit='ms')` để chuyển sang ngày giờ đọc được, sau đó `groupby` theo ngày lấy `min`, `max`, `first`, `last` để vẽ **Candlestick chart** bằng Plotly.

## 2. Cấu trúc HTML & Web Scraping với BeautifulSoup

**Web Scraping** là quá trình tự động tải và trích xuất dữ liệu từ trang web (thường qua `requests.get()` rồi phân tích HTML).

- **Cây tài liệu HTML (Document Tree / DOM):**
  - `<html>` là thẻ gốc chứa hai thẻ con (children) ngang hàng (siblings) là `<head>` (metadata) và `<body>` (nội dung hiển thị).
  - Mỗi thẻ HTML gồm thẻ mở, thuộc tính (`href="..."` trong `<a>`), nội dung (`NavigableString`) và thẻ đóng (`</a>`).
  - **HTML Table:** `<table>` chứa các hàng `<tr>`, ô tiêu đề `<th>` và ô dữ liệu `<td>` (table cell data).
- **So sánh nhanh công cụ Scraping:** `BeautifulSoup` (phân tích cây HTML/XML linh hoạt mọi thẻ), `Scrapy` (framework crawl quy mô lớn), `Selenium` (điều khiển trình duyệt thật cho trang chạy JavaScript động), `pd.read_html(url)` (trích xuất trực tiếp các thẻ `<table>` thành danh sách DataFrame).

```python
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/IBM"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")  # Bước 1: Tạo parse tree

# Điều hướng cây DOM & lọc phần tử
title_tag = soup.title            # Truy cập thẻ đầu tiên khớp tên
parent_tag = title_tag.parent     # Đi ngược lên thẻ cha (<head>)
next_sib = title_tag.find_next_sibling()

# Tìm tất cả thẻ <a> hoặc theo CSS selector / thuộc tính
links = soup.find_all("a")        # Trả về list các Tag objects
first_btn = soup.find("a", {"class": "link"})
headings = soup.select("h1")

# Đọc bảng HTML từ BeautifulSoup hoặc Pandas
for row in soup.find("table").find_all("tr"):
    cells = [td.text.strip() for td in row.find_all("td")]

import pandas as pd
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_largest_banks")
df_banks = tables[0]              # Chọn bảng đầu tiên dưới dạng DataFrame
```

## 3. Làm việc với nhiều định dạng tệp (CSV, JSON, XML, XLSX)

| Định dạng | Đặc điểm | Cách đọc chuẩn trong Python |
| --- | --- | --- |
| **CSV** (`.csv`) | Comma-Separated Values — văn bản bảng ngăn cách bởi dấu phẩy | `df = pd.read_csv("data.csv")` (gán `df.columns = [...]` nếu file thiếu header) |
| **JSON** (`.json`) | JavaScript Object Notation — cấu trúc `key: value` giống `dict` Python | `import json; data = json.load(open("file.json"))` hoặc `response.json()` |
| **XML** (`.xml`) | Extensible Markup Language — dữ liệu phân cấp theo thẻ tùy biến | `import xml.etree.ElementTree as ET; tree = ET.parse("file.xml")` (Pandas cổ điển không tự đọc trực tiếp như CSV) |
| **Excel** (`.xlsx`) | Bảng tính nhiều sheet, công thức | `df = pd.read_excel("file.xlsx")` |
| **Media / Binary** | Ảnh `.png`, âm thanh `.wav/.mp3` | Mở bằng mode `'rb'` (read binary) |

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm `scheme` với toàn bộ URL:** Trong `http://www.ibm.com/images/IDSNlogo.png`, **scheme** chỉ là `http://`, còn `www.ibm.com` là base URL/host và `/images/IDSNlogo.png` là route.
2. **Dùng `GET` cho form nhạy cảm (mật khẩu, thông tin cá nhân):** `GET` gắn tham số thẳng lên URL (lộ trong lịch sử trình duyệt và server logs); dữ liệu nhạy cảm bắt buộc phải gửi qua **`POST`** để nằm trong request body.
3. **Truyền sai tham số `params` vs `data` trong `requests`:** `requests.get(url, params=payload)` gắn vào query string; `requests.post(url, data=payload)` đưa vào form body; `json=payload` gửi JSON body kèm header `application/json`.
4. **Tin tưởng mù quáng `pd.read_html()`:** Một số trang web dùng `<table>` để dàn trang hình ảnh hoặc nhúng nhiều chú thích/hyperlink trong ô, khiến bảng trích xuất bị lệch chỉ số (`tables[2]` thay vì `tables[0]`) và cần làm sạch thêm bằng `BeautifulSoup` hoặc Pandas.
5. **Đạo đức & Pháp lý Web Scraping:** Luôn kiểm tra tệp `robots.txt` và điều khoản sử dụng (Terms of Use) của website trước khi crawl tự động với tần suất cao.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- **API** kết nối phần mềm với phần mềm; **REST API** chạy trên **HTTP** (`GET`, `POST`, `PUT`, `DELETE`) và trao đổi phổ biến bằng **JSON**.
- **URL** = `scheme` (`http://`) + `base URL` + `route`; **HTTP Response** = `status line` (`200 OK`) + `headers` + `body`.
- **BeautifulSoup** chuyển HTML thành cây đối tượng DOM để duyệt (`parent`, `find_next_sibling`) và tìm kiếm (`find`, `find_all`, `select`), trong đó `<table>`, `<tr>`, `<th>`, `<td>` biểu diễn bảng dữ liệu.
- Thành thạo nạp dữ liệu đa định dạng: `pd.read_csv()`, `pd.read_excel()`, `pd.read_html()`, `json.load()` / `r.json()`, và `xml.etree.ElementTree`.
