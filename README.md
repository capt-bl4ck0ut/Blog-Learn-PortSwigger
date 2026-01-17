# Blog Learn PortSwigger của Tôi.
Repo này là nơi mình **ghi chú quá trình học Web Security** theo lộ trình của **PortSwigger Web Security Academy**.  
Mục tiêu: hệ thống hóa kiến thức, lưu lại các kỹ thuật khai thác cơ bản → nâng cao, và tổng hợp writeup cho từng lab.

---
## 🎯 Mục tiêu học tập
- Nắm vững các lỗ hổng web phổ biến và cách khai thác.
- Hiểu tư duy kiểm thử bảo mật (recon → exploit → validate → report).
- Ghi chú ngắn gọn, dễ tra cứu, có ví dụ payload và lưu ý quan trọng.
- Hoàn thành lab theo từng chủ đề và viết lại writeup theo cách của riêng mình.
---
## 📌 Nội dung repo
Repo được chia theo **chủ đề (Topic)** tương ứng với PortSwigger:
- **ServerSides Topics/**
  - **Authentication vulnerabilities/**
    - **Note Authentication/**: ghi chú lý thuyết + kỹ thuật + checklist
    - **Writeup Authentication/**: writeup theo từng lab
  - **SQL Injection/**: ghi chú + writeup cho SQLi (Part 1/2...)

> Mỗi chủ đề thường có:
- `Note ....` : ghi chú tổng quan, giải thích khái niệm, tips, checklist.
- `Writeup ...` : writeup chi tiết lab (mục tiêu, cách làm, payload, kết quả).
---
## 🧠 Cách mình ghi chú / làm lab
**Quy trình chung:**
1. Đọc lý thuyết và note lại PortSwigger theo topic
2. Làm lab (tập trung hiểu bản chất hơn là “copy payload”)
3. Tổng hợp lại:
   - Dấu hiệu nhận biết lỗ hổng
   - Các kỹ thuật bypass phổ biến
   - Payload mẫu
   - Các lỗi hay gặp
4. Viết writeup cho từng lab:
   - Mục tiêu lab
   - Phân tích request/response
   - Hướng khai thác
   - Kết quả cuối cùng + cách khắc phục
## 🧩 Cấu trúc writeup
Mỗi writeup lab mình sẽ cố gắng theo format:
- **Lab name**
- **Goal**
- **Key idea / Vulnerability**
- **Steps**
- **Payload**
- **Result**
- **Takeaways**
---
## 🛠️ Tools mình dùng
- Burp Suite (Proxy, Repeater, Intruder,...)
- Browser DevTools
- VS Code (Markdown notes)
---
## 📌 Lưu ý
- Writeup mang tính **học tập và nghiên cứu**, chỉ thực hành trên môi trường lab hợp pháp.
- Repo được cập nhật dần theo tiến độ học.
---
## 📬 Contact
Nếu bạn muốn trao đổi thêm về lab/notes:
- Email: `vanphuc23062005@gmail.com`
