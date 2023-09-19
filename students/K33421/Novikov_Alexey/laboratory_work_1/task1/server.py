import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.settimeout(0.5)

try:
    while True:
        try:
            data, address = server_socket.recvfrom(1024)
            print(f"Message: {data.decode()}")
            server_socket.sendto("Hello, client".encode(), address)
        except socket.timeout:
            pass

except KeyboardInterrupt:
    server_socket.close()
