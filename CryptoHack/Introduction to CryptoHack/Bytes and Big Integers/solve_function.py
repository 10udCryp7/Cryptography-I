from Crypto.Util.number import long_to_bytes

cipher_text = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_text = long_to_bytes(cipher_text)

print(bytes_text.decode('utf-8'))


print(long_to_bytes(310400273487))