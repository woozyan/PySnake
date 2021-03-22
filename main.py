import pygame
import time
from minigame.constants import X_SIZE, Y_SIZE, CAPTION, WHITE_COLOR
from minigame.snake import Snake


window = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption(CAPTION)


def draw_window(window, snake):
    window.fill(WHITE_COLOR)
    snake.draw(window)
    pygame.display.update()


def main():
    running = True
    snake = Snake(50, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        snake.move()
        draw_window(window, snake)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
