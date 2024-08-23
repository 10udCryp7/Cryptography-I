# plaintext ghép từ giá trị binary của từng kí tự trong FLAG, mỗi giá trị binary được thêm số 0 ở đầu cho đủ 8 kí tự

# lặp qua từng số trong plaintext:
    # tính n = pow(a,e,p) với e lấy ngẫu nhiên từ 1 đến p
    # nếu b = 1 thì đưa n vào cipher text, không thì đưa inverse + của n vào flag

from random import randint


path = 'Study\CryptoHack\Modular Arithmetic\Adrien_Sign\output.txt'
with open(path, 'r') as file:
    lines = file.readlines()
n_string = lines[0][1:-2].split(',')
n = []
for string in n_string:
    n.append(int(string.strip()))


a = 288260533169915
p = 1007621497415251

print(p % 4)

# Thử đánh giá xem a có phải là quadratic residue không
# Nếu có thì tức là pow(a,e,p) cũng là quadratic residue

def is_qr(a,p):
    if pow(a,(p-1)//2,p) == 1:
        return True
    return False

# print(is_qr(a,p))

# =>pow(a,e,p) cũng là quadratic residue

# p = 4k + 3
# pow(a,(p-1)//2,p) = pow(a, 2k + 1, p)
# số mũ luôn là số lẻ, nếu ta chứng minh được -a là non-qr thì win game
a_non = p - a
print(pow(a**3,2,p) == pow(a_non**3, 2, p)) #kiểm tra xem khi số mũ là chẵn thì có bằng nhau hay không
print(pow(a_non,15,p) == p-pow(a,15,p))

res = ''
for num in n:
    if (is_qr(num,p)):
        res += '1'
    else:
        res += '0'

flag = ''
for i in range(0,len(res),8):
    flag += chr(int(res[i:i+8],2))

print(flag)
