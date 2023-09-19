import socket
import threading


class Client:
    def __init__(self, client_sock: socket.socket, address: tuple[str, int]):
        self.socket = client_sock
        self.address = address
        self.socket.settimeout(0.5)
        self.is_closed = False


class ClientThread(threading.Thread):
    def __init__(self, client: Client, client_lock: threading.Lock):
        super().__init__()
        self.client = client
        self.should_stop = threading.Event()
        self.client_lock = client_lock

    def run(self) -> None:
        self.broadcast("Присоединился к чату")

        while not self.should_stop.is_set():
            if self.client.is_closed:
                break
            try:
                message = self.client.socket.recv(1024).decode()
                if not message:
                    self.remove_client()
                    break
                else:
                    self.broadcast(message)
            except socket.timeout:
                pass
            except OSError:
                break
            except ConnectionResetError:
                self.remove_client()
                break

    def remove_client(self):
        self.client.is_closed = True
        self.broadcast("Покинул чат")
        self.client_lock.acquire()
        try:
            clients.remove(self.client)
        finally:
            self.client_lock.release()
        self.client.socket.close()
        self.should_stop.set()

    def broadcast(self, message: str) -> None:
        self.client_lock.acquire()
        try:
            other_clients = clients[:]
        finally:
            self.client_lock.release()
        for other_client in other_clients:
            if other_client != self.client:
                try:
                    other_client.socket.send(
                        f"{self.client.address[0]}:{self.client.address[1]} : "
                        f"{message}".encode()
                    )
                except socket.timeout:
                    pass


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(10)
server_socket.settimeout(0.5)

clients = []
client_lock = threading.Lock()

try:
    while True:
        try:
            client_sock, address = server_socket.accept()
            client = Client(client_sock, address)
            client_lock.acquire()
            try:
                clients.append(client)
            finally:
                client_lock.release()
            new_thread = ClientThread(client, client_lock)
            new_thread.start()

        except socket.timeout:
            pass

except KeyboardInterrupt:
    for client in clients:
        client.is_closed = True
        client.socket.close()
    server_socket.close()
