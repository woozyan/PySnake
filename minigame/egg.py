import pygame
from minigame.constants import BLOCK_SIZE, SCOPE_INIT_RADIUS, GREEN_COLOR, BLACK_COLOR, WHITE_COLOR
from minigame.board import board
from minigame.error import EggHitsSnakeError
from minigame.utils import min_dist


class Scope(object):
    def __init__(self):
        self.radius = SCOPE_INIT_RADIUS
        self.color = WHITE_COLOR

    def update_radius(self, radius):
        self.radius = radius

    def draw(self, window, egg):
        window.fill(BLACK_COLOR)
        pygame.draw.circle(window, self.color, (egg.x, egg.y), self.radius)


class Egg(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = BLOCK_SIZE
        self.color = GREEN_COLOR
        self.scope = Scope()

    def move_left(self):
        new_x = self.x - self.speed
        if board.is_valid(new_x, self.y):
            self.x = new_x

    def move_right(self):
        new_x = self.x + self.speed
        if board.is_valid(new_x, self.y):
            self.x = new_x

    def move_up(self):
        new_y = self.y - self.speed
        if board.is_valid(self.x, new_y):
            self.y = new_y

    def move_down(self):
        new_y = self.y + self.speed
        if board.is_valid(self.x, new_y):
            self.y = new_y

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

    def draw(self, window, use_egg_scope=False):
        if use_egg_scope:
            self.scope.draw(window, self)
        pygame.draw.circle(window, self.color, (self.x, self.y), BLOCK_SIZE / 2)

    def hit_snake(self, snake):
        if min_dist(snake, self) < BLOCK_SIZE:
            raise EggHitsSnakeError()

    def __repr__(self):
        return f"Egg({self.x}, {self.y})"
