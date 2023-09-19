import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(10)
server_socket.settimeout(0.5)

try:
    while True:
        try:
            client_socket, address = server_socket.accept()
            client_socket.send(
                "Введите через запятую без пробелов значения a, b и c, "
                "где a и b - основания трапеции, а h - высота.".encode()
            )

            data = client_socket.recv(1024).decode()
            a, b, h = (float(num) for num in data.split(","))
            area = (a + b) / 2 * h

            client_socket.send(f"Площадь трапеции: {area}".encode())

        except socket.timeout:
            pass

except KeyboardInterrupt:
    server_socket.close()
