hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

byte_string = bytes.fromhex(hex_string)

def to_string(hex_string):
    res = ""
    for i in range(0,len(hex_string),2):
        res += chr(int(hex_string[i:i+2], base = 16))
    return res

#print(to_string(hex_string))

print(byte_string.decode("utf-8"))

print(to_string('7e6'))