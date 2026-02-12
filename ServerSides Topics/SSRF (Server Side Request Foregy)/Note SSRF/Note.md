# SSRF (Server Side Requests Foregy)
Ở modul này mình sẽ giải thích và học SSRF là gì mô tả một số cách thức tấn công phổ biến.
## SSRF 
SSRF là gì? Là một tấn công giả mạo yêu cầu phía máy chủ là một máy chủ web thực hiện các yêu cầu đến một vị trí không mong muốn.
Trong một cuộc tấn công SSRF điển hình, kẻ tấn công có thể khiến máy chủ kết nối với các dịch vụ nội bộ trong cơ sở hạ tầng của ứng dụng. Rò rỉ dữ liệu nhạy cảm chẳng hạn như thông tin xác thực.
![alt text](image.png)
## Attack SSRF xảy ra hậu quả như nào?
SSRF thành công thường dẫn đến hành động trái phép hoặc truy cập dữ liệu trong tổ chức mà chúng không được cho phép.
Điều này xảy ra lỗ hổng SSRF cho phép kẻ tấn công thực hiện các lệnh tùy ý.
Lỗ hổng SSRF gây ra kết nối đến các hệ thống bên ngoài của bên thứ ba có thể dẫn đến các cuộc tấn công độc hại tiếp theo.
## Các cuộc tấn công SSRF phổ biến
### Tấn công SSRF vào máy chủ
Trong cuộc tân scoong SSRF nhằm vào máy chủ kẻ tấn công khiến thực hiện yêu cầu HTTP trở lại máy chủ đang lưu trữ ứng dụng đó.
Thông qua giao diện mạng loopback Điều này thường liên quan đến việc cung cấp URL với tên máy chủ như `127.0.0.1` hay `localhost` một tên thường được dùng cho máy chủ.
> Ví dụ, hãy tưởng tượng một ứng dụng mua sắm cho phép người dùng xem một mặt hàng có còn hàng tại một cửa hàng cụ thể hay không. Để cung cấp thông tin tồn kho, ứng dụng phải truy vấn nhiều API REST phía máy chủ. Ứng dụng thực hiện điều này bằng cách truyền URL đến điểm cuối API phía máy chủ có liên quan thông qua yêu cầu HTTP phía giao diện người dùng. Khi người dùng xem trạng thái tồn kho của một mặt hàng, trình duyệt của họ sẽ thực hiện yêu cầu sau: <br>
```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://stock.weliketoshop.net:8080/product/stock/check%3FproductId%3D6%26storeId%3D1
```
Điều này khiến máy chủ thực hiện yêu cầu HTTP được chỉ định và trả về thông tin người dùng bằng cách này kẻ tấn công có thể truyeefnf đối số được chỉ định một URL cục bộ trên máy chủ truy cập vào /admin
```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://localhost/admin
```
Máy chủ sẽ lấy nội dung của `/admin` URL và trả về cho người dùng
![alt text](image-1.png)
### Tấn công SSRF nhằm vào các hệ thống phụ trợ khác.
Chúng ta cùng tưởng tượng một giao diện quản trị tại URL máy chủ `https://192.168.0.68/admin`. Kẻ tấn công có thể gửi yêu cầu sau để khai thác lỗ hổng SSRF và truy xuất vào giao diện quản trị.
```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://192.168.0.68/admin
```
## Vượt qua các biện pháp phòng thủ SSRF phổ biến
### SSRF với bộ lọc đầu vào dựa trên danh sách đen
![alt text](image-2.png)
### SSRF với bộ lọc đầu vào dựa trên danh sách trắng
Đặc tả URL chứa một số tính năng có thể bị bỏ qua khi URL thực hiện phân tích cú pháp và xác thực tùy ý bằng phương pháp này:
> Có thể nhúng thông tin xác thực vào URL trước tên máy chủ bằng cách sử dụng ký tự `@` giả sử như `http://attacker:fakepassword@evil-host` <br>
> Có thể sử dụng ký tự `#` để chỉ định một phần của URL. Giả sử như : `http://attacker.com#expect-host` <br>
> Bạn có thể tận dụng hệ thống phân cấp đặt tên DNS để đưa thông tin cần thiết vào một tên DNS đủ điều kiện mà bạn kiểm soát. Ví dụ: `https://expected-host.evil-host` <br>
Có thể mã hóa URL các ký tự để gây nhầm lẫn cho mã phân tích cú pháp URL. Điều này đặc biệt hữu ích nếu mã thực hiện bộ lọc xử lý các ký tự được mã hóa URL khác với mã thực hiện yêu cầu HTTP ở phía máy chủ. <br>
Bạn cũng có thể thử mã hóa kép các ký tự; một số máy chủ giải mã URL đệ quy đầu vào mà chúng nhận được, điều này có thể dẫn đến những sai lệch hơn nữa. <br>
### Vượt qua bộ lọc SSRF thông qua chuyển hướng mở
Đôi khi chúng ta có thể vượt qua các biện pháp phòng thủ dựa trên bộ lọc bằng cách khai thác lỗ hổng chuyển hướng mở. 
Đôi khi người dùng gửi được kiểm tra nghiêm ngặt chặn việc khai thác độc hại hành vi SSRF. Tuy nhiên ứng dụng có các URL được cho phép lại chứa một lỗ hổng chuyển hướng mở. Và nếu API được sử dụng để thực hiện yêu cầu HTTP phía máy chủ hỗ trợ chuyển hướng và chúng ta có thể tạo URL thỏa mãn bộ lọc.
```
/product/nextProduct?currentProductId=6&path=http://evil-user.net
```
Trả về một liên kết
```
http://evil-user.net
```
Và chúng ta có thể lợi dụng nó để truy cập vào trang quản trị
## Tìm kiếm bề mặt tấn công tiềm ẩn cho các lỗ hổng SSRF
Với các yêu cầu tham số URL
### URL một phần trong yêu cầu
### URL trong các định dạng dữ liệu
Chẳng hạn như thông qua tệp XML có thể khai thác XXE kèm SSRF thông qua tiêu đề HTTP.
### SSRF thông qua tiêu đề Referer
Thường tiêu đề Referer dùng để xác định theo dõi khách truy cập. Thông thường, phần mềm phân tích sẽ truy cập bất kỳ URL bên thứ ba nào xuất hiện trong tiêu đề Referer. Thường xem xét trang web nào giới thiệu, bao gồm cả văn bản neo được sử dụng các liên kết đến. Do đó, tiêu đề Referer thường là bề mặt tấn công cho lỗ hổng SSRF.
### Blind SSRF là gì
Tức là kiểu như lỗ hổng SSRF mù phát sinh khi ứng dụng có thể bị tác động thông qua gửi yêu cầu HTTP đến máy chủ phụ trợ và không nhận được phản hồi trực tiếp lại .
### Tìm và khai thác lỗ hổng SSRF ẩn
Để phát hiện các lỗ hổng SSRF ẩn là sử dụng các kỹ thuật ngoài băng tần (OAST) kích hoạt một yêu cầu HTTP đến một hệ thống bên ngoài do kẻ tấn công kiểm soát.
