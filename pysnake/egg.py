import pygame
from pysnake.constants import BLOCK_SIZE, SCOPE_INIT_RADIUS, BLACK_COLOR, WHITE_COLOR, N_SPEED
from pysnake.board import board
from pysnake.error import EggHitsSnakeError
from pysnake.utils import min_dist, random_rgb


class Scope(object):
    def __init__(self, scope_size):
        self.radius = scope_size
        self.color = WHITE_COLOR

    def update_radius(self, radius):
        self.radius = radius

    def draw(self, window, egg):
        window.fill(BLACK_COLOR)
        pygame.draw.circle(window, self.color, (egg.x, egg.y), self.radius)


class Egg(object):

    def __init__(self, x, y, block_size=BLOCK_SIZE, n_speed=N_SPEED, scope_size=SCOPE_INIT_RADIUS):
        self.x = x
        self.y = y
        self.color = random_rgb()
        self.block_size = block_size
        self.n_speed = n_speed
        self.scope = Scope(scope_size)

    @property
    def speed(self):
        return self.n_speed * self.block_size

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
        if keys[pygame.K_w]:
            self.move_up()
        elif keys[pygame.K_s]:
            self.move_down()
        elif keys[pygame.K_a]:
            self.move_left()
        elif keys[pygame.K_d]:
            self.move_right()

    def draw(self, window, use_egg_scope=False):
        if use_egg_scope:
            self.scope.draw(window, self)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.block_size / 2)

    def hit_snake(self, snake):
        if min_dist(snake, self) < (self.block_size / 2 + snake.block_size / 2):
            return True
        else:
            return False

    def __repr__(self):
        return f"Egg({self.x}, {self.y})"
