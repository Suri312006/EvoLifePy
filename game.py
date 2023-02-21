import pygame

from core.Characters.playablecharacters.Assassins.MutantRaven import MutantRaven
from core.Characters.CharArchetypes.Mage import Mage as mag

from core.util import Colors as color
from core.elements.Button import Button as Button
from core.Player import Player
import core.util.References as image
from core.elements.Elements import Elements as elements


Player1 = Player(image.suri(), MutantRaven)
Player2 = Player(image.naila(), MutantRaven)

game_display = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

element = elements(game_display)

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

event = pygame.event.wait()
clock = pygame.time.Clock()

fullscreen_toggle = Button(text="toggle fullscreen", action=pygame.display.set_mode, action_target=[800, 800])

#
# player1_move1 = Button(text=Player1.char.get_move1()[0], action=Player1.char.basic_attack, action_target=Player2.char,
#                         width=150, height=50, text_size=30)

player1_move1 = Player1.get_button1(Player2)

# player1_move3 = Button(text=Player1.get_move3()[0], action=Player1.move3, action_target=Player2, width=150, height=50,
#                         text_size=30)
# player1_move4 = Button(text=Player1.get_move4()[0], action=Player1.move4, action_target=Player2, width=150, height=50,
#                         text_size=30)

# player1_buttons = (, Player1.get_button2(), Player1.get_button3(), Player1.get_button4())


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
    du()


def game_loop():
    element.button(player1_move1, 200, 600)


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
        clock.tick(60)


if __name__ == '__main__':
    init()
    main()
