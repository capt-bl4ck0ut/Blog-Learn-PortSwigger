# Access control vulnerabilities and privilege escalation
Ở modul này sẽ nói đến các kĩ thuật
> Leo thang đặc quyền <br>
> Các loại lỗ hổng bảo mật có thể phát sinh liên quan đến kiểm soát truy cập <br>
> Làm thế nào để ngăn ngừa các lỗ hổng bảo mật trong kiểm soát truy cập <br>
## Kiểm soát truy cập là gì?
Kiểm soát truy cập là kiểu như áp đặt người dùng hoặc đối tượng được phép thực hiện hành động hoặc truy cập tài nguyên.
> Xác thực: GIúp người dùng nhận biết rằng họ chính là người mà họ tự xưng <br>
> Quản lý phiên: Xác định những yêu cầu HTTP tiếp theo nào đang được thực hiện bởi cùng một người  <br>
> Kiểm soát truy cập: Xác định xem người dùng có được phép cố gắng truy cập vào các tài nguyên trái phép hay không <br>
Lỗi kiểm soát truy cập rất phổ biến và thường gây ra lỗ hổng bảo mật nghiêm trọng.
![alt text](image.png)
## Kiểm soát truy cập theo chiều dọc
Kiểm soát truy cập theo chiều dọc là các cơ chế hạn chế quyền truy cập vào các chức năng nhạy cảm đối với các loài người cụ thể.
Với cơ chế kiểm soát truy cập theo chiều dọc, các loài người người dùng khác nhau sẽ có quyền truy cập vào các chức năng ứng dụng khác nhau.
## Kiểm soát truy cập theo chiều ngang
Kiểm soát truy cập theo chiều ngang là các cơ chế quyền hạn quyền truy cập vào tài nguyên cho những người dùng cụ thể.
Với cơ chế kiểm soát truy cập ngang, người dùng khác nhau có quyền  truy cập vào một tập hợp con tài nguyên cùng loại.
> Chẳng hạn như một ứng dụng ngân hàng sẽ cho phép người dùng xem giao dịch và thực hiện thanh toán của họ nhưng không cho phép truy cập vào tài nguyên của bất kỳ người dùng nào khác <br>
## Các lỗi kiểm soát truy cập
Lỗ hổng xảy ra người dùng có thể thực hiện truy cập trái phép thực hiện các hành động mà họ không được phép
### Leo thang đặc quyền theo chiều dọc
Nếu người dùng có thể truy cập vào các chức năng mà họ không được phép truy cập thì đó là leo thang đặc quyền theo chiều dọc
#### Chức năng không được bảo vệ
Leo thang đặc quyền theo chiều dọc phát sinh khi một ứng dụng không thực thi bất kỳ biện pháp bảo vệ nào cho các chức năng nhạy cảm
Một trang web có thể lưu trữ các chức năng nhạy cảm tại URL sau:
```http
https://example.com/admin
```
Thông tin có thể truy cập bởi tất cả người dùng nào.
Có thể lộ các enpoint như ở `robots.txt, sitemap.xml....` kẻ tấn công có thể sử dụng chức năng vét cạn 
Một ứng dụng lưu trữ:
```http
https://insecure-website.com/administrator-panel-yb556
```
Điều này đôi khi ứng dụng URL bị tiết lộ trong mã Javascript
```js
<script>
	var isAdmin = false;
	if (isAdmin) {
		...
		var adminPanelTag = document.createElement('a');
		adminPanelTag.setAttribute('href', 'https://insecure-website.com/administrator-panel-yb556');
		adminPanelTag.innerText = 'Admin panel';
		...
	}
</script>
```
## Phương pháp kiểm soát truy cập dựa trên tham số
> Một cánh đồng ẩn <br>
> Một chiếc bánh quy <br>
> Một tham số chuỗi truy vấn được thiết lập sẵn <br>
Ứng dụng đưa ra quyết định kiểm soát truy cập dựa trên giá trị được gửi vào. Ví dụ:
```http
https://insecure-website.com/login/home.jsp?admin=true <br>
https://insecure-website.com/login/home.jsp?role=1
```
## Lỗi kiểm soát truy cập do cấu hình nền tảng không chính xác.
Một ứng dụng thực thi kiểm soát truy cập ở lớp nền tảng. Chúng lafmd dược điều này bằng cách hạn chế quyền truy cập vào các URL và phương thức HTTP cụ thể dựa trên vai trò của người dùng.
Quy tắc cấu hình:
```txt
DENY: POST, /admin/deleteUser, managers
```
Nó chặn truy cập POST nhưng chúng ta có thể bỏ qua bằng cách hgi đè tiêu dề URL chẳng hạn như : `X-Original-URL, X-Rewrite-URL` ứng dụng cho phép ghi đề URL thì có thể vượt qua các biện pháp
```HTTP
POST / HTTP/1.1
X-Original-URL: /admin/deleteUser
...
```
## Lỗi kiểm soát truy cập do sự không khơp URL
Các trang web có thể khác nhau về mức độ nghiêm ngặt trong việc khớp đường dẫn của yêu cầu đến với một điểm cuối được xác định. Ví dụ, chúng có thể chấp nhận việc viết hoa không nhất quán, vì vậy yêu cầu tới `/ADMIN/DELETEUSER` vẫn có thể được ánh xạ đến `/admin/deleteUser` điểm cuối đó
Những sai lệch tương tự có thể phát sinh nếu các nhà phát triển sử dụng framework Spring đã bật `useSuffixPatterMathch` tùy chọn Điều này cho phép các đường dẫn có phần mở rộng tệp tùy ý được ánh xạ tới một điểm cuối tương đương không có phần mở rộng tệp. Nói cách khác, yêu cầu tới `/admin/deleteUser.anything` tới `/admin/deleterUser` Trước phiên bản Spring 5.3, tùy chọn này được bật theo mặc định.

