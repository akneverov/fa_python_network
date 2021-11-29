import threading

from fa_python_network.server import Server

class ThreadedServer(Server):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.threads = []
        
    def run(self):
        while True:
            conn, addr = self.sock.accept()

            t = threading.Thread(target=self.handler, args=[conn, addr])
            self.threads.append(t)
            t.start()

    def stop(self):
        super().stop()
        self.closeThreads()

    def closeThreads(self):
        for t in self.threads:
            t.join()

if __name__ == "__main__":
    try:
        server = ThreadedServer("localhost", 9080)
        server.run()    
    finally:
        server.stop()