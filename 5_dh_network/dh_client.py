from random import randint

from fa_python_network.client import Client


class DHClient(Client):
    pass

if __name__ == "__main__":
    try:
        client = DHClient("localhost", randint(2000, 10000))
        client.connect("localhost", 9080)
    finally:
        client.closeSocket()