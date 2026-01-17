# Writeup File path traversal, traversal sequences stripped non-recursively
![alt text](image.png)
## Goal 
Mục tiêu lab này tìm cách bypass để đọc tệp /etc/passwd
## Khai thác
Và ở đây tôi sẽ sử dụng burp suite để dễ dàng việc bypass nhưng khi thực hiện duyệt đường dẫn nhận được kết quả `"No such file"`
![alt text](image.png)
Và có lẽ hệ thống đã xóa `../` trong filename bằng cách chúng ta có thể double `../` lên giả sử như hệ thống xóa `../` khi double lên `....//` khi đó dường dẫn chúng ta vẫn hợp lệ là `../` và kết quả đọc được tệp và solve LAB
![alt text](image-1.png)