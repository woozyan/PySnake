import pygame
from minigame.constants import X_SIZE, Y_SIZE


class Board(object):
    def __init__(self):
        self.x = X_SIZE
        self.y = Y_SIZE

    def is_valid(self, x, y):
        return 0 <= x <= self.x and 0 <= y <= self.y


board = Board()
