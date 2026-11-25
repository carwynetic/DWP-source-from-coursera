# Module 2: Understanding Function Components with Array and DOM Manipulation

> **Tư tưởng cốt lõi:** Function Components kết hợp với Hooks (`useState`, `useEffect`) là chuẩn hiện đại của React nhờ cú pháp gọn nhẹ và khả năng kết hợp (Component Composition) linh hoạt; việc render danh sách bằng `Array.map()` cùng cơ chế **Virtual DOM & Reconciliation** giúp React chỉ cập nhật đúng những phần tử DOM thực sự thay đổi với hiệu năng cao.

## 1. Function Components, Props & Nguyên tắc Component Composition

- **Function Component:** Là một hàm JavaScript (dùng `function` hoặc arrow function `const Comp = (props) => ...`) nhận đối tượng `props` (bất biến/read-only) và trả về JSX.
- **4 nguyên tắc của Props:** Reusability (tái sử dụng), Unidirectional Data Flow (dữ liệu một chiều Cha → Con), Customization (tùy biến hành vi/hiển thị), Composition (kết hợp lồng nhau).
- **5 nguyên tắc của Component Composition (ghép component nhỏ thành UI phức tạp):**

| Nguyên tắc | Ý nghĩa cốt lõi |
| --- | --- |
| **Abstraction (Trừu tượng hóa)** | Tạo các component tái sử dụng đóng gói trọn vẹn một tính năng UI (ẩn chi tiết triển khai bên trong) |
| **Reusability (Tái sử dụng)** | Một component (vd `Button`, `Card`) có thể dùng lại ở nhiều màn hình với `props` khác nhau |
| **Hierarchy (Phân cấp)** | Tổ chức component theo cây Cha–Con rõ ràng giúp cấu trúc ứng dụng mạch lạc, dễ bảo trì và khoanh vùng lỗi |
| **Props & `children`** | Truyền dữ liệu, callback và cả các phần tử JSX lồng bên trong (`props.children`) để tạo khung layout linh hoạt |
| **Higher-Order Components (HOCs)** | Hàm nhận vào một component và trả về component mới được bổ sung thêm logic/state chung mà **không sửa đổi mã gốc** của component đó |

## 2. Quản lý State với `useState` & Vòng đời 4 pha của Function Component

- **Cú pháp `useState` (Array Destructuring):**

```jsx
import React, { useState } from "react";

function UserProfile() {
  const [name, setName] = useState("Marie");
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div>
      <h3>{name}</h3>
      <button onClick={() => setName("Marie Torres")}>Cập nhật họ tên</button>

      {/* Conditional Rendering: Thu gọn/Mở rộng giảm rối màn hình */}
      <button onClick={() => setIsExpanded((prev) => !prev)}>
        {isExpanded ? "Thu gọn" : "Xem chi tiết"}
      </button>
      {isExpanded && <p>Thông tin hồ sơ chi tiết của người dùng...</p>}
    </div>
  );
}
```

### 4 pha vòng đời của Function Component (bằng Hooks)

| Pha vòng đời | Diễn biến bên trong React | Hook / Cơ chế tương ứng |
| --- | --- | --- |
| **1. Mounting (Initialization)** | Chạy thân hàm lần đầu, khởi tạo state ban đầu, gắn vào DOM và chạy side effects khởi tạo | `useState(initial)`, `useEffect(fn, [])` |
| **2. Updating** | Khi `state` hoặc `props` thay đổi, React **gọi lại thân hàm** và đánh giá lại JSX | `setState(...)`, `useEffect(fn, [dep])` |
| **3. Unmounting** | Trước khi gỡ component khỏi DOM, React thực thi hàm dọn dẹp (cleanup) | Hàm `return () => { ... }` bên trong `useEffect` |
| **4. Error Handling** | Bắt lỗi render trong cây con để **không làm sập toàn bộ ứng dụng** | Error Boundaries |

## 3. Làm việc với Mảng (Arrays) trong React

- Mảng trong JavaScript bắt đầu từ chỉ số **`0`** (`arr[0]` truy cập phần tử đầu tiên).
- **Các phương thức mảng hay gặp & phân biệt Mutating vs. Non-mutating:**

