import socket
from itertools import combinations
import os
import os

def clear_screen():
    os.system('clear')

# Ví dụ sử dụng

MAX_N = 100
SERVER_HOST = '34.134.101.136'
SERVER_PORT = 31809

def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_HOST, SERVER_PORT))
    return s

def receive_data(s):
    data = s.recv(999999999).decode()  # Adjust chunk size if needed
    return data

def send_data(s, message):
    s.sendall(message.encode())

def parse_challenge(data):
    lines = data.strip().split('\n')
    
    if len(lines) == 2:  
        lines_ans = lines[1].strip().split(' ')
    else:
        lines_ans = lines[2].strip().split(' ')
    arr = list(map(int, lines_ans[0:-1]))
    target_sum = int(lines_ans[-1])
    return arr, target_sum

# def find_indices(arr, target_sum):
#     n = len(arr)
#     for r in range(n + 1):
#         for indices in combinations(range(n), r):
#             if sum(arr[i] for i in indices) == target_sum:
#                 return indices
#     return []

def find_indices(set, n, sum):
    # Base Cases
    if sum == 0:
        return True, []
    if n == 0:
        return False, []

    # If last element is greater than sum, then ignore it
    if set[n - 1] > sum:
        return find_indices(set, n - 1, sum)

    # (a) Including the last element
    include, include_indices = find_indices(set, n - 1, sum - set[n - 1])
    if include:
        return True, include_indices + [n - 1]

    # (b) Excluding the last element
    exclude, exclude_indices = find_indices(set, n - 1, sum)
    if exclude:
        return True, exclude_indices

    return False, []


def main():
    s = connect_to_server()
    for stage in range(1, MAX_N + 1):
        clear_screen()
        print(f"Stage {stage}")
        
        data = receive_data(s)
        print(data)
        arr, target_sum = parse_challenge(data)
        check, indices = find_indices(arr,stage, target_sum)
        if not indices:
            print("Could not find correct indices")
            return
        
        answer = ' '.join(map(str, indices))
        send_data(s, answer + '\n')
        
    
    flag = receive_data(s)
    print(flag)

    s.close()

if __name__ == "__main__":
    main()
