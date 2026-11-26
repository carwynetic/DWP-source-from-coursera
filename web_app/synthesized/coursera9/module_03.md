# Module 3: Express Web Application Framework

> **Tư tưởng cốt lõi:** Express.js là web framework tối giản và linh hoạt chạy trên nền Node.js giúp trừu tượng hóa chi tiết HTTP cấp thấp thành cơ chế **Routing**, **Middleware pipeline**, **Template Rendering (SSR)** và **REST API** bảo mật bằng Session hoặc **JWT (`jsonwebtoken`)**.

## 1. Mở rộng Node.js & Kiến trúc Web Framework (MVC vs. REST API)

Module `http` lõi của Node.js khá thô sơ: bạn phải tự phân tích URL, body, định tuyến và xử lý XML/JSON thủ công (ví dụ dùng `buffer.match` trên XML rất dễ vỡ khi cấu trúc XML đổi; thay vào đó nên cài gói **`xml2js`** qua NPM để parse XML thành JS object). Vì vậy, lập trình viên dựa vào thư viện bên thứ ba (Lodash, Axios, `xml2js`) và **Node Web Frameworks**:

| Framework | Đặc trưng & Thế mạnh | Phù hợp cho |
| --- | --- | --- |
| **Express.js** | Phổ biến nhất, tối giản, linh hoạt, hệ sinh thái middleware đồ sộ | REST API, microservices, ứng dụng SSR tốc độ phát triển nhanh |
| **Koa** | Nhẹ, hiện đại, hỗ trợ async/await tốt | API gọn nhẹ, hiệu năng cao |
| **Socket.io** *(realtime)* | Giao tiếp hai chiều thời gian thực (server chủ động push data) | Chat, video conference, game nhiều người chơi |
| **Hapi.js** | Tích hợp nhiều plugin bảo mật sẵn, ít phụ thuộc middleware ngoài | Proxy server, API bảo mật cao |
| **NestJS** | Xây trên Express, hỗ trợ **TypeScript**, kiến trúc MVC + OOP/FRP | Hệ thống doanh nghiệp lớn, cần cấu trúc chặt chẽ |

Hai phong cách kiến trúc phổ biến có thể dùng song song trong Express:
- **MVC (Model-View-Controller):** *Model* quản lý dữ liệu & DB; *View* render giao diện từ dữ liệu; *Controller* điều phối luồng xử lý giữa input người dùng và Model.
- **REST API (REpresentational State Transfer):** Giao tiếp **stateless** (mỗi request tự chứa đủ thông tin trạng thái), **cacheable**, dựa trên **tài nguyên (danh từ số ít/số nhiều)** và ánh xạ vào các **HTTP Methods** chuẩn:

| HTTP Method | Mục đích | Idempotent? | HTTP Status Code chuẩn |
| --- | --- | --- | --- |
| `GET` | Đọc biểu diễn tài nguyên (không làm thay đổi dữ liệu) | Có | `200 OK` |
| `POST` | Tạo tài nguyên mới | Không (gọi nhiều lần tạo nhiều bản ghi) | `201 Created` |
| `PUT` | Cập nhật / thay thế toàn bộ tài nguyên | **Có** | `200 OK` hoặc `404 Not Found` |
| `PATCH` | Cập nhật một phần tài nguyên | Tùy triển khai | `200 OK` |
| `DELETE` | Xóa tài nguyên | **Có** | `204 No Content` |

*Quy ước URL RESTful chuẩn:* dùng chữ thường, dấu gạch nối `-` (tránh camelCase hay `_`), không kết thúc bằng `/` thừa, dùng danh từ thay vì động từ (`DELETE /users/123` thay vì `GET /removeUser/123`). Các dải status code: `200–299` (OK), `300–399` (Chuyển hướng), `400–499` (Lỗi phía client), `500–599` (Lỗi phía server).

## 2. Quy trình 5 bước thiết lập Express & Routing

