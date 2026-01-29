# Writeup Lab: Web shell upload via Content-Type restriction bypass
![alt text](./HinhAnh/image.png)
## Goal
Mục tiêu cũng như các LAB trước tìm cách bypass đọc được tập tin `/home/carlos/secret`
## Khai thác
Đầu tiên chúng ta cùng đăng nhập với cred `wiener:peter` khi vào ứng dụng nó cũng có chức năng upload hình ảnh như sau chúng ta cùng tiến hành upload 1 hình ảnh
![alt text](./HinhAnh/image-1.png)
Vẫn như LAB cũ chúng ta giả sử hệ thống không lọc đầu vào có thể truyền lên tập tin mở rộng `.php` bất kì thử xem thì nó cũng không lọc đầu vào
![alt text](./HinhAnh/image-2.png)
Tới đây chúng ta có thể GET webshell và lấy mã bí mật
![alt text](./HinhAnh/image-3.png)
Nộp mã bí mật và hoàn thành LAB
![alt text](./HinhAnh/image5.png)

