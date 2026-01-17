# Authentication vulnerabilities
Lỗ hổng xác thực này cho phép kẻ tấn công truy cập vào dữ liệu và chức năng nhạy cảm. Và có thể làm lộ thêm bề mặt tấn công cho các hình thức khai thác khác.
![image](https://hackmd.io/_uploads/H1LV-hDrbe.png)
## Xác thực là gì?
Xác thực là quá trình xác minh danh tính của người dùng hoặc của khách hàng.
Các trang web có nguy cơ bị tấn công bởi bất kỳ ai kết nối với Internet
Có 3 loại xác thực chính:
> Thông tin bạn biết -  chẳng hạn như password
> Thứ bạn sở hữu - Chẳng hạn như điện thoại hay mã bảo mật
> Những gì bạn là hoặc làm. - Các chỉ số sinh trắc học...

## Các lỗ hổng xác thực phát sinh như thế nào?
> Các cơ chế xác thực còn yếu vì chúng không đủ khả năng bảo vệ chống lại các cuộc tấn công vét cạn
> Lỗi logic hoặc lập trình kém trong quá trình triển khai khiến phá vỡ hệ thống xác thực
## Việc xác thực sẽ gây ra hậu quả gì?
Ảnh hưởng rất nghiêm trọng có thể bỏ qua quá trình xác thực hoặc tắn công bằng phương pháp vét cạn mật khẩu
Xâm phạm quyền riêng tư tài khoản người dùng khác
Ngay cả khi xâm nhập vào một tài khoản có quyền hạn thấp, kẻ tấn công vẫn có thể truy cập vào dữ liệu mà lẽ ra chúng không được phép có, chẳng hạn như thông tin kinh doanh nhạy cảm

## Chi tiết lỗ hổng
### Các lỗ hổng đăng nhập bằng mật khẩu
> Tấn công bằng vũ lực: Tấn công vét cạn (Brute-Force attack) là khi kẻ tấn công sử dụng phương pháp thử và sai để đoán thông tin đăng nhập hợp lệ của người dùng. Tự động hóa bằng cách sử dụng danh sách từ gồm tên người dùng và mật khẩu.
### Tấn công vét cạn tên người dùng
> Tên người dùng mã dễ đoán nếu chúng tuân theo một mẫu dễ nhận biết, chẳng hạn như địa chỉ Email. Rất phổ biến khi thấy tên doanh nghiệp định dạng <first_name>.lastname@somecompany.com và đôi khi các tài khoản có quyền hạn cao hơn như Administrator chẳng hạn.
### Tấn công vét cạn mật khẩu
> Điều này thường việc bắt buộc sử dụng mật khẩu có:
> Số lượng kí tự tối thiểu
> Sự kết hợp giữa chữ hoa và chữ thường
> Ít nhất một ký tự đặc biệt
### Liệt kê tên người dùng
> Kẻ tấn công có thể xem xét quá trình xem người dùng có thực sự hợp lệ hay không và đặc biệt chú ý đến bất kì sự khác biệt nào về:
> Mã trạng thái: Nếu một lần đoán trả về mã trạng thái khác, đây là dấu hiệu mạnh mẽ cho thấy tên người dùng là chính xác.
> Thông báo lỗi, Thời gian phản hồi: 

### Bảo vệ bằng vũ lực thô bạo có nhiều thiếu sót
Để ngăn chặn các cuộc tấn công vét cạn là:
> Khóa tài khoản mà người dùng từ xa đang cố gắng truy cập nếu họ đăng nhập không thành công quá nhiều lần
> Chặn địa chỉ IP của người dùng từ xa nếu họ thực hiện quá nhiều lần đăng nhập liên tiếp trong thời gian ngắn
Đôi khi thấy địa chỉ IP của mình bị chặn nếu đăng nhập không thành công quá nhiều lần. Trong một số hệ thống, bộ đếm số lần đăng nhập không thành công sẽ được đặt lại nếu chủ sỡ hữu IP đăng nhập thành công.
Điều này kẻ tấn công chỉ cần đăng nhập vào tài khoản của chúng sau mỗi vài lần thử để tránh đạt đến giới hạn này.
Bằng cách đó chúng ta chỉ cần chèn thông tin đăng nhập của kẻ tấn công vào danh sách khóa một cách đều đặn là đủ để khiến biện pháp phòng vệ gần như vô ích
## Khóa tài khoản 
Một trong số những cách mà trang web cố gắng ngăn chặn tấn công vét cạn mật khẩu là khóa tài khoản nếu đáp ứng kiểu như đăng nhập thất bại liên tiếp 
## Các lỗ hổng xác thực đa yếu tố
### Vượt qua xác thực 2 yếu tố
Đôi khi việc triển khai xác thực hai yếu tố bị lỗi đến mức có thể vượt qua hoàn toàn.
Nếu người dùng được yêu cầu nhập mật khâu trước, rồi sau đó được yêu cầu nhập mã xác minh trên một trang riêng biệt, thì người dùng đã ở trạng thái "Đã đăng nhập" trước khi họ nhập mã xác minh.
## Logic xác thực hai yếu tố bị lỗi
Đôi khi, lỗi logic trong xác thực 2 yếu tố dẫn đến việc sau khi người dùng hoàn tất bước đăng nhập đầu tiên, trang web không xác minh đầy đủ rằng cùng một người dùng đang được thực hiện bước 2
Ví dụ, người dùng đăng nhập bằng thông tin đăng nhập thông thường của họ ở bước đầu tiên như sau:
```HTTP
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com
...
username=carlos&password=qwerty
```
Sau đó họ được cấp một cookie liên quan đến tài khoản của mình, trước khi chuyển sang bước thứ 2 của quá trình đăng nhập
```HTTP
HTTP/1.1 200 OK
Set-Cookie: account=carlos

GET /login-steps/second HTTP/1.1
Cookie: account=carlos
```
Khi gửi mã xác minh, yêu cầu sử dụng cookie này để xác định người dùng đang cố gắng truy cập vào tài khoản nào
```HTTP
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos
...
verification-code=123456
```
Kẻ tấn công có thể đăng nhập bằng thông tin đăng nhập của chính mình nhưng sau đó thay đổi giá trị của `account` cookie thành bất kỳ tên người dùng nào khi gửi mã xác minh
```HTTP
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user
...
verification-code=123456
``


