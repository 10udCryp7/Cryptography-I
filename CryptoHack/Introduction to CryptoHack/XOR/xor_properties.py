from pwn import xor
import base64

# bài này cần convert từ hex_string sang bytes để thực hiện xor
# nếu giữ nguyên hex_string thì khi xor sẽ không ra kết quả đúng
# lí do là vì xor sẽ thực hiện trên từng byte của string
# nếu string là hex_string thì nó xor dựa trên từng ký tự của hex_string, không phải giá trị hex của nó
# bản chất các key và flag đều là hex, phải convert về giá trị dùng được, giá trị thực tế để xor
'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
'''

k1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k23 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
f_all = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

k1_bytes = bytes.fromhex(k1)
k23_bytes = bytes.fromhex(k23)
f_all_bytes = bytes.fromhex(f_all)
print(k1_bytes)
res = xor(k1_bytes, k23_bytes, f_all_bytes)
print(res.decode('utf-8'))