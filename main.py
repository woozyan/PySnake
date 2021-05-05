import pygame
import time
import random
from pysnake.constants import X_SIZE, Y_SIZE, CAPTION, WHITE_COLOR
from pysnake.snake import Snake
from pysnake.egg import Egg
from pysnake.utils import random_pos


window = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption(CAPTION)


def draw_window(window, snake, egg):
    window.fill(WHITE_COLOR)
    egg.draw(window)
    snake.draw(window)
    pygame.display.update()


def main():
    running = True
    snake = Snake(250, 250, 20)
    egg = Egg(100, 100, 20, 0.5)
    start_time = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        snake.move()
        if egg.hit_snake(snake):
            snake.grow(egg)
            x, y = random_pos(egg.block_size, egg.block_size, X_SIZE - egg.block_size, Y_SIZE - egg.block_size)
            egg = Egg(x, y, block_size=egg.block_size, n_speed=1.1 * egg.n_speed)
        egg.move()
        draw_window(window, snake, egg)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