Để xây dựng một ứng dụng Express hoàn chỉnh, bạn đi qua 5 bước chuẩn:
1. Khai báo `express` trong `package.json` (`npm init`).
2. Chạy `npm install` (hoặc `npm install --save express`) để tải module vào `node_modules/`.
3. Import `express` và khởi tạo `const app = express();`.
4. Định nghĩa các route handler (`app.get(path, callback)`, `app.post(...)`) hoặc gắn `express.Router()`.
5. Khởi chạy HTTP server bằng `app.listen(port, callback)`.

```javascript
const express = require("express");
const app = express();

// Built-in middleware: parse JSON body & phục vụ file tĩnh từ thư mục public/
app.use(express.json());
app.use(express.static("public"));

// Route cấp ứng dụng với path parameter (:location_code)
app.get("/temperature/:location_code", (req, res) => {
  const location = req.params.location_code;
  res.status(200).json({ location, status: "ok" });
});

app.listen(3333, () => console.log("Listening at http://localhost:3333"));
```

## 3. Middleware Pipeline & Template Rendering (SSR)

**Middleware** là các hàm trung gian đứng giữa request và response với chữ ký chuẩn `(req, res, next)`. Thứ tự thực thi phụ thuộc **chính xác vào thứ tự gọi `.use()`**. Nếu không gửi response kết thúc, middleware phải gọi `next()` để chuyển tiếp sang tầng kế tiếp.

| Loại Middleware | Cách gắn kết | Mục đích tiêu biểu |
| --- | --- | --- |
| **Application-level** | `app.use(fn)` | Kiểm tra đăng nhập, ghi log thời gian cho **mọi request** vào server |
| **Router-level** | `router.use(fn)` với `express.Router()` | Phân nhánh & áp dụng logic riêng cho từng nhóm route (`/user`, `/item`) |
| **Error-handling** | `app.use((err, req, res, next) => ...)` | **Bắt buộc đủ 4 tham số** `(err, req, res, next)` để xử lý lỗi tập trung |
| **Built-in** | `express.json()`, `express.static("dir")` | Parse JSON payload, trả tài nguyên HTML/CSS/ảnh tĩnh |
| **Third-party** | `npm install <pkg>` rồi `app.use(...)` | `express-session`, `body-parser`, `cors`, `helmet` |

```javascript
const express = require("express");
const app = express();
const userRouter = express.Router();

// Application-level middleware
app.use((req, res, next) => {
  req.timeReceived = new Date().toISOString();
  next();
});

// Router-level middleware chỉ chạy cho nhóm /user/*
userRouter.use((req, res, next) => {
  console.log("User query at:", req.timeReceived);
  next();
});
userRouter.get("/:id", (req, res) => {
  res.send(`User ${req.params.id} logged in at ${req.timeReceived}`);
});
app.use("/user", userRouter);

// Error-handling middleware (luôn đủ 4 tham số và đặt cuối cùng)
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: "Internal Server Error" });
});
```

- **API vs. SSR:** Dùng `res.json(data)` để trả JSON cho SPA/mobile client; dùng `res.render("index", { name: "Alice" })` với view engine (như `express-react-views` dùng tệp `.jsx`) để sinh HTML động từ phía server (Server-Side Rendering).

## 4. Xác thực & Phân quyền: Session, JWT và Passwordless

| Cơ chế | Cách hoạt động | Ưu / Nhược điểm |
| --- | --- | --- |
| **Session-based** (`express-session`) | Server xác thực credential → lưu session ID vào DB/store → gửi session ID về trình duyệt qua **cookie**. Đăng xuất sẽ hủy session ID | Quản lý hủy phiên dễ dàng; nhưng tốn bộ nhớ server và khó scale ngang nhiều server |
| **Token-based (JWT)** (`jsonwebtoken`) | Server cấp **Access Token** gồm 3 phần: **`Header.Payload.Signature`**. Client gửi kèm token (header `Authorization`) ở mỗi request; server dùng **`jwt.verify()`** xác minh chữ ký | **Stateless**, mở rộng đa server dễ dàng, linh hoạt cho microservices; cần secret key mạnh và thời hạn `expiresIn` ngắn |
| **Passwordless** | Không dùng mật khẩu; chứng minh danh tính bằng **biometrics**, **magic link** (qua email khôi phục mật khẩu), hoặc mã OTP, dựa trên cặp **Public Key** (mã hóa challenge) & **Private Key** (giải mã trên thiết bị người dùng) | Trải nghiệm mượt, tránh lộ mật khẩu yếu; phụ thuộc kênh email/SMS hoặc phần cứng thiết bị |

