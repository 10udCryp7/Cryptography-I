p = 28151

phi_p = p - 1

factor_list = [2, 5, 5, 563]

# dùng trick:
# ta tìm các factor của phi_p = p - 1
# ta chỉ cần kiểm tra xem tất cả pow(g, phi_p/f, p) với f là 1 factor xem có khác 1 không
# có thì nó là primitive element
# nói rõ hơn là test pow(g,a*b,p) với a và b là 2 giá trị bất kì trong tập factor

# source: https://math.stackexchange.com/questions/598485/finding-a-primitive-element-of-a-finite-field


for g in range(2,p):
    if all(pow(g,phi_p//f, p) != 1 for f in factor_list):
        print(g)
        break
