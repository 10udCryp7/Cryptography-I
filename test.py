# for j in range(0,126):
#     print(j^0x7f,end=" ")
#     print(127-j)

#all elements equal 127 - j      res[j] (0->43 (44gtri))  = for i (arr[i] * mypow(j+2, 42-i)  )

# print(0x348A627D10659)
import numpy as np

def my_pow(param_1, param_2):
    if param_2 == 0:
        return 1
    elif param_2 == 1:
        return param_1
    elif (param_2 & 1) == 0:
        return my_pow(param_1 * param_1, param_2 >> 1)
    else:
        lVar1 = my_pow(param_1 * param_1, (param_2 - 1) >> 1)
        return lVar1 * param_1
# Ví dụ hệ phương trình
# Ax = b
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2],
    [1, 2, 1]
])

# b = np.array([8, -11, -3, 10])

# # Sử dụng phương pháp Least Squares
# x, residuals, rank, s = np.linalg.inv(A, b, rcond=None)

# print("Nghiệm của hệ phương trình là: ")
# print(x)

ar = []
for j in range(2,46): ## 2->45
    arr = []
    for i in range(0,43): ## 0->42
        arr.append(my_pow(j,42-i))
    ar.append(arr)
A = np.array(ar)
print(f"{A = }")
print(f"{A.shape = }")
b = np.array([0x348A627D10659, 0x27485A840365FE61, 0x9E735DADF26D31CD,
              0x0EB801D915A30D3D, 0x3DFB7CC801D16BC9, 0x602A04EFE5DAD659,
              0x82714BC9F9B579D9, 0x217DBE10EDCB20A1, 0x0ADEE2637E875CA19,
              0x0CD44AED238E9871, 0x0D3BFF76AE6B504D, 0x7181426EFF59E789,
              0x477616CB20C2DAC9, 0x0CE1206E1E46CE4A9, 0x946E7CB964A3F87D,
              0x499607CBF0C3291, 0x6871D4372347C759, 0x75412F56B7D8B01,
              0x0F8E57C264786E34D, 0x194CA6020EC505B9, 0x3E1A22E34FE84949,
              0x0A46DE25172742B79, 0x0CD0E971BCBFE6E3D, 0x56561961138A2501,
              0x78D2B538AB53CA19, 0x0A9980CA75AB6D611, 0x5F81576B5D4716CD,
              0x17B9860825B93469, 0x0C012F75269298349, 0x17373EE9C7A3AAC9,
              0x0B2E50798B11E1A7D, 0x0ADA5A6562E0FD7F1, 0x0EC3D9A68F1C99E59,
              0x3D828B35505D79A1, 0x0F76E5264F7BD16CD, 0x0DD230B3EC48ED399,
              0x80D93363DCD354C9, 0x7031567681E76299, 0x8977338CD4E2A93D,
              0x8A5708A1D4C02B61, 0x2066296A21501019, 0x9E260D94A4D775B1,
              0x0E7667BBD72280F4D, 0x12DF4035E1684349])
A = A.astype(float)
b = b.astype(float)
print(f"{A =}")
A_inv = np.linalg.inv(A[:43,:])
print(f"{b = }")




