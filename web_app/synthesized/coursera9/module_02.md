# Module 2: Asynchronous I/O with Callback Programming

> **Tư tưởng cốt lõi:** Trong Node.js, mọi thao tác mạng và I/O đều chạy bất đồng bộ (non-blocking) để không lãng phí CPU chờ đợi; kết quả được xử lý qua chuỗi tiến hóa từ **Error-first Callbacks** sang **Promises** (`.then()`/`.catch()`) và **`async`/`await`** kết hợp **Axios** nhằm xóa bỏ Callback Hell và Inversion of Control.

## 1. Non-Blocking Network Operations & `http.request()`

Các thao tác mạng (gọi Web Service từ xa, truy vấn DB) có độ trễ không xác định. Nếu chương trình đứng chờ (blocking), luồng chính của Node.js bị đóng băng và không thể phục vụ người dùng khác. Vì vậy, Node.js thực hiện mọi tác vụ mạng theo cơ chế **non-blocking**:

1. Khi gọi `http.request(options, callback)`, Node.js **trả về ngay lập tức** một đối tượng `http.ClientRequest` biểu diễn trạng thái **"a request is in progress"** (yêu cầu đang được xử lý), chứ **chưa có** nội dung phản hồi từ server đích.
2. Tham số `callback` trong `http.request` là **tùy chọn (optional)**; khi server đích trả HTTP response message về cho Node.js framework, Node.js mới kích hoạt callback này với tham số là đối tượng `response`.
3. Bên trong callback, bạn dùng `object.on(eventName, handler)` để lắng nghe các sự kiện stream dữ liệu:
   - `'data'`: kích hoạt mỗi khi nhận một mảnh dữ liệu (`chunk`).
   - `'end'`: kích hoạt khi toàn bộ HTTP response message đã truyền xong.
   - `'error'` / `'close'`: xử lý khi kết nối lỗi hoặc đóng.

```javascript
const http = require("http");

const options = {
  hostname: "api.open-notify.org",
  path: "/astros.json",
  method: "GET"
};

const req = http.request(options, (res) => {
  let buffer = "";
  res.on("data", (chunk) => {
    buffer += chunk;
  });
  res.on("end", () => {
    const parsed = JSON.parse(buffer);
    console.log("Astronauts in space:", parsed.number);
  });
});

req.on("error", (err) => {
  console.error("Request error:", err.message);
});

req.end(); // Bắt buộc gọi để kết thúc và gửi request đi
```

## 2. Quy ước Error-First Callback & Truyền kết quả liên tầng

Trong SDK và các module Node.js, hàm callback tuân theo quy ước **Error-First Callback**: **tham số đầu tiên luôn là đối tượng `Error`** (`(err, data) => ...`).

- Nếu có lỗi: truyền `err` vào tham số thứ nhất, dọn dẹp kết nối đang mở và dừng xử lý.
- Nếu thành công: truyền **`null`** vào tham số thứ nhất và truyền dữ liệu kết quả vào tham số thứ hai.
- **Tại sao không dùng `return` trong callback?** Vì hàm bất đồng bộ đã trả điều khiển về cho hàm gọi trước khi server từ xa phản hồi; muốn trả kết quả từ module về ứng dụng chính, module phải nhận một `resultCallback` làm tham số và gọi lại nó trong sự kiện `'end'`.

```javascript
// weather.js (Custom module dùng Error-First Callback)
const http = require("http");

exports.current = function (location, resultCallback) {
  const req = http.request({ hostname: "example.com", path: `/weather?loc=${location}` }, (res) => {
    let body = "";
    res.on("data", (chunk) => (body += chunk));
    res.on("end", () => {
      // Thành công -> tham số đầu tiên là null
      resultCallback(null, body);
    });
  });

  req.on("error", (err) => {
    // Có lỗi -> truyền Error object ở tham số đầu tiên
    resultCallback(err);
  });
  req.end();
};

// app.js (Main application)
const weather = require("./weather");
http.createServer((req, response) => {
  weather.current("SFO", (err, tempF) => {
    if (err) {
      response.writeHead(500);
      return response.end("Error fetching weather");
    }
    response.end(`The current weather reading is ${tempF} degrees`);
  });
}).listen(8080);
```

## 3. Hai vấn đề lớn của Callbacks: Callback Hell & Inversion of Control

Dù callback (kể cả anonymous callback dùng inline hoặc arrow function) giúp viết code gọn cho các tác vụ đơn lẻ, khi hệ thống phức tạp sẽ lộ 2 nhược điểm nghiêm trọng:

| Vấn đề | Bản chất | Hậu quả thực tế |
| --- | --- | --- |
| **Callback Hell (Pyramid of Doom)** | Các tác vụ phụ thuộc tuần tự buộc phải lồng callback này bên trong callback kia tạo hình kim tự tháp | Code khó đọc, khó debug, bảo trì ác mộng (ví dụ: mua nguyên liệu → trộn bột → nướng bánh → trang trí → phục vụ) |
| **Inversion of Control (IoC)** | Trao quyền điều khiển luồng thực thi cho hàm bên thứ ba (3rd-party code) | Không kiểm soát được callback bị gọi **quá nhiều lần**, **không bao giờ gọi**, **gọi quá sớm/muộn**, mất context hoặc truyền sai tham số |

