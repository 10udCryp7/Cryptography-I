from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
import requests

# test expire
# for i in range(10):
#     print(int((datetime.today() + timedelta(days=1)).timestamp()))
    

base_url = 'https://aes.cryptohack.org/flipping_cookie/'
def send_request():
    r = requests.get(f'{base_url}/get_cookie/')
    data = r.json()
    return data['cookie']

time_start = int((datetime.today() + timedelta(days=1)).timestamp())

response = send_request()
print(len(response))
iv = response[:32]
cookie = response[32:]



