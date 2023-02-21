import pygame

from core.Characters.playablecharacters.Assassins.MutantRaven import MutantRaven
from core.Characters.playablecharacters.Assassins.MutantSpider import MutantSpider

from core.Characters.playablecharacters.Fighters.BeeWeasel import BeeWeasel
from core.Characters.playablecharacters.Fighters.SharkDoggy import SharkDoggy

from core.Characters.playablecharacters.Mages.MushRoon import MushRoon
from core.Characters.playablecharacters.Mages.AngryPlant import AngryPlant
from core.Characters.playablecharacters.Mages.ForestSpirit import ForestSpirit

from core.Characters.playablecharacters.Tanks.RolyPoly import RolyPoly
from core.Characters.playablecharacters.Tanks.TortiCat import TortiCat

from core.elements.Button import Button as Button
from core.elements.Elements import Elements as elements
from core.util import Colors as color
import core.util.References as image

from core.Player import Player

game_display = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

fullscreen_toggle = Button(text="toggle fullscreen", action=pygame.display.set_mode, action_target=[800, 800])

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

event = pygame.event.wait()
clock = pygame.time.Clock()
element = elements(game_display)

Player1 = Player(image.suri(), MutantRaven)
Player2 = Player(image.naila(), MutantRaven)

Player1.set_enemy(Player2)
Player2.set_enemy(Player1)

Player1_moves = [Player1.get_button1(),
                 Player1.get_button2(),
                 Player1.get_button3(),
                 Player1.get_button4()]

Player2_moves = [Player2.get_button1(),
                 Player2.get_button2(),
                 Player2.get_button3(),
                 Player2.get_button4()]


def loop_display_info():
    global WIDTH, HEIGHT
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h
    print(Player2.char.get_health())

    # button(fullscreen_toggle, WIDTH/5, HEIGHT/5)


def du():
    pygame.display.update()


def init():
    pygame.init()
    pygame.display.set_caption("EvoLife")
    clock.tick(60)


def draw_env():
    game_display.fill(color.white())
    element.character(Player1.get_char_img(), x_cord=10, y_cord=15)
    du()


def game_loop():
    element.button(Player1_moves[0], 200, 600)


def game_update():
    element.hpbar(Player1, WIDTH / 3 - Player1.get_char_hp_bar().get_max_length(), HEIGHT / 2)
    element.hpbar(Player2, 2 * WIDTH / 3, HEIGHT / 2)


def main():
    draw_env()
    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                quit()
        loop_display_info()
        game_loop()
        game_update()
        clock.tick(75)


if __name__ == '__main__':
    init()
    main()
