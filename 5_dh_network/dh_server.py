from fa_python_network.threaded_server import ThreadedServer

class DHServer(ThreadedServer):
    pass

if __name__ == "__main__":
    try:
        server = DHServer("localhost", 9080)
        server.run()
    finally:
        server.stop()