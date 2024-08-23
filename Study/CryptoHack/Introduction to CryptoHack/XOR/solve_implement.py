text = 'label'

res = ""
for c in text:
    res += chr(ord(c) ^ 13)

print(res)