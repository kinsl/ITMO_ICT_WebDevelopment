import socket
import threading


class ReceiveThread(threading.Thread):
    def __init__(self, client_sock: socket.socket):
        super().__init__()
        self.client_sock = client_sock
        self.server_closed = False

    def run(self) -> None:
        while not stop_threads and not self.server_closed:
            try:
                message = self.client_sock.recv(1024)
                if not message:
                    print(
                        "Сервер закрыл соединение! "
                        "Напишите любое сообщение или нажмите на Ctrl+C."
                    )
                    self.server_closed = True
                    break
                print(message.decode())
            except socket.timeout:
                continue


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))
client_socket.settimeout(0.5)

stop_threads = False
receiver = ReceiveThread(client_socket)
receiver.start()

try:
    while True:
        if receiver.server_closed:
            break
        try:
            message = input()
            client_socket.sendall(message.encode())
        except KeyboardInterrupt:
            print("Вы покинули чат!")
            break
except KeyboardInterrupt:
    print("Вы покинули чат!")
finally:
    stop_threads = True
    receiver.join()
    client_socket.close()
