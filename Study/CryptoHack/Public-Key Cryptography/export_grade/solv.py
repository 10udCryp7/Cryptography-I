from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv) 
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')




### SOLVE ###
iv = "be2dd4a34f00cdab3e47b42409425f9c"
ciphertext = "8d189d6921091be5a0d59cb37a76a325d2f78b10325b605718e6355cd9fc01d2"

p = "0xde26ab651b92a129"
g = "0x2"
A = "0xc723ac31206a942e"

B = "0xd863abf139e40d93"


p_int = int(p[2:], 16)
g_int = int(g[2:], 16)
A_int = int(A[2:],16)
B_int = int(B[2:],16)

print(f"{p_int = }")
print(f"{g_int = }")
print(f"{A_int = }")
print(f"{B_int = }")

# tìm a bằng tool https://www.alpertron.com.ar/DILOG.HTM
a = 7148301730902293734

print(A_int == pow(g_int, a, p_int))

shared_secret = pow(B_int, a, p_int)

print(decrypt_flag(shared_secret, iv, ciphertext))