Trên các hệ thống khác, bạn có thể gặp phải sự khác biệt trong việc liệu /admin/deleteUser và /admin/deleteUser/có được coi là các điểm cuối riêng biệt hay không. Trong trường hợp này, bạn có thể bỏ qua các kiểm soát truy cập bằng cách thêm dấu gạch chéo vào cuối đường dẫn.

## Leo thang đặc quyền theo chiều ngang
Tăng quyền truy cập theo chiều ngang xảy ra khi người dùng có thể truy cập vào tài nguyên thuộc về người dùng khác, thay vì chỉ truy cập vào tài nguyên của chính họ.
Các cuộc tấn công leo thang đặc quyền theo chiều ngang có thể sử dụng các phương pháp khai thác 
```http
https://insecure-website.com/myaccount?id=123
```
Kẻ tấn công có thể thay đổi id và có thể truy cập vào tài khoản của người khác.
> Trong một số ứng dụng, tham số có thể bị khai thác không có giá trị dự đoán được. Ví dụ, thay vì một số tăng dần, ứng dụng có thể sử dụng mã định danh duy nhất toàn cầu (GUID) để xác định người dùng. Điều này có thể ngăn kẻ tấn công đoán hoặc dự đoán mã định danh của người dùng khác. Tuy nhiên, các GUID thuộc về người dùng khác có thể bị tiết lộ ở những nơi khác trong ứng dụng nơi người dùng được tham chiếu, chẳng hạn như tin nhắn hoặc đánh giá của người dùng. <br>
> Trong một số trường hợp, ứng dụng có thể phát hiện khi người dùng không được phép truy cập tài nguyên và trả về trang chuyển hướng về trang đăng nhập. Tuy nhiên, phản hồi chứa thông tin chuyển hướng vẫn có thể bao gồm một số dữ liệu nhạy cảm thuộc về người dùng mục tiêu, do đó cuộc tấn công vẫn thành công. <br>

