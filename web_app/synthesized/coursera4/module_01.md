# Module 1: Introduction to React and Class Components

> **Tư tưởng cốt lõi:** React là thư viện JavaScript xây dựng giao diện người dùng theo kiến trúc thành phần (Component-based), cú pháp khai báo (Declarative UI), liên kết dữ liệu một chiều (One-way Data Binding), Virtual DOM và JSX; làm chủ cấu trúc dự án Vite, ES6 và vòng đời Class Component (Mounting → Updating → Unmounting) cùng sự khác biệt giữa `state` và `props` là nền tảng của toàn bộ khóa học.

## 1. Library vs. Framework & Các đặc trưng cốt lõi của React

| Tiêu chí | Library (Thư viện — vd: React, Lodash) | Framework (Khung ứng dụng — vd: Angular, Django) |
| --- | --- | --- |
| **Bản chất** | Kho chứa các hàm/thành phần viết sẵn cho tác vụ cụ thể | Nền tảng toàn diện quy định sẵn cấu trúc & kiến trúc toàn ứng dụng |
| **Quyền điều khiển (Inversion of Control)** | **Mã của bạn gọi thư viện** khi cần thiết | **Framework gọi mã của bạn** theo vòng đời & quy ước có sẵn |
| **Độ linh hoạt** | Cao — dễ kết hợp nhiều thư viện (routing, state, HTTP) | Chặt chẽ hơn — cung cấp giải pháp trọn gói (batteries-included) |

### 6 đặc trưng nổi bật của React
1. **Component-Based Architecture:** Chia nhỏ UI thành các khối độc lập, tái sử dụng được, rồi ghép vào component cha.
2. **Declarative Syntax (Cú pháp khai báo):** Bạn mô tả giao diện *trông như thế nào* ứng với từng trạng thái dữ liệu, React tự động cập nhật DOM khi dữ liệu đổi.
3. **Virtual DOM Optimization:** Bản sao nhẹ của DOM trong bộ nhớ giúp tính toán khác biệt (diffing) và chỉ cập nhật đúng nút thay đổi trên Real DOM.
4. **One-Way Data Binding (Luồng dữ liệu một chiều):** Dữ liệu truyền từ **Parent → Child** qua `props`, giúp luồng trạng thái dễ dự đoán và dễ debug.
5. **JSX (JavaScript XML):** Phần mở rộng cú pháp cho phép viết mã giống HTML ngay trong JavaScript; công cụ **Babel** biên dịch JSX thành các đối tượng JavaScript tiêu chuẩn (`React.createElement(...)`).
6. **React Hooks:** Cho phép Function Component sử dụng state và tính năng vòng đời mà không cần viết class.

## 2. Khởi tạo dự án React: Vite vs. Create React App (CRA)

- **Create React App (CRA):** Công cụ cũ hơn, cài đặt nhiều file/thư mục dư thừa dẫn đến dung lượng lớn và khởi động chậm.
- **Vite (`npm create vite@latest`):** Công cụ build hiện đại tận dụng ES Modules bản địa của trình duyệt, khởi động server tức thì, Hot Module Replacement (HMR) siêu nhanh và cấu trúc gọn nhẹ:

```text
my-react-app/
├── index.html          # Điểm vào HTML gốc (chứa <div id="root">)
├── package.json        # Metadata dự án, scripts và danh sách dependencies
├── .gitignore          # File/thư mục Git bỏ qua (như node_modules/)
├── node_modules/       # Toàn bộ gói thư viện cài qua npm/yarn
└── src/
    ├── main.jsx        # Điểm vào JavaScript gắn <App /> vào #root
    └── App.jsx         # Root component của ứng dụng React
```

- **Quy tắc bắt buộc của JSX:** Mọi biểu thức JSX trả về phải được bọc trong **duy nhất 1 thẻ cha** (như `<div>...</div>`) hoặc **Fragment rỗng `<>...</>`** (tránh tạo thêm thẻ `<div>` thừa trên DOM). Chèn biểu thức JS bằng cặp ngoặc nhọn `{expression}`.

## 3. Ba loại Component & Class Component trong React

React có 3 dạng component: **Functional Components**, **Class Components**, và **Higher-Order Components (HOCs)**.

- **Class Component** là một lớp ES6 kế thừa `React.Component` và bắt buộc định nghĩa phương thức `render()`:

