import socket
import pickle
from minigame.constants import IP, PORT, ONE_KB, ONE_MB


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IP
        self.port = PORT
        self.address = (self.server, self.port)
        self.character = self.connect()

    def get_character(self):
        return self.character

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(ONE_KB))
        except socket.error as e:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(ONE_KB))
        except socket.error as e:
            print(e)
