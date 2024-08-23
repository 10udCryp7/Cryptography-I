response = {"ciphertext": "accc47a04049b2995a8bce94b7348c661029e0c228ea1f16dad536ba7aee0e9cbf02ee949d7326273b298a64726fefa8"}

'''
ciphertext = iv.hex() + encrypted.hex()
'''
import os

# iv.hex() has len 32
print(len(os.urandom(16).hex()))
ciphertext = response['ciphertext']

iv_hex = ciphertext[:32]
encrypted = ciphertext[32:]

assert ciphertext == iv_hex + encrypted

'''
encrypted có len hex = 64 -> len bytes = 32
encrypted = block_1 + block_2
block_2 = E(block_1 xor input_2)
block_1 = E(input_1 xor iv)

D_block_2 = block_1 xor input_2
D_block_1 = input_1 xor iv

D_block_2 xor block_1 = input_2
D_block_1 xor iv = input_1
'''

import requests
import string
base_url = 'https://aes.cryptohack.org/ecbcbcwtf/'
def send_request(ciphertext):
    r = requests.get(f'{base_url}/decrypt/{ciphertext}/')
    data = r.json()
    return data['plaintext']

iv_bytes = bytes.fromhex(iv_hex)

block_1 = encrypted[:32]
block_2 = encrypted[32:]

block_1_bytes = bytes.fromhex(block_1)
block_2_bytes = bytes.fromhex(block_2)

decrypted_block2_bytes = bytes.fromhex(send_request(block_2))
decrypted_block1_bytes = bytes.fromhex(send_request(block_1))

from Crypto.Util.strxor import strxor

input_2 = strxor(decrypted_block2_bytes, block_1_bytes)
input_1 = strxor(decrypted_block1_bytes, iv_bytes)

# input_2 = decrypted_block2_bytes ^ block_1_bytes
# input_1 = decrypted_block1_bytes ^ iv_bytes
flag = (input_1 + input_2).decode('utf-8')

print(flag)



