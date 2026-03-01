# JWT Attacker
Trong Module này chúng ta cần xem xét các vấn đề thiết kế việc xử lý sai sót các mã thông báo JWT dẫn đến hậu quả xảy ra nghiêm trọng. Bởi vì mã JWT liên quan đến các trường hợp xác thực tài khoản, .....
![alt text](image.png)
## JWT là gì?
Mã thông báo JWT Web JSON (JWT) là định dạng chuẩn để gửi dữ liệu JSON được ký mã hóa giưã các hệ thống. Thường dùng để xác thực thông tin người dùng.
Không giống như các mã thông báo phiên truyền thống. Tất cả dữ liệu máy chủ cần đều được lưu trữ ở phía máy khách trong chính JWT.
### Định dnajg JWT
Một JWT gồm 3 thành phần: phần tiêu đề, phần dữ liệu và phần chữ ký.
```token
eyJraWQiOiI5MTM2ZGRiMy1jYjBhLTRhMTktYTA3ZS1lYWRmNWE0NGM4YjUiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTY0ODAzNzE2NCwibmFtZSI6IkNhcmxvcyBNb250b3lhIiwic3ViIjoiY2FybG9zIiwicm9sZSI6ImJsb2dfYXV0aG9yIiwiZW1haWwiOiJjYXJsb3NAY2FybG9zLW1vbnRveWEubmV0IiwiaWF0IjoxNTE2MjM5MDIyfQ.SYZBPIBg2CRjXAJ8vCER0LA_ENjII1JakvNQoP-Hw6GG1zfl4JyngsZReIfqRvIAEi5L4HV0q7_9qGhQZvy9ZdxEJbwTxRs_6Lb-fZTDpW6lKYNdMyjw45_alSCZ1fypsMWz_2mTpQzil0lOtps5Ei_z7mM7M8gCwe_AGpI53JxduQOaB5HkT5gVrv9cKu9CsW5MS6ZbqYXpGyOG5ehoxqm8DL5tFYaW3lB50ELxi0KsuTKEbD0t5BCl0aCR2MBJWAbN-xeLwEenaqBiwPVvKixYleeDQiBEIylFdNNIMviKRgXiYuAvMziVPbwSgkZVHeEdF5MQP1Oe2Spac-6IfA
```
## Signal JWT
Máy chủ phát hành mã thông báo thường tạo chữ ký bằng cách băm phần tiêu đề và phần dữ liệu. Trong một số trường hợp, chúng cũng mã hóa kết quả băm. <br>
Dù quá trình nào  quá trình này đều liên quan đến một khóa bí mật. Cơ chế này cung cấp để máy chủ có thể xác minh rằng không bị giả mạo <br>
> Vì chữ ký được tạo ra trực tiếp từ phần còn lại của mã thông báo, viejecc thay đổi một bye duy nhất tỏng pahanf tiêu đề haowjc aphanaf dư xlieuej sẽ dẫn đến chữ ký không khớp <br>
> Nếu không biết khóa bí mật của máy chủ, sẽ không thể tạo ra chữ ký chính xác cho tiêu đề hoặc content bên trong <br>
## JWT so với JWK và JWE
![alt text](image-1.png)
## Tấn công JWT là gì?
Tấn công JWT liên quan đến việc người dùng gửi dữ liệu JWT đã được sửa đổi lên server nhằm để đạt được mục đích của chúng chẳng hạn như truy cập được tài nguyên mà cơ bản chúng không được phép.
## Khai thác lỗ hổng trong quá trình xác minh chữ ký JWT
Đôi khi máy chủ tạo ra một JWT nhưng mỗi token là hoàn toàn độc lập. Điều này có một số ưu điểm nhưng cũng tạo ra một vấn đề cơ bản - máy chủ thực sự không biết gì về nội dung gốc Token
```json
{
    "username": "carlos",
    "isAdmin": false
}
```
Nếu máy chủ xác định phiên dựa trên giá trị `username` này kẻ tấn công có thể thay đổi giá trị set `isAdmin: True` và ccos thể vào được leo thang đặc quyền.
## Chấp nhận chữ kí tùy ý
Các thư viện JWT thường cung cấp một phương thức để xác minh token và một phương thức khác chỉ để giải mã chúng. <br>
Ví dụ như thư viện Node.js `jsonwebToken` có `verify()` và `decode()`
Đôi khi nhà phát triển có thể nhầm lẫn 2 phương thức này chỉ chuyển các token đến `decode()` và không hề xác minh.
## Chấp nhận mã thông báo không cần chữ ký.
Trong một số trường hợp, phần tiêu đề của JWT chứa một `alg` cho biết sử dụng thuật toán nào để xác minh chữ ký.
```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```
JWT có thể được kí bằng nhiều thuật toán khác nhau. Trong trường hợp có thể thay thế `alg` thành `None` cho biết đó là jwt không bảo mật và có thể sửa đổi thông tin tùy ý mà không cần chữ ký.
## Tấn công vét cạn các khóa bí mật
Một số thuật toán ký điện tử, chẳng hạn như `HS256` (`HMAC + SHA-256`) sử dụng một chuỗi kí tự tùy ý độc lập làm khóa bí mật.
### Tấn công vét cạn khóa bí mật bằng Hashcat
```shell
hashcat -a 0 -m 16500 <jwt> <wordlist>
```
Hashcat ký phần tiêu đề và phần dữ liệu của JWT bằng cách sử dụng từng khóa bí mật trong danh sách từ, sau đó so sánh chữ ký thu được với chữ ký gốc từ máy chủ. Nếu bất kỳ chữ ký nào trùng khớp, Hashcat sẽ xuất ra khóa bí mật đã được xác định theo định dạng sau, cùng với nhiều chi tiết khác:
```shell
<jwt>:<identified-secret>
```
## Chèn tham số tiêu đề JWT
Theo đặc tả JWS, chỉ có `alg` tham số tiêu đề là bắt buộc. Tuy nhiên, trên thực tế, tiêu đề JWT (còn đượcc gọi là tiêu đề JOSE) thường chứa một tham số khác. <br>
> jwk (khóa Web JSON) - Cung cấp một đối tượng JSON được nhúng đại diện cho khóa <br>
> jku (URL bộ khóa web json): Cung cấp URL mà từ đó máy chủ có thể lấy một bộ khóa chứa khóa chính xác. <br>
> kid (Mã định danh khóa) - Cung cấp mã định danh mà máy chủ có thể sử dụng để xác định khóa chính xác trong trường hợp có nhiều khóa để lựa chọn. <br>

## Chèn JWT tự ký thông qua tham số JWK

