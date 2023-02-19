import time
import pygame
from pygame.locals import *
from CharTypes.Assasin import Assassin as ass
from CharTypes.Mage import Mage as mag
from CharTypes.Fighter import Fighter as fig
from CharTypes.Tank import Tank as tan

Player1 = ass(name="lol")
Player2 = fig(name="okay")

WIDTH = 1000
HEIGHT = 800

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

GREEN = (0, 255, 0)
LGREEN = (155, 255, 125)
YELLOW = (255, 255, 0)
LRED = (255, 155, 155)
RED = (255, 0, 0)

game_display = pygame.display.set_mode([WIDTH, HEIGHT])
event = pygame.event.wait()
clock = pygame.time.Clock()


def du():
    pygame.display.update()


def init():
    pygame.init()
    pygame.display.set_caption("A bit Racey")
    clock.tick(60)


def draw_env():
    game_display.fill(WHITE)
    du()


def hpbar(player, x_cord, y_cord):
    length = player.get_hp_bar().get_max_length()
    height = player.get_hp_bar().hp_bar_height

    hp_bar_le = player.get_hp_bar().get_current_length()
    hp_color = player.get_hp_bar().get_color()
    offset = player.get_hp_bar().offset
    # background rect

    pygame.draw.rect(game_display, color=GRAY, rect=(x_cord, y_cord, length, height))
    # fillin rect
    pygame.draw.rect(game_display, color=WHITE,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
    # actual changing rect
    pygame.draw.rect(game_display, color=hp_color,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
    du()


def game_loop():
    pass


def game_update():

    hpbar(Player1, 50, 50)



def main():
    draw_env()
    Player1.get_hit(70)
    print(Player1.health_report())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_loop()
        game_update()
        clock.tick(60)


if __name__ == '__main__':
    init()
    main()
