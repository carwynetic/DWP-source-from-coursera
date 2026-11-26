# Module 4: Final Project — Online Book Review Application

> **Tư tưởng cốt lõi:** Dự án cuối khóa tích hợp toàn bộ kiến thức Node.js & Express để xây dựng **Online Book Review RESTful API** cho phép người dùng công khai tra cứu sách/đánh giá, người dùng đã đăng ký thực hiện CRUD đánh giá sách được bảo vệ bởi **Session + JWT Middleware**, và phía client Node.js dùng **Axios với Promises / `async-await`** để phục vụ đồng thời nhiều người dùng.

## 1. Kiến trúc tổng thể & Yêu cầu nghiệp vụ

Trong kịch bản dự án, bạn đóng vai Back-end Developer xây dựng máy chủ RESTful Web Service (fork từ repo khung `ibm-developer-skills-network/expressBookReview`) phục vụ ứng dụng bán sách trực tuyến với hai nhóm quyền truy cập:

| Nhóm người dùng | Quyền hạn & Chức năng bắt buộc | Cơ chế bảo vệ |
| --- | --- | --- |
| **General Users (Khách / Công khai)** | Xem toàn bộ danh sách sách; tìm sách theo **ISBN**, **Author**, **Title**; xem đánh giá (`reviews`) của sách; đăng ký tài khoản (`/register`) & đăng nhập (`/customer/login`) | Công khai (`public_users`), không yêu cầu token |
| **Registered Users (Đã đăng nhập)** | Thêm mới hoặc chỉnh sửa đánh giá sách (`PUT`), xóa đánh giá sách (`DELETE`) — **chỉ được sửa/xóa review của chính mình** | Bảo vệ qua **Session + JWT (`jsonwebtoken.verify`)** trên tiền tố `/customer/auth/*` |

Yêu cầu phi chức năng quan trọng: nhiều người dùng phải truy cập đồng thời mà không chặn lẫn nhau; phần client tích hợp (`general.js`) phải dùng **Promises** hoặc **`async/await`** kết hợp **Axios**.

## 2. Bản đồ Endpoints & Tiêu chí chấm điểm (Tasks 1–11)

| Task | Nhóm | Endpoint / Nhiệm vụ | Mục tiêu kiểm thử (cURL / GitHub) | Điểm |
| --- | --- | --- | --- | --- |
| **Task 1** | General | `GET /` | Lấy danh sách toàn bộ sách trong cửa hàng (`getallbooks`) | 2 |
| **Task 2** | General | `GET /isbn/:isbn` | Tìm chi tiết sách theo mã ISBN (`getbooksbyISBN`) | 2 |
| **Task 3** | General | `GET /author/:author` | Tìm các sách theo tên tác giả (`getbooksbyauthor`) | 2 |
| **Task 4** | General | `GET /title/:title` | Tìm các sách theo tiêu đề (`getbooksbytitle`) | 2 |
| **Task 5** | General | `GET /review/:isbn` | Lấy các đánh giá/bình luận của sách theo ISBN (`getbookreview`) | 2 |
| **Task 6** | General | `POST /register` | Đăng ký người dùng mới (`username`, `password`) (`register`) | 3 |
| **Task 7** | General | `POST /customer/login` | Đăng nhập, tạo Session + cấp JWT (`login`) | 3 |
| **Task 8** | Registered | `PUT /customer/auth/review/:isbn` | Thêm mới hoặc cập nhật review của user đang đăng nhập (`reviewadded`) | 2 |
| **Task 9** | Registered | `DELETE /customer/auth/review/:isbn` | Xóa review thuộc về chính user đang đăng nhập (`deletereview`) | 2 |
| **Task 10** | Node Client | `general.js` (4 phương thức) | Gọi 4 API đọc sách (All, ISBN, Author, Title) bằng **Axios + Promises / async-await** | 8 |
| **Task 11** | GitHub | Forked repository | Xác nhận repo được fork từ `ibm-developer-skills-network/expressBookReview` (`githubrepo`) | 2 |

## 3. Thiết kế bảo mật kết hợp Session + JWT Middleware

Điểm đặc sắc của bài toán này là kết hợp **Express Session** (lưu `accessToken` trong phiên làm việc) với **JWT** (xác thực tính toàn vẹn và danh tính `req.user`):

```javascript
// index.js — Cấu hình session & auth middleware cho /customer/auth/*
const express = require("express");
const jwt = require("jsonwebtoken");
const session = require("express-session");
const customer_routes = require("./router/auth_users.js").authenticated;
const genl_routes = require("./router/general.js").general;

const app = express();
app.use(express.json());

app.use("/customer", session({
  secret: "fingerprint_customer",
  resave: true,
  saveUninitialized: true
}));

// Middleware bảo vệ mọi route chỉnh sửa/xóa review
app.use("/customer/auth/*", function auth(req, res, next) {
  if (req.session.authorization) {
    const token = req.session.authorization["accessToken"];
    jwt.verify(token, "access", (err, user) => {
      if (!err) {
        req.user = user; // Gắn payload đã giải mã để route con kiểm tra quyền sở hữu
        next();
      } else {
        return res.status(403).json({ message: "User not authenticated" });
      }
    });
  } else {
    return res.status(403).json({ message: "User not logged in" });
  }
});

app.use("/customer", customer_routes);
app.use("/", genl_routes);
```

### Logic phân quyền Review ở `auth_users.js`

