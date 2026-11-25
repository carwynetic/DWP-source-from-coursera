# Module 1: Getting Started with SQL & Relational Databases

> **Tư tưởng cốt lõi:** Cơ sở dữ liệu quan hệ (RDBMS) tổ chức dữ liệu có cấu trúc thành các bảng liên kết qua Primary Key & Foreign Key, đảm bảo tính toàn vẹn ACID và độc lập dữ liệu; SQL là ngôn ngữ chuẩn gồm DDL (định nghĩa cấu trúc) và DML (truy vấn & thao tác dữ liệu) để làm việc với RDBMS.

## 1. Bản chất của Data, Database và DBMS

- **Data (Dữ liệu):** Tập hợp các sự kiện thô dưới dạng chữ, số, hình ảnh — tài sản cốt lõi của mọi hệ thống (ngân hàng, thương mại điện tử, y tế).
- **Database (Cơ sở dữ liệu):** Kho lưu trữ dữ liệu có tổ chức, hỗ trợ nhập, lưu trữ, tìm kiếm, truy xuất và chỉnh sửa nhanh chóng, an toàn.
- **DBMS (Database Management System):** Tập hợp các chương trình phần mềm tạo và duy trì database, cung cấp cơ chế **querying** (truy vấn) để lọc và trích xuất thông tin. *(Lưu ý: Database là kho dữ liệu, DBMS là phần mềm quản lý kho đó — hay bị dùng lẫn trong giao tiếp nhưng khác bản chất.)*

## 2. RDBMS vs. NoSQL — So sánh phản biện & Lựa chọn kiến trúc

| Tiêu chí | Relational Database (RDBMS) | Non-relational Database (NoSQL — *Not Only SQL*) |
| --- | --- | --- |
| **Cấu trúc lưu trữ** | Bảng (tables) gồm hàng (rows/records) và cột (columns/attributes) theo schema chặt chẽ | Schema-less / linh hoạt (Key-Value, Document, Column-Family, Graph) |
| **Loại dữ liệu** | Dữ liệu có cấu trúc (structured data) | Structured, semi-structured và unstructured (Big Data, IoT, Social) |
| **Ngôn ngữ truy vấn** | SQL (chuẩn hóa, mạnh về `JOIN` đa bảng) | API riêng theo mô hình (một số hỗ trợ giao diện giống SQL) |
| **Giao dịch & Tin cậy** | **ACID-compliant** (Atomicity, Consistency, Isolation, Durability) | Thường ưu tiên mở rộng ngang (scale-out) & tính sẵn sàng cao |
| **Chi phí & Hạ tầng** | Hệ thống thương mại cao cấp đắt đỏ; mạnh trên vertical scale & Cloud DBaaS | Thiết kế chạy phân tán trên phần cứng phổ thông (commodity hardware) |
| **Ứng dụng tiêu biểu** | OLTP (giao dịch tần suất cao), Data Warehouse (OLAP), ngân hàng | Caching, giỏ hàng/e-commerce, time-series IoT, mạng xã hội |
| **Ví dụ phổ biến** | IBM Db2, PostgreSQL, MySQL, Oracle, SQL Server (Cloud: RDS, Cloud SQL, Azure SQL) | Redis, MongoDB, Cassandra, Neo4j |

### 4 mô hình NoSQL cốt lõi (biết điểm mạnh & giới hạn)

| Mô hình NoSQL | Cách lưu trữ | Phù hợp nhất | Không phù hợp khi | Ví dụ |
| --- | --- | --- | --- | --- |
| **Key-Value** | Cặp `key -> value` (số, chuỗi, JSON) | User session, preferences, in-memory cache, real-time recommendation | Cần truy vấn theo giá trị bên trong, quan hệ giữa các giá trị | Redis, Memcached, DynamoDB |
| **Document-based** | Mỗi bản ghi & dữ liệu liên quan nằm trong 1 document (JSON/BSON) | E-commerce, CRM, hồ sơ y tế, analytics | Giao dịch đa thao tác phức tạp, tìm kiếm quan hệ chéo phức tạp | MongoDB, CouchDB, Cloudant, DocumentDB |
| **Column-based** | Nhóm ô theo **column family** liên tiếp trên đĩa | Ghi nặng (heavy write), time-series, thời tiết, cảm biến IoT | Truy vấn phức tạp hoặc mẫu truy vấn thay đổi liên tục | Apache Cassandra, HBase |
| **Graph-based** | **Nodes** (dữ liệu) nối bằng **Edges** (quan hệ) | Mạng xã hội, chống gian lận (fraud detection), sơ đồ mạng, access management | Phân tích khối lượng giao dịch khổng lồ (high-volume analytics) | Neo4j, CosmosDB |

