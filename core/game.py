import time
import pygame
from pygame.locals import *

from CharTypes.Assasin import Assassin as ass
from CharTypes.Mage import Mage as mag
from CharTypes.Fighter import Fighter as fig
from CharTypes.Tank import Tank as tan

from core.util import Colors as color

Player1 = ass(name="Zed")
Player2 = mag(name="Lux")

WIDTH = 1000
HEIGHT = 800

game_display = pygame.display.set_mode([WIDTH, HEIGHT])
event = pygame.event.wait()
clock = pygame.time.Clock()


def du():
    pygame.display.update()


def init():
    pygame.init()
    pygame.display.set_caption("EvoLife")
    clock.tick(60)


def draw_env():
    game_display.fill(color.white())
    du()


def hpbar(player, x_cord, y_cord):
    length = player.get_hp_bar().get_max_length()
    height = player.get_hp_bar().hp_bar_height

    hp_bar_le = player.get_hp_bar().get_current_length()
    hp_color = player.get_hp_bar().get_color()
    offset = player.get_hp_bar().offset
    # background rect

    pygame.draw.rect(game_display, color=color.gray(), rect=(x_cord, y_cord, length, height))
    # fillin rect
    pygame.draw.rect(game_display, color=color.white(),
                     rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
    # actual changing rect
    pygame.draw.rect(game_display, color=hp_color,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
    du()

def prompt_playe1():
    move1name = Player1.get_move1()


def game_loop():

    pass


def game_update():
    hpbar(Player1, WIDTH/3 - Player1.get_hp_bar().get_max_length(), HEIGHT/2)
    hpbar(Player2, 2*WIDTH/3, HEIGHT/2)


def main():
    draw_env()
    print(Player1.health_report())
    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_loop()
        game_update()
        clock.tick(60)


if __name__ == '__main__':
    init()
    main()
