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

    def character(self, char_img, char_img_x=1000, char_img_y=1000, x_cord=0, y_cord=0):

        scaled_img = pygame.transform.scale(char_img, (char_img_x, char_img_y))

        self._game_display.blit(scaled_img, (x_cord, y_cord))
        pygame.display.update()
