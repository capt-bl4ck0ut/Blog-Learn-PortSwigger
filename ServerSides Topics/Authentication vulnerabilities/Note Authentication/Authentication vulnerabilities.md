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

