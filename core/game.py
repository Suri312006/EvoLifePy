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


def healthbar(player, x_cord, y_cord, length=100, height=30, offset=10):
    max_hp = player.get_max_health()
    current_hp = player.health_report()[0]
    current_hp_percentage = player.health_report()[1]

    hp_color = GREEN
    if 60 < current_hp_percentage < 80:
        hp_color = LGREEN
    if 40 < current_hp_percentage < 60:
        hp_color = YELLOW
    if 20 < current_hp_percentage < 40:
        hp_color = LRED
    if 0 < current_hp_percentage < 20:
        hp_color = RED

    hp_bar_le = (current_hp_percentage / 100) * length

    # background rect
    pygame.draw.rect(game_display, color=GRAY, rect=(x_cord, y_cord, length, height))
    # fillin rect
    pygame.draw.rect(game_display, color=WHITE,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
    #actual changing rect
    pygame.draw.rect(game_display, color=hp_color,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
    du()


def main():
    draw_env()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        healthbar(Player1, 50, 50)
        clock.tick(60)


if __name__ == '__main__':
    init()
    main()

##healthbar ???
"""
need to create a health bar of some sort?
color changes with thingy

"""
