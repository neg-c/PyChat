import socket
import threading


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.lock = threading.Lock()

    def handle_client(self, conn, addr):
        with self.lock:
            print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            with self.lock:
                print(f"Received from {addr}: {data.decode('utf-8').strip()}")
            conn.sendall(data)
        with self.lock:
            print(f"Disconnected from {addr}")
        conn.close()

    def listen_forever(self):
        while True:
            conn, addr = self.sock.accept()
            clientThread = threading.Thread(
                target=self.handle_client, args=(conn, addr)
            )
            clientThread.start()
