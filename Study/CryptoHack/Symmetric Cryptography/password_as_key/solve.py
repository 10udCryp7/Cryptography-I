from Crypto.Cipher import AES
import hashlib
import random

"""
Cryptohack - Passwords as keys
Solution using the requests Python module
Ref:
    https://docs.python-requests.org/en/master/user/quickstart
"""

import requests

BASE_URL = "https://aes.cryptohack.org/passwords_as_keys/"


# get the word list
r = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
content = r.text

wordlist = content.splitlines()
print(wordlist[-1])
print(len(wordlist))
# get the ciphertext of the encrypted flag
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print(f"{ciphertext = }")

# brute force
def online_attack(ciphertext, key):
    route = f'https://aes.cryptohack.org/passwords_as_keys/decrypt/{ciphertext}/{key}/'
    r = requests.get(route)
    data = r.json()
    plaintext = data['plaintext']

def local_attack(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    

    cipher = AES.new(key, AES.MODE_ECB)
    
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.hex()

count = 0
for word in wordlist:
    print(count, end="\r", flush=True)
    count += 1
    key = hashlib.md5(word.encode()).digest()
    attack = local_attack(ciphertext=ciphertext, key=key)
    try:
        plaintext = bytes.fromhex(attack).decode('utf-8')
        print(plaintext)
        break
    except:
        continue
    # try:
    #     flag = bytes.fromhex(plaintext).decode('utf-8')  
    #     print(flag)
    #     break
    # except:
    #     continue