```jsx
import React, { Component } from "react";

export default class CounterCard extends Component {
  constructor(props) {
    super(props);
    // Khởi tạo state cục bộ trong constructor
    this.state = { count: 0 };
  }

  handleIncrement = () => {
    // LUÔN dùng this.setState(), KHÔNG sửa trực tiếp this.state.count++
    this.setState((prev) => ({ count: prev.count + 1 }));
  };

  render() {
    return (
      <>
        <h2>{this.props.title}</h2>
        <p>Giá trị hiện tại: {this.state.count}</p>
        <button onClick={this.handleIncrement}>Tăng +1</button>
      </>
    );
  }
}
```

### So sánh `State` vs. `Props`

| Tiêu chí | `state` (Trạng thái nội bộ) | `props` (Properties — Thuộc tính truyền vào) |
| --- | --- | --- |
| **Nguồn gốc** | Được khởi tạo và quản lý **bên trong** chính component (`this.state`) | Được truyền **từ ngoài vào** (Parent → Child) qua thuộc tính JSX (`<Child title="..." />`) |
| **Khả năng thay đổi** | Có thể thay đổi (mutable qua `this.setState()`) — mỗi lần đổi kích hoạt re-render | **Bất biến (read-only / immutable)** bên trong component con |
| **Phân loại** | Local state (cục bộ 1 component) & Shared state (chia sẻ nhiều component) | Dữ liệu & hàm callback dùng để truyền thông tin giữa các component |

## 4. Vòng đời của Class Component (Component Lifecycle)

Mỗi Class Component đi qua **3 pha chính**: **Mounting** (tạo & gắn vào DOM) → **Updating** (cập nhật khi `props` hoặc `state` đổi) → **Unmounting** (gỡ bỏ khỏi DOM).

| Pha vòng đời | Các phương thức gọi theo thứ tự | Mục đích sử dụng |
| --- | --- | --- |
| **1. Mounting** | `constructor()` → `getDerivedStateFromProps()` → `render()` → `componentDidMount()` | Khởi tạo state, đồng bộ state từ props (nếu cần), render JSX ra DOM, sau đó gọi API / đăng ký sự kiện trong `componentDidMount()` |
| **2. Updating** | `getDerivedStateFromProps()` → `shouldComponentUpdate()` → `render()` → `getSnapshotBeforeUpdate()` → `componentDidUpdate()` | Phản hồi khi `props` hoặc `state` thay đổi; `getDerivedStateFromProps()` dùng khi cần phản ánh thay đổi từ `props` vào `state` |
| **3. Unmounting** | `componentWillUnmount()` | Dọn dẹp (cleanup): hủy timer, hủy subscription, ngắt kết nối mạng để chống rò rỉ bộ nhớ |

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Thay đổi `this.state` trực tiếp (Direct Mutation):** Nếu viết `this.state.count = 5` thay vì `this.setState({ count: 5 })`, React **không nhận biết được sự thay đổi và sẽ KHÔNG re-render giao diện** (đồng thời có thể bị ghi đè ở lần `setState` tiếp theo).
2. **Trả về nhiều thẻ ngang hàng trong JSX không có thẻ bọc:** Luôn bọc bằng `<>...</>` hoặc thẻ cha duy nhất, nếu không Babel sẽ báo lỗi biên dịch cú pháp.
3. **Quên gọi `super(props)` trong `constructor(props)`:** Dẫn đến `this.props` bị `undefined` bên trong constructor.
4. **Cố gắng sửa đổi `this.props` bên trong component con:** Vi phạm nguyên tắc bất biến và luồng dữ liệu một chiều của React.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- **JSX** là cú pháp mở rộng của JavaScript giúp viết mã giống HTML trong JS và được **Babel** biên dịch thành đối tượng JS chuẩn.
- **Vite** là công cụ chuẩn hiện đại thay thế CRA để khởi tạo dự án React nhanh, nhẹ (`npm create vite@latest`).
- **Mounting** gọi lần lượt: `constructor()` → `getDerivedStateFromProps()` → `render()` → `componentDidMount()`.
- Truyền dữ liệu giữa các component bằng **`props`** (một chiều, chỉ đọc); quản lý dữ liệu thay đổi theo thời gian bằng **`state`** và cập nhật bằng **`this.setState()`**.
