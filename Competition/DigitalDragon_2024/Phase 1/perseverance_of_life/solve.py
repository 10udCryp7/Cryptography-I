from Crypto.Cipher import DES
from base64 import *

ciphertext = b64decode('XieqPMvg9A+LxlkvQvGh2z/ooR9oom/Qrk8XnF4f8OgU5Aym3oUDAaREtZKYPK1aKfCpULVCE2831zhbslzuAtyrzvPf8ruYFsy2rn0PHTo=')

KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
a = DES.new(KEY, DES.MODE_ECB)

import itertools

# Độ dài của khóa (ví dụ: 8 byte)
key_length = 8

# Hàm để brute-force từ khóa nhỏ nhất đến lớn nhất

def brute_force_keys(length):
    # Sinh tất cả các tổ hợp khóa có độ dài `length`
    for key in itertools.product(range(256), repeat=length):
        # Chuyển từng tổ hợp thành dạng byte
        yield bytes(key)
count = 0
for key in brute_force_keys(length=8):
    print(count, end = "\r", flush=True)
    count += 1
    a = DES.new(key, DES.MODE_ECB)
    try: 
        plaintext = a.decrypt(ciphertext).decode('utf-8')
    except:
        continue
    print("in", end = '\r', flush=True)
    if plaintext.startswith('flag'):
        print(plaintext)
        break