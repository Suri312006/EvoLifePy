import pygame
from core.screens.game_screen import game_screen

game_display = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

game = game_screen(game_display, WIDTH, HEIGHT)

event = pygame.event.wait()
clock = pygame.time.Clock()


def init():
    pygame.init()
    pygame.display.set_caption("EvoLife")
    clock.tick(60)


def main():
    game.draw_env()
    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                quit()
        game.run()
        clock.tick(75)


if __name__ == '__main__':
    init()
    main()
