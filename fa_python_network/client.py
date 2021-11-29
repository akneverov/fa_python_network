from random import randint
import socket


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))

    def closeSocket(self):
        self.sock.close()

    def connect(self, host, port):
        self.sock.connect((host, port))
        while True:
            msg = input("Enter message:")
            if not msg:
                break
            self.sock.send(msg.encode())

            data = self.sock.recv(1024).decode()
            print(data)

if __name__ == "__main__":
    try:
        client = Client("localhost", randint(2000, 10000))
        client.connect("localhost", 9080)
    finally:
        client.closeSocket()