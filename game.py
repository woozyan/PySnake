import pygame
import random
from datetime import datetime, timedelta
from pysnake.constants import X_SIZE, Y_SIZE, CAPTION, WHITE_COLOR
from pysnake.snake import Snake
from pysnake.egg import Egg
from pysnake.utils import random_pos


class Game(object):
    def __init__(self, game_id, players):
        self.game_id = game_id
        self.start_time = datetime.utcnow()
        self.players = [player for player in players]
        self.snake_index = None

    def assign_roles(self):
        for player in self.players:
            player.set_role(Egg)
        self.snake_index = random.randint(0, len(self.players)-1)
        self.players[self.snake_index].set_role(Snake)

    def new_game(self, window):
        self.assign_roles()
        running = True
        for player in self.players:
            player(random_pos(X_SIZE, Y_SIZE))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.players[self.snake_index].move()
            if snake.eat_egg(egg):
                egg = Egg(random.randint(0, X_SIZE), random.randint(0, X_SIZE))
            egg.move()
            self.draw_window(window, snake, egg)

    def draw_window(self, window, snake, egg):
        window.fill(WHITE_COLOR)
        egg.draw(window)
        snake.draw(window)
        pygame.display.update()
