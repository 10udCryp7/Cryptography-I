cipher_text = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
res = ""
while cipher_text > 0:
    # 0xff = 255 = 11111111 in binary, so it will take the last 8 bits of the number
    # xor each 8 bits with 11111111 to get the original message
    res = chr(cipher_text & 0xff) + res 
    # shift the number to the right by 8 bits to get the next 8 bits
    cipher_text >>= 8

print(res)