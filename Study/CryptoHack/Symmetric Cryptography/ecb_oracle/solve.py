import requests
import string
base_url = 'https://aes.cryptohack.org/ecb_oracle'
def send_request(plaintext):
    r = requests.get(f'{base_url}/encrypt/{plaintext}/')
    data = r.json()
    return data['ciphertext']

'''
for i in range(16):
    payload = 'a'*(i+1)
    payload_hex = payload.encode().hex()
    try:
        response = bytes.fromhex(send_request(payload_hex))
    except:
        continue
    if (len(response) == 48):
        print(i + 1) #7
        print(payload)
        break
'''

# hình dung nhé, tức là khi +7 giá trị thì chuyển qua block mới
# từ đó suy ra được độ dài flag là 16 + 16 - 7 = 25

# từ đây, ta cần gửi 'a'*31 -> 'a'*6 sẽ bóc được hết flag 
# nếu flag dài hơn, ta sẽ dùng payload k*16 lớn hơn độ dài flag, ví dụ bài này flag = 25 nên ta dùng payload với độ dài 32
flag = 'crypto'
alphabet = '{'+'_'+'@'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase
while (True):
    num = 32 - len(flag) - 1s
    payload = 'a'*num
    payload_hex = payload.encode().hex()
    response = bytes.fromhex(send_request(payload_hex))
    for char in alphabet:
        print(char, end = '\r', flush=True)
        payload_attack = 'a'*num + flag + char
        assert len(payload_attack) == 32
        payload_attack_hex = payload_attack.encode().hex()
        response_attack = bytes.fromhex(send_request(payload_attack_hex))
        if (response[:32] == response_attack[:32]):
            flag += char
            print(flag)
            break
    if (flag[-1] == '}'):
        break

print(flag)
    



