import pygame

from core.Characters.CharArchetypes.Assassin import Assassin as ass
from core.Characters.CharArchetypes.Mage import Mage as mag

from core.util import Colors as color
from core.elements.Button import Button as Button

from core.elements.Elements import Elements as elements

Player1 = ass(name="Zed")
Player2 = mag(name="Lux")



game_display = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)
##opens in full screen
##can be alt tabbed
##minimize?

element = elements(game_display)



WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

event = pygame.event.wait()
clock = pygame.time.Clock()

player1_attack = Button(text="attack", action=Player1.basic_attack, action_target=Player2)
fullscreen_toggle = Button(text="toggle fullscreen", action=pygame.display.set_mode, action_target=[800,800])


def loop_display_info():
    global WIDTH, HEIGHT
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h

    #button(fullscreen_toggle, WIDTH/5, HEIGHT/5)




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
    element.button(player1_attack, 200, 200)

    pass


def game_update():
    element.hpbar(Player1, WIDTH / 3 - Player1.get_hp_bar().get_max_length(),HEIGHT / 2)
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
