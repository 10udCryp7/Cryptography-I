import socket

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
server_address = ('0.cloud.chals.io', 33664)
client_socket.connect(server_address)

try:
    # Gửi dữ liệu lên server
    message = "Hello, Server!"  # Thay đổi thông điệp này nếu cần
    client_socket.sendall(message.encode())

    # Nhận phản hồi từ server (nếu có)
    response = client_socket.recv(1024)
    print('Phản hồi từ server:', response.decode())

finally:
    # Đóng kết nối
    client_socket.close()
