# Writeup Lab: Limit overrun race conditions
![alt text](./HinhAnh/image.png) 
## Goal
Mục tiêu LAB này cần Race Condition xung đột truy cập đồng thời cho phép mua <b>Áo khoác da Lightweight L33t</b>
## Khai THác
Đầu tien vào challenge chúng ta cùng truy cập cred `wiener:peter` ở đây tài khoản chúng ta có được `50$` và code giảm giá `PROMO20`
![alt text](./HinhAnh/image-1.png)
Tiến hành đặt hàng áo khoác da Lightweight L33t thì với giá tiền của chúng ta chúng ta không thể mua được mặt hàng này.
![alt text](./HinhAnh/image-2.png)
Vậy với cách nào chúng ta có thể mua cái áo khoác này trong khi có 1 mã code giảm có `PROMO20` 20% vậy chúng ta có thể sử dụng gửi mã giảm giá vào cùng 1 lúc áp mã giảm giá thì điều gì sẽ xảy ra chúng ta cùng thực hiện ở Burp Suite
![alt text](./HinhAnh/image-3.png)
![alt text](./HinhAnh/image-5.png)
Và để khai thác tình trạng chạy đua tranh chấp vượt qua giới hạn này, trước tiên chúng ta gỡ bỏ mã giảm giá của chúng
![alt text](./HinhAnh/image-6.png)
![alt text](./HinhAnh/image-7.png)
Sau đó, gửi `/cart/coupon` yêu cầu POST đến Repeater của Burp Suite khoảng 30 lần:
![alt text](./HinhAnh/image-8.png)
Add vào Group và tiến hành gửi request đồng thời của các request sau đó xem phản ứng kết quả ra sao.
![alt text](./HinhAnh/image-9.png)
Kết quả số tiền đã được giảm hắn 1 lượng nhất định khi thực race condition gửi xung đột vào cùng 1 thời điểm
![alt text](./HinhAnh/image-10.png)
![alt text](./HinhAnh/image-11.png)