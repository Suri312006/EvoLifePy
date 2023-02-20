import pygame

from core.Characters.CharArchetypes.Assassin import Assassin as ass
from core.Characters.CharArchetypes.Mage import Mage as mag

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
    pygame.draw.rect(game_display, color=color.gray(),
                     rect=(x_cord, y_cord, length, height))
    # fillin rect
    pygame.draw.rect(game_display, color=color.white(),
                     rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
    # actual changing rect
    pygame.draw.rect(game_display, color=hp_color,
                     rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
    du()


def render_text(message, x_cord=0, y_cord=0, font="arial", size=10, color=color.black()):
    font = pygame.sysfont.SysFont(font, size)

    text_surface = font.render(message, True, color)
    text_rectangle = text_surface.get_rect()

    text_rectangle.center = (x_cord, y_cord)
    game_display.blit(text_surface, text_rectangle)

    du()


clicked = False


def button(text="default", font='arial', text_size=10, text_color=color.black(), x_cord=0, y_cord=0, width=75,
           height=15, inactive_color=color.light_red(), active_color=color.red(), action=None, action_target=None):
    global clicked
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_cord + width > mouse[0] > x_cord and y_cord + height > mouse[1] > y_cord:
        pygame.draw.rect(game_display, active_color, (x_cord, y_cord, width, height))

        if not clicked:
            if click[0] == 1 and action is not None:
                action(action_target)
                clicked = True

        if click[0] == 0: clicked = False


    else:
        pygame.draw.rect(game_display, inactive_color, (x_cord, y_cord, width, height))

    font = pygame.sysfont.SysFont(font, text_size)

    text_surface = font.render(text, True, text_color)
    text_rectangle = text_surface.get_rect()

    text_rectangle.center = ((x_cord + (width / 2)), (y_cord + (height / 2)))
    game_display.blit(text_surface, text_rectangle)


def game_loop():
    button(text="attack", x_cord=500, y_cord=500, action=Player1.basic_attack, action_target=Player2)
    pass


def game_update():
    hpbar(Player1, WIDTH / 3 - Player1.get_hp_bar().get_max_length(), HEIGHT / 2)
    hpbar(Player2, 2 * WIDTH / 3, HEIGHT / 2)


def main():
    draw_env()
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
