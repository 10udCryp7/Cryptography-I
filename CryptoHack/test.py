import base64

ques_hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

print(len(ques_hex))
ques = bytes.fromhex(ques_hex)
print(ques)

print(base64.b64encode(ques).decode('utf-8'))

