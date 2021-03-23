import pygame
from minigame.constants import SNAKE_INIT_LEN, BLACK_COLOR, BLOCK_SIZE, N_SPEED
from minigame.board import board
from minigame.error import SnakeHitsItselfError, SnakeHitsBoundaryError, SnakeSpeedZeroError
from minigame.utils import dist


class SnakeNode(object):

    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.next = None
        self.color = BLACK_COLOR

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


class SnakeHead(SnakeNode):
    def __init__(self, x, y):
        super().__init__(x, y, None)
        self.x_speed = 0
        self.y_speed = 0
        self.color = BLACK_COLOR

    def init_speed(self, n_speed):
        self.y_speed = n_speed

    def set_speed(self, new_speed):
        if new_speed == 0:
            raise SnakeSpeedZeroError()
        if self.x_speed:
            self.x_speed = abs(new_speed) if self.x_speed > 0 else -1 * abs(new_speed)
        if self.y_speed:
            self.y_speed = abs(new_speed) if self.y_speed > 0 else -1 * abs(new_speed)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, 1.1 * BLOCK_SIZE, 1.1 * BLOCK_SIZE))


class Snake(object):

    def __init__(self, x, y):
        self.head = SnakeHead(x, y)
        self.tail = self.head
        self.init_snake(length=SNAKE_INIT_LEN)
        self.length = SNAKE_INIT_LEN

    def init_snake(self, length):
        parent = self.head
        x, y = parent.x, parent.y
        node = self.tail
        for i in range(1, length):
            node = SnakeNode(x, y - i * BLOCK_SIZE, parent)
            parent.next = node
            parent = node
        self.tail = node
        return

    def draw(self, window):
        node = self.head
        while node:
            node.draw(window)
            node = node.next
        return

    def move_down(self):
        head = self.head
        if head.y_speed != 0:
            return
        head.y_speed = abs(head.x_speed)
        head.x_speed = 0
        return

    def move_up(self):
        head = self.head
        if head.y_speed != 0:
            return
        head.y_speed = -1 * abs(head.x_speed)
        head.x_speed = 0
        return

    def move_right(self):
        head = self.head
        if head.x_speed != 0:
            return
        head.x_speed = abs(head.y_speed)
        head.y_speed = 0
        return

    def move_left(self):
        head = self.head
        if head.x_speed != 0:
            return
        head.x_speed = -1 * abs(head.y_speed)
        head.y_speed = 0
        return

    def straight_snake(self):
        head = self.head
        head.x += head.x_speed * BLOCK_SIZE
        head.y += head.y_speed * BLOCK_SIZE
        node = self.head.next
        i = 1
        while i < self.length:
            if head.x_speed:
                node.x = head.x + i * BLOCK_SIZE if head.x_speed < 0 else head.x - i * BLOCK_SIZE
            else:
                node.x = head.x
            if head.y_speed:
                node.y = head.y + i * BLOCK_SIZE if head.y_speed < 0 else head.y - i * BLOCK_SIZE
            else:
                node.y = head.y
            node = node.next
            i += 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.init_speed(N_SPEED)
            return
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
        elif keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()

        head = self.head
        n_speed = abs(head.x_speed) or abs(head.y_speed)

        if self.length <= n_speed:
            self.straight_snake()
        else:
            node = self.tail
            count = 0
            while count < n_speed:
                node = node.parent
                count += 1
            tail = self.tail
            while node:
                tail.x = node.x
                tail.y = node.y
                node = node.parent
                tail = tail.parent
            head = self.head
            head.x += head.x_speed * BLOCK_SIZE
            head.y += head.y_speed * BLOCK_SIZE
            node = head.next
            i = 1
            while i < n_speed:
                if head.x_speed:
                    node.x = head.x + i * BLOCK_SIZE if head.x_speed < 0 else head.x - i * BLOCK_SIZE
                else:
                    node.x = head.x
                if head.y_speed:
                    node.y = head.y + i * BLOCK_SIZE if head.y_speed < 0 else head.y - i * BLOCK_SIZE
                else:
                    node.y = head.y
                node = node.next
                i += 1

        if self.hit_self():
            raise SnakeHitsItselfError()
        if self.hit_board():
            raise SnakeHitsBoundaryError()

    def hit_board(self):
        return not board.is_valid(self.head.x, self.head.y)

    def hit_self(self):
        visited = set()
        node = self.head
        while node:
            if (node.x, node.y) in visited:
                return True
            visited.add((node.x, node.y))
            node = node.next
        return False

    def eat_egg(self, egg):
        if dist(self, egg) > 1.5 * BLOCK_SIZE:
            return False
        tail = self.tail
        new_tail = SnakeNode(tail.x, tail.y, tail)
        tail.next = new_tail
        self.tail = new_tail
        self.length += 1
        return True

    def set_speed(self, n_speed):
        self.head.set_speed(n_speed)

    def init_speed(self, n_speed):
        self.head.init_speed(n_speed)

    def __repr__(self):
        body = []
        node = self.head
        while node:
            body.append((node.x, node.y))
            node = node.next
        return f"Snake({body})"
