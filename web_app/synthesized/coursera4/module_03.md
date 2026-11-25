# Module 3: In-depth Understanding of Advanced React Functionality

> **Tư tưởng cốt lõi:** React Hooks (`useEffect`, Custom Hooks) giải quyết trọn vẹn side effects, gọi API ngoài và quản lý form có kiểm soát (Controlled Components); khi ứng dụng phình to với trạng thái dùng chung xuyên suốt nhiều màn hình (như giỏ hàng), **Redux** và **Redux Toolkit (RTK)** cung cấp kho trạng thái tập trung theo luồng dữ liệu một chiều bất biến kết hợp middleware bất đồng bộ (Thunk/Saga).

## 1. Quản lý Side Effects với `useEffect`, Gọi API & Custom Hooks

- **Side Effect (Tác dụng phụ):** Mọi thao tác bất đồng bộ hoặc tương tác ra ngoài phạm vi render thuần (gọi HTTP API, đăng ký event listener, đặt timer `setInterval`, thao tác DOM trực tiếp).
- **Cơ chế Dependency Array của `useEffect(callback, deps)`:**

| Cách truyền Dependency Array | Thời điểm `useEffect` chạy | Trường hợp sử dụng điển hình |
| --- | --- | --- |
| **Không truyền** (`useEffect(fn)`) | Sau **mọi** lần render | Hiếm dùng (dễ gây vòng lặp vô hạn nếu có gọi `setState`) |
| **Mảng rỗng `[]`** (`useEffect(fn, [])`) | **Chỉ chạy ĐÚNG 1 LẦN** sau lần render đầu tiên (khi component mount) | **Gọi API tải dữ liệu ban đầu** (`fetch` / `axios`) |
| **Có phụ thuộc `[a, b]`** | Chạy lần đầu và mỗi khi `a` hoặc `b` thay đổi | Tải lại dữ liệu khi `userId` hoặc từ khóa tìm kiếm đổi |

```jsx
import React, { useState, useEffect } from "react";

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://api.example.com/products")
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Fetch error:", err));
  }, []); // Mảng rỗng [] -> chỉ gọi API đúng 1 lần khi mount

  return <ul>{products.map((p) => <li key={p.id}>{p.name}</li>)}</ul>;
}
```

- **Gọi External Services (HTTP Requests):** Hai phương pháp chuẩn là **Fetch API** (tích hợp sẵn trong trình duyệt) và **Axios** (thư viện phổ biến tự động parse JSON, hỗ trợ interceptor & xử lý lỗi HTTP gọn hơn).
- **Custom Hooks:** Là hàm JavaScript tự định nghĩa (bắt đầu bằng tiền tố `use`, vd `useToggle`, `useFetch`) kết hợp một hoặc nhiều Hook chuẩn để **tách biệt và tái sử dụng logic có trạng thái** giữa nhiều component mà không làm phình to cây phân cấp component.

## 2. Quản lý Form: Controlled vs. Uncontrolled Components

| Tiêu chí | Controlled Component (Khuyến nghị) | Uncontrolled Component |
| --- | --- | --- |
| **Ai giữ giá trị input?** | **React State** (`useState`) là nguồn chân lý duy nhất | **DOM của trình duyệt** tự giữ giá trị (đọc qua `ref`) |
| **Cách cập nhật** | Gắn `value={state}` và bắt sự kiện `onChange={(e) => setState(e.target.value)}` | Không cần `onChange` cho từng phím gõ |
| **Xử lý Submit** | Gắn `onSubmit={handleSubmit}` lên `<form>` và gọi **`e.preventDefault()`** để chặn tải lại trang | Đọc `inputRef.current.value` khi submit |
| **Ưu điểm** | Kiểm soát tức thì, dễ validate real-time, vô hiệu hóa nút gửi động | Ít code hơn cho form cực đơn giản |

## 3. Quản lý trạng thái toàn ứng dụng với Redux & Redux Toolkit (RTK)

Khi nhiều component ở xa nhau cùng cần chia sẻ trạng thái (như giỏ hàng thương mại điện tử), việc truyền props qua nhiều tầng trung gian (**Prop Drilling**) trở nên rối rắm. **Redux** gom toàn bộ trạng thái ứng dụng vào **một nguồn chân lý duy nhất (Single Source of Truth)**.

### Luồng dữ liệu một chiều (Unidirectional Data Flow) trong Redux

```text
[UI Component] ──dispatch(action)──▶ [Store] ──(currentState, action)──▶ [Reducer (Pure Function)]
      ▲                                                                           │
      └──────────────────── re-render UI khi state thay đổi ◀───── [New Immutable State]
```