## 3. Thiết kế cơ sở dữ liệu: ER Model → Relational Table

- **Ưu điểm lớn nhất của Relational Model:** Đảm bảo **Data Independence** (độc lập dữ liệu) ở cả 3 mức: *Logical data independence*, *Physical data independence*, và *Physical storage independence*.
- **Entity-Relationship (ER) Model** là công cụ thiết kế trực quan (ERD) trước khi ánh xạ sang bảng:
  - **Entity (Thực thể — hình chữ nhật):** Đối tượng độc lập (danh từ: `Book`, `Author`, `Borrower`) → trở thành **Table**.
  - **Attribute (Thuộc tính — hình oval):** Đặc tính của thực thể (`title`, `edition`, `ISBN`) → trở thành **Columns**.
  - **Kiểu dữ liệu phổ biến:** `CHAR(n)` (độ dài cố định, vd mã tỉnh `CHAR(2)` hay `ISBN`), `VARCHAR(n)` (độ dài biến thiên, vd `title`), `INT`/`BIGINT`/`DECIMAL`, `DATE`/`TIMESTAMP`.
  - **Primary Key (PK):** Định danh duy nhất từng dòng (tuple/row), chống trùng lặp dữ liệu và làm điểm neo liên kết.
  - **Foreign Key (FK):** Cột (hoặc tập cột) tham chiếu đến PK của bảng khác để tạo liên kết giữa các bảng.

## 4. Phân loại lệnh SQL: DDL vs. DML

### A. DDL (Data Definition Language) — Định nghĩa & thay đổi cấu trúc bảng

```sql
-- 1. Tạo bảng kèm khóa chính và ràng buộc NOT NULL
CREATE TABLE author (
    author_id CHAR(2) PRIMARY KEY NOT NULL,
    lastname  VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    email     VARCHAR(40),
    city      VARCHAR(15),
    country   CHAR(2)
);

-- 2. Thay đổi cấu trúc bảng (chú ý: ALTER TABLE không dùng ngoặc đơn bọc danh sách)
ALTER TABLE author ADD COLUMN telephone_number BIGINT;
ALTER TABLE author ALTER COLUMN telephone_number SET DATA TYPE CHAR(20);
ALTER TABLE author DROP COLUMN telephone_number;

-- 3. Xóa toàn bộ dữ liệu nhanh (giữ lại cấu trúc bảng, không thể hoàn tác)
TRUNCATE TABLE author IMMEDIATE;

-- 4. Xóa luôn cả bảng lẫn dữ liệu bên trong
DROP TABLE author;
```

### B. DML (Data Manipulation Language) — Đọc & thao tác dữ liệu (CRUD)

```sql
-- CREATE: Thêm dòng mới (số lượng giá trị trong VALUES phải khớp số cột)
INSERT INTO author (author_id, lastname, firstname, email, city, country)
VALUES ('A1', 'Chong', 'Raul', 'rfc@ibm.com', 'Toronto', 'CA');

-- READ: Truy vấn với WHERE (predicate đánh giá True / False / Unknown)
SELECT book_id, title
FROM book
WHERE book_id = 'B1';

-- Các hàm & mệnh đề tiện ích đi kèm SELECT
SELECT COUNT(*) FROM medals WHERE country = 'CANADA';
SELECT DISTINCT country FROM medals WHERE medaltype = 'GOLD';
SELECT * FROM medals WHERE year = 2018 LIMIT 5;

-- Sắp xếp kết quả (mặc định ASC; có thể chỉ định tên cột hoặc số thứ tự cột trong SELECT)
SELECT title, pages FROM book ORDER BY title DESC;
SELECT title, pages FROM book ORDER BY 2 ASC;

-- Nhóm & lọc nhóm
SELECT country, COUNT(*) AS total
FROM medals
GROUP BY country
HAVING COUNT(*) > 1;

-- UPDATE: Cập nhật bản ghi thỏa điều kiện
UPDATE author
SET lastname = 'KATTA', firstname = 'LAKSHMI'
WHERE author_id = 'A2';

-- DELETE: Xóa bản ghi thỏa điều kiện
DELETE FROM author
WHERE author_id IN ('A2', 'A3');
```

