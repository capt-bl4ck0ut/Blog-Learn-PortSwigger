# Insecure Deserialization
Ở module này chúng ta sẽ tìm hiểu đến việc giải mã dữ liệu không an toàn và mô tả các trang web dễ bị tấn công nghiêm trọng. <br>
Cụ thể và giải mã dữ liệu trong PHP, Ruby và Java. 
![alt text](image.png)
## serialization là gì?
Tuần tự hóa là quá trình chuyển đổi các cấu trúc dữ liệu phức tạp chẳng hạn các đối tượng các trường của chúng thành định dạng phẳng hơn dưới một luồng byte. <br>
> Ghi dữ liệu phức tạp vào bộ nhớ giữa các tiến trình, tệp hoặc cơ sở dữ liệu <br>
> Gửi đữ liệu phức tạp <br>
| Lưu ý: <br>
KHi tuần tự hóa một đối tượng trạng thái của nó cũng được lưu giữ. Nói cách khác các thuộc tính của đối tượng được bảo toàn, cùng với các giá trị được gán cho chúng <br>
## Serialization vs deserialization
Chúng ta có thể được hiểu như sau tuần tự hóa là quá trinfhh chuyển đổi các đối tượng thành các luồng byte để lưu vào cơ sở dữ liệu và ngược lại giải mã dữ liệu là quá trình khôi phục luồng byte về trạng thái đối tượng ban đầu.
![alt text](image-1.png)
## Giải mã dữ liệu không an toàn là sao?
Là giải mã dữ liệu không an toàn xay ra khi dữ liệu do người dùng kiểm soát được giải mã bởi một trang web.<br>
Và điều này tiềm ẩn nguy cơ cho phép kẻ tấn công thao túng các đối tượng đã được mã hóa để truyền dữ liệu độc hại vào ứng dụng.
## Root-cause dẫn đến giải mã dữ liệu không an toàn hệ thống
Hệ thống luôn tin tưởng đầu vào của người dùng và nên được giải mã. Không xác thực hoặc làm sạch dữ liệu để xử lý mọi trường hợp có thể xảy ra. <br>
Các lỗ hổng cũng có thể phát sinh vì các đối tượng được giải mã thường được cho là đáng tin cậy. Đặc biệt khi sử dụng các ngôn ngữ có định dạng tuần tự hóa nhị phân.
## Tác động của việc giải mã dữ liệu không an toàn
Nó xảy ra rất nghiêm trọng nó tạo ra điểm yếu giúp mở rộng đáng kể bề mặt tấn công. Cho phép kẻ tấn công tái sử dụng mã ứng dụng hiện có dẫn đến thực thi mã từ xa RCE hoặc leo thang đặc quyền truy cập tệp tùy ý và các cuộc tấn công DDOS
## Cách khai thác các lỗ hổng giải mã dữ liệu không an toàn
### Cách nhận biết quá trình giải mã dữ liệu không an toàn
> Việc xác định lỗi giải mã dữ liệu không an toàn tương đối đơn giản bất kể bạn đang thực hiện kiểm thử hộp trắng hay hộp đen. <br>
> Trong quá trình kiểm toán, bạn nên xem xét tất cả dữ liệu được truyền vào trang web và cố gắng xác định bất kỳ dữ liệu nào trông giống như dữ liệu được tuần tự hóa. Dữ liệu được tuần tự hóa có thể được xác định tương đối dễ dàng nếu bạn biết định dạng mà các ngôn ngữ khác nhau sử dụng. Trong phần này, chúng ta sẽ trình bày các ví dụ về tuần tự hóa trong cả PHP và Java. Sau khi xác định được dữ liệu được tuần tự hóa, bạn có thể kiểm tra xem mình có thể kiểm soát nó hay không. <br>
## Định dạng tuần tự hóa PHP
PHP sử dụng định dạng chuỗi dễ đọc đối với con người trong đó các chữ cái đại điện cho từng kiểu dữ liệu và độ dài của mỗi phần tử. 
```php
$user->name = "carlos";
$user->isLoggin = true;
```
Khi được tuần tự hóa đối tượng sẽ như thế này
```php
O:4:"User":2:{s:4:"name":s:6:"carlos";s:10:"isLoggedIn":b:1;}
```
Điều này được hiểu như sau: <br>
> O:4:"User" -> Mỗi đối tượng có tên lớp gồm 4 ký tự "User" <br>
> 2 -> Đối tượng có 2 thuộc tính <br>
> s:4:"name":s:6:"carlos";s:10:"isLoggedIn" được hiểu là số lượng từng string <br>
> b: 1 -> Được hiểu như giá trị boolean true or false <br>
Các phương thức gốc của PHP để tuần tự hóa dữ liệu là `<string>` `serialize()` và `<string>` `unserialize()` <br>
## Định dạng tuần tự hóa Java
Định dạng Java sử dụng định dạng tuần tự hóa nhị phân và các đối tượng Java được tuần tự hóa luôn bắt đầu bằng cùng một nhóm byte được mã hóa `ac ed` dạng thập lục phân và `rO0 Base64` <br>
Hàm tuần tự hóa Java `java.io.Serializable` đều có thể tuần tự hóa và giải tuần tự hóa. `readObject()` phương thức này dùng để đọc và giải tuần tự hóa dữ liệu từ đối tượng `InputStream`.
### Sửa đổi kiểu dữ liệu
Logic dựa trên PHP đăc biệt dễ bị tổn thương bởi toán tử so sánh lỏng leo (`==`) khi so sánh các kiểu dữ liệu khác nhau. <br>
Giả sử so sánh giữa 1 số nguyên và chuỗi như sau: 
```
5 == "5"
```
Lúc này `PHP 7.x` trở xuống phiên bản cũ nó có lỗ hổng chuyển đổi chuỗi thành 1 số nguyên có nghĩa `5=5 -> true`
## Sử dụng chức năng của ứng dụng
Đôi khi kiểm tra giá trị thuộc tính, chức năng của trang web cũng cs thể thực hiện được thao tác nguy hiểm trên dữ liệu từ một đối tượng đã được giải mã.
Giả sử như chức năng xóa người dùng của trang web bằng cách truy cập đường dẫn tệp <br>
```php
$user->image_location
```
Nếu ảnh được tạo từ một đối tượng tuần tự hóa kẻ tấn công có thể khai thác lỗ hổng bằng cách truyền vào đối tượng sửa đổi và đặt đường dẫn `image_location` độc hại.
## Phương pháp ma thuật
Phương pháp ma thuật là một tập hợp con đặc biệt của các phương thức mà chúng ta không cần gọi rõ ràng <br>
Các nhà phát triển có thể thêm các phương thức ma thuật vào lớp để xác định được trước đoạn mã nào sẽ được thực thi khi sự kiện xảy ra. <br>
Theo tôi biết có tất cả `17 magic` và phổ biến PHP là `component()` `__constructor` được gọi bất cứ khi nào đối tượng của lớp được khởi tạo và `component()` của Python `__init__`. Thông thường các phương thức ma thuật như vậy sử dụng để khởi tạo các thuộc tính của đối tượng.
![alt text](image-2.png)
```text
Warning
If type declarations are used in the definition of a magic method, they must be identical to the signature described in this document. Otherwise, a fatal error is emitted. Prior to PHP 8.0.0, no diagnostic was emitted. However, __construct() and __destruct() must not declare a return type; otherwise a fatal error is emitted.
```
Quan trọng một số ngôn ngữ có các phương thức đặc biệt tự động trong quá trình giải mã dữ liệu. `unserialize()`