| Thành phần kiến trúc Redux | Vai trò cốt lõi |
| --- | --- |
| **Store** | Đối tượng trung tâm lưu trữ toàn bộ **Application State** (`getState()`, `dispatch()`, `subscribe()`) |
| **Action & Action Creator** | Đối tượng mô tả *"chuyện gì vừa xảy ra"* gồm `type` (bắt buộc) và `payload` (dữ liệu đi kèm); Action Creator là hàm sinh ra action object |
| **Reducer** | **Pure Function** `(currentState, action) => newState` quy định *cách cập nhật state*; **tuyệt đối không mutate state cũ**, luôn trả về state mới (có thể gộp bằng `combineReducers()`) |

### Xử lý bất đồng bộ (Async) trong Redux: Thunk vs. Saga

Vì Reducer thuần túy phải đồng bộ (synchronous), các tác vụ bất đồng bộ (gọi API) chạy song song cần thông qua **Middleware**:

| Middleware | Cơ chế hoạt động | Ưu điểm & Trường hợp phù hợp |
| --- | --- | --- |
| **Redux Thunk** | Cho phép Action Creator trả về một **hàm (function)** thay vì plain object, nhận `(dispatch, getState)` để thực thi logic async rồi dispatch kết quả | Đơn giản, dễ học, tích hợp sẵn trong Redux Toolkit — lý tưởng cho đa số ứng dụng gọi API thông thường |
| **Redux Saga** | Sử dụng **ES6 Generator Functions (`function*`, `yield`)** chạy nền quản lý các luồng side effects phức tạp | Rất mạnh cho luồng bất đồng bộ phức tạp (hủy request cũ, debounce, retry, racing) và dễ viết unit test tách biệt |

### Redux Toolkit (RTK) — Chuẩn phát triển Redux hiện đại

**Redux Toolkit** là gói chính thức của đội ngũ Redux nhằm giảm tối đa mã lặp lại (boilerplate):
- **`configureStore()`:** Gộp toàn bộ logic cấu hình store (root reducer, Redux Thunk middleware, Redux DevTools) vào **một lệnh gọi hàm duy nhất**.
- **`createSlice()`:** Định nghĩa một **"slice"** (lát cắt trạng thái theo tính năng, vd `cartSlice`) gom gọn `name`, `initialState`, `reducers` và tự động sinh Action Creators kèm cơ chế cập nhật bất biến an toàn (nhờ Immer bên dưới).

```javascript
import { createSlice, configureStore } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: { items: [] },
  reducers: {
    addItem: (state, action) => {
      state.items.push(action.payload); // RTK (Immer) tự chuyển thành cập nhật bất biến!
    },
    removeItem: (state, action) => {
      state.items = state.items.filter((i) => i.id !== action.payload);
    },
  },
});

export const { addItem, removeItem } = cartSlice.actions;
export const store = configureStore({ reducer: { cart: cartSlice.reducer } });
```

### Khi nào dùng React Hooks vs. Redux?
- **React Hooks (`useState`, `useContext`, Custom Hooks):** Phù hợp trạng thái cục bộ của component, ứng dụng vừa và nhỏ, ít chia sẻ chéo.
- **Redux / RTK:** Phù hợp ứng dụng lớn có **Application State** chia sẻ rộng rãi, cần dự đoán luồng dữ liệu chặt chẽ, time-travel debugging và quản lý async tập trung.

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Quên mảng rỗng `[]` trong `useEffect` khi gọi API:** Nếu thiếu dependency array, mỗi lần `setProducts(data)` chạy sẽ trigger re-render → gọi lại `useEffect` → tạo **vòng lặp gọi API vô hạn**!
2. **Quên `e.preventDefault()` trong `onSubmit` của React Form:** Khiến trình duyệt tải lại toàn bộ trang và xóa sạch trạng thái React hiện tại.
3. **Mutate state trực tiếp trong Redux Reducer cổ điển:** Nếu không dùng Redux Toolkit (`createSlice`), việc sửa thẳng `state.items.push(...)` sẽ phá vỡ quy tắc pure function khiến component không cập nhật.
4. **Cài Redux cho ứng dụng quá nhỏ:** Tăng độ phức tạp không cần thiết khi `useState` / lifting state up đã đủ giải quyết.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- Dùng **`useEffect(fn, [])`** để chạy side effect (như `fetch`/`axios`) **đúng 1 lần sau lần render đầu tiên**.
- **Custom Hooks** đóng gói và tái sử dụng logic có trạng thái giữa nhiều component.
- Trong Controlled Form, **`useState`** quản lý giá trị input qua `value` + `onChange`, và `onSubmit` chặn reload bằng `e.preventDefault()`.
- 3 trụ cột kiến trúc Redux: **Store** (lưu state), **Actions** (mô tả sự kiện), **Reducers** (hàm thuần cập nhật state); 2 middleware bất đồng bộ phổ biến: **Redux Thunk** và **Redux Saga**.
- **Redux Toolkit (RTK)** chuẩn hóa cấu hình bằng **`configureStore()`** và chia nhỏ trạng thái bằng **`createSlice()`**.
