# WRiteup LAB: URL-based access control can be circumvented
![alt text](image.png)
## Goal
Mục tiêu LAB bằng cách vào được admin để xóa người dùng `carlos` hoàn thành LAB
## Khai thác
Khi vào trang chủ thấy ngay TAB admin không biết có gì đặc biệt chúng ta thử click vào
![alt text](image-1.png)
Nhưng thật không may khi Click vào thì ứng dụng nó không cho phép không có quyền truy cập hiện tại tôi đang phương thức GET
![alt text](image-2.png)
Giả sử nếu tôi chuyển đổi phương thức `POST /admin/delete?username=carlos` thì sao cùng thử xem và cũng không được
Và LAB này có đề cập đến framework có hỗ trợ tiêu đề `X-Original-URL` header bằng cách này chúng ta có thể ghi đè tiêu đề mà server chỉ kiểm tra phương thức mà không kiểm tra tiêu đề 
và bằng cách đó chúng ta có thể ghi đè `X-Original-Url: /admin/delete` và truyền tham số `username=carlos` với phương thức `POST` chúng ta có thể xóa user người dùng
![alt text](image-3.png)
