import pygame
from minigame.constants import SNAKE_INIT_LEN, BLACK_COLOR, BLOCK_SIZE


class SnakeNode(object):

    def __init__(self, x, y, parent):
        self.x = x
        self.x_prev = None
        self.y = y
        self.y_prev = None
        self.parent = parent
        self.next = None
        self.x_speed = 0
        self.y_speed = BLOCK_SIZE
        self.color = BLACK_COLOR

    def move(self):
        self.x_prev = self.x
        self.y_prev = self.y
        if self.parent is None:
            self.x += self.x_speed
            self.y += self.y_speed
        else:
            self.x = self.parent.x_prev
            self.y = self.parent.y_prev


class Snake(object):

    def __init__(self, x, y):
        self.head = SnakeNode(x, y, parent=None)
        self.tail = self.head
        self.build_snake(length=SNAKE_INIT_LEN)
        self.length = SNAKE_INIT_LEN

    def build_snake(self, length):
        parent = self.head
        x, y = parent.x, parent.y
        node = self.tail
        for i in range(1, length):
            node = SnakeNode(x, y-i*BLOCK_SIZE, parent)
            parent.next = node
            parent = node
        self.tail = node
        return

    def draw(self, window):
        node = self.head
        while node:
            pygame.draw.rect(window, node.color, (node.x, node.y, BLOCK_SIZE, BLOCK_SIZE))
            node = node.next
        return

    def move_down(self):
        head = self.head
        if head.y_speed != 0:
            return
        head.x_speed_prev = head.x_speed
        head.y_speed_prev = head.y_speed
        head.y_speed = abs(head.x_speed)
        head.x_speed = 0
        return

    def move_up(self):
        head = self.head
        if head.y_speed != 0:
            return
        head.x_speed_prev = head.x_speed
        head.y_speed_prev = head.y_speed
        head.y_speed = -1 * abs(head.x_speed)
        head.x_speed = 0
        return

    def move_right(self):
        head = self.head
        if head.x_speed != 0:
            return
        head.x_speed_prev = head.x_speed
        head.y_speed_prev = head.y_speed
        head.x_speed = abs(head.y_speed)
        head.y_speed = 0
        return

    def move_left(self):
        head = self.head
        if head.x_speed != 0:
            return
        head.x_speed_prev = head.x_speed
        head.y_speed_prev = head.y_speed
        head.x_speed = -1 * abs(head.y_speed)
        head.y_speed = 0
        return

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
        elif keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()

        node = self.head
        while node:
            node.move()
            node = node.next
