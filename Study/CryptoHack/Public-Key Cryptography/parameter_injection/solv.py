p = '0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff'
g = '0x02'
A = '0x4c1314a1f67dd76e92633109be15e898398c18e1a504e815cb9e7a6a0c29659f7a6fc9459a14112c6db4dc96b0d00c7087eb8ad5e112e34b968f74f0be6f2aa9e17cd8fca5b2f838386d784340eb42d432393410542666dbf890cbdad879a056fc57406cc62c34eaede381ad95714da6b717b9b89a19cfd4a4306888eb0285ef117a2a286fb3dcc14db54bc9f9f9c91ee37382d93745312780111596d073f48375f5c23712b4278dbe3977ea4012a824b2ec46a527d8b946fe25f624c9305f93'

from Crypto.Util.number import bytes_to_long

p_int = int(p[2:], 16)
g_int = int(g[2:], 16)
a_int = int(A[2:],16)

c = 1
C = pow(g_int, c, p_int)

B = "0xab569cf66b73a01986267f7f07a15d0f14454b65a92344b7fcf2cc02c043bce5c1b1fa0f599f9983d53518c228bc82665c5ad0f3907fc6ba6119fb5a6d19a95e89cc7d41ffd073898d7c5fd87df9b92dcdc4162a4b7bb21f820012e9196c45c465994b8e6f876df2345422d1fea00190421d7f80a078af17a75026006e2edaa6f48d283fee0162cd0fc6fa8a3990cc4604aff5436feac79f74c072ec3575272aa084200473112f2c32b798a7f9a3d5d069ff43a30cab403932446e4548a6f0a0"

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
iv = "a216ca9efa7925371c4f0c5fc65acb37"
ciphertext = "d3f169c664cf8fcb7eb67034e88f6be61639d6a8ba89894ef4e148ab3acd7409"

shared_secret = pow(a_int,c,p_int)

print(decrypt_flag(shared_secret, iv, ciphertext))

