import pygame
import core.util.Colors as color
#from core.elements.Button import Button


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
        length = player.char.get_char_status().get_max_length()
        height = player.char.get_char_status().bar_height

        hp_bar_le = player.char.get_char_status().get_current_length()
        hp_color = player.char.get_char_status().get_color()
        offset = player.char.get_char_status().offset

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

    def char_status(self, player, x_cord, y_cord):
        char = player.char

        length = player.char.get_char_status().get_max_length()
        height = player.char.get_char_status().bar_height

        hp_bar_le = player.char.get_char_status().get_current_length()
        hp_color = player.char.get_char_status().get_color()
        offset = player.char.get_char_status().offset

        pygame.draw.rect(self._game_display, color=color.off_white(),
                         rect=(x_cord, y_cord, length * 1, height * 3))

        pygame.draw.rect(self._game_display, color=color.gray(),
                         rect=(x_cord, y_cord, length, height), border_radius=15)
        # fill-in rect
        pygame.draw.rect(self._game_display, color=color.white(),
                         rect=(x_cord + offset / 2, y_cord + offset / 2, length - offset, height - offset),
                         border_radius=14)
        # actual changing rect

        if hp_bar_le >0:
            pygame.draw.rect(self._game_display, color=hp_color,
                         rect=(x_cord + offset / 2, y_cord + offset / 2, hp_bar_le - offset, height - offset), border_radius=15)

        # background rect
        pygame.display.update()


    def character(self, char_img, char_img_x=1000, char_img_y=1000, x_cord=0, y_cord=0):

        scaled_img = pygame.transform.scale(char_img, (char_img_x, char_img_y))

        self._game_display.blit(scaled_img, (x_cord, y_cord))
        pygame.display.update()
