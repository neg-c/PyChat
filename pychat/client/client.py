import socket


class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_message(self, message):
        self.sock.sendall(message.encode("utf-8"))
        data = self.sock.recv(1024)
        print(f"Received from server: {data.decode('utf-8').strip()}")

    def close(self):
        self.sock.close()
