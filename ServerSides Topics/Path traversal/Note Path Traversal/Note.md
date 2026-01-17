# Path Traversal
Ở phần này tôi sẽ giải thích cách hoạt động :
> Thuật toán duyệt đường đi sẽ ra sao?
> Cách thực hiện các cuộc tấn công vượt đường dẫn ra sao và vượt qua các chướng ngại vật thường gặp
> Cách ngăn chặn duyệt đường dẫn tùy ý
![alt text](./HinhANh/hinh1.png)
## Duyệt đường dẫn là gì?
Là quá trình là cuộc tấn công duyệt thư mục, các lỗ hổng này cho phép duyệt đọc tập tin tùy ý ở bên trong hệ thống hay máy chủ.
> Có thể bao gồm mã và dữ liệu người dùng
> Thông tin đăng nhập các hệ thống máy chủ
> Các tập tin hệ điều hành nhạy cảm
## Đọc tập tin tùy ý thông qua duyệt đường dẫn 
Hãy tưởng tượng ta có đường dẫn như sau
```html
<img src="/loadImage?filename=2.png">
```
URL này `loadImage` nhận một param filename tham số và trả về hình ảnh chúng ta. Các tệp hình ảnh thường nằm ở `/var/www/images` và nói cách khác ứng dụng sẽ đọc đường dẫn `/var/www/images/2.png`
Bằng cách k có sự lọc đầu vào kẻ tấn công có thể tiến hành duyệt thư mục như sau `/var/www/images/../../../etc/passwd` khi đó sẽ tới thư mục root có thể đọc tập tin nhạy cảm tùy ý.
## Những trỡ ngại khi duyệt đường dẫn là gì?
Nhiều ứng dụng đặt dữ liệu nhập từ người dùng vào đường dẫn tệp tin và triển khai các biện pháp phòng chống tấn công duyệt thư mục
Các biện pháp này thường có thể bỏ qua bằng cách đọc đường đẫn gốc tuyệt đối chẳng hạn như `filename=/etc/passwd`
Có thể sử dụng chuỗi duyệt lồng nhau, chẳng hạn như `....//` để bypass
Có nhiều kỹ thuật bypass khác nhau nữa.
Đôi khi ứng dụng có thể yêu cầu tên tệp do người dùng cung cấp phải bắt đầu bằng thư mục gốc dự kiến, chẳng hạn như `/var/www/images` và kẻ tấn công có thể dưa chuỗi duyệt
`filename=/var/www/images/../../../etc/passwd`
## Bypass sử dụng bytenull
Một ứng dụng có thể yêu cầu tên tệp do người dùng cung cấp phải kết thúc bằng phần mở rộng tệp dự kiến, chẳng hạn như .png
có thể sử dụng một byte null để kết thúc đường dẫn tệp trước phần mở rộng bắt buộc. Ví dụ: `filename=../../../etc/passwd%00.png`
## Cách ngăn chặn tấn công duyệt đường dẫn
> Xác thực dữ liệu người dùng nhập vào trước khi xử lý. Tốt nhất là nên so sánh dữ liệu người dùng nhập và danh sách các giá trị được cho phép.
> Sau khi xác thực dữ liệu đầu vào, hãy thêm dữ liệu đó vào thư mục gốc và sử dụng API hệ thống tên tệp của nền tảng để chuẩn hóa đường dẫn
> một ví dụ về đoạn mã Java đơn giản để xác thực đường dẫn chính tắc của một tệp dựa trên dữ liệu người dùng nhập vào:

```java
File file = new File(BASE_DIRECTORY, userInput);
if (file.getCanonicalPath().startWiith(BASE_DIRECTORY)){
    // process file
}
```
