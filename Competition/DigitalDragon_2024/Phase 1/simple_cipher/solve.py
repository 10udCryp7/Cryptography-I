def create_matrix_from_string(s, height):
    length = len(s)
    width = (length + height - 1) // height  # Tính chiều rộng của ma trận dựa trên chiều cao

    matrix = []
    for i in range(height):
        start_index = i * width
        end_index = min(start_index + width, length)
        row = list(s[start_index:end_index])
        if len(row) < width:
            row.extend([' '] * (width - len(row)))  # Thêm khoảng trắng vào cuối dòng nếu cần
        matrix.append(row)
    
    return matrix

# Chuỗi và chiều cao mong muốn
s = "afle{d89gbf1e1693ac6abca8df52a53afb0d}"
height = 10  # Bạn có thể thay đổi giá trị này

matrix = create_matrix_from_string(s, height)

# Hiển thị ma trận
for row in matrix:
    print(' '.join(row))


flag1 = 'flag{d89ebf1e1693acab65a8dfc2a53afb0d}'

print(len(flag1))

string = 'helloworld'

print(string[::-1])