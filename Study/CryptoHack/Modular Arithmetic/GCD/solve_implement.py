a = 66528
b = 52920

def gcd(a : int,b : int):
    res = -1
    is_negative = False
    if (a < 0 and b >= 0) or (b < 0 and a >= 0):
        is_negative = True
    if (a < 0):
        a = -a
    if (b < 0):
        b = - b
    x = a
    y = b
    while (x!=0 and y!=0):
        if (x > y):
            x = x%y
        else:
            y = y%x
    if (x == 0):
        res = y
    else:
        res = x
    if (is_negative == True):
        res = -res
    return res

print(gcd(a,b))
