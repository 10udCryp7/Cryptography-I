state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    cipher = []
    for i in range(4):
        row_cipher = []
        for j in range(4):
            row_cipher.append(state[i][j] ^ round_key[i][j])
        cipher.append(row_cipher)
    return cipher
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text = ''
    for row in matrix:
        for num in row:
            text += chr(num)
    return text

print(matrix2bytes(add_round_key(state, round_key)))

