# Module 1: Introduction to Server-Side JavaScript

> **Tư tưởng cốt lõi:** Node.js là môi trường thực thi (runtime environment) mã nguồn mở chạy JavaScript phía server dựa trên Google V8 engine theo kiến trúc single-threaded, event-driven và non-blocking I/O; mã nguồn được tổ chức thành các module (CommonJS với `require()` hoặc ES Modules với `import`) và quản lý phụ thuộc tập trung qua NPM (`package.json`).

## 1. Kiến trúc Client-Server & Vai trò Back-end Development

Trong ứng dụng web/cloud hiện đại, hệ thống được chia thành **Front-end (client-side)** chạy trên trình duyệt (HTML, CSS, JavaScript, React/Angular/Vue) và **Back-end (server-side)** chạy trên máy chủ để xử lý logic nghiệp vụ, bảo mật, xác thực và truy xuất dữ liệu.

| Thành phần Back-end | Chức năng chính | Công nghệ / Ví dụ tiêu biểu |
| --- | --- | --- |
| **Web Server (HTTP Server)** | Tiếp nhận HTTP request từ trình duyệt, kiểm soát truy cập tệp tĩnh và trả về HTTP response | Nginx, Apache, module `http` của Node.js |
| **Application Server** | Chứa business logic, biến đổi dữ liệu thành nội dung động, điều phối API | Node.js + Express, Django, Ruby on Rails, Spring |
| **Database Server** | Lưu trữ, truy vấn và cập nhật dữ liệu có cấu trúc (SQL) hoặc phi cấu trúc (NoSQL) | MySQL, PostgreSQL, SQLite, MongoDB, Redis |
| **Web Service / Web API** | Giao diện chuẩn cho phép front-end và các server giao tiếp qua HTTP (thường dùng JSON payload) | REST API, GraphQL |

Ba trách nhiệm sống còn của kỹ sư Back-end gồm:
- **Scalability (Khả năng mở rộng):** Ứng dụng tự động thích ứng khi **load** (số người dùng đồng thời, số giao dịch, lưu lượng dữ liệu) tăng hoặc giảm mà không sụt hiệu năng.
- **Security & Authentication:** Bảo vệ dữ liệu nhạy cảm, xác thực danh tính và ngăn chặn tấn công.
- **Performance:** Tối ưu tốc độ truy xuất dữ liệu giữa các máy chủ và phản hồi kịp thời cho client.

## 2. Bản chất của Node.js Runtime & V8 Engine

Khác với hiểu lầm phổ biến, **Node.js không phải là ngôn ngữ lập trình hay web framework**, mà là một **runtime environment** đa nền tảng (Linux, Windows, macOS) giúp thực thi JavaScript bên ngoài trình duyệt.

- **Ngôn ngữ thông dịch (Interpreted):** JavaScript không cần biên dịch trước sang mã máy trước khi chạy; Google **V8 Engine** (viết bằng C++, dùng trong Chrome và Edge) biên dịch và thực thi trực tiếp mã JS với hiệu năng cao.
- **Event-Driven, Single-Threaded, Non-Blocking I/O:** Thay vì tạo một luồng (thread) riêng cho mỗi kết nối như mô hình truyền thống, Node.js chạy trên **một luồng chính (single thread)** kết hợp Event Loop. Khi gặp tác vụ I/O (đọc file, gọi DB, request mạng), Node.js không đứng chờ (non-blocking) mà đăng ký một **callback function** và tiếp tục phục vụ request khác; khi I/O hoàn tất, sự kiện (event) được kích hoạt để gọi callback xử lý kết quả.
- **JSON Native:** Vì JSON (JavaScript Object Notation) biểu diễn dữ liệu dạng cặp `key-value` tương thích tự nhiên với object trong JavaScript, việc parse/trả payload JSON trong Node.js diễn ra cực nhanh — rất phù hợp cho microservices, chat, gaming thời gian thực.