```javascript
// Đăng nhập: xác thực user -> ký JWT -> lưu vào req.session.authorization
regd_users.post("/login", (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ message: "Error logging in" });
  }
  if (authenticatedUser(username, password)) {
    const accessToken = jwt.sign({ data: password }, "access", { expiresIn: 60 * 60 });
    req.session.authorization = { accessToken, username };
    return res.status(200).send("User successfully logged in");
  }
  return res.status(401).json({ message: "Invalid Login. Check username and password" });
});

// Task 8: Thêm hoặc sửa review theo đúng username trong session
regd_users.put("/auth/review/:isbn", (req, res) => {
  const isbn = req.params.isbn;
  const review = req.query.review; // hoặc req.body.review tùy đề bài lab
  const username = req.session.authorization.username;

  if (!books[isbn]) return res.status(404).json({ message: "Book not found" });
  books[isbn].reviews[username] = review; // Tự động ghi đè nếu user đã review, tạo mới nếu chưa
  return res.status(200).json({ message: "Review added/updated", reviews: books[isbn].reviews });
});

// Task 9: Chỉ xóa đúng key username của người đang đăng nhập
regd_users.delete("/auth/review/:isbn", (req, res) => {
  const isbn = req.params.isbn;
  const username = req.session.authorization.username;

  if (books[isbn] && books[isbn].reviews[username]) {
    delete books[isbn].reviews[username];
    return res.status(200).json({ message: `Review by ${username} deleted` });
  }
  return res.status(404).json({ message: "Review not found for this user" });
});
```

## 4. Triển khai 4 phương thức Bất đồng bộ với Axios (`general.js` — Task 10)

Task 10 chiếm tỷ trọng điểm lớn nhất (8/30 điểm), yêu cầu dùng **Promises** hoặc **`async/await`** với **`axios`** để gọi bất đồng bộ 4 API tra cứu sách:

```javascript
const axios = require("axios");
const BASE_URL = "http://localhost:5000";

// 1. Lấy tất cả sách bằng async/await
async function getAllBooks() {
  try {
    const response = await axios.get(`${BASE_URL}/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching all books:", error.message);
  }
}

// 2. Tìm sách theo ISBN bằng Promise (.then / .catch)
function getBookByISBN(isbn) {
  return axios.get(`${BASE_URL}/isbn/${isbn}`)
    .then((res) => res.data)
    .catch((err) => console.error("ISBN lookup failed:", err.message));
}

// 3. Tìm sách theo Author bằng async/await
async function getBooksByAuthor(author) {
  const response = await axios.get(`${BASE_URL}/author/${encodeURIComponent(author)}`);
  return response.data;
}

// 4. Tìm sách theo Title bằng Promise
function getBooksByTitle(title) {
  return axios.get(`${BASE_URL}/title/${encodeURIComponent(title)}`)
    .then((res) => res.data);
}
```

### Quy trình kiểm thử bằng `cURL` với Session Cookie

Khi test các endpoint cần đăng nhập (`/customer/auth/*`) bằng `cURL`, bắt buộc lưu và gửi lại **cookie phiên (`-c` / `-b`)**, nếu không middleware sẽ báo `"User not logged in"`:

```bash
# Bước 1: Đăng ký & Đăng nhập (lưu session cookie vào cookies.txt)
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"student1","password":"pwd123"}'

curl -c cookies.txt -X POST http://localhost:5000/customer/login \
  -H "Content-Type: application/json" \
  -d '{"username":"student1","password":"pwd123"}'

# Bước 2: Dùng lại cookies.txt để thêm/sửa và xóa review
curl -b cookies.txt -X PUT "http://localhost:5000/customer/auth/review/1?review=Great+book"
curl -b cookies.txt -X DELETE http://localhost:5000/customer/auth/review/1
```

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Quên gửi cookie khi test `PUT`/`DELETE` bằng `cURL`:** Nếu không dùng `-c cookies.txt` lúc login và `-b cookies.txt` lúc gọi `/customer/auth/review/:isbn`, `req.session.authorization` sẽ luôn rỗng.
2. **Cho phép user A xóa/sửa review của user B:** Luôn lấy danh tính từ `req.session.authorization.username` (đã xác thực bởi server), tuyệt đối không tin `username` do client tự truyền lên qua `req.query` hay `req.body`.
3. **Không encode khoảng trắng trong URL khi tìm Author/Title:** Tên tác giả hoặc tiêu đề sách có dấu cách (vd `"Chinua Achebe"`) khi gọi qua `axios.get` cần bọc `encodeURIComponent(...)` để tránh lỗi URL không hợp lệ.
4. **Sửa đổi cấu trúc dữ liệu sách gốc của repo:** Hệ thống chấm điểm AI dùng chính tệp JSON danh sách sách chuẩn trong repo; chỉ giữ thao tác trên bộ nhớ (`books` object) theo đúng contract API.
5. **Viết Task 10 bằng `http.request` đồng bộ hoặc thiếu Axios/Promise:** Đề bài chấm riêng việc dùng **Promise / `async-await` với `axios`** cho cả 4 phương thức tra cứu.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Public endpoints (`/`, `/isbn/:isbn`, `/author/:author`, `/title/:title`, `/review/:isbn`)** cho phép đọc tự do; **Protected endpoints (`/customer/auth/*`)** bắt buộc đi qua middleware xác thực **Session + JWT**.
- Quy trình phát triển chuẩn: Fork repo → `npm install` → Triển khai auth & CRUD → Viết 4 hàm bất đồng bộ với **Axios** trong `general.js` → Test toàn bộ 11 task bằng **cURL/Postman** và lưu output nộp bài.
- Kết hợp **Session + JWT + Non-blocking I/O (Promises/async-await)** giúp server phục vụ nhiều người dùng đồng thời an toàn và mượt mà.
