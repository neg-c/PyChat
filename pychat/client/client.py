import socket
from pychat.encryption.RSA import RSA

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_message(self, message):
        public_key, _ = RSA.generate_keypair()
        encrypted_message = RSA.encrypt(public_key, message)

        encrypted_message_hex = ' '.join(format(x, '02X').zfill(2) for x in encrypted_message)
        encrypted_message_bytes = encrypted_message_hex.encode('utf-8')
        self.sock.sendall(encrypted_message_bytes)

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
