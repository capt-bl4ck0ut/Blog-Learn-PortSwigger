# Writeup LAB JWT authentication bypass via kid header path traversal
![alt text](./HinhAnh/image.png)
## Goal
To solve the lab, forge a JWT that gives you access to the admin panel at /admin, then delete the user carlos.
## Khai thác
Trang chủ
![alt text](./HinhAnh/image-1.png)
Đăng nhập với user wiener
![alt text](./HinhAnh/image-2.png)
Lịch sử Burp Suite 
![alt text](./HinhAnh/image-3.png)
Trong các bài thực hành trước, chúng ta đã thấy rằng cookie phiên sử dụng JWT (JSON Web Token) để quản lý phiên.
Thực hiện sao sao chép và dán chuỗi vào <a href="https://token.dev/">token.dev</a> một công cụ trực tuyển để giải mã token
![alt text](./HinhAnh/image-4.png)
Và chúng ta có thể thấy được header có tham số `kid` làm khóa định danh và ở thí nghiệm PortSwigger có nói đến:
> Nếu tham số này cũng dễ bị tấn công bằng phương pháp duyệt thư mục, kẻ tấn công có thể buộc máy chủ sử dụng một tệp bất kỳ từ hệ thống tệp của nó làm khóa xác minh. <br>
Và ở trong hệ thống này chúng ta có quyền thực hiện điều đó bằng cách sử dụng duyệt thư mục đường dẫn với `../../../../../../dev/null` mặc định trong Linux là thư mục rỗng chúng ta có thể kí khóa xác minh thành `AA==` được giải mã base64 là rỗng chúng ta cùng thực hiện ở file python <br>
Kết quả:
```txt
PS D:\Blog_Learn_PortSwigger\Advanced topics> & "D:\Tai Lieu Hoc Tap\IDE PyThon & PHP & Java\python.exe" "d:/Blog_Learn_PortSwigger/Advanced topics/JWT Attacker/Some Writeup JWT/JWT authentication bypass via kid header path traversal/sign.py"
eyJraWQiOiIuLi8uLi8uLi8uLi8uLi8uLi8uLi8uLi9kZXYvbnVsbCIsImFsZyI6IkhTMjU2IiwidHlwIjoiSldUIn0.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc3MjM3NzAxMywic3ViIjoiYWRtaW5pc3RyYXRvciJ9._vA3ukxxM-T_04wFAgVEBSh2eK2_zqa5r01TLcHMa_0
verified? True
```
Thực hiện dán token truy cập admin và lúc này đã vào được
![alt text](./HinhAnh/image-5.png)
Thực hiện xóa user carlos và hoàn thành LAB
![alt text](./HinhAnh/image-6.png)