```javascript
const express = require("express");
const jwt = require("jsonwebtoken");
const app = express();
app.use(express.json());

const JWT_SECRET = "aVeryVerySecretString";

// 1. Authentication: cấp JWT khi đăng nhập hợp lệ
app.post("/login", (req, res) => {
  const { username, password } = req.body;
  if (username === "user" && password === "password") {
    const token = jwt.sign({ username }, JWT_SECRET, { expiresIn: "1h" });
    return res.json({ token });
  }
  return res.status(401).json({ message: "Invalid credentials" });
});

// 2. Authorization: xác minh JWT bằng jsonwebtoken.verify()
app.get("/employees", (req, res) => {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1];
  if (!token) return res.status(401).send("Please log in to access this resource");

  jwt.verify(token, JWT_SECRET, (err, decoded) => {
    if (err) return res.status(401).send("Invalid token");
    res.status(200).json({ message: `Access successful for ${decoded.username}` });
  });
});
```

## 5. Tổ chức thư mục & Best Practices cho Express API

Express không ép cấu trúc thư mục, nhưng dự án thực tế nên tách rõ trách nhiệm:
```text
project-root/
├── config/       # db.js (kết nối DB), credentials.js (API keys, biến môi trường)
├── models/       # Schema dữ liệu / ORM (Mongoose, Sequelize...)
├── routes/       # Tách file theo từng tài nguyên (users.js, books.js)
├── views/        # Template SSR (nếu có)
├── public/       # Tài nguyên tĩnh (images, css, js)
├── app.js        # Khởi tạo Express app, gắn middleware & routes
├── routes.js     # Gom và export tập trung toàn bộ routes
└── package.json  # Metadata & dependencies (không bao giờ push node_modules lên Git!)
```

- **Quy ước đặt tên:** Tên file viết thường toàn bộ (`lowercase`); biến & tên module khi `require` dùng `camelCase`; tên package NPM dùng chữ thường nối dấu gạch ngang (`express-session`).
- **Kiểm thử & Tài liệu hóa:** Dùng **Mocha + SuperTest** để thực hiện **black-box testing** cho REST API; tài liệu hóa endpoint bằng **Swagger (OpenAPI)** hoặc **API Blueprint**.

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Thiếu tham số `next` trong Error-handling Middleware:** Nếu viết `(err, req, res)` thay vì đủ 4 tham số `(err, req, res, next)`, Express sẽ nhận nhầm thành middleware thường và không bắt được lỗi.
2. **Đặt middleware sai thứ tự:** Đặt `app.use(express.json())` *sau* định nghĩa route khiến `req.body` bị `undefined` khi `POST`.
3. **Quên gọi `next()` trong middleware không trả response:** Request bị treo vĩnh viễn không bao giờ tới được route handler.
4. **Push `node_modules/` lên Git:** Làm phình repo hàng trăm MB và lỗi tương thích hệ điều hành; luôn đưa `node_modules/` vào `.gitignore` và dùng `npm install --save` để ghi vào `package.json`.
5. **Dùng chuỗi regex/string matching để parse XML phức tạp:** Dễ gãy khi thẻ XML đổi cấu trúc hoặc có dữ liệu lỗi; hãy dùng `xml2js`.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- **Express** cung cấp lớp `app` để ánh xạ HTTP method + URL path (`app.get(path, cb)`) và `app.listen(port)` để mở cổng lắng nghe.
- 5 loại middleware: **Application-level**, **Router-level**, **Error-handling (4 tham số)**, **Built-in**, và **Third-party**.
- **JWT (`jsonwebtoken`)** gồm **Header, Payload, Signature**; dùng `jwt.sign()` khi đăng nhập và `jwt.verify()` để bảo vệ endpoint.
- Kiểm thử hộp đen REST API trong Node.js chuẩn dùng **Mocha/SuperTest**; mở rộng parse XML dùng **`xml2js`**.
