cipher = 'cixd{05655105yz79321bzz38b7456c028bc1}'

# caesar may be

ct = 'flag{05655105bc79321ecc38e7456f028ef1}'

print(int('05655105bc79321ecc38e7456f028ef1', 16))
from Crypto.Util.number import long_to_bytes

string = '05655105bc79321ecc38e7456f028ef1'

string_rev = string[1:-1:2]
print(long_to_bytes(int(string_rev, 16)))

print(len(ct))