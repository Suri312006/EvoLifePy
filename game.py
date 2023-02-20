import pygame

from core.Characters.CharArchetypes.Assassin import Assassin as ass
from core.Characters.CharArchetypes.Mage import Mage as mag

from core.util import Colors as color
from core.elements.Button import Button as Button

Player1 = ass(name="Zed")
Player2 = mag(name="Lux")

game_display = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)
##opens in full screen
##can be alt tabbed
##minimize?





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


def render_text(message, x_cord=0, y_cord=0, font="arial", size=10, color=color.black(), center=True):
    font = pygame.sysfont.SysFont(font, size)

    text_surface = font.render(message, True, color)
    text_rectangle = text_surface.get_rect()

    if center:
        text_rectangle.center = (x_cord, y_cord)

    game_display.blit(text_surface, text_rectangle)

    du()


def hpbar(player, x_cord, y_cord,):
    length = player.get_hp_bar().get_max_length()
    height = player.get_hp_bar().hp_bar_height

    hp_bar_le = player.get_hp_bar().get_current_length()
    hp_color = player.get_hp_bar().get_color()
    offset = player.get_hp_bar().offset

    # background rect
    pygame.draw.rect(game_display, color=color.gray(),
                     rect=(x_cord, y_cord, length, height))
    # fillin rect
    pygame.draw.rect(game_display, color=color.white(),
                     rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
    # actual changing rect
    pygame.draw.rect(game_display, color=hp_color,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
    du()


def button(butt, x_cord=0, y_cord=0):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_cord + butt.width > mouse[0] > x_cord and \
            y_cord + butt.height > mouse[1] > y_cord:
        pygame.draw.rect(game_display, butt.active_color,
                         (x_cord, y_cord, butt.width, butt.height))

        if not butt.clicked:
            if click[0] == 1 and butt.action is not None and butt.action_target is not None:
                butt.action(butt.action_target)
            if click[0] == 1 and butt.action is not None and butt.action_target is None:
                butt.action()
            butt.clicked = True

        if click[0] == 0:
            butt.clicked = False

    else:
        pygame.draw.rect(game_display, butt.inactive_color,
                         (x_cord, y_cord, butt.width, butt.height))

    render_text(butt.text, x_cord + butt.width / 2, y_cord + butt.height / 2, butt.font, butt.text_size,
                butt.text_color)


def game_loop():
    button(player1_attack, 200, 200)

    pass


def game_update():
    hpbar(Player1, WIDTH / 3 - Player1.get_hp_bar().get_max_length(),HEIGHT / 2, )
    hpbar(Player2, 2 * WIDTH / 3, HEIGHT / 2)



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