| Phương thức | Tác dụng | Có sửa trực tiếp mảng gốc? | Dùng trong React như thế nào? |
| --- | --- | :---: | --- |
| `map()` | Biến đổi từng phần tử và trả về mảng mới | Không | **Chuẩn để render danh sách JSX động** (`items.map(item => <li key={item.id}>...</li>)`) |
| `forEach()` | Duyệt và thực thi callback, trả về `undefined` | Không | Chạy tác vụ phụ (không dùng trực tiếp trong JSX để trả về phần tử) |
| `filter()` | Trả về mảng mới gồm các phần tử thỏa điều kiện | Không | Chuẩn để **xóa phần tử** khỏi React state bất biến |
| `push()` | Thêm phần tử mới vào **cuối mảng** | **Có (Mutate)** | Trong React state, ưu tiên `[...prev, newItem]` thay vì gọi `stateArr.push()` trực tiếp |
| `splice()` | Xóa/chèn phần tử trực tiếp tại vị trí chỉ định | **Có (Mutate)** | Sửa đổi trực tiếp mảng gốc — tránh gọi thẳng lên state array |

## 4. Virtual DOM, Reconciliation & Styling trong React

- **Các thành phần của DOM:** Nodes, Elements, **Attributes** (cung cấp thông tin bổ sung cho phần tử HTML như `id`, `className`, `disabled`, `data-*`), và Events.
- **Cơ chế hoạt động của Virtual DOM:**
  1. React duy trì một biểu diễn nhẹ của cây DOM thật ngay trong bộ nhớ (**Virtual DOM**).
  2. Khi `state` hoặc `props` đổi, React tạo cây Virtual DOM mới và so sánh với bản trước đó (**Diffing Algorithm**).
  3. Quá trình **Reconciliation** chỉ áp dụng đúng tập thay đổi tối thiểu (minimal patch) lên **Real DOM**, tránh thao tác DOM tốn kém toàn trang và tăng tốc độ hiển thị vượt trội.
- **Các cách Styling trong React:** Inline styles (truyền đối tượng JS với thuộc tính camelCase: `style={{ backgroundColor: "lightblue", borderRadius: "8px" }}`), CSS Stylesheets truyền thống, **CSS Modules** (cô lập phạm vi class theo component), và **Styled Components** (CSS-in-JS).
- **Testing React Components (User-Centric Testing):** Dùng **React Testing Library** để kiểm thử hành vi nhìn thấy bởi người dùng (click, loading states, cập nhật bất đồng bộ với `findBy*`/`waitFor`) thay vì kiểm tra chi tiết cài đặt nội bộ.

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Dùng `push()` hoặc `splice()` sửa trực tiếp mảng trong `useState`:** React so sánh tham chiếu mảng cũ/mới; nếu bạn mutate trực tiếp mảng gốc, tham chiếu không đổi nên UI **không re-render**. Hãy tạo mảng mới bằng spread `[...items, newItem]` hoặc `items.filter(...)`.
2. **Quên thuộc tính `key` duy nhất khi render bằng `.map()`:** Gây cảnh báo React và làm sai lệch thuật toán Reconciliation khi thêm/xóa/sắp xếp phần tử.
3. **Dùng `forEach()` thay vì `map()` trong JSX:** `forEach()` trả về `undefined` nên giao diện sẽ không hiển thị gì.
4. **Dùng tên thuộc tính CSS gạch ngang trong Inline Style:** Trong React inline style phải viết camelCase (`backgroundColor`, `fontSize`) thay vì `background-color`.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- Quản lý trạng thái trong Function Component bằng hook **`useState`** (`const [val, setVal] = useState(init)`).
- **Render danh sách động** luôn dùng **`array.map()`** kèm `key` duy nhất; **thu gọn/mở rộng (Conditional Rendering)** giúp giảm rối giao diện.
- **Virtual DOM** đồng bộ với Real DOM thông qua **Reconciliation**, chỉ cập nhật đúng phần thay đổi để tối ưu hiệu năng.
- Kiểm thử React hiện đại tập trung vào **trải nghiệm & hành vi người dùng** thay vì chi tiết nội bộ.
