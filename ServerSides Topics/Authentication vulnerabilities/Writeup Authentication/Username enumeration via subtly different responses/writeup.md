# Writeup LAB Liệt kê tên người dùng thông qua các phản hồi khác nhau một cách tinh tế
## Goal
Mục tiêu lab này tìm một tên người dùng hợp lệ, tấn công dò mật khẩu của người dùng đó bằng phương pháp vét cạn, sau đó truy cập vào trang tài khoản của họ.
## Khai thác
![alt text](./Hinh%20Anh/trangchu.png)
Chúng ta vào trang login và thử đăng nhập với một username password bất kì.
![alt text](./Hinh%20Anh/test.png)
Khi chung ta nhập sai tên người dùng, nó sẽ thông báo lỗi: `Invalid username or password.`
Tôi thử tấn công dò mật khẩu bằng đoạn mã Python để tìm kiếm username hợp lệ ở find `solve_find_username.py` thu được `Found user: adkit` tiếp theo thực hiện tấn công vét cạn tìm password của username: `adkit` ở file `solve_find_password` thu được `Found Password User adkit: yankees` tiến hành đăng nhập hoàn thành Lab
![alt text](./Hinh%20Anh/solve_lab.png)