### Luồng xử lý REST Request điển hình với Node.js

```
[Browser: HTML/CSS + JS] --(1. User action & validation)-->
[HTTP Request + JSON Payload] --(2. Gọi API)-->
[Node.js Server / REST Web Service] --(3. Xử lý logic & DB)-->
[HTTP Response + JSON Payload] --(4. Trả kết quả về Client)
```

## 3. Hệ thống Module: CommonJS (`require`) vs. ES Modules (`import`)

Một **module** là tệp `.js` chứa các hàm/biến đóng gói phục vụ một mục đích cụ thể; một **package** là thư mục gom một hoặc nhiều module kèm tệp mô tả `package.json`. Node.js hỗ trợ hai chuẩn đặc tả module chính:

| Tiêu chí | CommonJS (Mặc định của Node.js) | ES Modules (ESM) |
| --- | --- | --- |
| **Cú pháp nhập / xuất** | `require('./file')` và `module.exports` / `exports` | `import { x } from './file.mjs'` và `export { x }` |
| **Phần mở rộng tệp** | `.js` (mặc định) | `.mjs` (hoặc `.js` nếu `"type": "module"` trong `package.json`) |
| **Vị trí gọi lệnh** | Gọi được **bất cứ đâu** trong file (trong `if`, hàm) | Bắt buộc đặt ở **đầu tệp** (top-level), không đặt trong `if` |
| **Cơ chế liên kết (Binding)** | **Dynamic binding** — lỗi liên kết chỉ phát hiện lúc **run-time** | **Static binding** — lỗi phát hiện ngay lúc **compile-time** |
| **Cơ chế tải** | **Synchronous** (đồng bộ, tuần tự từng module) | **Asynchronous** (bất đồng bộ, tối ưu khi tải hàng trăm module) |

```javascript
// === CommonJS: messages.js & app.js ===
// messages.js
module.exports.getDate = function getDate() {
  return new Date().toLocaleString("en-US", { timeZone: "Australia/Brisbane" });
};

// app.js
const msg = require("./messages"); // Node tự giả định đuôi .js; nếu là thư mục sẽ tìm index.js
console.log(msg.getDate());

// === ES Modules: addTwoNos.mjs & main.mjs ===
// addTwoNos.mjs
function addTwo(num) {
  return num + 4;
}
export { addTwo };

// main.mjs
import { addTwo } from "./addTwoNos.mjs";
console.log(addTwo(4)); // 8
```

## 4. Ba loại Module & Các Core Modules thiết yếu

Node.js chia module thành 3 nhóm: **Core modules** (tích hợp sẵn, không cần cài), **Local modules** (do nhóm phát triển tự viết), và **Third-party modules** (cài qua NPM — cần kiểm tra license trước khi dùng).

```javascript
// 1. http: Tạo Web Server lắng nghe request trên port 8080
const http = require("http");
const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.write("Hello from server\n");
  res.end("Hello, World!");
});
server.listen(8080, () => console.log("Server listening on port 8080"));

// 2. fs: Thao tác File System (bất đồng bộ vs đồng bộ)
const fs = require("fs");
fs.readFile("sample.txt", "utf8", (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
// Đồng bộ (chỉ nên dùng lúc khởi động): const syncData = fs.readFileSync("content.md", "utf8");

// 3. path, os, util, url, querystring
const path = require("path");
const os = require("os");
const util = require("util");
const url = require("url");
const querystring = require("querystring");

console.log(path.basename("/content/index/home.html")); // "home.html"
console.log(os.platform(), os.arch());                  // vd: "linux" "x64"
console.log(util.format("Executed %d time(s).", 3));    // "Executed 3 time(s)."

const parsed = url.parse("http://localhost:2000/index.html?lastName=Kent&firstName=Clark", true);
console.log(parsed.query.firstName);                    // "Clark"
console.log(querystring.parse("lastName=Kent&firstName=Clark").firstName); // "Clark"
```

