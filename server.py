import socket
import random
import pickle
from _thread import *
from minigame.snake import Snake
from minigame.egg import Egg
from minigame.constants import IP, PORT


server = IP
port = PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server Started! Waiting for new connections...")


players = [Snake(250, 250), Egg(100, 100)]


def threaded_client(conn, player):
    print(player)
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print(f"received {data}")
                print(f"replied {reply}")

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


if __name__ == "__main__":
    player_id = 0
    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)

        start_new_thread(threaded_client, (conn, player_id, ))
        player_id += 1
