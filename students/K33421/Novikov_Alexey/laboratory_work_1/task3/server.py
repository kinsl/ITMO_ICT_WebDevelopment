import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(10)
server_socket.settimeout(0.5)

try:
    while True:
        try:
            client_socket, address = server_socket.accept()

            with open("index.html", encoding="utf-8") as f:
                index_html = f.read().encode()

            headers = (
                "HTTP/1.1 200 OK\n"
                "Content-Type: text/html\n"
                f"Content-Length: {len(index_html)}\n"
                "Connection: close\n\n"
            ).encode()

            client_socket.sendall(headers + index_html)

        except socket.timeout:
            pass

except KeyboardInterrupt:
    server_socket.close()
