import pwn

text = 'label'

res = pwn.xor(text, 13).decode('utf-8')

print(res)
