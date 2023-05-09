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

if __name__ == "__main__":
    client = ChatClient("localhost", 8888)
    while True:
        message = input("Enter message: ")
        client.send_message(message)
        if message == "exit":
            break
    client.close()
