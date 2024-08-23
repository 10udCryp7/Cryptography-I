import base64
hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
byte_string = bytes.fromhex(hex_string)

res = byte_string.decode('utf8')

print(res)