## 5. Quản lý gói với NPM & `package.json`

**NPM (Node Package Manager)** đóng 2 vai trò: (1) công cụ dòng lệnh **CLI** để cài đặt, cập nhật, gỡ bỏ và xuất bản package; (2) **kho lưu trữ trực tuyến (online registry)** chứa các package JavaScript kèm phiên bản và cây phụ thuộc.

- **`package.json`:** Nằm ở thư mục gốc dự án, chứa metadata định danh (`name`, `version`), entry point (`main`), `scripts`, và `dependencies`. Nếu một package thiếu `package.json`, Node.js mặc định tệp chính là **`index.js`**.
- **Local vs. Global Install:**

```bash
# Local install (mặc định & khuyến nghị): chỉ project hiện tại dùng được, lưu vào ./node_modules/
npm install express

# Global install: dùng chung cho mọi project trên máy (cẩn thận xung đột phiên bản!)
npm install -g nodemon
```

## 6. Nền tảng JavaScript cho Express: Biến, Array & Request Extraction

Khi chuyển sang Express ở các module sau, bạn cần nắm vững 3 cách trích xuất dữ liệu đầu vào từ HTTP request và các hàm xử lý mảng (`filter`, `map`, `reduce`):

```javascript
// Tách dữ liệu trong Express: req.params, req.query, req.body
app.get("/users/:id", (req, res) => res.send(req.params.id));       // /users/123 -> "123"
app.get("/books", (req, res) => res.send(req.query.author));        // /books?author=John -> "John"
app.post("/register", (req, res) => res.send(req.body.username));   // JSON body -> username

// Xử lý dữ liệu không đột biến (immutable) bằng filter/map/reduce
const books = [{ title: "JS", rating: 5 }, { title: "Node", rating: 3 }];
const topBooks = books.filter((b) => b.rating > 4);
const titles = books.map((b) => b.title);
const avgRating = books.reduce((sum, b) => sum + b.rating, 0) / books.length; // 4
```

## 7. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Nhầm lẫn Node.js là Web Framework:** Node.js là *runtime environment* thực thi JS; **Express.js** mới là *web framework* chạy trên nền Node.js.
2. **Dùng `import()` trong khối điều kiện `if`:** Lệnh `import` tĩnh bắt buộc ở đầu tệp; muốn nạp module có điều kiện theo chuẩn CommonJS thì dùng `require()`, hoặc dùng dynamic `import()` trả về Promise.
3. **Lạm dụng Global Install (`npm install -g`):** Cài global khiến nhiều dự án dùng chung một phiên bản thư viện, dễ gây vỡ tương thích khi nâng cấp; chỉ dùng `-g` cho CLI tool, còn thư viện ứng dụng phải cài local.
4. **Dùng `fs.readFileSync` trong route handler:** Hàm đồng bộ (`*Sync`) khóa cứng single thread của Event Loop, làm toàn bộ server ngừng phục vụ các request khác trong lúc đọc đĩa.
5. **Quên `res.end()` khi dùng module `http` thuần:** Nếu không gọi `res.end()`, kết nối HTTP sẽ treo vô hạn ở phía client cho tới khi timeout.

## 8. Điểm cốt lõi cần nhớ (Key Takeaways)

- Node.js chạy trên **V8 Engine** với mô hình **single-threaded, event-driven, non-blocking I/O**, xử lý kết quả bất đồng bộ thông qua **callback functions**.
- **CommonJS (`require`)** đồng bộ & liên kết động (chạy được mọi nơi trong file); **ES Modules (`import`)** bất đồng bộ & liên kết tĩnh (bắt đầu từ đầu file, đuôi `.mjs`).
- Ba nhóm module: **Core** (`http`, `fs`, `path`, `os`, `util`, `url`, `querystring`), **Local** (`./today`), và **Third-party** (qua **NPM**).
- Thiếu `package.json`, Node.js mặc định điểm khởi chạy của thư mục module là **`index.js`**.
