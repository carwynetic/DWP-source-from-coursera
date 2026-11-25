# Module 4: Application — Dynamic Pages (React Components & End-to-End Flow)

> **Tư tưởng cốt lõi:** Hoàn thiện tầng giao diện người dùng động bằng **React** gồm 3 thành phần cốt lõi — **`Dealers.jsx`** (danh sách & lọc đại lý theo bang), **`Dealer.jsx`** (chi tiết đại lý & danh sách đánh giá kèm biểu tượng cảm xúc AI), và **`PostReview.jsx`** (biểu mẫu gửi đánh giá dành riêng cho người dùng đã đăng nhập) — kết nối trực tiếp với các Django Proxy APIs từ Module 3.

## 1. Kiến trúc 3 React Components chính & Định tuyến (`App.js`)

| Route React (`App.js`) | Component | API Django gọi tới | Hành vi phân quyền UI |
| --- | --- | --- | --- |
| `/dealers` | **`Dealers.jsx`** | `GET /djangoapp/get_dealers`<br>`GET /djangoapp/get_dealers/:state` | Hiển thị bảng toàn bộ đại lý + dropdown lọc theo `State`. **Nếu đã đăng nhập (`isLoggedIn`):** hiển thị thêm cột & nút **`Review Dealer` (`PostReview`)** |
| `/dealer/:id` | **`Dealer.jsx`** | `GET /djangoapp/dealer/:id`<br>`GET /djangoapp/reviews/dealer/:id` | Hiển thị tên, địa chỉ đại lý và thẻ đánh giá kèm **icon cảm xúc** (*positive / neutral / negative* do NLTK phân tích). **Nếu đã đăng nhập:** hiện link/nút **`Post Review`** |
| `/postreview/:id` | **`PostReview.jsx`** | `GET /djangoapp/dealer/:id`<br>`GET /djangoapp/get_cars`<br>`POST /djangoapp/add_review` | Form nhập nội dung đánh giá (**Review**), **Purchase Date**, chọn **Car Make & Model**, **Car Year** và nút **`Post Review`** |

## 2. Cơ chế đồng bộ State & Xử lý sự kiện trong React

### A. Lọc đại lý theo bang trong `Dealers.jsx`
- Sử dụng `useState` để lưu `dealersList` và tập hợp duy nhất các bang `states` (`Array.from(new Set(allDealers.map(d => d.state)))`).
- Khi người dùng thay đổi dropdown `<select onChange={(e) => filterDealers(e.target.value)}>`:
  - Nếu chọn `"All"` → gọi lại `/djangoapp/get_dealers`.
  - Nếu chọn bang cụ thể (vd `"Kansas"`) → gọi `/djangoapp/get_dealers/Kansas` và cập nhật `setDealersList(...)`.

### B. Hiển thị biểu tượng cảm xúc trong `Dealer.jsx`
```jsx
const sentiIcon = (sentiment) => {
  if (sentiment === "positive") return positive_icon;
  if (sentiment === "negative") return negative_icon;
  return neutral_icon;
};
```

### C. Gửi đánh giá mới & Tự động cập nhật (`PostReview.jsx`)
```javascript
const postReview = async () => {
  if (!model || !review || !date || !year) {
    alert("All details are mandatory");
    return;
  }
  const [makeChosen, modelChosen] = model.split(" ");
  const res = await fetch("/djangoapp/add_review", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: `${sessionStorage.getItem("firstname")} ${sessionStorage.getItem("lastname")}`.trim()
            || sessionStorage.getItem("username"),
      dealership: id,
      review,
      purchase: true,
      purchase_date: date,
      car_make: makeChosen,
      car_model: modelChosen,
      car_year: year,
    }),
  });
  const json = await res.json();
  if (json.status === 200) {
    window.location.href = `${window.location.origin}/dealer/${id}`;
  }
};
```

## 3. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Tên người dùng hiển thị `null null` khi đăng bài:** Nếu tài khoản superuser tạo bằng CLI không có `first_name`/`last_name`, `sessionStorage.getItem("firstname")` trả về chuỗi `"null"`; cần fallback sang `username` để hiển thị sạch sẽ.
2. **Gửi đánh giá thành công nhưng không thấy xuất hiện ngay:** Kiểm tra xem sau khi `POST /djangoapp/add_review` trả `200`, React có điều hướng lại `/dealer/:id` để fetch danh sách review mới nhất từ MongoDB và chạy lại Sentiment Analyzer hay chưa.
3. **Quên `npm run build` sau khi thêm `Dealers`, `Dealer`, `PostReview`:** Phải build lại bundle React trước khi kiểm thử trên Django server.

## 4. Điểm cốt lõi cần nhớ (Key Takeaways)

- Luồng trải nghiệm hoàn chỉnh của người dùng: Xem danh sách đại lý (`/dealers`) → Lọc theo bang → Xem chi tiết & sắc thái đánh giá (`/dealer/:id`) → Đăng nhập → Gửi đánh giá mới (`/postreview/:id`) → Thấy ngay đánh giá mới kèm nhãn cảm xúc xuất hiện.
- Kiểm soát hiển thị nút **`PostReview`** dựa trên trạng thái đăng nhập ở cả `Dealers.jsx` lẫn `Dealer.jsx`.
