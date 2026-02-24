# Kĩ thuật khai thác SSRF mù với Shellshock
Việc chỉ đơn thuần xác định một lỗ hổng SSRF ẩn có thể kích hoạt các yêu cầu HTTP ngoài băng tần không tự nó đã cung cấp đường dẫn đến khả năng khai thác. <br>
Vì chúng ta không thể xem phản hồi từ yêu cầu phía máy chủ, nên hành vi này không thể được sử dụng để khám phá nội dung trên các hệ thống mà máy chủ ứng dụng có thể truy cập. <br>
Chúng ta có thể quét mù không gian địa chỉ IP nội bộ, gửi các payload được thiết kế phát hiện các lỗ hổng đã biết. Nếu các payload đó cũng sử dụng các kỹ thuật ngoài băng tần ẩn, thì bạn có thể phát hiện ra một lỗ hổng nghiêm trọng trên một máy chủ nội bộ chưa được vá lỗi.
# Vượt qua bộ lọc SSRF thông qua chuyển hướng mở
Đôi khi có thể vượt qua các biện pháp phòng thủ dựa trên bộ lọc bằng cách kahi thác lõ hổng chuyển hướng đang mở.
Hãy tưởng tượng URL do người dùng gửi được kiểm tra nghiêm ngặt để ngăn chặn khai thác độc hại hành vi SSRF.
Tuy nhiên đôi khi ứng dụng lại xảy ra lỗ hổng cho phép chuyển hướng mở không an toàn và với URL bất kì bằng cách này kẻ tấn công thực hiện cuộc tấn công chèn payload giả sử như ứng dụng :
```payload
http://attacker.com?currentProductId=6&path=https://product.com
```
Lúc này kẻ tấn công có thể thực hiện lệnh chuyển hướng mở vào nội bộ hạ tầng như sau và có thể vào admin mà không cần 1 thông tin xác thực gì
```payload
http://attacker.com?currentProductId=6&path=https://127.0.0.1:80/admin
```
## SSRF với bộ lọc đầu vào dựa trên danh sách trắng
Một số ứng dụng chỉ cho phép nhập các giá trị khớp với danh sách trắng giá trị được cho phép. Bộ lọc có thể tìm kiếm sự trùng khớp ở đầu hoặc bên trong chuỗi nhập liệu <br>
Có thể vượt qua bộ loc này bằng cách khai thác các điểm không nhất quán trong quá trình phân tích cú pháp và xác thực tùy ý bằng phương pháp này:
Có thể dùng `@` để xác thực URL được coi như cặp xác thực `username:password`
```shell
http://attacker-host:fakepass@evils-host
```
Hoặc có thể sử dụng `#` để chỉ định một phần của URL.
```shell
https://attacker-host#expected-host
```
Có thể tận dụng hệ thống phân cấp đặt tên DNS để đưa thông tin cần thiết vào một tên DNS đủ điều kiện chúng ta kiểm soát.
```shell
https://expected-host.evil-host
```
Có thể mã hóa URL các ký tự để gây nhầm lẫn cho mã phân tích cú pháp URL. Điều này đặc biệt nếu mã thực hiện bộ lọc xử lý các ký tự được mã hóa URL khác với mã thực hiện yêu cầu HTTP ở phía máy chủ. <br>
Cũng có thể mã hóa kép các ký tự, một số máy chủ giải mã URL đệ quy đầu vào mà chúng nhận được, điều này có thể dẫn đến sai lệch.


