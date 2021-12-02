from random import randint

from fa_python_network.threaded_server import ThreadedServer
from dh import DH_Endpoint

class DHServer(ThreadedServer):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.public_key, self.private_key = (randint(1e3, 1e4) for _ in range(2))
        self.DH = DH_Endpoint(self.public_key, None, self.private_key)

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            self.exchangeKeys(conn)
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
                data = self.DH.decrypt_message(data)
                print("Decrypt message from {} - {}".format(addr, data))

                res = self.DH.encrypt_message(data.upper())
                print("Send message -", res)
                print()
                conn.send(res.encode())
        except ConnectionAbortedError:
            print("Lost connection with", addr)
        finally:
            conn.close()

    def exchangeKeys(self, conn):
        client_pub_key = int(conn.recv(1024))
        self.DH.public_key2 = client_pub_key
        conn.send(str(self.public_key).encode())

        partial_client_key = int(conn.recv(1024))
        conn.send(str(self.DH.generate_partial_key()).encode())

        self.full_key = self.DH.generate_full_key(partial_client_key)

if __name__ == "__main__":
    try:
        server = DHServer("localhost", 9080)
        server.run()
    finally:
        server.stop()