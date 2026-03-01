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
> jwk (Khóa WEB JSON): Cung cấp một đối tượng JSON được nhúng đại diện cho khóa <br>
> jku (URL bộ khóa WEB JSON): Cung cấp URL mà từ đó máy chủ có thể lấy một bộ khóa chứa khóa chính xác. <br>
> kid (Mã định danh khóa): Cung cấp mã định dạnh mà máy chủ ccos thể sử dụng để xác định khóa chính xác trong trường hợp có nhiều khóa lựa chọn. <br>
## Chèn JWT tự ký thông qua tham số jwk
```
Đặc tả JSON WEB Signature (JWS) mô tả tham số jwk tiêu đề tùy chọn, mà các máy chủ có thể sử dụng để nhúng khóa công khai của chúng trực tiếp vào bên trong mã thông báo ở định dạng JWK
```
```json
{
    "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
    "typ": "JWT",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
        "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
    }
}
```
Đôi khi các máy chủ được cấu hình sai và sử dụng bất kỳ khóa nào được nhúng trong tham số `jwk`. <br>
Có thể khai thác hành vi này bằng cách ký một JWT đã được sửa đổi bằng khóa riêng RSA riêng mình. Sau đó nhúng khóa công khai tương ứng vào `jwk` tiêu đề.
![alt text](image-3.png)
## Chèn JWT tự ký thông qua tham số jku
Thay vì nhúng trực tiếp khóa công khai bằng tham số `jwk` tiêu đề, một số máy chủ cho phép chúng ta sử dụng tham số tiêu đề `jku` (URL Bộ JWK) để tham chiếu đến một bọ JWK chứa khóa. Khi xác minh chữ ký, máy chủ sẽ lấy khóa liên quan dến URL này.
> Bộ JWK: JWK Set là một đối tượng JSON chứa một mảng các JWK đại diện cho các khóa khác nhau. <br>
```json
{
    "keys": [
        {
            "kty": "RSA",
            "e": "AQAB",
            "kid": "75d0ef47-af89-47a9-9061-7c02a610d5ab",
            "n": "o-yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9mk6GPM9gNN4Y_qTVX67WhsN3JvaFYw-fhvsWQ"
        },
        {
            "kty": "RSA",
            "e": "AQAB",
            "kid": "d8fDFo-fS9-faS14a9-ASf99sa-7c1Ad5abA",
            "n": "fc3f-yy1wpYmffgXBxhAUJzHql79gNNQ_cb33HocCuJolwDqmk6GPM4Y_qTVX67WhsN3JvaFYw-dfg6DH-asAScw"
        }
    ]
}
```
Các bộ JWK như thế đôi khi được công khai thông qua một điểm cuối tiêu chuẩn, chăng hjan như `./well-known/jwks.json`
## Chèn JWT tự ký thông qua tham số kid
Máy chủ có thể sử dụng nhiều khóa mã để ký các loại dữ liệu khác nhau, không chỉ riêng JWT. Vì lý do này, phần tiêu đề của JWT có thể chứa kid tham số (Key ID), giúp máy chủ xác định khóa nào cần sử dụng khi xác minh chữ ký
Nếu tham số này cũng dễ bị tấn công bằng phương pháp duyệt thư mục, kẻ tấn công có thể buộc máy chủ sử dụng một tệp bất kỳ trong hệ thống làm khóa xác minh.
```json
{
    "kid": "../../path/to/file",
    "typ": "JWT",
    "alg": "HS256",
    "k": "asGsADas3421-dfh9DGN-AFDFDbasfd8-anfjkvc"
}
```
Về mặt lý thuyết, bạn có thể làm điều này với bất kỳ tập tin nào, nhưng một trong những phương pháp đơn giản nhất là sử dụng `/dev/null` tập tin này, vốn có sẵn trên hầu hết các hệ thống Linux. 
## Cách phòng chống các cuộc tấn công JWT
![alt text](image-4.png)
![alt text](image-5.png)
## Tấn công gây nhầm lẫn thuật toán
Xem chi tiết . <a href="https://portswigger.net/web-security/jwt/algorithm-confusion">Tại đây</a>