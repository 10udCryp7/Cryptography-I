from Crypto.Cipher import AES
import hashlib
import random

keyword = random.choice('America')

KEY = hashlib.md5(keyword.encode()).digest()

print(KEY.hex())