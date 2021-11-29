from random import randint
import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.bindSocket()

    def bindSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.sock.bind((self.host, self.port))
                break
            except OSError:
                self.port = randint(2000, 10000)

        self.sock.listen()
        print("Server started at {}:{}".format(self.host, self.port))

    def stop(self):
        self.closeSocket()

    def closeSocket(self):
        self.sock.close()

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            self.handler(conn, addr)

    def handler(self, conn, addr):
        print('Connected client', addr)
        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    print("Client disconnected", addr)
                    break

                print("Message from {} - {}".format(addr, data))
                conn.send(data.upper().encode())
        except ConnectionAbortedError:
            print("Lost connection with", addr)
        finally:
            conn.close()


if __name__ == "__main__":
    try:
        server = Server("localhost", 9080)
        server.run()
    finally:
        server.stop()