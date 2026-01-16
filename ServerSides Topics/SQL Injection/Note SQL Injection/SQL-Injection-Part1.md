# SQL Injection
![image](https://hackmd.io/_uploads/B1OXSrTNWx.png)
Tấn công SQL Injection là loại lỗ hổng bảo mật cho phép tấn công can thiệp vào các truy vấn mà ứng dụng thực hiện đối với cơ sở dữ liệu của nó.
Kẻ tấn công có thể truy xuất. Điều này bao gồm dữ liệu thuộc về người dùng khác.
Có thể sửa đổi thông tin xóa dữ liệu gây ra những thay đổi lâu dài đối với nội dung hoặc hành vi lợi dụng
## Lỗi tấn công SQL Injection ở các phần khác nhau truy vấn
Xảy ra trong các lệnh `WHERE` , `INSERT`, `UPDATE`, `SELECT`
Chúng ta có thể sử dụng một cuộc tấn công tương tự để khiến ứng dụng hiển thị tất cả sản phẩm trong bất kì danh mục nào, bao gồm cả những thành phần họ không biết đến
```text=
http://hacker.com/products?category=Gifr'+OR+1=1-- -
```
Điều này sẽ dẫn đến truy vấn SQL sau:
```txt=
SELECT * FROM products WHERE category='GIFT' OR 1=1-- -
```
Truy vấn sửa đổi đã trả về tất cả các mục trong đó là category, Gifts OR 1=1 vì 1=1 là giá trị luôn đúng.
## Phá vỡ logic ứng dụng
Logic ứng dụng giả sử ứng dụng đăng nhập cho phép người dùng test, password: test ứng dụng sẽ kiểm tra truy vấn SQL sau:
```sql=
SELECT * FROM users WHERE username='test' AND password='test'
```
Bằng cách đó kẻ tấn công có thể sử dụng cú pháp để phá vỡ logic ứng dụng administrator-- - thì cú pháp sẽ trở thành
```sql=
SELECT * FROM users WHERE username='administrator-- -' AND password='test'
```
Lúc đó kết quả trả về người dùng với username=administrator để đăng nhập ADMIN
## Truy xuất dữ liệu từ các bảng cơ sở dữ liệu bằng UNION
Có thể sử dụng khóa UNION để thực hiện một SELECT truy vấn bổ sung và nối kết quả vào truy vấn ban đầu , được hiểu nó là cùng dữ liệu cùng số cột mới khớp
Giả sử dụng dụng thực thi truy vấn chứa dữ liệu do người dùng nhập `GIFTS`
```sql=
SELECT name, description FROM products WHERE category='GIFTS'
```
Kẻ tấn công có thể sử dụng UNION gửi dữ liệu đầu vào
```sql=
' UNION SELECT username, password FROM users-- -
```
Điều này khiến ứng dụng trả về tất cả tên người dùng và mật khẩu cùng với tên và mô tả sản phẩm.
## Các dạng lỗ hổng tấn công SQL ẩn
Kích hoạt lỗi, time blind, Kích hoạt ngoài băng tấn, Boolean đúng sai với các sự nhận biết khác nhau.
## Tấn công SQL Injection trong các ngữ cảnh khác nhau
Ơ SQL Injection có thể trang web sẽ nhận dữ liệu đầu vào ở định dạng JSON hoặc XML và sử dụng để truy vấn cơ sở dữ liệu
Sử dụng XML để mã hóa ký tự `S` trong `SELECT`
```xml=
<stock>
    <productID>123</productID>
    <storeId>123 &#x53;ELECT * FROM information_schema.tables</storeId>
</stock>
```
## Ngăn chặn
Tránh sử dụng nối chuỗi đầu vào và sử dụng lệnh prepare trong php để mã hóa ngăn chặn việc dữ liệu người dùng can thiệp cấu trúc truy vấn
Thiết lập danh sách trắng cho các giá trị đầu vào được phép. Sử dụng các logic khác nhau để đạt được hành vi mong muốn.
## Kiểm tra cơ sở dữ liệu trong các cuộc tấn công SQL Injection
### Truy vấn loại phiên bản cơ sở dữ liệu
Microsoft, MYSQL: **SELECT @@version**
Oracle: **SELECT * FROM v$version**

PostgreSQL: **SELECT version()**
## Liệt kê nội dung cơ sở dữ liệu
Hầu hết các loại cơ sở dữ liệu ngoại trừ Oracle đều có một tập hợp là lược đồ cơ sở dữ liệu hay còn gọi là lược đồ thông tin.
`information_schema.tables` để liệt kê bảng
`information_schema.columns` để liệt kê chi tiết cột của từng bảng riêng lẻ
## Liệt kê nội dung của cơ sở dữ liệu Oracle
Trong oracle có lệnh `all_tables` để liệt kê bảng cơ sở dữ liệu, còn liệt kê cột bằng truy vấn `all_tab_columns`
## Tấn công UNION
UNION nó cho phép thực hiện một hoặc nhiều lệnh `SELECT` vào truy vấn bổ sung thêm kết quả vào ban đầu
```sql=
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```
Kết quả truy vấn trả về a, b trong table 1 và c, d trong table 2
Điều kiện để UNION hoạt động:
> Các truy vấn riêng lẻ phải trả về cùng số lượng cột
> Các kiểu dữ liệu mỗi cột phải tương thích giữa các truy vấn riêng lẻ


