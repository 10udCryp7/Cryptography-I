from pwn import xor

# Tư tưởng bài này là ta biết trước đầu của plain_text là 'crypto{'
# Ta thực hiện xor cipher với 'crypto{' để tìm key
# Ta thấy được key có thể là myXORkey
# Ta xor cipher với myXORkey
cipher_text = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

cipher_text_bytes = bytes.fromhex(cipher_text)

key = xor(cipher_text_bytes, 'crypto{') #myXORkey

plain_text = xor('myXORkey', cipher_text_bytes).decode('utf-8')

print(plain_text)

