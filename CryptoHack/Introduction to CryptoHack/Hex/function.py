import base64

print(hex(2022))
print(bin(2022))


print((2022).to_bytes(4))

print(int('7e6', base = 16))


use_hex = (2022).to_bytes(2).hex()
use_b16encode = base64.b16encode((2022).to_bytes(2))
print(f".hex: {use_hex}, type {type(use_hex)}")
print(f".b16encode: {use_b16encode}, type {type(use_b16encode)}")