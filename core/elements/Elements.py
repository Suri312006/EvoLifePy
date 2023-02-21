import pygame
import core.util.Colors as color
from core.elements.Button import Button


class Elements():

    def __init__(self, display):
        self._game_display = display

    def render_text(self, message, x_cord=0, y_cord=0, font="arial", size=10, color=color.black(), center=True):
        font = pygame.sysfont.SysFont(font, size)

        text_surface = font.render(message, True, color)
        text_rectangle = text_surface.get_rect()

        if center:
            text_rectangle.center = (x_cord, y_cord)

        self._game_display.blit(text_surface, text_rectangle)

        pygame.display.update()

    def hp_bar(self, player, x_cord, y_cord, ):
        length = player.char.get_hp_bar().get_max_length()
        height = player.char.get_hp_bar().hp_bar_height

        hp_bar_le = player.char.get_hp_bar().get_current_length()
        hp_color = player.char.get_hp_bar().get_color()
        offset = player.char.get_hp_bar().offset


        # background rect
        pygame.draw.rect(self._game_display, color=color.gray(),
                         rect=(x_cord, y_cord, length, height))
        # fill-in rect
        pygame.draw.rect(self._game_display, color=color.white(),
                         rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
        # actual changing rect
        pygame.draw.rect(self._game_display, color=hp_color,
                         rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
        pygame.display.update()


    def char_status(self,player,x_cord,y_cord):
        char = player.char

        length = player.char.get_hp_bar().get_max_length()
        height = player.char.get_hp_bar().hp_bar_height

        hp_bar_le = player.char.get_hp_bar().get_current_length()
        hp_color = player.char.get_hp_bar().get_color()
        offset = player.char.get_hp_bar().offset

        pygame.draw.rect(self._game_display, color=color.gray(),
                         rect=(x_cord , y_cord, length * 5, height * 3))


        # background rect
        pygame.draw.rect(self._game_display, color=color.gray(),
                         rect=(x_cord, y_cord, length, height))
        # fill-in rect
        pygame.draw.rect(self._game_display, color=color.white(),
                         rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset))
        # actual changing rect
        pygame.draw.rect(self._game_display, color=hp_color,
                         rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset))
        pygame.display.update()



    def button(self, butt, x_cord=0, y_cord=0):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x_cord + butt.width > mouse[0] > x_cord and \
                y_cord + butt.height > mouse[1] > y_cord:
            pygame.draw.rect(self._game_display, butt.active_color,
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
            pygame.draw.rect(self._game_display, butt.inactive_color,
                             (x_cord, y_cord, butt.width, butt.height))

        self.render_text(butt.text, x_cord + butt.width / 2, y_cord + butt.height / 2, butt.font, butt.text_size,
                         butt.text_color)

    def character(self, char_img, char_img_x=1000, char_img_y=1000, x_cord=0, y_cord=0):

        scaled_img = pygame.transform.scale(char_img, (char_img_x, char_img_y))

        self._game_display.blit(scaled_img, (x_cord, y_cord))
        pygame.display.update()
