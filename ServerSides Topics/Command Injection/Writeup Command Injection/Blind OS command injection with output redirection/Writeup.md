# Writeup Lab: Blind OS command injection with output redirection
![alt text](image.png)
## Goal
Mục tiêu của LAB này chúng ta tìm cách chèn lệnh shell và ghi ra một thư mục sau đó truy cập để xem kết quả thực thi `whoami` hoàn thành LAB
## Khai thác
Đầu tien chúng ta truy cập Form Feed Back gửi một mẫu tùy ý và tiến hành submit:
![alt text](image-1.png)
Lịch sử HTTP Burp Suite cho thấy khi submit kết quả trả về bằng một chuỗi rỗng
![alt text](image-2.png)
Với như các lab trước chúng ta cũng thử chèn lệnh shell hệ điều hành nhưng không có gì xảy ra và cũng như mô tả LAB chúng ta tìm cách ghi ra thư mục để xem kết quả thực thi
Ở LAB này có thể sử dụng chuyển hướng đầu để thu thập kết quả có một thư mục để ghi là `/var/www/images` bằng cách đó chúng ta có thể chèn lệnh shell vào biểu mẫu để ghi ra thư mục đúng không
## POC
`xx|| whoami > /var/www/images/POC.txt ||` 
![alt text](image-3.png)
Sau đó chúng ta có thể vào mục filename hình ảnh để get `POC.txt` chúng ta vừa ghi ra thư mục
![alt text](image-4.png)
Tấn công chèn lệnh shell whoami thành công và hoàn thành LAB
![alt text](image-5.png)
