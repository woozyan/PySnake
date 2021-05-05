from pysnake.constants import X_SIZE, Y_SIZE, BLOCK_SIZE


class Board(object):
    def __init__(self):
        self.x = X_SIZE
        self.y = Y_SIZE

    def is_valid(self, x, y):
        return BLOCK_SIZE / 2 <= x < self.x - BLOCK_SIZE / 2 and BLOCK_SIZE / 2 < y < self.y - BLOCK_SIZE / 2


board = Board()
