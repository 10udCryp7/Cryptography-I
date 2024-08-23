from pwn import xor

cipher_text = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

# convert to bytes
cipher_text_hex = bytes.fromhex(cipher_text)

# Bài này đơn giản là xor với tất cả các trường hợp bytes có thể.
# Do 1 bytes có 8 bit, nên có 2^8 trường hợp từ 00000000 -> 11111111 hay 0 -> 255
for i in range(256):
    check = xor(cipher_text_hex, i).decode('utf-8')
    if check.startswith('crypto'):
        print(check)
        break