## Leo thang đặc quyền từ ngang sang dọc
Thông thường cộc tấn công leo thang dặc quyền theo chiều ngang có thể được chuyển thành chiều dọc bằng cách chiếm quyền kiểm soát người dùng có đặc quyền cao hơn.
Giả sử: Leo thang đặc quyền chiều ngang có thể cho phép kẻ tấn công đặt lại hoặc lấy được mật khẩu của người dùng khác. Nếu thì chúng có thể truy cập vào quản trị do đó thực hiện leo thang đặc quyền theo chiều dọc
## Tham chiếu đối tượng trực tiếp không an toàn
Lỗ hổng tham chiếu đối tượng trực tiếp không an toàn thường được gọi là (IDOR) là một loại lỗ hổng nhỏ hơn trong kiểm soát truy cập.
IDOR xảy ra khi một ứng dụng sử dụng dữ liệu do người dùng cung cấp để truy cập trực tiếp vào các đối tượng và kẻ tấn công có thể sửa đổi dữ liệu tùy ý.
## Các lỗ hổng kiểm soát truy cập trong quy trình nhiều bước
Nhiều trang web triển khai các chức năng quan trọng thông qua một chuỗi các bước. Điều này thường xảy ra khi:
> Cần thu thập nhiều thông tin đầu vào hoặc tùy chọn khác nhau. <br>
> Người dùng cần xem xét và xác nhận các chi tiết trước khi thực hiện thao tác <br>
Ví dụ, chức năng quản trị để cập nhật thông tin người dùng có thể bao gồm các bước sau:
> 1. Tải biểu mẫu chứa thông tin chi tiết của một người dùng cụ thể. <br>
> 2. Gửi các thay đổi <br>
> 3. Xem lại các thay đổi và xác nhận <br>

## Kiểm soát truy cập dựa trên nguồn giới thiệu
Một số trang web dựa vào thông tin `Referer` tiêu đề được gửi trong yêu cầu HTTP để thiết lập quyền truy cập. 
Trình `Referer` duyệt có thể thêm tiêu đề này vào các yêu cầu để chỉ ra trang nào đã khởi tạo yêu cầu.
Ví dụ, một ứng dụng thực thi kiểm soát truy cập mạnh mẽ đối với trang quản trị chính tại `admin`, nhưng đối với các trang con như `/admin/deleteUser` chỉ kiểm tra Referertiêu đề. Nếu Referertiêu đề chứa URL chính `/admin`, thì yêu cầu được cho phép.
## Cách ngăn ngừa lỗ hổng kiểm soát truy cập
Các lỗ hổng bảo mật trong kiểm soát truy cập có thể được ngăn chặn bằng cách áp dụng phương pháp phòng thủ nhiều lớp và tuân thủ các nguyên tắc sau:
> Không bao giờ nên chỉ dựa vào việc che giấu mã nguồn để kiểm soát truy cập <br>
> Trừ khi tài nguyên đó được thiết kế để công khai, hãy từ chối quyền truy cập theo mặc định <br>
> Nếu có thể, hãy sử dụng một cơ chế duy nhất áp dụng cho toàn bộ ứng dụng để thực thi kiểm soát truy cập. <br>
> Ở cấp độ mã nguồn, hãy bắt buộc các nhà phát triển phải khai báo quyền truy cập được cho phép đối với từng tài nguyên và từ chối quyền truy cập theo mặc định. <br>
> Kiểm tra và thử nghiệm kỹ lưỡng các biện pháp kiểm soát truy cập để đảm bảo chúng hoạt động đúng như thiết kế. <br>

## IDOR
### Lỗ hổng IDOR liên quan trực tiếp đến các đối tượng cơ sở dữ liệu
Hãy xem xét một trang web sử dụng URL sau để truy cập trang tài khoản khách hàng, bằng cách lấy thông tin từ cơ sở dữ liệu phía máy chủ:
```http
https://insecure-website.com/customer_account?customer_number=132355
```
kẻ tấn công có thể dễ dàng sửa đổi giá customer_number trị, vượt qua các biện pháp kiểm soát truy cập để xem hồ sơ của các khách hàng khác. Đây là một ví dụ về lỗ hổng IDOR dẫn đến leo thang đặc quyền theo chiều ngang.
### Lỗ hổng IDOR liên quan trực tiếp đến các tập tin tĩnh.
Lỗ hổng IDOR thường phát sinh khi các tài nguyên nhạy cảm được lưu trữ trong các tệp tĩnh trên hệ thống tệp phía máy chủ. Ví dụ, một trang web có thể lưu bản ghi tin nhắn trò chuyện vào ổ đĩa bằng tên tệp tăng dần và cho phép người dùng truy xuất chúng bằng cách truy cập URL như sau:
```http
https://insecure-website.com/static/12144.txt
```
kẻ tấn công có thể dễ dàng thay đổi tên tệp để lấy được bản ghi người dùng khác tạo ra và có khả năng thu thập thông tin để đăng nhập người dùng cũng như cá cduwx liệu nhạy cảm khác.
