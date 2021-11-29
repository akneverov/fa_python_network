from fa_python_network.threaded_server import ThreadedServer

class WebServer(ThreadedServer):
    pass

if __name__ == "__main__":
    try:
        webserver = WebServer("localhost", 9080)
        webserver.run()
    finally:
        webserver.stop()