### C. Kết hợp đa bảng với `JOIN`

`JOIN` ghép các dòng từ 2 hoặc nhiều bảng thông qua cột chung (thường là PK của bảng này nối với FK của bảng kia):

```sql
-- INNER JOIN: Chỉ lấy các dòng khớp ở cả 2 bảng (phần giao)
SELECT b.title, a.lastname
FROM book b
INNER JOIN author a ON b.author_id = a.author_id;

-- Nối 3 bảng liên tiếp (Borrower -> Loan -> Copy)
SELECT br.name, l.loan_date, c.copy_id
FROM borrower br
INNER JOIN loan l ON br.borrower_id = l.borrower_id
INNER JOIN copy c ON l.copy_id = c.copy_id;
```

| Loại JOIN | Kết quả trả về |
| --- | --- |
| `INNER JOIN` | Chỉ các dòng có giá trị khớp ở cả hai bảng |
| `LEFT JOIN` | Toàn bộ bảng trái + các dòng khớp ở bảng phải (`NULL` nếu không khớp) |
| `RIGHT JOIN` | Toàn bộ bảng phải + các dòng khớp ở bảng trái |
| `FULL JOIN` | Toàn bộ các dòng từ cả hai bảng bất kể có khớp hay không |

## 5. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Quên `WHERE` trong `UPDATE` hoặc `DELETE`:** Nếu thiếu mệnh đề `WHERE`, **toàn bộ các dòng trong bảng** sẽ bị ghi đè hoặc xóa sạch!
2. **`DELETE` vs. `TRUNCATE` vs. `DROP`:**
   - `DELETE FROM t` (DML): xóa từng dòng theo điều kiện `WHERE`, chậm hơn nếu xóa cả bảng.
   - `TRUNCATE TABLE t IMMEDIATE` (DDL): xóa sạch mọi dòng tức thì, giữ nguyên cấu trúc bảng, không hoàn tác được.
   - `DROP TABLE t` (DDL): xóa mất luôn cả bảng lẫn dữ liệu.
3. **Đổi kiểu dữ liệu cột đang có dữ liệu (`ALTER COLUMN`):** Chuyển từ `CHAR` sang kiểu số sẽ báo lỗi nếu cột đã chứa ký tự không phải số (vd dấu `-`, `+`, `()`).
4. **Giới hạn của RDBMS:** Không phù hợp phân tích sâu dữ liệu bán cấu trúc/phi cấu trúc; di chuyển giữa 2 RDBMS đòi hỏi schema & kiểu dữ liệu tương thích; trường dữ liệu có giới hạn độ dài cố định.
5. **Chèn nhiều dòng trong SQLite:** Một số RDBMS hỗ trợ chèn nhiều bộ `VALUES (...), (...)` trong 1 lệnh `INSERT`, nhưng phiên bản SQLite cổ điển trong bài giảng yêu cầu lưu ý chèn từng dòng khi tương thích.

## 6. Điểm cốt lõi cần nhớ (Key Takeaways)

- 5 lệnh SQL nền tảng nhất: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
- `WHERE` luôn đòi hỏi một **predicate** (biểu thức trả về True, False hoặc Unknown) với các toán tử `=`, `>`, `<`, `>=`, `<=`, `<>`.
- Thứ tự cột hiển thị trong Result Set luôn tuân theo đúng thứ tự bạn liệt kê sau `SELECT`.
- RDBMS thắng thế ở **ACID + JOIN + OLTP**; NoSQL thắng thế ở **Schema linh hoạt + Scale-out phân tán + Big Data**.
