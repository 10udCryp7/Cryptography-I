from Crypto.Util.number import * 
from sympy import nextprime

p1 = bin(getPrime(1024))[2:]
p2 = p1[:605]
p2 = p2 + ('0'*(len(p1)-len(p2)))

p1 = int(p1,2)
# p2 = nextprime(int(p2,2))
p2 = int(p2,2)
count = 0
while p1 != p2:
    p2 = nextprime(p2)
    count += 1

print(count)