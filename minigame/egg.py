import pygame
from minigame.constants import BLOCK_SIZE, SCOPE_INIT_RADIUS, RED_COLOR, BLACK_COLOR, WHITE_COLOR


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
        self.color = RED_COLOR
        self.scope = Scope()

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

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

    def draw(self, window):
        self.scope.draw(window, self)
        pygame.draw.circle(window, self.color, (self.x, self.y), BLOCK_SIZE // 2)
