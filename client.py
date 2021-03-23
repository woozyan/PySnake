import pygame
from network import Network
from minigame.egg import Egg
from minigame.constants import X_SIZE, Y_SIZE, CAPTION, WHITE_COLOR

width = X_SIZE
height = Y_SIZE
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(CAPTION)


def update_window(window, p1, p2):
    window.fill(WHITE_COLOR)
    if isinstance(p1, Egg):
        p1.draw(window, use_egg_scope=True)
        p2.draw(window)
    else:
        p1.draw(window)
        p2.draw(window, use_egg_scope=False)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_character()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        update_window(window, p, p2)


if __name__ == "__main__":
    main()
