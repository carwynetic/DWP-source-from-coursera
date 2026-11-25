# Module 4: Practice, Final Project, and Submission and Evaluation

> **Tư tưởng cốt lõi:** Chuyển hóa toàn bộ kiến thức React, Component Composition, Hooks và Redux Toolkit thành hai ứng dụng Single-Page thực tế hoàn chỉnh — **Conference Expense Planner** (bài thực hành) và **Paradise Nursery Shopping Application** (dự án cuối khóa) — với kiến trúc Redux Slice quản lý giỏ hàng xuyên suốt các trang.

## 1. Practice Project: Conference Expense Planner

Bài thực hành đóng vai trò bước đệm kỹ thuật trước Final Project, xây dựng ứng dụng ước tính chi phí tổ chức hội nghị gồm 3 màn hình/luồng chính:
- **Landing Page:** Giới thiệu dịch vụ kèm nút chuyển sang trang chọn gói.
- **Product Selection Page:** Cho phép người dùng chọn số lượng **Phòng hội nghị (Venue/Rooms)**, **Thiết bị bổ sung (Add-ons)** và **Suất ăn (Meals)** — tự động tính toán chi phí theo thời gian thực bằng **Redux Toolkit slices**.
- **Summary Pop-up Modal:** Tổng hợp toàn bộ các hạng mục đã chọn thành bảng chi phí chi tiết và tổng tiền cuối cùng.

## 2. Final Project: Paradise Nursery Shopping Application

Dự án đánh giá cuối khóa xây dựng giao diện Front-End cho cửa hàng cây cảnh **Paradise Nursery** với đầy đủ luồng mua sắm thương mại điện tử gồm **3 trang chức năng** liên kết qua chung một **Redux Store**:

```text
Redux Store (store.js)
 └── cartSlice.jsx (items[], addItem, removeItem, updateQuantity)
        │
        ├── 1. Landing Page          -> Ảnh nền, tên thương hiệu, giới thiệu ngắn, nút "Get Started"
        ├── 2. Product Listing Page  -> Nhóm cây theo danh mục (≥ 3 nhóm), thẻ sản phẩm (ảnh, tên, giá, mô tả),
        │                               nút "Add to Cart" (tự disable & đổi chữ "Added to Cart" sau khi thêm)
        └── 3. Shopping Cart Page    -> Hiển thị từng sản phẩm đã chọn, tăng (+)/giảm (-) số lượng,
                                        nút Delete, tính thành tiền từng dòng & tổng giỏ hàng,
                                        nút "Continue Shopping" và "Checkout"
```

### Ánh xạ kiến trúc kỹ thuật cần đạt trong Final Project

| Yêu cầu chức năng | Giải pháp React + Redux Toolkit |
| --- | --- |
| **Thanh Header & Badge giỏ hàng đồng bộ** | Đọc tổng số lượng mặt hàng từ Redux Store qua `useSelector(state => state.cart.items)` và tính tổng bằng `.reduce((sum, item) => sum + item.quantity, 0)` |
| **Thêm sản phẩm vào giỏ hàng** | Dispatch action `addItem(plant)` từ `cartSlice`; lưu trạng thái `addedToCart[plant.name] = true` để vô hiệu hóa nút tránh bấm trùng |
| **Tăng / Giảm số lượng & Xóa mục** | Dispatch `updateQuantity({ name, quantity })`; nếu giảm từ `1` xuống `0` thì tự động dispatch `removeItem(name)` để không tồn tại mục số lượng 0 |
| **Tính tổng tiền (Subtotal & Grand Total)** | Chuyển chuỗi giá (vd `"$15"`) sang số `parseFloat(item.cost.substring(1))` rồi nhân `item.quantity`, cộng dồn bằng `.reduce()` |
| **Triển khai & Nộp bài** | Đẩy mã nguồn lên GitHub Repository công khai và xuất bản bản chạy thử trực tiếp bằng **GitHub Pages** (`vite.config.js` cấu hình đúng `base: "/<repo-name>/"`) |

## 3. Bẫy thường gặp khi nộp Final Project React

1. **Quên đổi chuỗi giá `"$15"` sang số trước khi nhân:** Dẫn đến kết quả `NaN` trên trang giỏ hàng. Luôn loại bỏ ký tự `$` và ép kiểu `parseFloat()` trước khi tính toán.
2. **Trang GitHub Pages trắng trơn (404 asset):** Nguyên nhân phổ biến là quên cấu hình thuộc tính `base` trong `vite.config.js` khớp với tên repository trên GitHub.
3. **Nút "Add to Cart" không kích hoạt lại khi xóa khỏi giỏ hàng:** Nếu chỉ lưu cờ `addedToCart` cục bộ trong component danh sách mà không đối chiếu trực tiếp với `cartItems` trong Redux Store, khi người dùng xóa sản phẩm trong giỏ và quay lại trang sản phẩm, nút vẫn bị khóa. **Giải pháp chuẩn:** Suy ra trạng thái đã thêm trực tiếp từ Redux Store: `cartItems.some(i => i.name === plant.name)`.

## 4. Liên kết lộ trình DWP301c

Hoàn thành Khóa 4, bạn đã nắm vững toàn bộ tầng **Front-End hiện đại (React + Redux Toolkit)**. Ở **Khóa 5 (Docker, Kubernetes & OpenShift)** và **Khóa 6 (Microservices & Serverless)**, bạn sẽ đóng gói ứng dụng Front-End và Back-End thành container để triển khai quy mô Cloud-Native, trước khi tích hợp toàn bộ trong **Khóa 7 (Full-Stack Capstone)**.