**Cách khắc phục:** Chia nhỏ hàm, viết chú thích rõ ràng, sử dụng **Promises** hoặc cú pháp **`async/await`**.

## 4. Promises, `async`/`await` và thư viện Axios

### A. Promise và 3 trạng thái vòng đời

**Promise** là một đối tượng đại diện cho kết quả hoàn thành (hoặc thất bại) trong tương lai của một tác vụ bất đồng bộ. Promise luôn ở một trong **3 trạng thái**:

1. **`pending`:** Trạng thái khởi tạo ban đầu, tác vụ chưa xong.
2. **`fulfilled` (hoặc `resolved`):** Tác vụ hoàn tất thành công, kích hoạt hàm truyền trong `.then()`.
3. **`rejected`:** Tác vụ thất bại / phát sinh lỗi, kích hoạt hàm truyền trong `.catch()`.

```javascript
const fs = require("fs").promises;

// Tạo Promise thủ công với new Promise((resolve, reject) => ...)
const checkTask = new Promise((resolve, reject) => {
  const success = true;
  if (success) resolve("The operation was successful!");
  else reject(new Error("The operation failed!"));
});

checkTask
  .then((msg) => console.log(msg))
  .catch((err) => console.error(err.message));

// Dùng fs.promises đọc file bất đồng bộ không cần callback lồng nhau
fs.readFile("example.txt", "utf8")
  .then((data) => console.log(data))
  .catch((err) => console.error("Error reading file:", err));
```

### B. `async`/`await` & Gọi HTTP API bằng `axios`

`async`/`await` là cú pháp đường (syntactic sugar) xây trên Promise giúp code bất đồng bộ đọc tuần tự tự nhiên như code đồng bộ:
- Hàm đánh dấu `async` **luôn trả về một Promise** (`return` tương ứng `resolve`, `throw` tương ứng `reject`).
- Từ khóa `await` tạm dừng thực thi *bên trong hàm `async` đó* cho tới khi Promise ổn định, bắt lỗi gọn gàng bằng `try ... catch`.
- **`axios`** là HTTP client dựa trên Promise rất phổ biến trong Node.js: tự động chuyển đổi JSON, trả dữ liệu qua `response.data`.

```javascript
const axios = require("axios");

// Cách 1: Dùng Promise chaining (.then / .catch)
axios.get("https://api.example.com/data")
  .then((response) => console.log("Fulfilled:", response.data))
  .catch((error) => console.error("Rejected:", error.message));

// Cách 2: Dùng async/await + try/catch (khuyến nghị)
async function postUserData() {
  try {
    const response = await axios.post("https://jsonplaceholder.typicode.com/posts", {
      title: "Node Async",
      body: "Using Axios with async/await",
      userId: 1
    });
    console.log("Created:", response.data);
  } catch (error) {
    console.error("Error posting data:", error.message);
  }
}
postUserData();
```

## 5. Xử lý JSON trong trao đổi dữ liệu API

JSON là chuẩn trao đổi dữ liệu (serialization/deserialization) mặc định của REST API và khớp trực tiếp với đối tượng JavaScript:

| Phương thức | Chức năng | Ví dụ |
| --- | --- | --- |
| `JSON.parse(str)` | Chuyển **chuỗi JSON** (nhận từ HTTP body) thành **JavaScript Object** | `const obj = JSON.parse('{"Company":"IBM"}');` |
| `JSON.stringify(obj)` | Chuyển **JavaScript Object** thành **chuỗi JSON** (để gửi qua HTTP) | `const str = JSON.stringify({ status: "ok" });` |

## 6. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Quên gọi `req.end()` khi dùng `http.request()`:** Request sẽ không bao giờ được gửi đi thực sự cho đến khi `req.end()` được gọi.
2. **Dùng `await` bên ngoài hàm `async`:** Ở CommonJS truyền thống, `await` chỉ hợp lệ bên trong hàm khai báo `async`; dùng sai sẽ gây `SyntaxError`.
3. **Bỏ qua khối `catch` hoặc `.catch()`:** Một Promise bị `rejected` không có handler sẽ dẫn tới `UnhandledPromiseRejection`, có thể làm sập tiến trình Node.js trên phiên bản mới.
4. **Nhầm `JSON.parse()` và `JSON.stringify()`:** `parse` biến chuỗi thành object để đọc thuộc tính (`obj.name`); `stringify` biến object thành chuỗi để ghi file hoặc gửi qua mạng.
5. **Trả về giá trị bằng `return` từ trong callback bất đồng bộ:** `return` trong callback chỉ thoát khỏi chính callback đó chứ không trả được giá trị ra cho hàm cha đã kết thúc trước đó.

## 7. Điểm cốt lõi cần nhớ (Key Takeaways)

- Mọi thao tác mạng trong Node.js là **non-blocking**: `http.request()` trả về ngay trạng thái đang xử lý, và **callback** chỉ chạy khi nhận được HTTP response message từ server đích.
- Quy ước SDK Node.js: tham số thứ nhất của callback là **`Error` object** (truyền **`null`** nếu thành công).
- **Promise** có 3 trạng thái (**pending**, **resolved/fulfilled**, **rejected**) và chuỗi `.then()` / `.catch()`.
- **`async`/`await`** + **`axios`** là bộ công cụ chuẩn để thay thế Callback Hell và tránh rủi ro Inversion of Control.
