import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto("Hello, server".encode(), ("127.0.0.1", 8080))
data, address = client_socket.recvfrom(1024)
print(f"Message: {data.decode()}")
