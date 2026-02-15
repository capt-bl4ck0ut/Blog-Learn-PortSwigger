# Kĩ thuật khai thác SSRF mù với Shellshock
Việc chỉ đơn thuần xác định một lỗ hổng SSRF ẩn có thể kích hoạt các yêu cầu HTTP ngoài băng tần không tự nó đã cung cấp đường dẫn đến khả năng khai thác. <br>
Vì chúng ta không thể xem phản hồi từ yêu cầu phía máy chủ, nên hành vi này không thể được sử dụng để khám phá nội dung trên các hệ thống mà máy chủ ứng dụng có thể truy cập. <br>
Chúng ta có thể quét mù không gian địa chỉ IP nội bộ, gửi các payload được thiết kế phát hiện các lỗ hổng đã biết. Nếu các payload đó cũng sử dụng các kỹ thuật ngoài băng tần ẩn, thì bạn có thể phát hiện ra một lỗ hổng nghiêm trọng trên một máy chủ nội bộ chưa được vá lỗi.
